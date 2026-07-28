# 19-Broken-Access-Control.md

# Part 1 — Fundamentals of Broken Access Control, Authorization Models, Trust Boundaries, and Enterprise Overview

> **"Authentication answers *'Who are you?'* Authorization answers *'What are you allowed to do?'* Broken Access Control occurs when an application fails to properly enforce those permissions."**

---

# Learning Objectives

After completing this part, you will understand:

- What Broken Access Control Is
- Authentication vs Authorization
- Access Control Fundamentals
- Authorization Models
- Trust Boundaries
- Least Privilege Principle
- Enterprise Access Control
- Business Impact
- Common Misconceptions
- Industry Importance

---

# What is Broken Access Control?

**Broken Access Control** occurs when an application allows users to perform actions or access resources beyond their intended permissions.

Instead of enforcing authorization rules consistently, the application unintentionally exposes sensitive functionality or data.

---

# Authentication vs Authorization

Many beginners confuse these concepts.

```
User

↓

Authentication

↓

Identity Verified

↓

Authorization

↓

Permission Check

↓

Access Granted

OR

Access Denied
```

Authentication always comes **before** authorization.

---

# Simple Example

Imagine a corporate office.

```
Building Entrance

↓

Security Guard

↓

Identity Verified

↓

Office Floor Access

↓

Department Permission

↓

Meeting Room Access
```

- Identity verification = Authentication
- Floor and room permissions = Authorization

A person may be an employee but still cannot enter every department.

---

# Why Access Control Matters

Every enterprise application contains sensitive resources.

```
Application

│

├── Customer Data

├── Employee Records

├── Financial Reports

├── Admin Dashboard

├── Configuration

└── APIs
```

Each resource requires different authorization rules.

---

# Enterprise Authorization Model

```
User

↓

Identity

↓

Assigned Role

↓

Permission Evaluation

↓

Business Rules

↓

Access Decision

↓

Resource
```

Authorization decisions should always occur on the server side.

---

# Security Goal

The objective of access control is simple:

```
Authorized User

↓

Authorized Resource

↓

Authorized Action

↓

Allowed

────────────

Everything Else

↓

Denied
```

---

# Principle of Least Privilege

One of the most important security principles.

```
Maximum Permissions

↓

Remove Unnecessary Rights

↓

Minimum Required Access

↓

Reduced Risk
```

Users should receive only the permissions necessary for their responsibilities.

---

# Why Least Privilege Works

```
Compromised Account

↓

Limited Permissions

↓

Limited Damage
```

Restricting permissions reduces the impact of account compromise.

---

# Access Control Components

```
Access Control

│

├── Users

├── Roles

├── Permissions

├── Resources

├── Policies

└── Enforcement
```

Every component contributes to secure authorization.

---

# Resources

Resources include anything that requires protection.

Examples:

- Web pages
- Files
- APIs
- Database records
- Images
- Administrative functions
- Cloud storage
- Reports

---

# Actions

Users perform actions on resources.

```
Resource

↓

Read

Write

Update

Delete

Share

Approve

Export
```

Each action may require different permissions.

---

# Authorization Decision

```
Request

↓

Identity

↓

Role

↓

Permission

↓

Policy

↓

Decision

↓

Allow

OR

Deny
```

Every protected request should undergo authorization checks.

---

# Trust Boundaries

Applications contain multiple trust boundaries.

```
Internet

↓

Browser

↓

Web Server

↓

Application

↓

Database
```

Authorization should never rely solely on data received from untrusted sources.

---

# Server-Side Enforcement

```
User Request

↓

Server

↓

Authorization Check

↓

Decision

↓

Response
```

The server—not the browser—must enforce access control decisions.

---

# Enterprise Example

An HR application:

```
Employee

↓

View Own Profile

↓

Allowed

──────────────

Employee

↓

Modify Payroll

↓

Denied
```

Different users require different capabilities.

---

# Common Authorization Levels

```
Guest

↓

User

↓

Manager

↓

Administrator

↓

Super Administrator
```

Higher privilege levels require stronger protection and additional review.

---

# Access Matrix

| User Role | View Data | Edit Data | Delete Data | Admin Functions |
|-----------|-----------|-----------|--------------|-----------------|
| Guest | ✓ Limited | ✗ | ✗ | ✗ |
| Employee | ✓ | Limited | ✗ | ✗ |
| Manager | ✓ | ✓ | Limited | ✗ |
| Administrator | ✓ | ✓ | ✓ | ✓ |

---

# Why Broken Access Control Happens

Common reasons include:

- Missing authorization checks
- Incorrect permission logic
- Inconsistent enforcement
- Complex business rules
- Rapid application growth
- Legacy code
- Poor testing

---

# Business Impact

Broken Access Control can result in:

```
Unauthorized Access

↓

Sensitive Data Exposure

↓

Business Disruption

↓

Financial Loss

↓

Regulatory Issues

↓

Reputation Damage
```

---

# Defense in Depth

Authorization should work alongside other controls.

```
Authentication

↓

Authorization

↓

Input Validation

↓

Logging

↓

Monitoring

↓

Incident Response
```

No single control provides complete protection.

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| Authentication automatically provides authorization | Authentication only verifies identity |
| Administrators need unrestricted access everywhere | Administrative access should still follow least privilege |
| Client-side restrictions are sufficient | Authorization must be enforced on the server |
| Internal users are always trusted | Insider threats and compromised accounts exist |

---

# Enterprise Workflow

```
User Login

↓

Authentication

↓

Role Assignment

↓

Permission Evaluation

↓

Business Rule Validation

↓

Access Granted

↓

Audit Logging
```

---

# Hands-on Lab (Conceptual)

1. Select a web application with multiple user roles.
2. List all available resources.
3. Identify which roles should access each resource.
4. Create a simple authorization matrix.
5. Review where server-side authorization checks should occur.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is Broken Access Control?
2. What is the difference between authentication and authorization?
3. Why is server-side authorization essential?
4. What is the principle of least privilege?
5. What are trust boundaries?
6. Why are authorization checks required for every protected request?
7. What types of resources require access control?
8. Why is client-side authorization insufficient?
9. What business risks result from broken access control?
10. Why is Broken Access Control ranked highly in the OWASP Top 10?

---

# Best Practices

- Enforce authorization on the server for every protected request.
- Apply the principle of least privilege to all users and services.
- Define clear roles and permissions.
- Maintain a documented authorization matrix.
- Review access rights regularly.
- Log authorization decisions for sensitive operations.
- Test authorization throughout the application's lifecycle.

---

# Common Mistakes

- Confusing authentication with authorization.
- Trusting client-side controls.
- Granting excessive permissions.
- Skipping authorization checks for internal users.
- Using inconsistent authorization logic across different endpoints.
- Failing to review permissions after role or application changes.

---

# Key Takeaways

- Authentication verifies identity; authorization determines permissions.
- Broken Access Control occurs when authorization rules are not properly enforced.
- Server-side authorization is mandatory for secure applications.
- Least privilege significantly reduces business risk.
- Access control is a foundational security mechanism across all enterprise applications.

# 19-Broken-Access-Control.md

# Part 2 — Access Control Models, Authorization Mechanisms, Privilege Escalation, IDOR, and Enterprise Design

> **"Access control is not a single security check—it is a collection of authorization rules applied consistently across every resource, operation, API, and business process."**

---

# Learning Objectives

After completing this part, you will understand:

- Access Control Models
- Authorization Mechanisms
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Discretionary & Mandatory Access Control
- Horizontal & Vertical Privilege Escalation
- Insecure Direct Object References (IDOR)
- Enterprise Authorization Design
- Common Authorization Weaknesses
- Defense Strategies

---

# Access Control Models

Organizations use different models depending on business requirements.

```
Access Control

│

├── RBAC

├── ABAC

├── DAC

├── MAC

└── Rule-Based Access Control
```

Each model determines **how permissions are evaluated**.

---

# Role-Based Access Control (RBAC)

RBAC assigns permissions to **roles**, and users inherit permissions from those roles.

```
User

↓

Assigned Role

↓

Role Permissions

↓

Resource Access
```

Example:

| Role | Permissions |
|------|-------------|
| Customer | View own profile, place orders |
| Support Agent | View customer records |
| Manager | Approve refunds |
| Administrator | Manage users and settings |

RBAC is one of the most widely used authorization models in enterprise applications.

---

# RBAC Architecture

```
Users

↓

Roles

↓

Permissions

↓

Resources
```

Benefits:

- Easier permission management
- Scalable
- Consistent authorization
- Simplified auditing

---

# Attribute-Based Access Control (ABAC)

ABAC evaluates multiple attributes before granting access.

```
User Attributes

+

Resource Attributes

+

Environment

+

Business Rules

↓

Authorization Decision
```

Possible attributes include:

- Department
- Location
- Time of day
- Device type
- Security clearance
- Resource owner

---

# ABAC Example

```
Employee

Department = Finance

↓

Financial Report

↓

Working Hours?

↓

Corporate Device?

↓

Access Decision
```

ABAC offers greater flexibility than RBAC but is more complex to implement.

---

# Discretionary Access Control (DAC)

In DAC, the resource owner determines who receives access.

```
Owner

↓

Grant Permission

↓

Other User

↓

Access Resource
```

Examples:

- Shared folders
- Personal documents
- Collaboration platforms

---

# Mandatory Access Control (MAC)

MAC enforces access using centrally defined security classifications.

```
Security Label

↓

User Clearance

↓

Policy Evaluation

↓

Allow

OR

Deny
```

Often used in:

- Government
- Military
- Critical infrastructure

---

# Rule-Based Access Control

Rules determine whether access is allowed.

```
Request

↓

Evaluate Rules

↓

Conditions Met?

↓

Allow

OR

Deny
```

Example rules:

- Office hours only
- Corporate network only
- Approved geographic locations

---

# Comparing Authorization Models

| Model | Best For | Flexibility | Complexity |
|--------|----------|------------|------------|
| RBAC | Enterprise applications | Medium | Low |
| ABAC | Dynamic environments | High | High |
| DAC | Collaboration systems | Medium | Medium |
| MAC | High-security environments | Low | High |
| Rule-Based | Conditional access | Medium | Medium |

---

# Privilege Escalation

Privilege escalation occurs when users gain permissions beyond those intended.

```
Normal User

↓

Unexpected Permission

↓

Higher Privilege

↓

Sensitive Resource
```

Authorization failures often lead to privilege escalation.

---

# Horizontal Privilege Escalation

A user accesses resources belonging to another user with the same privilege level.

```
Customer A

↓

Attempts Access

↓

Customer B's Data

↓

Authorization Check Missing

↓

Unauthorized Access
```

The privilege level remains the same, but ownership boundaries are violated.

---

# Vertical Privilege Escalation

A lower-privileged user gains access to higher-privileged functionality.

```
Employee

↓

Administrative Function

↓

Authorization Failure

↓

Administrator Capability
```

This type of failure often has significant business impact.

---

# Horizontal vs Vertical Escalation

| Horizontal | Vertical |
|------------|----------|
| Same privilege level | Higher privilege level |
| Cross-user access | Administrative access |
| Ownership violation | Permission violation |
| User-to-user | User-to-admin |

---

# Insecure Direct Object Reference (IDOR)

IDOR occurs when an application exposes a reference to an internal object without properly verifying authorization.

Conceptually:

```
User Request

↓

Object Identifier

↓

Authorization Check?

↓

Yes → Continue

No → Unauthorized Access
```

The core issue is **missing or insufficient authorization**, not the identifier itself.

---

# Object-Level Authorization

Every object should undergo authorization validation.

```
Request

↓

Resource Exists?

↓

User Authorized?

↓

Allow

OR

Deny
```

Object ownership should never be assumed.

---

# Function-Level Authorization

Administrative functions require separate authorization checks.

```
User

↓

Requests Admin Action

↓

Role Verification

↓

Permission Check

↓

Decision
```

Authentication alone is insufficient.

---

# Record-Level Authorization

Different users may access different records within the same system.

```
Database

↓

Customer Records

↓

Ownership Check

↓

Authorized Record

↓

Response
```

Each record should be evaluated independently.

---

# API Authorization

Modern applications frequently expose APIs.

```
Client

↓

API Gateway

↓

Authentication

↓

Authorization

↓

Business Logic

↓

Database
```

Every API endpoint should consistently enforce authorization rules.

---

# Enterprise Authorization Architecture

```
                 User

                  │

                  ▼

          Authentication

                  │

                  ▼

         Authorization Engine

        ┌─────────┼─────────┐

        ▼         ▼         ▼

     Roles    Policies   Attributes

        │         │         │

        └─────────┼─────────┘

                  ▼

          Business Rules

                  ▼

          Protected Resource
```

Centralized authorization improves consistency and maintainability.

---

# Least Privilege in Practice

```
Employee

↓

Only Required Permissions

↓

Specific Resources

↓

Specific Actions

↓

Reduced Attack Surface
```

Permissions should be granted based on business needs—not convenience.

---

# Authorization Lifecycle

```
User Created

↓

Role Assigned

↓

Permissions Granted

↓

Access Reviewed

↓

Role Updated

↓

Access Removed
```

Regular reviews help eliminate unnecessary privileges.

---

# Common Authorization Weaknesses

| Weakness | Security Impact |
|----------|-----------------|
| Missing object ownership checks | Cross-user data exposure |
| Missing function authorization | Administrative access |
| Excessive permissions | Larger attack surface |
| Inconsistent authorization logic | Unpredictable security |
| Hardcoded administrative privileges | Difficult governance |

---

# Enterprise Example

A banking application:

```
Customer

↓

View Own Accounts

↓

Allowed

────────────

Customer

↓

Approve Loans

↓

Denied

────────────

Loan Officer

↓

Approve Loans

↓

Allowed
```

Each business function is protected by explicit authorization rules.

---

# Hands-on Lab (Conceptual)

1. Create three user roles for a sample application.
2. Define permissions for each role.
3. Build an authorization matrix.
4. Identify where object-level, function-level, and record-level authorization checks are required.
5. Review how least privilege reduces business risk.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is RBAC?
2. How does ABAC differ from RBAC?
3. What is Mandatory Access Control (MAC)?
4. What is Discretionary Access Control (DAC)?
5. What is horizontal privilege escalation?
6. What is vertical privilege escalation?
7. What is IDOR?
8. Why should every API endpoint enforce authorization?
9. What is object-level authorization?
10. Why is least privilege important?

---

# Best Practices

- Perform authorization checks for every protected request.
- Validate object ownership before granting access.
- Protect administrative functions separately.
- Centralize authorization logic where practical.
- Apply least privilege across users, services, and APIs.
- Periodically review permissions and remove unnecessary access.
- Log authorization decisions for sensitive operations.

---

# Common Mistakes

- Checking authentication but not authorization.
- Assuming object identifiers are sufficient for access.
- Applying inconsistent authorization across APIs and web pages.
- Granting broad permissions "for convenience."
- Embedding authorization logic inconsistently throughout the application.

---

# Key Takeaways

- Multiple authorization models exist, each suited to different business needs.
- RBAC is common, while ABAC provides greater flexibility.
- Broken authorization can lead to horizontal and vertical privilege escalation.
- IDOR is fundamentally an authorization failure involving object access.
- Consistent, server-side authorization checks are essential for protecting enterprise applications.

# 19-Broken-Access-Control.md

# Part 3 — Authorization Testing, Common Access Control Weaknesses, Enterprise Architecture, and Defense Strategies

> **"Authorization is not verified by a single successful login. Every request, every API call, every business function, and every object access must be independently authorized."**

---

# Learning Objectives

After completing this part, you will understand:

- Authorization Testing Methodology
- Object-Level Authorization
- Function-Level Authorization
- Business Logic Authorization
- API Authorization
- Multi-Tenant Security
- Enterprise Authorization Architecture
- Defense Strategies
- Security Monitoring
- Secure Development Practices

---

# Authorization Testing Workflow

Authorization testing follows a systematic process.

```
Identify User

↓

Authenticate

↓

Identify Permissions

↓

Attempt Resource Access

↓

Evaluate Authorization

↓

Allow

OR

Deny
```

The objective is to verify that every authorization decision matches the application's intended security policy.

---

# Types of Authorization Testing

```
Authorization Testing

│

├── Page Access

├── API Access

├── Object Access

├── File Access

├── Administrative Functions

├── Business Logic

└── Multi-Tenant Isolation
```

Each area should be evaluated independently.

---

# Object-Level Authorization

Every object belongs to an authorized owner or group.

```
User Request

↓

Requested Object

↓

Ownership Check

↓

Authorized?

↓

Allow

OR

Deny
```

Authorization should be enforced for every object request.

---

# Function-Level Authorization

Sensitive functionality requires explicit permission checks.

```
User

↓

Administrative Function

↓

Role Verification

↓

Permission Check

↓

Decision
```

Examples:

- User management
- Payroll approval
- Configuration changes
- Financial approvals

---

# URL Authorization

Access control should never depend solely on whether a user can discover a URL.

```
Browser Request

↓

Application

↓

Authorization

↓

Allow

OR

Reject
```

Knowing or guessing a URL must not bypass authorization.

---

# API Authorization

Modern applications expose numerous APIs.

```
Client

↓

REST API

↓

Authentication

↓

Authorization

↓

Business Logic

↓

Database
```

Every API endpoint requires independent authorization.

---

# Record-Level Authorization

Applications frequently store data for many users.

```
Database

↓

Record

↓

Ownership Validation

↓

Access Decision
```

Each record should be evaluated separately.

---

# Multi-Tenant Applications

Cloud applications often serve multiple organizations.

```
Tenant A

↓

Application

↓

Tenant Isolation

↓

Tenant B
```

Tenant data must remain isolated even though the same application serves multiple customers.

---

# Multi-Tenant Authorization

```
User

↓

Tenant Validation

↓

Role Validation

↓

Resource Ownership

↓

Business Rules

↓

Access Decision
```

Multiple checks work together before access is granted.

---

# Business Logic Authorization

Authorization extends beyond pages and APIs.

```
Business Process

↓

Business Rule

↓

Authorization

↓

Execute

OR

Reject
```

Examples include:

- Refund approval
- Loan approval
- Salary modification
- Account closure

---

# Administrative Interfaces

Administrative functionality should receive additional protection.

```
Administrator

↓

Authentication

↓

Authorization

↓

Audit Logging

↓

Administrative Action
```

Administrative operations should be monitored and logged.

---

# File Authorization

Applications often manage sensitive files.

```
User

↓

File Request

↓

Ownership

↓

Permission

↓

Download

OR

Denied
```

Every file request should undergo authorization validation.

---

# Enterprise Authorization Flow

```
                    User

                     │

                     ▼

             Authentication

                     │

                     ▼

           Authorization Engine

                     │

          ┌──────────┼──────────┐

          ▼          ▼          ▼

       Roles     Attributes   Policies

          │          │          │

          └──────────┼──────────┘

                     ▼

            Business Validation

                     ▼

             Protected Resource
```

Centralizing authorization improves consistency across the application.

---

# Security Logging

Authorization events should be logged.

```
Authorization Request

↓

Decision

↓

Audit Log

↓

Security Monitoring

↓

SOC
```

Logging supports incident investigation and compliance requirements.

---

# Security Monitoring

Security teams should monitor:

```
✓ Authorization Failures

✓ Privileged Operations

✓ Administrative Changes

✓ Failed Permission Checks

✓ Unusual Resource Access

✓ Cross-Tenant Access Attempts

✓ High-Risk Business Actions
```

Repeated authorization failures may indicate probing or misconfiguration.

---

# Secure Development Lifecycle

Authorization should be considered during every SDLC phase.

```
Requirements

↓

Threat Modeling

↓

Architecture

↓

Development

↓

Testing

↓

Deployment

↓

Monitoring
```

Authorization should never be treated as an afterthought.

---

# Enterprise Authorization Checklist

```
✓ Server-Side Authorization

✓ Least Privilege

✓ Role Validation

✓ Object Ownership Checks

✓ Function-Level Authorization

✓ API Authorization

✓ Tenant Isolation

✓ Audit Logging

✓ Security Monitoring
```

---

# Enterprise Example

An online banking platform:

```
Customer

↓

Transfer Funds

↓

Own Accounts?

↓

Authorized

↓

Transfer

──────────────

Customer

↓

Approve Employee Payroll

↓

Denied
```

Each business operation is validated according to predefined authorization rules.

---

# Defense in Depth

Authorization works alongside other security controls.

```
Authentication

↓

Authorization

↓

Input Validation

↓

Secure Sessions

↓

Logging

↓

Monitoring

↓

Incident Response
```

Multiple controls reduce overall risk.

---

# Common Authorization Weaknesses

| Weakness | Security Impact |
|----------|-----------------|
| Missing ownership validation | Cross-user data exposure |
| Inconsistent authorization logic | Unpredictable behavior |
| Missing API authorization | Unauthorized API access |
| Weak tenant isolation | Cross-tenant data leakage |
| Excessive privileges | Increased attack surface |
| Missing audit logs | Difficult investigations |

---

# Secure Design Principles

```
Default Deny

↓

Least Privilege

↓

Centralized Authorization

↓

Consistent Enforcement

↓

Continuous Review
```

A secure design minimizes opportunities for authorization bypass.

---

# Hands-on Lab (Conceptual)

1. Design an authorization matrix for a multi-role application.
2. Identify object-level, function-level, and record-level resources.
3. Determine where authorization checks should occur.
4. Review tenant isolation requirements for a cloud application.
5. Document which authorization events should be logged.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is object-level authorization?
2. Why is function-level authorization important?
3. Why must every API endpoint enforce authorization?
4. What is tenant isolation?
5. Why should authorization be centralized where practical?
6. What authorization events should be logged?
7. Why is "default deny" considered a security best practice?
8. How does least privilege reduce business risk?
9. Why should authorization be considered during system design?
10. What challenges arise in multi-tenant applications?

---

# Best Practices

- Apply server-side authorization to every protected request.
- Validate ownership for all user-controlled resources.
- Protect sensitive business functions with explicit authorization checks.
- Centralize authorization logic where feasible.
- Apply the principle of default deny.
- Log sensitive authorization events.
- Review authorization policies after application changes.
- Test authorization across web pages, APIs, and business workflows.

---

# Common Mistakes

- Assuming authenticated users are automatically authorized.
- Protecting web pages but forgetting APIs.
- Trusting client-side role information.
- Missing ownership checks for records or files.
- Granting excessive permissions to simplify administration.
- Ignoring tenant isolation in multi-tenant applications.

---

# Key Takeaways

- Every protected request requires an independent authorization decision.
- Authorization applies to pages, APIs, objects, files, and business processes.
- Multi-tenant systems require strong tenant isolation.
- Logging and monitoring strengthen authorization by improving visibility.
- Secure authorization combines least privilege, default deny, centralized policy enforcement, and continuous review.

# 19-Broken-Access-Control.md

# Part 4 — Enterprise Governance, Secure Authorization Architecture, Incident Response, Best Practices, and Chapter Summary

> **"Broken Access Control is one of the most dangerous application security risks because it directly violates confidentiality, integrity, and trust. Strong authorization must be designed into the application—not added later."**

---

# Learning Objectives

After completing this final part, you will understand:

- Enterprise Authorization Governance
- Secure Authorization Architecture
- Incident Response
- Continuous Authorization Review
- Operational Best Practices
- Security Metrics
- Common Challenges
- Interview Revision
- Chapter Summary

---

# Enterprise Authorization Governance

Access control should be managed through organizational policies rather than ad hoc application logic.

```
Security Policy

↓

Authorization Standards

↓

Development Guidelines

↓

Implementation

↓

Testing

↓

Deployment

↓

Monitoring

↓

Periodic Review
```

Governance ensures consistent authorization across all enterprise applications.

---

# Authorization Lifecycle

Access permissions change over time.

```
User Created

↓

Identity Verified

↓

Role Assigned

↓

Permissions Granted

↓

Periodic Review

↓

Role Updated

↓

Access Revoked
```

Proper lifecycle management helps prevent unnecessary or outdated privileges.

---

# Joiner–Mover–Leaver (JML) Process

Organizations should manage user access throughout employment.

```
New Employee

↓

Grant Required Access

↓

Role Change

↓

Update Permissions

↓

Employee Departure

↓

Revoke All Access
```

Timely permission updates reduce security risks.

---

# Separation of Duties (SoD)

Critical operations should require different authorized individuals.

```
Employee A

↓

Create Payment

──────────────

Employee B

↓

Approve Payment
```

Separating responsibilities reduces the risk of fraud and accidental misuse.

---

# Principle of Default Deny

Applications should deny access unless permission is explicitly granted.

```
Access Request

↓

Permission Exists?

↓

Yes

↓

Allow

──────────────

No

↓

Deny
```

This approach minimizes accidental exposure of sensitive resources.

---

# Centralized Authorization

Large organizations often centralize authorization decisions.

```
Users

↓

Authentication

↓

Authorization Service

↓

Business Policies

↓

Protected Applications
```

Benefits include:

- Consistent policy enforcement
- Easier maintenance
- Simplified auditing
- Reduced duplication
- Improved governance

---

# Enterprise Authorization Architecture

```
                 Internet

                     │

                     ▼

             Identity Provider

                     │

                     ▼

            Authentication Layer

                     │

                     ▼

         Central Authorization Engine

          ┌──────────┼──────────┐

          ▼          ▼          ▼

      RBAC       ABAC       Policies

          │          │          │

          └──────────┼──────────┘

                     ▼

            Business Applications

                     │

                     ▼

                  Databases
```

A centralized architecture promotes consistency across applications.

---

# Authorization in APIs

API authorization should be enforced independently for every request.

```
API Request

↓

Authentication

↓

Authorization

↓

Business Validation

↓

Database

↓

Response
```

Authorization decisions should never rely on assumptions from previous requests.

---

# Authorization Caching

Some systems temporarily cache authorization information for performance.

```
User Request

↓

Authorization Cache

↓

Valid?

↓

Yes → Continue

──────────────

No

↓

Re-evaluate Permissions
```

Cached permissions should expire appropriately and reflect permission changes promptly.

---

# Access Reviews

Organizations should regularly review user permissions.

```
Users

↓

Current Roles

↓

Permission Review

↓

Unnecessary Access?

↓

Remove

↓

Document
```

Regular reviews help maintain least privilege.

---

# Privileged Access Management (PAM)

Highly privileged accounts require additional protection.

```
Administrator

↓

Strong Authentication

↓

Authorization

↓

Session Monitoring

↓

Audit Logging
```

Administrative actions should receive greater oversight than standard user activities.

---

# Security Logging

Authorization-related events should be logged.

Examples include:

- Administrative actions
- Permission changes
- Failed authorization attempts
- Role assignments
- Privilege changes
- Sensitive data access

---

# Security Monitoring

Security teams should continuously monitor:

```
✓ Failed Authorization Attempts

✓ Privilege Escalation Indicators

✓ Administrative Activities

✓ Permission Changes

✓ Cross-Tenant Access Attempts

✓ High-Risk Business Operations

✓ Unusual Access Patterns
```

Monitoring supports rapid detection and investigation.

---

# Incident Response

If an authorization issue is discovered:

```
Detection

↓

Validate Issue

↓

Containment

↓

Root Cause Analysis

↓

Correct Authorization Logic

↓

Testing

↓

Deployment

↓

Continuous Monitoring
```

After remediation, organizations should review whether similar weaknesses exist elsewhere.

---

# Enterprise Security Metrics

Useful authorization metrics include:

| Metric | Purpose |
|---------|----------|
| Failed Authorization Attempts | Detect abnormal activity |
| Privilege Escalation Incidents | Measure authorization effectiveness |
| Permission Review Completion | Ensure governance compliance |
| Dormant Privileged Accounts | Identify unnecessary risk |
| Time to Revoke Access | Measure offboarding efficiency |
| Unauthorized Access Events | Evaluate control effectiveness |

---

# Authorization Review Checklist

```
✓ Authentication Verified

✓ Server-Side Authorization

✓ Least Privilege Applied

✓ Default Deny Implemented

✓ Object Ownership Validated

✓ API Authorization Verified

✓ Tenant Isolation Confirmed

✓ Logging Enabled

✓ Monitoring Enabled

✓ Documentation Updated
```

---

# Enterprise Example

A multinational retail platform:

```
Customer

↓

Order History

↓

Ownership Check

↓

Authorized

↓

Display Orders

────────────────

Store Manager

↓

Inventory Management

↓

Role Validation

↓

Authorized

↓

Update Inventory

────────────────

Customer

↓

Inventory Management

↓

Denied
```

Each action is evaluated independently according to business rules.

---

# Defense in Depth

Authorization is one layer within a broader security architecture.

```
Secure Design

↓

Authentication

↓

Authorization

↓

Input Validation

↓

Output Encoding

↓

Encryption

↓

Logging

↓

Monitoring

↓

Incident Response
```

Combining multiple controls significantly improves resilience.

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Complex role structures | Define clear role hierarchies and document permissions |
| Excessive privileges | Conduct periodic access reviews |
| Legacy applications | Introduce centralized authorization gradually |
| Multiple development teams | Standardize authorization policies |
| Rapid application growth | Automate testing and governance where appropriate |

---

# Interview Revision

## Authentication vs Authorization

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| Happens first | Happens after authentication |
| Answers "Who are you?" | Answers "What can you do?" |

---

## Horizontal vs Vertical Privilege Escalation

| Horizontal | Vertical |
|------------|----------|
| Access another user's resources | Gain higher-level privileges |
| Same privilege level | Higher privilege level |
| Ownership violation | Permission violation |

---

## Common Authorization Models

```
RBAC

↓

ABAC

↓

DAC

↓

MAC

↓

Rule-Based Access Control
```

Each model serves different organizational requirements.

---

# Hands-on Lab (Conceptual)

1. Create an authorization matrix for a sample enterprise application.
2. Define roles, permissions, and protected resources.
3. Identify where object-level and function-level authorization checks are required.
4. Design a periodic permission review process.
5. Document authorization events that should be logged and monitored.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. Why is Broken Access Control ranked as one of the highest OWASP risks?
2. What is the principle of default deny?
3. Why is server-side authorization mandatory?
4. What is the purpose of separation of duties?
5. Why are periodic access reviews important?
6. What is Privileged Access Management (PAM)?
7. Why should authorization events be logged?
8. How does centralized authorization improve security?
9. What metrics help measure authorization effectiveness?
10. Why should authorization be considered throughout the application lifecycle?

---

# Best Practices

- Enforce authorization on every protected server-side request.
- Follow the principles of least privilege and default deny.
- Centralize authorization logic where practical.
- Perform regular access reviews and promptly revoke unnecessary permissions.
- Protect privileged accounts with stronger controls and monitoring.
- Log and monitor authorization decisions involving sensitive operations.
- Test authorization consistently across web interfaces, APIs, and business workflows.
- Integrate authorization reviews into the Secure SDLC.

---

# Common Mistakes

- Assuming authenticated users are automatically authorized.
- Trusting client-side permission checks.
- Leaving dormant privileged accounts active.
- Granting excessive permissions for convenience.
- Failing to review permissions after organizational changes.
- Ignoring authorization failures in monitoring systems.
- Applying inconsistent authorization rules across different applications.

---

# Chapter Summary

In this chapter, you learned:

- The fundamentals of Broken Access Control and why it is the **#1 OWASP Top 10 risk**.
- The distinction between authentication and authorization.
- Common authorization models including RBAC, ABAC, DAC, MAC, and rule-based access control.
- The concepts of horizontal and vertical privilege escalation and IDOR.
- How object-level, function-level, API-level, and business logic authorization protect enterprise applications.
- The importance of least privilege, default deny, separation of duties, centralized authorization, logging, monitoring, and periodic access reviews.
- How enterprise governance integrates authorization into the Secure Software Development Lifecycle (SSDLC).

Broken Access Control remains one of the most impactful web application security risks because authorization failures can expose sensitive information, administrative capabilities, and critical business functions. A robust authorization strategy requires secure architecture, consistent server-side enforcement, continuous monitoring, and ongoing governance to ensure that every request is evaluated according to clearly defined business rules.

