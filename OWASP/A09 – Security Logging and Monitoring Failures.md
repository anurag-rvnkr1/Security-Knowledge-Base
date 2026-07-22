# A09:2021 – Security Logging and Monitoring Failures

---

# Overview

Security controls are only effective if organizations can detect when they fail.

Many organizations successfully prevent thousands of attacks every day, but even the strongest defenses cannot stop every threat. When prevention fails, **logging and monitoring become the primary mechanisms for detecting, investigating, and responding to security incidents**.

OWASP A09 addresses failures related to:

- Missing security logs
- Insufficient audit trails
- Poor monitoring
- Delayed incident detection
- Missing alerts
- Log tampering
- Inadequate incident visibility

Without effective logging and monitoring, organizations may remain unaware of an attack for days, weeks, or even months.

---

# Why It Matters

Consider two organizations.

### Organization A

```
Attacker

↓

Compromises Account

↓

No Logging

↓

No Alerts

↓

Data Exfiltration

↓

Incident Discovered Months Later
```

---

### Organization B

```
Attacker

↓

Compromises Account

↓

Authentication Logged

↓

SIEM Detects Anomaly

↓

SOC Alert

↓

Incident Response Begins
```

Both organizations were attacked.

Only one detected the attack in time.

---

# Security Monitoring Architecture

```
Users

↓

Applications

↓

Operating Systems

↓

Network Devices

↓

Cloud Services

↓

Log Collection

↓

SIEM Platform

↓

Detection Rules

↓

Alerts

↓

SOC Analysts

↓

Incident Response
```

Every layer contributes valuable security telemetry.

---

# What is Logging?

Logging is the process of recording events that occur within systems or applications.

Examples include:

- User logins
- Failed authentication
- File access
- API requests
- Administrative actions
- Errors
- Security events
- System changes

Logs provide a historical record of system activity.

---

# What is Monitoring?

Monitoring is the continuous observation and analysis of logs and other telemetry to identify unusual or malicious behavior.

Logging records events.

Monitoring interprets them.

```
Logging

↓

Store Events

↓

Monitoring

↓

Analyze Events

↓

Detect Threats
```

---

# Security Logging vs Application Logging

| Application Logging | Security Logging |
|---------------------|------------------|
| Debugging | Threat detection |
| Performance | Incident investigation |
| Errors | Authentication events |
| Business metrics | Privilege changes |
| Feature usage | Administrative actions |

Many organizations maintain both types of logs because they serve different purposes.

---

# Why Security Logs Matter

Security logs enable organizations to:

- Detect attacks
- Investigate incidents
- Reconstruct attacker activity
- Meet compliance requirements
- Support forensic investigations
- Improve detection rules
- Identify insider threats
- Monitor privileged users

Without reliable logs, determining what happened during an incident becomes significantly more difficult.

---

# The Logging Lifecycle

```
Security Event

↓

Generate Log

↓

Collect

↓

Normalize

↓

Store

↓

Analyze

↓

Alert

↓

Investigate

↓

Archive
```

Each stage must preserve log integrity and availability.

---

# Common Log Sources

```
Enterprise Environment

├── Web Applications
├── API Gateways
├── Databases
├── Operating Systems
├── Firewalls
├── IDS/IPS
├── VPN Gateways
├── Active Directory
├── Cloud Platforms
├── Containers
├── Kubernetes
├── Email Systems
├── Endpoint Detection Platforms
└── Authentication Services
```

Collecting logs from multiple sources improves visibility across the environment.

---

# Security Events Worth Logging

Organizations should log security-relevant events such as:

## Authentication

- Successful logins
- Failed logins
- MFA enrollment
- MFA failures
- Password resets
- Account lockouts

---

## Authorization

- Privilege changes
- Role assignments
- Access denials
- Administrative actions

---

## User Activity

- Account creation
- Account deletion
- Profile updates
- Sensitive data access
- File downloads
- File uploads

---

## Application Events

- API requests
- Input validation failures
- Security exceptions
- Unexpected errors
- Configuration changes

---

## Infrastructure Events

- Server startup
- Server shutdown
- Service failures
- Network changes
- Firewall modifications
- DNS changes

---

## Cloud Events

- IAM changes
- Storage bucket policy updates
- Security group changes
- Resource creation
- Resource deletion
- API key generation

---

# Log Components

A security log should contain sufficient context for investigation.

Typical fields include:

```
Timestamp

User

Source IP

Destination

Event Type

Resource

Action

Status

Request ID

Session ID
```

Additional fields may include device identifiers, geolocation, or correlation IDs depending on the environment.

---

# Example Authentication Log

```
Timestamp:

2026-08-15 10:42:31 UTC

User:

alice@example.com

IP:

203.0.113.42

Action:

Login

Result:

Success

MFA:

Completed
```

This provides enough information to investigate future authentication-related incidents.

---

# Structured vs Unstructured Logs

### Structured Logs

Example (JSON):

```json
{
  "timestamp": "2026-08-15T10:42:31Z",
  "user": "alice@example.com",
  "event": "login",
  "result": "success"
}
```

Advantages:

- Easier to search
- Easier to parse
- Better SIEM integration
- Consistent formatting

---

### Unstructured Logs

Example:

```
User Alice successfully logged in.
```

While human-readable, unstructured logs are more difficult to search and correlate at scale.

---

# Log Levels

Applications commonly categorize log events by severity.

| Level | Purpose |
|--------|----------|
| DEBUG | Detailed troubleshooting information |
| INFO | Normal operational events |
| WARNING | Unexpected but non-critical conditions |
| ERROR | Operation failed |
| CRITICAL / FATAL | Severe failure requiring immediate attention |

Production environments should avoid excessive DEBUG logging unless required for troubleshooting, as it can expose sensitive information and increase storage costs.

---

# Log Correlation

A single attack often generates events across multiple systems.

Example:

```
VPN Login

↓

Web Login

↓

Database Query

↓

Privilege Escalation

↓

Large File Download
```

Individually, each event may appear benign.

Correlated together, they may indicate a compromise.

---

# Logging Architecture Example

```
Application

↓

Structured Logs

↓

Log Collector

↓

Central Log Storage

↓

SIEM

↓

Detection Rules

↓

SOC

↓

Incident Response
```

Centralized logging simplifies investigation and reduces the risk of losing evidence from individual systems.

---

# Business Impact

Weak logging and monitoring can lead to:

- Delayed breach detection
- Incomplete forensic investigations
- Regulatory non-compliance
- Increased incident response time
- Insider threats going unnoticed
- Difficulty proving what occurred
- Greater financial and reputational damage

---

# Key Takeaways

- Logging records security-relevant events, while monitoring analyzes those events for signs of malicious activity.
- Effective logging requires complete, structured, and centralized event collection.
- Security logs should capture authentication, authorization, administrative, application, infrastructure, and cloud events.
- Log correlation across multiple systems provides greater visibility than isolated event analysis.
- Strong logging and monitoring capabilities are essential for timely incident detection, investigation, and response.

# Enterprise Log Management and SIEM

---

# Overview

Enterprise environments generate millions of security events every day.

Examples include:

- User logins
- API requests
- Firewall events
- DNS queries
- Endpoint alerts
- Cloud activity
- Authentication failures
- Administrative changes

Without centralized collection and analysis, detecting malicious activity becomes extremely difficult.

A modern logging architecture aggregates data from many systems into a centralized platform for correlation, alerting, and investigation.

---

# Enterprise Logging Architecture

```
                  Users
                     │
                     ▼
      Applications / APIs / Databases
                     │
                     ▼
 Servers ─ Firewalls ─ VPN ─ Active Directory
                     │
                     ▼
             Log Collectors
                     │
                     ▼
           Log Normalization
                     │
                     ▼
              Central Storage
                     │
                     ▼
                   SIEM
                     │
                     ▼
           Detection Rules
                     │
                     ▼
              Alerts / Cases
                     │
                     ▼
                    SOC
                     │
                     ▼
            Incident Response
```

Each component contributes to detection and investigation.

---

# Centralized Logging

## Overview

Instead of storing logs separately on each device:

```
Server A

Server B

Firewall

Application
```

Organizations forward logs to a central location.

```
Server A

↓

Server B

↓

Firewall

↓

Central Log Platform
```

Benefits include:

- Easier searching
- Better correlation
- Simplified investigations
- Reduced risk of log loss
- Centralized retention policies

---

# Log Collectors

Log collectors receive logs from multiple systems and forward them for storage and analysis.

Responsibilities include:

- Receiving events
- Buffering during outages
- Compression
- Encryption in transit
- Reliable forwarding

Examples include lightweight agents or native log forwarding mechanisms.

---

# Log Forwarders

Forwarders run on endpoints or servers and send logs to collectors or directly to a SIEM.

Typical workflow:

```
Application

↓

Log File

↓

Forwarder

↓

Collector

↓

SIEM
```

Reliable forwarding prevents loss during network interruptions.

---

# Syslog

## Overview

Syslog is a widely used logging protocol in Unix/Linux environments and is also supported by many network devices.

Common sources:

- Linux servers
- Routers
- Switches
- Firewalls
- IDS/IPS
- Load balancers

---

## Syslog Flow

```
Linux Server

↓

Syslog

↓

Collector

↓

SIEM
```

Syslog messages generally include:

- Timestamp
- Hostname
- Facility
- Severity
- Message

---

# Syslog Severity Levels

| Level | Meaning |
|--------|----------|
| Emergency | System unusable |
| Alert | Immediate action required |
| Critical | Critical condition |
| Error | Error condition |
| Warning | Warning |
| Notice | Significant normal event |
| Informational | General information |
| Debug | Debugging details |

Severity assists analysts in prioritizing events.

---

# Windows Event Logs

Windows stores operating system and application events in structured event logs.

Common log categories include:

```
Security

System

Application

Setup

Forwarded Events
```

Security logs are particularly valuable for detecting:

- Authentication activity
- Privilege changes
- Process creation
- Policy modifications
- Account management

---

# Linux Log Locations

Linux commonly stores logs under:

```
/var/log/
```

Examples include:

```
auth.log

secure

syslog

messages

kern.log

audit.log
```

Exact locations vary by distribution.

---

# Structured Logging

Structured logs use machine-readable formats such as JSON.

Example:

```json
{
  "timestamp": "2026-08-15T12:40:15Z",
  "user": "alice@example.com",
  "event": "login",
  "status": "success",
  "ip": "203.0.113.25"
}
```

Advantages include:

- Easier parsing
- Better searching
- Consistent field names
- Improved SIEM correlation

---

# Log Normalization

Different systems record similar events using different formats.

Example:

Application:

```
User Login Successful
```

Firewall:

```
Authentication Accepted
```

Active Directory:

```
Logon Success
```

Normalization converts these into a consistent schema.

```
Different Formats

↓

Normalization

↓

Common Event Schema

↓

SIEM
```

This simplifies rule creation and correlation.

---

# Time Synchronization

Accurate timestamps are critical for investigations.

Without synchronized clocks:

```
Server A

12:01
```

```
Firewall

11:58
```

```
Application

12:05
```

Reconstructing an attack becomes difficult.

Organizations should synchronize systems using trusted time sources (such as NTP).

---

# Why Time Matters

Example attack timeline:

```
VPN Login

12:00

↓

Application Login

12:01

↓

Database Query

12:02

↓

Large Download

12:04
```

Consistent timestamps enable investigators to accurately reconstruct events.

---

# Security Information and Event Management (SIEM)

## Overview

A SIEM centralizes security logs and applies analytics to detect suspicious activity.

Primary functions include:

- Log collection
- Correlation
- Alerting
- Dashboards
- Search
- Investigation support
- Reporting

---

# SIEM Architecture

```
Applications

Operating Systems

Firewalls

Cloud

Identity Systems

↓

Collectors

↓

Normalization

↓

SIEM

↓

Detection Rules

↓

Alerts

↓

SOC Analysts
```

---

# SIEM Functions

```
SIEM

├── Collect
├── Normalize
├── Enrich
├── Correlate
├── Detect
├── Alert
├── Investigate
└── Report
```

Each function contributes to improving detection quality and analyst efficiency.

---

# Event Correlation

Individual events often appear harmless.

Example:

```
Failed Login

↓

Successful Login

↓

Privilege Change

↓

Sensitive File Download

↓

External Connection
```

Correlation links these events into a meaningful security story.

---

# Log Retention

Organizations should define retention policies based on:

- Business requirements
- Regulatory obligations
- Incident response needs
- Storage capacity

Typical lifecycle:

```
Collect

↓

Hot Storage

↓

Warm Storage

↓

Archive

↓

Deletion
```

Retention periods vary by industry and legal requirements.

---

# Log Integrity

Attackers frequently attempt to modify or delete logs.

Organizations should protect logs using:

- Restricted access
- Cryptographic integrity checks
- Centralized storage
- Immutable storage where appropriate
- Regular backups

---

# WORM Storage

**Write Once Read Many (WORM)** storage prevents modification after data is written.

```
Write Log

↓

Immutable Storage

↓

Read Only
```

This helps preserve forensic evidence.

---

# Chain of Custody

When logs become evidence, organizations should document:

- Who collected the logs
- When they were collected
- How they were transferred
- Where they were stored
- Who accessed them

Maintaining a documented chain of custody supports the integrity and admissibility of evidence where required.

---

# Detection Engineering

Detection engineering is the process of designing, testing, and improving detection logic.

Typical workflow:

```
Threat Intelligence

↓

Threat Model

↓

Detection Rule

↓

SIEM

↓

Alert

↓

Validation

↓

Continuous Improvement
```

Detection content should evolve as attacker techniques change.

---

# Common Detection Data Sources

Examples include:

- Authentication logs
- Process creation events
- DNS logs
- Web proxy logs
- Endpoint telemetry
- Firewall logs
- Cloud audit logs
- Email security logs
- Identity provider logs
- Kubernetes audit logs

Using multiple data sources improves detection coverage.

---

# Business Impact

Poor log management may result in:

- Missed attacks
- Incomplete investigations
- Regulatory violations
- Increased response time
- Loss of forensic evidence
- Reduced visibility across enterprise systems

---

# Key Takeaways

- Centralized logging provides visibility across applications, infrastructure, cloud services, and identity systems.
- Log collectors, forwarders, and normalization improve reliability and consistency.
- SIEM platforms correlate events from multiple sources to detect suspicious activity.
- Accurate time synchronization is essential for reconstructing attack timelines.
- Protecting log integrity through access controls, immutable storage, and documented chain of custody strengthens incident investigations.
- Detection engineering continuously improves monitoring by transforming threat intelligence into actionable detection rules.

# Detection Engineering, Alerting, and SOC Operations

---

# Overview

Collecting logs alone does not improve security.

Organizations derive value from logs only when they transform raw events into actionable detections that enable rapid investigation and response.

Detection engineering is the discipline of designing, testing, maintaining, and improving these detections.

```
Raw Logs

↓

Normalization

↓

Correlation

↓

Detection Rule

↓

Alert

↓

Investigation

↓

Incident Response
```

---

# What is Detection Engineering?

Detection engineering is the process of creating logic that identifies malicious or suspicious activity from collected telemetry.

Its goals include:

- Detect attacks early
- Reduce attacker dwell time
- Minimize false positives
- Improve analyst efficiency
- Continuously adapt to new attacker techniques

Detection engineering combines:

- Threat intelligence
- Threat modeling
- Log analysis
- Security operations
- Continuous testing

---

# Detection Engineering Lifecycle

```
Threat Intelligence

↓

Threat Modeling

↓

Select Data Sources

↓

Create Detection Rule

↓

Test Rule

↓

Deploy

↓

Monitor

↓

Tune

↓

Repeat
```

Detection content should be treated as living code and reviewed regularly.

---

# Detection Rule

A detection rule defines the conditions that indicate potentially malicious behavior.

Example logic:

```
IF

5 Failed Logins

+

1 Successful Login

Within 10 Minutes

↓

Generate Alert
```

Detection rules should be:

- Specific
- Measurable
- Testable
- Tuned
- Version controlled

---

# Detection Pipeline

```
Security Event

↓

Log Generated

↓

Collector

↓

SIEM

↓

Correlation Rule

↓

Alert

↓

SOC Investigation
```

---

# Indicators of Compromise (IOCs)

## Overview

IOCs are observable artifacts suggesting that a system may already be compromised.

Examples:

- Malicious IP addresses
- Malicious domains
- File hashes
- Registry modifications
- Suspicious processes
- Known malware signatures

Example:

```
Known Malicious IP

↓

Firewall Log

↓

Alert
```

IOCs are valuable but often become less useful as attackers change infrastructure.

---

# Indicators of Attack (IOAs)

IOAs focus on attacker behavior rather than known artifacts.

Examples:

- Credential dumping
- Lateral movement
- Privilege escalation
- Defense evasion
- Unusual PowerShell execution
- Suspicious cloud API usage

Example:

```
Normal User

↓

Creates Administrator Account

↓

Alert
```

Behavior-based detections are generally more resilient than IOC-only detections.

---

# IOC vs IOA

| Indicator of Compromise (IOC) | Indicator of Attack (IOA) |
|--------------------------------|----------------------------|
| Evidence of compromise | Evidence of attacker behavior |
| Often artifact-based | Behavior-based |
| IPs, hashes, domains | Techniques and tactics |
| Easier to evade | More difficult to evade |

Effective security programs typically use both approaches.

---

# MITRE ATT&CK Mapping

Many organizations map detections to the MITRE ATT&CK framework.

Example:

```
Credential Dumping

↓

MITRE ATT&CK

↓

Credential Access

↓

Detection Rule
```

Benefits include:

- Standardized terminology
- Coverage analysis
- Gap identification
- Threat-informed defense

---

# Detection Use Cases

A use case describes a security scenario that should generate an alert.

Examples include:

Authentication

- Impossible travel
- Excessive failed logins
- MFA bypass attempts

Endpoint

- Suspicious PowerShell execution
- Credential dumping
- Unsigned driver loading

Cloud

- Root account usage
- New IAM administrator
- Public storage bucket

Network

- DNS tunneling
- Port scanning
- Data exfiltration

Application

- SQL injection attempts
- Authentication bypass
- Privilege escalation

---

# Correlation Rules

Single events often appear benign.

Correlation links multiple related events.

Example:

```
VPN Login

↓

New Device

↓

Administrative Login

↓

Sensitive Database Access

↓

Large Download

↓

Alert
```

Correlation reduces noise while improving detection quality.

---

# Alert Lifecycle

```
Detection Rule

↓

Alert Created

↓

Alert Prioritized

↓

SOC Review

↓

Investigation

↓

Incident?

↓

Response

↓

Closure

↓

Lessons Learned
```

Every alert should have a documented workflow.

---

# Alert Severity

Organizations commonly classify alerts by impact.

| Severity | Typical Response |
|-----------|------------------|
| Informational | Record only |
| Low | Monitor |
| Medium | Analyst review |
| High | Immediate investigation |
| Critical | Incident response activation |

Severity should consider:

- Asset value
- Threat confidence
- Business impact
- Exploitation evidence

---

# Alert Enrichment

Raw alerts often lack sufficient context.

Enrichment may add:

- User identity
- Device information
- Threat intelligence
- Geolocation
- Asset criticality
- Previous alerts
- Vulnerability data

Example:

```
Login Alert

↓

Threat Intelligence

↓

Known Malicious IP

↓

Critical Alert
```

---

# False Positives

A false positive occurs when benign activity is incorrectly identified as malicious.

Example:

```
System Administrator

↓

Runs PowerShell

↓

Detection Rule

↓

Alert

↓

Benign Activity
```

High false-positive rates increase analyst workload and contribute to alert fatigue.

---

# False Negatives

A false negative occurs when malicious activity is not detected.

Example:

```
Attacker

↓

Credential Theft

↓

No Alert

↓

Compromise Continues
```

False negatives increase organizational risk because attacks remain undetected.

---

# Balancing Detection Quality

```
Sensitive Rules

↓

Many Alerts

↓

Higher False Positives
```

```
Strict Rules

↓

Fewer Alerts

↓

Higher False Negatives
```

Detection engineering seeks an appropriate balance between sensitivity and precision.

---

# User and Entity Behavior Analytics (UEBA)

UEBA identifies deviations from normal behavior.

Examples:

```
Normal Login

India

↓

Sudden Login

Another Country

↓

Alert
```

Additional examples include:

- New device usage
- Unusual working hours
- Excessive downloads
- Privilege abuse
- Rare administrative actions

UEBA complements rule-based detection by identifying anomalous behavior.

---

# Security Orchestration, Automation, and Response (SOAR)

SOAR platforms automate repetitive security tasks.

Typical workflow:

```
Alert

↓

Automatic Enrichment

↓

Threat Intelligence Lookup

↓

Create Case

↓

Notify Analyst

↓

Optional Automated Response
```

Automation allows analysts to focus on higher-value investigations.

---

# Threat Hunting vs Monitoring

| Monitoring | Threat Hunting |
|-------------|----------------|
| Reactive | Proactive |
| Waits for alerts | Searches for hidden threats |
| Rule-based | Hypothesis-driven |
| Continuous | Periodic or ongoing campaigns |

Both approaches are important components of mature security operations.

---

# SOC Workflow

```
Log Collection

↓

SIEM

↓

Detection Rule

↓

Alert

↓

Tier 1 Analyst

↓

Tier 2 Investigation

↓

Incident Response

↓

Recovery

↓

Lessons Learned
```

Each stage should have documented procedures and escalation criteria.

---

# Incident Escalation

Not every alert becomes a security incident.

Example workflow:

```
Alert

↓

Validation

↓

False Positive?

↓

Yes

↓

Close
```

```
No

↓

Incident

↓

Escalation

↓

Containment

↓

Recovery
```

---

# Detection Maturity

Organizations typically progress through several stages:

```
Manual Log Review

↓

Basic Alerts

↓

Correlation Rules

↓

Threat Intelligence

↓

Behavior Analytics

↓

Automation

↓

Continuous Improvement
```

Detection maturity is an ongoing journey rather than a one-time achievement.

---

# Business Impact

Effective detection engineering helps organizations:

- Reduce attacker dwell time
- Detect sophisticated threats
- Improve analyst productivity
- Reduce investigation time
- Enhance threat visibility
- Improve incident response
- Support compliance requirements

---

# Key Takeaways

- Detection engineering transforms raw security telemetry into actionable alerts.
- Indicators of Compromise (IOCs) identify known malicious artifacts, while Indicators of Attack (IOAs) focus on attacker behavior.
- Mapping detections to MITRE ATT&CK improves coverage analysis and communication.
- Correlation, enrichment, and UEBA improve detection quality beyond simple event matching.
- Balancing false positives and false negatives is essential for effective security operations.
- SOAR platforms automate repetitive tasks and help analysts respond more efficiently.
- Continuous tuning and testing are necessary because attacker techniques and enterprise environments evolve over time.