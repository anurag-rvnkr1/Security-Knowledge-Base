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

**Next:** HTTP Methods in REST, Idempotency, Safe Methods, Request and Response Structure, Status Codes, Content Negotiation, and Enterprise REST Best Practices.