# 07 - HTTP Methods

# Introduction

HTTP (Hypertext Transfer Protocol) is the foundation of communication on the World Wide Web.

Every interaction between a client and a web server is performed using an **HTTP request** and an **HTTP response**.

An HTTP method (also called an HTTP verb) tells the server **what action the client wants to perform** on a resource.

Examples include:

- Retrieve data
- Create data
- Update data
- Delete data
- Modify data
- Check resource availability

Understanding HTTP methods is essential for:

- REST API development
- API security
- Penetration testing
- Secure backend engineering
- Detection engineering
- Threat hunting
- Incident response

Almost every modern web application, REST API, GraphQL endpoint, and many gRPC gateways ultimately rely on HTTP.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand HTTP methods.
- Learn HTTP request semantics.
- Differentiate safe and idempotent methods.
- Map HTTP methods to CRUD operations.
- Understand method-specific security risks.
- Learn enterprise API design principles.
- Identify common implementation mistakes.
- Perform HTTP method security testing.
- Build detection rules for HTTP abuse.

---

# What is an HTTP Method?

An HTTP method defines the **intended action** for a resource.

Example

```
Client

      │

GET /users/10

      ▼

Server

      │

Return User

      ▼

Response
```

The server interprets the method before processing the request.

---

# HTTP Request Structure

```
GET /users/10 HTTP/1.1

Host: api.company.com

Authorization: Bearer <token>

User-Agent: Browser

Accept: application/json
```

Components

- Method
- URI
- HTTP Version
- Headers
- Body (optional)

---

# HTTP Response Structure

```
HTTP/1.1 200 OK

Content-Type: application/json

Content-Length: 180

{
    "id":10,
    "name":"Alice"
}
```

Components

- Status line
- Headers
- Response body

---

# HTTP Request Lifecycle

```
Client

   │

DNS Resolution

   │

TCP Connection

   │

TLS Handshake

   │

HTTP Request

   │

Web Server

   │

Application

   │

Database

   │

HTTP Response

   ▼

Client
```

Each stage introduces its own security considerations.

---

# Common HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve resource |
| POST | Create resource |
| PUT | Replace resource |
| PATCH | Partial update |
| DELETE | Remove resource |
| HEAD | Retrieve headers only |
| OPTIONS | Discover supported methods |
| TRACE | Diagnostic loopback |
| CONNECT | Create network tunnel |

---

# CRUD Mapping

| CRUD Operation | HTTP Method |
|---------------|-------------|
| Create | POST |
| Read | GET |
| Update | PUT / PATCH |
| Delete | DELETE |

This mapping is the foundation of RESTful API design.

---

# HTTP Method Classification

Methods can be categorized by behavior.

```
HTTP Methods

        │

 ┌──────┼────────┐

 ▼      ▼        ▼

Safe  Unsafe  Idempotent
```

Understanding these properties helps developers design predictable APIs.

---

# Safe Methods

A safe method **does not modify server state**.

Safe methods

- GET
- HEAD
- OPTIONS

Example

```
GET

↓

Read Data

↓

No Modification
```

Safe methods should only retrieve information.

---

# Unsafe Methods

Unsafe methods modify server state.

Examples

- POST
- PUT
- PATCH
- DELETE

Example

```
DELETE

↓

Remove Resource
```

Unsafe methods require stronger security controls.

---

# Idempotent Methods

An idempotent method produces the same result regardless of how many times it is repeated.

Example

```
DELETE /users/100

↓

User Deleted

↓

DELETE Again

↓

Still Deleted
```

The resource remains deleted.

---

# Non-Idempotent Methods

POST is generally non-idempotent.

Example

```
POST /orders

↓

Create Order

↓

POST Again

↓

Second Order Created
```

Repeated requests may create duplicate resources.

---

# Safe vs Idempotent

| Method | Safe | Idempotent |
|---------|------|------------|
| GET | Yes | Yes |
| HEAD | Yes | Yes |
| OPTIONS | Yes | Yes |
| POST | No | No |
| PUT | No | Yes |
| PATCH | No | Usually No |
| DELETE | No | Yes |

Understanding this distinction is critical for API design and retry logic.

---

# GET Method

Purpose

Retrieve information.

Example

```
GET /products/100
```

Typical response

```json
{
    "id":100,
    "name":"Laptop"
}
```

Characteristics

- Safe
- Idempotent
- Cacheable
- Read-only

GET requests should not change application state.

---

# GET Request Flow

```
Client

 │

GET

 ▼

API

 │

Database

 ▼

Response
```

GET is the most frequently used HTTP method.

---

# Common GET Use Cases

Examples

- Retrieve user profile
- Search products
- Fetch order history
- Download public content
- Read configuration

---

# GET Security Considerations

Sensitive information should **never** be placed in the URL.

Avoid

```
GET /login?password=Secret123
```

Problems

- Browser history
- Proxy logs
- Server logs
- Analytics tools
- Referrer headers

Sensitive information belongs in protected request bodies or secure authentication mechanisms—not query strings.

---

# Query Parameters

GET requests commonly use query parameters.

Example

```
GET /products?page=2&limit=20
```

Common parameters

- page
- limit
- search
- category
- sort
- filter

Every parameter requires validation.

---

# POST Method

Purpose

Create new resources.

Example

```
POST /users
```

Request

```json
{
    "name":"Alice",
    "email":"alice@example.com"
}
```

Response

```
201 Created
```

POST requests usually include a request body.

---

# POST Request Flow

```
Client

 │

POST

 ▼

Application

 │

Validation

 │

Database

 ▼

Created Resource
```

POST requests frequently trigger business logic.

---

# Common POST Use Cases

Examples

- User registration
- Login
- Create order
- Upload file
- Submit payment
- Create support ticket

---

# POST Security Considerations

POST endpoints often process untrusted input.

Validate:

- Input format
- Length
- Data types
- Business rules
- Authentication
- Authorization

Protect against:

- Injection attacks
- Mass assignment
- Business logic abuse
- File upload vulnerabilities

---

# PUT Method

Purpose

Replace an existing resource.

Example

```
PUT /users/10
```

Request

```json
{
    "name":"Alice",
    "email":"alice@example.com"
}
```

The supplied representation replaces the existing resource.

---

# PUT Characteristics

- Idempotent
- Replaces entire resource
- Often used for configuration updates
- Should validate all required fields

Repeated identical requests should not create additional resources.

---

# PUT Request Flow

```
Client

 │

PUT

 ▼

Validate

 │

Replace Resource

 ▼

Response
```

PUT is preferred when the client provides the complete updated representation.

---

# PATCH Method

Purpose

Modify part of a resource.

Example

```
PATCH /users/10
```

Request

```json
{
    "email":"new@example.com"
}
```

Only the specified fields are updated.

---

# PUT vs PATCH

| PUT | PATCH |
|------|--------|
| Full replacement | Partial update |
| Entire resource required | Selected fields |
| Idempotent | Often non-idempotent |
| Simpler semantics | More flexible |

PATCH reduces bandwidth when only a few fields change.

---

# DELETE Method

Purpose

Remove a resource.

Example

```
DELETE /users/10
```

Typical response

```
204 No Content
```

Characteristics

- Unsafe
- Idempotent
- Requires strong authorization

Deletion operations should be logged and audited.

---

# DELETE Request Flow

```
Client

 │

DELETE

 ▼

Authorization

 │

Database

 ▼

Deleted
```

DELETE operations should verify ownership and permissions before execution.

---

# HEAD Method

HEAD behaves like GET but returns **headers only**.

Example

```
HEAD /report.pdf
```

Response

```
HTTP/1.1 200 OK

Content-Length: 125600

Content-Type: application/pdf
```

No response body is returned.

---

# Common HEAD Use Cases

Examples

- Check file existence
- Verify cache freshness
- Determine content length
- Monitor service availability

HEAD requests reduce unnecessary bandwidth usage.

---

# OPTIONS Method

OPTIONS returns the communication options supported by a resource.

Example

```
OPTIONS /users
```

Typical response

```
Allow:

GET

POST

PUT

DELETE
```

OPTIONS plays an important role in Cross-Origin Resource Sharing (CORS).

---

# TRACE Method

TRACE echoes the received request for diagnostic purposes.

```
Client

 │

TRACE

 ▼

Server

 │

Echo Request

 ▼

Client
```

Modern production systems commonly disable TRACE because it can contribute to information disclosure.

---

# CONNECT Method

CONNECT establishes a network tunnel.

```
Client

 │

CONNECT

 ▼

Proxy

 │

TLS Tunnel

 ▼

Destination Server
```

CONNECT is primarily used by proxies to establish encrypted HTTPS connections.

---

# Enterprise Example

An e-commerce platform exposes the following API:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/products` | GET | Browse products |
| `/products/{id}` | GET | View product |
| `/orders` | POST | Create order |
| `/orders/{id}` | GET | View order |
| `/users/{id}` | PATCH | Update profile |
| `/users/{id}` | DELETE | Remove account |

Each method is selected according to the intended resource operation.

---

# Key Takeaways

- HTTP methods define the intended action on a resource.
- GET retrieves data and should never modify server state.
- POST creates resources and commonly executes business logic.
- PUT replaces resources, while PATCH performs partial updates.
- DELETE removes resources and requires strict authorization.
- HEAD, OPTIONS, TRACE, and CONNECT serve specialized purposes.
- Safe and idempotent properties influence API design, caching, retries, and security.

---

# HTTP Method Security

HTTP methods determine **what action a client is requesting**, but they do **not** provide security by themselves.

Every HTTP method must be protected using appropriate:

- Authentication
- Authorization
- Input validation
- Rate limiting
- Logging
- Monitoring

Security controls should be applied consistently regardless of the HTTP method.

---

# Security Model

```
               Client

                  │

                  ▼

        Authentication Layer

                  │

                  ▼

        Authorization Layer

                  │

                  ▼

        HTTP Method Validation

                  │

                  ▼

         Input Validation

                  │

                  ▼

        Business Logic Layer

                  │

                  ▼

            Database
```

Each layer protects against different attack vectors.

---

# Method-Based Authorization

Different HTTP methods often require different permissions.

Example

```
Anonymous User

↓

GET /products

↓

Allowed
```

```
Authenticated User

↓

POST /orders

↓

Allowed
```

```
Administrator

↓

DELETE /users

↓

Allowed
```

Authorization decisions should consider:

- User identity
- Role
- Resource ownership
- Business rules

---

# Principle of Least Privilege

Users should receive only the permissions necessary to perform their tasks.

Example

```
Customer

↓

GET /orders

↓

Own Orders Only
```

```
Support Engineer

↓

GET /customers

↓

Assigned Customers
```

```
Administrator

↓

DELETE /users

↓

Authorized
```

Limiting permissions reduces the impact of compromised accounts.

---

# Broken Function Level Authorization (BFLA)

A common API vulnerability occurs when sensitive HTTP methods are accessible to unauthorized users.

Example

```
DELETE /api/users/100
```

If every authenticated user can invoke this endpoint,

```
Authenticated User

↓

DELETE

↓

Administrative Action
```

This represents Broken Function Level Authorization.

Mitigation

- Role verification
- Permission checks
- Server-side authorization
- Audit logging

---

# Broken Object Level Authorization (BOLA)

Object ownership must be verified.

Example

```
GET /orders/100
```

Attacker changes

```
100

↓

101
```

If ownership is not validated,

```
Customer B Order

↓

Information Disclosure
```

Every object request must validate ownership before returning data.

---

# GET Method Security

Although GET is considered safe, it can expose sensitive information.

Potential risks

- Sensitive query parameters
- Information disclosure
- Insecure Direct Object References (IDOR)
- Excessive data exposure
- Enumeration

Example

```
GET /users?email=user@example.com
```

Sensitive identifiers should be handled carefully.

---

# Secure GET Practices

Recommendations

- Validate query parameters
- Require authentication where appropriate
- Enforce authorization
- Limit returned fields
- Implement pagination
- Apply rate limiting
- Avoid exposing internal identifiers

---

# POST Method Security

POST commonly performs operations that modify server state.

Examples

- User registration
- Login
- Payment processing
- File uploads
- Order creation

Security controls

- CSRF protection (where applicable)
- Authentication
- Authorization
- Input validation
- Business logic validation
- Rate limiting

---

# PUT Security

PUT replaces entire resources.

Potential risks

- Unauthorized modification
- Mass assignment
- Missing validation
- Resource replacement

Example

```
PUT /users/10
```

Ensure clients cannot overwrite protected attributes.

---

# PATCH Security

PATCH modifies selected fields.

Potential risks

```
PATCH

↓

Unexpected Fields

↓

Privilege Escalation
```

Example

```json
{
    "role":"Administrator"
}
```

Servers should explicitly allow only approved fields to be modified.

---

# DELETE Security

DELETE operations have significant security impact.

Requirements

- Strong authentication
- Strong authorization
- Ownership verification
- Audit logging
- Soft-delete where appropriate
- Multi-factor approval for sensitive operations

Example

```
DELETE /payments/100
```

Deletion requests should be carefully controlled.

---

# HEAD Security

Although HEAD returns no body, it can still disclose information.

Potential exposure

- File existence
- Content length
- Server type
- Resource availability

Protect sensitive resources with the same authentication and authorization as GET.

---

# OPTIONS Security

OPTIONS reveals supported HTTP methods.

Example

```
Allow:

GET

POST

PUT

DELETE
```

Attackers may use this information for reconnaissance.

Recommendations

- Return only supported methods
- Avoid exposing unnecessary functionality
- Authenticate sensitive endpoints when appropriate

---

# TRACE Security

TRACE echoes the received request.

Potential risks

- Information disclosure
- Cross-Site Tracing (XST)
- Header exposure

Most production servers disable TRACE.

Example

```
TRACE

↓

Echo Authorization Header

↓

Information Leakage
```

---

# CONNECT Security

CONNECT establishes proxy tunnels.

Potential risks

- Proxy abuse
- Unauthorized tunneling
- Bypass of security controls

Recommendations

- Restrict CONNECT
- Authenticate proxy users
- Monitor unusual tunnel creation

---

# HTTP Method Enumeration

Attackers often identify supported methods.

Example

```
OPTIONS /users
```

Response

```
GET

POST

PUT

DELETE
```

Enumeration helps attackers understand the application's capabilities.

---

# Method Fuzzing

Security assessments frequently test unexpected methods.

Examples

```
MOVE

COPY

SEARCH

LINK

UNLINK

PROPFIND

MKCOL
```

Applications should reject unsupported methods.

Expected response

```
405 Method Not Allowed
```

---

# HTTP Method Override

Some applications support overriding HTTP methods.

Example

```
POST

↓

X-HTTP-Method-Override: DELETE
```

Result

```
DELETE Executed
```

If not properly controlled, attackers may bypass filtering or firewall rules.

---

# Method Override Headers

Common override mechanisms

```
X-HTTP-Method-Override

X-Method-Override

_method
```

Servers should only support method overrides when absolutely necessary.

---

# Security Risks of Method Override

Potential attacks

- Firewall bypass
- Proxy bypass
- Authorization bypass
- Logging inconsistencies
- Unexpected request processing

Mitigations

- Disable unnecessary overrides
- Validate override headers
- Log effective HTTP methods
- Apply authorization after method resolution

---

# Cross-Origin Resource Sharing (CORS)

CORS controls which origins may invoke HTTP methods.

Example

```
Origin A

↓

GET

↓

Allowed
```

```
Origin B

↓

DELETE

↓

Blocked
```

Unsafe methods typically require additional browser preflight checks.

---

# Preflight Requests

Browsers send an OPTIONS request before certain cross-origin requests.

```
Browser

 │

OPTIONS

 ▼

Server

 │

Allowed Methods

 ▼

Browser

 │

POST

 ▼

Server
```

Servers should respond with appropriate CORS headers.

---

# Idempotency and Security

Idempotent methods reduce unintended side effects.

Example

```
DELETE

↓

Retry

↓

No Additional Deletion
```

POST operations often require additional controls such as:

- Idempotency keys
- Duplicate request detection
- Transaction identifiers

---

# Rate Limiting by HTTP Method

Different methods often require different rate limits.

Example

| Method | Example Limit |
|---------|---------------|
| GET | Higher |
| POST | Moderate |
| PUT | Moderate |
| PATCH | Moderate |
| DELETE | Lower |

Destructive operations generally require stricter controls.

---

# Logging Requirements

Log

- HTTP method
- URI
- Status code
- User identity
- Source IP
- Request size
- Response size
- Execution time
- Authentication status

Example

```
POST

↓

/orders

↓

201 Created

↓

User: 1200
```

Comprehensive logging supports investigations and compliance.

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| DELETE Spike | Sudden increase in DELETE requests |
| Failed Authorization | Multiple 401 or 403 responses |
| Method Enumeration | Repeated OPTIONS requests |
| TRACE Attempts | TRACE requests observed |
| Unsupported Methods | Multiple 405 responses |
| Method Override Abuse | Frequent override headers |
| Enumeration | Sequential GET requests against object identifiers |
| High-Risk Operations | Multiple PATCH or DELETE requests in short periods |

Detection rules should be tuned according to expected application behavior.

---

# SIEM Integration

Recommended telemetry

```
Access Logs

       │

Authentication Logs

       │

Authorization Logs

       │

API Gateway Logs

       │

Application Logs

       ▼

Enterprise SIEM

       │

Correlation Rules

       ▼

SOC Alerts
```

Example correlation rules

- Multiple DELETE requests across different resources
- Enumeration followed by successful access
- Repeated method override attempts
- Large increase in OPTIONS requests
- Unauthorized PATCH attempts
- TRACE requests against production systems

---

# Enterprise Security Architecture

```
                  Internet

                      │

                      ▼

              Web Application Firewall

                      │

                      ▼

                 API Gateway

                      │

                      ▼

            Authentication Service

                      │

                      ▼

           Authorization Engine

                      │

                      ▼

             HTTP Method Validation

                      │

                      ▼

             Application Services

                      │

                      ▼

                 Database Layer

                      │

                      ▼

           Logging & Monitoring

                      │

                      ▼

                 SIEM / SOC
```

Each request should traverse every security control before reaching application logic.

---

# Hands-on Lab 1 – HTTP Method Enumeration

**Objective**

Identify which HTTP methods are supported by an authorized application.

**Steps**

1. Review API documentation or use an authorized testing environment.
2. Send an `OPTIONS` request to selected endpoints.
3. Record the methods returned in the `Allow` header.
4. Compare supported methods with expected functionality.

**Learning Outcomes**

- HTTP method discovery
- API documentation validation
- Endpoint analysis

---

# Hands-on Lab 2 – Authorization Verification

**Objective**

Verify authorization controls for different HTTP methods.

**Steps**

1. Authenticate with a low-privilege account.
2. Attempt permitted read operations.
3. Verify that privileged methods (such as `DELETE`) are rejected.
4. Document authorization behavior and ownership enforcement.

**Learning Outcomes**

- Method-level authorization
- Least privilege
- Ownership validation

---

# Hands-on Lab 3 – Method Override Review

**Objective**

Determine whether HTTP method override functionality is enabled.

**Steps**

1. Review application documentation or configuration.
2. Identify whether override headers or parameters are supported.
3. Confirm that authorization and logging remain consistent when overrides are used.
4. Record findings and recommendations.

**Learning Outcomes**

- Method override understanding
- Authorization validation
- Logging verification

---

# Common Security Mistakes

Avoid:

- Missing authorization for DELETE
- Exposing sensitive data through GET
- Accepting unsupported HTTP methods
- Allowing unrestricted method overrides
- Returning verbose error messages
- Missing audit logging
- Weak rate limiting
- Ignoring object ownership
- Excessive data exposure
- Missing input validation

---

# Troubleshooting

## 405 Method Not Allowed

Possible causes

- Unsupported method
- Incorrect endpoint
- Proxy restrictions
- API configuration

---

## 401 Unauthorized

Possible causes

- Missing credentials
- Invalid token
- Expired session
- Authentication failure

---

## 403 Forbidden

Possible causes

- Insufficient permissions
- Ownership validation
- Role restrictions
- Policy enforcement

---

## Unexpected DELETE Success

Possible causes

- Missing authorization
- Broken access control
- Incorrect policy configuration
- Privilege escalation vulnerability

---

## CORS Preflight Failure

Possible causes

- Missing `Access-Control-Allow-Methods`
- Incorrect origin configuration
- Unsupported headers
- Proxy misconfiguration

---

# Interview Questions

## Fundamental

1. What is an HTTP method?
2. What is the difference between GET and POST?
3. What makes a method safe?
4. What makes a method idempotent?
5. When should PUT be used instead of PATCH?
6. Why is DELETE considered high risk?
7. What is the purpose of the OPTIONS method?
8. Why is TRACE commonly disabled?
9. What is an HTTP preflight request?
10. What is HTTP method override?

---

## Intermediate

11. How would you secure DELETE endpoints?
12. Explain Broken Function Level Authorization.
13. How would you prevent HTTP method override abuse?
14. Why should GET requests avoid sensitive query parameters?
15. How would you detect HTTP method enumeration?
16. What events should be forwarded to a SIEM?
17. How do CORS and HTTP methods interact?
18. Why are PATCH requests susceptible to privilege escalation?
19. How would you rate-limit different HTTP methods?
20. What logging fields are essential for HTTP method monitoring?

---

## Scenario-Based

**Scenario 1**

A production API suddenly experiences a significant increase in `DELETE` requests.

- Which logs and metrics would you review first?
- How would you determine whether the activity is legitimate or malicious?
- Which immediate containment measures could reduce risk?

---

**Scenario 2**

A penetration test reveals that an application accepts `X-HTTP-Method-Override: DELETE` even though only `POST` is expected.

- What risks does this introduce?
- How would you remediate the issue while preserving required functionality?

---

**Scenario 3**

A customer reports receiving another user's data after modifying an identifier in a `GET` request.

- Which access control weakness does this indicate?
- How would you verify and remediate the vulnerability?

---

# Chapter Summary

In this chapter, we explored the security implications of HTTP methods and their role in secure API design.

We covered:

- HTTP method semantics
- Safe and idempotent methods
- Method-based authorization
- BOLA and BFLA
- Method override attacks
- CORS interactions
- Rate limiting
- Logging
- Detection engineering
- SIEM integration
- Hands-on exercises
- Troubleshooting
- Interview preparation

Proper implementation of HTTP methods improves API predictability, strengthens security controls, and supports effective monitoring and incident response.

---

# Chapter Review

You should now be able to answer:

- What distinguishes safe and idempotent methods?
- How should authorization differ across HTTP methods?
- Why are DELETE and PATCH operations considered higher risk?
- What is HTTP method override, and why can it be dangerous?
- How should applications respond to unsupported methods?
- Which HTTP method patterns should be monitored in a SIEM?
- How would you investigate suspicious method usage in production?

If you can confidently answer these questions, you are ready to continue with **Chapter 08 – HTTP Headers**, where you'll explore request and response headers, security-related headers, caching directives, content negotiation, and header-based attacks.

---

# References

## Standards

- RFC 9110 – HTTP Semantics
- RFC 9112 – HTTP/1.1
- RFC 9113 – HTTP/2
- RFC 9114 – HTTP/3

## Security Standards

- OWASP API Security Top 10
- OWASP ASVS
- OWASP Web Security Testing Guide (WSTG)
- NIST SP 800-53
- NIST Cybersecurity Framework (CSF)

## Further Reading

- HTTPWG Specifications
- Mozilla HTTP Documentation
- OWASP Cheat Sheets

---

# What's Next?

➡️ **Chapter 08 – HTTP Headers**

In the next chapter, we will explore:

- Request headers
- Response headers
- Security headers
- Authentication headers
- Caching headers
- Content negotiation
- Header injection
- Header-based attacks
- Detection engineering
- Enterprise best practices