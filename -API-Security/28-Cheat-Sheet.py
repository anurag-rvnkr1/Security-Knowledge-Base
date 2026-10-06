# 28 - API Security Cheat Sheet

# Introduction

This chapter is a quick-reference guide that summarizes the most important concepts covered throughout this handbook.

Use it for:

- Interview revision
- Penetration testing
- Secure development
- Code reviews
- Incident response
- Daily engineering work
- Security assessments

---

# API Security Lifecycle

```
Design

   │

Develop

   │

Test

   │

Deploy

   │

Monitor

   │

Respond

   ▼

Improve
```

---

# Secure API Principles

✓ Security by Design

✓ Defense in Depth

✓ Zero Trust

✓ Least Privilege

✓ Complete Mediation

✓ Secure Defaults

✓ Fail Securely

✓ Input Validation

✓ Output Encoding

✓ Continuous Monitoring

---

# CIA Triad

```
Confidentiality

      │

Integrity

      │

Availability
```

---

# REST Constraints

- Client-Server
- Stateless
- Cacheable
- Uniform Interface
- Layered System
- Code-on-Demand (Optional)

---

# HTTP Methods

| Method | Purpose | Idempotent |
|----------|----------|------------|
| GET | Read | Yes |
| POST | Create | No |
| PUT | Replace | Yes |
| PATCH | Partial Update | Usually No |
| DELETE | Delete | Yes |
| HEAD | Headers Only | Yes |
| OPTIONS | Discover Supported Methods | Yes |

---

# Common HTTP Status Codes

## Success

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |

---

## Client Errors

| Code | Meaning |
|------|----------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 409 | Conflict |
| 415 | Unsupported Media Type |
| 422 | Unprocessable Content |
| 429 | Too Many Requests |

---

## Server Errors

| Code | Meaning |
|------|----------|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

---

# Common HTTP Headers

## Request Headers

- Authorization
- Content-Type
- Accept
- User-Agent
- Host
- Origin
- Referer
- Cookie

---

## Response Headers

- Content-Type
- Cache-Control
- Content-Length
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

---

# Authentication

Common mechanisms

- API Keys
- Basic Authentication
- Session Cookies
- JWT
- OAuth 2.0
- OpenID Connect
- Mutual TLS

---

# Authorization Models

- RBAC
- ABAC
- ACL
- Policy-Based Authorization
- Resource-Based Authorization

---

# Authentication vs Authorization

```
Authentication

Who are you?

──────────────

Authorization

What are you allowed to do?
```

---

# JWT Structure

```
Header

   .

Payload

   .

Signature
```

Remember

✓ Verify signatures

✓ Validate expiration

✓ Validate issuer

✓ Validate audience

✓ Never trust unsigned tokens

---

# OAuth 2.0 Grant Types

| Grant | Typical Use |
|---------|-------------|
| Authorization Code + PKCE | Public clients |
| Client Credentials | Service-to-service |
| Refresh Token | Session renewal |
| Device Authorization | Limited-input devices |

---

# OpenID Connect

Provides

- Authentication
- Identity
- User Information
- ID Token

OAuth provides authorization.

OIDC provides authentication.

---

# API Gateway Responsibilities

✓ Authentication

✓ Authorization

✓ Routing

✓ Rate Limiting

✓ Monitoring

✓ Logging

✓ TLS Enforcement

✓ Version Management

---

# Rate Limiting

Common algorithms

- Token Bucket
- Leaky Bucket
- Sliding Window
- Fixed Window

Protect

- Login
- Search
- Password Reset
- File Upload
- Expensive Operations

---

# Input Validation Checklist

Validate

✓ Length

✓ Type

✓ Format

✓ Allowed Values

✓ Required Fields

✓ Numeric Ranges

✓ Object Structure

Reject unexpected input.

---

# Output Security

Remember

- Encode output appropriately
- Return minimum required data
- Hide internal implementation details
- Do not expose stack traces
- Avoid information leakage

---

# Secret Management

Never store

- Passwords
- API Keys
- Database Credentials
- Private Keys
- Cloud Credentials

Use

- Secret Managers
- Environment Variables (with appropriate controls)
- Credential Rotation
- Access Control

---

# Cryptography

Encrypt

- Data in Transit
- Sensitive Data at Rest
- Backup Data
- Authentication Tokens (when appropriate)

Do not create custom cryptographic algorithms.

---

# Secure Logging

Always log

- Authentication
- Authorization
- Administrative Actions
- Configuration Changes
- Errors
- Audit Events

Never log

- Passwords
- Secrets
- Private Keys
- Sensitive Tokens
- Encryption Keys

---

# Observability

```
Logs

Metrics

Traces
```

Use

- Correlation IDs
- Distributed Tracing
- Structured Logging
- Dashboards

---

# Monitoring

Monitor

- Availability
- Latency
- Error Rate
- Authentication
- Authorization
- Resource Usage
- Rate Limiting
- API Versions

---

# Detection Engineering

High-value detections

- Credential Stuffing
- Token Abuse
- API Enumeration
- Object Enumeration
- GraphQL Abuse
- Privilege Escalation
- Data Exfiltration
- Configuration Changes

---

# SIEM Workflow

```
Logs

   │

Normalization

   │

Correlation

   │

Detection

   │

Alert

   ▼

SOC
```

---

# Incident Response Lifecycle

```
Preparation

     │

Detection

     │

Analysis

     │

Containment

     │

Eradication

     │

Recovery

     │

Lessons Learned
```

---

# API Testing Workflow

```
Recon

   │

Enumeration

   │

Authentication

   │

Authorization

   │

Input Validation

   │

Business Logic

   │

Reporting
```

---

# API Fuzzing Checklist

Test

✓ Query Parameters

✓ Path Parameters

✓ Headers

✓ Cookies

✓ JSON

✓ XML

✓ File Uploads

✓ Authentication

✓ Authorization

✓ Large Payloads

✓ Boundary Values

---

# API Penetration Testing Checklist

Review

✓ Documentation

✓ OpenAPI Specification

✓ Authentication

✓ Authorization

✓ Session Management

✓ Business Logic

✓ Error Handling

✓ Rate Limiting

✓ Logging

✓ Monitoring

---

# OWASP API Security Top 10

| Risk | Description |
|------|-------------|
| API1 | Broken Object Level Authorization |
| API2 | Broken Authentication |
| API3 | Broken Object Property Level Authorization |
| API4 | Unrestricted Resource Consumption |
| API5 | Broken Function Level Authorization |
| API6 | Unrestricted Access to Sensitive Business Flows |
| API7 | Server-Side Request Forgery (SSRF) |
| API8 | Security Misconfiguration |
| API9 | Improper Inventory Management |
| API10 | Unsafe Consumption of APIs |

---

# Secure Development Checklist

✓ Threat Modeling

✓ Input Validation

✓ Output Encoding

✓ Least Privilege

✓ Secret Management

✓ Dependency Scanning

✓ Secure Error Handling

✓ Logging

✓ Monitoring

✓ Security Testing

---

# DevSecOps Pipeline

```
Developer

    │

Commit

    │

Code Review

    │

SAST

    │

Dependency Scan

    │

Secret Scan

    │

Unit Tests

    │

Contract Tests

    │

DAST

    │

API Fuzzing

    │

Deployment

    │

Monitoring
```

---

# Enterprise API Security Architecture

```
Internet

     │

Load Balancer

     │

Web Application Firewall

     │

API Gateway

     │

Authentication

     │

Authorization

     │

Backend APIs

     │

Database

     │

Logging

     │

Monitoring

     │

SIEM

     ▼

SOC
```

---

# Common Mistakes

Avoid

✗ Trusting client input

✗ Missing authorization checks

✗ Hard-coded secrets

✗ Weak logging

✗ Exposing stack traces

✗ Ignoring rate limits

✗ Outdated dependencies

✗ Missing monitoring

✗ Poor API inventory

✗ Skipping security testing

---

# Interview Quick Revision

Know how to explain

- REST
- GraphQL
- gRPC
- HTTP Methods
- HTTP Status Codes
- Authentication
- Authorization
- JWT
- OAuth 2.0
- OpenID Connect
- API Gateway
- Rate Limiting
- CORS
- CSRF
- OWASP API Security Top 10
- Secure Coding
- API Testing
- API Fuzzing
- API Pentesting
- DevSecOps
- Monitoring
- SIEM
- Incident Response

---

# Golden Rules

1. Never trust user input.
2. Authenticate every identity.
3. Authorize every request.
4. Encrypt sensitive communications.
5. Apply least privilege.
6. Protect secrets.
7. Validate all external input.
8. Log security events.
9. Monitor continuously.
10. Test security throughout the SDLC.
11. Patch vulnerabilities promptly.
12. Maintain an accurate API inventory.
13. Prepare for incidents before they happen.
14. Automate security where appropriate.
15. Continuously improve defenses.

---

# Final Review Checklist

Before deploying any API, verify:

| Control | Complete |
|----------|----------|
| Threat Model | □ |
| Authentication | □ |
| Authorization | □ |
| HTTPS Enabled | □ |
| Input Validation | □ |
| Output Encoding | □ |
| Secrets Protected | □ |
| Logging Enabled | □ |
| Monitoring Configured | □ |
| Rate Limiting | □ |
| Error Handling Reviewed | □ |
| Security Testing Completed | □ |
| Dependencies Updated | □ |
| Documentation Updated | □ |
| Incident Response Ready | □ |

---

# API Security Master Workflow

```
Requirements

      │

Threat Modeling

      │

Architecture

      │

Development

      │

Security Testing

      │

CI/CD

      │

Deployment

      │

Monitoring

      │

Detection

      │

Incident Response

      │

Lessons Learned

      ▼

Continuous Improvement
```

---

# Congratulations!

You have completed the **API Security Handbook**.

By working through these chapters, you have covered:

- API fundamentals
- REST, SOAP, GraphQL, and gRPC
- HTTP protocols
- Authentication and authorization
- JWT, OAuth 2.0, and OpenID Connect
- API gateways and rate limiting
- CORS and CSRF
- Input validation
- OWASP API Security Top 10
- API vulnerability testing
- API fuzzing
- API penetration testing
- API security tools
- Secure API development
- Monitoring and observability
- Incident response
- Enterprise architectures
- DevSecOps integration
- Detection engineering
- Interview preparation
- Practical security checklists

This cheat sheet serves as a concise reference for day-to-day engineering, security assessments, interview preparation, and secure API design.