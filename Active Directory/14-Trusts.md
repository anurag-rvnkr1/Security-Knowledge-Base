# 14-Trusts.md

# Part 1 — Active Directory Trust Fundamentals, Types of Trusts and Enterprise Authentication

---

# Learning Objectives

After completing this chapter, you will understand:

- What Active Directory Trusts are
- Why Trusts are needed
- Authentication across Domains
- Authentication across Forests
- Trust Relationships
- Trust Direction
- Trust Transitivity
- Types of Trusts
- Trust Architecture
- Enterprise Use Cases

---

# Introduction

Modern enterprises rarely operate with a single Active Directory domain.

Large organizations may have:

- Multiple Domains
- Multiple Forests
- Multiple Geographic Regions
- Subsidiary Companies
- Partner Organizations
- Acquired Businesses

Example:

```
Global Corporation

├── India
├── USA
├── Germany
├── Japan
└── Australia
```

Every location may have its own Active Directory domain.

The challenge becomes:

> **How can users in one domain securely access resources in another?**

The answer is:

**Active Directory Trusts**

---

# What is a Trust?

A **Trust** is a secure relationship between two Active Directory domains or forests that allows authentication requests to be accepted across security boundaries.

Simply put,

A trust tells another domain:

```
I trust your authentication.

If you verify a user,
I will accept that identity
according to my authorization rules.
```

---

# Simple Analogy

Imagine two office buildings.

```
Building A

Employee ID

↓

Building B

Security Guard

↓

Trust Exists?

↓

Yes

↓

Allow Entry
```

Without a trust:

```
Employee ID

↓

Unknown

↓

Access Denied
```

The employee's identity is recognized only because the buildings trust each other's identity verification process.

---

# Why Trusts are Required

Without trusts:

```
Domain A

Users

×

Domain B

Resources
```

Users cannot authenticate across domains.

With trusts:

```
Domain A

↓

Trust

↓

Domain B

↓

Access Resources
```

The trust enables authentication, while authorization still determines what the user can access.

---

# Authentication vs Authorization

Trusts provide authentication.

Permissions provide authorization.

Example:

```
User

↓

Authenticated

↓

File Server

↓

Check NTFS Permissions

↓

Access Granted or Denied
```

A trust does **not** automatically grant permissions.

---

# Enterprise Example

Company:

```
Contoso
```

Domains:

```
india.contoso.com

us.contoso.com

europe.contoso.com
```

An employee from:

```
india.contoso.com
```

needs access to:

```
File Server

↓

us.contoso.com
```

Instead of creating another account,

the trust allows the employee's existing identity to be used.

---

# Trust Relationship

A trust relationship looks like this:

```
Domain A

⇄

Domain B
```

The domains recognize each other's authentication process according to the configured trust direction.

---

# Trust Terminology

Common terms include:

| Term | Meaning |
|------|----------|
| Trusting Domain | Accepts authentication from another domain |
| Trusted Domain | The domain whose users are trusted |
| Trust Direction | Which domain accepts authentication |
| Transitive Trust | Trust extends through additional trusted domains |
| Non-Transitive Trust | Trust applies only to the directly connected domains |

---

# Understanding Trust Direction

Trusts have a direction.

Example:

```
Domain A

────────►

Domain B
```

Meaning:

```
Domain B

Trusts

Domain A
```

Users from Domain A can potentially access resources in Domain B, subject to permissions.

---

# One-Way Trust

```
Domain A

────────►

Domain B
```

Characteristics:

- Authentication flows one way.
- Users in Domain A may access resources in Domain B (if authorized).
- The reverse is not automatically true.

---

# Example

```
Head Office

────────►

Research Domain
```

Researchers can access selected Head Office resources only if the trust and permissions are configured accordingly.

---

# Two-Way Trust

```
Domain A

◄────────►

Domain B
```

Both domains trust each other.

Users from either domain can authenticate across the trust, provided authorization allows access.

---

# One-Way vs Two-Way

| Feature | One-Way | Two-Way |
|----------|----------|----------|
| Authentication Direction | One Direction | Both Directions |
| Administration | Simpler | More Flexible |
| Typical Use | Limited access | Internal enterprise collaboration |

---

# What is Transitivity?

A transitive trust extends trust relationships automatically.

Example:

```
Domain A

↓

Trust

↓

Domain B

↓

Trust

↓

Domain C
```

With transitive trusts,

Domain A can authenticate with Domain C through Domain B.

---

# Transitive Trust

```
Domain A

⇄

Domain B

⇄

Domain C
```

Authentication can flow across the trust chain.

This simplifies administration in large Active Directory environments.

---

# Non-Transitive Trust

A non-transitive trust does **not** extend beyond the directly connected domains.

```
Domain A

⇄

Domain B

×

Domain C
```

Domain A has no automatic trust with Domain C.

A separate trust would be required.

---

# Trust Visualization

### Transitive

```
A

↓

B

↓

C

↓

D

✓ Trust Extends
```

---

### Non-Transitive

```
A

↓

B

×

C

×

D

✗ No Automatic Trust
```

---

# Default Trusts in Active Directory

Within a single forest:

```
Root Domain

↓

Child Domain

↓

Grandchild Domain
```

Windows automatically creates transitive trust relationships between parent and child domains.

Administrators typically do not need to create these manually.

---

# Enterprise Example

```
corp.example.com

│

├── india.corp.example.com

├── us.corp.example.com

└── europe.corp.example.com
```

When a new child domain is added,

Active Directory automatically establishes the appropriate parent-child trust.

---

# Authentication Across Domains

Example:

```
User

↓

india.corp.example.com

↓

Trust

↓

us.corp.example.com

↓

SQL Server
```

Authentication is validated using the trust relationship.

The SQL Server then checks the user's permissions before granting access.

---

# Enterprise Authentication Flow

```
User

↓

Local Domain Controller

↓

Trust Path

↓

Remote Domain Controller

↓

Identity Verified

↓

Resource Server

↓

Authorization Check

↓

Access Granted
```

---

# Benefits of Trusts

- Single identity across multiple domains
- Reduced account duplication
- Simplified administration
- Improved collaboration
- Centralized identity management
- Better user experience
- Scalable enterprise authentication

---

# Cybersecurity Perspective

Trusts expand authentication boundaries.

Poorly planned trust relationships can:

- Increase the attack surface.
- Allow unintended authentication paths.
- Complicate security monitoring.
- Increase administrative complexity.

Security teams should:

- Create only necessary trusts.
- Regularly review trust relationships.
- Remove obsolete trusts.
- Monitor cross-domain authentication.
- Apply least-privilege permissions across trusted domains.

Remember:

> A trust enables authentication—not unrestricted access.

---

# Hands-on Lab

## Objective

Explore trust relationships in Active Directory.

### Step 1

Open:

```
Active Directory Domains and Trusts
```

---

### Step 2

Select your domain.

Open:

```
Properties

↓

Trusts
```

Observe existing trust relationships.

---

### Step 3

Identify:

- Parent domains
- Child domains
- Forest root domain

---

### Step 4

Record:

- Trust direction
- Trust type
- Transitivity

---

### Step 5

Draw the trust topology for your environment.

---

# Interview Questions

### Q1: What is an Active Directory Trust?

**Answer:** A secure relationship between domains or forests that allows authentication across security boundaries.

---

### Q2: Does a trust automatically grant resource access?

**Answer:** No. A trust enables authentication, while permissions determine authorization.

---

### Q3: What is the difference between a one-way and two-way trust?

**Answer:** A one-way trust allows authentication in a single direction, whereas a two-way trust allows authentication in both directions.

---

### Q4: What is a transitive trust?

**Answer:** A trust that automatically extends through other trusted domains.

---

### Q5: What is a non-transitive trust?

**Answer:** A trust that applies only to the directly connected domains and does not extend further.

---

### Q6: Are parent-child trusts created automatically?

**Answer:** Yes. Active Directory automatically creates transitive parent-child trusts within the same forest.

---

# Best Practices

- Create trusts only when there is a valid business requirement.
- Prefer transitive trusts within a forest.
- Periodically review trust relationships.
- Document trust direction and purpose.
- Monitor authentication across trust boundaries.
- Apply least-privilege access to trusted users.

---

# Common Mistakes

- Assuming a trust grants permissions.
- Creating unnecessary trust relationships.
- Forgetting to document trust configurations.
- Ignoring the security impact of cross-domain authentication.
- Leaving obsolete trusts in place after organizational changes.

---

# Key Takeaways

- Trusts enable authentication between Active Directory domains and forests.
- Authentication and authorization are separate processes.
- Trusts can be one-way or two-way.
- Trusts can be transitive or non-transitive.
- Parent-child trusts are automatically created within a forest.
- Proper trust design improves scalability while maintaining security.

---

# 14-Trusts.md

# Part 2 — Types of Active Directory Trusts, Trust Paths and Cross-Forest Authentication

---

# Learning Objectives

After completing this part, you will understand:

- Parent-Child Trust
- Tree-Root Trust
- Shortcut Trust
- External Trust
- Forest Trust
- Realm Trust
- Trust Paths
- Cross-Domain Authentication
- Cross-Forest Authentication
- Enterprise Trust Design

---

# Introduction

In Part 1, we learned:

- What Trusts are
- Trust Direction
- Trust Transitivity
- Authentication across Domains

Now we will study the different **types of Active Directory Trusts** used in enterprise environments and understand when each should be implemented.

---

# Types of Active Directory Trusts

Active Directory supports several trust types.

| Trust Type | Typical Purpose |
|------------|-----------------|
| Parent-Child Trust | Connect parent and child domains |
| Tree-Root Trust | Connect separate domain trees within the same forest |
| Shortcut Trust | Reduce authentication path length |
| External Trust | Connect to a specific external domain |
| Forest Trust | Connect two separate forests |
| Realm Trust | Connect Active Directory with a Kerberos realm |

Each trust type solves a different business requirement.

---

# Parent-Child Trust

A Parent-Child Trust is automatically created when a new child domain is added.

Example:

```
corp.example.com

        │

        ▼

india.corp.example.com
```

Windows automatically establishes:

```
corp.example.com

⇄

india.corp.example.com
```

Characteristics:

- Automatically created
- Two-way by default
- Transitive
- No manual configuration required

---

# Parent-Child Authentication

```
User

↓

india.corp.example.com

↓

Trust

↓

corp.example.com

↓

File Server
```

The user authenticates using the existing trust relationship.

---

# Tree-Root Trust

A forest may contain multiple domain trees.

Example:

```
Forest

│

├── corp.example.com

└── fabrikam.net
```

Although the DNS namespaces differ,

both belong to the same forest.

A Tree-Root Trust is automatically created between the root domains.

---

# Tree-Root Characteristics

- Automatic
- Two-way
- Transitive
- Connects multiple trees within one forest

---

# Example

```
Forest

│

├── corp.example.com

│

└── research.local
```

Users can authenticate across both trees using the trust relationship.

---

# Shortcut Trust

Large enterprises may contain many domains.

Authentication may otherwise travel through several intermediate domains.

Example:

Without shortcut:

```
Domain A

↓

Domain B

↓

Domain C

↓

Domain D
```

Authentication must traverse each trust.

---

# Shortcut Trust Solution

Instead of:

```
A

↓

B

↓

C

↓

D
```

Create:

```
A

────────────►

D
```

Authentication becomes shorter and more efficient.

---

# Benefits of Shortcut Trusts

- Faster authentication
- Reduced authentication traffic
- Improved logon performance
- Better scalability in large forests

---

# Enterprise Example

Company:

```
GlobalCorp
```

Domains:

```
HQ

↓

Europe

↓

Germany

↓

Berlin
```

Employees in Berlin frequently access resources in HQ.

Instead of traversing multiple domains,

a shortcut trust connects:

```
Berlin

⇄

HQ
```

This reduces authentication latency.

---

# External Trust

An External Trust connects Active Directory to a domain **outside the current forest**.

Example:

```
Forest A

↓

External Trust

↓

Legacy Domain
```

Characteristics:

- Usually non-transitive
- Manual configuration
- Connects individual domains
- Often used during migrations or coexistence

---

# Example Scenario

A company acquires another organization that has its own independent Active Directory domain.

Instead of merging immediately,

an External Trust enables controlled authentication between the two domains.

---

# Forest Trust

A Forest Trust connects two separate Active Directory forests.

Example:

```
Forest A

⇄

Forest B
```

Each forest maintains:

- Its own schema
- Its own configuration
- Its own administrators
- Its own Domain Controllers

Forest Trusts allow authentication between them.

---

# Forest Trust Example

```
Contoso Forest

⇄

Fabrikam Forest
```

Employees can authenticate across forests if permissions allow.

---

# Forest Trust Characteristics

- Connects forests
- Typically transitive between the two forests
- Supports enterprise collaboration
- Frequently used after mergers or long-term partnerships

---

# Realm Trust

A Realm Trust connects Active Directory with a non-Windows Kerberos realm.

Example:

```
Active Directory

⇄

MIT Kerberos Realm
```

Common scenarios include:

- UNIX/Linux environments
- Academic institutions
- Research organizations
- Mixed operating system environments

---

# Trust Type Comparison

| Trust Type | Automatic | Transitive | Typical Use |
|-------------|-----------|------------|-------------|
| Parent-Child | Yes | Yes | Child domains |
| Tree-Root | Yes | Yes | Multiple trees |
| Shortcut | No | Yes | Faster authentication |
| External | No | No | Specific external domain |
| Forest | No | Yes | Separate forests |
| Realm | No | Depends on configuration | Kerberos interoperability |

---

# Authentication Path

Without a shortcut:

```
User

↓

Domain A

↓

Domain B

↓

Domain C

↓

Resource
```

Authentication crosses every trust.

---

# Optimized Authentication

With a shortcut trust:

```
User

↓

Domain A

────────────►

Domain C

↓

Resource
```

The authentication path is significantly shorter.

---

# Trust Path

The **Trust Path** is the sequence of trust relationships followed during authentication.

Example:

```
Domain A

↓

Domain B

↓

Domain C

↓

Domain D
```

Authentication travels through the trust path until the target domain is reached.

---

# Enterprise Authentication Example

Company:

```
Global Manufacturing
```

Infrastructure:

```
Forest

│

├── Americas

├── Europe

├── Asia

└── Australia
```

Employee:

```
Asia Domain
```

Needs access to:

```
Europe SQL Server
```

Authentication Flow:

```
User

↓

Asia Domain Controller

↓

Trust Path

↓

Europe Domain Controller

↓

Identity Verified

↓

SQL Server

↓

Authorization Check

↓

Access Granted
```

---

# Enterprise Design Considerations

When designing trust relationships:

Consider:

- Business requirements
- Administrative boundaries
- Authentication traffic
- Geographic locations
- Security requirements
- Organizational growth
- Disaster recovery planning

Avoid creating unnecessary trust relationships simply for convenience.

---

# Cybersecurity Perspective

Trusts increase connectivity between security boundaries.

Potential risks include:

- Unauthorized lateral movement if permissions are poorly managed.
- Increased complexity in monitoring authentication.
- Legacy trusts remaining after mergers or migrations.
- Overly broad permissions granted to trusted users.

Security recommendations:

- Periodically audit all trust relationships.
- Remove unused trusts.
- Use selective authentication where appropriate.
- Monitor cross-domain authentication events.
- Limit administrative privileges across trust boundaries.

---

# Hands-on Lab

## Objective

Explore trust types in an Active Directory lab.

### Step 1

Open:

```
Active Directory Domains and Trusts
```

---

### Step 2

Review existing trust relationships.

Identify whether each trust is:

- Parent-Child
- Tree-Root
- External
- Forest
- Shortcut

---

### Step 3

Draw the trust topology.

Example:

```
Forest

│

├── Domain A

├── Domain B

└── Domain C
```

---

### Step 4

Identify:

- Trust direction
- Trust type
- Transitivity
- Authentication path

---

### Step 5

Discuss where a Shortcut Trust could improve authentication efficiency.

---

# Interview Questions

### Q1: What is a Parent-Child Trust?

**Answer:** An automatically created, two-way, transitive trust between a parent domain and a newly created child domain.

---

### Q2: What is the purpose of a Shortcut Trust?

**Answer:** To shorten authentication paths and improve performance in large Active Directory forests.

---

### Q3: What is an External Trust?

**Answer:** A manually created, typically non-transitive trust between a domain in one forest and a domain outside that forest.

---

### Q4: What is a Forest Trust?

**Answer:** A trust relationship that allows authentication between two separate Active Directory forests.

---

### Q5: When would you use a Realm Trust?

**Answer:** To integrate Active Directory with a non-Windows Kerberos realm, such as an MIT Kerberos environment.

---

### Q6: What is a Trust Path?

**Answer:** The sequence of trust relationships that authentication follows to reach the target domain.

---

# Best Practices

- Use automatic trusts where appropriate.
- Deploy Shortcut Trusts only when authentication paths become unnecessarily long.
- Prefer Forest Trusts for long-term collaboration between organizations.
- Remove temporary External Trusts after migration projects are complete.
- Regularly review and document all trust relationships.
- Monitor authentication across trust boundaries.

---

# Common Mistakes

- Creating unnecessary trust relationships.
- Forgetting to remove obsolete trusts.
- Assuming all trusts are transitive.
- Using External Trusts when a Forest Trust better fits the business requirement.
- Ignoring authentication path optimization in large forests.

---

# Key Takeaways

- Active Directory supports multiple trust types for different enterprise scenarios.
- Parent-Child and Tree-Root Trusts are automatically created within a forest.
- Shortcut Trusts improve authentication efficiency.
- External Trusts connect individual domains outside the forest.
- Forest Trusts enable collaboration between separate forests.
- Proper trust design balances scalability, performance, and security.

---

**Next:** Part 3