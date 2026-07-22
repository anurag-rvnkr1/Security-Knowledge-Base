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