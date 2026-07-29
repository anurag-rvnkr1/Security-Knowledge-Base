# 03 - REST API

# Introduction

Representational State Transfer (REST) is the most widely adopted architectural style for designing web APIs. Nearly every modern web application, mobile application, cloud platform, Software-as-a-Service (SaaS) product, and enterprise system exposes REST APIs for communication.

Companies such as Amazon, Google, Microsoft, Netflix, GitHub, Stripe, PayPal, Salesforce, and thousands of other organizations rely heavily on REST APIs to provide secure, scalable, and interoperable services.

Unlike traditional Remote Procedure Call (RPC) systems, REST emphasizes resources, standard HTTP methods, stateless communication, and uniform interfaces. These characteristics make REST APIs easy to understand, scalable, cacheable, and suitable for distributed systems.

From a cybersecurity perspective, REST APIs expose business functionality directly over HTTP, making them one of the primary attack surfaces targeted by attackers. Understanding REST is therefore essential for secure API design, penetration testing, DevSecOps, cloud security, and enterprise application security.

This chapter explores REST from both architectural and security perspectives, providing the foundation for the advanced API security topics covered later in this handbook.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand REST and its history.
- Explain REST architectural principles.
- Understand resources and representations.
- Design RESTful URIs.
- Differentiate REST from RPC.
- Understand HTTP methods in REST.
- Explain stateless communication.
- Understand REST request and response structures.
- Identify REST API components.
- Recognize common REST API design patterns.
- Build secure REST APIs.
- Understand enterprise REST architectures.

---

# What is REST?

REST stands for:

> **Representational State Transfer**

REST is an architectural style introduced by **Roy Fielding** in his doctoral dissertation in 2000.

Rather than being a protocol or programming language, REST provides a set of architectural constraints for designing distributed systems.

Applications that follow these constraints are referred to as **RESTful APIs**.

---

# REST Definition

REST is an architectural style in which clients interact with resources exposed by servers using standard HTTP methods through a uniform interface.

Instead of invoking functions directly, clients manipulate resources.

For example:

```
User Resource

↓

GET /users/15
```

instead of

```
getUser(15)
```

The API exposes resources rather than internal implementation details.

---

# History of REST

Before REST became popular, enterprise applications primarily relied on technologies such as:

- CORBA
- DCOM
- SOAP
- XML-RPC
- Java RMI

These technologies often introduced:

- Tight coupling
- Complex message formats
- Heavy XML payloads
- Difficult interoperability
- High implementation complexity

Roy Fielding proposed REST to leverage the existing capabilities of HTTP, resulting in simpler, more scalable web architectures.

---

# REST in Modern Applications

REST APIs are widely used across industries.

Examples include:

Financial Services

- Online banking
- Payment gateways
- Digital wallets

Healthcare

- Patient management
- Electronic health records
- Laboratory systems

E-commerce

- Product catalogs
- Shopping carts
- Order management

Cloud Platforms

- Virtual machines
- Storage
- Networking
- Identity management

Social Media

- Posts
- Comments
- Messaging
- Notifications

Artificial Intelligence

- Model inference
- Image generation
- Natural language processing

---

# REST Communication Model

A REST API follows a client-server communication model.

```
           HTTP Request
Client ----------------------► REST API

Client ◄---------------------- REST API
           HTTP Response
```

The client requests a resource.

The server processes the request and returns a representation of that resource.

---

# Resource-Oriented Architecture

The fundamental concept in REST is the **resource**.

A resource represents any identifiable object managed by the application.

Examples:

```
Users

Orders

Products

Invoices

Employees

Customers

Payments

Transactions
```

Each resource has a unique identifier.

Example:

```
/users/15

/products/87

/orders/542
```

---

# Resource Representation

Clients never interact with the actual resource stored internally.

Instead, they receive a **representation**.

Example JSON response:

```json
{
  "id": 15,
  "name": "Alice",
  "email": "alice@example.com"
}
```

The database may contain dozens of additional fields, but the API returns only the required representation.

---

# REST Architecture Overview

```
                  Client

                     │

             HTTP Request

                     ▼

               REST API Server

                     │

             Business Logic

                     │

                Database

                     │

            HTTP Response

                     ▼

                  Client
```

Each layer has a clearly defined responsibility.

---

# REST Constraints

REST is defined by six architectural constraints.

Applications that follow these constraints are considered RESTful.

The constraints are:

- Client-Server
- Stateless
- Cacheable
- Uniform Interface
- Layered System
- Code on Demand (optional)

These constraints promote scalability, simplicity, and interoperability.

---

# Constraint 1 — Client-Server

Clients and servers are separated.

```
Browser

      │

HTTP

      ▼

API Server
```

Advantages:

- Independent development
- Better scalability
- Easier maintenance
- Platform independence

---

# Constraint 2 — Stateless

Each request contains all information required to process it.

```
Request 1

↓

Complete Information

↓

Response
```

```
Request 2

↓

Complete Information

↓

Response
```

The server does not rely on previous requests to process the current request.

Benefits:

- Easier scaling
- Better reliability
- Simpler load balancing
- Fault tolerance

---

# Constraint 3 — Cacheable

Responses may be cached.

```
Client

 │

 ▼

Cache

 │

 ├── Hit

 │      ▼

 │   Response

 │

 └── Miss

        ▼

REST Server
```

Benefits:

- Reduced latency
- Lower server load
- Improved scalability
- Faster response times

HTTP headers such as `Cache-Control`, `ETag`, and `Expires` help control caching behavior.

---

# Constraint 4 — Uniform Interface

REST APIs expose a consistent interface regardless of implementation.

Examples:

```
GET /users

POST /users

PUT /users/15

DELETE /users/15
```

Clients interact with resources in a predictable manner, reducing complexity and improving interoperability.

---

# Constraint 5 — Layered System

A client does not need to know whether it communicates directly with the application or through intermediary components.

```
Client

 │

 ▼

CDN

 │

 ▼

Load Balancer

 │

 ▼

API Gateway

 │

 ▼

Application Server

 │

 ▼

Database
```

Each layer performs a specific function without exposing internal details to the client.

---

# Constraint 6 — Code on Demand (Optional)

A server may optionally provide executable code to clients.

Examples include:

- JavaScript
- WebAssembly
- Client-side plugins

Unlike the other five constraints, this constraint is optional and is less commonly used in modern REST APIs.

---

# REST vs Traditional RPC

| REST | RPC |
|------|-----|
| Resource-oriented | Function-oriented |
| Uses HTTP methods | Uses procedure calls |
| Standard URIs | Method names |
| Stateless | May maintain state |
| Highly scalable | Often tightly coupled |
| Widely adopted for web APIs | Common in internal systems |

Example:

RPC

```
getCustomer()
```

REST

```
GET /customers/15
```

---

# Characteristics of REST APIs

Well-designed REST APIs typically exhibit the following characteristics:

- Stateless
- Resource-oriented
- Uniform interface
- Layered architecture
- Cacheable responses
- Platform independent
- Scalable
- Easy to consume
- Easy to document
- Secure by design

These principles form the basis of most enterprise web APIs today.

---

# Enterprise Example

A global banking platform exposes the following REST resources:

```
GET /accounts

GET /transactions

POST /payments

GET /cards

POST /beneficiaries

GET /loans

POST /transfers
```

Each endpoint represents a business resource rather than an internal function, allowing clients to interact with the banking system using standardized HTTP semantics.

---

# Key Takeaways

- REST is an architectural style rather than a protocol.
- REST APIs expose resources instead of internal functions.
- Resources are identified using URIs and represented using formats such as JSON.
- REST is built upon six architectural constraints that promote scalability, simplicity, and interoperability.
- Client-server separation, statelessness, caching, and layered systems are fundamental principles of REST.
- REST has become the dominant architectural style for modern web APIs due to its flexibility, simplicity, and compatibility with HTTP.

---

# Resource Identification

Everything in a REST API revolves around **resources**.

A resource is any object, entity, or piece of information that can be identified and manipulated through a URI.

Examples include:

- Users
- Products
- Orders
- Customers
- Employees
- Invoices
- Payments
- Books
- Vehicles
- Flights

A resource is identified using a **Uniform Resource Identifier (URI).**

Example:

```
/users
/orders
/products
/payments
```

Each URI uniquely identifies a collection or an individual resource.

---

# Collections vs Individual Resources

REST distinguishes between collections and individual resources.

Collection:

```
GET /users
```

Returns:

```
All Users
```

Individual Resource:

```
GET /users/101
```

Returns:

```
User 101
```

Architecture Diagram:

```
Users Collection

/users
   │
   ├────────► User 101
   │
   ├────────► User 102
   │
   ├────────► User 103
   │
   └────────► User 104
```

---

# URI Structure

A well-designed REST URI follows a predictable hierarchy.

General format:

```
https://api.company.com/version/resource/id/subresource
```

Example:

```
https://api.company.com/v1/users/105/orders
```

Components:

| Component | Description |
|-----------|-------------|
| https | Protocol |
| api.company.com | Domain |
| v1 | API Version |
| users | Resource Collection |
| 105 | Resource Identifier |
| orders | Child Resource |

---

# URI Naming Best Practices

REST URIs should follow consistent naming conventions.

Good Examples

```
/users

/products

/orders

/customers

/invoices
```

Bad Examples

```
/GetUsers

/CreateOrder

/deleteCustomer

/getAllProducts

/FindInvoice
```

REST focuses on **resources**, not actions.

---

# Use Nouns Instead of Verbs

Incorrect

```
POST /createUser

GET /getOrders

DELETE /deleteOrder
```

Correct

```
POST /users

GET /orders

DELETE /orders/15
```

The HTTP method already defines the action.

---

# Use Plural Resource Names

Recommended

```
/users

/orders

/products

/employees

/customers
```

Avoid

```
/user

/order

/product
```

Plural naming improves consistency and readability.

---

# Use Lowercase URIs

Recommended

```
/users

/user-profile

/order-items
```

Avoid

```
/Users

/UserProfile

/ORDER
```

Reasons:

- Consistency
- Better portability
- Easier documentation
- Reduced ambiguity

---

# Use Hyphens Instead of Underscores

Good

```
/user-profile

/payment-history

/order-items
```

Avoid

```
/user_profile

/payment_history

/order_items
```

Hyphens improve readability and align with common REST conventions.

---

# Avoid File Extensions

Avoid

```
/users.json

/products.xml
```

Instead

```
/users
```

The response format should be determined using the `Accept` header rather than embedding file types in the URI.

---

# Hierarchical Resources

Resources often have parent-child relationships.

Example:

```
Customer

 └────► Orders

            └────► Order Items
```

Corresponding URIs:

```
/customers/25/orders

/customers/25/orders/101

/customers/25/orders/101/items
```

Hierarchy should reflect real business relationships.

---

# Nested Resources

Nested resources represent ownership or containment.

Example:

```
Department

   │

   ▼

Employees

   │

   ▼

Projects
```

REST URIs:

```
/departments/4/employees

/departments/4/employees/20

/departments/4/employees/20/projects
```

Avoid excessive nesting.

Instead of:

```
/company/1/departments/2/teams/3/employees/5/projects/8/tasks/10
```

Prefer flatter structures where practical.

---

# Resource Relationships

Resources may have different types of relationships.

### One-to-One

```
User

 │

 ▼

Profile
```

URI

```
/users/15/profile
```

---

### One-to-Many

```
Customer

 │

 ▼

Orders
```

URI

```
/customers/10/orders
```

---

### Many-to-Many

```
Students

     │

     ▼

Courses
```

Possible URIs

```
/students/50/courses

/courses/12/students
```

---

# Query Parameters

Query parameters filter, sort, and paginate results.

Filtering

```
GET /products?category=laptops
```

Sorting

```
GET /products?sort=price
```

Descending

```
GET /products?sort=-price
```

Pagination

```
GET /products?page=2&limit=25
```

Searching

```
GET /products?search=keyboard
```

Multiple Filters

```
GET /products?brand=Dell&category=Laptop&price=50000
```

Query parameters should **not** change the identity of a resource.

---

# Path Parameters vs Query Parameters

| Path Parameter | Query Parameter |
|---------------|-----------------|
| Identifies a resource | Filters resources |
| Mandatory | Usually optional |
| Part of URI path | Appears after `?` |
| `/users/15` | `/users?page=2` |

Example:

```
GET /users/25
```

Retrieves User 25.

```
GET /users?country=India
```

Retrieves users filtered by country.

---

# Resource Versioning

Enterprise APIs evolve over time.

Versioning prevents breaking existing clients.

Examples:

URI Versioning

```
/v1/users

/v2/users
```

Header Versioning

```
Accept: application/vnd.company.v2+json
```

Query Versioning

```
/users?version=2
```

URI versioning is the most widely adopted approach because it is explicit and easy to document.

---

# REST Maturity Model

The Richardson Maturity Model evaluates how closely an API follows REST principles.

```
Level 0

↓

Level 1

↓

Level 2

↓

Level 3
```

Each level introduces additional REST capabilities.

---

# Level 0 — Single Endpoint

Everything is handled by one endpoint.

Example

```
POST /api
```

Request body determines the operation.

Problems:

- Poor scalability
- Difficult documentation
- Not RESTful

---

# Level 1 — Resources

Separate resources are introduced.

Example

```
/users

/orders

/products
```

Resources are identified independently.

---

# Level 2 — HTTP Methods

HTTP methods express operations.

```
GET

POST

PUT

PATCH

DELETE
```

Example

```
GET /products

POST /products

DELETE /products/10
```

This is where most production REST APIs operate.

---

# Level 3 — Hypermedia (HATEOAS)

Responses include links to related actions.

Example:

```json
{
  "id": 100,
  "status": "Processing",
  "links": [
    {
      "rel": "cancel",
      "href": "/orders/100/cancel"
    },
    {
      "rel": "payment",
      "href": "/orders/100/payment"
    }
  ]
}
```

Clients discover available actions dynamically.

---

# REST Resource Lifecycle

```
Create

   │

   ▼

Read

   │

   ▼

Update

   │

   ▼

Delete
```

This lifecycle maps naturally to CRUD operations and standard HTTP methods.

---

# Enterprise REST Design Principles

Successful enterprise APIs follow several design principles.

- Resource-oriented design
- Predictable URIs
- Consistent naming
- Proper use of HTTP methods
- Versioning strategy
- Stateless communication
- Pagination support
- Filtering and sorting
- Clear error responses
- Comprehensive documentation
- Security by design
- Backward compatibility

Following these principles improves developer experience and long-term maintainability.

---

# Enterprise Example

An online retail platform exposes the following REST resources:

```
GET    /products

GET    /products/200

POST   /orders

GET    /orders/500

GET    /customers/25/orders

PATCH  /orders/500

DELETE /cart/items/20
```

Notice that the URIs represent business resources, while the HTTP methods indicate the desired operation.

---

# Common URI Design Mistakes

Avoid these common mistakes:

❌ Using verbs in URIs

```
/createUser
```

✔ Correct

```
POST /users
```

---

❌ Inconsistent naming

```
/users

/getOrders

/ProductList
```

✔ Correct

```
/users

/orders

/products
```

---

❌ Excessive nesting

```
/companies/1/departments/2/teams/3/projects/5/tasks/10/comments/15
```

Prefer simpler resource structures where possible.

---

# Key Takeaways

- Resources are the core building blocks of REST APIs.
- Every resource should have a unique and meaningful URI.
- URIs should use nouns, plural names, lowercase letters, and consistent structures.
- Path parameters identify resources, while query parameters filter or modify result sets.
- REST maturity progresses from single endpoints to hypermedia-driven APIs.
- Well-designed resource hierarchies improve usability, maintainability, and scalability.
- Consistent URI design is essential for enterprise-grade API development.

---

# HTTP Methods in REST

HTTP methods define the action that should be performed on a resource.

Unlike traditional RPC systems where the action is embedded in the URI, REST uses standardized HTTP methods while keeping the URI focused on the resource.

Example:

```
GET /users/15
```

The URI identifies the resource.

The HTTP method defines the operation.

This separation is one of the core principles of REST.

---

# Common HTTP Methods

The most commonly used HTTP methods are:

| Method | Purpose |
|----------|----------|
| GET | Retrieve resource |
| POST | Create resource |
| PUT | Replace resource |
| PATCH | Partially update resource |
| DELETE | Delete resource |
| HEAD | Retrieve headers only |
| OPTIONS | Discover supported methods |
| TRACE | Diagnostic method (rarely enabled) |
| CONNECT | Establish tunnel (used by proxies) |

In REST APIs, the first five methods are used most frequently.

---

# GET Method

The GET method retrieves information from the server.

It should **never modify data**.

Example:

```
GET /products
```

Retrieve all products.

```
GET /products/101
```

Retrieve Product 101.

Architecture

```
Client

   │

GET /products

   ▼

REST API

   │

Database

   │

Return Data

   ▼

Client
```

Example Response

```json
[
  {
    "id": 101,
    "name": "Laptop"
  },
  {
    "id": 102,
    "name": "Keyboard"
  }
]
```

---

# Characteristics of GET

Properties:

- Read-only
- Safe
- Idempotent
- Cacheable
- No request body required

Suitable for:

- Search
- Listing resources
- Viewing details
- Downloading data

---

# POST Method

POST creates new resources.

Example:

```
POST /users
```

Request

```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

Architecture

```
Client

   │

POST

   ▼

API

   │

Create User

   ▼

Database

   │

New Record

   ▼

Response
```

Example Response

```json
{
  "id": 120,
  "name": "Alice",
  "email": "alice@example.com"
}
```

Typical status code:

```
201 Created
```

---

# Characteristics of POST

Properties:

- Creates resources
- Not idempotent
- Usually contains request body
- Often changes server state

Common Uses

- Registration
- Login
- Payment processing
- File uploads
- Creating orders
- Sending messages

---

# PUT Method

PUT completely replaces an existing resource.

Example

```
PUT /users/25
```

Request

```json
{
  "name": "Alice Smith",
  "email": "alice@example.com"
}
```

Entire resource is replaced.

If fields are omitted, they may be overwritten depending on implementation.

---

# PUT Architecture

```
Existing User

↓

Replace Entire Record

↓

Save

↓

Return Updated Resource
```

Example Response

```json
{
  "id": 25,
  "name": "Alice Smith",
  "email": "alice@example.com"
}
```

---

# PATCH Method

PATCH modifies only specific fields.

Example

```
PATCH /users/25
```

Request

```json
{
  "email": "alice.new@example.com"
}
```

Only the email changes.

Everything else remains unchanged.

---

# PATCH Architecture

```
Current User

 │

 ▼

Update Email

 │

 ▼

Save

 │

 ▼

Return Updated User
```

PATCH is generally preferred for partial updates because it minimizes data transfer and reduces the risk of unintentionally overwriting fields.

---

# PUT vs PATCH

| PUT | PATCH |
|------|--------|
| Full replacement | Partial update |
| Entire resource sent | Changed fields only |
| Larger payload | Smaller payload |
| Idempotent | Usually idempotent when implemented correctly |
| May overwrite missing fields | Updates specified fields only |

Example

PUT

```json
{
  "name":"Alice",
  "email":"alice@example.com",
  "phone":"9876543210"
}
```

PATCH

```json
{
  "phone":"9876543210"
}
```

---

# DELETE Method

DELETE removes a resource.

Example

```
DELETE /users/15
```

Architecture

```
Client

 │

DELETE

 ▼

API

 │

Delete Record

 ▼

Database

 │

Success

 ▼

Response
```

Typical Response

```
204 No Content
```

Some APIs instead return:

```
200 OK
```

with confirmation details.

---

# HEAD Method

HEAD behaves similarly to GET but returns only response headers.

Example

```
HEAD /products
```

Response

```
Headers Only

No Response Body
```

Uses

- Checking file size
- Cache validation
- Health checks
- Metadata retrieval

---

# OPTIONS Method

OPTIONS returns information about supported operations.

Example

```
OPTIONS /users
```

Response

```
Allow:

GET

POST

PUT

DELETE
```

This method is heavily used during **CORS preflight requests**.

---

# TRACE Method

TRACE returns the received request for diagnostic purposes.

```
TRACE /users
```

Most production servers disable TRACE because it can assist attackers during reconnaissance.

---

# CONNECT Method

CONNECT establishes a network tunnel through an HTTP proxy.

```
Client

 │

CONNECT

 ▼

Proxy

 │

Encrypted Tunnel

 ▼

Destination Server
```

This method is primarily used by proxy servers and is rarely implemented in REST APIs.

---

# Safe Methods

A safe method does **not modify server data**.

Safe Methods

```
GET

HEAD

OPTIONS
```

Unsafe Methods

```
POST

PUT

PATCH

DELETE
```

Safe methods should only retrieve information.

---

# Idempotent Methods

An idempotent method produces the same result even if executed multiple times.

Example

```
GET /users/15
```

Calling it 100 times returns the same resource.

```
GET

↓

Same Result

↓

Same Resource
```

---

# Idempotency Table

| Method | Safe | Idempotent |
|----------|------|------------|
| GET | Yes | Yes |
| POST | No | No |
| PUT | No | Yes |
| PATCH | No | Usually* |
| DELETE | No | Yes |
| HEAD | Yes | Yes |
| OPTIONS | Yes | Yes |

\*PATCH is commonly implemented to be idempotent, but this depends on the API's update logic.

---

# Why Idempotency Matters

Idempotency improves reliability.

Example:

```
Payment Request

↓

Network Failure

↓

Retry
```

If the operation is idempotent:

```
Only One Update
```

Without idempotency:

```
Duplicate Processing

↓

Duplicate Payment

↓

Business Loss
```

Many payment APIs use **Idempotency Keys** to safely retry requests.

---

# CRUD Mapping

REST naturally maps HTTP methods to CRUD operations.

| CRUD | HTTP Method |
|-------|-------------|
| Create | POST |
| Read | GET |
| Update | PUT / PATCH |
| Delete | DELETE |

Architecture

```
Create

↓

POST

──────────────

Read

↓

GET

──────────────

Update

↓

PUT / PATCH

──────────────

Delete

↓

DELETE
```

---

# Choosing the Correct Method

| Requirement | Recommended Method |
|--------------|-------------------|
| Retrieve users | GET |
| Create account | POST |
| Replace profile | PUT |
| Update password | PATCH |
| Delete order | DELETE |
| Retrieve headers | HEAD |
| Discover supported methods | OPTIONS |

Selecting the correct HTTP method improves API consistency and interoperability.

---

# Enterprise Example

A banking application may expose the following endpoints:

```
GET    /accounts

GET    /accounts/5001

POST   /payments

PATCH  /accounts/5001

PUT    /customers/120

DELETE /beneficiaries/8
```

Each endpoint combines a resource-oriented URI with the appropriate HTTP method to clearly express the intended operation.

---

# Common Mistakes

### Using GET for Updates

Incorrect

```
GET /updateBalance
```

Correct

```
PATCH /accounts/1001
```

---

### Using POST for Every Operation

Incorrect

```
POST /getUsers

POST /deleteUser

POST /updateProfile
```

Correct

```
GET /users

DELETE /users/25

PATCH /users/25
```

---

### Ignoring Idempotency

Using POST for operations that may be retried can lead to duplicate transactions if retries occur after network failures.

Design APIs with retries and idempotency in mind, especially for financial and transactional systems.

---

# Best Practices

- Use HTTP methods according to their intended semantics.
- Keep GET requests free of side effects.
- Use POST only for resource creation or non-idempotent operations.
- Use PUT for complete replacements.
- Use PATCH for partial updates.
- Use DELETE to remove resources.
- Support HEAD and OPTIONS where appropriate.
- Design idempotent operations for reliable retries.
- Return meaningful HTTP status codes.
- Document the behavior of every endpoint clearly.

---

# Key Takeaways

- HTTP methods define the action performed on a resource.
- REST separates resource identification (URI) from the operation (HTTP method).
- GET, POST, PUT, PATCH, and DELETE form the foundation of RESTful APIs.
- Safe methods do not modify server state, while idempotent methods produce consistent results across repeated requests.
- Proper use of HTTP methods improves API usability, reliability, and interoperability.
- Designing APIs with correct method semantics and idempotency is essential for enterprise-grade systems.

---

# HTTP Request Structure

Every interaction between a client and a REST API begins with an **HTTP request**.

An HTTP request contains all the information required for the server to understand what the client wants to do.

A typical request consists of:

- Request Line
- HTTP Headers
- Optional Request Body

Architecture

```
                HTTP Request

+------------------------------------------+
| Request Line                             |
+------------------------------------------+
| Headers                                  |
+------------------------------------------+
| Blank Line                               |
+------------------------------------------+
| Request Body (Optional)                  |
+------------------------------------------+
```

The server processes the request and generates an HTTP response.

---

# HTTP Request Lifecycle

```
Client

   │

Create HTTP Request

   │

DNS Resolution

   │

TCP Connection

   │

TLS Handshake (HTTPS)

   │

Send Request

   ▼

REST API

   │

Authentication

   │

Authorization

   │

Validation

   │

Business Logic

   │

Database

   │

Generate Response

   ▼

Client
```

Every API request follows this general lifecycle.

---

# Request Line

The first line of an HTTP request contains three components.

```
GET /users/101 HTTP/1.1
```

Components

| Component | Description |
|-----------|-------------|
| GET | HTTP Method |
| /users/101 | Request URI |
| HTTP/1.1 | HTTP Version |

Example

```
POST /orders HTTP/1.1
```

This indicates:

- Method → POST
- Resource → /orders
- Protocol → HTTP/1.1

---

# Request Headers

Headers provide additional information about the request.

Example

```
GET /users HTTP/1.1

Host: api.company.com

Authorization: Bearer <JWT>

Accept: application/json

User-Agent: Mozilla/5.0
```

Headers do not usually contain business data.

Instead, they describe how the request should be processed.

---

# Common Request Headers

| Header | Purpose |
|----------|----------|
| Host | Target server |
| Authorization | Authentication token |
| Accept | Expected response format |
| Content-Type | Format of request body |
| User-Agent | Client information |
| Cookie | Session data |
| Origin | Browser origin |
| Referer | Previous page |
| Accept-Language | Preferred language |
| Cache-Control | Cache behavior |

Many security mechanisms rely heavily on HTTP headers.

---

# Authorization Header

The Authorization header carries authentication credentials.

Example

```
Authorization: Bearer eyJhbGciOiJIUzI1...
```

Other examples:

```
Authorization: Basic username:password
```

```
Authorization: ApiKey xxxxxxxxx
```

Proper validation of this header is critical for API security.

---

# Accept Header

The client tells the server which response format it prefers.

Example

```
Accept: application/json
```

Other examples

```
Accept: application/xml
```

```
Accept: text/plain
```

The server attempts to return data in one of the requested formats.

---

# Content-Type Header

Content-Type specifies the format of the request body.

Example

```
Content-Type: application/json
```

Common values

```
application/json

application/xml

multipart/form-data

application/x-www-form-urlencoded

text/plain
```

Servers validate the body according to this header.

---

# User-Agent Header

Identifies the client software.

Example

```
User-Agent:

Mozilla/5.0
```

Other examples

```
curl

PostmanRuntime

Python Requests

Java HttpClient
```

Many organizations analyze User-Agent values during threat detection.

---

# Request Body

The request body contains data sent to the server.

Usually used with:

- POST
- PUT
- PATCH

Example

```json
{
    "name": "Alice",
    "email": "alice@example.com"
}
```

GET requests generally do not include a request body.

---

# JSON Payload

JSON has become the standard payload format for REST APIs.

Example

```json
{
    "id": 101,
    "product": "Laptop",
    "price": 85000,
    "quantity": 2
}
```

Advantages

- Human readable
- Lightweight
- Widely supported
- Easy to parse
- Language independent

---

# XML Payload

Some enterprise systems continue using XML.

Example

```xml
<User>
    <Name>Alice</Name>
    <Email>alice@example.com</Email>
</User>
```

XML is still common in:

- Legacy systems
- Banking
- Telecommunications
- SOAP services

---

# Multipart Requests

Used primarily for file uploads.

Example

```
POST /upload

Content-Type:

multipart/form-data
```

Body

```
Image

Document

Metadata
```

Common use cases

- Profile pictures
- PDFs
- Videos
- Medical images

---

# HTTP Response Structure

After processing the request, the server returns a response.

Architecture

```
              HTTP Response

+----------------------------------+
| Status Line                      |
+----------------------------------+
| Response Headers                 |
+----------------------------------+
| Blank Line                       |
+----------------------------------+
| Response Body                    |
+----------------------------------+
```

---

# Status Line

Example

```
HTTP/1.1 200 OK
```

Components

| Component | Description |
|-----------|-------------|
| HTTP/1.1 | HTTP Version |
| 200 | Status Code |
| OK | Status Message |

---

# Response Headers

Examples

```
Content-Type: application/json

Cache-Control: no-cache

Server: nginx

Content-Length: 235
```

Response headers provide metadata about the returned data.

---

# Response Body

Contains the requested resource or an error message.

Example

```json
{
    "id": 101,
    "name": "Alice",
    "email": "alice@example.com"
}
```

---

# HTTP Status Codes

HTTP status codes indicate the result of processing a request.

Categories

| Range | Meaning |
|---------|---------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Errors |
| 5xx | Server Errors |

---

# 1xx Informational

Examples

```
100 Continue

101 Switching Protocols

102 Processing
```

Rarely seen in everyday REST APIs.

---

# 2xx Success

Common success codes

| Status Code | Meaning |
|--------------|----------|
| 200 OK | Successful request |
| 201 Created | Resource created |
| 202 Accepted | Processing later |
| 204 No Content | Successful without response body |

Example

```
POST /users

↓

201 Created
```

---

# 3xx Redirection

Examples

```
301 Moved Permanently

302 Found

304 Not Modified

307 Temporary Redirect

308 Permanent Redirect
```

REST APIs generally use redirects less frequently than web browsers.

---

# 4xx Client Errors

Common client-side errors

| Code | Meaning |
|-------|----------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 406 | Not Acceptable |
| 408 | Request Timeout |
| 409 | Conflict |
| 415 | Unsupported Media Type |
| 422 | Unprocessable Content |
| 429 | Too Many Requests |

These usually indicate issues with the client's request.

---

# 5xx Server Errors

Common server-side errors

| Code | Meaning |
|-------|----------|
| 500 | Internal Server Error |
| 501 | Not Implemented |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

These errors indicate failures on the server or infrastructure.

---

# Content Negotiation

Content negotiation allows clients and servers to agree on the data format.

Example

Client

```
Accept: application/json
```

Server

```
Content-Type: application/json
```

Another example

Client

```
Accept: application/xml
```

Server

```
Content-Type: application/xml
```

This mechanism improves interoperability between diverse clients.

---

# Standard Error Response

Well-designed APIs return structured error messages.

Example

```json
{
    "timestamp": "2026-07-29T12:30:00Z",
    "status": 404,
    "error": "Not Found",
    "message": "User does not exist",
    "path": "/users/500"
}
```

Benefits

- Easier debugging
- Better automation
- Consistent error handling
- Improved developer experience

---

# Enterprise Request Example

```
POST /payments HTTP/1.1

Host: api.bank.com

Authorization: Bearer <JWT>

Content-Type: application/json

Accept: application/json
```

Body

```json
{
    "fromAccount": "1001",
    "toAccount": "2002",
    "amount": 5000,
    "currency": "INR"
}
```

Response

```
HTTP/1.1 201 Created
```

```json
{
    "transactionId": "TX982734",
    "status": "SUCCESS"
}
```

---

# Common Mistakes

### Missing Content-Type

Incorrect

```
POST /users
```

No Content-Type specified.

Correct

```
Content-Type: application/json
```

---

### Incorrect Status Codes

Returning

```
200 OK
```

for every operation reduces clarity.

Use appropriate status codes.

Examples

```
201 Created

204 No Content

404 Not Found

409 Conflict
```

---

### Returning Sensitive Errors

Avoid exposing:

- Database names
- Stack traces
- SQL queries
- Internal IP addresses
- File paths
- Framework versions

Instead, return generic client-facing errors while logging detailed information internally.

---

# REST Response Best Practices

- Return appropriate HTTP status codes.
- Use JSON consistently unless another format is required.
- Keep responses concise.
- Avoid exposing internal implementation details.
- Include meaningful error messages.
- Support content negotiation where appropriate.
- Use caching headers when applicable.
- Document all response formats.
- Ensure consistent response structures across endpoints.
- Log errors internally without leaking sensitive information.

---

# Key Takeaways

- HTTP requests consist of a request line, headers, and an optional body.
- HTTP responses include a status line, headers, and an optional response body.
- Headers carry metadata that influences request processing and response handling.
- JSON is the dominant representation format for REST APIs, while XML remains common in some enterprise environments.
- HTTP status codes communicate the outcome of a request and should be used consistently.
- Content negotiation enables clients and servers to exchange data in mutually supported formats.
- Structured error responses and consistent response design improve usability, security, and maintainability.

---

**Next:** REST API Security, Stateless Authentication, Caching, Versioning, Pagination, Filtering, HATEOAS, Best Practices, Hands-on Labs, Troubleshooting, and Interview Questions.