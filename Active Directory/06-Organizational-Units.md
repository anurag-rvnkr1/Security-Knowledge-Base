# 06-Organizational-Units.md

# Part 1 — Organizational Units (OUs): Fundamentals, Architecture, and Enterprise Design

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Organizational Units (OUs) are.
- Differentiate OUs from Containers.
- Understand why OUs exist in Active Directory.
- Learn how enterprises organize their Active Directory using OUs.
- Understand delegation at a high level.
- Design an enterprise-ready OU hierarchy.
- Prepare for Group Policy and Delegation concepts covered in later chapters.

---

# What is an Organizational Unit (OU)?

An **Organizational Unit (OU)** is a logical container within an Active Directory domain that is used to organize objects such as:

- Users
- Groups
- Computers
- Printers
- Service Accounts
- Other OUs

Unlike a physical folder on a disk, an OU is simply a management boundary that helps administrators organize and manage Active Directory efficiently.

Think of an OU as a folder that helps administrators organize objects for administration—not as a security boundary.

---

# Why Do Organizational Units Exist?

Imagine a company with:

- 50,000 employees
- 12 countries
- 300 departments
- 2,000 servers
- 45,000 workstations

Without OUs, every object would appear directly under the domain.

Example:

```text
company.com

├── User1
├── User2
├── User3
├── User4
├── User5
├── User6
├── Server1
├── Server2
├── Laptop1
├── Laptop2
├── Printer1
├── Printer2
├── ServiceAccount1
├── Group1
├── Group2
└── Thousands More...
```

Administration would quickly become unmanageable.

---

# Active Directory with Organizational Units

Instead, enterprises organize objects into meaningful structures.

Example:

```text
company.com

├── Corporate
│   ├── Users
│   ├── Computers
│   └── Groups
│
├── Finance
│   ├── Users
│   ├── Computers
│   └── Servers
│
├── HR
│   ├── Users
│   ├── Computers
│   └── Groups
│
├── IT
│   ├── Servers
│   ├── Administrators
│   ├── Workstations
│   └── Service Accounts
│
└── Branch Offices
    ├── Bangalore
    ├── London
    └── New York
```

This hierarchy improves organization, administration, and policy management.

---

# Real-World Analogy

Consider a university.

```text
University

├── Engineering
├── Medical
├── Commerce
├── Arts
└── Administration
```

Each department contains:

- Students
- Faculty
- Staff
- Laboratories

Similarly, Active Directory uses OUs to group related directory objects.

---

# Characteristics of an OU

An Organizational Unit:

- Exists within a domain.
- Can contain objects.
- Can contain child OUs.
- Supports Group Policy linking.
- Supports delegation of administration.
- Is replicated with Active Directory.
- Is not a security boundary.

---

# What Can Be Stored Inside an OU?

An OU may contain:

```text
Organizational Unit

│

├── Users

├── Groups

├── Computers

├── Printers

├── Service Accounts

├── Managed Service Accounts

└── Child OUs
```

This flexibility allows administrators to model business structures.

---

# Nested Organizational Units

OUs can contain additional OUs.

Example:

```text
Company

│

└── IT

      │

      ├── Servers

      ├── Workstations

      ├── Administrators

      ├── Security

      │      ├── SOC

      │      ├── Blue Team

      │      └── Red Team

      └── Cloud
```

Nested OUs help create logical administrative hierarchies.

---

# Benefits of Organizational Units

OUs provide:

- Logical organization
- Easier administration
- Delegation capabilities
- Group Policy targeting
- Improved scalability
- Better visibility
- Simplified automation
- Reduced administrative complexity

---

# Organizational Units vs Containers

Active Directory includes both **Containers** and **Organizational Units**.

Many beginners confuse the two.

---

# Default Containers

When a new domain is created, several containers already exist.

Example:

```text
Builtin

Computers

Users

ForeignSecurityPrincipals

Managed Service Accounts

Program Data
```

These are containers—not Organizational Units.

---

# Container vs OU Comparison

| Feature | Container | Organizational Unit |
|----------|------------|--------------------|
| Stores Objects | Yes | Yes |
| Can contain child OUs | No | Yes |
| Can contain child containers | Limited | Yes |
| Supports Group Policy | No | Yes |
| Supports Delegation | No | Yes |
| Administrative Flexibility | Limited | Excellent |
| Enterprise Usage | Minimal | Extensive |

---

# Why Not Use Default Containers?

Consider the default **Users** container.

```text
Users

├── Administrator

├── Guest

├── Default Accounts

├── User1

├── User2

├── User3

└── User5000
```

Problems:

- Difficult to manage
- Cannot directly link Group Policies
- Cannot delegate administration effectively
- Poor scalability

---

# Enterprise Recommendation

Most organizations create dedicated OUs.

Example:

```text
Company

│

├── Users

├── Servers

├── Workstations

├── Service Accounts

├── Domain Controllers

├── IT

├── HR

├── Finance

└── Branch Offices
```

This structure supports long-term growth and administration.

---

# OU Hierarchy Design Principles

Good OU design should reflect administrative needs rather than organizational charts alone.

Consider:

- Administrative ownership
- Group Policy requirements
- Delegation requirements
- Geographic locations
- Security requirements
- Device management
- Scalability

Avoid creating unnecessary depth.

---

# Example Enterprise OU Structure

```text
company.com

├── Corporate

│     ├── Users

│     ├── Groups

│     ├── Computers

│     └── Printers

├── IT

│     ├── Servers

│     ├── Workstations

│     ├── Service Accounts

│     └── Admin Accounts

├── Finance

│     ├── Users

│     └── Computers

├── HR

│     ├── Users

│     └── Computers

├── Research

├── Production

└── Branch Offices
```

This layout separates resources by administrative function and simplifies policy application.

---

# Naming Conventions

Use clear, consistent naming.

Examples:

Good:

```text
OU=Finance

OU=HR

OU=Servers

OU=Workstations

OU=Service Accounts

OU=Domain Controllers
```

Avoid:

```text
OU=Dept1

OU=NewOU

OU=ABC

OU=Temp

OU=Misc
```

Meaningful names improve maintainability.

---

# Distinguished Name (DN) Example

Every OU has a Distinguished Name (DN).

Example:

```text
OU=Finance,DC=company,DC=com
```

Nested example:

```text
OU=Users,OU=Finance,DC=company,DC=com
```

The DN uniquely identifies the object's location in Active Directory.

---

# Enterprise Example

A multinational organization operates in three regions.

```text
company.com

├── India

│     ├── Users

│     ├── Servers

│     └── Workstations

├── Europe

│     ├── Users

│     ├── Servers

│     └── Workstations

└── North America

      ├── Users

      ├── Servers

      └── Workstations
```

Each regional IT team can manage its own resources while adhering to corporate standards.

---

# Cybersecurity Perspective

Well-designed OUs support security operations by enabling:

- Targeted Group Policy deployment.
- Separation of privileged accounts.
- Isolation of sensitive systems.
- Easier auditing.
- Controlled administrative delegation.
- Consistent security configurations.

Although OUs are **not** security boundaries, they are a key component of secure administration.

---

# Common Mistakes

Avoid:

- Creating an OU for every individual employee.
- Deeply nested OU structures with little purpose.
- Naming OUs inconsistently.
- Mixing servers, users, and privileged accounts without planning.
- Using default containers for long-term administration.
- Designing OUs solely to mirror the company org chart.

---

# Hands-on Lab

## Objective

Explore the OU structure of an Active Directory domain.

### Tasks

1. Open **Active Directory Users and Computers (ADUC)**.
2. Identify:
   - Existing OUs
   - Default containers
3. Create a test OU named `Lab`.
4. Inside `Lab`, create:
   - `Users`
   - `Computers`
   - `Groups`
5. Observe the Distinguished Name (DN) of each OU.
6. Delete the test OUs after completing the exercise (if appropriate in your lab environment).

---

# Interview Questions

1. What is an Organizational Unit?
2. Why are OUs used in Active Directory?
3. Can an OU contain another OU?
4. What types of objects can be stored in an OU?
5. What is the difference between an OU and a Container?
6. Why are default containers generally avoided in enterprise environments?
7. What is a Distinguished Name (DN)?
8. Are Organizational Units security boundaries?
9. What are the benefits of using nested OUs?
10. What factors should influence OU design?

---

# Key Takeaways

- OUs provide logical organization for Active Directory objects.
- OUs support delegation and Group Policy.
- OUs can contain child OUs and a variety of directory objects.
- Default containers have limited management capabilities compared to OUs.
- Enterprise OU design should prioritize administrative and policy requirements over organizational charts.
- Proper OU planning simplifies management, automation, and security.

---

# 06-Organizational-Units.md

# Part 2 — OU Delegation, Group Policy Integration, Protection, and Enterprise Administration

---

# Learning Objectives

After completing this part, you will be able to:

- Understand administrative delegation using OUs.
- Learn how Group Policy is linked to OUs.
- Understand inheritance.
- Learn how objects are moved between OUs.
- Understand OU protection mechanisms.
- Design administrative boundaries for enterprise environments.
- Apply Microsoft best practices.

---

# Why Delegation Matters

Imagine a company with:

- 100,000 employees
- 15 IT departments
- 40 branch offices
- Hundreds of administrators

If every administrator had **Domain Admin** privileges, the environment would become extremely risky.

Instead, Active Directory allows administrators to delegate limited permissions.

---

# What is Delegation?

Delegation is the process of assigning specific administrative tasks to users or groups without granting full administrative control over the domain.

Example:

```text
Company

│

├── HR OU

│     └── HR Administrator

│

├── Finance OU

│     └── Finance Administrator

│

└── IT OU

      └── Infrastructure Team
```

Each administrator manages only their own OU.

---

# Benefits of Delegation

Delegation provides:

- Least privilege
- Better security
- Reduced administrative workload
- Departmental autonomy
- Easier auditing
- Lower risk of accidental changes
- Better compliance

---

# Delegation vs Domain Admin

| Domain Admin | Delegated Administrator |
|--------------|------------------------|
| Full domain control | Limited scope |
| Can modify every object | Can manage selected OUs |
| High security risk | Lower security risk |
| Used rarely | Used daily |
| Enterprise administrators | Department administrators |

---

# Real-World Example

Human Resources should manage:

- Employee accounts
- Password resets
- Disabled users
- Employee information

They should **not** manage:

- Domain Controllers
- DNS
- FSMO Roles
- Enterprise Admins
- Schema

Delegation allows this separation.

---

# Delegation Wizard

Active Directory Users and Computers provides the **Delegation of Control Wizard**.

It helps assign permissions such as:

- Reset passwords
- Create users
- Delete users
- Modify group membership
- Unlock accounts
- Join computers to the domain
- Create custom delegated tasks

---

# Delegation Workflow

```text
Domain Admin

        │

Delegates Permissions

        │

Department Administrator

        │

Manages

        │

Specific OU
```

The delegated administrator cannot exceed the permissions granted.

---

# Example Delegation

```text
company.com

├── Finance

│      ├── Users

│      ├── Groups

│      └── Computers

│

└── Finance IT Team
```

Permissions granted:

✔ Reset passwords

✔ Unlock accounts

✔ Create users

✔ Disable users

Not granted:

✖ Modify Domain Controllers

✖ Modify DNS

✖ Schema changes

✖ Forest-wide administration

---

# Delegation Best Practices

Delegate permissions to **security groups**, not individual users.

Example:

```text
Finance-Helpdesk

HR-Admins

Branch-IT

Server-Operators
```

Then add users to those groups.

This simplifies administration.

---

# Principle of Least Privilege

One of the most important security principles.

Give administrators:

✔ Only the permissions they need

Never:

✔ "Just in case" permissions

Example:

```text
Helpdesk

↓

Reset Password

Unlock Account

Modify Telephone Number
```

Instead of:

```text
Domain Admin
```

---

# Delegation Through ACLs

Delegation works by modifying the **Access Control List (ACL)** on an OU.

Simplified:

```text
OU

↓

ACL

↓

Permissions

↓

Administrator
```

The ACL determines what actions are allowed.

---

# Group Policy and Organizational Units

One of the primary reasons OUs exist is to apply **Group Policy Objects (GPOs).**

Example:

```text
OU

↓

Linked GPO

↓

Applies Settings

↓

Users & Computers
```

Without OUs, targeted policy application becomes much more difficult.

---

# Why Link GPOs to OUs?

Different departments require different settings.

Example:

Finance

- Disable USB
- Enable BitLocker
- Restrict PowerShell

HR

- Office settings
- Printer deployment
- Desktop wallpaper

IT

- Remote administration
- RSAT tools
- Developer utilities

Each OU can receive its own policies.

---

# Enterprise Example

```text
Company

│

├── Finance

│      └── Finance GPO

│

├── HR

│      └── HR GPO

│

├── IT

│      └── IT Admin GPO

│

└── Servers

       └── Server Hardening GPO
```

Each department receives only relevant policies.

---

# Moving Objects Between OUs

Objects may need to be reorganized.

Example:

Employee transfers from Finance to HR.

Old location:

```text
Finance

└── Alice
```

New location:

```text
HR

└── Alice
```

Moving the user changes the OU and may result in different Group Policies being applied.

---

# Effects of Moving Objects

Moving a user or computer can affect:

- Applied GPOs
- Login scripts
- Software deployment
- Security settings
- Folder redirection
- Administrative ownership

Always assess the impact before moving objects.

---

# Administrative Boundaries

Many enterprises organize OUs by administration rather than by the company's reporting structure.

Instead of:

```text
CEO

↓

Managers

↓

Employees
```

Use:

```text
Servers

Workstations

Users

Service Accounts

Privileged Accounts
```

This aligns better with management tasks.

---

# Geographic OU Design

Example:

```text
Company

├── India

│      ├── Users

│      ├── Computers

│      └── Servers

├── Germany

│      ├── Users

│      ├── Computers

│      └── Servers

└── USA

       ├── Users

       ├── Computers

       └── Servers
```

Regional administrators can manage their own resources.

---

# Department-Based Design

Example:

```text
Company

├── Finance

├── HR

├── Sales

├── Marketing

├── IT

└── Legal
```

Simple and suitable for smaller organizations.

---

# Hybrid OU Design

Many enterprises combine multiple approaches.

Example:

```text
Company

├── India

│      ├── Finance

│      ├── HR

│      ├── IT

│      └── Sales

├── Europe

│      ├── Finance

│      ├── HR

│      ├── IT

│      └── Sales

└── North America

       ├── Finance

       ├── HR

       ├── IT

       └── Sales
```

This supports both geographic and departmental administration.

---

# Protecting Organizational Units

Active Directory provides the option:

> **Protect object from accidental deletion**

When enabled:

```text
Administrator

↓

Delete OU

↓

Denied
```

This protection helps prevent accidental removal of important OUs.

---

# Why Protection Matters

Deleting an OU may remove:

- Hundreds of users
- Thousands of computers
- Group memberships
- Linked policies
- Administrative structure

Protection reduces the likelihood of costly mistakes.

---

# Common Administrative Tasks

Typical OU administration includes:

- Creating OUs
- Renaming OUs
- Moving OUs
- Delegating permissions
- Linking GPOs
- Managing child OUs
- Auditing permissions
- Reviewing inheritance

---

# Cybersecurity Perspective

A well-designed OU structure improves security by enabling:

- Separation of privileged accounts
- Different security baselines for servers and workstations
- Department-specific hardening
- Easier compliance audits
- Reduced administrative privileges
- Controlled delegation

Remember:

> OUs are management boundaries—not security boundaries.

Security enforcement is achieved through permissions, authentication, and Group Policy.

---

# Common Mistakes

Avoid:

- Granting Domain Admin to departmental administrators.
- Delegating permissions directly to users instead of groups.
- Creating unnecessary nested OUs.
- Moving objects without understanding policy impacts.
- Mixing privileged accounts with standard user accounts.
- Leaving critical OUs unprotected against accidental deletion.

---

# Hands-on Lab

## Objective

Practice delegation and OU management.

### Tasks

1. Create an OU named `Finance`.
2. Create child OUs:
   - Users
   - Computers
   - Groups
3. Create a security group named `Finance-Helpdesk`.
4. Use the **Delegation of Control Wizard** to grant:
   - Reset Password
   - Unlock Account
5. Enable **Protect object from accidental deletion** on the `Finance` OU.
6. Move a test user into the `Finance\Users` OU.
7. Document the resulting Distinguished Name (DN).

---

# Interview Questions

1. What is delegation in Active Directory?
2. Why should administrators avoid assigning Domain Admin rights broadly?
3. What is the Delegation of Control Wizard used for?
4. Why should permissions be delegated to groups instead of users?
5. How do OUs help with Group Policy?
6. What happens when an object is moved to another OU?
7. What is the purpose of "Protect object from accidental deletion"?
8. Are OUs security boundaries?
9. Why is the principle of least privilege important?
10. What factors influence enterprise OU design?

---

# Key Takeaways

- Delegation enables secure, limited administration of Active Directory.
- OUs are the primary targets for Group Policy.
- Moving objects between OUs can change applied policies and administrative ownership.
- Enterprise OU structures should reflect administrative and policy requirements.
- Always protect critical OUs from accidental deletion.
- Delegate permissions through security groups and follow the principle of least privilege.

---

# 06-Organizational-Units.md

# Part 3 — Group Policy Inheritance, OU Design Strategies, Automation, Troubleshooting, and Enterprise Best Practices

---

# Learning Objectives

After completing this part, you will be able to:

- Understand how Group Policy inheritance works with OUs.
- Learn Block Inheritance and Enforced policies.
- Design scalable OU structures.
- Understand Microsoft's recommended OU design.
- Learn automation concepts.
- Troubleshoot common OU-related issues.
- Apply enterprise best practices.

---

# Organizational Units and Group Policy

One of the biggest advantages of Organizational Units is their ability to receive **Group Policy Objects (GPOs).**

A GPO linked to an OU automatically affects the users and computers located inside that OU unless inheritance is blocked or filtering prevents application.

Example:

```text
Company.com

│

├── Finance OU
│      ├── Users
│      └── Computers
│
└── HR OU
       ├── Users
       └── Computers

Finance GPO
        ↓
Finance Users & Computers
```

---

# Understanding Group Policy Scope

A Group Policy can be linked to:

- Site
- Domain
- Organizational Unit

Example:

```text
Site

↓

Domain

↓

Parent OU

↓

Child OU

↓

User / Computer
```

Policies flow downward unless configured otherwise.

---

# Group Policy Inheritance

Inheritance means that child OUs receive policies linked to their parent containers.

Example:

```text
Company

│

├── Corporate

│     ├── Users

│     └── Computers
```

If a policy is linked to **Corporate**, both child OUs inherit it.

---

# Example

```text
Company

│

├── IT

│     ├── Servers

│     └── Workstations
```

If a password policy or software deployment GPO is linked to **IT**, both **Servers** and **Workstations** inherit that policy (unless filtering or blocking changes the behavior).

---

# Policy Processing Flow

```text
Local Policy

↓

Site GPO

↓

Domain GPO

↓

Parent OU

↓

Child OU
```

This is commonly referred to as the **LSDOU** processing order, which will be explored in detail in the Group Policy chapter.

---

# Block Inheritance

Sometimes an OU should **not** receive policies from its parent.

Example:

```text
Company

│

├── Corporate

│

└── Research
      (Block Inheritance)
```

The Research OU ignores inherited policies unless a parent policy is marked as **Enforced**.

Common use cases:

- Test environments
- Research labs
- Isolated administrative environments

---

# Enforced Policies

An administrator may require a policy to apply regardless of Block Inheritance.

Example:

```text
Company Password Policy

↓

Enforced

↓

All Child OUs
```

Enforced policies override Block Inheritance.

Typical enterprise examples include:

- Security settings
- Audit configuration
- Domain-wide restrictions

---

# Inheritance Example

```text
Domain

│

├── Corporate

│      │
│      └── Finance

│

└── Research
```

Policy Linked:

```text
Domain Password Policy
```

Results:

| OU | Receives Policy |
|----|-----------------|
| Corporate | Yes |
| Finance | Yes |
| Research | Yes (unless special configuration exists) |

---

# When Should Block Inheritance Be Used?

Use it only when necessary.

Good examples:

- Dedicated lab environments
- Specialized testing
- Temporary migration projects
- Isolated development forests

Poor examples:

- Avoiding proper GPO design
- Solving policy conflicts without analysis
- Everyday administration

---

# Designing Enterprise OUs

Microsoft recommends designing OUs based on:

- Administration
- Policy requirements
- Security requirements
- Geographic regions
- Device type

Avoid designing OUs purely around reporting structures.

---

# Poor OU Design

```text
CEO

├── VP

│     ├── Manager

│           ├── Employee

│                 ├── Employee

│                      ├── Employee
```

Problems:

- Difficult administration
- Frequent restructuring
- Deep hierarchy
- Complex policy management

---

# Better Enterprise Design

```text
Company

├── Users

├── Computers

├── Servers

├── Service Accounts

├── Privileged Accounts

├── Workstations

├── Domain Controllers

└── Groups
```

Administrative tasks become much easier.

---

# Separating Workstations and Servers

Never mix servers and workstations inside the same OU.

Recommended:

```text
Company

├── Servers

│      ├── File Servers

│      ├── Web Servers

│      └── SQL Servers

└── Workstations
```

Reason:

Different security policies apply to each.

---

# Privileged Accounts

Enterprise administrators usually maintain a dedicated OU.

Example:

```text
Privileged Accounts

├── Domain Admins

├── Enterprise Admins

├── Server Admins

└── Security Admins
```

Separate policies protect privileged identities.

---

# Service Accounts

Dedicated OU:

```text
Service Accounts

├── SQL Service

├── IIS Service

├── Backup Service

└── Monitoring Service
```

Benefits:

- Easier auditing
- Dedicated security settings
- Simplified lifecycle management

---

# Computer Lifecycle Example

```text
New Computer

↓

Staging OU

↓

Deployment

↓

Production OU

↓

Retirement OU

↓

Deletion
```

Many organizations use temporary OUs during provisioning.

---

# User Lifecycle Example

```text
New User

↓

HR OU

↓

Department OU

↓

Transferred

↓

Disabled Users OU

↓

Deleted
```

OUs help organize identity lifecycle processes.

---

# Automation with OUs

PowerShell simplifies OU management.

Example tasks include:

- Create OUs
- Rename OUs
- Move users
- Bulk user creation
- Bulk computer movement
- Generate reports

Example:

```powershell
New-ADOrganizationalUnit -Name "Finance"
```

Move a user:

```powershell
Move-ADObject
```

Detailed PowerShell examples are covered in Chapter 17.

---

# Enterprise Automation

Large enterprises automate:

- Department creation
- Branch office deployment
- New user onboarding
- Computer staging
- Security auditing
- Compliance reporting

Automation reduces manual errors and improves consistency.

---

# OU Troubleshooting

Common issues include:

- GPO not applying
- User in wrong OU
- Computer moved accidentally
- Delegation not working
- Missing permissions
- Replication delays
- Incorrect inheritance settings

---

# Troubleshooting Checklist

| Check | Why It Matters |
|---------|----------------|
| Correct OU | Ensures expected GPOs apply |
| Replication healthy | Prevents inconsistent views |
| Permissions | Confirms delegated access |
| Inheritance | Verifies policy flow |
| Security filtering | Confirms GPO scope |
| WMI filters | Checks device targeting |
| Object location | Ensures correct administrative scope |

---

# Monitoring OUs

Administrators should monitor:

- New OU creation
- Deleted OUs
- Moved objects
- Permission changes
- Delegation changes
- GPO links
- Administrative activity

Logging helps identify unauthorized modifications.

---

# Enterprise Case Study

Company:

- 75,000 employees
- 15 countries
- 9 regional IT teams

OU Design:

```text
Company

├── Users

├── Workstations

├── Servers

├── Privileged Accounts

├── Service Accounts

├── Branch Offices

└── Contractors
```

Each regional IT team receives delegated permissions only for its assigned OUs.

Benefits:

- Reduced administrative risk
- Simplified GPO management
- Faster onboarding
- Better compliance
- Easier auditing

---

# Cybersecurity Perspective

A well-planned OU structure strengthens security operations by:

- Separating privileged identities.
- Applying different hardening baselines.
- Isolating administrative accounts.
- Supporting least privilege.
- Simplifying incident response.
- Improving auditability.

Example:

```text
Standard Users

↓

Standard GPO

Privileged Users

↓

Hardened GPO

↓

MFA

↓

Restricted Logon

↓

Enhanced Auditing
```

---

# Common Mistakes

Avoid:

- Extremely deep OU hierarchies.
- Frequent OU restructuring.
- Mixing privileged and standard accounts.
- Applying every GPO at the domain level.
- Using Block Inheritance excessively.
- Ignoring documentation.
- Delegating permissions without regular review.

---

# Best Practices Checklist

✔ Design OUs around administration.

✔ Keep the hierarchy simple.

✔ Separate servers from workstations.

✔ Create dedicated OUs for privileged accounts.

✔ Use meaningful names.

✔ Delegate permissions through groups.

✔ Document OU structure.

✔ Protect important OUs from accidental deletion.

✔ Review delegated permissions periodically.

✔ Test Group Policy before production deployment.

---

# Hands-on Lab

## Objective

Design a scalable OU hierarchy for a fictional enterprise.

### Scenario

Company:

- 3,000 employees
- IT
- HR
- Finance
- Sales
- London
- Bengaluru
- New York

### Tasks

1. Create a root OU for each location.
2. Create child OUs:
   - Users
   - Computers
   - Groups
   - Servers
3. Create a dedicated `Privileged Accounts` OU.
4. Create a `Service Accounts` OU.
5. Link placeholder GPOs to:
   - Servers
   - Workstations
   - Privileged Accounts
6. Enable accidental deletion protection on all production OUs.
7. Document the final hierarchy.

---

# Interview Questions

1. Why should OUs be designed around administration instead of organizational charts?
2. What is Group Policy inheritance?
3. What is Block Inheritance?
4. What does an Enforced GPO do?
5. Why should servers and workstations be placed in separate OUs?
6. Why are privileged accounts usually stored in a dedicated OU?
7. What are the benefits of PowerShell automation for OU management?
8. How can accidental deletion of an OU be prevented?
9. What should be checked when a GPO is not applying to an OU?
10. What are common OU design mistakes?

---

# Key Takeaways

- OUs are central to enterprise administration and Group Policy management.
- Policies inherit through the OU hierarchy unless inheritance is blocked or overridden by an Enforced GPO.
- Design OUs based on administrative and policy requirements, not organizational charts alone.
- Separate privileged accounts, servers, workstations, and service accounts into dedicated OUs.
- Automation and documentation improve consistency and reduce administrative overhead.
- Regular reviews of delegation, permissions, and OU structure help maintain a secure Active Directory environment.

---

**Next:** Part 4