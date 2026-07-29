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

```text id="rrks28"
**Next:** Part 2
```