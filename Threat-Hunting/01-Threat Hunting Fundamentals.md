# Threat Hunting Fundamentals

## Overview

Threat Hunting is the proactive and systematic process of searching through security telemetry to identify malicious activity, attacker behavior, and security weaknesses that may not have been detected by existing security controls.

Traditional security operations generally follow an alert-driven model:

```text
Security Event
      ↓
Detection Rule
      ↓
Alert
      ↓
SOC Investigation
      ↓
Incident Response
```

Threat hunting introduces a proactive approach:

```text
Threat Intelligence
        ↓
Threat Hypothesis
        ↓
Identify Required Telemetry
        ↓
Search Security Data
        ↓
Investigate Anomalies
        ↓
Validate Findings
        ↓
Create / Improve Detection
        ↓
Continuous Hunting
```

The objective of threat hunting is not simply to find malware.

The broader objective is to discover **evidence of adversary behavior that existing security controls may have missed** and use those findings to continuously improve an organization's defensive capabilities.

---

# Why Threat Hunting Matters

Modern attackers increasingly use techniques designed to evade traditional security controls.

Examples include:

* Living-off-the-land techniques
* Legitimate administrative tools
* Fileless execution
* Credential abuse
* Cloud identity compromise
* Living-off-the-cloud techniques
* Supply-chain compromise
* Custom malware
* Encrypted command-and-control traffic
* Valid account abuse

An attacker may therefore operate without generating an obvious malware alert.

Example:

```text
Attacker
   ↓
Compromised Account
   ↓
Legitimate PowerShell
   ↓
Credential Access
   ↓
Lateral Movement
   ↓
Data Access
```

No single event may appear obviously malicious.

Threat hunting attempts to connect these individual behaviors into a meaningful attack story.

---

# Threat Hunting vs Traditional Security Monitoring

## Traditional Monitoring

Traditional monitoring is primarily alert-driven.

```text
Event
 ↓
Rule
 ↓
Alert
 ↓
Analyst
```

The SOC waits for known detection logic to identify suspicious activity.

---

## Threat Hunting

Threat hunting begins with a question or hypothesis.

```text
Hypothesis
 ↓
Search Telemetry
 ↓
Find Evidence
 ↓
Investigate
 ↓
Validate
```

For example:

> "Could an attacker be using compromised credentials to access systems outside the user's normal working pattern?"

The hunter then searches authentication, endpoint, network, and identity telemetry for supporting evidence.

---

# Threat Hunting vs Incident Response

These disciplines are related but different.

| Threat Hunting              | Incident Response                         |
| --------------------------- | ----------------------------------------- |
| Proactive                   | Primarily reactive                        |
| Searches for hidden threats | Responds to confirmed/suspected incidents |
| Hypothesis-driven           | Incident-driven                           |
| Looks for unknown activity  | Investigates known activity               |
| Improves detections         | Contains and eradicates threats           |
| Searches telemetry          | Collects evidence and responds            |

Typical relationship:

```text
Threat Hunt
     ↓
Suspicious Activity
     ↓
Investigation
     ↓
Confirmed Incident
     ↓
Incident Response
     ↓
Lessons Learned
     ↓
Improved Detection
```

---

# Threat Hunting vs Vulnerability Management

These are also different disciplines.

### Vulnerability Management

Focuses on weaknesses:

```text
Asset
 ↓
Vulnerability
 ↓
Risk
 ↓
Patch / Mitigation
```

### Threat Hunting

Focuses on adversary activity:

```text
Telemetry
 ↓
Suspicious Behavior
 ↓
Investigation
 ↓
Threat Discovery
```

A vulnerable system does not necessarily mean it has been compromised.

Threat hunting investigates whether suspicious activity is actually occurring.

---

# Threat Hunting vs Penetration Testing

| Penetration Testing               | Threat Hunting                                |
| --------------------------------- | --------------------------------------------- |
| Simulates attacker behavior       | Searches for real/simulated attacker behavior |
| Controlled offensive activity     | Defensive investigation                       |
| Identifies exploitable weaknesses | Identifies suspicious activity                |
| Usually time-bound                | Continuous/recurring                          |
| Primarily attacker perspective    | Primarily defender perspective                |

Both disciplines complement each other.

For example:

```text
Penetration Test
       ↓
Attacker Technique
       ↓
Security Telemetry
       ↓
Threat Hunt
       ↓
Detection Rule
```

---

# Threat Hunting Lifecycle

A mature hunt follows a repeatable lifecycle.

```text
1. Preparation
       ↓
2. Hypothesis
       ↓
3. Data Collection
       ↓
4. Hunt
       ↓
5. Investigation
       ↓
6. Validation
       ↓
7. Detection Engineering
       ↓
8. Documentation
       ↓
9. Continuous Improvement
```

---

# 1. Preparation

Before starting a hunt, understand the environment.

Determine:

* What assets exist?
* Which users are privileged?
* Which logs are available?
* Which endpoints are monitored?
* Which cloud platforms are used?
* Which applications are critical?
* Which security controls are deployed?

Example:

```text
Environment

├── Windows
├── Linux
├── Active Directory
├── AWS
├── Kubernetes
├── Web Applications
├── Firewalls
├── EDR
└── SIEM
```

A hunter cannot investigate telemetry that the organization does not collect.

---

# 2. Threat Hypothesis

A threat hypothesis is a testable statement about potentially malicious activity.

Weak hypothesis:

```text
Look for hackers.
```

Strong hypothesis:

```text
An attacker who compromises a user's credentials
may authenticate from an unusual device or location
before accessing privileged resources.
```

A good hypothesis should define:

* Threat actor behavior
* Target
* Expected evidence
* Relevant telemetry
* Investigation direction

---

# Hunt Hypothesis Structure

Use:

```text
Because [threat scenario],

I believe [attacker behavior]

will produce [observable evidence]

in [data source].
```

Example:

```text
Because attackers may abuse compromised credentials,

I believe successful authentication from unusual
devices followed by privileged activity

will produce observable anomalies

in identity and authentication logs.
```

---

# 3. Identify Required Telemetry

After creating a hypothesis, determine what data can validate it.

Example:

```text
Hypothesis:
Compromised account

        ↓

Required Telemetry

├── Authentication Logs
├── VPN Logs
├── MFA Logs
├── Endpoint Telemetry
├── Cloud Audit Logs
└── Network Logs
```

This is an important skill for threat hunters.

The question is not only:

> "What query should I run?"

It is:

> "What evidence would prove or disprove my hypothesis?"

---

# 4. Hunt

The hunter searches available telemetry.

Possible approaches include:

* Exact IOC searches
* Behavioral searches
* Statistical analysis
* Baseline comparison
* Time-series analysis
* Process-tree analysis
* Network analysis
* Identity analytics
* Threat intelligence correlation

---

# IOC-Based Hunting

IOC stands for **Indicator of Compromise**.

Examples:

* IP addresses
* Domains
* URLs
* File hashes
* Email addresses
* Registry artifacts

Example:

```text
Known Malicious IP

        ↓

Firewall Logs

        ↓

Endpoint Connections

        ↓

Affected Hosts
```

IOC hunting is useful but limited because attackers can change infrastructure.

---

# Behavior-Based Hunting

Behavior-based hunting focuses on what an attacker does rather than a known artifact.

Example:

```text
Unusual PowerShell
       +
Encoded Command
       +
Network Connection
       +
Rare Parent Process
```

Together, these behaviors may indicate suspicious activity.

Behavior-based hunting is often more resilient against changing attacker infrastructure.

---

# Baseline-Based Hunting

A baseline describes normal activity.

Example:

```text
User Alice

Normal:

09:00–18:00
Bengaluru
Laptop-A
Finance Application
```

Observed:

```text
02:30
Foreign Location
Unknown Device
Administrative Application
```

The difference becomes a hunting lead.

Important:

> An anomaly is not automatically malicious.

It must be investigated in context.

---

# Statistical Hunting

Statistical techniques can identify unusual activity.

Examples:

* Rare processes
* Unusual login times
* High-volume DNS requests
* Large data transfers
* Unusual authentication frequency
* Rare destination domains

Example:

```text
Average DNS Requests

100 / hour

↓

Endpoint

↓

8,000 / hour

↓

Investigate
```

---

# 5. Investigation

Finding an anomaly is only the beginning.

Investigate:

```text
Who?

What?

When?

Where?

Why?

How?
```

---

## Who?

Identify:

* User
* Account
* Host
* Service
* Process owner

---

## What?

Determine:

* Process executed
* File accessed
* Network connection
* Authentication event
* Configuration change

---

## When?

Build a timeline.

```text
09:14
Login

↓

09:16
PowerShell

↓

09:18
Credential Access

↓

09:22
Remote Connection

↓

09:30
Sensitive File Access
```

---

## Where?

Determine:

* Source host
* Destination host
* IP address
* Cloud region
* Network segment

---

## Why?

Determine whether the activity has a legitimate business explanation.

Example:

```text
Suspicious PowerShell

↓

Administrator

↓

Approved Maintenance Window

↓

Benign
```

Context prevents unnecessary escalation.

---

## How?

Determine the possible attack path.

```text
Initial Access
      ↓
Execution
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Collection
```

---

# 6. Validate Findings

Not every suspicious event represents an attack.

Possible outcomes:

```text
Finding

├── Benign
├── False Positive
├── Suspicious
├── Confirmed Malicious
└── Insufficient Evidence
```

The hunter should document the reasoning behind the conclusion.

---

# False Positive

A false positive occurs when legitimate activity triggers suspicion.

Example:

```text
PowerShell Execution

↓

Detection

↓

Authorized Administrator

↓

Expected Activity

↓

False Positive
```

The solution may involve tuning the detection.

---

# False Negative

A false negative occurs when malicious activity is not detected.

Example:

```text
Credential Theft

↓

No Alert

↓

Attacker Continues
```

Threat hunting can uncover these detection gaps.

---

# 7. Detection Engineering

A successful hunt should ideally improve permanent security controls.

```text
Threat Hunt

↓

New Malicious Behavior

↓

Detection Logic

↓

Sigma / KQL / SPL

↓

SIEM / EDR

↓

Continuous Detection
```

This is one of the most valuable outcomes of threat hunting.

---

# Hunt-to-Detection Pipeline

```text
Hypothesis
     ↓
Hunt
     ↓
Evidence
     ↓
Validated Threat
     ↓
Detection Rule
     ↓
Testing
     ↓
Deployment
     ↓
Monitoring
     ↓
Tuning
```

---

# 8. Documentation

Every hunt should be documented.

Recommended format:

```text
Hunt Name

Objective

Hypothesis

MITRE ATT&CK Mapping

Data Sources

Hunt Queries

Findings

Evidence

False Positives

Conclusion

Detection Opportunity

Recommendations
```

Professional documentation allows another analyst to reproduce the investigation.

---

# 9. Continuous Improvement

Threat hunting should feed back into the security program.

```text
Hunt

↓

Finding

↓

Detection Gap

↓

New Detection

↓

Better Telemetry

↓

Improved SOC

↓

Future Hunt
```

This creates a continuous defensive feedback loop.

---

# Threat Hunting Pyramid

A useful way to think about hunting is through levels of observable information.

```text
             TTPs
              ▲
             / \
            /   \
           /     \
          /       \
       Behaviors
        /       \
       /         \
     Artifacts
      /         \
     /           \
    IOCs
```

The lower levels are often easier to search but easier for attackers to change.

The higher levels focus on attacker behavior and techniques.

---

# IOC → Behavior → TTP

### IOC

```text
203.0.113.50
```

Very specific.

---

### Behavior

```text
Endpoint communicates with a rare
external destination immediately after
suspicious process execution.
```

More general.

---

### TTP

```text
Command and Control

MITRE ATT&CK Technique
```

Most reusable.

A mature hunting program increasingly focuses on behavior and TTPs rather than relying exclusively on static IOCs.

---

# Threat Hunting Data Sources

## Endpoint Telemetry

Examples:

* Process creation
* Parent-child relationships
* Command lines
* File creation
* Registry activity
* Services
* Scheduled tasks
* Network connections

---

## Windows

Important sources include:

* Windows Security Event Log
* Sysmon
* PowerShell logs
* Windows Defender
* EDR telemetry
* Active Directory events

---

## Linux

Examples:

```text
/var/log/auth.log

/var/log/secure

/var/log/syslog

auditd

journald
```

---

## Network

Sources include:

* DNS
* Firewall
* Proxy
* NetFlow
* Zeek
* IDS/IPS
* VPN

---

## Cloud

Examples:

* AWS CloudTrail
* Azure Activity Logs
* Microsoft Entra ID logs
* Google Cloud Audit Logs

---

# Threat Hunting Data Quality

Good hunting requires good telemetry.

Important properties include:

### Coverage

Are important systems monitored?

### Accuracy

Are events recorded correctly?

### Completeness

Are important fields available?

### Timeliness

Are events available quickly enough for investigation?

### Retention

Are historical events retained long enough?

---

# Threat Hunting Hypothesis Example

## Scenario

An attacker may attempt to move laterally using compromised credentials.

### Hypothesis

```text
An attacker using compromised credentials may
authenticate to systems that the legitimate user
rarely or never accesses.
```

### Data Sources

```text
Authentication Logs
       +
VPN Logs
       +
Active Directory
       +
Endpoint Telemetry
```

### Hunt

Search for:

* Rare source hosts
* Unusual destination systems
* Administrative authentication
* Authentication outside normal hours
* Multiple systems accessed rapidly

### Investigation

```text
User

↓

Source Host

↓

Destination Host

↓

Authentication Type

↓

Time

↓

Subsequent Activity
```

### Outcome

If malicious:

```text
Threat Hunt
    ↓
Confirmed Behavior
    ↓
Incident Response
    ↓
Detection Rule
```

---

# MITRE ATT&CK Integration

Threat hunters should understand adversary behavior through the MITRE ATT&CK framework.

A hunt can map:

```text
Hunt Hypothesis
      ↓
ATT&CK Technique
      ↓
Data Source
      ↓
Detection
      ↓
Investigation
```

Example:

```text
Suspicious PowerShell

↓

T1059.001

↓

PowerShell Logs

↓

Process Telemetry

↓

Detection
```

MITRE ATT&CK mapping should be covered in depth in Chapter 2.

---

# Threat Hunting Maturity Model

A practical maturity progression:

```text
Level 1
Reactive Investigation

        ↓

Level 2
IOC-Based Hunting

        ↓

Level 3
Hypothesis-Driven Hunting

        ↓

Level 4
Behavior-Based Hunting

        ↓

Level 5
Continuous Detection Engineering
```

---

## Level 1 — Reactive

The team investigates only after alerts.

```text
Alert
 ↓
Investigation
```

---

## Level 2 — IOC Hunting

The team searches for known:

* IPs
* Domains
* Hashes
* URLs

---

## Level 3 — Hypothesis-Driven

Hunters proactively investigate possible attacker behaviors.

---

## Level 4 — Behavior-Based

The organization hunts for:

* Anomalies
* TTPs
* Behavioral patterns
* Rare events

---

## Level 5 — Continuous Detection Engineering

Threat hunting, detection engineering, threat intelligence, and SOC operations operate as a continuous feedback loop.

---

# Threat Hunting Workflow

```text
                 Threat Intelligence
                         │
                         ▼
                 Hunt Hypothesis
                         │
                         ▼
                 Identify Telemetry
                         │
                         ▼
                   Hunt Query
                         │
                         ▼
                    Findings
                         │
                         ▼
                   Investigation
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           Benign                Malicious
              │                     │
              ▼                     ▼
        Tune Detection        Incident Response
                                    │
                                    ▼
                           Detection Engineering
                                    │
                                    ▼
                            Continuous Monitoring
```

---

# Common Threat Hunting Mistakes

## 1. Searching Without a Hypothesis

Bad:

```text
Search Everything
```

Better:

```text
Hypothesis
 ↓
Relevant Data
 ↓
Targeted Hunt
```

---

## 2. Relying Only on IOCs

Attackers can change:

* IP addresses
* Domains
* File hashes

Behavior is often more durable.

---

## 3. Ignoring Context

An unusual event may have a legitimate explanation.

Always consider:

* User role
* Business function
* Maintenance windows
* Asset criticality
* Known administrative activity

---

## 4. Ignoring Telemetry Gaps

If logs are missing, document the limitation.

```text
Cannot Detect

↓

Missing Telemetry

↓

Telemetry Improvement
```

---

## 5. Not Converting Hunts into Detections

If the same threat is discovered repeatedly, it should often become a detection rule.

---

# Threat Hunting Best Practices

* Start with a clear hypothesis.
* Understand the environment before hunting.
* Know what telemetry is available.
* Hunt behavior, not only indicators.
* Map findings to ATT&CK techniques.
* Correlate multiple data sources.
* Establish normal baselines.
* Investigate anomalies in context.
* Document evidence.
* Record false positives.
* Convert valuable hunts into detections.
* Continuously tune detection logic.
* Track telemetry gaps.
* Revisit previous hunts as environments change.

---

# Professional Hunt Documentation Template

Every future hunt in this repository should follow this structure:

```text
# Hunt Name

## Objective

## Threat Hypothesis

## Threat Scenario

## MITRE ATT&CK Mapping

## Data Sources

## Required Telemetry

## Hunt Methodology

## Hunt Queries

## Expected Results

## Investigation Workflow

## False Positives

## Findings

## Evidence

## Conclusion

## Detection Opportunity

## Recommended Controls

## Lessons Learned

## References
```

This makes the repository useful as both a learning resource and a professional portfolio.

---

# Practical Lab

## Lab Objective

Perform a hypothesis-driven threat hunt against a controlled dataset.

### Scenario

A user account is suspected of being compromised.

The organization provides:

```text
Authentication Logs
DNS Logs
VPN Logs
Windows Events
Endpoint Telemetry
```

### Hypothesis

```text
A compromised user account may authenticate
from an unusual source and subsequently perform
activities outside the user's normal behavior.
```

### Investigation

Start with:

```text
Authentication Events
        ↓
Source IP
        ↓
Device
        ↓
Login Time
        ↓
MFA
        ↓
Endpoint Activity
        ↓
Network Activity
```

### Questions

Determine:

1. Was the authentication unusual?
2. Was the device known?
3. Was MFA successful?
4. Did the user access unusual systems?
5. Did suspicious processes execute afterward?
6. Was there unusual network activity?
7. Does the evidence support compromise?

### Final Deliverable

Produce:

```text
Hunt Report

├── Hypothesis
├── Data Sources
├── Queries
├── Findings
├── Evidence
├── Timeline
├── Conclusion
└── Detection Recommendation
```

Only perform testing against datasets or systems for which you have explicit authorization.

---

# Interview Questions

## Beginner

### What is threat hunting?

Threat hunting is the proactive search for malicious activity or suspicious behavior that may not have been detected by existing security controls.

---

### How is threat hunting different from SOC monitoring?

SOC monitoring primarily analyzes incoming alerts and events, while threat hunting proactively searches telemetry for threats that may not have generated alerts.

---

### What is a threat hypothesis?

A threat hypothesis is a testable statement describing an expected attacker behavior and the evidence that should exist if that behavior occurred.

---

### What is an IOC?

An Indicator of Compromise is an observable artifact associated with potentially malicious activity, such as a malicious IP address, domain, URL, or file hash.

---

## Intermediate

### What is the difference between IOC and IOA?

IOC-based hunting searches for known artifacts associated with compromise.

IOA-based hunting focuses on behaviors indicating that an attack may be occurring.

---

### Why is threat hunting hypothesis-driven?

A hypothesis provides direction and identifies what evidence should be searched for. This makes hunting more focused, repeatable, and measurable.

---

### What telemetry would you need to hunt credential abuse?

Potential sources include:

* Authentication logs
* Active Directory
* VPN logs
* MFA logs
* Endpoint telemetry
* Cloud identity logs
* Network logs

---

### What should happen after discovering malicious activity?

The finding should be validated, documented, escalated according to the organization's incident response process, and used to improve detection and prevention controls.

---

## Advanced

### How would you perform a threat hunt from beginning to end?

A structured process would be:

```text
Understand Environment
        ↓
Define Threat Scenario
        ↓
Create Hypothesis
        ↓
Identify Telemetry
        ↓
Develop Hunt Queries
        ↓
Analyze Results
        ↓
Investigate Anomalies
        ↓
Validate Findings
        ↓
Document Results
        ↓
Create / Improve Detection
```

---

### How do you measure threat hunting effectiveness?

Possible metrics include:

* Number of meaningful hunts completed
* Confirmed threats discovered
* Detection gaps identified
* New detections created
* False-positive reduction
* Telemetry coverage improvements
* Mean Time to Detect (MTTD)
* Mean Time to Respond (MTTR)
* ATT&CK technique coverage

Metrics should focus on meaningful security outcomes rather than simply counting hunts.

---

### What makes a good threat hunter?

A strong threat hunter combines:

```text
Security Knowledge
+
Adversary Understanding
+
Data Analysis
+
Query Skills
+
Critical Thinking
+
Investigation Skills
+
Detection Engineering
```

The ability to ask the right question is often more important than knowing a particular SIEM query syntax.

---

# Tools Covered in This Repository

Future chapters will explore:

### SIEM

* Splunk
* Microsoft Sentinel
* Elastic Security

### Endpoint

* Sysmon
* Microsoft Defender
* Velociraptor
* osquery

### Network

* Wireshark
* Zeek
* Suricata

### Detection

* Sigma
* YARA

### Intelligence

* MITRE ATT&CK
* MISP
* STIX/TAXII

---

# Skills Demonstrated

Completing this chapter should demonstrate understanding of:

```text
Threat Hunting
Threat Intelligence
Hypothesis-Driven Investigation
Security Telemetry
IOC Analysis
Behavior Analysis
SIEM
Detection Engineering
MITRE ATT&CK
Incident Response
Security Analytics
```

---

# References

## Frameworks and Standards

* MITRE ATT&CK
* NIST Cybersecurity Framework
* NIST SP 800-61
* NIST SP 800-92

## Threat Hunting

* MITRE ATT&CK Data Sources
* Threat Hunting methodologies
* Detection Engineering practices

## Defensive Security

* CISA guidance
* Microsoft security documentation
* AWS security documentation
* Google Cloud security documentation

---

# Chapter Summary

Threat hunting is a proactive cybersecurity discipline focused on discovering adversary activity that may evade existing security controls.

A mature hunting process follows:

```text
Hypothesis
    ↓
Telemetry
    ↓
Hunt
    ↓
Investigation
    ↓
Validation
    ↓
Detection
    ↓
Continuous Improvement
```

The most important mindset is:

> **Do not only investigate what your security tools tell you. Investigate what an attacker could be doing that your tools have not yet detected.**

Effective threat hunting combines threat intelligence, adversary behavior, security telemetry, data analysis, investigation, and detection engineering.

The ultimate goal is not simply to find threats.

It is to continuously improve the organization's ability to:

```text
PREVENT
   ↓
DETECT
   ↓
INVESTIGATE
   ↓
RESPOND
   ↓
LEARN
   ↓
DETECT BETTER
```

---

# Next Chapter

## 02 — MITRE ATT&CK for Threat Hunters

The next chapter will cover:

* MITRE ATT&CK fundamentals
* Enterprise ATT&CK
* Tactics
* Techniques
* Sub-techniques
* Procedures
* Data Sources
* Data Components
* ATT&CK Navigator
* Mapping hunts to ATT&CK
* Mapping detections to ATT&CK
* Identifying detection gaps
* Threat actor profiles
* ATT&CK-based hunting methodology
* Practical ATT&CK hunting exercises
* Interview questions
