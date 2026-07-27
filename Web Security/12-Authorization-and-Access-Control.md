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

```text id="jid720"
**Next:** Part 2
```