# Network, Endpoint, and Application Incident Response

> **An enterprise guide to investigating and responding to security incidents across network infrastructure, endpoints, servers, web applications, APIs, databases, and supporting security controls.**

---

# Overview

Modern incidents rarely remain confined to a single technology layer.

An application compromise may lead to:

```text id="9k7v3p"
Internet
   │
   ▼
Web Application
   │
   ▼
Application Server
   │
   ▼
Database
   │
   ▼
Identity
   │
   ▼
Internal Network
```

An endpoint compromise may similarly become:

```text id="0j4z1q"
Endpoint
   │
   ▼
Credentials
   │
   ▼
Network
   │
   ▼
Server
   │
   ▼
Application
   │
   ▼
Data
```

Effective incident response therefore requires correlation across:

- Network
- Endpoint
- Identity
- Application
- Database
- Cloud
- Security infrastructure

---

# Why It Matters

A security team that investigates only one layer may miss the rest of the attack.

For example:

```text id="m0t5di"
WAF Alert
   │
   ▼
Web Exploit
   │
   ▼
Application Compromise
   │
   ▼
Web Shell
   │
   ▼
Server Access
   │
   ▼
Credential Theft
```

Investigating only the WAF alert would produce an incomplete incident.

---

# Incident Response Layers

```text id="8o5y0j"
                 Enterprise
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     Network       Endpoint     Identity
       │             │             │
       └─────────────┼─────────────┘
                     ▼
                Application
                     │
                     ▼
                  Database
                     │
                     ▼
                    Data
```

Each layer provides different evidence.

---

# Network Incident Response

Network incidents involve suspicious or malicious communication across:

- Internal networks
- Internet connections
- VPN
- Wireless infrastructure
- Firewalls
- Proxies
- DNS
- Routers
- Network sensors

---

# Network Incident Categories

Common examples:

- C2 communication
- Port scanning
- Network intrusion
- Lateral movement
- DDoS
- Data exfiltration
- DNS abuse
- Unauthorized remote access
- Rogue devices
- Network segmentation violations

---

# Network Investigation Model

```text id="9y9e4v"
Source
  │
  ▼
Destination
  │
  ▼
Protocol
  │
  ▼
Port
  │
  ▼
Timestamp
  │
  ▼
Payload / Metadata
  │
  ▼
Identity / Asset
```

---

# Network Evidence

Potential sources:

- Firewall logs
- DNS logs
- Proxy logs
- NetFlow
- PCAP
- IDS/IPS
- VPN logs
- DHCP
- NAC
- Load balancers
- Cloud flow logs

---

# Firewall Investigation

Firewall logs can help establish:

```text id="y4u6mj"
Who?
Source IP

Where?
Destination IP

When?
Timestamp

How?
Protocol / Port

Result?
Allowed / Denied
```

Example:

```text id="1t2c1h"
10.10.10.25
      │
      │ TCP/443
      ▼
203.0.113.50
      │
      ▼
Allowed
```

A single allowed connection does not prove compromise.

---

# DNS Investigation

DNS is valuable for identifying:

- Suspicious domains
- C2
- Malware infrastructure
- Domain generation behavior
- Newly observed destinations
- Internal DNS anomalies

Example:

```text id="d1j7s7"
Host
 │
 ▼
DNS
 │
 ├── normal.example
 ├── suspicious.example
 └── unknown.example
```

---

# Network Beaconing

Repeated connections at predictable intervals may indicate automated communication.

Example:

```text id="f1r7s8"
10:00 → Destination
10:05 → Destination
10:10 → Destination
10:15 → Destination
```

Investigate:

- Process responsible
- Destination
- DNS
- User
- Host
- Protocol

Periodic communication can also occur legitimately, so context is essential.

---

# Network Scanning

Potential indicators:

```text id="9v1k8a"
Host A
 │
 ├──► Host B
 ├──► Host C
 ├──► Host D
 ├──► Host E
 └──► Host F
```

Investigate whether the source is:

- Vulnerability scanner
- Network monitoring system
- Administrator
- Security tool
- Potential attacker

---

# Lateral Movement

Network evidence can help identify:

```text id="8v1z4y"
Source Host
     │
     ▼
Remote Protocol
     │
     ▼
Destination Host
     │
     ▼
Authentication
```

Common enterprise protocols include:

- RDP
- SMB
- SSH
- WinRM
- Remote administration tools

Legitimate administrative traffic must be distinguished from malicious activity.

---

# Network Containment

Potential controls:

- Firewall block
- Host isolation
- VLAN isolation
- Network segmentation
- DNS blocking
- Proxy restriction
- Egress control
- VPN restriction

Containment should be proportional to the incident.

---

# DDoS Incidents

DDoS incidents primarily target availability.

Potential indicators:

- Traffic volume spike
- Connection exhaustion
- Application request surge
- Resource saturation

Response may involve:

```text id="7a0hbd"
Traffic Spike
    │
    ▼
Detection
    │
    ▼
Traffic Analysis
    │
    ▼
Filtering / Rate Limiting
    │
    ▼
Upstream Mitigation
    │
    ▼
Service Validation
```

Coordinate with network providers when required.

---

# Endpoint Incident Response

Endpoints include:

- Laptops
- Desktops
- Servers
- Virtual machines
- Workstations
- Mobile devices
- Specialized systems

---

# Endpoint Incident Categories

Examples:

- Malware
- Credential theft
- Unauthorized software
- Persistence
- Exploitation
- Privilege escalation
- Data theft
- Suspicious scripts
- Endpoint security tampering

---

# Endpoint Investigation Model

```text id="9x1q2u"
Host
 │
 ├── User
 ├── Processes
 ├── Files
 ├── Registry / Configuration
 ├── Network
 ├── Persistence
 └── Security Controls
```

---

# Process Investigation

Analyze:

```text id="8r5wz7"
Process
 │
 ├── Parent
 ├── Command Line
 ├── User
 ├── Path
 ├── Hash
 ├── Network
 └── Children
```

Example:

```text id="6p7fgi"
explorer.exe
      │
      ▼
powershell.exe
      │
      ▼
unknown.exe
```

This process chain should be investigated in context.

---

# Command-Line Investigation

Command-line telemetry can reveal:

- Script execution
- Download behavior
- Security-control changes
- Discovery
- Remote administration
- Persistence

Command lines should be correlated with:

- User
- Parent process
- Host
- Timestamp
- Network activity

---

# Endpoint Persistence

Common areas include:

```text id="l4q1hm"
Windows
 ├── Services
 ├── Scheduled Tasks
 ├── Registry
 ├── Startup
 └── WMI

Linux
 ├── Cron
 ├── systemd
 ├── SSH
 └── Profiles
```

---

# Endpoint Containment

Potential actions:

- EDR isolation
- Network isolation
- Account containment
- Process termination
- Application blocking

Process termination should be considered carefully when evidence preservation matters.

---

# Endpoint Recovery

Recovery may involve:

```text id="4u8j2z"
Evidence
   │
   ▼
Scope
   │
   ▼
Eradication
   │
   ▼
Patch
   │
   ▼
Rebuild / Clean
   │
   ▼
EDR Validation
   │
   ▼
Production
```

---

# Application Incident Response

Applications are frequently exposed to the Internet and therefore represent a major attack surface.

Examples:

- Web applications
- APIs
- Mobile backends
- SaaS applications
- Internal portals
- Authentication systems

---

# Application Incident Categories

Examples:

- SQL injection
- Authentication bypass
- Authorization failure
- Remote code execution
- File upload abuse
- SSRF
- XSS
- API abuse
- Credential compromise
- Supply-chain compromise

---

# Application Investigation Model

```text id="0ip4f1"
Request
   │
   ▼
Web / API Layer
   │
   ▼
Application
   │
   ▼
Database
   │
   ▼
External Services
```

Trace the attack through each layer.

---

# Web Application Logs

Useful fields include:

- Timestamp
- Source IP
- HTTP method
- URL
- Status code
- User agent
- Authentication identity
- Request ID
- Response size

Example:

```text id="u8x0df"
10:15:01
POST /login
401

10:15:04
POST /login
401

10:15:07
POST /login
200
```

This may warrant investigation for credential attack activity.

---

# Request Correlation

Application logs should ideally contain a request or correlation ID.

Example:

```text id="q4n2cq"
Request ID:
abc-123

Web Server
    │
    ▼
Application
    │
    ▼
Database
```

This allows investigators to trace one transaction across multiple components.

---

# Web Shell Investigation

A web shell may provide attackers with server-side command execution.

Potential indicators:

- Unexpected server-side files
- Recent file creation
- Suspicious application changes
- Unusual child processes
- Web process spawning shell processes

Example:

```text id="qg8e4s"
Web Server
    │
    ▼
Application Process
    │
    ▼
Shell Process
```

This process relationship can be highly suspicious depending on the application architecture.

---

# Web Shell Response

Potential steps:

1. Preserve evidence.
2. Identify affected application.
3. Identify malicious file.
4. Determine initial access.
5. Scope related systems.
6. Contain application.
7. Remove persistence.
8. Patch vulnerability.
9. Rebuild if necessary.
10. Validate.

---

# API Incident Response

APIs introduce additional attack surfaces:

- Authentication
- Authorization
- Tokens
- API keys
- Rate limiting
- Object access
- Input validation

---

# API Abuse Indicators

Potential indicators:

- Unusual request volume
- Enumeration
- Repeated authorization failures
- Access to unexpected objects
- Token anomalies
- Large data retrieval
- Unusual API clients

---

# API Investigation

Trace:

```text id="x0j3hh"
Client
  │
  ▼
API Gateway
  │
  ▼
Application
  │
  ▼
Database
```

Correlate:

```text id="7n0f9e"
Token
+
Source
+
Endpoint
+
Object
+
Timestamp
```

---

# Database Incident Response

Databases may contain the most sensitive organizational information.

Investigate:

- Authentication
- Queries
- Privilege changes
- Schema changes
- Data exports
- Bulk reads
- Administrative actions

---

# Database Investigation Model

```text id="9f0c5f"
Identity
   │
   ▼
Database Session
   │
   ▼
Query
   │
   ▼
Object
   │
   ▼
Result
```

---

# Suspicious Database Activity

Examples:

```text id="z8r8k1"
Normal:
Small application queries

Suspicious:
Large query against sensitive table
```

Context matters.

A legitimate analytics job may generate large queries.

---

# Database Containment

Potential actions:

- Disable compromised account
- Restrict network access
- Revoke sessions
- Rotate credentials
- Restrict affected application
- Preserve database logs

Avoid destructive changes before evidence requirements are understood.

---

# Application Secrets

Applications often contain:

- API keys
- Database credentials
- Cloud credentials
- Signing keys
- Encryption secrets

If an application is compromised, these secrets should be assessed.

```text id="9e8v2g"
Application Compromise
       │
       ▼
Secrets Exposure?
       │
   ┌───┴───┐
   ▼       ▼
  Yes      No
   │
   ▼
Rotate
```

---

# CI/CD Incident Response

A compromised pipeline can become a supply-chain incident.

Investigate:

- Repository access
- Commit changes
- Build jobs
- Runner activity
- Secrets
- Artifacts
- Deployment actions

Architecture:

```text id="l8k7i2"
Developer
   │
   ▼
Repository
   │
   ▼
CI/CD
   │
   ▼
Artifact
   │
   ▼
Production
```

---

# CI/CD Containment

Potential actions:

- Disable compromised credentials
- Suspend suspicious workflows
- Restrict deployment access
- Rotate secrets
- Preserve logs
- Validate artifacts

---

# Network + Endpoint Correlation

Example:

```text id="8h3k0p"
Endpoint
  │
  ├── suspicious.exe
  │
  ▼
DNS
  │
  ▼
malicious-domain.example
  │
  ▼
Firewall
  │
  ▼
External IP
```

This correlation strengthens the incident hypothesis.

---

# Endpoint + Application Correlation

Example:

```text id="kq3n5x"
Web Application
      │
      ▼
Suspicious Request
      │
      ▼
Server Process
      │
      ▼
Shell Process
      │
      ▼
Outbound Connection
```

This can reveal application-to-host compromise.

---

# Application + Database Correlation

```text id="4kg4b0"
HTTP Request
    │
    ▼
Application
    │
    ▼
Database Query
    │
    ▼
Sensitive Data
```

Correlating request and database logs can determine whether an attack resulted in data access.

---

# Network + Application + Identity

A mature investigation correlates:

```text id="y3s2d8"
Identity
   │
   ▼
Application
   │
   ▼
Endpoint
   │
   ▼
Network
   │
   ▼
Data
```

This produces an end-to-end attack path.

---

# Incident Correlation Architecture

```text id="6x8c9y"
                   SIEM
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
   Network       Endpoint       Identity
      │             │             │
      └─────────────┼─────────────┘
                    ▼
               Application
                    │
                    ▼
                 Database
                    │
                    ▼
                   Data
```

---

# Network Containment Decision Matrix

| Condition | Potential Action |
|---|---|
| Confirmed C2 | Block destination |
| Compromised endpoint | Isolate host |
| Lateral movement | Restrict protocols |
| DDoS | Rate-limit / upstream mitigation |
| Suspicious DNS | Block / monitor domain |
| Data exfiltration | Restrict egress |

---

# Endpoint Containment Decision Matrix

| Condition | Potential Action |
|---|---|
| Active malware | Isolate |
| Suspicious process | Investigate / terminate if appropriate |
| Credential theft | Secure identity |
| Persistence | Contain and investigate |
| Root-level compromise | Consider rebuild |

---

# Application Containment Decision Matrix

| Condition | Potential Action |
|---|---|
| Active exploit | Restrict vulnerable endpoint |
| Web shell | Isolate affected application/server |
| API abuse | Rate-limit / restrict |
| Credential compromise | Revoke credentials |
| Data exposure | Restrict access |
| Vulnerability | Patch / mitigate |

---

# Common Network Incident Mistakes

## 1. Blocking Only One IP

Attackers can change infrastructure.

## 2. Ignoring Internal Traffic

Lateral movement often occurs internally.

## 3. Ignoring DNS

DNS can provide important C2 evidence.

## 4. Blocking Critical Infrastructure Without Coordination

Containment can create outages.

## 5. Assuming Encrypted Traffic Is Invisible

Metadata can remain valuable.

---

# Common Endpoint Incident Mistakes

## 1. Killing the Process Immediately

Evidence may be lost.

## 2. Rebooting Before Evidence Collection

Volatile evidence may disappear.

## 3. Ignoring Parent Processes

Process lineage provides important context.

## 4. Ignoring Persistence

Malware may return.

## 5. Rebuilding Without Understanding Root Cause

Other systems may remain compromised.

---

# Common Application Incident Mistakes

## 1. Looking Only at WAF Alerts

The application and host may also be compromised.

## 2. Ignoring Database Logs

Data impact may be missed.

## 3. Deleting Suspicious Files

Evidence may be destroyed.

## 4. Rotating One Secret

Other application secrets may remain exposed.

## 5. Ignoring CI/CD

The attacker may have modified the software supply chain.

---

# Common Misconfigurations

### No Centralized Logging

Makes cross-layer correlation difficult.

### No Request IDs

Makes application tracing harder.

### Short Log Retention

Historical evidence disappears.

### No EDR

Endpoint visibility is limited.

### Flat Network

Lateral movement becomes easier.

### Excessive Application Privileges

Compromise has greater impact.

### Secrets in Source Code

Credential exposure becomes easier.

### No Database Auditing

Data access cannot be reconstructed reliably.

---

# Detection Strategy

A mature architecture should correlate:

```text id="s6z8hi"
Network
   │
   ├── DNS
   ├── Firewall
   └── Proxy
        │
        ▼
Endpoint
   │
   ├── Process
   ├── File
   └── Network
        │
        ▼
Application
   │
   ├── Request
   ├── Authentication
   └── Error
        │
        ▼
Database
   │
   └── Query
        │
        ▼
Identity
```

---

# Practical Commands

These commands are intended for authorized defensive investigation.

## Windows

### Network Connections

```powershell id="rqj8c8"
Get-NetTCPConnection
```

### Processes

```powershell id="2kv0k5"
Get-Process
```

### Process Details

```powershell id="e9f5ti"
Get-CimInstance Win32_Process |
Select-Object ProcessId, ParentProcessId, Name, CommandLine
```

### DNS Cache

```powershell id="qg2gqj"
Get-DnsClientCache
```

---

# Linux

### Network Connections

```bash id="nq6rji"
ss -tunap
```

### Processes

```bash id="y8d4u7"
ps aux
```

### Listening Services

```bash id="7xk8w2"
ss -lntup
```

### DNS Resolution

```bash id="v7p3lk"
dig example.com
```

---

# Web Server Investigation

For Apache/Nginx environments, locate configured access/error logs according to the deployment.

Typical locations may include:

```text id="7u6v9m"
/var/log/nginx/
/var/log/apache2/
```

Search carefully for:

- Suspicious requests
- Unexpected status codes
- Repeated exploitation attempts
- Unusual user agents
- Unexpected paths

---

# Practical Lab

# Lab — Multi-Layer Web Application Incident

## Scenario

The SOC receives a WAF alert:

```text id="w7n2w0"
Possible exploitation attempt
Target:
web-app-01
```

Shortly afterward:

```text id="5z5z0r"
Web Server
   │
   ▼
Suspicious Child Process
   │
   ▼
Outbound Connection
```

The application also accesses a sensitive database.

---

# Task 1 — Investigate the Network

Determine:

```text id="j4m5dn"
Source
Destination
Port
Protocol
DNS
Frequency
```

---

# Task 2 — Investigate the Endpoint

Determine:

```text id="my8h3u"
Parent process
Child process
User
Command line
Executable
Network connections
Persistence
```

---

# Task 3 — Investigate the Application

Search:

```text id="f4f8d0"
Request
Timestamp
Endpoint
Parameters
User
Response
Status
```

---

# Task 4 — Investigate the Database

Determine:

```text id="6y6j9n"
Account
Query
Table
Timestamp
Volume
Export
```

---

# Task 5 — Determine Impact

Answer:

```text id="l9w7ko"
Was code execution achieved?
Was persistence established?
Was the database accessed?
Was sensitive data accessed?
Was data exfiltrated?
```

---

# Task 6 — Containment

Design controls for:

```text id="r9m8w8"
Network
Endpoint
Application
Database
Identity
```

---

# Expected Attack Chain

```text id="g8l7o8"
Internet
   │
   ▼
Malicious Request
   │
   ▼
Web Application
   │
   ▼
Application Process
   │
   ▼
Shell / Malicious Process
   │
   ├──► C2
   │
   └──► Database
            │
            ▼
       Sensitive Data
```

---

# Advanced Lab — API Compromise

## Scenario

An API begins generating unusual traffic.

Indicators:

```text id="5m8u5q"
One Token
   │
   ├── Thousands of Requests
   ├── Multiple Object IDs
   ├── Authorization Errors
   └── Successful Access
```

Investigate:

1. Token owner
2. Source IP
3. Device
4. API endpoints
5. Objects accessed
6. Response volume
7. Database queries
8. Data exfiltration

---

# Professional Network Incident Record

```text id="n8f7e1"
Incident ID:
________________________

Source:
________________________

Destination:
________________________

Protocol:
________________________

Time Range:
________________________

Network Evidence:
________________________

Endpoint:
________________________

Application:
________________________

Identity:
________________________

Database:
________________________

Containment:
________________________

Impact:
________________________

Recovery:
________________________
```

---

# Multi-Layer Investigation Checklist

## Network

```text id="6c4z7p"
[ ] Source identified
[ ] Destination identified
[ ] Protocol identified
[ ] DNS reviewed
[ ] Firewall reviewed
[ ] Proxy reviewed
[ ] Network scope assessed
```

## Endpoint

```text id="p5j2pr"
[ ] Process tree reviewed
[ ] Command line reviewed
[ ] Files reviewed
[ ] Persistence reviewed
[ ] Network connections reviewed
[ ] Credentials assessed
```

## Application

```text id="n7h1j3"
[ ] Request identified
[ ] User identified
[ ] Endpoint identified
[ ] Parameters reviewed
[ ] Application logs preserved
[ ] Host relationship established
```

## Database

```text id="f0o9lq"
[ ] Account identified
[ ] Queries reviewed
[ ] Sensitive tables identified
[ ] Data volume assessed
[ ] Export assessed
```

---

# Maturity Model

## Level 1 — Reactive

- Individual log investigation
- Manual endpoint response
- Limited application visibility

## Level 2 — Repeatable

- Centralized logs
- EDR
- Standard application response

## Level 3 — Defined

- Cross-layer correlation
- Request IDs
- Network segmentation
- Database auditing

## Level 4 — Measured

- Detection coverage
- Response metrics
- Attack-path analysis

## Level 5 — Optimized

- Automated correlation
- Identity-aware detection
- Continuous attack-surface monitoring
- Automated containment with human oversight

---

# Metrics

### Network MTTD

Time to detect suspicious network activity.

### Endpoint MTTC

Time to contain a compromised endpoint.

### Application Detection Coverage

Percentage of critical applications with sufficient security telemetry.

### Cross-Layer Correlation Rate

Percentage of incidents where network, endpoint, identity, and application evidence can be correlated.

### Recovery Validation Rate

Percentage of recovered systems passing security validation.

---

# Interview Questions

## 1. Why should network and endpoint evidence be correlated?

Because network telemetry identifies communication while endpoint telemetry can identify the process responsible for that communication.

---

## 2. How would you investigate a web server compromise?

```text id="o1p4os"
WAF
 ↓
Web Logs
 ↓
Application Logs
 ↓
Process Tree
 ↓
Network
 ↓
Persistence
 ↓
Database
```

---

## 3. What is a web shell?

A malicious server-side component that provides unauthorized command or functionality to an attacker.

---

## 4. What would indicate a possible web shell?

Examples include:

- Unexpected server-side files
- Recent file modifications
- Web process spawning shell processes
- Unusual outbound connections

---

## 5. Why are request IDs useful?

They allow investigators to correlate a single application request across multiple services.

---

## 6. How would you investigate an API abuse incident?

Correlate:

```text id="v9b6d1"
Token
+
Source
+
Endpoint
+
Object
+
Timestamp
+
Response
+
Database
```

---

## 7. How would you investigate database compromise?

Review:

- Authentication
- Sessions
- Queries
- Privilege changes
- Sensitive table access
- Export activity

---

## 8. Why is a WAF alert not sufficient to determine compromise?

A WAF can identify suspicious requests, but it does not necessarily establish whether the application was successfully exploited or whether the host and database were affected.

---

## 9. What is cross-layer correlation?

Connecting evidence from multiple infrastructure layers to reconstruct an end-to-end attack.

---

## 10. Why are application secrets important?

Application compromise may expose credentials that allow attackers to access databases, APIs, cloud infrastructure, or other systems.

---

## 11. How can CI/CD become part of an incident?

An attacker may compromise source repositories, build systems, runners, artifacts, or deployment credentials and use them to introduce malicious changes into production.

---

## 12. How would you respond to suspicious outbound traffic from a web server?

```text id="4i6w1m"
Identify Process
  ↓
Identify Destination
  ↓
Review Application Logs
  ↓
Check DNS
  ↓
Investigate Host
  ↓
Contain if Required
  ↓
Scope Environment
```

---

# Integration With Threat Hunting

Network and application incidents provide excellent hunt opportunities.

Example:

```text id="w2n9f4"
Compromised Web Server
       │
       ▼
Known C2 Domain
       │
       ▼
Search DNS
       │
       ▼
Other Hosts
       │
       ▼
Potential Campaign
```

---

# Integration With Detection Engineering

Investigation findings can produce detections such as:

- Web server spawning shells
- Unusual application-to-internet connections
- Suspicious API enumeration
- Database access anomalies
- Unexpected CI/CD changes
- Unusual server authentication

---

# Enterprise Incident Response Architecture

```text id="o7k4qf"
                         Internet
                            │
                            ▼
                      WAF / Gateway
                            │
                            ▼
                       Application
                            │
                ┌───────────┼───────────┐
                ▼           ▼           ▼
             Endpoint     Network     Identity
                │           │           │
                └───────────┼───────────┘
                            ▼
                         Database
                            │
                            ▼
                            Data
                            │
                            ▼
                           SIEM
                            │
                            ▼
                     Incident Response
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          Contain        Investigate      Recover
```

---

# Key Takeaways

Network, endpoint, and application incidents must be investigated as interconnected events.

A mature workflow is:

```text id="0m4y6s"
Detect
  ↓
Correlate
  ↓
Identify Attack Path
  ↓
Scope
  ↓
Contain
  ↓
Preserve Evidence
  ↓
Eradicate
  ↓
Recover
  ↓
Validate
  ↓
Monitor
```

The most important principles are:

- Investigate beyond the initial alert.
- Correlate network and endpoint telemetry.
- Trace application requests into backend systems.
- Investigate database access during application incidents.
- Treat exposed application secrets seriously.
- Preserve evidence before destructive remediation where feasible.
- Investigate identity alongside infrastructure.
- Consider CI/CD when application integrity is affected.
- Use request IDs and consistent timestamps.
- Treat encrypted network traffic as metadata-rich rather than invisible.
- Validate containment and recovery.

> **An enterprise incident rarely belongs to a single layer. The responder's job is to connect the layers and reconstruct the complete attack path.**

---

# References

### NIST

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

Guide to Integrating Forensic Techniques:

https://csrc.nist.gov/publications/detail/sp/800-86/final

### CISA

https://www.cisa.gov/

### MITRE ATT&CK

Network Service Scanning:

https://attack.mitre.org/techniques/T1046/

Command and Control:

https://attack.mitre.org/tactics/TA0011/

Exfiltration:

https://attack.mitre.org/tactics/TA0010/

### OWASP

Web Security:

https://owasp.org/www-project-web-security-testing-guide/

API Security:

https://owasp.org/www-project-api-security/

### CIS Controls

https://www.cisecurity.org/controls

### FIRST

https://www.first.org/

### SANS

https://www.sans.org/

---

# Chapter Summary

A complete incident investigation should connect:

```text
Network
   +
Endpoint
   +
Identity
   +
Application
   +
Database
   +
Cloud
   +
Data
```

When these layers are correlated, the security team can move from isolated alerts to a defensible attack narrative.

> **Do not investigate alerts in isolation. Follow the evidence across the infrastructure until the complete attack path and impact are understood.**
