# Active-Directory/

# 09-Active-Directory-Trusts.md

# Part 1 — Introduction to Active Directory Trusts, Authentication Flow, Types of Trusts, and Enterprise Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Active Directory Trusts are.
- Learn why trusts are required.
- Understand authentication across domains.
- Learn the different trust types.
- Understand trust directions.
- Learn trust transitivity.
- Understand enterprise trust architecture.

---

# Introduction

Imagine a multinational organization with multiple domains.

```text
Forest

│

├── company.com

├── sales.company.com

├── finance.company.com

├── hr.company.com

└── research.company.com
```

Each domain has:

- Users
- Groups
- Computers
- Servers
- Applications

Question:

> How can a user in **Sales** access a file server located in **Finance** without creating a duplicate account?

The answer is:

> **Active Directory Trusts**

---

# What is an Active Directory Trust?

A **Trust** is a secure relationship between two security boundaries that allows authentication requests to be accepted across those boundaries.

Simply put,

> "I trust your authentication decisions."

A trust **does not automatically grant permissions**.

It only allows authentication to cross domains or forests.

Authorization is still controlled using permissions such as NTFS ACLs, Share Permissions, or application-specific access controls.

---

# Authentication vs Authorization

This is one of the most important concepts.

Authentication answers:

```text
Who are you?
```

Authorization answers:

```text
What are you allowed to access?
```

Trusts assist with:

```text
Authentication
```

Permissions determine:

```text
Authorization
```

---

# Example

Sales User:

```text
Alice
```

Lives in:

```text
sales.company.com
```

Needs access to:

```text
finance.company.com

Payroll Server
```

Process:

```text
Alice

↓

Authenticated

↓

Trust

↓

Finance Domain

↓

Permission Check

↓

Access Granted (if authorized)
```

---

# Why Trusts Exist

Without trusts:

```text
Sales User

↓

Finance Server

↓

Unknown User

↓

Access Denied
```

Administrator would have to:

- Create duplicate accounts
- Maintain multiple passwords
- Synchronize identities

This creates administrative overhead and security risks.

---

# With Trusts

```text
Sales User

↓

Authenticated

↓

Trust Relationship

↓

Finance Domain

↓

Identity Recognized

↓

Authorization

↓

Access
```

---

# Trust Architecture

```text
Domain A

──────────── Trust ────────────

Domain B
```

Authentication requests travel through the trust relationship.

---

# Real Enterprise Example

Company:

```text
company.com
```

Departments:

```text
sales.company.com

finance.company.com

hr.company.com
```

Employees:

- Finance users
- HR users
- Sales users

Each department manages its own accounts.

Trusts allow collaboration without duplicating identities.

---

# Security Boundary

A domain represents a security boundary.

```text
Domain

↓

Users

↓

Policies

↓

Resources
```

Trusts allow secure authentication **between** these boundaries.

---

# Default Trusts

When a child domain is created:

```text
company.com

↓

Create

↓

sales.company.com
```

Windows automatically creates trusts between the parent and child domains.

Administrators normally do not create these manually.

---

# Parent-Child Trust

Example:

```text
company.com

↓

sales.company.com
```

Authentication can travel between them because a trust exists.

---

# Tree Root Trust

Example:

```text
company.com

engineering.net
```

Both trees belong to the same forest.

A trust is automatically established between the tree roots.

---

# Forest Trust Model

```text
Forest

│

├── Tree A

├── Tree B

└── Tree C
```

Trusts allow authentication across the forest while maintaining separate domains.

---

# Trust Direction

A trust has a **direction**.

This determines which domain accepts authentication from another.

---

## One-Way Trust

```text
Domain A

────────►

Domain B
```

Meaning:

Domain B trusts authentication coming from Domain A.

Users in Domain A can potentially access resources in Domain B if they are granted permissions.

The reverse is **not** automatically true.

---

## Two-Way Trust

```text
Domain A

◄────────►

Domain B
```

Both domains trust each other's authentication decisions.

This is the most common trust type inside an Active Directory forest.

---

# Trust Direction Example

Finance trusts Sales.

```text
Sales

────────►

Finance
```

Sales users may access Finance resources **if** permissions allow.

Finance users do not automatically gain access to Sales resources unless a reverse trust also exists or the trust is bidirectional.

---

# Trust Transitivity

Another important concept.

A trust can be:

- Transitive
- Non-Transitive

---

## Transitive Trust

Suppose:

```text
Domain A

↓

Domain B

↓

Domain C
```

If trusts are transitive,

```text
A trusts B

B trusts C

↓

A can authenticate through B to C
```

Authentication can flow across the trust path.

---

## Non-Transitive Trust

```text
A trusts B

B trusts C

↓

A does NOT automatically trust C
```

Each trust must be explicitly configured.

---

# Trust Relationship Diagram

```text
                 Forest

                    │

      ┌─────────────┴─────────────┐

      │                           │

 company.com               engineering.net

      │                           │

 sales.company.com        dev.engineering.net
```

Authentication follows the established trust relationships.

---

# Default Trust Characteristics

Within the same forest:

- Automatically created (where applicable)
- Two-way
- Transitive

This enables seamless authentication across domains while preserving separate administration.

---

# Authentication Flow

```text
User

↓

Local Domain Controller

↓

Trust

↓

Target Domain Controller

↓

Authorization Check

↓

Access Granted
```

---

# Enterprise Example

Organization:

- 8 domains
- 5,000 employees
- Shared applications

Instead of creating accounts in every domain:

```text
Single User Account

↓

Trust

↓

Shared Authentication

↓

Resource Access
```

This reduces administrative complexity.

---

# Benefits of Trusts

| Benefit | Description |
|----------|-------------|
| Centralized identities | One account per user |
| Cross-domain authentication | Secure authentication across domains |
| Reduced administration | No duplicate user accounts |
| Scalability | Supports large enterprises |
| Better user experience | Single identity across trusted domains |

---

# Common Misconceptions

## Myth 1

> A trust automatically gives users access to resources.

**Reality:**

Trusts allow authentication.

Permissions determine authorization.

---

## Myth 2

> Every trust is two-way.

**Reality:**

Trusts may be one-way or two-way.

---

## Myth 3

> Every trust is transitive.

**Reality:**

Some trust types are transitive, while others are non-transitive.

---

# Cybersecurity Perspective

Trusts increase connectivity between security boundaries.

Security recommendations:

- Create only necessary trusts.
- Follow the principle of least privilege.
- Regularly review trust relationships.
- Monitor authentication across trust boundaries.
- Remove obsolete trusts.
- Audit privileged access spanning multiple domains or forests.

Poorly managed trusts can expand the impact of credential compromise.

---

# Hands-on Lab

## Objective

Explore trust relationships.

### Tasks

1. Open:

```text
Active Directory Domains and Trusts
```

2. Select:

```text
Domain

↓

Properties

↓

Trusts
```

3. Identify:

- Parent-child trusts
- Forest trusts
- Trust direction

4. Document:

- Trust type
- Direction
- Transitivity

---

# Key Takeaways

- A trust enables authentication across security boundaries.
- Trusts do **not** grant permissions.
- Authentication and authorization are different concepts.
- Trusts may be one-way or two-way.
- Trusts may be transitive or non-transitive.
- Parent-child trusts are automatically created within a forest.

---

# Interview Questions

1. What is an Active Directory Trust?
2. Why are trusts required?
3. What is the difference between authentication and authorization?
4. Does a trust automatically grant access to resources?
5. What is a one-way trust?
6. What is a two-way trust?
7. What is a transitive trust?
8. What is a non-transitive trust?
9. Why are trusts important in enterprise environments?
10. How are parent-child trusts created?

---

# References

- Microsoft Learn – Active Directory Trusts
- Microsoft Learn – Active Directory Domains and Trusts
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# 09-Active-Directory-Trusts.md

# Part 2 — Trust Types, External Trusts, Forest Trusts, Realm Trusts, Shortcut Trusts, SID Filtering, and Enterprise Design

---

# Learning Objectives

After completing this part, you will be able to:

- Understand every major Active Directory trust type.
- Learn when each trust should be used.
- Differentiate internal and external trust relationships.
- Understand SID filtering and why it is important.
- Design enterprise trust architectures.
- Apply security best practices for trust management.

---

# Review

From Part 1:

A trust provides:

```text
Authentication

Across

Security Boundaries
```

A trust **does not** provide:

```text
Permissions
```

Permissions are still required for resource access.

---

# Active Directory Trust Types

Microsoft Active Directory supports several trust types.

```text
Trusts

│

├── Parent-Child Trust

├── Tree-Root Trust

├── Shortcut Trust

├── External Trust

├── Forest Trust

└── Realm Trust
```

Each trust serves a different business requirement.

---

# Parent-Child Trust

Created automatically when:

```text
Parent Domain

↓

Child Domain Created
```

Example:

```text
company.com

↓

sales.company.com
```

Characteristics:

- Automatic
- Two-way
- Transitive

---

# Parent-Child Authentication

```text
Sales User

↓

sales.company.com

↓

Parent Trust

↓

company.com

↓

Resource Access
```

---

# Tree-Root Trust

Created automatically when a new tree is added to an existing forest.

Example:

```text
Forest

│

├── company.com

└── engineering.net
```

Characteristics:

- Automatic
- Two-way
- Transitive

---

# Tree Example

```text
Forest

│

├── company.com

│      └── sales.company.com

│

└── engineering.net

       └── dev.engineering.net
```

Tree-root trusts enable authentication between trees within the same forest.

---

# Shortcut Trust

As organizations grow, authentication paths may become long.

Example:

```text
Domain A

↓

Domain B

↓

Domain C

↓

Domain D
```

Without a shortcut:

```text
Authentication

↓

A

↓

B

↓

C

↓

D
```

---

# Shortcut Trust Solution

Create:

```text
Domain A

──────────────

Domain D
```

Authentication path becomes:

```text
A

↓

D
```

Benefits:

- Reduced authentication hops
- Lower latency
- Improved user experience
- Reduced Domain Controller workload

---

# Shortcut Trust Characteristics

| Property | Value |
|----------|-------|
| Automatic | No |
| Manual | Yes |
| Scope | Within the same forest |
| Transitive | Yes |
| Direction | One-way or Two-way |

---

# External Trust

An External Trust connects:

```text
Active Directory Domain

↓

Another Active Directory Domain

↓

Different Forest

OR

Standalone Domain
```

It does **not** create forest-wide authentication.

---

# External Trust Example

```text
Company A

────────────

Company B
```

Only the explicitly trusted domains participate.

Characteristics:

- Manual
- Non-transitive
- One-way or Two-way

---

# External Trust Authentication

```text
User

↓

Company A

↓

External Trust

↓

Company B

↓

Resource
```

Authentication does not automatically extend beyond the trusted domain.

---

# Forest Trust

A Forest Trust connects:

```text
Entire Forest A

↓

Entire Forest B
```

Example:

```text
Forest A

↓

company.com
```

```text
Forest B

↓

partner.com
```

One trust can support authentication between domains in both forests, subject to trust configuration and permissions.

---

# Forest Trust Characteristics

| Property | Value |
|----------|-------|
| Manual | Yes |
| Transitive | Yes (between the two forests) |
| Scope | Entire Forest |
| Direction | One-way or Two-way |

---

# Forest Trust Example

```text
Forest A

│

├── Sales

├── Finance

└── HR

      │

      │ Forest Trust

      ▼

Forest B

│

├── IT

├── Research

└── Support
```

---

# Realm Trust

A Realm Trust connects:

```text
Active Directory

↓

Kerberos Realm
```

Historically, this was commonly used to interoperate with non-Windows Kerberos implementations (for example, certain UNIX or MIT Kerberos environments).

Characteristics may vary depending on the Kerberos implementation and trust configuration.

---

# Realm Trust Example

```text
Active Directory

↓

Kerberos Trust

↓

UNIX Kerberos Realm
```

---

# Trust Comparison

| Trust Type | Automatic | Transitive | Typical Scope |
|------------|-----------|------------|---------------|
| Parent-Child | ✔ | ✔ | Same Forest |
| Tree-Root | ✔ | ✔ | Same Forest |
| Shortcut | ✘ | ✔ | Same Forest |
| External | ✘ | ✘ | Specific Domains |
| Forest | ✘ | ✔ | Two Forests |
| Realm | ✘ | Depends on configuration | AD ↔ Kerberos Realm |

---

# Enterprise Example

Company acquires another organization.

Before acquisition:

```text
Company A

Separate

Company B
```

Instead of migrating users immediately:

```text
Forest Trust

↓

Shared Authentication

↓

Business Continues
```

This allows collaboration while longer-term integration plans are developed.

---

# Authentication Path Comparison

Without Shortcut Trust:

```text
A

↓

B

↓

C

↓

D
```

With Shortcut Trust:

```text
A

↓

D
```

Fewer hops generally improve efficiency.

---

# Security Boundary

A trust **does not remove** security boundaries.

Each domain or forest continues to manage:

- Users
- Groups
- Policies
- Administrative authority

Trusts only allow authentication to cross those boundaries.

---

# SID Filtering

One of the most important security protections for trusts is:

> **SID Filtering**

---

# Why SID Filtering Exists

Suppose an attacker attempts to modify authorization information by adding unauthorized SIDs to a security token.

Without protection:

```text
Compromised Domain

↓

Forged SID

↓

Trusted Domain
```

This could increase risk if accepted.

SID Filtering helps reduce this risk by restricting which SIDs from a trusted source are honored across certain trust boundaries.

---

# Simplified SID Filtering Flow

```text
Authentication

↓

Trusted Domain

↓

SID Filtering

↓

Invalid SIDs Removed

↓

Resource Domain
```

---

# SID Filtering Benefits

- Helps prevent SID history abuse across applicable trusts.
- Reduces certain privilege escalation risks.
- Strengthens trust boundary security.
- Supports enterprise defense-in-depth.

---

# Enterprise Trust Design

Example:

```text
Corporate Forest

↓

Forest Trust

↓

Partner Forest
```

Internally:

```text
Parent-Child Trusts

↓

Shortcut Trusts

↓

Fast Authentication
```

This combines operational efficiency with controlled external collaboration.

---

# Design Considerations

| Requirement | Recommendation |
|-------------|----------------|
| Same Forest | Parent-Child or Tree-Root Trust |
| Long Authentication Paths | Shortcut Trust |
| Specific External Domain | External Trust |
| Two Organizations | Forest Trust |
| AD with Non-Windows Kerberos | Realm Trust |

---

# Common Administrative Mistakes

Avoid:

- Creating unnecessary trusts.
- Forgetting to review trust direction.
- Assuming every trust is transitive.
- Assuming authentication automatically grants permissions.
- Disabling security protections without understanding the implications.
- Leaving obsolete trusts in place after organizational changes.

---

# Best Practices

- Create only required trusts.
- Document every trust relationship.
- Review trust configurations regularly.
- Use the narrowest trust scope that satisfies business needs.
- Apply least privilege to resource permissions.
- Monitor authentication across trust boundaries.
- Review security settings, including SID filtering where applicable.

---

# Cybersecurity Perspective

Trusts increase connectivity between environments.

Potential risks include:

- Credential compromise
- Misconfigured trusts
- Excessive permissions
- Trust abuse
- Cross-boundary lateral movement

Defensive recommendations:

- Audit trust relationships regularly.
- Limit administrative access.
- Monitor cross-forest authentication.
- Review privileged group membership.
- Remove unused trusts promptly.
- Protect Domain Controllers and Global Catalog servers.

---

# Hands-on Lab

## Objective

Explore trust types.

### Tasks

1. Open:

```text
Active Directory Domains and Trusts
```

2. Review:

- Parent-child trusts
- Tree-root trusts
- External trusts
- Forest trusts (if available)

3. Document:

- Trust type
- Direction
- Transitivity
- Business purpose

4. Explain when a Shortcut Trust would improve authentication.

---

# Key Takeaways

- Active Directory supports multiple trust types for different scenarios.
- Parent-child and tree-root trusts are created automatically within a forest.
- Shortcut trusts reduce authentication path length.
- External trusts connect specific domains.
- Forest trusts connect two forests.
- SID filtering helps protect trust boundaries.

---

# Interview Questions

1. What is the difference between an External Trust and a Forest Trust?
2. When should a Shortcut Trust be created?
3. Which trust types are automatically created?
4. Which trust type is non-transitive?
5. What is a Realm Trust?
6. Why is SID filtering important?
7. Can a Forest Trust connect individual domains only?
8. Does a trust remove security boundaries?
9. Why should unnecessary trusts be removed?
10. How does a Shortcut Trust improve authentication?

---

# References

- Microsoft Learn – Active Directory Trusts
- Microsoft Learn – Forest Trusts
- Microsoft Learn – External Trusts
- Microsoft Learn – Kerberos Authentication
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# 09-Active-Directory-Trusts.md

# Part 3 — Trust Authentication Flow, Kerberos Across Trusts, Name Suffix Routing, Selective Authentication, SID History, and Troubleshooting

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Kerberos authentication across trusts.
- Learn referral ticket flow.
- Understand Name Suffix Routing.
- Learn Selective Authentication.
- Understand SID History.
- Troubleshoot trust-related authentication problems.
- Apply enterprise security best practices.

---

# Review

Previous parts covered:

- What Active Directory Trusts are
- Trust directions
- Trust transitivity
- Parent-Child Trusts
- Tree-Root Trusts
- Shortcut Trusts
- External Trusts
- Forest Trusts
- Realm Trusts
- SID Filtering

Now we'll see **how authentication actually travels across trust boundaries.**

---

# Cross-Domain Authentication

Suppose:

```text
Forest

│

├── sales.company.com

└── finance.company.com
```

User:

```text
Alice

↓

sales.company.com
```

Needs access to:

```text
Payroll Server

↓

finance.company.com
```

---

# Authentication Flow

```text
User

↓

Sales Domain Controller

↓

Trust

↓

Finance Domain Controller

↓

Authorization

↓

Payroll Server
```

The user authenticates in the home domain first.

---

# Authentication Steps

```text
1. User logs in

↓

2. Home Domain Controller validates credentials

↓

3. Kerberos Ticket Granting Ticket (TGT) issued

↓

4. User requests access to another domain

↓

5. Referral generated

↓

6. Target Domain validates referral

↓

7. Service Ticket issued

↓

8. Resource Access
```

---

# Kerberos Across Trusts

Kerberos remains the primary authentication protocol.

Example:

```text
Sales User

↓

Sales KDC

↓

Trust Referral

↓

Finance KDC

↓

Service Ticket

↓

Finance Server
```

Authentication remains secure because each domain trusts the authentication process—not the user's permissions.

---

# Kerberos Referral

One of Kerberos' strengths is the use of **referrals**.

Example:

```text
Client

↓

Sales KDC

↓

"Resource belongs to Finance"

↓

Referral Ticket

↓

Finance KDC

↓

Service Ticket

↓

Finance File Server
```

This allows authentication without sending passwords between domains.

---

# Referral Diagram

```text
Client

↓

Home Domain

↓

Referral

↓

Trusted Domain

↓

Service Ticket

↓

Target Server
```

---

# Ticket Flow

```text
User

↓

TGT

↓

Referral Ticket

↓

Service Ticket

↓

Application
```

Each ticket has a specific purpose.

---

# Trust Path Example

```text
Domain A

↓

Domain B

↓

Domain C

↓

Application
```

If a direct shortcut trust exists:

```text
Domain A

↓

Domain C

↓

Application
```

The authentication path becomes shorter.

---

# Name Suffix Routing

Forest Trusts support:

> **Name Suffix Routing**

---

# What is Name Suffix Routing?

Suppose:

```text
Forest A

↓

company.com
```

```text
Forest B

↓

partner.com
```

When a user attempts to authenticate using:

```text
user@partner.com
```

Active Directory determines:

```text
partner.com

↓

Forest B
```

and routes authentication appropriately.

---

# Name Suffix Routing Flow

```text
Authentication Request

↓

UPN Suffix

↓

Routing Table

↓

Correct Forest

↓

Authentication
```

This allows Forest Trusts to identify which forest should receive the authentication request.

---

# User Principal Name (UPN)

Example:

```text
alice@company.com
```

The suffix:

```text
company.com
```

is evaluated during routing decisions.

---

# Multiple Name Suffixes

Example:

```text
company.com

corp.company.com

research.company.com

partner.org
```

Each suffix can be configured for routing where appropriate.

---

# Selective Authentication

By default, trusted users may authenticate to servers according to the trust configuration and resource permissions.

For environments requiring tighter control, administrators can enable:

> **Selective Authentication**

---

# Why Selective Authentication?

Instead of allowing every authenticated user from a trusted domain to attempt authentication broadly,

administrators specify:

```text
Allowed Servers
```

Only approved systems accept authentication from the trusted domain.

---

# Selective Authentication Flow

```text
Trusted User

↓

Target Server

↓

Allowed to Authenticate?

↓

YES

↓

Continue

OR

↓

NO

↓

Access Denied
```

This provides an additional authorization gate before service access.

---

# Enterprise Example

Company acquires another organization.

Instead of allowing every employee immediate access:

```text
Forest Trust

↓

Selective Authentication

↓

Specific Servers Only
```

This limits exposure during integration.

---

# SID History

During migrations,

users often move between domains.

Example:

```text
Old Domain

↓

New Domain
```

Without assistance,

old permissions would stop working.

---

# What is SID History?

SID History stores previous Security Identifiers (SIDs) associated with an object.

This allows existing permissions referencing the old SID to continue working while migration is in progress.

---

# SID History Example

Before migration:

```text
Old SID

↓

Permissions
```

After migration:

```text
New SID

+

Old SID History

↓

Access Continues
```

---

# Why SID History Exists

Benefits:

- Simplifies domain migrations
- Maintains access during transition
- Reduces immediate ACL changes
- Supports phased migrations

---

# SID History and Security

Although useful,

SID History must be protected.

Potential risks include:

- Unauthorized SID History modification
- Privilege escalation
- Abuse during migrations

Monitor SID History changes carefully.

---

# Trust Authentication Example

```text
User

↓

Home Domain

↓

Kerberos TGT

↓

Referral

↓

Trusted Domain

↓

Service Ticket

↓

File Server
```

---

# Authentication Decision Process

```text
Identity Verified

↓

Trust Exists?

↓

YES

↓

Authorization

↓

Permissions Exist?

↓

YES

↓

Access Granted
```

---

# Common Trust Problems

Examples:

- DNS resolution failures
- Broken trust relationship
- Incorrect trust direction
- Time synchronization issues
- Kerberos failures
- Firewall restrictions
- Incorrect Name Suffix Routing
- Replication issues

---

# Troubleshooting Workflow

```text
Authentication Failure

↓

Verify DNS

↓

Verify Time Synchronization

↓

Verify Trust

↓

Verify Kerberos

↓

Verify Permissions

↓

Review Logs

↓

Resolve
```

---

# Useful Administrative Tools

| Tool | Purpose |
|------|----------|
| Active Directory Domains and Trusts | Manage trusts |
| Event Viewer | Authentication events |
| PowerShell AD Module | Query trust configuration |
| DCDiag | Domain Controller diagnostics |
| Repadmin | Replication validation |
| Klist | View Kerberos tickets |
| NLTest | Test trust relationships |

---

# Example Commands

Display Kerberos tickets:

```powershell
klist
```

List trust relationships:

```powershell
Get-ADTrust -Filter *
```

Verify trust:

```text
nltest /domain_trusts
```

---

# Enterprise Case Study

Organization:

- 3 Forests
- 18 Domains
- 120 Domain Controllers

Configuration:

```text
Forest Trusts

↓

Selective Authentication

↓

SID Filtering

↓

Tiered Administration

↓

Continuous Monitoring
```

Benefits:

- Controlled access
- Secure collaboration
- Reduced attack surface
- Improved governance

---

# Common Administrative Mistakes

Avoid:

- Ignoring DNS issues during trust troubleshooting.
- Assuming a trust grants permissions.
- Leaving unused trusts enabled.
- Forgetting to review Name Suffix Routing after organizational changes.
- Misconfiguring Selective Authentication.
- Failing to monitor SID History during migrations.

---

# Best Practices

- Use Kerberos wherever possible.
- Keep clocks synchronized.
- Monitor trust health regularly.
- Use Selective Authentication for external organizations when appropriate.
- Protect SID History.
- Review trust configurations periodically.
- Document every trust relationship.

---

# Cybersecurity Perspective

Trusts extend authentication across security boundaries and therefore require strong governance.

Security recommendations:

- Audit trust creation and modification.
- Monitor cross-domain authentication activity.
- Enable Selective Authentication where business needs require restricted access.
- Protect privileged accounts used across trusted environments.
- Review SID History during migrations.
- Monitor for unusual Kerberos referral activity.
- Remove obsolete trusts promptly.

---

# Hands-on Lab

## Objective

Examine trust authentication and verification.

### Tasks

1. Open:

```text
Active Directory Domains and Trusts
```

2. Review:

- Existing trust relationships
- Trust direction
- Authentication settings

3. Run:

```powershell
Get-ADTrust -Filter *
```

4. Run:

```text
nltest /domain_trusts
```

5. View Kerberos tickets:

```text
klist
```

6. Document:

- Trust type
- Authentication method
- Name Suffix Routing (if applicable)
- Security recommendations

---

# Key Takeaways

- Kerberos uses referral tickets to authenticate across trusted domains.
- Name Suffix Routing directs authentication requests between trusted forests.
- Selective Authentication restricts which servers accept authentication from trusted users.
- SID History supports domain migrations while preserving access.
- DNS, time synchronization, and Kerberos are fundamental to successful trust authentication.

---

# Interview Questions

1. How does Kerberos authenticate across trusted domains?
2. What is a referral ticket?
3. What is Name Suffix Routing?
4. When is Selective Authentication useful?
5. What is SID History?
6. Why is SID History important during migrations?
7. Which tool displays Kerberos tickets?
8. Which PowerShell cmdlet lists trust relationships?
9. What are common causes of trust failures?
10. Why is time synchronization critical for trust authentication?

---

# References

- Microsoft Learn – Active Directory Trust Authentication
- Microsoft Learn – Forest Trusts
- Microsoft Learn – Kerberos Authentication
- Microsoft Learn – SID History
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 4 — Trust Security, Monitoring, Best Practices, Final Revision, Chapter Summary, and Interview Preparation**