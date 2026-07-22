# A04:2021 – Insecure Design

---

# Overview

**Insecure Design** refers to weaknesses that originate from poor security architecture, flawed business logic, or missing security controls during the design phase of an application.

Unlike coding vulnerabilities such as SQL Injection or Broken Access Control, Insecure Design is **not caused by programming mistakes**. Instead, it results from designing a system that cannot adequately defend against foreseeable threats.

In other words:

> **Secure code cannot fix an insecure design.**

If security requirements are missing during planning and architecture, no amount of input validation or patching can fully eliminate the resulting risk.

---

# Why It Matters

Every software project begins with design decisions.

Examples include:

- Authentication flow
- Authorization model
- Password reset mechanism
- API architecture
- Payment workflow
- User registration
- Session management
- Multi-factor authentication
- Business approval process

If these are designed incorrectly, attackers may abuse the application's intended functionality rather than exploiting traditional software bugs.

---

# Implementation Bug vs Design Flaw

This distinction is critical.

## Implementation Bug

Developer writes:

```python
query = "SELECT * FROM users WHERE id=" + user_input
```

The application's design is acceptable.

The developer implemented it incorrectly.

This becomes:

```
SQL Injection
```

---

## Design Flaw

Suppose a banking application allows users to transfer unlimited money without:

- Transaction limits
- Fraud detection
- Multi-factor verification
- Risk scoring
- Velocity checks

Even if every line of code is correct, the system is insecure because the design itself is flawed.

---

# Architecture Comparison

## Secure Design

```
User

↓

Authentication

↓

Authorization

↓

Business Rules

↓

Validation

↓

Logging

↓

Database
```

Multiple layers reduce risk.

---

## Insecure Design

```
User

↓

Database
```

Security controls are missing entirely.

---

# What Makes a Design Secure?

A secure design anticipates abuse before development begins.

Questions asked during design include:

- What assets require protection?
- Who can access them?
- What happens if authentication fails?
- Can users abuse legitimate functionality?
- What happens if rate limits are exceeded?
- How is sensitive data protected?
- What if an attacker controls every request?

These questions help identify threats before implementation.

---

# Root Causes

Insecure Design commonly results from:

- Missing threat modeling
- Ignoring abuse cases
- Missing business rules
- Inadequate security requirements
- Poor architecture decisions
- Overly trusting users
- Assuming users behave honestly
- Failure to design for misuse
- Lack of security review during planning

---

# Security by Design

Security should be considered from the very beginning of the Software Development Life Cycle (SDLC), not added after development is complete.

```
Requirements

↓

Architecture

↓

Design

↓

Development

↓

Testing

↓

Deployment

↓

Maintenance
```

Security activities should occur throughout every stage.

---

# Secure Development Lifecycle (Secure SDLC)

A Secure SDLC integrates security into every phase.

```
Planning

↓

Threat Modeling

↓

Secure Design

↓

Secure Coding

↓

Code Review

↓

Security Testing

↓

Deployment

↓

Continuous Monitoring
```

Security becomes a continuous process rather than a final checklist.

---

# Threat Modeling

Threat modeling is the process of identifying potential attackers, assets, attack paths, and security controls before implementation.

Rather than asking:

> "How do we fix this bug?"

Threat modeling asks:

> "How could this system be abused?"

---

## Questions Asked During Threat Modeling

- What are we building?
- What assets are valuable?
- Who might attack the system?
- How might they attack it?
- Which security controls are required?
- What are the consequences if an attack succeeds?

---

# Example

Application:

```
Online Banking
```

Assets:

- Customer accounts
- Money
- Personal information
- Transactions
- Authentication tokens

Potential attackers:

- Criminal groups
- Insider threats
- Credential stuffing attackers
- Malware operators

Threat modeling identifies protections before implementation.

---

# Trust Boundaries

A trust boundary is a point where data moves between components with different trust levels.

Example:

```
Internet

↓

Web Server

↓

Application Server

↓

Database
```

Each transition requires validation and security controls.

Never assume data remains trustworthy after crossing a trust boundary.

---

# Business Logic

Business logic defines how an application is intended to behave.

Examples:

- Coupon redemption
- Shopping cart pricing
- Loan approval
- Refund requests
- Airline booking
- Reward points
- Ticket purchases

Attackers often exploit weaknesses in business logic without exploiting traditional software vulnerabilities.

---

# Example

A shopping website allows:

```
Apply Coupon
```

The designer intended:

```
One Coupon Per Order
```

However, the system never checks this rule.

Attack:

```
Coupon

↓

Coupon

↓

Coupon

↓

Coupon
```

Final price:

```
₹0
```

No coding bug exists.

The business rule was never enforced.

---

# Abuse Cases

Traditional software design focuses on expected user behavior.

Secure design also considers malicious behavior.

Example:

Normal use:

```
User

↓

Login

↓

Purchase

↓

Logout
```

Abuse case:

```
Attacker

↓

Automated Login

↓

Credential Stuffing

↓

Account Takeover
```

Both workflows should be considered during design.

---

# Key Principles of Secure Design

Security architects should apply principles such as:

- Least Privilege
- Defense in Depth
- Fail Securely
- Separation of Duties
- Secure Defaults
- Complete Mediation
- Economy of Mechanism
- Minimize Attack Surface
- Zero Trust
- Compartmentalization

These principles influence architecture before any code is written.

---

# Why Traditional Security Testing Isn't Enough

Static analysis can detect:

- SQL Injection
- XSS
- Hardcoded credentials

However, it usually cannot determine whether:

- Money transfers should require approval
- Password resets should expire
- Purchases should have quantity limits
- Refunds should require ownership verification

These are design decisions.

---

# Real-World Examples

Examples of insecure design include:

- Unlimited password reset attempts
- Unlimited login attempts
- Missing rate limiting
- Unlimited coupon usage
- No approval workflow for high-value transfers
- No fraud detection
- Missing transaction confirmation
- Predictable account recovery process
- Weak onboarding process
- Missing separation between customer and administrator functions

---

# Key Takeaways

- Insecure Design focuses on architectural and business logic weaknesses rather than coding bugs.
- Secure code cannot compensate for missing security requirements or flawed system design.
- Threat modeling, abuse case analysis, and Secure SDLC are essential for preventing design flaws.
- Every system should be designed with the assumption that attackers will intentionally misuse legitimate functionality.
- Security is most effective when integrated into architecture from the beginning rather than added after development.