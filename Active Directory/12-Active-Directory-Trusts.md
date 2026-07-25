# 12-Active-Directory-Trusts.md

# Part 1 — Introduction to Active Directory Trusts, Authentication Across Domains, Trust Architecture, and Enterprise Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what an Active Directory Trust is.
- Learn why trusts are required.
- Understand authentication across domains.
- Learn trust terminology.
- Understand trust architecture.
- Differentiate authentication from authorization.
- Prepare for advanced trust concepts.

---

# Introduction

Large organizations often have multiple:

- Domains
- Forests
- Business units
- Geographic regions

Example:

```text
Company Forest

│

├── india.company.com

├── europe.company.com

├── usa.company.com

└── japan.company.com
```

Even though these domains belong to the same organization, users frequently need access to resources located outside their own domain.

Active Directory solves this problem using **Trust Relationships**.

---

# What is an Active Directory Trust?

An **Active Directory Trust** is a secure relationship between two domains or forests that allows authentication requests to be accepted across administrative boundaries.

A trust does **not** automatically grant access to resources.

Instead, it allows one domain to **recognize and validate** identities from another trusted domain.

---

# Simple Example

Suppose:

```text
Domain A

↓

Alice
```

Needs access to:

```text
Domain B

↓

File Server
```

Without a trust:

```text
Alice

↓

Authentication Request

↓

Rejected
```

With a trust:

```text
Alice

↓

Authentication Request

↓

Domain B

↓

Trusts Domain A

↓

Authentication Accepted
```

---

# Real-World Analogy

Imagine two companies.

Company A issues employee ID cards.

Company B decides:

> "We trust Company A's identity verification process."

Employees from Company A can now enter Company B's office after verification.

However, they still need permission to enter specific rooms.

Trust verifies **identity**, not **permission**.

---

# Authentication vs Authorization

One of the most misunderstood Active Directory concepts is the difference between authentication and authorization.

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to access?

---

# Example

User:

```text
Rahul
```

Authentication:

```text
Username

↓

Password

↓

Verified
```

Authorization:

```text
Can Rahul Access

Finance Share?

↓

Yes / No
```

Trusts participate in **authentication**, while permissions and Access Control Lists (ACLs) determine **authorization**.

---

# Why Trusts Are Needed

Without trusts:

```text
India Domain

↓

Cannot Validate

Europe User
```

Every domain would require:

- Separate accounts
- Duplicate administration
- Duplicate passwords
- Duplicate permissions

This quickly becomes difficult to manage.

---

# With Trusts

```text
India Domain

↓

Trust

↓

Europe Domain

↓

Authentication Works
```

Users maintain a single identity while accessing authorized resources across trusted domains.

---

# Enterprise Example

Organization:

```text
GlobalTech

│

├── india.globaltech.com

├── europe.globaltech.com

├── usa.globaltech.com

└── japan.globaltech.com
```

Employee:

```text
Emma

↓

Europe Domain
```

Needs access to:

```text
Engineering Wiki

↓

India Domain
```

Instead of creating another account:

```text
Trust

↓

Authentication

↓

ACL Verification

↓

Access Granted
```

---

# Trust Architecture

```text
Domain A

←──── Trust ────→

Domain B
```

The trust relationship enables authentication requests to travel securely between domains.

---

# What Happens During Authentication?

Example:

```text
User

↓

Logs Into

Domain A
```

Later:

```text
Access Resource

↓

Domain B
```

Workflow:

```text
Domain B

↓

Trusts Domain A

↓

Authentication Verified

↓

Authorization Checked

↓

Resource Access
```

---

# Identity Remains in the Home Domain

The user's account always belongs to its original domain.

Example:

```text
User

↓

india.company.com
```

Accessing:

```text
europe.company.com
```

The account is **not copied** into Europe.

Instead:

```text
Europe Domain

↓

Trusts

↓

India Domain

↓

Identity Verified
```

---

# Trust Does Not Mean Full Access

A common misconception:

```text
Trust Exists

↓

Everything Accessible
```

Incorrect.

Actual workflow:

```text
Trust

↓

Authentication

↓

ACL Evaluation

↓

Access Decision
```

Permissions are still enforced.

---

# Benefits of Trusts

Trusts provide:

- Centralized identity
- Reduced administrative overhead
- Single user account
- Cross-domain authentication
- Improved scalability
- Better resource sharing
- Simplified administration

---

# Common Scenarios

Trusts are commonly used for:

- Multi-domain forests
- Company mergers
- Acquisitions
- Business partnerships
- Resource forests
- Enterprise application access

---

# Trust Components

Every trust relationship involves:

- Trusting domain
- Trusted domain
- Authentication path
- Security boundary
- Access control

Together, these define how identities are validated across domains.

---

# Example Authentication Flow

```text
User

↓

Home Domain

↓

Requests File

↓

Remote Domain

↓

Trust Verification

↓

Permission Check

↓

Access Granted
```

---

# Forest Example

```text
Forest

│

├── HR Domain

├── Finance Domain

├── IT Domain

└── Sales Domain
```

An HR employee can access an IT application only if:

- Authentication succeeds through trust.
- Authorization permits access.

---

# Why Trusts Improve Security

Without trusts:

Organizations often create duplicate accounts.

Problems include:

- Password inconsistencies
- Forgotten accounts
- Excessive permissions
- Increased attack surface

Trusts help reduce unnecessary identity duplication.

---

# Enterprise Benefits

Large organizations gain:

- Easier identity management
- Lower administrative costs
- Better user experience
- Centralized authentication
- Improved scalability
- Consistent security model

---

# Cybersecurity Perspective

Trust relationships are security-sensitive because they extend authentication between security boundaries.

Security teams should:

- Regularly review trust relationships.
- Remove unused trusts.
- Monitor authentication across trusts.
- Audit privileged access.
- Document trust architecture.
- Apply least privilege.

Poorly managed trusts can expand the impact of a compromised account.

---

# Common Mistakes

Avoid:

- Confusing authentication with authorization.
- Assuming trusts automatically grant permissions.
- Creating unnecessary trusts.
- Forgetting to document trust relationships.
- Ignoring trust security during mergers or acquisitions.

---

# Hands-on Lab

## Objective

Explore trust relationships.

### Tasks

1. Open:

```text
Active Directory Domains and Trusts
```

2. Select your domain.

3. Open:

```text
Properties

↓

Trusts Tab
```

4. Record:

- Existing trusts
- Trust direction
- Trust type
- Trusted domains

5. Draw a simple trust diagram for your environment.

---

# Interview Questions

1. What is an Active Directory Trust?
2. Why are trusts required?
3. What is the difference between authentication and authorization?
4. Does a trust automatically grant access?
5. What happens when a user accesses a resource in another trusted domain?
6. Why are duplicate user accounts discouraged?
7. What are common enterprise use cases for trusts?
8. Which Microsoft console is commonly used to manage trusts?
9. Why are trust relationships considered security-sensitive?
10. What information should administrators document about trusts?

---

# Key Takeaways

- Active Directory Trusts allow domains or forests to recognize and authenticate identities across security boundaries.
- Trusts enable authentication but do **not** automatically grant authorization to resources.
- Users retain a single identity in their home domain while accessing authorized resources in trusted domains.
- Properly designed trusts simplify administration and improve scalability in multi-domain and multi-forest environments.
- Trust relationships should be carefully planned, documented, monitored, and secured.

---

# 12-Active-Directory-Trusts.md

# Part 2 — Trust Directions, Trust Types, Transitive & Non-Transitive Trusts, Forest Trusts, External Trusts, Shortcut Trusts, and Realm Trusts

---

# Learning Objectives

After completing this part, you will be able to:

- Understand trust directions.
- Differentiate one-way and two-way trusts.
- Learn transitive and non-transitive trusts.
- Understand various Active Directory trust types.
- Learn where each trust type is used.
- Design trust relationships for enterprise environments.

---

# Understanding Trust Direction

Trust direction defines **which domain accepts authentication requests from another domain**.

Many administrators mistakenly assume trust direction refers to data flow.

It actually defines **authentication flow**.

---

# Basic Trust Model

Example:

```text
Domain A

──────── Trust ────────>

Domain B
```

Interpretation:

```text
Domain B

Accepts Authentication

From

Domain A
```

Users in Domain A can be authenticated by Domain B (subject to permissions).

---

# Trusting Domain vs Trusted Domain

| Component | Meaning |
|-----------|---------|
| Trusted Domain | Contains the user account being authenticated |
| Trusting Domain | Accepts authentication from the trusted domain |

Example:

```text
User

↓

india.company.com
```

Accessing:

```text
finance.company.com
```

If Finance accepts authentication:

```text
Finance Domain

↓

Trusting Domain
```

```text
India Domain

↓

Trusted Domain
```

---

# One-Way Trust

In a **One-Way Trust**, authentication works in only one direction.

Example:

```text
Domain A

────────────>

Domain B
```

Meaning:

- Domain B accepts users from Domain A.
- Domain A does **not** automatically accept users from Domain B.

---

# One-Way Trust Example

```text
HR Domain

────────────>

Finance Domain
```

Result:

```text
HR Users

↓

Can Authenticate

↓

Finance Resources
```

But:

```text
Finance Users

↓

Cannot Authenticate

↓

HR Resources
```

Unless another trust is created.

---

# Two-Way Trust

A **Two-Way Trust** allows authentication in both directions.

```text
Domain A

<────────────>

Domain B
```

Both domains recognize authenticated users from each other.

Authorization is still controlled separately.

---

# Two-Way Enterprise Example

```text
Engineering

<────────────>

Research
```

Benefits:

- Shared applications
- Cross-domain collaboration
- Simplified authentication
- Reduced duplicate accounts

---

# Comparing Trust Directions

| Feature | One-Way | Two-Way |
|----------|---------|----------|
| Authentication | Single direction | Both directions |
| Administration | More restrictive | More flexible |
| Resource Sharing | Limited | Easier |
| Typical Usage | Partners, restricted access | Internal enterprise domains |

---

# Understanding Transitive Trust

A **Transitive Trust** extends trust beyond directly connected domains.

Example:

```text
Domain A

<────>

Domain B

<────>

Domain C
```

Because trust is transitive:

```text
Domain A

↓

Can Authenticate

↓

Domain C
```

(assuming the trust chain supports it and permissions allow access).

---

# Transitive Trust Illustration

```text
A

↓

Trust

↓

B

↓

Trust

↓

C

↓

Authentication Possible
```

Trust automatically extends through the chain.

---

# Advantages of Transitive Trusts

Benefits include:

- Less administrative effort
- Simplified management
- Better scalability
- Automatic trust extension
- Ideal for enterprise forests

---

# Non-Transitive Trust

A **Non-Transitive Trust** exists only between two directly connected domains.

Example:

```text
A

<────>

B

C
```

Domain C is **not** included.

---

# Non-Transitive Example

```text
Company Domain

↓

Trust

↓

Partner Domain
```

Another unrelated partner:

```text
Vendor Domain
```

No automatic authentication exists between:

```text
Partner

×

Vendor
```

---

# Comparing Transitive and Non-Transitive Trusts

| Feature | Transitive | Non-Transitive |
|----------|------------|----------------|
| Trust Extension | Automatic | No |
| Enterprise Scalability | Excellent | Limited |
| Typical Usage | Internal forests | External organizations |

---

# Trust Types Overview

Active Directory supports multiple trust types.

| Trust Type | Typical Use |
|-------------|-------------|
| Parent-Child Trust | Domains within the same tree |
| Tree-Root Trust | Between domain trees in the same forest |
| Forest Trust | Between separate forests |
| External Trust | Between separate domains |
| Shortcut Trust | Reduce authentication path length |
| Realm Trust | Integrate with Kerberos realms (such as MIT Kerberos) |

---

# Parent-Child Trust

Whenever a child domain is created:

```text
company.com

↓

sales.company.com
```

Active Directory automatically creates:

```text
company.com

<────────────>

sales.company.com
```

Characteristics:

- Automatic
- Two-way
- Transitive

---

# Parent-Child Trust Example

```text
company.com

│

├── hr.company.com

├── sales.company.com

└── finance.company.com
```

Each child has an automatic trust with its parent.

---

# Tree-Root Trust

Suppose one forest contains multiple domain trees.

```text
Forest

│

├── company.com

└── enterprise.net
```

Active Directory automatically creates a trust between the tree roots.

Characteristics:

- Automatic
- Two-way
- Transitive

---

# Forest Trust

A **Forest Trust** connects two separate Active Directory forests.

Example:

```text
Forest A

<────────────>

Forest B
```

Forest trusts are commonly used after:

- Mergers
- Acquisitions
- Enterprise collaboration

---

# Forest Trust Characteristics

Typical properties:

- Between forests
- Can be one-way or two-way
- Transitive between participating forests
- Requires Forest Functional Level support

---

# Forest Trust Example

```text
Contoso Forest

<────────────>

Fabrikam Forest
```

Users can authenticate across forests if:

- Trust exists.
- Permissions are granted.

---

# External Trust

An **External Trust** connects domains that are **not** joined through a forest trust.

Example:

```text
Company Domain

↓

External Trust

↓

Legacy Domain
```

Characteristics:

- Usually non-transitive
- Often used for legacy migrations
- Supports interoperability during transition projects

---

# External Trust Scenario

```text
Modern AD Domain

↓

Needs Access

↓

Legacy Windows Domain
```

An external trust allows authentication without joining both environments into one forest.

---

# Shortcut Trust

A **Shortcut Trust** improves authentication performance in large forests.

Instead of following a long authentication path:

```text
Domain A

↓

Domain B

↓

Domain C

↓

Domain D
```

A shortcut creates:

```text
Domain A

────────────>

Domain D
```

---

# Benefits of Shortcut Trusts

Advantages:

- Faster authentication
- Reduced authentication hops
- Lower domain controller workload
- Better performance in large forests

---

# Realm Trust

A **Realm Trust** connects Active Directory with a non-Windows Kerberos realm.

Example:

```text
Active Directory

↓

Realm Trust

↓

MIT Kerberos Realm
```

This enables cross-platform authentication in heterogeneous environments.

---

# Summary of Trust Types

| Trust | Automatic | Transitive | Typical Scenario |
|--------|-----------|------------|------------------|
| Parent-Child | Yes | Yes | Child domains |
| Tree-Root | Yes | Yes | Multiple trees in one forest |
| Forest | No | Yes (between forests) | Separate forests |
| External | No | Usually No | Legacy or external domains |
| Shortcut | No | Yes | Optimize authentication |
| Realm | No | Configurable | AD ↔ Kerberos integration |

---

# Enterprise Design Example

```text
Forest

│

├── company.com

│      │

│      ├── HR

│      ├── Finance

│      └── IT

│

└── partnerforest.com

        │

        ├── Sales

        └── Support
```

Configuration:

- Automatic Parent-Child Trusts
- Automatic Tree-Root Trusts (if multiple trees exist)
- Forest Trust between the two forests
- Shortcut Trusts where authentication latency becomes significant

---

# Cybersecurity Perspective

Trusts increase authentication reach across environments.

Security recommendations:

- Use one-way trusts where appropriate.
- Avoid unnecessary two-way trusts.
- Regularly review forest and external trusts.
- Remove obsolete partner trusts.
- Audit cross-domain authentication.
- Document trust purpose and ownership.

Excessive or poorly planned trusts can increase the impact of credential compromise.

---

# Common Mistakes

Avoid:

- Confusing trust direction with permission inheritance.
- Assuming all trusts are transitive.
- Creating shortcut trusts unnecessarily.
- Leaving external trusts after migration is complete.
- Using broad two-way trusts when one-way access is sufficient.

---

# Hands-on Lab

## Objective

Identify trust types in your environment.

### Tasks

1. Open:

```text
Active Directory Domains and Trusts
```

2. Inspect every trust.

3. Record:

- Trust name
- Trust type
- Trust direction
- Transitive or non-transitive
- One-way or two-way

4. Draw the trust relationships as a diagram.

---

# Interview Questions

1. What is the difference between a one-way and two-way trust?
2. What is a transitive trust?
3. What is a non-transitive trust?
4. What is a Forest Trust?
5. When would you use an External Trust?
6. What problem does a Shortcut Trust solve?
7. What is a Realm Trust?
8. Which trust types are created automatically?
9. Are Parent-Child Trusts transitive?
10. Why should unnecessary trusts be removed?

---

# Key Takeaways

- Trust direction determines which domain accepts authentication from another.
- One-way trusts provide restricted authentication, while two-way trusts support mutual authentication.
- Transitive trusts automatically extend authentication through trust chains; non-transitive trusts do not.
- Active Directory supports Parent-Child, Tree-Root, Forest, External, Shortcut, and Realm trusts for different scenarios.
- Selecting the appropriate trust type is essential for security, scalability, and efficient enterprise identity management.

---

**Next:** Part 3