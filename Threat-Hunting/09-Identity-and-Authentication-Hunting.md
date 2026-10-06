# Identity and Authentication Hunting

## Overview

Identity is one of the most important security boundaries in modern enterprise environments.

Attackers increasingly target identities rather than individual endpoints because a compromised identity can provide access to:

- Workstations
- Servers
- Active Directory
- Cloud platforms
- SaaS applications
- Databases
- Source-code repositories
- VPN infrastructure
- Administrative consoles
- APIs
- Sensitive business applications

A compromised identity can therefore allow an attacker to operate using legitimate credentials while appearing like a normal user.

This creates a fundamental threat-hunting challenge:

> **The presence of valid credentials does not mean the activity is legitimate.**

Identity and authentication hunting focuses on identifying anomalous authentication behavior, credential abuse, privilege escalation, lateral movement, account takeover, and suspicious identity relationships.

A mature identity-hunting capability correlates:

```text
Identity
   +
Authentication
   +
Endpoint
   +
Network
   +
Cloud
   +
Application
   +
Behavioral Baseline
```

---

# Why Identity Hunting Matters

Traditional security monitoring often asks:

```text
"Did malware execute?"
```

Modern identity security must also ask:

```text
"Who authenticated?"

"From where?"

"To what?"

"Using which authentication method?"

"Was the authentication successful?"

"Was MFA used?"

"Was the session expected?"

"What happened after authentication?"
```

A typical identity attack may look like:

```text
Credential Theft
      │
      ▼
Valid Account
      │
      ▼
Authentication
      │
      ▼
Internal Access
      │
      ▼
Privilege Escalation
      │
      ▼
Lateral Movement
      │
      ▼
Cloud / Application Access
```

---

# Identity Threat-Hunting Architecture

```text
                       IDENTITY SOURCES
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
       Active Directory     Cloud IAM           SaaS
          │                   │                   │
          ▼                   ▼                   ▼
      Authentication      Authentication      Sign-In
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                           SIEM
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
             Baseline      Detection     Hunting
                 │            │            │
                 └────────────┼────────────┘
                              ▼
                           SOC / IR
```

---

# Identity Data Sources

Important identity telemetry includes:

- Windows Security logs
- Domain Controller logs
- Active Directory events
- Kerberos events
- NTLM events
- VPN authentication
- MFA logs
- Identity provider logs
- Entra ID / Microsoft identity telemetry
- AWS CloudTrail
- Google Cloud Audit Logs
- SaaS audit logs
- Application authentication logs
- SSO logs
- OAuth events
- Privileged access management logs
- Endpoint logon events

---

# Authentication Event Model

A normalized authentication event may contain:

```text
Timestamp
User
Source IP
Source Host
Destination
Authentication Protocol
Authentication Method
Result
MFA Status
Application
Device
Location
Risk
```

Example:

```text
User:
alice@example.com

Source:
10.10.20.15

Application:
VPN

Authentication:
Successful

MFA:
Approved

Time:
09:31
```

The event alone is not suspicious.

Context determines risk.

---

# Authentication Lifecycle

```text
User
 │
 ▼
Credential Submission
 │
 ▼
Authentication
 │
 ├── Failed
 │
 └── Successful
       │
       ▼
      MFA
       │
       ├── Failed
       └── Approved
              │
              ▼
           Session
              │
              ▼
           Resource
```

Threat hunting can investigate anomalies at every stage.

---

# Authentication vs Authorization

These concepts must be distinguished.

## Authentication

> Who are you?

## Authorization

> What are you allowed to access?

Example:

```text
Authentication
      │
      ▼
alice@example.com
      │
      ▼
Authorization
      │
      ├── Email ✓
      ├── HR System ✓
      └── Domain Admin ✗
```

An attacker may compromise a legitimate account but still attempt unauthorized privilege escalation.

---

# Windows Authentication

Windows environments provide extensive authentication telemetry.

Important events include:

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4647 | User-initiated logoff |
| 4648 | Explicit credential use |
| 4672 | Special privileges assigned |
| 4768 | Kerberos TGT request |
| 4769 | Kerberos service ticket request |
| 4771 | Kerberos pre-authentication failure |
| 4776 | NTLM credential validation |

These events should be correlated rather than analyzed independently.

---

# Windows Logon Types

Common Windows logon types include:

| Type | Meaning |
|---|---|
| 2 | Interactive |
| 3 | Network |
| 4 | Batch |
| 5 | Service |
| 7 | Unlock |
| 8 | NetworkCleartext |
| 9 | NewCredentials |
| 10 | RemoteInteractive |
| 11 | CachedInteractive |

For example:

```text
Logon Type 10
```

commonly represents an RDP-style remote interactive logon.

---

# Authentication Investigation

For a successful login:

```text
User
 │
 ▼
Source IP
 │
 ▼
Source Host
 │
 ▼
Destination
 │
 ▼
Authentication Method
 │
 ▼
Session
 │
 ▼
Post-Authentication Activity
```

The final step is critical.

A login may be legitimate while the subsequent activity is malicious.

---

# Failed Authentication Hunting

A single failed login is usually uninteresting.

A pattern such as:

```text
User A → Failed
User B → Failed
User C → Failed
User D → Failed
User E → Failed
```

from one source may indicate password spraying.

---

# Password Spraying

Password spraying attempts a small number of passwords against many accounts.

Conceptually:

```text
Attacker
   │
   ├──► User A ── Failed
   ├──► User B ── Failed
   ├──► User C ── Success
   ├──► User D ── Failed
   └──► User E ── Failed
```

The key characteristic is:

> **Many accounts, relatively few password attempts per account.**

---

# Brute Force vs Password Spraying

## Brute Force

```text
One Account
     │
     ├── Password 1
     ├── Password 2
     ├── Password 3
     └── Password 4
```

## Password Spraying

```text
One Password
     │
     ├── User A
     ├── User B
     ├── User C
     └── User D
```

The detection strategy differs.

---

# Password Spray Hunting

Useful dimensions:

```text
Source IP
Source Host
User
Failure Count
Unique Users
Time Window
Authentication Protocol
```

Example:

```text
Source IP: 203.0.113.20

Unique Users: 87
Failures: 146
Time Window: 20 minutes
```

This deserves investigation.

---

# Successful Authentication After Failures

A particularly important pattern:

```text
Many Failures
      │
      ▼
Successful Login
      │
      ▼
New Host / New Location
```

This can indicate credential compromise.

---

# Account Lockout Hunting

Repeated authentication failures may trigger account lockouts.

Investigate:

```text
Account
Source
Time
Application
Authentication Protocol
```

Patterns may reveal:

- Password spraying
- Stale credentials
- Misconfigured applications
- Scheduled jobs
- Malware
- Credential attacks

---

# Kerberos

Kerberos is a central authentication protocol in Active Directory environments.

Simplified flow:

```text
User
 │
 ▼
Authentication
 │
 ▼
KDC
 │
 ├── AS
 └── TGS
      │
      ▼
Service
```

---

# Kerberos Authentication Flow

```text
Client
   │
   │ Authentication Request
   ▼
KDC / AS
   │
   │ TGT
   ▼
Client
   │
   │ Service Ticket Request
   ▼
KDC / TGS
   │
   │ Service Ticket
   ▼
Client
   │
   ▼
Service
```

Understanding this flow is important for detecting identity abuse.

---

# Kerberos Hunting

Useful events include:

```text
4768
4769
4771
```

Potential anomalies:

- Unusual TGT requests
- Unusual service ticket volume
- Rare service access
- Unusual source hosts
- Authentication at unusual times
- Service account anomalies

---

# Kerberoasting Hunting

Kerberoasting targets service accounts by requesting service tickets associated with SPNs.

Hunting signals may include:

```text
User
   │
   ▼
Unusual Volume of TGS Requests
   │
   ▼
Many Service Accounts
```

The activity may be legitimate in some administrative or application scenarios.

Therefore investigate:

```text
Source Host
User
Ticket Volume
SPNs Requested
Time
Historical Behavior
```

---

# AS-REP Roasting

Accounts configured without Kerberos pre-authentication can create additional attack opportunities.

Defensive hunting should identify:

- Accounts with risky configuration
- Unusual AS requests
- Unexpected authentication behavior

Configuration review is generally more reliable than waiting for attack telemetry.

---

# NTLM

NTLM is an older authentication protocol that remains present in many environments.

Threat hunters should monitor:

- NTLM authentication
- Source/destination relationships
- Legacy applications
- Unusual NTLM usage
- NTLM authentication from unexpected hosts

---

# Pass-the-Hash

Pass-the-Hash abuses NTLM credential material rather than requiring the plaintext password.

Potential signals include:

```text
Compromised Credential Material
       │
       ▼
Remote Authentication
       │
       ▼
Unusual Host
       │
       ▼
Administrative Activity
```

Useful correlation:

```text
Authentication
+
Source Host
+
Destination
+
Account Privilege
+
Remote Service
```

---

# Pass-the-Ticket

Pass-the-Ticket abuses Kerberos ticket material.

Potential investigation signals include:

- Unusual Kerberos service access
- Ticket use from unexpected hosts
- Suspicious privileged sessions
- Authentication inconsistencies

Endpoint telemetry is often necessary for deeper investigation.

---

# Explicit Credential Use

Windows Event ID `4648` can indicate explicit credential use.

Potential scenarios include:

```text
RunAs
Remote Administration
Scheduled Tasks
Application Authentication
Credential Abuse
```

A single event is not inherently malicious.

Correlate it with:

```text
User
Process
Destination
Time
Privilege
```

---

# Privileged Account Hunting

Privileged identities deserve enhanced monitoring.

Examples:

```text
Domain Admin
Enterprise Admin
Cloud Administrator
Global Administrator
Root
Security Administrator
```

Monitor:

- Authentication
- Privilege assignment
- Group membership
- Password changes
- MFA changes
- New sessions
- Remote access

---

# Privileged Account Baseline

For each privileged identity establish:

```text
Normal Hosts
Normal Hours
Normal Applications
Normal Destinations
Normal Administrative Tasks
```

Then hunt for deviations.

Example:

```text
Admin Account
Normal:
Corporate Admin Workstation

Observed:
Unknown Endpoint
02:17 AM
External VPN
```

This deserves immediate investigation.

---

# Privileged Group Changes

Important changes include:

```text
User Added to Admin Group
User Removed from Admin Group
New Privileged Account
Group Membership Modification
```

A simplified model:

```text
User
 │
 ▼
Group Modification
 │
 ▼
Privileged Group
 │
 ▼
Administrative Access
```

---

# Identity Persistence

Attackers may attempt persistence through:

- New accounts
- Added group memberships
- OAuth application grants
- API keys
- Service accounts
- Access keys
- MFA changes
- Recovery-method changes
- Delegation changes

Identity hunting must therefore include configuration changes, not only authentication.

---

# Service Account Hunting

Service accounts frequently have:

- Long-lived credentials
- High privileges
- Non-interactive access
- Broad permissions

Potential anomalies:

```text
Service Account
      │
      ├── Interactive Login
      ├── VPN Login
      └── New Workstation
```

These may be suspicious depending on the account's intended purpose.

---

# Service Account Baselines

Document:

```text
Expected Hosts
Expected Services
Expected Authentication
Expected Hours
Expected Destinations
Expected Privileges
```

Then identify deviations.

---

# Dormant Accounts

Dormant accounts can become attractive targets.

Hunt for:

```text
Inactive Account
      │
      ▼
Sudden Authentication
      │
      ▼
Privileged Resource Access
```

Investigate:

- Who owns the account?
- Why was it activated?
- Which device used it?
- Was the activity authorized?

---

# Disabled Account Activity

Authentication attempts involving disabled accounts can reveal:

- Stale credentials
- Malware
- Credential stuffing
- Misconfiguration
- Attack attempts

Repeated activity should be investigated.

---

# New Account Hunting

Monitor:

```text
Account Created
      │
      ▼
Group Membership
      │
      ▼
Authentication
      │
      ▼
Resource Access
```

A newly created privileged account deserves higher scrutiny.

---

# MFA Hunting

Multi-factor authentication reduces the risk associated with stolen passwords but introduces new attack surfaces.

Monitor:

- MFA enrollment
- MFA method changes
- MFA failures
- MFA approvals
- Repeated MFA prompts
- Recovery method changes

---

# MFA Fatigue

MFA fatigue involves repeated authentication prompts intended to encourage a user to approve an unexpected request.

Conceptual pattern:

```text
Attacker
   │
   ├── MFA Prompt
   ├── MFA Prompt
   ├── MFA Prompt
   ├── MFA Prompt
   │
   ▼
User Approval
   │
   ▼
Account Access
```

Potential hunting signal:

```text
Many MFA Requests
+
Unusual Source
+
User Reports Unexpected Prompts
```

---

# MFA Bypass Hunting

Possible attack paths can include:

- Session theft
- Token theft
- Legacy authentication
- OAuth abuse
- Recovery-method abuse
- Device compromise

Identity hunting should therefore investigate the entire authentication chain.

---

# Impossible Travel

Impossible-travel detection identifies authentication events that appear geographically or temporally inconsistent.

Example:

```text
09:00
India

09:15
United States
```

If the travel time is physically impossible, investigate.

However, this signal can produce false positives because of:

- VPNs
- Corporate proxies
- Cloud infrastructure
- Mobile networks
- GeoIP inaccuracies

---

# Impossible Travel Investigation

Do not immediately classify it as compromise.

Investigate:

```text
Source IP
VPN
Proxy
Device
User Agent
MFA
Session
Application
Historical Location
```

---

# New Device Hunting

A new device accessing an identity may be legitimate or suspicious.

Example:

```text
User
 │
 ├── Laptop A ✓
 ├── Laptop B ✓
 └── Device X ?
```

Investigate:

```text
Device Identity
OS
Browser
IP
Location
MFA
Application
```

---

# New Country Authentication

A new geographic location can be useful for prioritization.

But consider:

```text
VPN
Travel
Cloud Proxy
Corporate Egress
Mobile Network
```

Geo-location should therefore be a signal, not an automatic verdict.

---

# User-Agent Hunting

Authentication logs may include User-Agent information.

Suspicious patterns can include:

- Unusual browser
- Scripted clients
- Automation tools
- Legacy protocols
- Unexpected operating system

Correlate with:

```text
Device
IP
User
Application
MFA
```

---

# OAuth and OIDC

Modern identity systems frequently use OAuth and OpenID Connect.

Simplified model:

```text
User
 │
 ▼
Identity Provider
 │
 ▼
Authentication
 │
 ▼
Token
 │
 ▼
Application
```

The token may then be used to access resources.

---

# OAuth Application Abuse

Attackers may attempt to abuse:

- Malicious applications
- Excessive permissions
- Consent grants
- OAuth tokens
- Service principals

Hunt for:

```text
New Application
+
New Consent
+
High Privilege
+
Unusual User
```

---

# OAuth Consent Hunting

Monitor:

```text
Application
User
Permissions
Timestamp
Source
```

Especially investigate applications requesting access to:

- Mail
- Files
- Directory
- Administrative APIs

---

# Token-Based Attacks

Modern environments frequently use tokens instead of repeatedly transmitting passwords.

Compromise of a valid token can allow access without a conventional password authentication event.

Therefore hunt for:

```text
Session
Token
Device
Application
Location
Resource
```

and unusual token usage.

---

# Cloud Identity

Cloud identities include:

```text
Human Users
Service Principals
Managed Identities
Roles
Groups
API Keys
Access Keys
Workload Identities
```

Each identity type has different behavior.

---

# AWS Identity Hunting

Useful telemetry includes CloudTrail events such as:

```text
ConsoleLogin
CreateUser
CreateAccessKey
AttachUserPolicy
AttachRolePolicy
AssumeRole
GetCallerIdentity
CreateRole
PutUserPolicy
```

The exact event set should be tailored to the environment.

---

# AWS Access Key Hunting

Potentially suspicious behavior:

```text
New Access Key
      │
      ▼
Unusual IP
      │
      ▼
API Activity
      │
      ▼
Privilege Escalation
```

Investigate:

```text
Who created the key?
Why?
When?
Who used it?
From where?
What APIs were called?
```

---

# Azure / Entra Identity Hunting

Relevant categories include:

- Sign-in activity
- Audit activity
- Directory changes
- Application registrations
- Consent
- Role assignments
- Conditional Access
- MFA events

Hunt for:

```text
User
+
New Application
+
Privilege Change
+
Unusual Sign-In
```

---

# GCP Identity Hunting

Google Cloud environments provide audit telemetry useful for investigating:

- IAM changes
- Service accounts
- Role assignments
- API usage
- Authentication
- Resource access

A useful model:

```text
Identity
   │
   ▼
Authentication
   │
   ▼
API Call
   │
   ▼
Resource
```

---

# Identity-Based Lateral Movement

Lateral movement often appears as:

```text
User
 │
 ▼
Host A
 │
 ▼
Authentication
 │
 ▼
Host B
 │
 ▼
Administrative Access
```

Hunt for new or unusual relationships between:

```text
User ↔ Host
User ↔ Server
Host ↔ Host
Account ↔ Service
```

---

# Identity Graph

A graph model can expose unusual relationships.

```text
             User A
            /      \
           /        \
      Host A       Host B
        |             |
        |             |
     Admin         Server
        \             /
         \           /
          Service C
```

Unexpected edges can be valuable hunting candidates.

---

# Authentication Graph Hunting

Example:

```text
Normal:
Alice → Laptop → File Server

Observed:
Alice → Unknown Laptop → Domain Controller
```

The relationship itself is suspicious.

---

# Session Anomalies

A session can be suspicious due to:

- New device
- New location
- New application
- Unusual duration
- Unusual time
- Multiple simultaneous sessions
- Unusual resource access

A mature identity hunt therefore considers sessions rather than only login events.

---

# Concurrent Session Hunting

Example:

```text
User A

09:00 → Bangalore
09:05 → London
09:07 → Singapore
```

Potential explanations:

- VPN
- Proxy
- Shared account
- Cloud infrastructure
- Credential compromise

Investigate the infrastructure before concluding.

---

# Account Takeover Pattern

A possible account takeover sequence:

```text
Password Failures
      │
      ▼
Successful Login
      │
      ▼
New Device
      │
      ▼
MFA Approval
      │
      ▼
Mailbox Access
      │
      ▼
OAuth Consent
```

This chain is significantly more valuable than any individual event.

---

# Identity Incident Timeline

Example:

```text
08:14
Password failures begin

08:16
Successful authentication

08:17
New device observed

08:18
MFA approval

08:20
New OAuth consent

08:22
Mailbox accessed

08:27
Sensitive document downloaded
```

This can strongly indicate account compromise.

---

# Identity + Endpoint Correlation

Suppose:

```text
Authentication:
User = alice
Host = LAPTOP-01
```

Then EDR shows:

```text
powershell.exe
   │
   ▼
Credential Access
   │
   ▼
Network Connection
```

Identity and endpoint telemetry together provide much stronger evidence.

---

# Identity + Network Correlation

```text
User
 │
 ▼
Authentication
 │
 ▼
Source IP
 │
 ▼
Internal Network
 │
 ▼
Remote Service
```

This can reveal lateral movement.

---

# Identity + Cloud Correlation

```text
User
 │
 ▼
Cloud Login
 │
 ▼
Role Change
 │
 ▼
API Calls
 │
 ▼
Sensitive Resource
```

This is particularly important for cloud compromise investigations.

---

# Identity Threat-Hunting Queries

## Password Spray Concept

```text
Authentication
| group by source_ip
| count unique users
| count failures
| identify high-volume sources
```

The exact syntax depends on the SIEM.

---

# Successful Login After Failures

```text
Failed Authentication
        │
        ▼
Same User / Source
        │
        ▼
Successful Authentication
        │
        ▼
Unusual Resource Access
```

This sequence should be prioritized.

---

# New Device Query

```text
User
  │
  ▼
Devices Used
  │
  ▼
Historical Baseline
  │
  ▼
New Device
```

---

# Privileged Account Query

```text
Privileged User
   │
   ▼
Authentication
   │
   ├── New Host
   ├── New Location
   ├── After Hours
   └── External Source
```

---

# Identity Hunt With Splunk

Conceptual password-spray hunt:

```spl id="ydgr5w"
index=auth action=failure
| stats
    count as failures
    dc(user) as unique_users
    by src_ip
| where unique_users >= 10
| sort -unique_users
```

Thresholds should be tuned using organizational baselines.

---

# Successful Login Correlation

```spl id="7o1e6n"
index=auth
| transaction user src_ip maxspan=30m
| search failure_count > 5 success_count > 0
```

Exact fields and transaction behavior depend on the logging architecture.

---

# Identity Hunting With KQL

Conceptual:

```kusto id="6y3r0r"
SigninLogs
| summarize
    Attempts = count(),
    Users = dcount(UserPrincipalName)
    by IPAddress
| where Users > 10
```

Use environment-specific schemas and thresholds.

---

# Practical Lab 1 — Password Spray Hunt

## Objective

Identify a source attempting authentication against many users.

### Procedure

1. Collect authentication failures.
2. Group by source IP.
3. Count unique users.
4. Count attempts.
5. Identify successful authentications.
6. Investigate successful accounts.

### Questions

```text
Which accounts were targeted?
Was any account successfully accessed?
Was MFA used?
What happened after success?
```

---

# Practical Lab 2 — Privileged Login Hunt

## Objective

Identify anomalous privileged authentication.

Search:

```text
Privileged Account
+
New Host
OR
New Location
OR
After Hours
```

Then correlate:

```text
Endpoint
Network
Cloud
Application
```

---

# Practical Lab 3 — Dormant Account Hunt

## Objective

Identify dormant accounts becoming active.

Workflow:

```text
Inactive Account
      │
      ▼
New Authentication
      │
      ▼
New Device
      │
      ▼
Sensitive Access
```

Investigate the account owner and authorization.

---

# Practical Lab 4 — MFA Fatigue Hunt

Search for:

```text
Repeated MFA Requests
+
Short Time Window
+
Same User
```

Then determine:

```text
Was one request eventually approved?
Where did the approval originate?
Was the device expected?
```

---

# Practical Lab 5 — New OAuth Consent

Identify:

```text
New OAuth Application
+
New Consent
+
High Privilege
```

Review:

```text
Application
Publisher
Permissions
User
Time
Source
Historical Usage
```

---

# Practical Lab 6 — Lateral Movement Hunt

Identify:

```text
User
  │
  ▼
New Host
  │
  ▼
Remote Authentication
  │
  ▼
Administrative Activity
```

Focus on unusual user-host relationships.

---

# Practical Lab 7 — Service Account Anomaly

Hypothesis:

> A service account is being used outside its expected behavior.

Search for:

```text
Service Account
+
Interactive Login
OR
VPN Login
OR
New Host
OR
External Source
```

Validate against documented service-account behavior.

---

# Practical Lab 8 — Cloud Identity Compromise

Hypothesis:

> A cloud identity may have been compromised.

Investigate:

```text
Authentication
 ↓
Device / IP
 ↓
MFA
 ↓
Role
 ↓
API Calls
 ↓
Resource Access
```

Look for:

- New locations
- New devices
- New credentials
- Privilege changes
- Unusual API calls

---

# Identity Detection Engineering

A mature identity detection pipeline:

```text
Identity Telemetry
       │
       ▼
Normalization
       │
       ▼
Baseline
       │
       ▼
Behavioral Detection
       │
       ▼
Correlation
       │
       ▼
Risk Scoring
       │
       ▼
SOC Investigation
```

---

# Identity Risk Scoring

A conceptual risk model:

```text
Risk =
Authentication Anomaly
+
Device Anomaly
+
Location Anomaly
+
Privilege Anomaly
+
Application Anomaly
+
Post-Authentication Behavior
```

Avoid making every anomaly an incident.

Risk scoring should prioritize investigation.

---

# Example Identity Detection

```text
IF

User authenticates from a new device

AND

Source location is unusual

AND

MFA approval occurs

AND

Sensitive resource is accessed

THEN

Generate high-priority identity investigation
```

---

# Identity Detection Tuning

Poor rule:

```text
New Country = Alert
```

Better:

```text
New Country
+
New Device
+
Unusual Time
+
Sensitive Resource
```

Better still:

```text
New Country
+
New Device
+
Unusual Time
+
MFA Anomaly
+
Sensitive Resource
+
Endpoint Risk
```

---

# Identity Telemetry Gaps

Example:

```text
Authentication Logs       ✓
Source IP                 ✓
User                      ✓
Device                    ✓
MFA                       ✗
Application               ✓
Session                   ✗
Post-Auth Activity        ✗
```

Without MFA and session visibility, account-takeover investigations become harder.

---

# Identity Security Best Practices

## Least Privilege

Users and service accounts should have only the access they require.

---

## MFA

Use strong MFA for privileged and sensitive access.

---

## Privileged Access Management

Separate administrative identities and monitor privileged sessions.

---

## Service Account Governance

Document:

```text
Owner
Purpose
Hosts
Permissions
Rotation
Authentication
```

---

## Disable Dormant Accounts

Reduce unnecessary attack surface.

---

## Monitor Identity Changes

Track:

```text
Accounts
Groups
Roles
Applications
Credentials
MFA
Recovery Methods
```

---

# Identity Hunting Checklist

## Authentication

- [ ] Failed logins
- [ ] Successful logins
- [ ] Authentication method
- [ ] Source IP
- [ ] Source device
- [ ] Location
- [ ] MFA

## Privilege

- [ ] Privileged accounts
- [ ] Group changes
- [ ] Role assignments
- [ ] New administrators
- [ ] Service accounts

## Anomalies

- [ ] New device
- [ ] New location
- [ ] Impossible travel
- [ ] After-hours activity
- [ ] Concurrent sessions
- [ ] Rare user-host relationship

## Cloud

- [ ] API credentials
- [ ] OAuth
- [ ] Application consent
- [ ] Role changes
- [ ] Access keys
- [ ] Service principals

## Response

- [ ] Disable compromised account
- [ ] Revoke sessions/tokens
- [ ] Reset credentials
- [ ] Review MFA
- [ ] Review OAuth grants
- [ ] Scope affected resources

---

# Common Identity Hunting Mistakes

## 1. Treating Every New Location as Malicious

VPNs and proxies produce legitimate geographic anomalies.

---

## 2. Monitoring Authentication Without Authorization

A valid login does not prove valid resource usage.

---

## 3. Ignoring Service Accounts

Service accounts often have broad privileges and long-lived credentials.

---

## 4. Ignoring Cloud Identities

Modern attacks frequently target cloud identities.

---

## 5. Ignoring MFA Events

Authentication and MFA should be investigated together.

---

## 6. Ignoring Post-Authentication Activity

What happened after login may be more important than the login itself.

---

# Identity Investigation Template

```text
Incident ID:

Date/Time:

User:

Account Type:

Source IP:

Source Host:

Destination:

Application:

Authentication Method:

Authentication Result:

MFA:

Device:

Location:

Session:

Privileges:

Role / Group:

Previous Baseline:

Anomaly:

Post-Authentication Activity:

Cloud Activity:

Endpoint Activity:

Network Activity:

Related Accounts:

Related Hosts:

MITRE ATT&CK:

Timeline:

Assessment:

Containment:

Credential Reset:

Session Revocation:

Remediation:

Detection Improvement:

Lessons Learned:
```

---

# MITRE ATT&CK Mapping

Relevant identity-related techniques include:

| Technique | Description |
|---|---|
| T1078 | Valid Accounts |
| T1078.001 | Default Accounts |
| T1078.002 | Domain Accounts |
| T1078.003 | Local Accounts |
| T1078.004 | Cloud Accounts |
| T1110 | Brute Force |
| T1110.001 | Password Guessing |
| T1110.003 | Password Spraying |
| T1550 | Use Alternate Authentication Material |
| T1550.002 | Pass the Hash |
| T1550.003 | Pass the Ticket |
| T1558 | Steal or Forge Kerberos Tickets |
| T1558.003 | Kerberoasting |
| T1528 | Steal Application Access Token |
| T1098 | Account Manipulation |
| T1098.001 | Additional Cloud Roles |
| T1098.003 | Additional Cloud Roles / Account Manipulation |
| T1136 | Create Account |
| T1136.002 | Create Cloud Account |

Validate technique and sub-technique mappings against the current ATT&CK knowledge base before using them in production content.

---

# Interview Questions

## 1. Why is identity threat hunting important?

Because attackers can use legitimate credentials to bypass traditional malware-focused controls and access enterprise resources.

---

## 2. What is password spraying?

Password spraying attempts a small number of commonly used passwords against many accounts rather than repeatedly attacking one account.

---

## 3. How do you distinguish password spraying from brute force?

Brute force generally targets one account with many passwords.

Password spraying generally targets many accounts with relatively few password attempts per account.

---

## 4. What is Kerberos?

Kerberos is a network authentication protocol heavily used by Active Directory environments.

---

## 5. What is Kerberoasting?

Kerberoasting is an attack technique involving service-ticket requests that can expose material useful for offline password cracking against service accounts.

---

## 6. What is Pass-the-Hash?

Pass-the-Hash uses captured NTLM credential material to authenticate without requiring the plaintext password.

---

## 7. What is Pass-the-Ticket?

Pass-the-Ticket abuses Kerberos ticket material to authenticate to services.

---

## 8. What is MFA fatigue?

MFA fatigue is an attack pattern where an attacker repeatedly triggers MFA prompts in an attempt to persuade the victim to approve one.

---

## 9. How would you investigate impossible travel?

I would examine:

```text
Source IP
VPN
Proxy
Device
MFA
User Agent
Session
Application
Historical Behavior
```

before concluding that the account is compromised.

---

## 10. What makes a privileged account suspicious?

Examples include:

- New device
- Unusual location
- Unusual time
- Unexpected VPN
- Unusual administrative action
- Unexpected privilege change

---

## 11. How would you hunt for compromised service accounts?

I would establish the account's expected hosts, services, authentication methods, and schedules, then hunt for deviations.

---

## 12. Why should OAuth consent be monitored?

Attackers may abuse OAuth applications and delegated permissions to maintain access without directly compromising the user's password.

---

## 13. What is valid-account abuse?

It is the use of legitimate credentials or accounts to perform unauthorized activity.

---

## 14. How would you investigate a suspicious successful login?

I would examine:

```text
User
Source
Device
Location
MFA
Application
Session
Resource Access
Post-Authentication Activity
```

---

## 15. What is the most important identity-hunting principle?

> **A successful authentication is not proof of legitimate activity.**

The identity, device, location, session, authorization, and subsequent behavior must all be considered.

---

# Key Takeaways

1. **Identity is a primary enterprise security boundary.**
2. **Valid credentials can be abused by attackers.**
3. **Authentication must be correlated with authorization and post-authentication activity.**
4. **Password spraying and brute force require different detection strategies.**
5. **Kerberos and NTLM telemetry are critical in Active Directory environments.**
6. **Privileged accounts require enhanced monitoring.**
7. **Service accounts require strict baselines and governance.**
8. **MFA events should be correlated with authentication activity.**
9. **New devices and locations are signals, not automatic proof of compromise.**
10. **OAuth and cloud identities introduce additional attack paths.**
11. **Identity graphs can expose unusual user-host relationships.**
12. **Account persistence can occur through roles, groups, tokens, applications, and credentials.**
13. **Post-authentication behavior is often more valuable than authentication alone.**
14. **Identity, endpoint, network, and cloud telemetry should be correlated.**
15. **Successful identity hunts should become repeatable detections.**

The core mindset is:

> **Don't ask only "Was this user authenticated?" Ask "Was this authentication expected, from the expected device, using the expected method, accessing the expected resources, followed by the expected behavior?"**

---

# References

- MITRE ATT&CK — Valid Accounts  
  https://attack.mitre.org/techniques/T1078/

- MITRE ATT&CK — Brute Force  
  https://attack.mitre.org/techniques/T1110/

- Microsoft Windows Security Auditing  
  https://learn.microsoft.com/windows/security/threat-protection/auditing/

- Microsoft Entra Documentation  
  https://learn.microsoft.com/entra/

- Microsoft Entra Sign-in Logs  
  https://learn.microsoft.com/entra/identity/monitoring-health/concept-sign-ins

- Microsoft Kerberos Documentation  
  https://learn.microsoft.com/windows-server/security/kerberos/

- MITRE ATT&CK — Steal Web Session Cookie  
  https://attack.mitre.org/techniques/T1539/

- MITRE ATT&CK — Steal Application Access Token  
  https://attack.mitre.org/techniques/T1528/

- AWS CloudTrail Documentation  
  https://docs.aws.amazon.com/awscloudtrail/

- Google Cloud Audit Logs  
  https://cloud.google.com/logging/docs/audit

- OpenID Connect  
  https://openid.net/developers/how-connect-works/

- OAuth 2.0 — RFC 6749  
  https://www.rfc-editor.org/rfc/rfc6749

- NIST Digital Identity Guidelines  
  https://pages.nist.gov/800-63-3/
