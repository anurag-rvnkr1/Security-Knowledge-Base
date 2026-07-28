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

```text id="rrks28"
**Next:** Part 2
```