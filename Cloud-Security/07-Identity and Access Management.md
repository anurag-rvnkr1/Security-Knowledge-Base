# Identity and Access Management (IAM)

## Overview

Identity and Access Management (IAM) is the foundation of cloud security. It is a framework of policies, technologies, and processes used to ensure that the **right identities have the right level of access to the right resources at the right time**.

Unlike traditional on-premises environments where network perimeters formed the primary security boundary, cloud computing places **identity at the center of security**. Every action performed in a cloud environment—whether creating a virtual machine, accessing a storage bucket, deploying a container, or invoking a serverless function—is authenticated and authorized through IAM.

Modern cloud platforms such as AWS, Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI), and IBM Cloud all implement comprehensive IAM systems to protect cloud resources.

A properly designed IAM architecture helps organizations:

- Protect sensitive resources
- Enforce least privilege
- Prevent unauthorized access
- Meet compliance requirements
- Reduce insider threats
- Secure machine identities
- Enable Zero Trust architectures
- Improve auditability

Poor IAM practices remain one of the leading causes of cloud security incidents.

---

## Why It Matters

Identity is often referred to as the **new security perimeter**.

Traditional security models assumed that anything inside a trusted corporate network could be trusted. Cloud computing fundamentally changes this assumption because users, applications, workloads, and APIs operate from multiple locations across the internet.

As a result, security decisions are based on **identity rather than network location**.

```
Traditional Security

Internet

↓

Firewall

↓

Trusted Network

↓

Resources


Cloud Security

User

↓

Identity Verification

↓

Authorization

↓

Cloud Resource
```

A compromised identity can provide attackers with legitimate access to cloud resources without exploiting software vulnerabilities.

Effective IAM helps organizations:

- Prevent account compromise
- Minimize attack surfaces
- Enforce security policies
- Protect sensitive information
- Enable secure remote work
- Support regulatory compliance
- Improve visibility into user activities

---

## Architecture

A typical cloud IAM architecture consists of multiple interconnected components.

```
                    Users

      Employees | Developers | Contractors

                       │

                       ▼

             Identity Provider (IdP)

                       │

          Authentication (MFA, Password,
             Certificate, Biometrics)

                       │

                       ▼

             Identity and Access Management

        ┌──────────────┼──────────────┐

        ▼              ▼              ▼

   Roles          Policies       Groups

        │              │              │

        └──────────────┼──────────────┘

                       ▼

                Authorization Engine

                       │

                       ▼

             Cloud Resources

   Compute | Storage | Database | Network

 Containers | APIs | Serverless | Secrets
```

The IAM system evaluates every request before allowing access to cloud resources.

---

## Key Concepts

### Identity

An identity represents any entity that can authenticate and interact with cloud resources.

Examples include:

- Human users
- Administrators
- Developers
- Applications
- Services
- Virtual machines
- Containers
- APIs
- Serverless functions

Identities are broadly categorized into:

| Identity Type | Description |
|--------------|-------------|
| Human Identity | Employees, contractors, administrators |
| Machine Identity | Applications, virtual machines, containers |
| Service Identity | Cloud services communicating with other services |
| Federated Identity | External identities authenticated through an Identity Provider (IdP) |

Every identity should have a unique identifier and appropriate permissions.

---

### Authentication

Authentication answers the question:

> **"Who are you?"**

Authentication verifies the identity of a user or service before granting access.

Common authentication methods include:

- Username and password
- Multi-Factor Authentication (MFA)
- Biometrics
- Security keys
- Smart cards
- Certificates
- OAuth authentication
- OpenID Connect (OIDC)
- Single Sign-On (SSO)

```
User

↓

Username

↓

Password

↓

MFA Verification

↓

Authenticated
```

Authentication does **not** determine what a user can do—it only verifies identity.

---

### Authorization

Authorization answers the question:

> **"What are you allowed to do?"**

Once an identity has been authenticated, IAM evaluates permissions before allowing operations.

Examples:

Developer

Allowed:

- Deploy applications
- View logs
- Read source repositories

Not Allowed:

- Delete production databases
- Modify IAM policies
- Access payroll systems

Authorization is enforced through IAM policies and roles.

---

### Principal

A **Principal** is an authenticated identity requesting access to a cloud resource.

Examples include:

- User accounts
- Applications
- Virtual machines
- Kubernetes workloads
- Cloud services
- API clients

Every access request originates from a principal.

---

### Resource

A resource is any object protected by IAM.

Examples include:

- Virtual Machines
- Object Storage Buckets
- Databases
- Kubernetes Clusters
- Serverless Functions
- Virtual Networks
- APIs
- Secrets
- Key Vaults
- Monitoring Services

Resources define what identities can access.

---

### Permissions

Permissions specify the operations an identity can perform on a resource.

Examples:

```
Storage Bucket

Read

Write

Delete

List

Update Permissions
```

Each permission should be granted only when required.

---

### Policies

Policies are collections of permissions expressed as rules.

Policies define:

- Allowed actions
- Denied actions
- Applicable resources
- Conditions
- Constraints

Example:

```
Developer Policy

Allow

↓

Read Source Code

Deploy Application

View Logs

---------------------

Deny

↓

Delete Production Database
```

Policies are the primary mechanism for implementing authorization.

---

### Roles

A role is a collection of permissions assigned to identities.

Instead of assigning permissions individually, organizations assign roles.

Example:

| Role | Permissions |
|------|-------------|
| Cloud Administrator | Full administrative access |
| Developer | Deploy applications, view logs |
| Security Analyst | Read security logs, investigate alerts |
| Database Administrator | Manage databases only |
| Auditor | Read-only access to audit resources |

Role-based administration improves scalability and consistency.

---

### Groups

Groups simplify permission management by organizing users.

```
Engineering Group

↓

Developer A

Developer B

Developer C

↓

Developer Role Assigned
```

Instead of assigning permissions individually, permissions are assigned to groups.

---

### Role-Based Access Control (RBAC)

RBAC grants permissions based on organizational roles.

```
Employee

↓

Assigned Role

↓

Permissions

↓

Cloud Resource
```

Advantages:

- Easier administration
- Consistent permissions
- Reduced configuration errors
- Simplified audits
- Better scalability

RBAC is widely used across enterprise cloud platforms.

---

### Attribute-Based Access Control (ABAC)

ABAC evaluates attributes rather than static roles.

Attributes may include:

User attributes:

- Department
- Location
- Employment type

Resource attributes:

- Classification
- Environment
- Owner

Environmental attributes:

- Time
- Device
- IP address
- Risk score

Example:

```
IF

Department = Finance

AND

Location = India

AND

MFA = Enabled

THEN

Allow Access
```

ABAC enables highly granular authorization decisions.

---

### Principle of Least Privilege (PoLP)

The Principle of Least Privilege states that every identity should receive only the minimum permissions required to perform its responsibilities.

```
Developer

↓

Deploy Application

Read Logs

────────────────────

No Billing Access

No IAM Management

No Database Deletion
```

Benefits include:

- Reduced attack surface
- Lower insider risk
- Better compliance
- Easier auditing
- Reduced blast radius during compromise

PoLP is considered a fundamental cloud security principle.

---

### Separation of Duties (SoD)

Critical operations should require different individuals or teams.

Example:

| Task | Responsible Team |
|------|------------------|
| Code Development | Development Team |
| Security Review | Security Team |
| Production Approval | Change Advisory Board |
| Deployment | DevOps Team |

Separation of Duties reduces fraud, accidental changes, and abuse of privileged access.

---

### Multi-Factor Authentication (MFA)

MFA requires users to provide two or more independent authentication factors.

Typical factors include:

Something you know:

- Password
- PIN

Something you have:

- Mobile authenticator
- Hardware security key
- Smart card

Something you are:

- Fingerprint
- Facial recognition
- Iris scan

```
Password

+

Authenticator App

↓

Access Granted
```

Enabling MFA significantly reduces the risk of credential theft and phishing attacks.

---

### Single Sign-On (SSO)

Single Sign-On enables users to authenticate once and access multiple applications.

```
User

↓

Identity Provider

↓

Authenticated Once

↓

Cloud Portal

↓

Email

↓

DevOps Tools

↓

Monitoring Platform
```

Benefits include:

- Improved user experience
- Reduced password fatigue
- Centralized identity management
- Simplified access revocation

---

### Identity Federation

Federation allows identities from external identity providers to access cloud resources without creating separate accounts.

Common federation protocols include:

- SAML 2.0
- OAuth 2.0
- OpenID Connect (OIDC)

```
Corporate Identity Provider

↓

Federation

↓

Cloud Platform

↓

Cloud Resources
```

Federation supports centralized identity management across multiple platforms.

---

### Privileged Access

Privileged identities possess elevated permissions capable of modifying critical cloud resources.

Examples include:

- Cloud administrators
- Subscription owners
- Root accounts
- Security administrators
- Organization administrators

These accounts require enhanced protections such as:

- MFA
- Just-In-Time (JIT) access
- Session monitoring
- Approval workflows
- Privileged Access Management (PAM)

---

## How It Works

Identity and Access Management (IAM) operates through a sequence of authentication, authorization, and policy evaluation steps before granting access to cloud resources.

Every request—whether initiated by a human user, application, virtual machine, container, or API—is evaluated against configured IAM policies.

The following workflow illustrates a typical IAM authorization process.

```
          User / Application

                  │

                  ▼

        Identity Authentication

                  │

         Password / MFA / SSO

                  │

                  ▼

      Authentication Successful?

         │                    │

       Yes                    No

        │                     │

        ▼                     ▼

 Retrieve Roles & Policies   Access Denied

        │

        ▼

 Evaluate Authorization Rules

        │

        ▼

 Resource Access Granted?
      │               │

     Yes             No

      │               │

      ▼               ▼

 Access Granted   Access Denied

      │

      ▼

 Audit Logs Generated
```

Every successful and unsuccessful request should be recorded for auditing and forensic investigations.

---

### Step 1 – Identity Creation

Before a user can access cloud resources, an identity must exist.

Examples include:

- Employee accounts
- Administrator accounts
- Service accounts
- Applications
- Virtual machines
- Containers
- Serverless functions

Each identity should have:

- Unique identifier
- Authentication method
- Assigned roles
- Security policies
- Ownership
- Lifecycle management

Example:

```
Developer

↓

Corporate Identity

↓

Cloud IAM Account

↓

Developer Role Assigned
```

---

### Step 2 – Authentication

The identity proves who it is.

Authentication methods may include:

- Password
- Passkey
- Multi-Factor Authentication
- Security key
- Certificate
- Smart card
- Biometrics

Example:

```
Username

↓

Password

↓

MFA Challenge

↓

Identity Verified
```

Authentication alone does not provide access.

---

### Step 3 – Token Generation

After successful authentication, the Identity Provider (IdP) usually issues a temporary authentication token.

Examples:

- JWT (JSON Web Token)
- OAuth Access Token
- SAML Assertion
- OIDC ID Token

```
Identity Verified

↓

Token Issued

↓

Token Contains

• Identity

• Roles

• Expiration

• Claims
```

Temporary credentials are preferred over long-lived credentials because they reduce exposure if compromised.

---

### Step 4 – Authorization

IAM evaluates whether the authenticated identity has permission to perform the requested action.

Example request:

```
Developer

↓

Delete Production Database
```

IAM evaluates:

```
Developer Role

↓

Allowed Actions

↓

Requested Action

↓

Decision
```

If permission does not exist, the request is denied.

---

### Step 5 – Policy Evaluation

Cloud platforms evaluate multiple policy sources before making an authorization decision.

Typical evaluation includes:

```
Identity Policy

↓

Resource Policy

↓

Organization Policy

↓

Permission Boundary

↓

Conditional Rules

↓

Final Decision
```

An explicit deny normally overrides allow statements.

---

### Step 6 – Resource Access

If authorization succeeds:

```
Identity

↓

Authorized

↓

Cloud Resource

↓

Operation Executed
```

Otherwise:

```
Identity

↓

Authorization Failed

↓

Access Denied
```

---

### Step 7 – Audit Logging

Every request should be logged.

Typical log information includes:

- Identity
- Timestamp
- Source IP
- Requested resource
- Action performed
- Authentication method
- Result
- Geographic location
- Device information

Example:

```
09:42 UTC

↓

Developer

↓

Create Virtual Machine

↓

Success
```

These logs support:

- Security investigations
- Compliance
- Threat hunting
- Incident response

---

## IAM Authorization Flow

```
User

↓

Authenticate

↓

Identity Verified

↓

Retrieve Roles

↓

Retrieve Policies

↓

Evaluate Conditions

↓

Allow or Deny

↓

Audit Log
```

This process occurs within milliseconds for most cloud platforms.

---

## Practical Example

### Example 1 – Developer Deploying an Application

An application developer wants to deploy a new version of a web application.

```
Developer

↓

Authenticate

↓

MFA Verification

↓

Developer Role

↓

Deploy Application

↓

Deployment Successful
```

Permissions granted:

- Deploy applications
- Read logs
- View monitoring dashboards

Permissions denied:

- Delete storage buckets
- Modify IAM policies
- Manage billing
- Access HR databases

This follows the Principle of Least Privilege.

---

### Example 2 – Unauthorized Database Deletion

A developer accidentally attempts to delete a production database.

```
Developer

↓

Delete Database

↓

IAM Policy Evaluation

↓

Permission Missing

↓

Access Denied

↓

Security Log Created
```

IAM prevents accidental or malicious destructive actions.

---

### Example 3 – Administrator Access

Cloud administrators require elevated permissions.

```
Administrator

↓

Authenticate

↓

MFA

↓

Privileged Role

↓

Modify Firewall Rules

↓

Access Granted
```

Administrative actions should be:

- Logged
- Monitored
- Approved where appropriate
- Regularly reviewed

---

### Example 4 – Machine Identity

Applications frequently access cloud resources without human intervention.

```
Application

↓

Managed Identity

↓

Temporary Token

↓

Database Access

↓

Retrieve Records
```

No passwords are stored inside the application.

---

### Example 5 – Federated Login

An employee signs in using corporate credentials.

```
Employee

↓

Corporate Identity Provider

↓

SAML Authentication

↓

Cloud Platform

↓

Cloud Dashboard
```

The employee never creates a separate cloud password.

---

### Example 6 – API Access

A monitoring application calls a cloud API.

```
Application

↓

OAuth Token

↓

Cloud API

↓

Policy Evaluation

↓

Metrics Returned
```

The API validates the token before processing requests.

---

## IAM Decision Matrix

| Identity | Requested Action | Permission | Result |
|----------|------------------|------------|--------|
| Developer | Deploy Application | Allow | Granted |
| Developer | Delete Database | Deny | Blocked |
| Auditor | Read Logs | Allow | Granted |
| Auditor | Modify Resources | Deny | Blocked |
| Administrator | Create VM | Allow | Granted |
| Guest User | View Billing | Deny | Blocked |

---

## Common Authentication Methods

| Method | Security Level | Typical Use Case |
|---------|---------------|------------------|
| Password | Medium | General user access |
| Password + MFA | High | Administrative access |
| Passkey | Very High | Passwordless authentication |
| Smart Card | High | Enterprise environments |
| Hardware Security Key | Very High | Privileged users |
| Certificate Authentication | High | Servers and devices |
| Biometrics | High | Mobile devices and secure workstations |

---

## Common Authorization Models

| Model | Description | Example |
|--------|-------------|---------|
| RBAC | Access based on roles | Developer role |
| ABAC | Access based on attributes | Department = Finance |
| DAC | Resource owner grants permissions | File sharing |
| MAC | Central authority controls access | Government systems |

---

## Indicators of IAM Security Issues (Detection)

Effective IAM monitoring helps identify unauthorized access attempts, privilege misuse, and identity-based attacks before they lead to compromise.

Common indicators include:

### Unusual Login Activity

Examples:

- Logins from unfamiliar geographic locations
- Impossible travel events
- Logins outside business hours
- Simultaneous logins from different countries

Example:

```
09:00

India Login

↓

09:20

Germany Login

↓

Impossible Travel Alert
```

---

### Repeated Authentication Failures

Large numbers of failed login attempts may indicate:

- Password spraying
- Credential stuffing
- Brute-force attacks
- Account enumeration

Example indicators:

- Hundreds of failed logins
- Multiple usernames targeted
- Sequential password attempts

---

### Excessive Privilege Changes

Security teams should investigate:

- New administrator accounts
- Privilege escalation
- Unexpected role assignments
- Policy modifications
- Root account usage

---

### Dormant Account Activity

Inactive accounts suddenly becoming active may indicate compromise.

```
Account Inactive

↓

180 Days

↓

Unexpected Login

↓

Security Investigation
```

---

### Suspicious API Usage

Indicators include:

- Unusual API calls
- Access from unknown IP addresses
- Large numbers of failed API requests
- Unexpected service account activity

---

### Machine Identity Abuse

Security monitoring should detect:

- Service accounts used by humans
- Tokens used from unexpected locations
- Expired credentials being reused
- Unauthorized application access

---

### IAM Monitoring Sources

Security teams commonly analyze:

- Authentication logs
- Authorization logs
- Cloud audit logs
- Identity Provider logs
- API gateway logs
- VPN logs
- Privileged access logs
- Federation events

---

## Detection Best Practices

- Enable audit logging for all IAM activities.
- Monitor privileged account usage continuously.
- Detect impossible travel events.
- Alert on privilege escalation attempts.
- Review failed authentication trends.
- Monitor inactive accounts.
- Detect unusual API usage patterns.
- Integrate IAM logs with SIEM platforms.
- Perform regular access reviews.
- Investigate all unexpected administrative activities.

---

