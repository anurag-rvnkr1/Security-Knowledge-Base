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

# Secure Design Principles

Secure design principles are fundamental guidelines that help architects and developers build systems that remain secure even when individual controls fail.

Rather than relying on a single security feature, secure systems use multiple complementary controls to reduce risk.

---

# 1. Defense in Depth

## Overview

Defense in Depth means protecting a system with **multiple independent layers of security**.

If one layer fails, additional layers continue to provide protection.

---

## Insecure Architecture

```
Internet

↓

Database
```

If an attacker reaches the database, there are no additional barriers.

---

## Secure Architecture

```
Internet

↓

Firewall

↓

Web Server

↓

Web Application Firewall (WAF)

↓

Application

↓

Authentication

↓

Authorization

↓

Input Validation

↓

Logging & Monitoring

↓

Database
```

Even if one control is bypassed, others continue to reduce the attacker's progress.

---

## Real-World Example

Online banking typically uses:

- HTTPS
- Multi-Factor Authentication (MFA)
- Device recognition
- Fraud detection
- Transaction limits
- Session monitoring
- Account lockout
- Behavioral analytics

No single control is expected to stop every attack.

---

## Benefits

- Reduces single points of failure
- Improves resilience
- Limits attacker movement
- Increases detection opportunities

---

# 2. Principle of Least Privilege

## Overview

Every user, application, and service should receive **only the minimum permissions necessary** to perform its intended tasks.

---

## Example

Customer:

✔ View profile

✔ Place orders

✘ Delete users

✘ Access admin dashboard

---

Administrator:

✔ Manage users

✔ Configure system

✔ View audit logs

---

## Application Example

Instead of connecting to the database as:

```
root
```

Create a dedicated account:

```
app_user
```

with only:

- SELECT
- INSERT
- UPDATE

Avoid unnecessary permissions such as:

- DROP DATABASE
- CREATE USER
- GRANT ALL

---

## Benefits

- Reduces damage after compromise
- Limits insider abuse
- Simplifies auditing
- Reduces attack surface

---

# 3. Fail Securely

## Overview

When an error occurs, the application should default to a secure state.

---

## Insecure Example

Authentication service becomes unavailable.

Application response:

```
Authentication Failed

↓

Allow Access
```

This is catastrophic.

---

## Secure Example

Authentication service becomes unavailable.

Application response:

```
Authentication Failed

↓

Access Denied
```

The system prioritizes security over convenience.

---

## Examples

Secure failures include:

- Denying access when authorization cannot be verified.
- Rejecting malformed tokens.
- Blocking expired sessions.
- Refusing invalid cryptographic keys.

---

# 4. Secure by Default

## Overview

The default configuration should be the safest configuration.

Users should never have to enable security manually.

---

## Example

New account:

```
Password Required

MFA Optional

Email Verification Required
```

Better:

```
Password Required

Email Verification Required

Strong Password Policy Enabled

Secure Session Configuration Enabled
```

---

## Server Example

Default:

```
Directory Listing

Enabled
```

Secure Default:

```
Directory Listing

Disabled
```

---

# 5. Complete Mediation

## Overview

Every request to a protected resource should be authorized.

Never assume that a previous authorization remains valid forever.

---

## Architecture

```
User

↓

Request

↓

Authorization Check

↓

Resource
```

Every request follows this process.

---

## Common Mistake

Application checks authorization only during login.

Subsequent requests bypass authorization.

Attackers exploit this by directly accessing protected endpoints.

---

# 6. Separation of Duties

## Overview

Critical actions should require multiple independent roles or approvals.

---

## Banking Example

Employee:

```
Create Transfer
```

Manager:

```
Approve Transfer
```

Finance:

```
Release Funds
```

No single individual controls the entire process.

---

## Benefits

- Reduces fraud
- Prevents accidental mistakes
- Improves accountability
- Supports compliance requirements

---

# 7. Economy of Mechanism

## Overview

Security mechanisms should be as simple as possible while still meeting security requirements.

Complex systems are more difficult to understand, test, and maintain.

---

## Example

Instead of:

```
15 Custom Authentication Modules
```

Use:

```
One Well-Tested Authentication Framework
```

Simple, well-understood solutions are generally more secure than overly complex custom implementations.

---

# 8. Minimize Attack Surface

## Overview

Every exposed feature is a potential entry point for attackers.

Reduce unnecessary functionality.

---

## Remove

- Unused APIs
- Debug endpoints
- Test accounts
- Default credentials
- Sample applications
- Unnecessary services
- Legacy protocols

---

## Example

Instead of exposing:

```
80 APIs
```

Expose only:

```
20 Required APIs
```

---

## Benefits

- Fewer vulnerabilities
- Smaller testing scope
- Reduced maintenance effort
- Lower risk

---

# 9. Zero Trust

## Overview

Zero Trust assumes that no user, device, or network should be trusted automatically.

Every request must be continuously verified.

Core principle:

> **Never trust. Always verify.**

---

## Traditional Model

```
Internal Network

↓

Trusted
```

---

## Zero Trust Model

```
User

↓

Authenticate

↓

Authorize

↓

Evaluate Device

↓

Evaluate Context

↓

Grant Limited Access
```

---

## Continuous Verification

Checks may include:

- User identity
- Device health
- Geographic location
- Time of access
- Risk score
- Behavioral analytics

Trust is not permanent.

---

# 10. Compartmentalization

## Overview

Separate systems into isolated components so that compromise of one component does not automatically compromise the entire environment.

---

## Example

Instead of:

```
One Large Database

↓

Everything
```

Use:

```
Customer Database

Inventory Database

Payment Database

Logging Database
```

Compromise of one component has limited impact.

---

## Cloud Example

Separate:

- Production
- Development
- Testing

Use different:

- Accounts
- Networks
- Secrets
- IAM roles

---

# Comparing Secure vs Insecure Designs

| Principle | Secure Design | Insecure Design |
|------------|---------------|-----------------|
| Defense in Depth | Multiple security layers | Single control |
| Least Privilege | Minimal permissions | Excessive permissions |
| Fail Securely | Deny on failure | Allow on failure |
| Secure by Default | Security enabled | Security optional |
| Complete Mediation | Check every request | Check once |
| Separation of Duties | Multiple approvals | Single actor controls everything |
| Economy of Mechanism | Simple, well-tested controls | Complex custom security |
| Attack Surface | Only necessary features exposed | Unused features remain enabled |
| Zero Trust | Verify every request | Trust internal users automatically |
| Compartmentalization | Isolated components | Flat architecture |

---

# Applying These Principles Together

A mature application rarely depends on just one principle.

Example:

```
Internet

↓

Firewall

↓

Load Balancer

↓

Web Application Firewall

↓

Authentication

↓

Authorization

↓

Business Rules

↓

Rate Limiting

↓

Application

↓

Audit Logging

↓

Encrypted Database
```

Each layer complements the others and limits the impact of failures elsewhere.

---

# Key Takeaways

- Secure design is achieved through multiple complementary principles rather than a single security feature.
- Defense in Depth, Least Privilege, and Complete Mediation are foundational concepts in modern application security.
- Zero Trust extends verification beyond traditional network boundaries.
- Simplicity, compartmentalization, and minimizing attack surface reduce opportunities for attackers.
- Applying these principles during system design is significantly more effective than attempting to retrofit security after development.