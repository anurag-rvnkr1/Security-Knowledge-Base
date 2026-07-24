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

**Next:** **Part 2 — Trust Types, External Trusts, Forest Trusts, Realm Trusts, Shortcut Trusts, SID Filtering, and Enterprise Design**