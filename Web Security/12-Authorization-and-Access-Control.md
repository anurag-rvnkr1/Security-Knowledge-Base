# 12-Authorization-and-Access-Control.md

# Part 1 — Authorization Fundamentals, Access Control Models, Permissions, Roles, and Enterprise Authorization Architecture

> **"Authentication answers 'Who are you?'. Authorization answers 'What are you allowed to do?'. Even perfectly authenticated users must never receive permissions they do not require."**

---

# Learning Objectives

After completing this part, you will understand:

- What Authorization Is
- Authentication vs Authorization
- Access Control
- Permissions
- Roles
- Resources
- Subjects and Objects
- Access Control Models
- Principle of Least Privilege
- Enterprise Authorization Architecture

---

# What is Authorization?

Authorization is the process of determining **what an authenticated user is allowed to access or perform**.

```
User

↓

Authenticated

↓

Authorization Check

↓

Access Granted

OR

Access Denied
```

Authorization decisions occur **after** successful authentication.

---

# Why Authorization Matters

Consider an online banking application.

```
Customer A

↓

Authenticated

↓

Attempts to View

↓

Customer B's Account
```

Although Customer A is authenticated, they **must not** be authorized to access Customer B's information.

Authorization protects resources from unauthorized access.

---

# Authentication vs Authorization

```
Authentication

↓

Who Are You?

──────────────

Authorization

↓

What Can You Do?
```

Example:

```
Login

↓

Authentication

↓

Success

↓

Authorization

↓

Dashboard
```

Both processes are required for secure applications.

---

# Authorization Workflow

```
User Request

↓

Authentication

↓

Authorization Policy

↓

Permission Check

↓

Allow

OR

Deny
```

Every protected request should pass through authorization checks.

---

# Core Authorization Components

```
Authorization

│

├── Subject

├── Resource

├── Action

├── Policy

└── Decision
```

Each component contributes to the final access decision.

---

# Subject

A **subject** is the entity requesting access.

Examples:

- User
- Administrator
- Employee
- Service Account
- API Client

---

# Object (Resource)

An object (or resource) is the item being accessed.

Examples:

- File
- Database Record
- Customer Profile
- API Endpoint
- Dashboard
- Cloud Resource

---

# Action

The requested operation.

Examples:

- Read
- Write
- Create
- Delete
- Update
- Download
- Upload
- Execute

---

# Authorization Decision

```
Subject

↓

Resource

↓

Action

↓

Policy Evaluation

↓

Allow

OR

Deny
```

---

# Permissions

Permissions specify what actions are allowed.

Examples:

```
Read Reports

Write Reports

Delete Reports

Manage Users

Export Data
```

Permissions are often grouped into roles.

---

# Roles

A role represents a collection of permissions.

Example:

```
Administrator

↓

Manage Users

Manage Roles

Delete Records

View Reports

Configure System
```

---

# Example Roles

| Role | Example Permissions |
|-------|---------------------|
| Customer | View own profile, update own details |
| Employee | Access internal dashboard |
| Manager | Approve requests, view reports |
| Administrator | Manage users and configuration |
| Auditor | Read audit logs |

---

# Resources

Resources may include:

```
Application

│

├── Pages

├── APIs

├── Files

├── Reports

├── Databases

└── Administrative Functions
```

Every sensitive resource should have authorization checks.

---

# Access Control

Access control enforces authorization decisions.

```
Request

↓

Access Control

↓

Policy

↓

Decision
```

Without access control, users may reach resources they should not access.

---

# Access Control Matrix

Example:

| User | Reports | Users | Settings |
|------|---------|-------|----------|
| Employee | Read | No | No |
| Manager | Read/Write | No | No |
| Administrator | Full | Full | Full |

An access control matrix helps visualize permissions.

---

# Access Control Models

Common authorization models include:

```
Access Control

│

├── DAC

├── MAC

├── RBAC

└── ABAC
```

Each model addresses different organizational requirements.

---

# Discretionary Access Control (DAC)

In DAC, the resource owner determines access.

```
Owner

↓

Grant Permission

↓

Other User
```

Example:

A document owner shares a file with selected colleagues.

---

# Mandatory Access Control (MAC)

MAC uses centrally enforced security policies.

```
Security Policy

↓

Access Decision

↓

User
```

Users cannot change permissions independently.

MAC is common in highly regulated environments.

---

# Role-Based Access Control (RBAC)

RBAC grants permissions through roles.

```
User

↓

Role

↓

Permissions

↓

Resources
```

RBAC simplifies permission management in large organizations.

---

# RBAC Example

```
Employee

↓

Sales Role

↓

View Customers

Create Orders

Update Orders
```

Changing the user's role automatically changes available permissions.

---

# Attribute-Based Access Control (ABAC)

ABAC evaluates attributes before granting access.

```
User Attributes

+

Resource Attributes

+

Environment

↓

Policy Engine

↓

Decision
```

Attributes may include:

- Department
- Clearance
- Location
- Device Type
- Time of Day

---

# Comparing Access Control Models

| Model | Primary Decision Based On |
|---------|---------------------------|
| DAC | Resource owner |
| MAC | Security policy |
| RBAC | User role |
| ABAC | Multiple attributes |

Many enterprise systems combine multiple models.

---

# Principle of Least Privilege

Users should receive only the minimum permissions necessary.

```
User

↓

Required Permissions

↓

No Extra Access
```

Least privilege reduces the impact of compromised accounts.

---

# Need-to-Know Principle

Even within authorized groups:

```
User

↓

Business Need

↓

Specific Data

↓

Access Granted
```

Access should be limited to information necessary for assigned responsibilities.

---

# Separation of Duties

Critical tasks should be divided among multiple individuals.

Example:

```
Employee A

↓

Create Payment

──────────────

Employee B

↓

Approve Payment
```

Separating responsibilities helps reduce fraud and mistakes.

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

        ┌────────┼────────┐

        ▼                 ▼

   Policy Store      Role Database

        │

        ▼

 Permission Evaluation

        │

        ▼

 Protected Resources
```

The authorization engine evaluates permissions before granting access.

---

# Enterprise Example

A hospital information system uses authorization as follows:

```
Doctor

↓

Authenticated

↓

Role Evaluation

↓

Patient Assignment

↓

Medical Record Access
```

A doctor may view records only for patients they are authorized to treat.

---

# Hands-on Lab (Conceptual)

Using a sample web application:

1. Create multiple user accounts.
2. Assign different roles.
3. Log in with each account.
4. Compare accessible pages.
5. Verify unauthorized pages return an access denied response.
6. Observe how role changes affect available functionality.

---

# Interview Questions

1. What is authorization?
2. How does authorization differ from authentication?
3. What is a permission?
4. What is a role?
5. Explain the Principle of Least Privilege.
6. What is Separation of Duties?
7. Compare DAC, MAC, RBAC, and ABAC.
8. Why are authorization checks required on every protected request?
9. What is an access control matrix?
10. Why should access decisions be policy-driven?

---

# Best Practices

- Perform authentication before authorization.
- Enforce authorization on every protected request.
- Apply the Principle of Least Privilege.
- Use role-based or attribute-based authorization where appropriate.
- Separate administrative and standard user permissions.
- Regularly review permissions and roles.
- Deny access by default unless explicitly permitted.

---

# Common Mistakes

- Trusting client-side authorization checks.
- Assuming authenticated users can access all resources.
- Granting excessive permissions.
- Failing to review outdated roles.
- Using shared administrative accounts.
- Omitting authorization checks on APIs or backend services.

---

# Key Takeaways

- Authentication verifies identity; authorization determines permitted actions.
- Authorization decisions are based on subjects, resources, actions, and policies.
- Permissions define allowed operations and are commonly grouped into roles.
- DAC, MAC, RBAC, and ABAC are widely used access control models.
- Enterprise authorization relies on least privilege, separation of duties, and centralized policy enforcement.


# 12-Authorization-and-Access-Control.md

# Part 2 — Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), Policy Enforcement, Permission Management, and Enterprise Authorization Design

> **"Enterprise authorization is not about granting access—it is about granting only the right access, at the right time, to the right identity, under the right conditions."**

---

# Learning Objectives

After completing this part, you will understand:

- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Policy-Based Access Control
- Permission Management
- Resource Hierarchies
- Access Decisions
- Fine-Grained Authorization
- Enterprise Authorization Services
- Authorization Lifecycle
- Secure Authorization Design

---

# Authorization Decision Process

Every authorization decision evaluates several inputs.

```
Authenticated User

↓

Requested Resource

↓

Requested Action

↓

Policy Evaluation

↓

Allow

OR

Deny
```

Authorization should occur for **every protected request**.

---

# Authorization Components

```
Authorization

│

├── Identity

├── Resource

├── Action

├── Policy

├── Context

└── Decision
```

Each component contributes to determining whether access should be granted.

---

# Role-Based Access Control (RBAC)

RBAC assigns permissions to roles instead of individual users.

```
User

↓

Role

↓

Permissions

↓

Resources
```

This simplifies administration in organizations with many users.

---

# RBAC Architecture

```
             Users

               │

               ▼

             Roles

               │

               ▼

          Permissions

               │

               ▼

          Protected Resources
```

Adding or removing users from roles updates their permissions automatically.

---

# RBAC Example

```
Sales Employee

↓

Sales Role

↓

Read Customers

Create Orders

View Products
```

```
Sales Manager

↓

Manager Role

↓

Read Customers

Approve Orders

Generate Reports
```

---

# Role Hierarchy

Organizations often define hierarchical roles.

```
Administrator

│

├── Manager

│

└── Employee

│

└── Guest
```

Higher-level roles may inherit permissions from lower-level roles depending on organizational policy.

---

# Permission Inheritance

Example:

```
Employee

↓

Read Dashboard

────────────

Manager

↓

Employee Permissions

+

Approve Requests

────────────

Administrator

↓

Manager Permissions

+

Manage Users
```

Inheritance reduces duplicated permission definitions.

---

# Designing Roles

Good roles should be:

- Business-oriented
- Easy to understand
- Limited in scope
- Stable over time
- Reviewed regularly

Roles should represent **job functions**, not individual users.

---

# Problems with Too Many Roles

```
Few Roles

↓

Easy Management

──────────────

Hundreds of Roles

↓

Role Explosion

↓

Complex Administration
```

Role explosion makes authorization difficult to maintain.

---

# Attribute-Based Access Control (ABAC)

ABAC evaluates multiple attributes before making an authorization decision.

```
User

+

Resource

+

Environment

↓

Policy Engine

↓

Decision
```

---

# Types of Attributes

### User Attributes

Examples:

- Department
- Job title
- Clearance level
- Employment status

---

### Resource Attributes

Examples:

- Owner
- Classification
- Department
- Sensitivity
- Data type

---

### Environmental Attributes

Examples:

- Time
- Date
- Location
- Device type
- Network
- Authentication strength

---

### Action Attributes

Examples:

- Read
- Create
- Delete
- Download
- Share
- Approve

---

# ABAC Example

```
IF

Department = Finance

AND

Device = Corporate

AND

Business Hours = True

↓

Allow Access
```

If any required condition is not satisfied, access is denied.

---

# RBAC vs ABAC

| RBAC | ABAC |
|-------|------|
| Based on roles | Based on attributes |
| Easier administration | More flexible |
| Good for stable organizations | Better for dynamic environments |
| Simple policies | Complex policy evaluation |

Many enterprise environments combine both approaches.

---

# Hybrid Access Control

```
Authentication

↓

Role Evaluation

↓

Attribute Evaluation

↓

Policy Engine

↓

Final Decision
```

Hybrid authorization balances simplicity and flexibility.

---

# Policy-Based Authorization

Instead of embedding authorization rules directly into application code:

```
Application

↓

Authorization Service

↓

Policy Store

↓

Decision
```

This centralizes authorization logic and improves consistency.

---

# Policy Engine

A policy engine evaluates authorization rules.

```
Access Request

↓

Policy Engine

↓

Evaluate Rules

↓

Allow

OR

Deny
```

Applications ask the policy engine rather than making independent decisions.

---

# Authorization Policies

Policies define business rules.

Examples:

```
Managers

↓

Approve Expense Reports

──────────────

Employees

↓

Cannot Approve Their Own Reports
```

Policies should be easy to review and update.

---

# Resource Hierarchy

Applications often organize resources hierarchically.

```
Organization

│

├── Department

│

├── Projects

│

├── Documents

│

└── Files
```

Permissions may propagate through resource hierarchies according to organizational policy.

---

# Fine-Grained Authorization

Authorization can occur at multiple levels.

```
Application

↓

Page

↓

API

↓

Database Record

↓

Field
```

The deeper the authorization layer, the more precise the access control.

---

# Object-Level Authorization

Example:

```
Customer A

↓

Own Profile

↓

Allowed

──────────────

Customer B Profile

↓

Denied
```

Ownership is frequently part of authorization decisions.

---

# Record-Level Authorization

Example:

```
Doctor

↓

Assigned Patients

↓

Medical Records

↓

Access Allowed
```

The doctor cannot automatically access records for every patient.

---

# Field-Level Authorization

Different users may see different parts of the same record.

```
Employee Record

│

├── Name

├── Department

├── Salary

└── Performance Review
```

HR personnel may view salary information while general managers cannot.

---

# API Authorization

Every protected API endpoint should verify permissions.

```
Client

↓

API Gateway

↓

Authentication

↓

Authorization

↓

API

↓

Response
```

Backend authorization must not rely on client-side checks.

---

# Authorization Cache

To improve performance:

```
Policy Evaluation

↓

Cached Decision

↓

Fast Response
```

Cached decisions should expire appropriately when permissions change.

---

# Enterprise Authorization Architecture

```
                User

                  │

                  ▼

           Authentication

                  │

                  ▼

          API Gateway / WAF

                  │

                  ▼

        Authorization Service

        ┌─────────┼─────────┐

        ▼                   ▼

   Role Store         Policy Store

        │

        ▼

 Attribute Service

        │

        ▼

 Decision Engine

        │

        ▼

 Protected Resources
```

This centralized approach promotes consistent authorization across applications.

---

# Authorization Lifecycle

```
User Created

↓

Assign Role

↓

Grant Permissions

↓

Periodic Review

↓

Role Updated

↓

Access Revoked
```

Permissions should evolve with organizational responsibilities.

---

# Enterprise Example

A multinational retailer manages authorization as follows:

```
Employee

↓

Authentication

↓

Sales Role

↓

Store Attribute

↓

Regional Policy

↓

Inventory System

↓

Access Granted
```

A sales employee can manage inventory only for their assigned store.

---

# Hands-on Lab (Conceptual)

Using a sample application:

1. Create multiple roles.
2. Assign permissions to each role.
3. Test user access with different accounts.
4. Modify role assignments.
5. Verify authorization changes immediately affect resource access.
6. Observe how resource ownership influences authorization.

---

# Interview Questions

1. What is Role-Based Access Control (RBAC)?
2. What is Attribute-Based Access Control (ABAC)?
3. What is role inheritance?
4. What causes role explosion?
5. Why are policies preferable to hard-coded authorization logic?
6. What is fine-grained authorization?
7. What is object-level authorization?
8. What is field-level authorization?
9. Why should APIs perform server-side authorization?
10. Why are authorization policies reviewed regularly?

---

# Best Practices

- Centralize authorization decisions.
- Design roles around business responsibilities.
- Apply least privilege.
- Use fine-grained authorization for sensitive data.
- Evaluate authorization on every protected request.
- Separate authentication from authorization logic.
- Review permissions periodically.
- Keep authorization policies maintainable and well documented.

---

# Common Mistakes

- Hard-coding permissions throughout application code.
- Allowing users to inherit unnecessary permissions.
- Performing authorization only on the client side.
- Ignoring object ownership during authorization.
- Creating excessive numbers of overlapping roles.
- Forgetting to remove permissions when roles change.

---

# Key Takeaways

- RBAC simplifies permission management through business-oriented roles.
- ABAC provides flexible, context-aware authorization using attributes.
- Policy engines centralize authorization decisions and improve consistency.
- Fine-grained authorization can protect APIs, records, objects, and individual fields.
- Enterprise authorization combines roles, attributes, policies, and centralized decision-making to enforce secure access control.

# 12-Authorization-and-Access-Control.md

# Part 3 — Authorization Enforcement, Object-Level Security, API Authorization, Access Reviews, Zero Trust Authorization, and Enterprise Access Control

> **"The most secure authorization policy is meaningless if it is not enforced consistently. Every request, every API call, every object, and every sensitive operation must be validated by the server."**

---

# Learning Objectives

After completing this part, you will understand:

- Authorization Enforcement
- Policy Enforcement Points (PEP)
- Policy Decision Points (PDP)
- Object-Level Authorization
- Record-Level Authorization
- API Authorization
- Function-Level Authorization
- Access Reviews
- Zero Trust Authorization
- Enterprise Authorization Monitoring

---

# Authorization Enforcement

Authorization is effective only when every protected request is validated.

```
Client Request

↓

Authentication

↓

Authorization

↓

Protected Resource

↓

Response
```

Skipping authorization checks on even a single endpoint can expose sensitive resources.

---

# Enforcement Points

Authorization is typically enforced at multiple layers.

```
Application

│

├── Web Pages

├── APIs

├── Business Logic

├── Services

└── Database Operations
```

Each layer should independently validate access where appropriate.

---

# Policy Enforcement Point (PEP)

The Policy Enforcement Point intercepts requests.

```
User Request

↓

Policy Enforcement Point

↓

Policy Decision Point

↓

Allow / Deny

↓

Application
```

The PEP does not decide permissions itself—it enforces the decision.

---

# Policy Decision Point (PDP)

The PDP evaluates authorization policies.

```
Request

↓

Policy Decision Point

↓

Evaluate Policies

↓

Decision

↓

Allow / Deny
```

Centralizing decisions promotes consistent authorization across applications.

---

# Policy Information Point (PIP)

The Policy Information Point supplies attributes used during policy evaluation.

```
Policy Engine

↓

Needs Attributes

↓

User Directory

↓

Resource Metadata

↓

Device Information
```

These attributes help the PDP make informed authorization decisions.

---

# End-to-End Authorization Flow

```
User

↓

Authentication

↓

PEP

↓

PDP

↓

PIP

↓

Decision

↓

Protected Resource
```

This separation improves scalability and maintainability.

---

# Object-Level Authorization

Authorization should verify ownership or entitlement for each object.

Example:

```
User A

↓

Document A

↓

Allowed

──────────────

User A

↓

Document B

↓

Denied
```

Authentication alone does not grant access to every object.

---

# Record-Level Authorization

Applications often store many users' data together.

```
Database

│

├── Record 1

├── Record 2

├── Record 3

└── Record 4
```

Each request should verify that the authenticated user is permitted to access the specific record.

---

# Row-Level Authorization Example

```
Customer

↓

Order History

↓

Own Orders

↓

Allowed

──────────────

Other Customer's Orders

↓

Denied
```

Authorization decisions should be based on business rules rather than assumptions.

---

# Field-Level Authorization

Sometimes only selected fields should be visible.

```
Employee Record

│

├── Name

├── Department

├── Salary

├── Tax Information

└── Performance Rating
```

Different roles may receive different views of the same record.

---

# Function-Level Authorization

Applications expose many functions.

```
Application

│

├── View Dashboard

├── Export Data

├── Delete Records

├── Manage Users

└── Configure Settings
```

Each function should have explicit authorization requirements.

---

# Administrative Functions

Administrative operations require additional protection.

Examples include:

- User management
- Role management
- System configuration
- Audit log access
- Security settings
- Backup management

These functions should be restricted to authorized administrators.

---

# API Authorization

Every API endpoint should verify authorization.

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

Authorization should never depend solely on client-side controls.

---

# API Gateway Authorization

API gateways frequently perform:

```
Request

↓

Authentication

↓

Authorization

↓

Rate Limiting

↓

Routing

↓

Backend Service
```

Gateways provide a centralized enforcement layer.

---

# Microservice Authorization

In distributed systems:

```
Client

↓

Gateway

↓

Service A

↓

Service B

↓

Service C
```

Each service should validate that requests are authorized rather than assuming upstream services performed all checks.

---

# Backend Authorization

```
Browser

↓

Frontend

↓

Backend

↓

Authorization

↓

Database
```

The backend remains the authoritative source for access decisions.

---

# Access Control Lists (ACLs)

An ACL associates permissions directly with a resource.

Example:

| Resource | User/Role | Permission |
|----------|-----------|------------|
| Report A | Manager | Read |
| Report A | Employee | Read |
| Report A | Guest | Denied |
| Report B | Administrator | Full |

ACLs are useful for resources with individualized permissions.

---

# Authorization Policies

Policies commonly evaluate:

- User role
- Resource ownership
- Department
- Location
- Device trust
- Authentication strength
- Time restrictions

Policies should be reviewed regularly.

---

# Time-Based Authorization

Some systems restrict access based on time.

```
Business Hours

↓

Allow

──────────────

Outside Business Hours

↓

Additional Approval

OR

Deny
```

Time is one possible policy attribute.

---

# Location-Based Authorization

Policies may also evaluate location.

```
Corporate Network

↓

Allow

──────────────

Unknown Network

↓

Additional Verification
```

Location should be combined with other security controls rather than used alone.

---

# Device-Based Authorization

Authorization decisions may consider:

- Managed device
- Operating system compliance
- Endpoint protection status
- Device certificate

Device trust is commonly used in enterprise Zero Trust environments.

---

# Risk-Based Authorization

Authorization can adapt to changing risk.

```
Authenticated User

↓

Risk Evaluation

↓

Normal Risk

↓

Continue

──────────────

Elevated Risk

↓

Require Additional Verification
```

High-risk situations may require stronger verification before sensitive actions.

---

# Just-In-Time (JIT) Access

Some privileged permissions are granted only when required.

```
Request Privileged Access

↓

Approval

↓

Temporary Access

↓

Task Completed

↓

Access Removed
```

This minimizes long-term privileged access.

---

# Access Reviews

Organizations periodically review permissions.

```
Users

↓

Assigned Roles

↓

Manager Review

↓

Approve

OR

Revoke
```

Regular reviews help maintain least privilege.

---

# Access Recertification

Large enterprises often require scheduled recertification.

```
Quarterly Review

↓

Managers

↓

Validate Access

↓

Remove Unnecessary Permissions
```

This reduces permission accumulation over time.

---

# Segregation of Duties Review

Organizations ensure incompatible permissions are not assigned together.

Example:

```
Create Invoice

+

Approve Invoice

↓

Conflict

↓

Review Required
```

Segregation of duties helps reduce fraud and operational risk.

---

# Zero Trust Authorization

Zero Trust assumes no request is automatically trusted.

```
Every Request

↓

Authenticate

↓

Authorize

↓

Evaluate Context

↓

Grant Limited Access
```

Authorization decisions are continuous rather than one-time events.

---

# Authorization Logging

Important authorization events include:

- Access granted
- Access denied
- Administrative actions
- Role assignments
- Permission changes
- Privileged operations
- Policy updates

Logs support investigations and compliance.

---

# Authorization Monitoring

```
Authorization Logs

↓

SIEM

↓

Correlation

↓

Alerting

↓

Security Operations Center
```

Monitoring helps identify abnormal access patterns.

---

# Enterprise Authorization Architecture

```
                 User

                   │

                   ▼

           Authentication

                   │

                   ▼

            API Gateway

                   │

                   ▼

      Policy Enforcement Point

                   │

                   ▼

      Policy Decision Point

        ┌─────────┼─────────┐

        ▼                   ▼

 Policy Store      Attribute Store

        │

        ▼

 Protected Services

        │

        ▼

 Databases / APIs
```

This architecture centralizes policy evaluation while allowing distributed enforcement.

---

# Enterprise Example

A multinational healthcare provider authorizes access as follows:

```
Doctor

↓

Authentication

↓

Role Verification

↓

Assigned Patient Check

↓

Department Policy

↓

Medical Record

↓

Access Granted
```

Additional controls include:

- Least privilege
- MFA for privileged actions
- Continuous monitoring
- Audit logging
- Quarterly access reviews
- Temporary privileged access for emergency maintenance

---

# Hands-on Lab (Conceptual)

Using a sample application:

1. Create multiple roles with different permissions.
2. Test access to protected pages.
3. Verify API responses for authorized and unauthorized users.
4. Modify object ownership and observe authorization changes.
5. Review authorization logs after successful and denied requests.
6. Simulate an access review by removing unnecessary permissions.

---

# Interview Questions

1. What is a Policy Enforcement Point (PEP)?
2. What is a Policy Decision Point (PDP)?
3. What is a Policy Information Point (PIP)?
4. Why should authorization be enforced on every API request?
5. What is object-level authorization?
6. Why is backend authorization essential?
7. What is Just-In-Time (JIT) access?
8. What are access reviews?
9. Why is segregation of duties important?
10. How does Zero Trust influence authorization?

---

# Best Practices

- Enforce authorization on every protected request.
- Perform authorization on the server.
- Protect APIs independently of the frontend.
- Apply least privilege throughout the system.
- Use centralized policy evaluation where practical.
- Perform regular access reviews and recertification.
- Log authorization decisions and privileged operations.
- Implement temporary privileged access for administrative tasks.

---

# Common Mistakes

- Assuming authentication automatically grants authorization.
- Trusting client-side permission checks.
- Missing authorization checks on internal APIs.
- Granting permanent privileged access.
- Ignoring object ownership during authorization.
- Failing to review accumulated permissions.
- Allowing incompatible duties without review.

---

# Key Takeaways

- Authorization must be consistently enforced across pages, APIs, services, and data.
- PEP, PDP, and PIP separate enforcement, decision-making, and policy information for scalable enterprise authorization.
- Object-level, record-level, and field-level authorization protect sensitive resources with fine granularity.
- Zero Trust authorization evaluates every request using context and policy.
- Continuous monitoring, logging, access reviews, and least privilege are essential for maintaining secure enterprise authorization.

# 12-Authorization-and-Access-Control.md

# Part 4 — Enterprise Authorization Governance, Identity Lifecycle, Access Auditing, Security Testing, Troubleshooting, Best Practices, and Chapter Summary

> **"Authorization is successful only when the correct permissions are granted, continuously validated, regularly reviewed, and immediately revoked when no longer required."**

---

# Learning Objectives

After completing this final part, you will understand:

- Enterprise Authorization Governance
- Identity Lifecycle Management
- Permission Reviews
- Access Auditing
- Authorization Monitoring
- Security Testing
- Authorization Troubleshooting
- Compliance Considerations
- Enterprise Best Practices
- Chapter Summary

---

# Enterprise Authorization Lifecycle

Authorization is not a one-time configuration.

```
User Created

↓

Assign Role

↓

Grant Permissions

↓

Access Resources

↓

Periodic Review

↓

Modify Permissions

↓

Revoke Access

↓

Archive Audit Records
```

Permissions should evolve as users' responsibilities change.

---

# Identity Lifecycle Management

A user's access changes throughout their employment or relationship with an organization.

```
Join Organization

↓

Account Created

↓

Role Assigned

↓

Department Change

↓

Role Updated

↓

Promotion

↓

Additional Permissions

↓

Resignation

↓

Access Revoked
```

Failure to manage this lifecycle increases security risk.

---

# Joiner-Mover-Leaver (JML) Model

Most enterprises follow the **Joiner-Mover-Leaver (JML)** process.

```
Joiner

↓

Create Account

↓

Assign Initial Role

──────────────

Mover

↓

Review Role

↓

Adjust Permissions

──────────────

Leaver

↓

Disable Account

↓

Terminate Sessions

↓

Remove Access
```

JML helps ensure permissions remain aligned with business responsibilities.

---

# Access Request Workflow

```
User Requests Access

↓

Manager Approval

↓

Security Review

↓

Permission Granted

↓

Audit Logged
```

Sensitive permissions should require appropriate approvals.

---

# Permission Revocation

Access should be removed promptly when no longer needed.

```
Permission No Longer Required

↓

Review

↓

Remove Permission

↓

Log Event
```

Delayed revocation may expose unnecessary risk.

---

# Permission Creep

Permission creep occurs when users accumulate access over time.

```
Employee

↓

Role Change

↓

Old Permissions Kept

↓

New Permissions Added

↓

Excessive Access
```

Regular access reviews help prevent permission creep.

---

# Access Certification

Managers periodically verify that users still require assigned permissions.

```
Assigned Permissions

↓

Manager Review

↓

Approve

OR

Remove Access
```

Certification supports least privilege and regulatory compliance.

---

# Privileged Access Governance

Privileged accounts require additional controls.

Examples:

- Domain administrators
- Database administrators
- Cloud administrators
- Security administrators
- Backup operators

Additional safeguards often include:

- MFA
- Just-In-Time (JIT) access
- Session recording (where appropriate)
- Approval workflows
- Enhanced monitoring

---

# Emergency Access ("Break Glass")

Organizations sometimes maintain emergency administrative accounts.

```
Emergency Incident

↓

Emergency Account

↓

Temporary Administrative Access

↓

Incident Resolved

↓

Password Rotation

↓

Audit Review
```

Emergency accounts should be tightly controlled and thoroughly audited.

---

# Authorization Monitoring

Organizations monitor authorization events continuously.

```
Access Request

↓

Authorization Decision

↓

Logging

↓

SIEM

↓

Security Team
```

Monitoring helps identify abnormal permission usage.

---

# High-Value Authorization Events

Important events include:

- Permission granted
- Permission revoked
- Role assignment
- Role removal
- Administrative action
- Policy modification
- Privileged access activation
- Access denial
- Resource deletion

---

# Authorization Audit Trail

```
User

↓

Authentication

↓

Authorization

↓

Protected Action

↓

Audit Log

↓

Compliance Review
```

Audit trails help reconstruct security events.

---

# Centralized Authorization Logging

```
Applications

↓

Authorization Logs

↓

Central Log Platform

↓

SIEM

↓

Analytics

↓

Alerting
```

Centralization simplifies investigations across multiple systems.

---

# Compliance Considerations

Many regulations require organizations to demonstrate proper authorization controls.

Typical expectations include:

- Least privilege
- Role-based access management
- Audit logging
- Access reviews
- Separation of duties
- Timely access revocation

Specific compliance requirements vary by industry and jurisdiction.

---

# Authorization Metrics

Organizations commonly monitor:

| Metric | Purpose |
|---------|----------|
| Failed authorization attempts | Detect misuse or misconfiguration |
| Privileged access requests | Monitor administrative activity |
| Access review completion | Governance effectiveness |
| Permission changes | Track authorization updates |
| Dormant privileged accounts | Identify unnecessary access |
| Role assignment trends | Detect unusual changes |

These metrics help measure the health of the authorization program.

---

# Authorization Security Testing

Authorization testing should evaluate:

- Role enforcement
- Object ownership validation
- Record-level authorization
- API authorization
- Administrative functions
- Privileged workflows
- Access revocation
- Policy consistency

Testing must always be performed only with proper authorization.

---

# Authorization Testing Workflow

```
Protected Resource

↓

Authenticate

↓

Attempt Access

↓

Expected Policy

↓

Verify Result

↓

Document Findings
```

Expected and actual behavior should match the defined authorization policy.

---

# Authorization Review Checklist

```
✓ Authentication Required

✓ Server-Side Authorization

✓ Least Privilege

✓ Role Reviews

✓ Object-Level Checks

✓ API Authorization

✓ Administrative Protection

✓ Access Revocation

✓ Audit Logging

✓ Continuous Monitoring
```

---

# Enterprise Troubleshooting

| Symptom | Possible Cause |
|----------|----------------|
| User cannot access resource | Missing role or permission |
| Administrator cannot perform action | Incorrect policy assignment or privilege issue |
| User sees another user's data | Missing object-level authorization |
| API returns access denied | Authorization policy or role mismatch |
| Access remains after role removal | Permission synchronization or cache issue |

Investigate authorization issues systematically.

---

# Troubleshooting Workflow

```
Authorization Issue

↓

Authentication Verified?

↓

Correct Role?

↓

Correct Permissions?

↓

Policy Evaluation

↓

Object Ownership

↓

Audit Logs

↓

Resolved
```

Each layer should be examined independently.

---

# Enterprise Authorization Architecture

```
                     Users

                       │

                       ▼

                Authentication

                       │

                       ▼

              API Gateway / WAF

                       │

                       ▼

          Policy Enforcement Point

                       │

                       ▼

           Policy Decision Point

         ┌──────────┼──────────┐

         ▼                     ▼

   Role Directory       Policy Repository

         │

         ▼

 Attribute Sources

         │

         ▼

 Business Services

         │

         ▼

 Databases / APIs / Files
```

This architecture supports centralized policy decisions with distributed enforcement.

---

# Enterprise Example

A global insurance company implements authorization as follows:

```
Claims Adjuster

↓

Authenticate

↓

RBAC Evaluation

↓

Department Attribute

↓

Claim Ownership Check

↓

Authorization Policy

↓

Claims Portal

↓

Audit Logging
```

Additional protections include:

- Multi-Factor Authentication for privileged operations
- Quarterly access reviews
- Automatic permission revocation after role changes
- Continuous SIEM monitoring
- Just-In-Time administrative access
- Segregation of duties for claim approval workflows

---

# Hands-on Lab (Conceptual)

Using a sample enterprise application:

1. Create users with different roles.
2. Assign object ownership to resources.
3. Verify access to authorized resources.
4. Attempt access to unauthorized resources and confirm denial.
5. Modify a user's role and verify updated permissions.
6. Remove access and ensure authorization changes take effect.
7. Review authorization logs for successful and denied requests.

---

# Interview Questions

1. What is the Joiner-Mover-Leaver (JML) process?
2. What is permission creep?
3. Why are periodic access reviews necessary?
4. What is privileged access governance?
5. What is a "break glass" account?
6. Why should authorization events be logged?
7. What should be included in an authorization security assessment?
8. Why is object-level authorization important?
9. What metrics help measure authorization effectiveness?
10. Why should access be revoked immediately after a user leaves an organization?

---

# Best Practices

- Apply the Principle of Least Privilege throughout the organization.
- Perform server-side authorization for every protected request.
- Review roles and permissions regularly.
- Remove unnecessary access immediately.
- Monitor privileged account activity continuously.
- Protect administrative functions with stronger controls.
- Maintain centralized authorization policies where practical.
- Log authorization decisions and permission changes.
- Automate Joiner-Mover-Leaver processes where possible.
- Conduct regular security and compliance reviews.

---

# Common Mistakes

- Allowing permission creep to accumulate.
- Forgetting to revoke access after role changes.
- Relying on client-side authorization.
- Sharing privileged accounts.
- Failing to review dormant accounts.
- Ignoring authorization logs.
- Embedding authorization logic inconsistently across applications.
- Performing authorization only at login instead of every protected request.

---

# Quick Revision

Authorization Flow

```
Authenticate

↓

Policy Evaluation

↓

Permission Check

↓

Access Granted

OR

Access Denied
```

Enterprise Governance

```
Provision

↓

Assign Role

↓

Review Access

↓

Modify Permissions

↓

Revoke Access
```

Authorization Architecture

```
User

↓

Authentication

↓

Policy Enforcement

↓

Policy Decision

↓

Protected Resource
```

---

# Chapter Summary

In this chapter, you learned:

- The difference between authentication and authorization.
- Core authorization concepts including subjects, resources, actions, permissions, and policies.
- Access control models such as DAC, MAC, RBAC, and ABAC.
- Enterprise authorization architecture using Policy Enforcement Points (PEP), Policy Decision Points (PDP), and Policy Information Points (PIP).
- Fine-grained authorization techniques including object-level, record-level, field-level, and API authorization.
- Governance concepts such as Joiner-Mover-Leaver (JML), permission reviews, privileged access management, and Just-In-Time (JIT) access.
- Authorization monitoring, centralized logging, security testing, troubleshooting, and enterprise best practices.

Effective authorization is a continuous process that combines centralized policy management, least privilege, fine-grained access control, regular reviews, and comprehensive monitoring to ensure users can access only the resources necessary for their legitimate business responsibilities.


