# MITRE ATT&CK for Threat Hunters

## Overview

**MITRE ATT&CK** is a globally used knowledge base of adversary behaviors based on real-world observations.

ATT&CK organizes attacker behavior into:

- Tactics
- Techniques
- Sub-techniques
- Procedures
- Groups
- Software
- Campaigns
- Data Sources
- Data Components

For threat hunters, ATT&CK provides a common language for answering questions such as:

> What is the attacker trying to accomplish?

> How could the attacker perform it?

> What evidence would that behavior leave behind?

> What telemetry should we search?

> Do we have a detection for it?

A simplified threat-hunting workflow is:

```text
                 Threat Intelligence
                         │
                         ▼
                  ATT&CK Technique
                         │
                         ▼
                  Hunt Hypothesis
                         │
                         ▼
                 Required Telemetry
                         │
                         ▼
                    Hunt Query
                         │
                         ▼
                    Evidence
                         │
                         ▼
                   Investigation
                         │
                         ▼
                  Detection Rule
                         │
                         ▼
                Coverage Improvement
```

---

# 1. What Is MITRE ATT&CK?

MITRE ATT&CK stands for:

> **Adversarial Tactics, Techniques, and Common Knowledge**

It is maintained by **MITRE**, a nonprofit organization that develops research and knowledge resources for cybersecurity and other technical domains.

ATT&CK documents how adversaries operate rather than simply listing malware signatures.

For example, instead of saying:

```text
Malware:
example-malware.exe
```

ATT&CK focuses on behavior:

```text
Command and Scripting Interpreter
        ↓
PowerShell
        ↓
Execution
```

This behavioral approach makes ATT&CK particularly useful for threat hunting and detection engineering.

---

# 2. Why ATT&CK Matters to Threat Hunters

Threat hunting often starts with incomplete information.

A hunter may know:

```text
An attacker is believed to be targeting
Windows endpoints.
```

ATT&CK helps expand that into possible behaviors:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command and Control
      ↓
Exfiltration
      ↓
Impact
```

The hunter can then ask:

```text
What techniques could support each stage?

What telemetry would those techniques generate?

Do we collect that telemetry?

Can we detect it?

Can we hunt it?
```

---

# 3. ATT&CK Core Concepts

The most important concepts for hunters are:

```text
Tactics
   ↓
Techniques
   ↓
Sub-Techniques
   ↓
Procedures
   ↓
Telemetry
   ↓
Detection
```

Let's examine each one.

---

# 4. Tactics

A **tactic** represents the adversary's high-level objective.

Examples include:

- Reconnaissance
- Resource Development
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Command and Control
- Exfiltration
- Impact

The important distinction is:

> **Tactic = Why the attacker is doing something.**

Example:

```text
Attacker Objective
        ↓
Credential Access
```

The attacker wants credentials.

---

# 5. Techniques

A **technique** describes how an attacker can accomplish a tactical objective.

Example:

```text
Tactic:
Credential Access

Technique:
OS Credential Dumping
```

Another example:

```text
Tactic:
Execution

Technique:
Command and Scripting Interpreter
```

Therefore:

```text
Tactic
  = Why

Technique
  = How
```

---

# 6. Sub-Techniques

Sub-techniques provide additional detail.

For example:

```text
T1059
Command and Scripting Interpreter
        │
        ├── T1059.001 PowerShell
        ├── T1059.002 AppleScript
        ├── T1059.003 Windows Command Shell
        ├── T1059.004 Unix Shell
        └── ...
```

This level is particularly useful for threat hunters because telemetry requirements can vary significantly between sub-techniques.

---

# 7. Procedures

A **procedure** describes how a particular threat actor or piece of software has been observed implementing a technique.

Conceptually:

```text
Technique
    ↓
Observed Adversary
    ↓
Actual Procedure
```

For example:

```text
Technique:
PowerShell

Procedure:
Threat actor executes PowerShell commands
to download and execute a payload.
```

Procedures make ATT&CK more practical because they connect abstract techniques to observed adversary behavior.

---

# 8. ATT&CK Relationship Model

A simplified relationship is:

```text
Threat Actor
     │
     ▼
Uses Software
     │
     ▼
Performs Procedure
     │
     ▼
Uses Technique
     │
     ▼
Achieves Tactical Objective
```

Example:

```text
Threat Actor
     ↓
PowerShell
     ↓
Encoded Command
     ↓
T1059.001
     ↓
Execution
```

---

# 9. Enterprise ATT&CK

For enterprise threat hunting, the **Enterprise ATT&CK** knowledge base is particularly important.

It covers adversary behavior across environments such as:

- Windows
- Linux
- macOS
- Cloud
- Containers
- Identity systems
- Enterprise applications

This makes it highly relevant to modern SOC environments.

---

# 10. ATT&CK Tactics

A threat hunter should understand the major Enterprise tactics.

## Reconnaissance

The adversary gathers information before attempting an attack.

Examples:

- Target identification
- Organization information gathering
- Vulnerability research
- Search engine discovery

---

## Resource Development

The adversary prepares infrastructure and resources.

Examples:

- Domains
- Servers
- Accounts
- Malware
- Staging infrastructure

---

## Initial Access

The attacker attempts to gain an initial foothold.

Examples:

- Phishing
- Exploitation of public-facing applications
- Valid accounts
- External remote services

---

## Execution

The attacker executes malicious code or commands.

Examples:

- PowerShell
- Command shell
- Scripting
- User execution
- Scheduled execution

---

## Persistence

The attacker attempts to maintain access.

Examples:

- Scheduled tasks
- Services
- Startup items
- Account manipulation
- Registry Run Keys

---

## Privilege Escalation

The attacker attempts to obtain higher privileges.

Examples:

- Exploitation
- Token manipulation
- Misconfigured permissions
- Valid privileged accounts

---

## Defense Evasion

The attacker attempts to avoid detection.

Examples:

- Obfuscated files
- Indicator removal
- Masquerading
- Impairing defenses
- Process injection

---

## Credential Access

The attacker attempts to obtain credentials.

Examples:

- Credential dumping
- Password stores
- Kerberos attacks
- Input capture
- Credentials from files

---

## Discovery

The attacker learns about the environment.

Examples:

- System information
- Account discovery
- Network discovery
- Process discovery
- Domain trust discovery

---

## Lateral Movement

The attacker moves from one system to another.

Examples:

- Remote services
- SMB
- RDP
- WinRM
- SSH
- Pass-the-Hash

---

## Collection

The attacker gathers useful information.

Examples:

- Files
- Email
- Screenshots
- Clipboard
- Browser data

---

## Command and Control

The attacker communicates with compromised infrastructure.

Examples:

- Application layer protocols
- Web protocols
- DNS
- Encrypted channels
- Proxy-aware communication

---

## Exfiltration

The attacker removes data from the environment.

Examples:

- Exfiltration over web service
- Automated exfiltration
- Exfiltration over C2 channel

---

## Impact

The attacker attempts to disrupt or manipulate systems.

Examples:

- Data destruction
- Data encryption
- Service disruption
- Resource hijacking

---

# 11. ATT&CK as a Threat Hunting Framework

ATT&CK should not simply be treated as a list of techniques.

A hunter can use ATT&CK to create an investigation workflow.

```text
ATT&CK Technique
       ↓
Threat Hypothesis
       ↓
Expected Behavior
       ↓
Required Telemetry
       ↓
Hunt Query
       ↓
Evidence
       ↓
Detection
```

---

# 12. Example: PowerShell Hunting

Suppose threat intelligence indicates that an adversary frequently uses PowerShell.

ATT&CK mapping:

```text
Tactic:
Execution

Technique:
T1059

Sub-Technique:
T1059.001 — PowerShell
```

The hunter can formulate:

> A compromised Windows endpoint may execute PowerShell commands that are unusual for the associated user or host.

Required telemetry:

- Process creation
- Command line
- Parent process
- User
- Host
- PowerShell operational logs
- Network connections

Hunt workflow:

```text
PowerShell Event
       ↓
Command Line
       ↓
Parent Process
       ↓
User
       ↓
Destination
       ↓
Related Events
```

---

# 13. ATT&CK Data Sources

ATT&CK can help determine what evidence may be required for a particular technique.

Examples of useful telemetry include:

### Process

- Process creation
- Process termination
- Parent-child relationships
- Command-line arguments

### Network

- Network connections
- DNS queries
- Proxy connections
- Firewall events

### Authentication

- Logons
- Authentication attempts
- Account changes
- Privilege changes

### Files

- File creation
- File modification
- File deletion

### Registry

- Registry modification
- Registry queries

### Cloud

- API activity
- IAM events
- Resource changes

---

# 14. Data Source vs Data Component

This distinction is important.

A **data source** represents a broad category of telemetry.

A **data component** provides more specific observable information within that source.

Conceptually:

```text
Data Source
    │
    ├── Data Component
    ├── Data Component
    └── Data Component
```

Example:

```text
Process

├── Process Creation
├── Process Termination
└── Process Metadata
```

For threat hunters, this helps answer:

> Do we actually collect the telemetry required to hunt this technique?

---

# 15. ATT&CK-Based Hunt Hypothesis

A strong hypothesis can be created directly from ATT&CK.

Example:

```text
ATT&CK:
T1059.001 PowerShell

        ↓

Threat Scenario:
Attacker executes commands through PowerShell

        ↓

Hypothesis:
A compromised endpoint may execute unusual
PowerShell commands from uncommon parent processes.

        ↓

Telemetry:
Process + Command Line + User + Host

        ↓

Hunt
```

This creates a repeatable process.

---

# 16. ATT&CK-Based Hunting Methodology

Use the following workflow:

```text
01. Select Technique
        ↓
02. Understand Adversary Behavior
        ↓
03. Define Hypothesis
        ↓
04. Identify Data Sources
        ↓
05. Identify Data Components
        ↓
06. Develop Hunt Query
        ↓
07. Search Historical Data
        ↓
08. Investigate Results
        ↓
09. Validate Activity
        ↓
10. Map Findings
        ↓
11. Create Detection
        ↓
12. Measure Coverage
```

---

# 17. Hunting From Threat Intelligence

Threat intelligence can provide:

```text
Threat Actor
     ↓
Known Techniques
     ↓
ATT&CK Mapping
     ↓
Potential Behaviors
     ↓
Hunt Hypotheses
```

Example:

```text
Threat Actor
     ↓
PowerShell
     ↓
Credential Dumping
     ↓
Remote Services
     ↓
Data Collection
```

Instead of searching only for the actor's known IP addresses, hunt for their known behaviors.

---

# 18. IOC Hunting vs ATT&CK Hunting

## IOC Hunting

```text
Known IP
Known Domain
Known Hash
```

Advantages:

- Fast
- Easy to operationalize
- Useful for known threats

Limitations:

- Easily changed
- Infrastructure can rotate
- Poor visibility into unknown variants

---

## ATT&CK-Based Hunting

```text
Behavior
   ↓
Technique
   ↓
Telemetry
   ↓
Detection
```

Advantages:

- More resilient
- Behavior-focused
- Useful for unknown variants
- Supports detection engineering

---

# 19. Example: Credential Dumping Hunt

Suppose intelligence indicates that an attacker may perform credential dumping.

ATT&CK:

```text
T1003
OS Credential Dumping
```

Possible hypothesis:

> An attacker with elevated privileges may attempt to access credential material from protected operating-system processes.

Potential telemetry:

- Process creation
- Process access
- Security events
- EDR telemetry
- Privilege changes

Investigation:

```text
Suspicious Process
      ↓
Target Process
      ↓
Access Rights
      ↓
User Context
      ↓
Parent Process
      ↓
Network Activity
```

The goal is to identify whether the behavior is legitimate administrative activity or malicious credential access.

---

# 20. Example: Lateral Movement Hunt

Possible technique:

```text
Remote Services
```

Hypothesis:

> A compromised account may authenticate to multiple internal systems that it does not normally access.

Telemetry:

- Authentication logs
- Windows events
- VPN
- EDR
- Network flows
- Active Directory

Hunt:

```text
User
 ↓
Source Host
 ↓
Destination Host
 ↓
Authentication
 ↓
Frequency
 ↓
Time
 ↓
Subsequent Activity
```

---

# 21. ATT&CK Navigator

**ATT&CK Navigator** is a visualization tool that can be used to represent ATT&CK techniques.

A security team can highlight:

- Techniques used by an adversary
- Detection coverage
- Hunting coverage
- Gaps
- Priority techniques

Conceptually:

```text
             ATT&CK Matrix

Initial Access      ███
Execution           █████
Persistence         ██
Credential Access   █████
Discovery           ████
Lateral Movement    █████
C2                  ███
Exfiltration        ██
```

This makes security coverage easier to communicate.

---

# 22. Detection Coverage

One of the most useful applications of ATT&CK is measuring detection coverage.

For each technique, ask:

```text
Can we detect it?

Can we hunt it?

What telemetry supports it?

How reliable is the detection?

Has it been tested?
```

Example:

| Technique | Telemetry | Detection | Hunt | Coverage |
|---|---|---|---|---|
| PowerShell | Process + PowerShell logs | Yes | Yes | High |
| Credential Dumping | EDR | Partial | Yes | Medium |
| DNS Tunneling | DNS | No | Yes | Low |
| RDP | Authentication + network | Yes | Yes | High |

---

# 23. Detection Gap Analysis

ATT&CK can expose gaps.

```text
Technique
    ↓
Required Telemetry
    ↓
Telemetry Available?
       │
   ┌───┴───┐
   │       │
  Yes      No
   │       │
   ▼       ▼
Detection  Telemetry
          Improvement
```

This is extremely important for security engineering.

---

# 24. Hunt Coverage vs Detection Coverage

These should not be confused.

### Detection Coverage

Can the security system automatically identify the behavior?

### Hunt Coverage

Can an analyst manually search for the behavior?

Example:

```text
Technique:
DNS Tunneling

Detection:
No

Telemetry:
Yes

Hunt:
Yes
```

This means the organization can investigate the behavior but does not yet have reliable automated detection.

---

# 25. ATT&CK and Detection Engineering

Threat hunting frequently produces detection opportunities.

```text
ATT&CK Technique
       ↓
Hunt
       ↓
Observed Behavior
       ↓
Detection Logic
       ↓
Sigma Rule
       ↓
SIEM
       ↓
Alert
```

A mature organization therefore connects:

```text
Threat Intelligence
        +
ATT&CK
        +
Threat Hunting
        +
Detection Engineering
        +
SOC
```

---

# 26. ATT&CK and SIEM

SIEM platforms can use ATT&CK mappings to classify detections.

Example:

```text
SIEM Alert

Suspicious PowerShell

        ↓

MITRE ATT&CK

T1059.001

        ↓

Tactic

Execution
```

This helps SOC analysts understand the potential stage of an attack.

---

# 27. ATT&CK and EDR

EDR telemetry is particularly useful for hunting endpoint techniques.

Example:

```text
Process Tree

explorer.exe
     │
     └── powershell.exe
             │
             └── rundll32.exe
                     │
                     └── network connection
```

A hunter can map suspicious behaviors to ATT&CK techniques.

Possible investigation:

```text
PowerShell
    ↓
Execution

Rundll32
    ↓
Signed Binary Proxy Execution

Network Connection
    ↓
Command and Control
```

---

# 28. ATT&CK and Threat Intelligence

Threat intelligence becomes significantly more useful when mapped to ATT&CK.

Instead of:

```text
APT Group
IP: X.X.X.X
Domain: example.com
Hash: abc123
```

A richer intelligence model is:

```text
APT Group
   │
   ├── Initial Access
   ├── PowerShell
   ├── Credential Access
   ├── Discovery
   ├── Lateral Movement
   └── Command and Control
```

The security team can then hunt for behavior rather than relying only on static indicators.

---

# 29. ATT&CK and Threat Actor Profiling

Threat actor profiles can be represented as technique collections.

Example:

```text
Threat Actor
     │
     ├── T1566
     │     Phishing
     │
     ├── T1059.001
     │     PowerShell
     │
     ├── T1003
     │     Credential Dumping
     │
     ├── T1021
     │     Remote Services
     │
     └── T1071
           Application Layer Protocol
```

A hunter can prioritize hunts based on the techniques associated with relevant adversaries.

---

# 30. ATT&CK-Based Threat Hunting Example

## Scenario

A financial organization is concerned about ransomware.

### Step 1 — Threat Intelligence

Known ransomware operations commonly use:

- Phishing
- PowerShell
- Credential access
- Remote services
- Discovery
- Data collection
- Data destruction/encryption

### Step 2 — ATT&CK Mapping

```text
Initial Access
       ↓
Execution
       ↓
Credential Access
       ↓
Discovery
       ↓
Lateral Movement
       ↓
Collection
       ↓
Impact
```

### Step 3 — Hunt Hypotheses

Examples:

```text
H1:
Unusual PowerShell execution may indicate
initial execution.

H2:
Privileged credential access may indicate
preparation for lateral movement.

H3:
Rapid remote authentication across multiple
hosts may indicate lateral movement.

H4:
Unusual file modification at scale may indicate
ransomware activity.
```

### Step 4 — Telemetry

Collect:

```text
Windows Events
Sysmon
EDR
Authentication
DNS
Network
File Activity
```

### Step 5 — Investigation

Correlate:

```text
User
 +
Host
 +
Process
 +
Network
 +
Authentication
 +
File Activity
```

---

# 31. ATT&CK-Based Hunt Chain

Threat hunters should think in terms of attack chains rather than isolated events.

```text
Phishing
   ↓
User Execution
   ↓
PowerShell
   ↓
Credential Access
   ↓
Discovery
   ↓
Remote Services
   ↓
Lateral Movement
   ↓
Data Collection
   ↓
Exfiltration / Impact
```

If one stage is missed, another stage may provide useful evidence.

This is why **cross-technique correlation** is important.

---

# 32. Technique Chaining

Individual behaviors may be ambiguous.

For example:

```text
PowerShell
```

could be legitimate.

But:

```text
PowerShell
    +
Encoded Command
    +
Rare Parent Process
    +
External Connection
    +
New Scheduled Task
```

is significantly more suspicious.

Technique chaining increases confidence.

---

# 33. ATT&CK-Based Correlation

A useful hunting model is:

```text
Technique A
     +
Technique B
     +
Technique C
     ↓
Higher Confidence
```

Example:

```text
T1059.001
PowerShell

      +

T1082
System Information Discovery

      +

T1046
Network Service Scanning

      ↓

Potential Post-Compromise Activity
```

The individual techniques may have legitimate uses.

Their sequence and context can make the activity suspicious.

---

# 34. ATT&CK and the Cyber Kill Chain

MITRE ATT&CK and the Cyber Kill Chain are related but different models.

### Cyber Kill Chain

Provides a high-level attack progression.

```text
Reconnaissance
↓
Weaponization
↓
Delivery
↓
Exploitation
↓
Installation
↓
Command & Control
↓
Actions on Objectives
```

### MITRE ATT&CK

Provides much greater behavioral detail.

```text
Tactic
 ↓
Technique
 ↓
Sub-Technique
 ↓
Procedure
```

A security team can use both frameworks together.

---

# 35. ATT&CK and the Pyramid of Pain

The Pyramid of Pain illustrates the increasing difficulty attackers face when defenders detect higher-level adversary characteristics.

```text
            TTPs
           /────\
          /      \
        Tools
       /────────\
      Network / Host
     Artifacts
    /────────────\
   Domain Names
  /──────────────\
 IP Addresses
/────────────────\
Hash Values
```

Low-level indicators are easier for attackers to replace.

Higher-level behaviors and TTPs are generally more difficult to change.

This reinforces the value of behavior-focused hunting.

---

# 36. ATT&CK-Based Hunt Prioritization

Not every technique deserves equal hunting effort.

Prioritize based on:

### Threat Relevance

Is the technique used by relevant adversaries?

### Business Impact

Could exploitation cause significant damage?

### Exposure

Are affected systems internet-facing or highly privileged?

### Telemetry

Can the organization actually observe the behavior?

### Detection Gap

Is there currently weak or missing detection?

### Likelihood

How realistic is the attack scenario?

A practical prioritization model:

```text
Priority =
Threat Relevance
+
Business Impact
+
Exposure
+
Detection Gap
+
Feasibility
```

---

# 37. ATT&CK Coverage Matrix

A simple internal matrix can track security capabilities.

| ATT&CK Technique | Telemetry | Hunt | Detection | Tested |
|---|---:|---:|---:|---:|
| PowerShell | ✅ | ✅ | ✅ | ✅ |
| Credential Dumping | ✅ | ✅ | ⚠️ | ⚠️ |
| Network Service Scanning | ✅ | ✅ | ❌ | ⚠️ |
| Remote Services | ✅ | ✅ | ✅ | ✅ |
| DNS Tunneling | ✅ | ✅ | ❌ | ❌ |
| Scheduled Task | ✅ | ✅ | ✅ | ✅ |

Legend:

```text
✅ Covered
⚠️ Partial
❌ Missing
```

This is useful for security program maturity assessments.

---

# 38. Practical Hunt: PowerShell

## Objective

Identify potentially suspicious PowerShell execution.

## ATT&CK

```text
T1059.001
PowerShell
```

## Hypothesis

> An attacker may use PowerShell to execute commands on a compromised Windows endpoint.

## Telemetry

- Process creation
- Command line
- PowerShell logs
- Parent process
- User
- Host
- Network activity

## Investigation

Look for combinations such as:

```text
powershell.exe

+

Encoded command

+

Unusual parent

+

External connection
```

## Validation

Determine:

- Was the user authorized?
- Was there a maintenance window?
- Is the parent process expected?
- What command executed?
- Did the process connect externally?
- What happened afterward?

## Detection Opportunity

A validated malicious pattern can become:

```text
Sigma Rule
     ↓
SIEM Rule
     ↓
EDR Detection
```

---

# 39. Practical Hunt: Lateral Movement

## Objective

Identify potential lateral movement.

## Hypothesis

> A compromised account may authenticate to multiple internal systems in a short period of time.

## Telemetry

- Authentication events
- Windows Security logs
- Active Directory
- EDR
- Network flows

## Investigation

```text
User
 ↓
Source
 ↓
Destination
 ↓
Authentication Type
 ↓
Time
 ↓
Frequency
```

Look for:

- Unusual destination hosts
- Administrative authentication
- Rare source devices
- Multiple systems accessed rapidly
- Activity outside normal hours

---

# 40. Practical Hunt: Suspicious DNS

## ATT&CK Context

DNS can be abused for command-and-control and data transfer.

## Hypothesis

> A compromised endpoint may communicate with an attacker-controlled infrastructure through abnormal DNS activity.

## Telemetry

- DNS queries
- Query frequency
- Domain age/reputation
- Query length
- NXDOMAIN responses
- Client host

## Investigation

Look for:

```text
High Query Volume
       +
Long Random-Looking Domains
       +
Rare Destination
       +
Periodic Timing
```

This does not automatically prove DNS tunneling.

Context and additional evidence are required.

---

# 41. ATT&CK-Based Threat Hunting Checklist

Before a hunt:

```text
[ ] Define threat scenario
[ ] Select ATT&CK technique
[ ] Understand technique behavior
[ ] Create hypothesis
[ ] Identify telemetry
[ ] Check data availability
[ ] Define hunt logic
```

During the hunt:

```text
[ ] Search historical data
[ ] Establish baseline
[ ] Identify anomalies
[ ] Correlate events
[ ] Investigate context
[ ] Map findings
```

After the hunt:

```text
[ ] Validate findings
[ ] Document evidence
[ ] Record false positives
[ ] Identify telemetry gaps
[ ] Create detection opportunities
[ ] Update ATT&CK coverage
[ ] Share lessons learned
```

---

# 42. Common Mistakes

## Treating ATT&CK as a Checklist

Bad approach:

```text
Complete every technique
```

Better approach:

```text
Prioritize techniques relevant to
your environment and threat model.
```

---

## Mapping Everything to ATT&CK

Not every event needs an ATT&CK mapping.

Use ATT&CK when it adds analytical or operational value.

---

## Confusing Technique With Detection

A technique describes adversary behavior.

A detection describes how you identify that behavior.

```text
Technique
   ≠
Detection
```

---

## Ignoring Telemetry

You cannot reliably hunt a technique if the required telemetry is unavailable.

---

## Hunting Only One Technique

Attackers use multiple techniques.

Correlating techniques often produces stronger evidence.

---

## Assuming ATT&CK Mapping Proves Maliciousness

ATT&CK techniques can describe legitimate administrative behavior.

For example:

```text
PowerShell
```

is not inherently malicious.

Context determines risk.

---

# 43. Best Practices

- Use ATT&CK as a behavioral knowledge base.
- Start hunts with realistic threat scenarios.
- Build explicit hypotheses.
- Map relevant techniques and sub-techniques.
- Identify required telemetry before writing queries.
- Hunt across multiple data sources.
- Correlate related techniques.
- Maintain an ATT&CK coverage matrix.
- Distinguish hunt coverage from detection coverage.
- Prioritize techniques based on risk.
- Test detections with realistic activity.
- Document false positives.
- Convert successful hunts into detections.
- Track telemetry gaps.
- Revisit coverage as the environment changes.

---

# 44. Interview Questions

## Beginner

### What is MITRE ATT&CK?

MITRE ATT&CK is a knowledge base that documents adversary tactics, techniques, sub-techniques, and observed procedures based on real-world behavior.

---

### What is a tactic?

A tactic represents an adversary's high-level objective.

Example:

```text
Credential Access
```

---

### What is a technique?

A technique describes how an adversary may accomplish a tactical objective.

---

### What is a sub-technique?

A sub-technique provides a more specific implementation of a parent technique.

---

### What is a procedure?

A procedure describes how a specific threat actor or software has been observed implementing a technique.

---

## Intermediate

### How does ATT&CK help threat hunters?

It helps hunters translate adversary behavior into hunt hypotheses, identify relevant telemetry, develop queries, map findings, and measure detection coverage.

---

### What is ATT&CK data source information used for?

It helps identify the types of security telemetry that can provide evidence for particular adversary techniques.

---

### How would you create a hunt from an ATT&CK technique?

```text
Technique
 ↓
Understand Behavior
 ↓
Threat Scenario
 ↓
Hypothesis
 ↓
Telemetry
 ↓
Query
 ↓
Investigation
 ↓
Detection
```

---

### What is ATT&CK coverage?

ATT&CK coverage describes how effectively an organization can observe, hunt, detect, or respond to adversary techniques.

---

## Advanced

### What is the difference between detection coverage and hunt coverage?

Detection coverage indicates whether automated controls can identify a technique.

Hunt coverage indicates whether analysts have sufficient telemetry and methodology to manually investigate that technique.

---

### Why should threat hunters focus on techniques instead of only IOCs?

IOCs can change rapidly. Techniques and behaviors are generally more stable and therefore provide more durable hunting opportunities.

---

### How can ATT&CK help identify telemetry gaps?

For each prioritized technique, security teams can determine which data sources and data components are required. If those telemetry sources are unavailable, the organization has an observability gap.

---

### How would you measure ATT&CK-based detection maturity?

Consider:

- Technique coverage
- Telemetry availability
- Detection quality
- Hunt coverage
- Detection testing
- False-positive rate
- Detection response capability
- Time to detect
- Time to investigate

---

# 45. Practical Exercise

## Scenario

You are a threat hunter at an enterprise organization.

Threat intelligence indicates that an adversary commonly uses:

```text
PowerShell
Credential Access
Remote Services
Network Discovery
```

Your environment contains:

```text
Windows Endpoints
Active Directory
EDR
SIEM
DNS Logs
Firewall Logs
```

### Task

Create a hunt plan.

### Step 1

Map each behavior to ATT&CK.

### Step 2

Create hypotheses.

### Step 3

Identify required telemetry.

### Step 4

Develop queries.

### Step 5

Search historical data.

### Step 6

Correlate findings.

### Step 7

Determine whether activity is malicious.

### Step 8

Identify detection gaps.

### Step 9

Create detection recommendations.

### Step 10

Document the investigation.

---

# 46. Hunt Report Template

```markdown
# Threat Hunt Report

## Hunt Name

## Date

## Analyst

## Threat Scenario

## Threat Hypothesis

## MITRE ATT&CK Mapping

### Tactic

### Technique

### Sub-Technique

## Data Sources

## Required Telemetry

## Hunt Queries

## Findings

## Investigation Timeline

## Evidence

## False Positives

## Conclusion

## Detection Gap

## Detection Recommendation

## Telemetry Recommendation

## Risk Assessment

## Lessons Learned

## References
```

---

# 47. ATT&CK-to-Hunt Mapping

The core relationship to remember is:

```text
                 MITRE ATT&CK
                      │
                      ▼
                 Tactic
                      │
                      ▼
                Technique
                      │
                      ▼
              Sub-Technique
                      │
                      ▼
              Adversary Behavior
                      │
                      ▼
               Hunt Hypothesis
                      │
                      ▼
                 Telemetry
                      │
                      ▼
                  Query
                      │
                      ▼
                Investigation
                      │
                      ▼
                 Detection
```

This is the central methodology for using ATT&CK as a threat hunter.

---

# 48. Chapter Summary

MITRE ATT&CK provides threat hunters with a structured language for understanding adversary behavior.

The most important concepts are:

```text
Tactic
   ↓
Technique
   ↓
Sub-Technique
   ↓
Procedure
```

For threat hunting, this becomes:

```text
ATT&CK
  ↓
Threat Scenario
  ↓
Hypothesis
  ↓
Telemetry
  ↓
Hunt
  ↓
Evidence
  ↓
Detection
```

The goal is not to achieve a visually impressive ATT&CK coverage percentage.

The goal is to determine:

> **Can we observe, investigate, detect, and respond to the adversary behaviors that matter to our organization?**

A mature threat hunting program therefore combines:

```text
MITRE ATT&CK
       +
Threat Intelligence
       +
Security Telemetry
       +
Threat Hunting
       +
Detection Engineering
       +
Incident Response
```

The result is a continuous defensive feedback loop:

```text
Threat Intelligence
        ↓
ATT&CK
        ↓
Hunt
        ↓
Discovery
        ↓
Detection
        ↓
Validation
        ↓
Improved Coverage
        ↓
Better Hunting
```

---

# References

- MITRE ATT&CK — https://attack.mitre.org/
- MITRE ATT&CK Enterprise — https://attack.mitre.org/matrices/enterprise/
- MITRE ATT&CK Data Sources — https://attack.mitre.org/datasources/
- MITRE ATT&CK Navigator — https://mitre-attack.github.io/attack-navigator/
- MITRE ATT&CK Groups — https://attack.mitre.org/groups/
- MITRE ATT&CK Software — https://attack.mitre.org/software/
- MITRE Center for Threat-Informed Defense — https://ctid.mitre.org/
- CISA — https://www.cisa.gov/
- NIST Cybersecurity Framework — https://www.nist.gov/cyberframework

---

