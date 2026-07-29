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

**Next:** HTTP Method Security, Method Override Attacks, Unsafe Method Exposure, CORS Interactions, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.