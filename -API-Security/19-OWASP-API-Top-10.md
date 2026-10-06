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

# Real-World Attack Scenarios

The OWASP API Security Top 10 is based on vulnerabilities repeatedly observed in production environments.

Understanding how these vulnerabilities are exploited helps security teams design effective preventive and detective controls.

---

# Attack Chain Example

```
Reconnaissance

      │

API Discovery

      │

Authentication Attack

      │

Authorization Bypass

      │

Sensitive Data Access

      │

Privilege Escalation

      │

Persistence

      ▼

Data Exfiltration
```

Multiple API vulnerabilities are often chained together during a real attack.

---

# Scenario 1 – BOLA Attack

Target

```
Customer Portal API
```

Attack

```
GET

/api/orders/1001

↓

Change Object ID

↓

/api/orders/1002

↓

Receive Another User's Data
```

Root Cause

- Missing ownership validation

Impact

- Customer data exposure
- Privacy violations
- Regulatory consequences

Mitigation

- Object-level authorization
- Ownership verification
- Centralized authorization middleware

---

# Scenario 2 – Broken Authentication

Target

```
Login API
```

Attack

```
Credential Stuffing

        │

Thousands of Accounts

        │

Weak Passwords

        ▼

Successful Login
```

Root Cause

- Weak authentication controls

Impact

- Account takeover
- Fraud
- Data theft

Mitigation

- MFA
- Rate limiting
- Password monitoring
- Device reputation
- Risk-based authentication

---

# Scenario 3 – BOPLA

Target

```
Profile API
```

Attack

```
PATCH

/profile

↓

"isAdmin": true

↓

Privilege Escalation
```

Root Cause

- Mass assignment
- Missing property authorization

Mitigation

- DTOs
- Property allowlists
- Field-level authorization

---

# Scenario 4 – Resource Exhaustion

Target

```
Search API
```

Attack

```
Large Queries

↓

Complex Database Search

↓

High CPU

↓

Service Slowdown
```

Root Cause

- No resource limits
- Expensive queries

Mitigation

- Pagination
- Query limits
- Timeouts
- Rate limiting
- Query complexity analysis

---

# Scenario 5 – Function Authorization

Target

```
Admin API
```

Attack

```
Employee

↓

/admin/deleteUser

↓

Function Executes
```

Root Cause

- Missing role validation

Mitigation

- RBAC
- ABAC
- Deny-by-default
- Authorization middleware

---

# Scenario 6 – Business Logic Abuse

Target

```
Coupon API
```

Attack

```
Coupon

↓

Unlimited Redemption

↓

Financial Loss
```

Root Cause

- Missing business validation

Mitigation

- Redemption limits
- Fraud detection
- Behavioral analytics
- Risk scoring

---

# Scenario 7 – SSRF

Target

```
Image Fetch API
```

Attack

```
URL

↓

Internal Metadata

↓

Sensitive Information

↓

Attacker
```

Root Cause

- Unvalidated outbound requests

Mitigation

- URL allowlists
- Outbound proxy
- Metadata protection
- Network segmentation

---

# Scenario 8 – Security Misconfiguration

Target

```
Production API
```

Attack

```
Debug Mode

↓

Stack Trace

↓

Framework Details

↓

Attack Planning
```

Mitigation

- Secure defaults
- Configuration reviews
- Continuous compliance
- Infrastructure as Code

---

# Scenario 9 – Inventory Management

Target

```
Deprecated API

v1
```

Attack

```
Internet Scan

↓

Forgotten API

↓

Known Vulnerability

↓

Compromise
```

Mitigation

- API inventory
- Version lifecycle
- Asset discovery
- Continuous monitoring

---

# Scenario 10 – Unsafe API Consumption

Target

```
Third-Party Payment API
```

Attack

```
Unexpected Response

↓

Application Trusts Data

↓

Business Failure
```

Mitigation

- Response validation
- Schema enforcement
- Timeout handling
- Fail securely

---

# Mapping Risks to MITRE ATT&CK

| OWASP API Risk | Relevant ATT&CK Techniques (Examples) |
|----------------|----------------------------------------|
| API1 | Exploitation of exposed services, valid accounts |
| API2 | Credential access, valid accounts |
| API3 | Privilege escalation, abuse of application features |
| API4 | Resource hijacking, endpoint denial of service |
| API5 | Abuse of elevated permissions |
| API6 | Automated collection, business process abuse |
| API7 | Internal network discovery, cloud metadata access |
| API8 | Exploitation of misconfigurations |
| API9 | Active scanning, service discovery |
| API10 | Supply chain compromise, trusted relationship abuse |

The exact ATT&CK techniques vary depending on implementation and attack path.

---

# Threat Modeling

OWASP risks should be considered during threat modeling.

```
Assets

     │

Threat Actors

     │

Attack Surface

     │

OWASP Risks

     │

Security Controls

     ▼

Residual Risk
```

---

# Secure SDLC Integration

```
Requirements

      │

Threat Modeling

      │

Architecture Review

      │

Secure Coding

      │

Code Review

      │

Security Testing

      │

Deployment

      │

Continuous Monitoring
```

OWASP guidance should be incorporated into every development phase.

---

# Secure Coding Checklist

Developers should verify:

- Authentication implemented correctly.
- Authorization performed server-side.
- Object ownership validated.
- Input validation enforced.
- Sensitive data filtered.
- Security headers configured.
- Error handling is generic.
- Logging is structured.
- Secrets are protected.
- Dependencies are maintained.

---

# API Security Testing

Testing should include:

- Authentication testing
- Authorization testing
- Object enumeration
- Input validation
- Injection testing
- Rate limiting
- Business logic testing
- File upload testing
- SSRF validation
- Third-party API assessment

---

# Detection Engineering

Recommended detections for each OWASP risk.

| Risk | Detection Indicator |
|------|---------------------|
| API1 | Repeated object identifier changes |
| API2 | Credential stuffing indicators |
| API3 | Unexpected property modifications |
| API4 | Large request volumes and expensive queries |
| API5 | Administrative endpoint access failures |
| API6 | High-volume business workflow execution |
| API7 | Outbound requests to unusual destinations |
| API8 | Configuration drift or unexpected changes |
| API9 | Requests to deprecated API versions |
| API10 | Third-party API failures or schema deviations |

---

# Detection Workflow

```
API Gateway

      │

Structured Logs

      │

Normalization

      │

Correlation

      │

Detection Rules

      │

Alert

      ▼

SOC
```

---

# High-Value Detection Rules

## Rule 1 – Possible BOLA

```
User

 │

Sequential Object IDs

 │

HTTP 200

 │

Different Owners

 ▼

High Severity Alert
```

---

## Rule 2 – Broken Authentication

```
Failed Logins

       │

Successful Login

       │

Unknown Device

       ▼

Possible Account Takeover
```

---

## Rule 3 – Function Abuse

```
Normal User

      │

Admin Endpoint

      │

Authorization Failure

      ▼

Privilege Escalation Attempt
```

---

## Rule 4 – SSRF

```
API

 │

Outbound Request

 │

Internal Address

 ▼

Critical Alert
```

---

## Rule 5 – Business Logic Abuse

```
Single User

      │

Thousands of Orders

      │

Short Time

      ▼

Fraud Investigation
```

---

# SIEM Integration

Recommended log sources

- API Gateway
- Identity Provider
- Web Application Firewall
- Reverse Proxy
- Application Logs
- Database Audit Logs
- Kubernetes Audit Logs
- Cloud Audit Logs
- DNS Logs
- Network Firewall Logs

---

# Enterprise Correlation

```
Gateway Logs

      │

Authentication

      │

Authorization

      │

Application Logs

      │

Cloud Logs

      ▼

SIEM

      │

Correlation

      ▼

SOC Investigation
```

---

# SOC Monitoring Dashboard

Recommended widgets

- Authentication failures
- Authorization failures
- HTTP 4xx trends
- HTTP 5xx trends
- Top API consumers
- Rate-limit events
- SSRF detections
- Deprecated API usage
- High-risk API endpoints
- Geographic request distribution

---

# Enterprise Architecture

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

         ┌──────────┼───────────┬──────────┐

         ▼          ▼           ▼          ▼

 Authentication Authorization Validation Logging

                         │

                         ▼

                 Backend Services

                         │

      ┌──────────────────┼───────────────────┐

      ▼                  ▼                   ▼

 Database          Message Queue        Third-Party APIs

      │

      ▼

 Observability Platform

      │

      ▼

      SIEM

      │

      ▼

      SOC
```

---

# Hands-on Lab 1 – Object Authorization Assessment

**Objective**

Assess object-level authorization in an authorized environment.

**Steps**

1. Authenticate as a standard user.
2. Access an authorized object.
3. Modify the object identifier.
4. Observe authorization behavior.
5. Review application logs.

**Learning Outcomes**

- Object authorization
- Authorization testing
- Secure API assessment

---

# Hands-on Lab 2 – Business Logic Testing

**Objective**

Evaluate business rule enforcement.

**Steps**

1. Identify a business workflow.
2. Execute the workflow normally.
3. Attempt excessive or automated execution.
4. Observe system behavior.
5. Document protections and findings.

**Learning Outcomes**

- Business logic assessment
- Abuse detection
- Fraud prevention

---

# Hands-on Lab 3 – SSRF Assessment

**Objective**

Review outbound request controls in an authorized environment.

**Steps**

1. Identify functionality that retrieves external resources.
2. Review URL validation controls.
3. Verify outbound network restrictions.
4. Confirm that unauthorized destinations are blocked.

**Learning Outcomes**

- SSRF assessment methodology
- Outbound request security
- Network segmentation

---

# Troubleshooting

## Excessive Authorization Failures

Possible causes

- Broken RBAC policy
- Misconfigured roles
- Token issues
- Incorrect ownership validation

---

## High Authentication Failures

Possible causes

- Credential stuffing
- Password spraying
- User error
- MFA configuration issues

---

## Unexpected Outbound Requests

Possible causes

- SSRF attempts
- Third-party integrations
- Misconfigured webhooks
- Proxy configuration issues

---

## Deprecated API Traffic

Possible causes

- Legacy clients
- Forgotten integrations
- Automated scanners
- Inventory management gaps

---

## Resource Consumption Alerts

Possible causes

- Legitimate traffic spikes
- Expensive queries
- Automated abuse
- Denial-of-service attempts

---

# Interview Questions

## Fundamental

1. What is the OWASP API Security Top 10?
2. What is Broken Object Level Authorization (BOLA)?
3. How does BOPLA differ from BOLA?
4. What is Broken Function Level Authorization (BFLA)?
5. What is Unrestricted Resource Consumption?
6. Why is API inventory management important?
7. What is Unsafe Consumption of APIs?
8. Why is SSRF included in the OWASP API Top 10?
9. What is business logic abuse?
10. Why should OWASP guidance be integrated into the SDLC?

---

## Intermediate

11. How would you prevent BOLA in a REST API?
12. Explain the differences between API1, API3, and API5.
13. How would you detect business flow abuse?
14. How should an enterprise manage deprecated APIs?
15. How would you secure outbound requests against SSRF?
16. Which OWASP API risks are most commonly observed in production?
17. How should API security events be monitored in a SIEM?
18. What telemetry is most valuable for authorization monitoring?
19. How would you build a threat model using the OWASP API Top 10?
20. How would you prioritize remediation across multiple API risks?

---

## Scenario-Based

**Scenario 1**

An authenticated user can retrieve another customer's invoice by modifying the invoice identifier in the request URL.

- Which OWASP API risk does this represent?
- What server-side control is missing?
- How would you verify that the issue has been fully remediated?

---

**Scenario 2**

A public search endpoint experiences a sustained increase in complex queries, causing database latency to rise significantly.

- Which OWASP API risk is most relevant?
- Which gateway and application controls would you implement?
- Which metrics would you monitor after mitigation?

---

**Scenario 3**

An internal integration consumes data from a third-party API without validating the response schema. The provider unexpectedly changes a response field, resulting in application failures.

- Which OWASP API risk applies?
- What validation strategy should be introduced?
- How would you improve resilience against future changes?

---

# Chapter Summary

In this chapter, we examined the **OWASP API Security Top 10 (2023)** and explored how each risk manifests in enterprise environments.

We covered:

- API1 through API10
- Real-world attack scenarios
- Enterprise mitigations
- Secure SDLC integration
- Detection engineering
- SIEM integration
- SOC monitoring
- Hands-on labs
- Troubleshooting
- Interview preparation

The OWASP API Security Top 10 should serve as a foundational framework for designing, developing, testing, deploying, and monitoring secure APIs throughout their lifecycle.

---

# Chapter Review

You should now be able to answer:

- Why is BOLA considered one of the highest-risk API vulnerabilities?
- How do API1, API3, and API5 differ?
- What controls mitigate unrestricted resource consumption?
- Why is business logic abuse difficult to detect?
- How should enterprises manage API inventories?
- Which telemetry is essential for detecting OWASP API Top 10 attacks?
- How would you integrate the OWASP API Top 10 into an organization's SDLC and SOC operations?

If you can confidently answer these questions, you are ready to continue with **Chapter 20 – API Vulnerability Testing**, where you'll learn structured API security assessment methodologies, testing workflows, OpenAPI-based testing, authorization testing, fuzzing strategies, automation, reporting, and enterprise penetration testing practices.

---

# References

## Standards

- OWASP API Security Top 10 (2023)
- OpenAPI Specification
- RFC 9110 – HTTP Semantics

## Security Standards

- OWASP ASVS
- OWASP Web Security Testing Guide (WSTG)
- NIST SP 800-53
- NIST Secure Software Development Framework (SSDF)

## Further Reading

- MITRE ATT&CK Framework
- OWASP Cheat Sheet Series
- OWASP Application Security Verification Standard (ASVS)

---

# What's Next?

➡️ **Chapter 20 – API Vulnerability Testing**

Topics include:

- API security assessment methodology
- Testing preparation
- OpenAPI and Swagger testing
- Authentication testing
- Authorization testing
- Business logic testing
- Injection testing
- Automated testing
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions