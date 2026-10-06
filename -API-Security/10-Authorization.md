# 10 - Authorization

# Introduction

Authorization is the process of determining **what an authenticated identity is allowed to access or perform** within a system.

While authentication answers:

> **Who are you?**

Authorization answers:

> **What are you allowed to do?**

Authorization is one of the most critical security controls in modern applications because even a successfully authenticated user should only be able to perform actions that align with their assigned permissions.

Every modern system—including:

- REST APIs
- GraphQL APIs
- gRPC Services
- Cloud Platforms
- Kubernetes
- Enterprise Applications
- Mobile Applications
- Microservices

depends on robust authorization mechanisms.

Poor authorization is consistently ranked among the most critical API security risks.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand authorization fundamentals.
- Differentiate authentication from authorization.
- Learn authorization models.
- Understand Role-Based Access Control (RBAC).
- Explore Attribute-Based Access Control (ABAC).
- Learn Access Control Lists (ACLs).
- Understand Policy-Based Access Control (PBAC).
- Explore Object-Level Authorization.
- Identify authorization vulnerabilities.
- Perform authorization security assessments.

---

# Authentication vs Authorization

```
User

 │

 ▼

Authentication

 │

Identity Verified

 ▼

Authorization

 │

Permission Evaluation

 ▼

Protected Resource
```

Authentication always precedes authorization.

---

# What is Authorization?

Authorization evaluates whether an authenticated identity is permitted to perform a requested operation.

Example

```
User

 │

GET /orders/100

 │

Permission Check

 │

Allowed

 ▼

Order Returned
```

If authorization fails,

```
403 Forbidden
```

should typically be returned.

---

# Authorization Workflow

```
Authenticated User

        │

        ▼

Resource Request

        │

        ▼

Policy Evaluation

        │

 ┌──────┴──────┐

 ▼             ▼

Allow        Deny

 │             │

 ▼             ▼

Resource    403 Forbidden
```

Every request to a protected resource should undergo authorization checks.

---

# Authorization Components

```
Authorization

      │

 ┌────┼─────┬─────────┐

 ▼    ▼     ▼         ▼

Subject Resource Action Policy
```

Definitions

| Component | Description |
|------------|-------------|
| Subject | User, application, or service |
| Resource | Object being accessed |
| Action | Requested operation |
| Policy | Rules determining access |

---

# Subjects

Subjects represent identities requesting access.

Examples

- Employee
- Customer
- Administrator
- API Client
- Microservice
- Service Account

Each subject possesses specific permissions.

---

# Resources

Resources are protected objects.

Examples

- User Profile
- Orders
- Customer Records
- API Endpoints
- Files
- Databases
- Cloud Storage Objects

Authorization determines whether access to each resource is permitted.

---

# Actions

Common actions include:

```
Read

Write

Update

Delete

Execute

Upload

Download

Approve
```

Actions often map directly to HTTP methods.

| Action | HTTP Method |
|----------|-------------|
| Read | GET |
| Create | POST |
| Update | PUT / PATCH |
| Delete | DELETE |

---

# Authorization Policies

Policies define access rules.

Example

```
IF

Role = Manager

AND

Department = Finance

THEN

Allow Payroll Access
```

Policies should be centrally managed whenever possible.

---

# Authorization Models

The most common models are:

```
Authorization

       │

 ┌─────┼─────┬───────┬────────┐

 ▼     ▼     ▼       ▼

RBAC  ABAC  ACL     PBAC
```

Each model is suitable for different business requirements.

---

# Role-Based Access Control (RBAC)

RBAC assigns permissions based on predefined roles.

Example

```
Employee

↓

Role

↓

Permissions
```

Roles simplify permission management.

---

# RBAC Example

| Role | Permissions |
|------|-------------|
| Customer | View own profile |
| Support | View customer records |
| Manager | Approve requests |
| Administrator | Full access |

Users inherit permissions from their assigned roles.

---

# RBAC Architecture

```
User

 │

Assigned Role

 │

Permission Set

 │

Authorization

 ▼

Application
```

RBAC is the most widely implemented enterprise authorization model.

---

# RBAC Advantages

Benefits

- Easy to manage
- Simple auditing
- Predictable permissions
- Enterprise scalability
- Centralized administration

---

# RBAC Limitations

Challenges

- Role explosion
- Difficult handling of exceptions
- Complex hierarchical organizations
- Dynamic business rules

Large enterprises often require additional authorization models alongside RBAC.

---

# Attribute-Based Access Control (ABAC)

ABAC evaluates attributes instead of relying solely on roles.

Example attributes

Subject

- Department
- Clearance
- Employment Status

Resource

- Owner
- Classification
- Region

Environment

- Time
- Location
- Device

---

# ABAC Decision Flow

```
Request

 │

Collect Attributes

 │

Evaluate Policy

 │

Decision

 ▼

Allow / Deny
```

ABAC supports highly granular authorization decisions.

---

# ABAC Example

```
IF

Department = Finance

AND

Country = India

AND

Time < 18:00

THEN

Allow
```

Multiple attributes contribute to the authorization decision.

---

# ABAC Advantages

Benefits

- Fine-grained control
- Dynamic decisions
- Context awareness
- Cloud-native compatibility
- Zero Trust readiness

---

# ABAC Challenges

Potential drawbacks

- Increased policy complexity
- Performance considerations
- Difficult troubleshooting
- Policy maintenance overhead

Effective governance is essential for successful ABAC deployments.

---

# Access Control Lists (ACLs)

ACLs associate permissions directly with resources.

Example

```
Document

 │

ACL

 ├── Alice → Read

 ├── Bob → Write

 └── Carol → Full Control
```

ACLs are commonly used in file systems and object storage platforms.

---

# ACL Workflow

```
User

 │

Resource

 │

Read ACL

 │

Permission Found?

 ┌──────┴──────┐

 ▼             ▼

Yes           No

 │             │

Allow        Deny
```

ACLs are resource-centric rather than identity-centric.

---

# Policy-Based Access Control (PBAC)

PBAC evaluates centralized authorization policies.

```
Application

 │

Authorization Request

 │

Policy Engine

 │

Decision

 ▼

Application
```

Policy logic is separated from application code.

---

# PBAC Components

| Component | Purpose |
|------------|----------|
| Policy Engine | Evaluates policies |
| Policy Store | Stores authorization rules |
| Policy Administration Point | Manages policies |
| Policy Decision Point | Makes decisions |
| Policy Enforcement Point | Enforces decisions |

This architecture enables centralized authorization management.

---

# Enterprise Example

A financial institution implements authorization as follows:

```
Authentication

        │

Identity Provider

        │

RBAC

        │

ABAC

        │

Business Rules

        │

Decision

        ▼

Core Banking API
```

Static roles determine baseline permissions, while attributes provide contextual restrictions.

---

# Least Privilege

Users should receive only the permissions required to perform their responsibilities.

Example

```
Developer

↓

Read Logs

↓

Deploy Own Service

↓

No Database Administration
```

Least privilege reduces the potential impact of compromised accounts.

---

# Need-to-Know Principle

Access should be granted only when required for legitimate business purposes.

Example

```
HR Employee

↓

Employee Records

↓

Allowed

```

```
HR Employee

↓

Financial Ledger

↓

Denied
```

Need-to-know complements least privilege.

---

# Separation of Duties (SoD)

Critical operations should require multiple independent roles.

Example

```
Employee

↓

Creates Payment

```

```
Manager

↓

Approves Payment
```

No single individual should control an entire high-risk process.

---

# Privileged Access

Privileged accounts include:

- System Administrators
- Database Administrators
- Cloud Administrators
- Security Administrators
- Domain Administrators

Additional controls

- MFA
- Session recording
- Just-In-Time (JIT) access
- Approval workflows
- Enhanced logging

---

# Just-In-Time (JIT) Access

Instead of permanent administrative permissions,

users receive temporary elevated access.

```
Request Access

 │

Approval

 │

Temporary Permission

 │

Expiration

 ▼

Privilege Removed
```

JIT significantly reduces standing privileges.

---

# Just-Enough Access (JEA)

Users receive only the minimum permissions required for a specific task.

```
Patch Server

↓

Temporary Patch Permission

↓

Permission Removed
```

JEA minimizes unnecessary exposure.

---

# Enterprise Authorization Architecture

```
                  User

                    │

                    ▼

             Authentication

                    │

                    ▼

          Identity Provider

                    │

                    ▼

        Authorization Engine

        │       │       │

        ▼       ▼       ▼

      RBAC    ABAC    Policies

        │       │       │

        └───────┼───────┘

                ▼

       Decision (Allow/Deny)

                │

                ▼

          Protected Resource
```

Centralized authorization simplifies governance and auditing.

---

# Best Practices

Authorization

- Deny by default.
- Validate authorization on every request.
- Apply least privilege.
- Centralize policy management.
- Review permissions regularly.

Operations

- Log authorization decisions.
- Protect privileged accounts.
- Use temporary elevation where possible.
- Remove stale permissions promptly.

Development

- Avoid client-side authorization decisions.
- Validate permissions on the server.
- Separate authentication from authorization logic.

---

# Common Mistakes

Avoid:

- Implicit allow rules
- Missing object ownership checks
- Excessive permissions
- Client-side authorization enforcement
- Shared administrator accounts
- Permanent privileged access
- Hardcoded authorization rules
- Missing authorization logging
- Stale roles and permissions

---

# Key Takeaways

- Authorization determines what authenticated identities may access.
- Authentication and authorization are distinct but complementary.
- RBAC, ABAC, ACL, and PBAC each solve different authorization challenges.
- Least privilege, need-to-know, and separation of duties strengthen enterprise security.
- Every protected request should undergo consistent server-side authorization.

---

# Object-Level Authorization

Object-Level Authorization determines whether an authenticated user is permitted to access a **specific resource instance**.

Examples

- Order #100
- Customer Profile
- Invoice #500
- Employee Record
- Bank Account

Authorization must verify not only that the user can access the resource type, but also that they own or are otherwise permitted to access the individual object.

---

# Object-Level Authorization Flow

```
            User

              │

              ▼

     GET /orders/100

              │

              ▼

 Authentication Passed

              │

              ▼

 Ownership Verification

              │

      ┌───────┴────────┐

      ▼                ▼

   Owner           Not Owner

      │                │

      ▼                ▼

 Allow            403 Forbidden
```

Every object request should perform an ownership or permission check.

---

# Broken Object Level Authorization (BOLA)

Broken Object Level Authorization (BOLA) occurs when an application fails to verify whether a user is authorized to access a specific object.

It is consistently one of the most critical API security risks.

Example

```
GET /api/orders/100
```

Attacker changes

```
100

↓

101
```

If Order 101 belongs to another customer and is returned,

authorization has failed.

---

# BOLA Example

Customer A

```
GET /orders/501
```

Own order

↓

Allowed

---

Customer A changes request

```
GET /orders/502
```

Order belongs to Customer B

↓

Application returns data

↓

BOLA Vulnerability

---

# Why BOLA Happens

Common causes

- Missing ownership validation
- Trusting client-supplied identifiers
- Missing server-side authorization
- Predictable identifiers
- Incomplete API testing
- Business logic errors

---

# Secure Object Validation

Always verify

```
Authenticated User

          │

Requested Object

          │

Retrieve Owner

          │

Owner Matches?

     ┌────┴────┐

     ▼         ▼

   Yes        No

     │         │

 Allow      Deny
```

Authorization should never rely solely on client input.

---

# Identifier Types

Common identifiers

```
Sequential IDs

100

101

102
```

```
UUID

5a0f9a22

...

```

Although UUIDs make enumeration more difficult,

they **do not replace authorization checks**.

---

# Predictable Identifier Risks

Sequential identifiers enable enumeration.

```
/users/1

/users/2

/users/3

/users/4
```

Attackers may attempt automated access across many identifiers.

---

# UUID Benefits

```
550e8400-e29b-41d4-a716-446655440000
```

Advantages

- Difficult to guess
- Reduces enumeration
- Better distributed systems support

Limitations

- Not a security control
- Ownership validation remains mandatory

---

# Function-Level Authorization

Function-Level Authorization determines whether a user may perform a particular operation.

Example

```
DELETE

Create User

Reset Password

Export Database

Approve Loan
```

These operations often require elevated privileges.

---

# Broken Function Level Authorization (BFLA)

BFLA occurs when users can invoke privileged functionality without appropriate authorization.

Example

```
DELETE /api/users/50
```

If every authenticated user can invoke this endpoint,

administrative functionality becomes exposed.

---

# BFLA Workflow

```
Authenticated User

          │

DELETE User

          │

Role Check?

     ┌────┴────┐

     ▼         ▼

Present    Missing

     │         │

Allow     Vulnerability
```

Role and permission checks must precede privileged operations.

---

# BOLA vs BFLA

| BOLA | BFLA |
|------|------|
| Object-specific | Function-specific |
| Ownership validation | Permission validation |
| Accessing another user's data | Executing privileged operations |
| Resource level | Business function level |

Both vulnerabilities frequently coexist.

---

# Horizontal Privilege Escalation

Users access resources belonging to other users with similar privilege levels.

Example

```
Customer A

↓

Customer B Order

↓

Unauthorized Access
```

Typical cause

Missing ownership verification.

---

# Vertical Privilege Escalation

A lower-privileged user performs administrative actions.

Example

```
Customer

↓

DELETE User

↓

Administrator Function
```

Typical cause

Missing role verification.

---

# Horizontal vs Vertical Escalation

| Horizontal | Vertical |
|------------|-----------|
| Same privilege level | Higher privilege level |
| Access peer resources | Access administrative functions |
| Usually BOLA | Usually BFLA |

---

# Context-Aware Authorization

Modern authorization decisions often consider context.

Examples

- Device trust
- User location
- Network
- Risk score
- Time
- Authentication strength

Example

```
Admin

↓

Unknown Country

↓

Require MFA

↓

Grant Access
```

---

# Risk-Based Authorization

Authorization may adapt dynamically.

Example

```
Known Device

↓

Low Risk

↓

Allow
```

```
Unknown Device

↓

High Risk

↓

Step-Up Authentication
```

Risk signals improve security without unnecessarily impacting legitimate users.

---

# Zero Trust Authorization

Zero Trust assumes that no request should be trusted automatically.

Principles

- Verify explicitly
- Least privilege
- Continuous evaluation
- Assume breach

---

# Zero Trust Authorization Flow

```
Request

   │

Identity

   │

Device

   │

Location

   │

Risk

   │

Authorization

   ▼

Decision
```

Authorization is evaluated continuously rather than only during login.

---

# Policy Decision Point (PDP)

The Policy Decision Point evaluates authorization policies.

```
Application

      │

Authorization Request

      │

Policy Decision Point

      │

Allow / Deny

      ▼

Application
```

The PDP should remain independent from application logic where practical.

---

# Policy Enforcement Point (PEP)

The Policy Enforcement Point applies the authorization decision.

```
Decision

↓

Allow

↓

Continue Request
```

or

```
Decision

↓

Deny

↓

403 Forbidden
```

The PEP ensures consistent enforcement across applications.

---

# Policy Information Point (PIP)

The Policy Information Point supplies attributes used during authorization.

Examples

- User role
- Department
- Device posture
- Geolocation
- Resource classification

These attributes enable dynamic authorization decisions.

---

# Authorization in Microservices

```
          Client

             │

             ▼

        API Gateway

             │

             ▼

 Authorization Service

             │

      ┌──────┼──────┐

      ▼      ▼      ▼

 Service A Service B Service C
```

Centralized authorization avoids inconsistent policy enforcement.

---

# Authorization in Cloud Environments

Cloud platforms commonly use policy-based authorization.

Examples

- Cloud IAM
- Resource Policies
- Service Policies
- Conditional Access

Access decisions may consider

- Identity
- Region
- Resource Tags
- Device
- Risk

---

# API Authorization Best Practices

Validate

- Identity
- Object ownership
- Resource state
- Business rules
- HTTP method
- Permissions

Never rely on

- Hidden URLs
- Client-side checks
- Obscure identifiers
- Browser logic

---

# Authorization Logging

Log

- User ID
- Resource ID
- Action
- Decision
- Policy evaluated
- Source IP
- Device ID
- Timestamp
- Correlation ID

Avoid logging sensitive business data unless operationally required and appropriately protected.

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Sequential Object Access | Consecutive object identifiers requested |
| Repeated 403 Responses | Authorization failures |
| Privileged Endpoint Access | Non-admin users accessing admin APIs |
| Enumeration | Large volume of object requests |
| Role Changes | Unexpected privilege assignments |
| Policy Evaluation Failures | Authorization engine errors |
| Cross-Tenant Access | Access attempts across tenant boundaries |
| Permission Abuse | Sudden increase in privileged actions |

Behavioral baselines improve detection quality.

---

# SIEM Integration

Recommended telemetry

```
Authentication Logs

        │

Authorization Decisions

        │

API Gateway Logs

        │

Application Logs

        │

Cloud IAM Logs

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

Example correlation rules

- Multiple object access denials followed by one success
- Enumeration immediately followed by data downloads
- Privileged action from a newly assigned role
- Cross-tenant access attempts
- Administrative API usage outside business hours

---

# Enterprise Authorization Architecture

```
                  User

                    │

                    ▼

            Authentication

                    │

                    ▼

           Identity Provider

                    │

                    ▼

          Authorization Service

          │       │        │

          ▼       ▼        ▼

       RBAC     ABAC     Policies

          │       │        │

          └────────┼────────┘

                   ▼

          Policy Decision Point

                   │

          Policy Enforcement Point

                   │

                   ▼

            Protected Resource

                   │

                   ▼

           Logging & Monitoring

                   │

                   ▼

               SIEM / SOC
```

---

# Hands-on Lab 1 – Object Authorization Review

**Objective**

Verify that users cannot access objects they do not own.

**Steps**

1. Create two authorized test accounts.
2. Create separate resources for each account.
3. Attempt to access another account's resources.
4. Confirm that access is denied.

**Learning Outcomes**

- Ownership validation
- BOLA assessment
- API authorization testing

---

# Hands-on Lab 2 – Function Authorization Review

**Objective**

Verify that privileged functions require appropriate permissions.

**Steps**

1. Authenticate using a low-privilege account.
2. Attempt privileged administrative operations.
3. Confirm that unauthorized requests receive `403 Forbidden`.
4. Review authorization logs.

**Learning Outcomes**

- BFLA assessment
- Role verification
- Privileged access validation

---

# Hands-on Lab 3 – Policy Review

**Objective**

Review enterprise authorization policies.

**Steps**

1. Identify RBAC and ABAC policies.
2. Verify least privilege.
3. Review separation of duties.
4. Document unnecessary permissions.

**Learning Outcomes**

- Policy analysis
- Least privilege assessment
- Authorization governance

---

# Common Security Mistakes

Avoid

- Missing ownership validation
- Client-side authorization
- Excessive privileges
- Hardcoded permissions
- Predictable identifiers without authorization
- Shared privileged accounts
- Missing authorization logs
- Ignoring cross-tenant access
- Permanent administrative privileges
- Weak policy governance

---

# Troubleshooting

## Unexpected 403 Forbidden

Possible causes

- Incorrect role assignment
- Missing object ownership
- Policy misconfiguration
- Expired permissions

---

## User Can Access Another User's Data

Possible causes

- Missing ownership validation
- Broken Object Level Authorization
- Identifier trust
- Business logic flaw

---

## Administrative Function Accessible

Possible causes

- Missing role checks
- Broken Function Level Authorization
- Incorrect policy evaluation
- API gateway misconfiguration

---

## Authorization Service Failure

Possible causes

- Policy engine unavailable
- Identity provider connectivity
- Attribute retrieval failure
- Configuration error

---

## Cross-Tenant Access

Possible causes

- Tenant isolation failure
- Incorrect resource filtering
- Policy bug
- Shared identifiers

---

# Interview Questions

## Fundamental

1. What is authorization?
2. How does authorization differ from authentication?
3. What is RBAC?
4. What is ABAC?
5. What is an ACL?
6. What is the principle of least privilege?
7. What is separation of duties?
8. What is Broken Object Level Authorization (BOLA)?
9. What is Broken Function Level Authorization (BFLA)?
10. What is Zero Trust authorization?

---

## Intermediate

11. Compare RBAC and ABAC.
12. Why are UUIDs not sufficient to prevent BOLA?
13. How would you design authorization for a multi-tenant SaaS platform?
14. Explain horizontal and vertical privilege escalation.
15. What are the responsibilities of a Policy Decision Point?
16. How would you centralize authorization in a microservices architecture?
17. Which authorization events should be forwarded to a SIEM?
18. How would you detect object enumeration attacks?
19. Why is server-side authorization mandatory?
20. How would you audit privileged access?

---

## Scenario-Based

**Scenario 1**

A customer can retrieve another customer's invoices by changing the invoice ID in the request URL.

- Which vulnerability does this indicate?
- How would you remediate it?

---

**Scenario 2**

A standard user successfully invokes an administrative endpoint that deletes user accounts.

- Which authorization weakness is present?
- Which controls should be implemented immediately?

---

**Scenario 3**

Your SOC observes repeated requests for sequential object identifiers followed by successful downloads.

- What attack is likely occurring?
- Which logs and controls would you review during the investigation?

---

# Chapter Summary

In this chapter, we explored enterprise authorization and access control.

We covered:

- Authorization fundamentals
- RBAC
- ABAC
- ACL
- PBAC
- Object-Level Authorization
- Function-Level Authorization
- BOLA
- BFLA
- Least privilege
- Zero Trust authorization
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Effective authorization ensures authenticated identities can access only the resources and functions required for their legitimate business responsibilities.

---

# Chapter Review

You should now be able to answer:

- How do authentication and authorization differ?
- When should RBAC, ABAC, ACL, or PBAC be used?
- What distinguishes BOLA from BFLA?
- How can horizontal and vertical privilege escalation be prevented?
- Why are UUIDs insufficient without authorization checks?
- Which authorization events should be monitored by a SIEM?
- How would you implement centralized authorization for a microservices environment?

If you can confidently answer these questions, you are ready to continue with **Chapter 11 – JWT Security**, where you'll explore JSON Web Tokens, token structure, signing algorithms, validation, common attacks, secure implementation, and enterprise best practices.

---

# References

## Standards

- RFC 7644 – SCIM
- NIST SP 800-162 – Guide to Attribute Based Access Control
- XACML 3.0 Specification

## Security Standards

- OWASP API Security Top 10
- OWASP ASVS
- OWASP Authorization Cheat Sheet
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53

## Further Reading

- Zero Trust Architecture (NIST SP 800-207)
- Open Policy Agent (OPA) Documentation
- Enterprise IAM Best Practices

---

# What's Next?

➡️ **Chapter 11 – JWT Security**

In the next chapter, we will explore:

- JSON Web Token (JWT) fundamentals
- JWT structure
- Claims
- Signing algorithms
- Token validation
- Access and refresh tokens
- JWT attacks
- Secure implementation
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions