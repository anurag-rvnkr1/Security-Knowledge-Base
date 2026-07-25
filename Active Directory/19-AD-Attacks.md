# 19-AD-Attacks.md

# Part 1 — Introduction to Active Directory Attacks, Attack Lifecycle, Initial Access, Identity Attacks and Defensive Understanding

> **Important Note**
>
> This chapter is intended **solely for defensive cybersecurity education, security awareness, blue-team training, and authorized security assessments**. Understanding attacker techniques helps defenders detect, prevent, and respond to threats more effectively. All examples are presented from a defensive perspective.

---

# Learning Objectives

After completing this part, you will understand:

- Why Active Directory is targeted
- The Active Directory attack lifecycle
- Common attack objectives
- Identity-based attacks
- Credential-related attacks (conceptual)
- Initial Access
- Privilege Escalation (conceptual)
- Lateral Movement (conceptual)
- Persistence (conceptual)
- Defensive security principles

---

# Introduction

Modern cyber attacks frequently target **identity systems** rather than individual computers.

Since Active Directory controls:

- Authentication
- Authorization
- User identities
- Computer identities
- Group Policies
- Administrative privileges

it often becomes the primary objective after an attacker gains an initial foothold inside an enterprise network.

---

# Why Attackers Target Active Directory

An attacker interested in Active Directory may seek to:

- Access sensitive business data
- Escalate privileges
- Expand access across the environment
- Disrupt business operations
- Maintain unauthorized persistence
- Obtain administrative control

Understanding these objectives enables defenders to implement appropriate security controls.

---

# Active Directory Attack Lifecycle

A simplified attack lifecycle can be represented as:

```
Reconnaissance

        │

        ▼

Initial Access

        │

        ▼

Credential Abuse

        │

        ▼

Privilege Escalation

        │

        ▼

Lateral Movement

        │

        ▼

Persistence

        │

        ▼

Objective Achieved
```

Security teams should aim to detect and disrupt activity at every stage.

---

# Enterprise Attack Surface

```
              Active Directory

                     │

     ┌───────────────┼────────────────┐

     ▼               ▼                ▼

Users          Computers      Domain Controllers

     ▼               ▼                ▼

Applications    File Servers    Authentication

                     │

                     ▼

             Business Resources
```

Every connected identity and system contributes to the overall attack surface.

---

# Common Attack Goals

Attackers generally attempt to:

- Obtain credentials
- Increase privileges
- Access sensitive systems
- Maintain access
- Avoid detection

These goals are not unique to Active Directory but are particularly impactful within identity infrastructure.

---

# Initial Access

Initial access refers to the first successful entry into an organization's environment.

Possible sources include:

- Compromised user credentials
- Phishing
- Exploited vulnerabilities
- Misconfigurations
- Third-party compromise

Initial access does **not** necessarily imply compromise of Active Directory itself.

---

# Example Attack Progression

```
Compromised Workstation

↓

Authenticated User

↓

Network Access

↓

Attempted Privilege Escalation

↓

Attempted Lateral Movement

↓

Sensitive Resources
```

Each stage provides defenders with opportunities to detect and contain the activity.

---

# Identity-Based Attacks

Modern attacks frequently focus on identities instead of infrastructure alone.

Targets include:

- User accounts
- Administrative accounts
- Service accounts
- Privileged groups
- Authentication mechanisms

Protecting identities significantly improves enterprise resilience.

---

# Credential Abuse (Conceptual)

Credential abuse involves the unauthorized use of valid credentials.

Examples include:

- Stolen passwords
- Reused passwords
- Weak passwords
- Exposed privileged accounts

Strong credential hygiene helps reduce this risk.

---

# Privilege Escalation (Conceptual)

Privilege escalation occurs when an attacker attempts to obtain permissions beyond those originally available.

Example:

```
Standard User

↓

Attempt to Gain

↓

Administrative Rights
```

Preventing excessive privilege and monitoring administrative changes are key defensive measures.

---

# Lateral Movement (Conceptual)

After gaining access to one system, an attacker may attempt to move to additional systems.

Example:

```
Workstation

↓

Application Server

↓

File Server

↓

Administrative Systems
```

Network segmentation, monitoring, and least privilege help reduce lateral movement opportunities.

---

# Persistence (Conceptual)

Persistence refers to maintaining unauthorized access after an initial compromise.

Potential indicators include:

- Unexpected privileged accounts
- Unauthorized scheduled tasks
- Unknown services
- Suspicious configuration changes

Regular reviews and auditing help identify persistence mechanisms.

---

# Defense-in-Depth Against AD Attacks

```
Security Awareness

↓

Identity Protection

↓

Least Privilege

↓

Administrative Tiering

↓

Endpoint Protection

↓

Network Segmentation

↓

Logging

↓

SIEM

↓

Incident Response
```

Multiple layers of defense increase the likelihood of detecting and stopping attacks.

---

# MITRE ATT&CK Alignment

Many Active Directory attacks align with tactics documented in the MITRE ATT&CK framework, including:

- Initial Access
- Credential Access
- Discovery
- Privilege Escalation
- Lateral Movement
- Persistence
- Defense Evasion

Using a common framework helps defenders organize detection and response strategies.

---

# High-Value Assets

The following systems require the highest level of protection:

```
Tier 0 Assets

├── Domain Controllers

├── Enterprise Admin Accounts

├── Domain Admin Accounts

├── Certificate Services

├── Authentication Infrastructure

└── Identity Management Systems
```

Compromise of these assets can have organization-wide consequences.

---

# Early Warning Indicators

Security teams should investigate:

- Unusual privileged logons
- Unexpected group membership changes
- Multiple failed authentication attempts
- Administrative activity outside normal hours
- Sudden creation of privileged accounts
- Unauthorized GPO modifications
- Replication anomalies
- Unexpected authentication failures

These indicators may have legitimate causes but warrant investigation.

---

# Enterprise Example

Company:

```
Fabrikam Industries
```

Environment:

- 90,000 Users
- 36 Domain Controllers
- Multiple Regions

Security Controls:

- Multi-Factor Authentication
- Tiered Administration
- Centralized Logging
- SIEM Monitoring
- Dedicated Administrative Workstations
- Quarterly Privileged Access Reviews

When suspicious privileged logon activity is detected, the SOC:

1. Validates the alert.
2. Reviews authentication logs.
3. Confirms account ownership.
4. Contains affected accounts if necessary.
5. Documents findings.
6. Performs a post-incident review.

---

# Cybersecurity Perspective

Defenders should focus on:

- Reducing attack surface
- Protecting privileged identities
- Monitoring authentication
- Reviewing administrative changes
- Limiting unnecessary privileges
- Maintaining accurate asset inventories
- Practicing incident response

Understanding attacker objectives allows defenders to deploy effective preventive and detective controls.

---

# Hands-on Lab

## Objective

Map potential attack paths from a defender's perspective.

### Step 1

Identify:

- Tier 0 assets
- Domain Controllers
- Privileged groups
- Critical authentication systems

---

### Step 2

Review:

- Privileged account memberships
- Administrative workstations
- Authentication logs

Document any unusual observations.

---

### Step 3

Create a simple attack lifecycle diagram for your lab environment and identify where security controls exist.

---

### Step 4

List three controls that could detect:

- Unauthorized privileged logons
- Unexpected group membership changes
- Administrative configuration changes

---

### Step 5

Recommend improvements based on your findings.

---

# Interview Questions

### Q1: Why is Active Directory a common target?

**Answer:** Because it manages authentication, authorization, identities, and privileged access across the enterprise, making it a high-value target.

---

### Q2: What is meant by the attack lifecycle?

**Answer:** It describes the progression of an attack from initial access through privilege escalation, lateral movement, persistence, and the attacker's objectives.

---

### Q3: Why are privileged accounts attractive targets?

**Answer:** They provide elevated permissions that can significantly increase an attacker's access if compromised.

---

### Q4: What is lateral movement?

**Answer:** Lateral movement is an attacker's attempt to move from one compromised system to additional systems within the environment.

---

### Q5: What is persistence?

**Answer:** Persistence refers to techniques used to maintain unauthorized access after an initial compromise.

---

### Q6: How can organizations reduce Active Directory attack risk?

**Answer:** By applying least privilege, administrative tiering, strong authentication, monitoring, logging, security baselines, and regular security reviews.

---

# Best Practices

- Protect Tier 0 assets with the strongest controls.
- Enable comprehensive logging and monitoring.
- Use dedicated administrative accounts.
- Implement least privilege.
- Review privileged groups regularly.
- Conduct periodic security assessments.
- Test incident response procedures.
- Maintain accurate documentation.

---

# Common Mistakes

- Granting excessive administrative privileges.
- Ignoring authentication anomalies.
- Failing to review privileged group memberships.
- Treating Domain Controllers like ordinary servers.
- Delaying investigation of suspicious administrative activity.
- Neglecting identity-focused security controls.

---

# Key Takeaways

- Active Directory is a primary target because it controls enterprise identity and access.
- Understanding the attack lifecycle helps defenders deploy layered security controls.
- Identity protection, least privilege, monitoring, and rapid incident response are essential defensive strategies.
- Every stage of an attack presents opportunities for detection and containment.
- A mature Active Directory security program combines prevention, detection, response, and continuous improvement.

---

**Next:** Part 2