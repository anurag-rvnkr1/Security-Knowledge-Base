# 66-Web-Security-Cheat-Sheet.md

# Part 1 — Web Security Quick Reference, Essential Concepts, Security Principles, HTTP, Authentication, and Secure Development

> **"A good security engineer may not memorize every detail, but they know the core principles, where to apply them, and how to use them consistently."**

---

# Learning Objectives

After completing this part, you will have a quick-reference guide for:

- Web Security Fundamentals
- CIA Triad
- Security Principles
- HTTP & HTTPS
- Authentication & Authorization
- Session Management
- Secure Development
- Common Security Terminology
- Enterprise Quick Reference

---

# Purpose of this Cheat Sheet

This chapter is designed as a rapid revision guide for:

- Interviews
- Certification preparation
- Daily development
- Security reviews
- Secure coding
- Architecture discussions
- Quick refresh before meetings

---

# Web Security at a Glance

```
Users

↓

Identity

↓

Authentication

↓

Authorization

↓

Application

↓

Database

↓

Monitoring

↓

Governance
```

---

# CIA Triad

```
CIA

│

├── Confidentiality

├── Integrity

└── Availability
```

| Principle | Goal | Example |
|-----------|------|---------|
| Confidentiality | Protect information from unauthorized access | Access controls and encryption |
| Integrity | Ensure data remains accurate and trustworthy | Validation and integrity checks |
| Availability | Ensure systems remain accessible | Redundancy and resilience |

---

# Core Security Principles

```
Security Principles

│

├── Least Privilege

├── Defense in Depth

├── Secure by Design

├── Secure by Default

├── Separation of Duties

├── Fail Securely

├── Risk-Based Decisions

└── Continuous Improvement
```

---

# Security Lifecycle

```
Requirements

↓

Design

↓

Development

↓

Testing

↓

Deployment

↓

Monitoring

↓

Improvement
```

---

# HTTP Request Flow

```
Client

↓

DNS

↓

Web Server

↓

Application

↓

Database

↓

Response
```

---

# HTTP Request Components

```
Request

│

├── Method

├── URL

├── Headers

├── Cookies

└── Body
```

---

# Common HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Submit new data |
| PUT | Replace existing data |
| PATCH | Partially update data |
| DELETE | Remove data |
| HEAD | Retrieve headers only |
| OPTIONS | Discover supported methods |

---

# Common HTTP Status Codes

## 1xx

```
Informational
```

---

## 2xx

```
Success
```

Examples:

- 200 OK
- 201 Created
- 204 No Content

---

## 3xx

```
Redirection
```

Examples:

- 301 Moved Permanently
- 302 Found
- 304 Not Modified

---

## 4xx

```
Client Errors
```

Examples:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 429 Too Many Requests

---

## 5xx

```
Server Errors
```

Examples:

- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable
- 504 Gateway Timeout

---

# HTTPS Benefits

```
HTTPS

│

├── Encryption

├── Integrity

└── Authentication
```

Benefits:

- Protects data in transit
- Reduces tampering risk
- Verifies server identity

---

# Authentication

```
User

↓

Credentials

↓

Identity Verification

↓

Authenticated Session
```

Common authentication factors:

- Something you know
- Something you have
- Something you are

---

# Authorization

```
Authenticated User

↓

Permission Check

↓

Access Decision

↓

Resource
```

---

# Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| Happens first | Happens second |
| "Who are you?" | "What can you access?" |

---

# Session Lifecycle

```
Login

↓

Session Created

↓

Authenticated Requests

↓

Session Expiration

↓

Logout
```

---

# Identity and Access Management (IAM)

```
Identity

↓

Authentication

↓

Authorization

↓

Monitoring

↓

Review
```

---

# Role-Based Access Control (RBAC)

```
User

↓

Role

↓

Permissions

↓

Resources
```

---

# Secure Password Practices

Recommended practices:

- Strong unique passwords
- Password managers
- Multi-Factor Authentication (MFA)
- Secure password storage
- Regular access reviews

---

# Input Validation

```
Input

↓

Validation

↓

Business Rules

↓

Processing
```

Validate:

- Type
- Length
- Format
- Allowed values
- Business constraints

---

# Output Encoding

```
Application Data

↓

Output Encoding

↓

Browser
```

Output encoding helps ensure data is safely rendered in the intended context.

---

# Secure Communication

```
Client

↓

HTTPS

↓

Server
```

Always protect sensitive communications using secure transport protocols.

---

# Secure Development Principles

```
Secure Development

│

├── Security by Design

├── Code Reviews

├── Testing

├── Logging

├── Monitoring

├── Secure Configuration

├── Documentation

└── Continuous Improvement
```

---

# Logging Essentials

Log important events such as:

```
Logs

│

├── Authentication

├── Authorization

├── Errors

├── Administrative Actions

├── Configuration Changes

└── Audit Events
```

---

# Monitoring Essentials

```
Applications

↓

Monitoring

↓

Alerts

↓

Analysis

↓

Response
```

---

# Enterprise Security Workflow

```
Business Goals

↓

Risk Assessment

↓

Security Design

↓

Implementation

↓

Validation

↓

Deployment

↓

Monitoring

↓

Continuous Improvement
```

---

# Enterprise Example

A financial organization secures its customer portal by combining:

- Secure authentication
- Role-based authorization
- Secure communication
- Logging
- Continuous monitoring
- Governance
- Regular security reviews
- Business continuity planning

This layered approach improves operational resilience while supporting business objectives.

---

# Quick Revision Table

| Topic | Key Point |
|--------|-----------|
| CIA Triad | Confidentiality, Integrity, Availability |
| Authentication | Verify identity |
| Authorization | Verify permissions |
| RBAC | Role-based permissions |
| IAM | Identity lifecycle management |
| HTTPS | Secure communication |
| Input Validation | Validate all incoming data |
| Logging | Record important events |
| Monitoring | Observe security and operations |
| Secure SDLC | Integrate security throughout development |

---

# Conceptual Hands-on Lab

1. Draw the HTTP request flow from memory.
2. Explain the difference between authentication and authorization.
3. List the HTTP status code categories and common examples.
4. Draw the Secure SDLC lifecycle.
5. Create a one-page summary of the CIA Triad and core security principles.

> Practice only conceptual and defensive exercises. Do not perform testing against systems without explicit authorization.

---

# Best Practices

- Keep this cheat sheet available during revision.
- Focus on understanding concepts rather than memorizing definitions.
- Review diagrams regularly.
- Connect each principle to real-world enterprise scenarios.
- Update your notes as technologies and standards evolve.

---

# Common Mistakes

- Confusing authentication with authorization.
- Memorizing HTTP status codes without understanding their categories.
- Ignoring security principles in application design.
- Assuming client-side validation is sufficient.
- Treating logging and monitoring as optional.

---

# Key Takeaways

- The CIA Triad forms the foundation of information security.
- Secure development integrates security throughout the software lifecycle.
- Authentication verifies identity; authorization determines permissions.
- HTTPS protects communication through encryption, integrity, and server authentication.
- Strong security depends on layered controls, monitoring, governance, and continuous improvement.

# 66-Web-Security-Cheat-Sheet.md

# Part 2 — OWASP, Secure Headers, Cookies, Sessions, API Security, Encryption, Authentication, and Authorization

> **"Most web security incidents can be significantly reduced by consistently applying well-established security best practices across authentication, sessions, APIs, data protection, and application design."**

---

# Learning Objectives

After completing this part, you will have a quick-reference guide for:

- OWASP Top Risks
- Secure HTTP Headers
- Cookies
- Session Management
- API Security
- Authentication & Authorization
- Encryption
- Data Protection
- Enterprise Security Controls

---

# OWASP Security Philosophy

```
Secure Design

↓

Secure Coding

↓

Security Testing

↓

Deployment

↓

Monitoring

↓

Continuous Improvement
```

---

# Common Web Security Risk Categories

| Category | Primary Goal |
|----------|--------------|
| Broken Access Control | Prevent unauthorized access |
| Cryptographic Failures | Protect sensitive information |
| Injection | Prevent untrusted input from affecting application behavior |
| Insecure Design | Build security into architecture |
| Security Misconfiguration | Maintain secure defaults |
| Vulnerable Components | Keep software updated |
| Identification & Authentication Failures | Protect user identities |
| Software & Data Integrity Failures | Preserve trusted software and data |
| Security Logging & Monitoring Failures | Improve visibility |
| Server-Side Request Forgery (SSRF) | Validate outbound requests appropriately |

---

# Secure Authentication Flow

```
User

↓

Identity Verification

↓

Multi-Factor Authentication

↓

Authenticated Session

↓

Application Access
```

---

# Authorization Flow

```
Authenticated User

↓

Role Evaluation

↓

Permission Check

↓

Resource Access

↓

Audit Logging
```

---

# Authentication Factors

```
Authentication

│

├── Something You Know

├── Something You Have

└── Something You Are
```

Combining multiple factors strengthens identity verification.

---

# Password Best Practices

```
Passwords

│

├── Strong

├── Unique

├── Long

├── Password Manager

├── MFA Enabled

└── Secure Storage
```

---

# Session Security Checklist

```
✓ Secure Session IDs

✓ HTTPS Only

✓ Appropriate Expiration

✓ Secure Logout

✓ Session Renewal

✓ Continuous Validation
```

---

# Secure Cookie Attributes

| Attribute | Purpose |
|-----------|----------|
| Secure | Send only over HTTPS |
| HttpOnly | Reduce client-side script access |
| SameSite | Reduce unintended cross-site requests |
| Appropriate Expiration | Limit session lifetime |

---

# Secure HTTP Headers

| Header | Purpose |
|---------|----------|
| Content-Security-Policy | Restrict allowed content sources |
| Strict-Transport-Security | Enforce HTTPS |
| X-Content-Type-Options | Reduce MIME type confusion |
| Referrer-Policy | Control referrer information |
| Permissions-Policy | Limit browser feature access |
| Cache-Control | Manage caching of sensitive responses |

---

# Input Validation Checklist

```
Input

↓

Validate Type

↓

Validate Length

↓

Validate Format

↓

Validate Business Rules

↓

Process
```

Validate every input regardless of its source.

---

# Output Encoding

```
Application Data

↓

Context-Aware Encoding

↓

Browser

↓

Safe Rendering
```

Encode output according to the destination context (such as HTML, JavaScript, CSS, or URLs).

---

# API Security Fundamentals

```
Client

↓

Authentication

↓

Authorization

↓

Input Validation

↓

Business Logic

↓

Logging

↓

Monitoring
```

---

# API Security Checklist

```
✓ Authentication

✓ Authorization

✓ HTTPS

✓ Rate Limiting

✓ Input Validation

✓ Logging

✓ Monitoring

✓ Error Handling
```

---

# Encryption Overview

```
Sensitive Data

↓

Encryption

↓

Secure Storage

↓

Authorized Access
```

Encryption helps protect sensitive information both in transit and at rest.

---

# Data Classification

```
Data

│

├── Public

├── Internal

├── Confidential

└── Restricted
```

Security controls should match the sensitivity of the data being protected.

---

# Least Privilege

```
User

↓

Minimum Permissions

↓

Business Tasks

↓

Review

↓

Adjustment
```

Grant only the permissions required to perform legitimate responsibilities.

---

# Defense in Depth

```
Users

↓

Identity

↓

Application

↓

Network

↓

Infrastructure

↓

Monitoring

↓

Governance
```

Multiple security layers improve resilience.

---

# Zero Trust

```
Request

↓

Verify Identity

↓

Verify Device

↓

Evaluate Policy

↓

Grant Limited Access
```

Trust is established through continuous verification rather than network location.

---

# Secure SDLC Reminder

```
Requirements

↓

Design

↓

Development

↓

Testing

↓

Deployment

↓

Operations

↓

Continuous Improvement
```

---

# Logging Checklist

Log important events such as:

```
Logs

│

├── Login Events

├── Access Decisions

├── Administrative Actions

├── Configuration Changes

├── Security Events

├── Errors

└── Audit Records
```

---

# Monitoring Checklist

```
Applications

↓

Metrics

↓

Logs

↓

Alerts

↓

Analysis

↓

Operational Response
```

---

# Security Configuration Checklist

```
✓ Secure Defaults

✓ Remove Unnecessary Services

✓ Strong Authentication

✓ Least Privilege

✓ Regular Updates

✓ Configuration Reviews

✓ Documentation
```

---

# Vulnerability Management Lifecycle

```
Identify

↓

Assess

↓

Prioritize

↓

Remediate

↓

Validate

↓

Continuous Monitoring
```

---

# Patch Management Lifecycle

```
Update Available

↓

Evaluation

↓

Testing

↓

Deployment

↓

Verification

↓

Documentation
```

---

# Enterprise Security Layers

```
Governance

↓

Identity

↓

Application

↓

Network

↓

Infrastructure

↓

Monitoring

↓

Business Continuity
```

---

# Enterprise Example

An e-commerce company protects its customer platform by implementing:

- MFA for administrators
- RBAC for internal users
- Secure cookie settings
- HTTPS across all services
- Context-aware output encoding
- Centralized logging
- Continuous monitoring
- Regular vulnerability management
- Governance reviews

These controls work together to strengthen the organization's security posture.

---

# Quick Revision Table

| Topic | Quick Reminder |
|--------|----------------|
| MFA | Multiple authentication factors |
| RBAC | Role-based permissions |
| Least Privilege | Minimum required access |
| CSP | Restrict content sources |
| HSTS | Enforce HTTPS |
| Secure Cookies | Secure, HttpOnly, SameSite |
| API Security | Authentication + Authorization + Validation |
| Encryption | Protect sensitive data |
| Defense in Depth | Multiple independent controls |
| Zero Trust | Verify every request |

---

# Conceptual Hands-on Lab

1. Draw a secure authentication workflow.
2. Create a checklist for reviewing cookie settings.
3. Design a conceptual API request flow showing authentication, authorization, validation, logging, and monitoring.
4. Classify sample business data into Public, Internal, Confidential, and Restricted.
5. Review an application's security headers and explain the purpose of each.

> Perform all exercises conceptually and only in authorized environments.

---

# Best Practices

- Apply security controls consistently across all applications.
- Protect authentication with multiple factors where appropriate.
- Use secure cookie attributes for session management.
- Validate all inputs on the server side.
- Implement context-aware output encoding.
- Log security-relevant events while protecting sensitive information.
- Review configurations regularly.
- Integrate security into every phase of the SDLC.

---

# Common Mistakes

- Treating authentication as sufficient without authorization.
- Granting excessive permissions.
- Using insecure default configurations.
- Forgetting to review session management settings.
- Neglecting logging and monitoring.
- Applying encryption without proper key management governance.
- Failing to update components and configurations regularly.

---

# Key Takeaways

- Authentication, authorization, session management, and secure configuration are foundational web security controls.
- Defense in Depth and Zero Trust complement each other in enterprise environments.
- Secure headers, cookies, encryption, and API protections improve application resilience.
- Continuous monitoring, logging, vulnerability management, and governance help maintain a strong security posture.
- Consistent application of best practices is more effective than relying on any single security control.

```text id="rrks28"
**Next:** Part 3
```