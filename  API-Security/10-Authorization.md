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

**Next:** Object-Level Authorization, Function-Level Authorization, BOLA, BFLA, Zero Trust Authorization, Authorization Attacks, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.