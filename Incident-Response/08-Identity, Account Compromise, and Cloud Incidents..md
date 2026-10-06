# Identity, Account Compromise, and Cloud Incidents

> **An enterprise guide to investigating and responding to compromised identities across Active Directory, Entra ID, SaaS platforms, cloud infrastructure, privileged accounts, service identities, and modern authentication systems.**

---

# Overview

Identity has become one of the most important security boundaries in modern environments.

An attacker who compromises an identity may not need malware on a traditional endpoint.

They may authenticate directly to:

- VPN
- SaaS applications
- Cloud consoles
- APIs
- Databases
- Internal applications
- Administrative interfaces

A modern attack can therefore look like:

```text
Phishing
   │
   ▼
Credential Theft
   │
   ▼
Identity Compromise
   │
   ├── SaaS
   ├── Cloud
   ├── VPN
   ├── Internal Applications
   └── Privileged Systems
```

Identity incidents require investigation across authentication, authorization, sessions, devices, applications, and cloud activity.

---

# Why It Matters

Traditional incident response often starts with:

> "Which machine was compromised?"

Modern identity-centric incidents require another question:

> **"Which identity was compromised, and what could that identity access?"**

Consider:

```text
Compromised User
      │
      ├── Email
      ├── VPN
      ├── SaaS
      ├── Cloud
      ├── Source Code
      └── Internal Applications
```

A single compromised identity can therefore have a much larger blast radius than one endpoint.

---

# Identity Attack Surface

```text
                    Identity
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Authentication  Authorization    Session
        │              │              │
        ▼              ▼              ▼
 Password          Roles           Tokens
 MFA               Groups          Cookies
 SSO               Policies        Refresh Tokens
 Certificates      Permissions     API Keys
```

Every layer can become an attack target.

---

# Identity Incident Categories

Common categories include:

1. Credential theft
2. Password spraying
3. Brute-force activity
6. MFA abuse
7. Session/token theft
8. OAuth abuse
9. Privilege escalation
10. Account takeover
11. Service account compromise
12. Cloud credential compromise
13. API key exposure
14. Insider misuse
15. Identity provider compromise

---

# Authentication vs Authorization

## Authentication

Answers:

> **Who are you?**

Examples:

- Password
- MFA
- Certificate
- Hardware key
- Biometrics

## Authorization

Answers:

> **What are you allowed to do?**

Examples:

- IAM role
- Group membership
- ACL
- Application permission
- Cloud policy

```text
Authentication
      │
      ▼
Identity Established
      │
      ▼
Authorization
      │
      ▼
Resource Access
```

A successful login does not automatically mean the requested action is authorized.

---

# Identity Incident Architecture

```text
                 Identity Provider
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      Users         Service IDs     Applications
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Authentication
                       │
                       ▼
                  Authorization
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
          SaaS       Cloud      Internal
```

---

# Identity Evidence Sources

Important evidence may include:

- Authentication logs
- MFA events
- SSO logs
- VPN logs
- Directory logs
- Group changes
- Privilege changes
- Token activity
- OAuth events
- Cloud audit logs
- API activity
- Device information
- Conditional access results

---

# Account Compromise Investigation

A practical investigation begins with:

```text
Compromised Account
       │
       ▼
Authentication History
       │
       ▼
Source Devices
       │
       ▼
Source IPs
       │
       ▼
Applications Accessed
       │
       ▼
Privileges Used
       │
       ▼
Actions Performed
```

---

# Authentication Timeline

Build a timeline such as:

```text
09:00  Normal login
09:05  MFA challenge
09:06  Login from unusual location
09:07  New session
09:10  Cloud API activity
09:12  Privilege change
09:20  Data access
09:25  SOC alert
```

The timeline can reveal where the compromise began and what happened afterward.

---

# Impossible Travel

Impossible-travel detections identify authentication events that appear geographically or temporally inconsistent.

Example:

```text
08:00
Bengaluru
      │
      │ 20 minutes
      ▼
08:20
London
```

This may indicate:

- Credential theft
- VPN usage
- Proxy infrastructure
- Corporate egress
- Cloud routing

Therefore, impossible travel should be treated as an investigative signal rather than automatic proof of compromise.

---

# Unusual Login Context

Investigate:

- New country
- New ASN
- New device
- New browser
- New operating system
- Unusual time
- New application
- New authentication method

Example:

```text
User:
analyst01

Normal:
Corporate device
Corporate network
Business hours

Observed:
Unknown device
Residential ASN
03:20 local time
```

This warrants investigation.

---

# MFA Events

MFA telemetry can reveal:

- Repeated challenges
- Unexpected approvals
- New MFA device registration
- MFA method changes
- Failed challenges
- Authentication method downgrade

---

# MFA Fatigue

MFA fatigue occurs when attackers repeatedly trigger authentication requests hoping the user eventually approves one.

Conceptually:

```text
Attacker
   │
   ├── MFA Request
   ├── MFA Request
   ├── MFA Request
   ├── MFA Request
   │
   ▼
User Accidentally Approves
   │
   ▼
Account Access
```

Defensive controls include:

- Number matching
- Phishing-resistant authentication
- Rate limiting
- User awareness
- Conditional access
- Risk-based authentication

---

# Phishing-Resistant Authentication

Stronger authentication mechanisms can reduce certain credential phishing risks.

Examples include:

- FIDO2
- WebAuthn
- Hardware security keys
- Passkeys

These mechanisms can provide stronger resistance against phishing than passwords and some legacy MFA methods.

---

# Password Spraying

Password spraying attempts a small number of commonly used passwords across many accounts.

Example pattern:

```text
Password A
   │
   ├── user01
   ├── user02
   ├── user03
   ├── user04
   └── user05
```

This differs from brute force against one account.

---

# Password Spraying Detection

Potential signals:

```text
Many Accounts
     │
     ▼
Same Source
     │
     ▼
Few Password Attempts
     │
     ▼
Authentication Failures
```

Detection should consider legitimate authentication infrastructure and shared NAT sources.

---

# Brute Force

Brute force typically focuses many authentication attempts against one or more accounts.

Potential signals:

- High failure rate
- Repeated attempts
- Account lockouts
- Unusual source
- Successful login following many failures

---

# Credential Stuffing

Credential stuffing uses credentials obtained from previous breaches.

Attack pattern:

```text
Leaked Credential Set
        │
        ▼
Automated Login Attempts
        │
        ▼
Multiple Applications
```

Controls include:

- MFA
- Password managers
- Breached-password detection
- Rate limiting
- Bot detection

---

# Session Hijacking

A stolen session token may allow access without the attacker needing the user's password.

Conceptually:

```text
User
 │
 ▼
Authenticated Session
 │
 ▼
Session Token
 │
 X
Attacker Obtains Token
 │
 ▼
Unauthorized Session
```

This makes session telemetry important.

---

# Token Theft

Potential token types include:

- Session cookies
- Refresh tokens
- OAuth tokens
- API tokens
- Cloud access tokens

Response may require:

```text
Revoke
   │
▼
Rotate
   │
▼
Reauthenticate
```

---

# OAuth Abuse

OAuth applications can receive permissions to access resources.

An attacker may abuse unauthorized OAuth applications.

Investigate:

- Application registration
- Consent events
- Permission scopes
- Token issuance
- Application owner
- Access activity

Example:

```text
User
 │
 ▼
OAuth Consent
 │
 ▼
Application
 │
 ▼
Mailbox / Files / APIs
```

---

# OAuth Incident Response

Potential actions:

1. Identify suspicious application.
2. Determine consent scope.
3. Identify affected users.
4. Revoke consent.
5. Revoke tokens.
6. Investigate application activity.
7. Review identity activity.
8. Determine whether credentials were also compromised.

---

# Privileged Account Compromise

Privileged identity compromise should receive high priority.

Examples:

- Domain Administrator
- Global Administrator
- Root
- Cloud Security Administrator
- Database Administrator

Potential actions:

```text
Privileged Account
       │
       ▼
Emergency Protection
       │
       ├── Session Revocation
       ├── Credential Rotation
       ├── Access Review
       └── Activity Investigation
```

---

# Service Account Compromise

Service accounts are often overlooked.

They may have:

- Long-lived credentials
- Broad permissions
- Limited monitoring
- Non-interactive access

A compromised service account can create significant persistence.

---

# Service Account Investigation

Determine:

```text
Where is it used?
What systems can it access?
What privileges does it have?
What credentials exist?
When was it last used?
Which processes use it?
```

---

# Identity Blast Radius

A useful investigation model:

```text
Compromised Identity
       │
       ▼
Permissions
       │
       ▼
Accessible Resources
       │
       ▼
Actions Performed
       │
       ▼
Potential Impact
```

---

# Active Directory Incidents

Active Directory remains a critical enterprise identity system.

Potential incidents include:

- Account compromise
- Privilege escalation
- Group membership modification
- Kerberos abuse
- NTLM credential abuse
- Domain controller compromise
- GPO modification
- Unauthorized service accounts

---

# Active Directory Investigation

Investigate:

```text
User
 │
 ├── Groups
 ├── Logons
 ├── Privileges
 ├── Authentication
 └── Remote Access
```

Then determine:

```text
User
 │
 ▼
Endpoint
 │
 ▼
Other Endpoint
 │
 ▼
Privileged Account
 │
 ▼
Domain Resources
```

---

# Domain-Level Compromise

A domain-level incident is significantly more serious than an isolated endpoint compromise.

Potential concerns include:

- Domain Administrator compromise
- Domain Controller compromise
- Kerberos trust abuse
- Widespread credential exposure
- GPO manipulation
- Persistence through privileged identities

Containment and recovery require specialized coordination.

---

# Cloud Identity

Cloud environments introduce identities such as:

- Users
- Service principals
- Managed identities
- Roles
- Workload identities
- API users

Example:

```text
Human User
     │
     ▼
Identity Provider
     │
     ▼
Cloud Role
     │
     ▼
Cloud Resource
```

---

# Cloud Credential Types

Potential credentials include:

- Passwords
- Access keys
- Temporary tokens
- Service credentials
- Certificates
- Managed identities

Each requires different containment procedures.

---

# Cloud API Activity

API logs can reveal:

- Who performed an action
- Which API was called
- Which resource was accessed
- When it occurred
- Source context
- Success/failure

Example:

```text
Identity
   │
   ▼
API Request
   │
   ▼
Resource
   │
   ▼
Audit Log
```

---

# Cloud Privilege Escalation

Potential indicators:

- New IAM role
- New policy
- Permission expansion
- Role assumption
- New service principal
- New access key

Example:

```text
Compromised User
       │
       ▼
Existing Role
       │
       ▼
Privilege Change
       │
       ▼
Administrative Access
```

---

# Cloud Containment

Potential actions:

```text
Compromised Identity
        │
        ├── Revoke Sessions
        ├── Disable Credentials
        ├── Rotate Keys
        ├── Remove Unauthorized Roles
        └── Restrict Access
```

Exact mechanisms differ across cloud providers.

---

# API Key Exposure

API keys may be exposed through:

- Source code
- Public repositories
- Logs
- CI/CD systems
- Configuration files
- Developer machines

If exposure is confirmed:

```text
Identify Key
    │
    ▼
Determine Scope
    │
    ▼
Revoke / Rotate
    │
    ▼
Identify Usage
    │
    ▼
Investigate
```

---

# Secrets in CI/CD

CI/CD environments may contain:

- Cloud credentials
- Package registry tokens
- Deployment keys
- Signing credentials
- API tokens

An attacker compromising CI/CD credentials may gain access to production infrastructure.

---

# Identity and CI/CD Architecture

```text
Developer
   │
   ▼
Source Repository
   │
   ▼
CI/CD
   │
   ├── Cloud Credentials
   ├── Secrets
   └── Deployment Access
          │
          ▼
       Production
```

---

# Identity Persistence

Attackers may maintain access through:

- New accounts
- New API keys
- OAuth applications
- SSH keys
- Service principals
- IAM roles
- Scheduled identity automation

Therefore:

> **Credential reset alone does not guarantee identity eradication.**

---

# Identity Eradication

A mature identity eradication process includes:

```text
Identify Compromised Identity
          │
          ▼
Identify Credentials
          │
          ▼
Revoke Sessions
          │
          ▼
Rotate Credentials
          │
          ▼
Remove Persistence
          │
          ▼
Review Privileges
          │
          ▼
Validate
```

---

# Account Recovery

Before restoring an account:

```text
[ ] Compromise understood
[ ] Sessions revoked
[ ] Credentials reset
[ ] MFA validated
[ ] Unauthorized devices reviewed
[ ] Privileges reviewed
[ ] Persistence removed
[ ] Monitoring active
```

---

# Cloud Incident Recovery

Recovery should verify:

```text
Identity
   │
   ├── Credentials
   ├── Sessions
   ├── Roles
   └── Policies
         │
         ▼
Resources
   │
   ├── Compute
   ├── Storage
   ├── Network
   └── Applications
```

---

# Identity Detection

Useful detection categories include:

### Authentication

- Impossible travel
- New device
- New location
- Unusual time

### Privilege

- New admin
- Role escalation
- Group modification

### Session

- Token anomalies
- Concurrent unusual sessions

### Cloud

- New access key
- New service principal
- Suspicious API activity

### OAuth

- Suspicious consent
- High-risk scopes

---

# Detection Example

A suspicious identity sequence:

```text
Failed Login
     │
     ▼
Successful Login
     │
     ▼
New Device
     │
     ▼
MFA Change
     │
     ▼
Privilege Change
     │
     ▼
Cloud API Activity
```

Correlation across these events is more valuable than analyzing each alert independently.

---

# Identity Incident Correlation

```text
Authentication
      │
      ├────────┐
      ▼        │
Device         │
      │        │
      ▼        │
Privilege ─────┤
      │        │
      ▼        │
Cloud Activity│
      │        │
      └────────┘
           │
           ▼
     Incident Score
```

---

# Common Identity Incident Mistakes

## 1. Resetting Only the Password

Tokens may remain valid.

## 2. Ignoring Sessions

Existing sessions may provide continued access.

## 3. Ignoring OAuth

Third-party applications may retain permissions.

## 4. Ignoring Service Accounts

Non-human identities may remain compromised.

## 5. Ignoring Privileges

An attacker may have escalated access before detection.

## 6. Ignoring Cloud Activity

Cloud APIs may provide independent attacker access.

## 7. Trusting Location Alone

VPNs and proxies can make location misleading.

## 8. Failing to Review Persistence

New keys or accounts may provide continued access.

---

# Common Misconfigurations

### No MFA

Password compromise becomes significantly more dangerous.

### Weak MFA

Legacy or easily phished methods may increase risk.

### Excessive Privileges

A compromised user can cause greater damage.

### Long-Lived Credentials

Stolen credentials remain useful for longer.

### No Session Revocation

Attackers may retain access after password resets.

### No Cloud Audit Logging

Identity investigations become difficult.

### Unmonitored Service Accounts

Non-human identities become blind spots.

### Unrestricted OAuth Consent

Users may authorize risky applications.

---

# Practical Commands

These examples are for authorized administrative and defensive investigation.

## Windows

### Current User

```powershell id="5zcr6s"
whoami
```

### Groups

```powershell id="5ykc9j"
whoami /groups
```

### Logged-On Sessions

```powershell id="1e8vvi"
quser
```

### Local Administrators

```powershell id="b8t0v3"
Get-LocalGroupMember Administrators
```

---

# Linux

### Current Identity

```bash id="xv0lry"
id
```

### Current User

```bash id="v3a8qb"
whoami
```

### Logged-In Users

```bash id="u3n3je"
who
```

### SSH Keys

```bash id="7xq8od"
ls -la ~/.ssh/
```

---

# Identity Investigation Queries

A generic investigation query should correlate:

```text
User
+
Source IP
+
Device
+
Timestamp
+
Authentication Method
+
Application
+
Privilege
+
Action
```

This is more useful than simply searching for failed logins.

---

# Practical Lab

# Lab — Compromised Enterprise Identity

## Scenario

SOC detects:

```text
User:
analyst01

Events:
09:10 Failed login
09:12 Successful login
09:13 New device
09:14 MFA method change
09:17 Cloud login
09:20 New API key
09:22 Storage access
```

---

# Task 1 — Assess

Determine:

```text
Is the account compromised?
What credentials may be affected?
What resources were accessed?
Is the attacker still active?
```

---

# Task 2 — Contain

Design actions covering:

```text
Account
Sessions
MFA
API Key
Cloud Access
```

---

# Task 3 — Scope

Search for:

```text
User
Source IP
Device
API Key
Cloud resources
OAuth applications
Privilege changes
```

---

# Task 4 — Eradicate

Remove:

- Unauthorized sessions
- Unauthorized keys
- Unauthorized permissions
- Persistence

---

# Task 5 — Recover

Restore the identity only after:

```text
Credential reset
MFA validation
Privilege review
Persistence review
Monitoring
```

---

# Expected Investigation

```text
Initial Access:
Credential compromise suspected

Persistence:
API key created

Privilege:
Under investigation

Cloud:
Unauthorized storage activity

Containment:
Sessions revoked
API key disabled
Identity secured

Next:
Review data access
Review source device
Investigate initial credential theft
```

---

# Advanced Lab — Cloud Identity Compromise

## Scenario

A cloud user creates:

```text
New Access Key
       │
       ▼
New IAM Role
       │
       ▼
Storage Enumeration
       │
       ▼
Large Data Read
```

Investigate:

1. Who created the key?
2. From where?
3. Which role was created?
4. What permissions existed?
5. Which resources were accessed?
6. Was data downloaded?
7. Did the identity create persistence?

---

# Advanced Identity Investigation Model

```text
Identity
   │
   ├── Authentication
   │
   ├── Devices
   │
   ├── Sessions
   │
   ├── Credentials
   │
   ├── Privileges
   │
   ├── Applications
   │
   ├── Cloud
   │
   └── Persistence
```

---

# Identity Incident Checklist

## Detection

```text
[ ] Alert validated
[ ] Authentication timeline created
[ ] Source IP identified
[ ] Device identified
```

## Scope

```text
[ ] Credentials reviewed
[ ] Sessions reviewed
[ ] Privileges reviewed
[ ] OAuth reviewed
[ ] Cloud activity reviewed
[ ] Service accounts reviewed
```

## Containment

```text
[ ] Sessions revoked
[ ] Credentials secured
[ ] API keys disabled
[ ] Unauthorized roles removed
[ ] Suspicious applications restricted
```

## Eradication

```text
[ ] Persistence removed
[ ] Unauthorized identities removed
[ ] Privileges corrected
[ ] Root cause fixed
```

## Recovery

```text
[ ] MFA validated
[ ] Credentials rotated
[ ] Identity restored
[ ] Monitoring enabled
```

---

# Identity Incident Record

```text
Incident ID:
________________________

Identity:
________________________

Identity Type:
[ ] User
[ ] Admin
[ ] Service Account
[ ] Cloud Identity
[ ] Application

Initial Detection:
________________________

Compromise Evidence:
________________________

Credentials Affected:
________________________

Sessions:
________________________

Privileges:
________________________

Resources Accessed:
________________________

Containment:
________________________

Eradication:
________________________

Recovery:
________________________

Monitoring:
________________________
```

---

# Identity Maturity

## Level 1 — Reactive

- Basic authentication logs
- Manual account disabling
- Limited MFA

## Level 2 — Repeatable

- MFA
- Standard account response
- Basic identity monitoring

## Level 3 — Defined

- Conditional access
- Privileged identity management
- Centralized identity telemetry
- Cloud audit logging

## Level 4 — Measured

- Risk-based authentication
- Identity analytics
- Session monitoring
- Automated response

## Level 5 — Optimized

- Phishing-resistant authentication
- Continuous identity risk evaluation
- Automated containment
- Just-in-time privilege
- Identity threat detection and response

---

# Identity Security Metrics

### MFA Coverage

Percentage of applicable identities protected by MFA.

### Privileged Account Coverage

Percentage of privileged identities under enhanced controls.

### Credential Rotation Time

Time required to rotate compromised credentials.

### Session Revocation Time

Time between compromise identification and session invalidation.

### Identity Incident MTTD

Mean time to detect identity compromise.

### Identity Incident MTTC

Mean time to contain identity compromise.

### Privilege Exposure

Amount of unnecessary privilege present in the environment.

---

# Interview Questions

## 1. Why are identity incidents difficult?

Because a compromised identity can access many independent systems without requiring traditional malware.

---

## 2. What is the difference between authentication and authorization?

Authentication establishes identity.

Authorization determines what the identity is allowed to access or perform.

---

## 3. Is a successful login proof of compromise?

No.

A successful login must be evaluated using context such as device, source, time, authentication method, behavior, and subsequent activity.

---

## 4. What is MFA fatigue?

Repeated MFA prompts designed to pressure a user into approving an authentication request.

---

## 5. How would you respond to a compromised privileged account?

Priorities include:

```text
Protect Identity
Revoke Sessions
Rotate Credentials
Review Privileges
Investigate Activity
Identify Persistence
Scope Related Systems
Monitor
```

---

## 6. Why isn't a password reset always sufficient?

Existing sessions, refresh tokens, API keys, OAuth grants, certificates, or other credentials may remain valid.

---

## 7. What is OAuth abuse?

Unauthorized or malicious use of delegated application permissions to access resources.

---

## 8. How would you investigate a compromised cloud identity?

Review:

- Authentication
- API activity
- IAM changes
- Resource access
- Credentials
- Roles
- Persistence

---

## 9. What is a service account?

A non-human identity used by applications, services, workloads, or automation.

---

## 10. Why are service accounts dangerous?

They may have long-lived credentials, broad permissions, and limited monitoring.

---

## 11. What is password spraying?

Attempting a small number of common passwords against many accounts rather than repeatedly attacking one account.

---

## 12. What is credential stuffing?

Using previously leaked username/password combinations against other services.

---

## 13. What is identity persistence?

Mechanisms that allow an attacker to maintain access after the original credential or session has been removed.

Examples include:

- New accounts
- API keys
- OAuth grants
- Service principals
- SSH keys
- IAM roles

---

## 14. What would you investigate after discovering an attacker-created API key?

Determine:

```text
Who created it?
When?
From where?
What permissions?
What was it used for?
Which resources were accessed?
Was data accessed?
Does it still exist?
```

---

# Integration With Threat Hunting

Identity incidents provide strong hunt opportunities.

Example:

```text
Compromised Account
       │
       ▼
Known Source IP
       │
       ▼
Search Authentication Logs
       │
       ▼
Find Other Accounts
       │
       ▼
Potential Campaign
```

---

# Integration With Detection Engineering

Forensic and incident findings can become detections:

```text
Incident
   │
   ▼
Attacker Created API Key
   │
   ▼
Detection Rule
   │
   ▼
Alert on Future Key Creation
```

Other examples:

- Privilege escalation
- MFA changes
- New OAuth consent
- New service principal
- Unusual role assignment

---

# Enterprise Identity Incident Architecture

```text
                       Identity Provider
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
            Users        Service IDs       Applications
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                       Authentication
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                  Device     MFA       Session
                    │         │         │
                    └─────────┼─────────┘
                              ▼
                         Authorization
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
            SaaS            Cloud          Internal
                              │
                              ▼
                         Audit Logs
                              │
                              ▼
                              SIEM
                              │
                              ▼
                         Detection
                              │
                              ▼
                       Incident Response
```

---

# Key Takeaways

Identity is one of the most important security boundaries in modern enterprise environments.

A mature identity incident response process is:

```text
Detect
  ↓
Validate
  ↓
Investigate Authentication
  ↓
Determine Scope
  ↓
Secure Credentials
  ↓
Revoke Sessions
  ↓
Remove Persistence
  ↓
Review Privileges
  ↓
Investigate Cloud / SaaS Activity
  ↓
Recover
  ↓
Monitor
```

The most important principles are:

- Investigate identity, not just endpoints.
- Treat privileged identity compromise as high risk.
- Password reset alone may not remove attacker access.
- Revoke sessions and tokens when appropriate.
- Investigate OAuth grants.
- Review API keys and service identities.
- Examine cloud API activity.
- Review privilege changes.
- Investigate identity persistence.
- Protect and monitor administrative accounts.
- Use phishing-resistant authentication where appropriate.
- Integrate identity telemetry with the SIEM and incident response process.

> **In modern environments, identity is infrastructure. Protecting the identity plane is therefore equivalent to protecting the systems that identity controls.**

---

# References

### NIST

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

Digital Identity Guidelines:

https://pages.nist.gov/800-63-3/

### CISA

Identity and access management resources:

https://www.cisa.gov/

### MITRE ATT&CK

Credential Access:

https://attack.mitre.org/tactics/TA0006/

Persistence:

https://attack.mitre.org/tactics/TA0003/

Privilege Escalation:

https://attack.mitre.org/tactics/TA0004/

### OWASP

Authentication guidance:

https://owasp.org/www-project-authentication-cheat-sheet/

### Cloud Security Alliance

https://cloudsecurityalliance.org/

### CIS Controls

https://www.cisecurity.org/controls

### FIRST

https://www.first.org/

---

# Chapter Summary

Identity incidents should be investigated as complete attack paths rather than isolated authentication events.

A useful mental model is:

```text
Identity
   │
   ├── Who authenticated?
   ├── From where?
   ├── Using what method?
   ├── On which device?
   ├── With what privileges?
   ├── Accessing which resources?
   ├── Using which sessions/tokens?
   └── Creating what persistence?
```

When those questions are answered, responders can determine the true blast radius of an account compromise.

> **Secure the identity, revoke the access, remove the persistence, investigate the activity, and verify that the attacker no longer has a path back into the environment.**
