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

```text id="rrks28"
**Next:** Part 3
```