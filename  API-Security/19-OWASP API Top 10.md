# 19 - OWASP API Security Top 10

# Introduction

The **OWASP API Security Top 10** is the industry's most widely recognized awareness document for identifying and mitigating the most critical security risks affecting modern APIs.

Unlike the traditional **OWASP Top 10** for web applications, the API Security Top 10 focuses specifically on vulnerabilities that arise from API architectures, business logic, authentication models, object relationships, and machine-to-machine communication.

Organizations use it to:

- Secure API design
- Threat modeling
- Security testing
- Secure coding
- Penetration testing
- Compliance assessments
- Developer training
- Detection engineering

The current version is **OWASP API Security Top 10 (2023)**.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand every OWASP API Security Top 10 risk.
- Learn real-world attack scenarios.
- Identify vulnerable API designs.
- Understand enterprise mitigation strategies.
- Build security detections.
- Integrate API security with SOC operations.
- Apply secure API development practices.

---

# Why OWASP API Security Top 10 Matters

```
                 API

                  │

     ┌────────────┼────────────┐

     ▼            ▼            ▼

 Design      Development    Operations

     │            │            │

     └────────────┼────────────┘

                  ▼

      OWASP API Security Top 10
```

The framework provides practical guidance throughout the software development lifecycle.

---

# OWASP API Security Top 10 (2023)

| ID | Risk |
|----|------|
| API1 | Broken Object Level Authorization (BOLA) |
| API2 | Broken Authentication |
| API3 | Broken Object Property Level Authorization (BOPLA) |
| API4 | Unrestricted Resource Consumption |
| API5 | Broken Function Level Authorization (BFLA) |
| API6 | Unrestricted Access to Sensitive Business Flows |
| API7 | Server Side Request Forgery (SSRF) |
| API8 | Security Misconfiguration |
| API9 | Improper Inventory Management |
| API10 | Unsafe Consumption of APIs |

---

# API1 – Broken Object Level Authorization (BOLA)

## Overview

BOLA occurs when an API allows users to access objects they do not own because object ownership is not properly validated.

It is one of the most common and impactful API vulnerabilities.

---

# BOLA Attack Example

```
User A

GET /api/orders/1001

        │

Changes ID

        ▼

GET /api/orders/1002

        │

Server Returns

Another User's Order
```

Changing a resource identifier should never grant access to another user's data.

---

# Why BOLA Happens

Common causes include:

- Missing ownership validation
- Predictable object identifiers
- Trusting client-supplied IDs
- Missing authorization checks
- Inconsistent authorization logic

---

# BOLA Workflow

```
Authenticated User

        │

Requests Object

        │

Authorization Check?

   ┌────┴─────┐

   ▼          ▼

Yes         No

   ▼          ▼

Allowed   Data Exposure
```

---

# BOLA Mitigations

- Verify object ownership on every request.
- Enforce authorization in backend services.
- Avoid relying solely on API Gateway decisions.
- Implement least privilege.
- Use centralized authorization frameworks.
- Log authorization failures.

---

# Enterprise Example

```
Employee

        │

HR API

        │

Employee ID Modified

        │

Payroll Data

        ▼

Unauthorized Disclosure
```

---

# API2 – Broken Authentication

## Overview

Broken Authentication allows attackers to compromise user identities.

Examples

- Weak passwords
- Credential stuffing
- Session hijacking
- Token theft
- Token replay
- Weak MFA
- Long-lived tokens

---

# Authentication Attack

```
Attacker

      │

Credential Stuffing

      │

Login API

      │

Successful Login

      ▼

Account Compromise
```

---

# Authentication Mitigations

- MFA
- Strong password policy
- Rate limiting
- Device reputation
- Secure token lifecycle
- Short-lived access tokens
- Refresh token rotation
- Login monitoring

---

# API3 – Broken Object Property Level Authorization (BOPLA)

## Overview

BOPLA occurs when users can read or modify object properties that should not be accessible.

This combines risks historically associated with excessive data exposure and mass assignment.

---

# Example

Expected response

```
{
  "id": 100,
  "name": "Alice"
}
```

Actual response

```
{
  "id":100,
  "name":"Alice",
  "salary":950000,
  "internalNotes":"..."
}
```

Sensitive properties should not be exposed unless explicitly authorized.

---

# Property Modification

```
PATCH

/users/100

↓

"isAdmin": true
```

Applications should ignore or reject unauthorized properties.

---

# BOPLA Mitigations

- Response filtering
- DTOs
- Field-level authorization
- Property allowlists
- Mass assignment protection
- Least privilege

---

# API4 – Unrestricted Resource Consumption

## Overview

Attackers consume excessive resources until the application becomes unavailable or incurs excessive operational costs.

Examples

- CPU exhaustion
- Memory exhaustion
- Storage exhaustion
- Database overload
- Cloud cost amplification

---

# Resource Consumption Attack

```
Attacker

     │

Millions of Requests

     │

Expensive Search

     │

Database

     ▼

Service Degradation
```

---

# Resource Consumption Controls

- Rate limiting
- Quotas
- Pagination
- Payload size limits
- Query complexity limits
- Timeouts
- Resource quotas
- Autoscaling with safeguards

---

# API5 – Broken Function Level Authorization (BFLA)

## Overview

BFLA occurs when users access functions outside their authorized role.

---

# Example

```
Employee

↓

POST

/admin/deleteUser

↓

Function Executed
```

Authentication alone is insufficient.

Authorization must validate the user's permissions for every function.

---

# Function Authorization Workflow

```
Authenticated User

        │

Administrative API

        │

Role Check

   ┌────┴────┐

   ▼         ▼

Admin     Employee

   ▼         ▼

Allow    Reject
```

---

# BFLA Mitigations

- RBAC
- ABAC
- Central authorization
- Least privilege
- Deny-by-default
- Continuous authorization testing

---

# API6 – Unrestricted Access to Sensitive Business Flows

## Overview

Some APIs expose business processes that can be abused through automation.

Examples include

- Ticket purchasing
- Inventory reservation
- Reward redemption
- Coupon usage
- Account creation
- Password reset

---

# Business Flow Abuse

```
Bot

 │

Rapid Requests

 │

Purchase API

 │

Inventory Reserved

 ▼

Customers Blocked
```

The API behaves as designed, but the business outcome is undesirable.

---

# Business Flow Controls

- Rate limiting
- CAPTCHA where appropriate
- User verification
- Behavioral analytics
- Device fingerprinting
- Business rule validation
- Risk scoring

---

# API7 – Server Side Request Forgery (SSRF)

## Overview

SSRF occurs when an application fetches attacker-controlled URLs without proper validation.

```
Attacker

      │

URL

      ▼

Application Server

      │

Internal Network

      ▼

Cloud Metadata
```

SSRF may expose internal systems or cloud instance metadata.

---

# SSRF Mitigations

- Allowlist destinations
- Disable unnecessary outbound access
- Validate URLs
- Restrict protocols
- Network segmentation
- Metadata service protections
- Outbound proxy controls

---

# API8 – Security Misconfiguration

## Overview

Security misconfiguration includes insecure defaults and operational mistakes.

Examples

- Default credentials
- Debug mode
- Directory listing
- Excessive CORS
- Verbose errors
- Unnecessary services
- Weak TLS configuration

---

# Misconfiguration Example

```
Production

↓

Debug Enabled

↓

Stack Trace

↓

Information Disclosure
```

---

# Misconfiguration Controls

- Secure defaults
- Infrastructure as Code
- Configuration reviews
- Security baselines
- Automated compliance scanning
- Secrets management

---

# API9 – Improper Inventory Management

## Overview

Organizations frequently lose visibility into deployed APIs.

Examples

- Forgotten APIs
- Deprecated versions
- Shadow APIs
- Test environments
- Zombie endpoints

---

# API Inventory

```
Known APIs

──────────────

Unknown APIs

──────────────

Deprecated APIs

──────────────

Shadow APIs
```

Unmanaged APIs often become attractive attack targets.

---

# Inventory Controls

- API catalog
- Asset discovery
- Version management
- API lifecycle governance
- Continuous scanning
- Documentation maintenance

---

# API10 – Unsafe Consumption of APIs

## Overview

Applications often trust responses from third-party APIs without sufficient validation.

```
Application

      │

Third-Party API

      │

Unexpected Response

      ▼

Application Failure
```

External APIs should always be treated as untrusted inputs.

---

# Unsafe Consumption Controls

- Validate third-party responses
- Verify schemas
- Authenticate upstream services
- Enforce TLS
- Implement timeouts
- Retry safely
- Fail securely
- Monitor dependencies

---

# Risk Mapping

| OWASP Risk | Primary Security Control |
|-------------|--------------------------|
| API1 | Object Authorization |
| API2 | Strong Authentication |
| API3 | Property Authorization |
| API4 | Resource Limits |
| API5 | Function Authorization |
| API6 | Business Logic Protection |
| API7 | SSRF Defenses |
| API8 | Secure Configuration |
| API9 | API Inventory |
| API10 | Secure Third-Party Integration |

---

# Enterprise Defense-in-Depth

```
                    Internet

                        │

                        ▼

              DDoS Protection

                        │

                        ▼

          Web Application Firewall

                        │

                        ▼

                 API Gateway

        ┌────────┼────────┬─────────┐

        ▼        ▼        ▼         ▼

 Authentication Authorization Rate Limit Logging

                        │

                        ▼

              Validation Layer

                        │

                        ▼

              Business Logic

                        │

                        ▼

                 Backend APIs

                        │

                        ▼

                  Databases

                        │

                        ▼

                   SIEM / SOC
```

---

# OWASP API Top 10 and SDLC

```
Requirements

      │

Design

      │

Development

      │

Testing

      │

Deployment

      │

Operations

      ▼

Continuous Improvement
```

Each OWASP API risk should be addressed throughout the software development lifecycle rather than only during penetration testing.

---

# Key Takeaways

- The OWASP API Security Top 10 identifies the most significant API security risks.
- Authorization failures remain among the highest-impact vulnerabilities.
- Business logic abuse is increasingly targeted by attackers.
- Secure design, testing, monitoring, and governance all contribute to reducing API risk.
- Defense-in-depth is essential for enterprise API security.

---

**Next:** Real-world attack scenarios, detection engineering, SIEM integration, enterprise case studies, hands-on labs, troubleshooting, interview questions, and chapter summary.