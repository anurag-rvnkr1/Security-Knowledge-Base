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

**Next:** Part 2