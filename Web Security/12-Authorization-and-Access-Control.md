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

```text id="jid720"
**Next:** Part 3
```