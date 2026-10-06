# Threat Intelligence & Hunt Hypotheses

## Overview

**Cyber Threat Intelligence (CTI)** is the process of collecting, processing, analyzing, and applying information about threats, threat actors, campaigns, vulnerabilities, infrastructure, malware, and adversary behavior.

For threat hunters, intelligence is valuable because it provides the context needed to answer:

> **Who might target us, why would they target us, how would they attack us, and what evidence would they leave behind?**

Threat intelligence transforms threat hunting from an open-ended search into a focused investigation.

```text
Threat Intelligence
        ↓
Threat Understanding
        ↓
Threat Scenario
        ↓
Hunt Hypothesis
        ↓
Required Telemetry
        ↓
Hunt Query
        ↓
Investigation
        ↓
Detection Engineering
```

The objective is not simply to collect threat feeds.

The objective is to turn intelligence into **actionable defensive decisions**.

---

# 1. What Is Cyber Threat Intelligence?

Cyber Threat Intelligence is analyzed information about cyber threats that helps an organization make better security decisions.

It can describe:

- Threat actors
- Campaigns
- Malware
- Attack infrastructure
- Vulnerabilities
- Techniques
- Tactics
- Procedures
- Indicators
- Victimology
- Targeting patterns
- Adversary objectives

A raw indicator is not necessarily intelligence.

For example:

```text
IP Address:
203.0.113.50
```

is simply an indicator.

Adding context:

```text
203.0.113.50

Associated with:
- Threat Actor X
- Command-and-control infrastructure
- Campaign Y
- Observed targeting of financial organizations
- First observed: Date
- Last observed: Date
```

makes the information much more useful.

---

# 2. Intelligence vs Information vs Data

These terms are often confused.

## Data

Raw observations.

```text
IP: 203.0.113.50
```

## Information

Data with basic context.

```text
203.0.113.50
was observed communicating with
multiple compromised endpoints.
```

## Intelligence

Analyzed information that supports a decision.

```text
The IP is associated with infrastructure
used by a threat actor targeting organizations
in our industry and should be investigated
against historical network telemetry.
```

The transformation is:

```text
Data
 ↓
Information
 ↓
Analysis
 ↓
Intelligence
 ↓
Decision
```

---

# 3. Why Threat Intelligence Matters to Hunters

Without intelligence:

```text
Search Everything
       ↓
Huge Dataset
       ↓
Noise
       ↓
Analyst Fatigue
```

With intelligence:

```text
Threat
 ↓
Likely Behavior
 ↓
Relevant Technique
 ↓
Relevant Telemetry
 ↓
Focused Hunt
```

Threat intelligence helps prioritize where to look.

---

# 4. Threat Intelligence Lifecycle

A typical intelligence lifecycle is:

```text
1. Planning & Direction
          ↓
2. Collection
          ↓
3. Processing
          ↓
4. Analysis
          ↓
5. Dissemination
          ↓
6. Feedback
          ↓
      Reassessment
```

---

# 5. Planning and Direction

Before collecting intelligence, determine what intelligence is actually needed.

Questions include:

- Who are our likely adversaries?
- Which assets are most important?
- Which industries are being targeted?
- Which threats are relevant to our organization?
- What decisions must the intelligence support?

Example:

```text
Organization:
Financial Services

Critical Assets:
├── Customer Data
├── Payment Systems
├── Internet Banking
└── Identity Infrastructure
```

Relevant intelligence priorities may include:

- Banking malware
- Credential theft
- Web application attacks
- Ransomware
- Identity attacks
- Supply-chain attacks

---

# 6. Collection

Threat intelligence can come from many sources.

## Internal Sources

- SIEM
- EDR
- Firewall
- DNS
- Proxy
- Email security
- Authentication systems
- Incident response
- Vulnerability scanners

## External Sources

- CERTs
- Government advisories
- Security vendors
- Threat research
- ISACs
- Public reporting
- Malware repositories
- Threat intelligence platforms

---

# 7. Processing

Raw intelligence often contains:

- Duplicate indicators
- Different formats
- Missing context
- False positives
- Expired infrastructure
- Inconsistent naming

Processing converts raw information into usable datasets.

```text
Raw Intelligence
       ↓
Normalize
       ↓
Deduplicate
       ↓
Validate
       ↓
Enrich
       ↓
Structured Intelligence
```

---

# 8. Analysis

Analysis is where intelligence becomes meaningful.

A hunter may ask:

```text
Who is using this infrastructure?

What malware is associated with it?

Which organizations are targeted?

Which ATT&CK techniques are involved?

How recent is the activity?

Is the infrastructure still active?

Do we have related activity internally?
```

---

# 9. Dissemination

Intelligence should reach the people who need it.

Examples:

### SOC

Needs:

- IOCs
- Detection logic
- TTPs
- Investigation context

### Threat Hunters

Need:

- Adversary behavior
- Techniques
- Campaign information
- Hypotheses

### Incident Response

Needs:

- Indicators
- Infrastructure
- Attack patterns
- Investigation leads

### Executives

Need:

- Risk
- Business impact
- Threat relevance
- Recommended actions

The same intelligence may therefore be presented differently to different audiences.

---

# 10. Feedback

Intelligence is not a one-way process.

After a hunt:

```text
Threat Intelligence
        ↓
Hunt
        ↓
Finding
        ↓
New Intelligence
        ↓
Updated Hypothesis
        ↓
New Hunt
```

Feedback improves future intelligence.

---

# 11. Types of Threat Intelligence

Threat intelligence is commonly divided into:

```text
Strategic
Operational
Tactical
Technical
```

---

# 12. Strategic Threat Intelligence

Strategic intelligence focuses on high-level risk.

Audience:

- Executives
- CISOs
- Risk teams
- Security leadership

Questions:

```text
Who threatens our organization?

Why would they target us?

What is the potential business impact?

What threats are increasing?
```

Example:

> Ransomware activity targeting organizations in the financial sector has increased, with attackers increasingly abusing identity infrastructure and legitimate remote management tools.

Strategic intelligence supports:

- Investment
- Risk management
- Security strategy
- Business decisions

---

# 13. Operational Threat Intelligence

Operational intelligence focuses on campaigns and adversary operations.

It answers:

```text
Who is conducting the campaign?

What are they targeting?

How are they operating?

What infrastructure are they using?
```

It is particularly useful for:

- Threat hunters
- Incident responders
- CTI analysts

---

# 14. Tactical Threat Intelligence

Tactical intelligence focuses on adversary **TTPs**.

TTP means:

```text
Tactics
Techniques
Procedures
```

Example:

```text
Tactic:
Credential Access

Technique:
OS Credential Dumping

Procedure:
Adversary attempts to access credential material
from protected operating-system processes.
```

Tactical intelligence is highly valuable for threat hunting.

---

# 15. Technical Threat Intelligence

Technical intelligence focuses on technical indicators.

Examples:

- IP addresses
- Domains
- URLs
- File hashes
- Email addresses
- Malware signatures
- Certificates

Example:

```text
SHA-256:
<hash>

Domain:
example[.]com

IP:
203.0.113.50
```

Technical intelligence is useful for IOC matching.

---

# 16. Strategic vs Tactical vs Technical

| Type | Primary Question | Audience |
|---|---|---|
| Strategic | What risks matter? | Leadership |
| Operational | What campaigns are happening? | CTI / IR |
| Tactical | How does the attacker operate? | Hunters / SOC |
| Technical | What indicators can we search? | SOC / Detection |

---

# 17. IOC — Indicator of Compromise

An IOC is an observable artifact that may indicate malicious activity.

Examples:

```text
IP Address
Domain
URL
File Hash
Email Address
Certificate
Registry Artifact
Filename
```

Example:

```text
Malicious Domain:

evil-example[.]com
```

A hunter can search:

```text
DNS Logs
Proxy Logs
Firewall Logs
Endpoint Logs
```

for evidence of the indicator.

---

# 18. Limitations of IOC Hunting

IOCs can become obsolete.

Attackers can change:

```text
IP
 ↓
New IP

Domain
 ↓
New Domain

Hash
 ↓
Modified Malware
```

Therefore:

```text
IOC Hunting
+
Behavior Hunting
```

is stronger than IOC hunting alone.

---

# 19. IOA — Indicator of Attack

An **Indicator of Attack (IOA)** focuses on suspicious behavior associated with an attack.

Example:

```text
PowerShell
+
Encoded Command
+
Unusual Parent Process
+
External Network Connection
```

This may be more useful than searching for a known malware hash.

---

# 20. IOC vs IOA

| IOC | IOA |
|---|---|
| Artifact | Behavior |
| Often specific | Often generalized |
| Easy to change | More resilient |
| Hash/IP/domain | Process/network/auth behavior |
| Good for known threats | Good for behavioral hunting |

---

# 21. TTP Intelligence

TTP-based intelligence focuses on how adversaries operate.

Example:

```text
Threat Actor
      ↓
PowerShell
      ↓
Credential Access
      ↓
Remote Services
      ↓
Data Collection
```

This is highly valuable because TTPs are generally more stable than individual infrastructure indicators.

---

# 22. Threat Actor Intelligence

Threat actor intelligence may include:

- Motivation
- Targeting
- Geography
- Victimology
- Known malware
- Infrastructure
- TTPs
- ATT&CK techniques
- Campaign history

Example:

```text
Threat Actor
│
├── Targeting
│   └── Financial organizations
│
├── Initial Access
│   └── Phishing
│
├── Execution
│   └── PowerShell
│
├── Credential Access
│   └── Credential Dumping
│
├── Lateral Movement
│   └── Remote Services
│
└── C2
    └── Web Protocols
```

This profile can directly generate hunt hypotheses.

---

# 23. Threat Intelligence and MITRE ATT&CK

ATT&CK provides a structured vocabulary for representing adversary behavior.

The workflow becomes:

```text
Threat Actor
      ↓
Known Campaign
      ↓
ATT&CK Techniques
      ↓
Potential Behaviors
      ↓
Hunt Hypotheses
```

Example:

```text
Threat Actor
    ↓
T1059.001 PowerShell
    ↓
Execution Hypothesis
    ↓
PowerShell Telemetry
    ↓
Hunt
```

---

# 24. Intelligence-Driven Threat Hunting

A mature process looks like:

```text
External Intelligence
        ↓
Internal Relevance
        ↓
ATT&CK Mapping
        ↓
Hunt Hypothesis
        ↓
Telemetry
        ↓
Hunt
        ↓
Investigation
        ↓
Detection
```

This is called **intelligence-driven threat hunting**.

---

# 25. Intelligence Relevance

Not every threat is relevant to every organization.

Consider:

### Industry

Is the threat targeting your industry?

### Geography

Does the adversary target your region?

### Technology

Does your organization use the affected technology?

### Exposure

Are your systems exposed?

### Business Model

Does your organization possess the type of data or access the adversary wants?

---

# 26. Threat Relevance Matrix

A simple prioritization model:

| Threat | Industry | Technology | Exposure | Priority |
|---|---:|---:|---:|---:|
| Ransomware A | High | High | High | Critical |
| Cloud Campaign B | High | Medium | High | High |
| Malware C | Low | High | Low | Medium |
| Campaign D | Low | Low | Low | Low |

This prevents analysts from spending resources on irrelevant threats.

---

# 27. Hunt Hypotheses

A **hunt hypothesis** is a testable statement about potentially malicious behavior.

Weak:

```text
Look for malware.
```

Better:

```text
An attacker may use PowerShell
after obtaining initial access.
```

Strong:

```text
A compromised Windows endpoint may execute
PowerShell from an unusual parent process,
followed by an outbound connection to a rare
external destination.
```

The strong hypothesis identifies observable evidence.

---

# 28. Hypothesis Structure

A useful structure is:

```text
Threat Scenario
      ↓
Expected Attacker Behavior
      ↓
Expected Evidence
      ↓
Data Source
      ↓
Hunt Query
```

Example:

```text
Scenario:
Compromised workstation

Behavior:
PowerShell execution

Evidence:
Unusual command + rare parent process

Data:
Endpoint telemetry

Query:
Search process creation events
```

---

# 29. Hypothesis Categories

Hunt hypotheses can focus on:

### Execution

> Attackers may execute commands through scripting interpreters.

### Persistence

> Attackers may create scheduled tasks to maintain access.

### Credential Access

> Attackers may access credential stores after obtaining elevated privileges.

### Discovery

> Attackers may enumerate hosts and services after gaining access.

### Lateral Movement

> Attackers may authenticate to multiple systems using compromised credentials.

### Command and Control

> Compromised endpoints may communicate periodically with rare external destinations.

### Exfiltration

> An attacker may transfer unusually large amounts of sensitive data to external infrastructure.

---

# 30. Hypothesis Quality

A strong hypothesis should be:

### Specific

Clearly describe the behavior.

### Testable

There must be observable evidence.

### Relevant

It should relate to a realistic threat.

### Measurable

Results should be possible to evaluate.

### Actionable

Findings should lead to investigation or defensive improvement.

---

# 31. Hypothesis Lifecycle

```text
Create
  ↓
Prioritize
  ↓
Test
  ↓
Investigate
  ↓
Validate
  ↓
Document
  ↓
Convert to Detection
  ↓
Retest
```

---

# 32. Hunt Hypothesis Example — Credential Abuse

## Threat Scenario

An attacker has obtained a valid employee credential.

## Hypothesis

> A compromised account may authenticate from an unusual device and access systems that are not normally associated with the account.

## Data Sources

- Authentication logs
- VPN
- Active Directory
- EDR
- Identity provider
- Cloud audit logs

## Hunt Logic

```text
User
 ↓
Source Device
 ↓
Source IP
 ↓
Destination
 ↓
Authentication Time
 ↓
MFA
 ↓
Post-Authentication Activity
```

---

# 33. Hunt Hypothesis Example — PowerShell

## Scenario

An attacker gains access to a Windows endpoint.

## Hypothesis

> The attacker may execute PowerShell commands using unusual command-line parameters or parent processes.

## Evidence

```text
PowerShell
+
Encoded/obfuscated command
+
Rare parent
+
External network connection
```

## Investigation

Correlate:

- Process creation
- Command line
- User
- Host
- Parent process
- Network connection

---

# 34. Hunt Hypothesis Example — DNS

## Scenario

An attacker establishes command and control.

## Hypothesis

> A compromised endpoint may generate periodic DNS queries to a rare or suspicious domain with unusually long or high-entropy subdomains.

## Evidence

```text
Rare Domain
+
High Query Frequency
+
Long Subdomains
+
Periodic Requests
```

Additional context is required before concluding that DNS tunneling or C2 is present.

---

# 35. Hunt Hypothesis Example — Cloud

## Scenario

An attacker obtains cloud credentials.

## Hypothesis

> A compromised cloud identity may perform API operations from an unusual location or device and create resources inconsistent with its normal behavior.

Potential telemetry:

- Cloud audit logs
- IAM events
- Authentication logs
- API calls
- Resource creation
- Security group changes

---

# 36. Threat Intelligence Sources

Threat intelligence can originate from:

## Government

- CISA
- CERT organizations
- National cybersecurity agencies

## Security Vendors

- Microsoft
- Google
- Palo Alto Networks
- CrowdStrike
- Mandiant
- Cisco Talos
- Sophos
- Fortinet

## Community

- MISP
- AlienVault OTX
- Abuse.ch
- Malware research communities

## Standards and Frameworks

- MITRE ATT&CK
- STIX
- TAXII

Always validate intelligence before operationalizing it.

---

# 37. STIX

**Structured Threat Information Expression (STIX)** is a standardized language and serialization format for representing cyber threat intelligence.

STIX can represent objects such as:

- Threat actors
- Malware
- Indicators
- Campaigns
- Attack patterns
- Relationships

Conceptually:

```text
Threat Actor
     │
     ├── uses
     ▼
 Malware
     │
     ├── communicates with
     ▼
 Infrastructure
     │
     └── associated with
     ▼
 Campaign
```

STIX helps organizations exchange structured threat intelligence.

---

# 38. TAXII

**Trusted Automated Exchange of Intelligence Information (TAXII)** is a protocol for exchanging CTI, commonly used with STIX.

Simplified:

```text
STIX
"What is the intelligence format?"

TAXII
"How is the intelligence exchanged?"
```

Example:

```text
Threat Intelligence Provider
          ↓
         TAXII
          ↓
       STIX Data
          ↓
       TIP / SIEM
          ↓
        Hunting
```

---

# 39. MISP

**MISP — Malware Information Sharing Platform and Threat Sharing** — is an open-source platform used to collect, manage, correlate, and share threat intelligence.

Typical workflow:

```text
Threat Intelligence
        ↓
       MISP
        ↓
Correlation
        ↓
Enrichment
        ↓
SIEM / EDR
        ↓
Threat Hunt
```

MISP can be useful for managing:

- Indicators
- Threat actors
- Malware
- Events
- Relationships
- Intelligence feeds

---

# 40. IOC Enrichment

An IOC becomes more useful when enriched with additional context.

Example:

```text
IP Address
    ↓
WHOIS
    ↓
ASN
    ↓
Geolocation
    ↓
Reputation
    ↓
Historical DNS
    ↓
Threat Intelligence
    ↓
Internal Observations
```

Enrichment can help determine whether an indicator deserves investigation.

---

# 41. IOC Confidence

Not all intelligence has equal confidence.

A useful classification:

```text
High Confidence
Medium Confidence
Low Confidence
Unknown
```

Factors include:

- Source reliability
- Recency
- Corroboration
- Historical activity
- Context
- False-positive history

Avoid automatically blocking every indicator from an external feed.

---

# 42. Intelligence Recency

Threat intelligence has a lifecycle.

An IP address associated with malicious activity six months ago may no longer be malicious.

Consider:

```text
First Seen
    ↓
Active
    ↓
Last Seen
    ↓
Aging
    ↓
Reassessment
```

Always consider timestamp and context.

---

# 43. Threat Intelligence and SIEM

A SIEM can ingest threat intelligence and correlate it with internal telemetry.

```text
Threat Feed
     ↓
IOC Database
     ↓
SIEM
     ↓
Internal Logs
     ↓
Correlation
     ↓
Alert
```

Example:

```text
External IOC
     +
Internal DNS Event
     +
Endpoint Connection
     ↓
Potential Compromise
```

---

# 44. Intelligence-Driven Detection

Threat intelligence can directly produce detections.

```text
Threat Intelligence
       ↓
ATT&CK Mapping
       ↓
Behavior
       ↓
Detection Logic
       ↓
SIEM / EDR
```

Example:

```text
Threat Actor
    ↓
PowerShell
    ↓
Encoded Commands
    ↓
Hunt
    ↓
Detection
```

---

# 45. Intelligence-Driven Threat Hunting Workflow

A professional workflow:

```text
01. Collect Intelligence
          ↓
02. Validate Intelligence
          ↓
03. Determine Relevance
          ↓
04. Map to ATT&CK
          ↓
05. Identify Expected Behavior
          ↓
06. Create Hunt Hypothesis
          ↓
07. Identify Telemetry
          ↓
08. Develop Query
          ↓
09. Search Historical Data
          ↓
10. Investigate Results
          ↓
11. Validate Findings
          ↓
12. Improve Detection
```

---

# 46. Threat Intelligence Quality

Good intelligence should be:

- Relevant
- Timely
- Accurate
- Actionable
- Contextual
- Reliable
- Appropriate for its audience

A large quantity of low-quality intelligence can create more noise than value.

---

# 47. Intelligence Fatigue

Security teams can receive thousands of indicators.

```text
100,000 IOCs
      ↓
SIEM
      ↓
Millions of comparisons
      ↓
High Alert Volume
      ↓
Analyst Fatigue
```

The solution is not necessarily more intelligence.

Better approaches include:

- Prioritization
- Confidence scoring
- Deduplication
- Context enrichment
- Relevance filtering
- Expiration
- Correlation with internal activity

---

# 48. Threat Intelligence Prioritization

A practical model:

```text
Priority =
Threat Relevance
+
Confidence
+
Recency
+
Internal Exposure
+
Business Impact
```

For example:

```text
High-Relevance Actor
+
High-Confidence IOC
+
Recent Activity
+
Internal Match
+
Critical Asset
```

should receive immediate attention.

---

# 49. Intelligence-to-Hypothesis Pipeline

This is one of the most important workflows in this chapter.

```text
External Intelligence
        ↓
Threat Actor
        ↓
Known TTP
        ↓
ATT&CK Technique
        ↓
Expected Behavior
        ↓
Hunt Hypothesis
        ↓
Telemetry
        ↓
Query
        ↓
Evidence
```

Example:

```text
Threat Intelligence:
Actor uses PowerShell

        ↓

ATT&CK:
T1059.001

        ↓

Hypothesis:
Actor may execute PowerShell
after initial compromise

        ↓

Telemetry:
Process + Command Line

        ↓

Hunt
```

---

# 50. Hunt Prioritization

Organizations often have more possible hunts than analysts.

Prioritize based on:

### Threat Relevance

Is the threat relevant to the organization?

### Business Impact

Could the activity affect critical systems?

### Likelihood

Is the attack plausible?

### Exposure

Are vulnerable assets exposed?

### Detection Gap

Is automated detection weak or missing?

### Telemetry Availability

Can the activity actually be investigated?

---

# 51. Hunt Priority Matrix

| Factor | Low | Medium | High |
|---|---|---|---|
| Threat relevance | Low | Moderate | Critical |
| Business impact | Minor | Significant | Severe |
| Exposure | Limited | Moderate | High |
| Detection gap | Covered | Partial | Missing |
| Telemetry | Poor | Adequate | Strong |

A high-priority hunt generally has:

```text
High Threat Relevance
+
High Business Impact
+
High Exposure
+
Detection Gap
+
Available Telemetry
```

---

# 52. Hypothesis Tracking

Maintain a hunt register.

| ID | Hypothesis | ATT&CK | Priority | Status |
|---|---|---|---|---|
| H-001 | Suspicious PowerShell | T1059.001 | High | Completed |
| H-002 | Credential abuse | T1078 | Critical | Active |
| H-003 | DNS tunneling | C2 | Medium | Planned |
| H-004 | Lateral movement | T1021 | High | Active |

Possible statuses:

```text
Planned
Active
Completed
Confirmed
Benign
Inconclusive
Converted to Detection
```

---

# 53. Hunt Outcome Classification

A hunt should produce a documented outcome.

```text
No Suspicious Activity
        │
        ├── Hypothesis disproved
        └── Continue monitoring

Suspicious Activity
        │
        ├── Requires investigation
        └── Additional telemetry

Confirmed Malicious
        │
        ├── Incident Response
        ├── Detection
        └── Lessons Learned
```

---

# 54. Converting a Hunt Into a Detection

A successful hunt should be evaluated for automation.

```text
Hunt Finding
     ↓
Stable Behavioral Pattern?
     │
 ┌───┴───┐
No      Yes
 │        │
 ▼        ▼
Manual   Detection
Hunt     Engineering
          ↓
       Test Rule
          ↓
       Tune Rule
          ↓
       Deploy
```

Not every hunt should become an alert.

Some behaviors are better suited for:

- Scheduled analytics
- Dashboards
- Risk scoring
- Investigation queries
- Periodic hunting

---

# 55. Threat Intelligence Feedback Loop

A mature organization continuously feeds findings back into intelligence.

```text
External Intelligence
        ↓
Internal Hunt
        ↓
Internal Finding
        ↓
New Evidence
        ↓
Threat Intelligence Update
        ↓
Improved Hypothesis
        ↓
New Hunt
```

This creates an adaptive security program.

---

# 56. Practical Lab — Intelligence-Driven Hunt

## Scenario

Your organization receives intelligence that a threat actor targeting your industry has been observed using:

```text
PowerShell
Credential Access
Remote Services
DNS-based C2
```

Your environment contains:

```text
Windows
Active Directory
EDR
SIEM
DNS
Firewall
```

---

## Objective

Determine whether historical telemetry contains behavior consistent with the threat actor's known techniques.

---

## Step 1 — Create Intelligence Profile

Document:

```text
Threat Actor

Targeting

Motivation

Known Malware

Known Infrastructure

Known TTPs

ATT&CK Techniques
```

---

## Step 2 — Map Techniques

Example:

```text
PowerShell
    ↓
T1059.001

Credential Access
    ↓
Relevant ATT&CK Technique

Remote Services
    ↓
Relevant ATT&CK Technique

DNS C2
    ↓
Relevant ATT&CK Technique
```

---

## Step 3 — Create Hypotheses

### H1

> An attacker may execute PowerShell after gaining access to a Windows endpoint.

### H2

> An attacker may attempt credential access before moving laterally.

### H3

> A compromised endpoint may establish periodic DNS communication with attacker-controlled infrastructure.

### H4

> A compromised account may authenticate to multiple internal systems.

---

## Step 4 — Identify Telemetry

```text
Process Logs
PowerShell Logs
Authentication
EDR
DNS
Firewall
Active Directory
```

---

## Step 5 — Hunt

Search historical telemetry for:

- Rare PowerShell activity
- Suspicious process relationships
- Credential access indicators
- Unusual authentication
- Repeated DNS patterns
- Rare domains
- Unusual remote connections

---

## Step 6 — Correlate

Do not investigate each event in isolation.

Build timelines:

```text
Initial Authentication
        ↓
PowerShell
        ↓
Credential Access
        ↓
Discovery
        ↓
Remote Authentication
        ↓
DNS Activity
```

---

## Step 7 — Determine Outcome

Classify:

```text
Benign
Suspicious
Confirmed Malicious
Inconclusive
```

---

## Step 8 — Improve Detection

For validated behavior:

```text
Finding
 ↓
Detection Logic
 ↓
Test
 ↓
Tune
 ↓
Deploy
```

---

# 57. Practical Intelligence Analysis Questions

When receiving new intelligence, ask:

### Relevance

- Does this threat target our industry?
- Does it target our geography?
- Does it target our technology stack?

### Recency

- When was the activity observed?
- Is the infrastructure still active?

### Confidence

- How reliable is the source?
- Is the intelligence corroborated?

### Exposure

- Do we operate affected systems?
- Are they externally accessible?

### Detection

- Can we detect the described behavior?
- Do we have the required telemetry?

### Hunting

- Can we search historical data?
- How far back does our telemetry go?

---

# 58. Common Threat Intelligence Mistakes

## Treating Every IOC as Malicious Forever

Indicators can become stale.

---

## Consuming Too Many Feeds

More feeds do not automatically mean better intelligence.

---

## Ignoring Context

An IOC without context has limited value.

---

## Focusing Only on IOCs

TTP intelligence is often more durable.

---

## Not Validating Intelligence

External intelligence may contain:

- False positives
- Stale indicators
- Attribution uncertainty
- Duplicates

---

## Not Connecting Intelligence to Internal Telemetry

Threat intelligence becomes much more useful when compared against actual organizational activity.

---

# 59. Best Practices

- Define intelligence requirements.
- Prioritize relevant threats.
- Validate external intelligence.
- Track confidence and recency.
- Enrich indicators before operationalizing them.
- Map adversary behavior to ATT&CK.
- Convert TTP intelligence into hunt hypotheses.
- Use multiple telemetry sources.
- Hunt historically where possible.
- Correlate behaviors instead of relying on isolated events.
- Document hunt outcomes.
- Feed discoveries back into intelligence.
- Convert stable findings into detections.
- Expire or reassess stale intelligence.
- Measure intelligence effectiveness.

---

# 60. Interview Questions

## Beginner

### What is threat intelligence?

Threat intelligence is analyzed information about cyber threats that helps an organization understand threats and make informed security decisions.

---

### What is the difference between data and intelligence?

Data is raw information. Intelligence is analyzed and contextualized information that supports a security decision.

---

### What are the major types of threat intelligence?

Common categories are:

- Strategic
- Operational
- Tactical
- Technical

---

### What is an IOC?

An IOC is an observable artifact that may indicate compromise, such as an IP address, domain, URL, or file hash.

---

## Intermediate

### What is TTP-based intelligence?

TTP-based intelligence describes adversary tactics, techniques, and procedures rather than focusing exclusively on individual indicators.

---

### Why is TTP-based hunting valuable?

Attackers can frequently change infrastructure and malware hashes, while their operational behaviors and techniques may remain more consistent.

---

### What is STIX?

STIX is a standardized language and format for representing structured cyber threat intelligence.

---

### What is TAXII?

TAXII is a protocol used to exchange cyber threat intelligence, commonly STIX-formatted information.

---

### What is MISP?

MISP is an open-source threat intelligence platform used to collect, correlate, enrich, manage, and share threat intelligence.

---

## Advanced

### How do you turn threat intelligence into a hunt hypothesis?

```text
Threat Intelligence
       ↓
Relevant Adversary
       ↓
Known TTP
       ↓
ATT&CK Technique
       ↓
Expected Behavior
       ↓
Observable Evidence
       ↓
Telemetry
       ↓
Hunt Hypothesis
```

---

### How do you determine whether threat intelligence is relevant?

Evaluate:

- Industry targeting
- Geographic targeting
- Technology overlap
- Asset exposure
- Threat actor motivation
- Business impact
- Intelligence confidence
- Recency

---

### Why shouldn't an organization automatically block every IOC?

Because intelligence can contain stale indicators, false positives, shared infrastructure, compromised legitimate services, or insufficient context. Blocking should be based on confidence, relevance, and organizational risk.

---

### How do threat intelligence and threat hunting work together?

Threat intelligence identifies relevant threats and adversary behaviors, while threat hunting searches internal telemetry for evidence that those behaviors may be occurring.

---

# 61. Professional Threat Intelligence Workflow

A mature CTI program can be represented as:

```text
                  REQUIREMENTS
                       │
                       ▼
                   COLLECTION
                       │
                       ▼
                   PROCESSING
                       │
                       ▼
                    ANALYSIS
                       │
                       ▼
                 INTELLIGENCE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
         SOC         Hunting         IR
          │            │            │
          └────────────┼────────────┘
                       ▼
                    FEEDBACK
                       │
                       ▼
                 New Intelligence
```

---

# 62. Intelligence-to-Detection Pipeline

```text
Threat Intelligence
        ↓
Threat Actor
        ↓
TTP
        ↓
MITRE ATT&CK
        ↓
Threat Hypothesis
        ↓
Hunt
        ↓
Validated Behavior
        ↓
Detection Logic
        ↓
Sigma / KQL / SPL
        ↓
SIEM / EDR
        ↓
SOC Alert
        ↓
Incident Response
```

This pipeline connects threat intelligence with the entire defensive security lifecycle.

---

# 63. Chapter Summary

Threat intelligence gives threat hunters context.

The most important transformation is:

```text
Raw Data
   ↓
Information
   ↓
Intelligence
   ↓
Threat Understanding
   ↓
Hunt Hypothesis
   ↓
Hunt
   ↓
Evidence
   ↓
Detection
```

The most effective intelligence programs do not simply collect thousands of indicators.

They answer:

```text
Who?

Why?

Who is being targeted?

How does the adversary operate?

What techniques do they use?

What evidence will they leave?

Can we observe that evidence?

Can we detect it?

Can we hunt for it historically?
```

The ultimate objective is to turn intelligence into **actionable defensive capability**.

```text
INTELLIGENCE
      ↓
UNDERSTANDING
      ↓
HYPOTHESIS
      ↓
HUNT
      ↓
DISCOVERY
      ↓
DETECTION
      ↓
RESPONSE
      ↓
LESSONS LEARNED
      ↓
BETTER INTELLIGENCE
```

---

# References

## Threat Intelligence

- CISA — https://www.cisa.gov/
- MITRE ATT&CK — https://attack.mitre.org/
- MITRE Center for Threat-Informed Defense — https://ctid.mitre.org/
- NIST Cybersecurity Framework — https://www.nist.gov/cyberframework

## Structured Intelligence

- STIX — https://oasis-open.github.io/cti-documentation/
- TAXII — https://oasis-open.github.io/cti-documentation/
- MISP — https://www.misp-project.org/

## Threat Research

- CISA Known Exploited Vulnerabilities Catalog — https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK Groups — https://attack.mitre.org/groups/
- MITRE ATT&CK Techniques — https://attack.mitre.org/techniques/

---

