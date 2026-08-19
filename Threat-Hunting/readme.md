# Threat Hunting

> A practical, detection-driven cybersecurity knowledge base for proactively discovering threats that evade traditional security controls.

## Overview

**Threat Hunting** is the proactive process of searching for malicious activity, attacker behavior, and security anomalies that may not have triggered existing security alerts.

Traditional security monitoring often follows:

```text
Event
  ↓
Detection Rule
  ↓
Alert
  ↓
Investigation
```

Threat hunting reverses the approach:

```text
Threat Intelligence / Hypothesis
            ↓
       Hunt Strategy
            ↓
      Security Telemetry
            ↓
      Data Analysis
            ↓
      Suspicious Activity
            ↓
        Investigation
            ↓
 Detection Engineering
            ↓
 Improved Security Controls
```

This repository documents the methodologies, tools, techniques, and practical workflows used to perform effective threat hunting across endpoints, networks, identities, cloud environments, applications, and enterprise infrastructure.

---

## Why Threat Hunting Matters

Attackers can bypass:

* Signature-based antivirus
* Static Indicators of Compromise (IOCs)
* Basic firewall rules
* Traditional detection rules
* Endpoint security controls
* Network monitoring

Threat hunting helps security teams discover suspicious behavior that existing controls may have missed.

A mature security operation should not only ask:

> "Did an alert trigger?"

It should also ask:

> "What could an attacker be doing that our current detections would miss?"

---

## Threat Hunting Philosophy

Threat hunting is based on **hypothesis-driven investigation**.

Instead of searching randomly:

```text
Collect Everything
      ↓
Search Everything
      ↓
Hope Something Appears
```

A structured hunt follows:

```text
Threat Intelligence
        ↓
Threat Hypothesis
        ↓
Required Telemetry
        ↓
Hunt Query
        ↓
Evidence
        ↓
Validation
        ↓
Detection Improvement
```

---

## Repository Goals

This repository is designed to build practical knowledge in:

* Threat Hunting
* Detection Engineering
* SOC Operations
* Incident Response
* Digital Forensics
* Endpoint Detection
* Network Detection
* Identity Threat Detection
* Cloud Threat Hunting
* Malware Analysis
* MITRE ATT&CK
* SIEM Engineering
* Security Analytics

The objective is not simply to memorize attacker techniques, but to understand:

```text
How attackers behave
        ↓
What evidence they leave
        ↓
Where that evidence exists
        ↓
How to find it
        ↓
How to detect it
        ↓
How to respond
```

---

# Repository Structure

```text
Threat-Hunting/
│
├── README.md
│
├── 01-Fundamentals/
│   ├── Threat-Hunting-Fundamentals.md
│   ├── Threat-Hunting-Lifecycle.md
│   ├── Hunting-Hypotheses.md
│   ├── IOC-vs-IOA.md
│   ├── Threat-Intelligence.md
│   └── Threat-Hunting-Maturity.md
│
├── 02-MITRE-ATT&CK/
│   ├── ATTACK-Fundamentals.md
│   ├── Tactics.md
│   ├── Techniques.md
│   ├── Sub-Techniques.md
│   └── ATTACK-Mapping.md
│
├── 03-Endpoint-Hunting/
│   ├── Windows.md
│   ├── Linux.md
│   ├── PowerShell.md
│   ├── Process-Execution.md
│   ├── Persistence.md
│   └── Privilege-Escalation.md
│
├── 04-Network-Hunting/
│   ├── Network-Telemetry.md
│   ├── DNS-Hunting.md
│   ├── HTTP-Hunting.md
│   ├── TLS-Hunting.md
│   ├── Proxy-Logs.md
│   └── Network-Anomalies.md
│
├── 05-Identity-Hunting/
│   ├── Authentication-Hunting.md
│   ├── Credential-Attacks.md
│   ├── Privilege-Escalation.md
│   ├── Lateral-Movement.md
│   └── Account-Anomalies.md
│
├── 06-Cloud-Hunting/
│   ├── AWS.md
│   ├── Azure.md
│   ├── Google-Cloud.md
│   ├── IAM-Hunting.md
│   └── Cloud-Audit-Logs.md
│
├── 07-SIEM-Hunting/
│   ├── SIEM-Fundamentals.md
│   ├── Splunk.md
│   ├── Microsoft-Sentinel.md
│   ├── Elastic.md
│   ├── KQL.md
│   └── SPL.md
│
├── 08-Detection-Engineering/
│   ├── Detection-Lifecycle.md
│   ├── Detection-Rules.md
│   ├── Sigma.md
│   ├── YARA.md
│   └── Detection-Tuning.md
│
├── 09-Hunt-Playbooks/
│   ├── Credential-Stuffing.md
│   ├── PowerShell-Abuse.md
│   ├── Suspicious-DNS.md
│   ├── Lateral-Movement.md
│   ├── Persistence.md
│   ├── Data-Exfiltration.md
│   └── Cloud-Account-Compromise.md
│
├── 10-Threat-Hunting-Labs/
│   ├── Lab-01-Windows-Hunting/
│   ├── Lab-02-DNS-Hunting/
│   ├── Lab-03-PowerShell-Hunting/
│   ├── Lab-04-Identity-Hunting/
│   └── Lab-05-Cloud-Hunting/
│
├── 11-Queries/
│   ├── Splunk/
│   ├── KQL/
│   ├── Elastic/
│   ├── SQL/
│   └── Sigma/
│
├── 12-Case-Studies/
│   ├── Ransomware.md
│   ├── APT.md
│   ├── Credential-Theft.md
│   └── Supply-Chain-Attacks.md
│
└── 13-References/
    ├── Tools.md
    ├── Frameworks.md
    └── Resources.md
```

---

# Core Threat Hunting Framework

Every hunt in this repository should follow a consistent methodology.

## 1. Define the Objective

Clearly identify what you are looking for.

Example:

```text
Detect possible credential theft
from Windows endpoints.
```

---

## 2. Build a Hypothesis

Example:

```text
Hypothesis:

An attacker who has compromised a workstation
may attempt to access credential stores or
execute processes associated with credential theft.
```

---

## 3. Identify Required Telemetry

Determine what evidence is needed.

Possible sources:

* Windows Event Logs
* Sysmon
* EDR
* Authentication logs
* DNS logs
* Proxy logs
* Firewall logs
* Cloud audit logs
* Process telemetry

---

## 4. Search the Data

Use:

* SIEM queries
* EDR queries
* Network analytics
* Threat intelligence
* Statistical analysis

---

## 5. Investigate Anomalies

A suspicious event is not automatically malicious.

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

## 6. Validate the Hypothesis

Determine whether evidence supports or disproves the original hypothesis.

```text
Hypothesis

↓

Evidence

↓

Supported?

├── Yes → Investigate
│
└── No  → Refine Hunt
```

---

## 7. Create or Improve Detection

A successful hunt should ideally produce something reusable.

```text
Threat Hunt

↓

Interesting Behavior

↓

Detection Logic

↓

SIEM Rule

↓

Alert

↓

SOC Workflow
```

This turns one-time hunting into continuous defensive capability.

---

# Threat Hunting Data Sources

Effective hunting depends heavily on telemetry quality.

## Endpoint

* Process creation
* Command-line arguments
* File creation
* Registry activity
* Network connections
* Service creation
* Scheduled tasks
* PowerShell activity

## Network

* DNS
* HTTP
* HTTPS metadata
* Firewall
* Proxy
* NetFlow
* VPN

## Identity

* Login events
* Failed authentication
* MFA activity
* Account creation
* Privilege changes
* Group membership changes

## Cloud

* Cloud audit logs
* IAM events
* API activity
* Object storage access
* Security group changes
* Resource creation

---

# MITRE ATT&CK Integration

Threat hunting should be mapped to the **MITRE ATT&CK** framework.

Example:

```text
Threat Behavior

      ↓

MITRE ATT&CK Technique

      ↓

Required Telemetry

      ↓

Hunt Query

      ↓

Detection
```

ATT&CK mapping helps identify:

* Detection coverage
* Telemetry gaps
* Hunting opportunities
* Adversary behaviors
* Defensive priorities

---

# Threat Hunting vs SOC Monitoring

| SOC Monitoring                   | Threat Hunting                           |
| -------------------------------- | ---------------------------------------- |
| Alert-driven                     | Hypothesis-driven                        |
| Reactive                         | Proactive                                |
| Primarily detects known patterns | Searches for suspicious unknown activity |
| Continuous alert monitoring      | Focused investigations                   |
| Detection rules                  | Analytics + investigation                |
| Handles alerts                   | Searches beyond alerts                   |

A mature SOC needs both.

---

# Threat Hunting vs Incident Response

### Threat Hunting

```text
"What might be happening?"
```

### Incident Response

```text
"What happened and how do we contain it?"
```

They work together:

```text
Threat Hunt
     ↓
Suspicious Activity
     ↓
Incident
     ↓
Incident Response
     ↓
Lessons Learned
     ↓
New Detection
```

---

# Threat Hunting Toolset

This repository will cover tools and technologies commonly used in defensive security operations.

### SIEM

* Splunk
* Microsoft Sentinel
* Elastic Security

### Endpoint

* Microsoft Defender
* Sysmon
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

### Cloud

* AWS CloudTrail
* Microsoft Entra ID logs
* Azure Activity Logs
* Google Cloud Audit Logs

---

# Query Languages

Practical hunting queries will be documented for:

```text
SPL

KQL

EQL

SQL

Sigma
```

The goal is to understand the **logic behind the hunt**, rather than simply memorizing syntax.

---

# Hunt Documentation Standard

Every hunt should document:

```text
Hunt Name

Objective

Threat Hypothesis

MITRE ATT&CK Mapping

Required Data Sources

Hunt Logic

Query

Expected Results

False Positives

Investigation Steps

Evidence

Conclusion

Detection Opportunity

Recommendations
```

This creates professional, repeatable hunting documentation.

---

# Example Hunt

## Suspicious PowerShell Execution

### Hypothesis

```text
An attacker may use PowerShell to execute
commands after gaining access to a Windows endpoint.
```

### Telemetry

* Process creation
* PowerShell logs
* Command-line arguments
* Parent-child process relationships
* Network connections

### Investigation

```text
PowerShell Process

↓

Parent Process

↓

Command Line

↓

User

↓

Network Connections

↓

Related Events
```

### Outcome

If malicious behavior is confirmed:

```text
Threat Hunt

↓

Evidence

↓

Detection Rule

↓

SOC Alert
```

---

# Threat Hunting Maturity

A useful maturity progression is:

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

The goal is to progressively move from reactive investigation toward proactive, threat-informed defense.

---

# Repository Objectives

This repository aims to demonstrate practical capability in:

* Security Operations
* Threat Hunting
* Detection Engineering
* SIEM
* Incident Response
* MITRE ATT&CK
* Security Analytics
* Endpoint Detection
* Network Security
* Cloud Security

It is intended to demonstrate **how security professionals investigate threats**, not simply provide theoretical definitions.

---

# Learning Path

```text
01
Threat Hunting Fundamentals
        ↓
02
MITRE ATT&CK
        ↓
03
Endpoint Hunting
        ↓
04
Network Hunting
        ↓
05
Identity Hunting
        ↓
06
Cloud Hunting
        ↓
07
SIEM Hunting
        ↓
08
Detection Engineering
        ↓
09
Hunt Playbooks
        ↓
10
Practical Labs
        ↓
11
Hunting Queries
        ↓
12
Real-World Case Studies
```

---

# Recruiter-Focused Skills Demonstrated

This repository is designed to demonstrate practical familiarity with:

```text
Threat Hunting
Detection Engineering
SOC Operations
SIEM
MITRE ATT&CK
Incident Response
Digital Forensics
Windows Security
Linux Security
Network Security
Cloud Security
Security Analytics
KQL
SPL
Sigma
YARA
Threat Intelligence
```

---

# Ethical Use

All techniques and labs in this repository are intended for:

* Authorized security testing
* Defensive security research
* Threat hunting
* Detection engineering
* Cybersecurity education
* Isolated laboratory environments

Do not use the techniques documented here against systems, networks, accounts, or organizations without explicit authorization.

---

# Repository Philosophy

> **Don't just wait for alerts. Hunt for what the alerts missed.**

Effective threat hunting combines:

```text
Threat Intelligence
        +
Security Telemetry
        +
Adversary Knowledge
        +
Hypothesis
        +
Data Analysis
        +
Detection Engineering
```

The ultimate objective is not simply to find an attacker.

It is to continuously improve the organization's ability to:

```text
Prevent
   ↓
Detect
   ↓
Investigate
   ↓
Respond
   ↓
Learn
   ↓
Detect Better
```

---

# Recommended Next Topics

After this README, the repository will progressively cover:

1. **Threat Hunting Fundamentals**
2. **Threat Hunting Lifecycle**
3. **Hypothesis-Driven Hunting**
4. **MITRE ATT&CK for Hunters**
5. **Windows Threat Hunting**
6. **Linux Threat Hunting**
7. **PowerShell Threat Hunting**
8. **Network Threat Hunting**
9. **DNS Threat Hunting**
10. **Identity Threat Hunting**
11. **Cloud Threat Hunting**
12. **SIEM-Based Threat Hunting**
13. **Detection Engineering**
14. **Sigma Rules**
15. **YARA Rules**
16. **Threat Hunting Playbooks**
17. **Practical Hunting Labs**
18. **Real-World Threat Hunting Case Studies**

---

## Status

🚧 **Active Development**

This repository is continuously expanded with new hunting methodologies, detection queries, investigation workflows, practical labs, and security case studies.

---

## Disclaimer

This repository is intended for educational and defensive cybersecurity purposes.

All practical testing should be performed only against systems and environments for which you have explicit authorization.

---

## Author

**Anurag**

Cybersecurity | Threat Hunting | Detection Engineering | SOC | VAPT

---

## ⭐ Contributing

Contributions that improve technical accuracy, detection coverage, defensive guidance, and educational value are welcome.

Please review the repository contribution guidelines before submitting changes.
