# 05 - GraphQL Security

# Introduction

GraphQL is a modern API query language and runtime developed by Facebook (now Meta) to address many of the limitations of traditional REST APIs.

Unlike REST, where clients interact with multiple endpoints, GraphQL exposes a **single endpoint** that allows clients to request exactly the data they need.

This approach reduces:

- Over-fetching
- Under-fetching
- Multiple network requests
- Client-side complexity

GraphQL has become widely adopted by organizations building modern web, mobile, and cloud-native applications.

Examples include:

- GitHub
- Shopify
- Netflix
- Airbnb
- Meta
- Pinterest
- Atlassian

Although GraphQL offers tremendous flexibility, it also introduces unique security challenges that differ significantly from REST and SOAP.

Understanding GraphQL security is essential for:

- API Security Engineers
- Penetration Testers
- SOC Analysts
- DevSecOps Engineers
- Backend Developers
- Cloud Security Engineers

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand GraphQL fundamentals.
- Learn GraphQL architecture.
- Understand schemas and type systems.
- Differentiate queries, mutations, and subscriptions.
- Understand GraphQL resolvers.
- Learn GraphQL execution flow.
- Identify GraphQL attack surfaces.
- Understand GraphQL authentication and authorization.
- Learn GraphQL security best practices.
- Perform GraphQL security assessments.

---

# What is GraphQL?

GraphQL is both:

- A query language for APIs.
- A runtime for executing those queries.

Instead of exposing many endpoints like REST,

```
/users

/orders

/products

/payments
```

GraphQL exposes one endpoint.

```
/graphql
```

Clients specify exactly which fields they want.

---

# Why GraphQL Was Created

REST APIs often require multiple requests to gather related information.

Example

```
GET /users/100

↓

GET /orders/100

↓

GET /payments/100
```

GraphQL allows all required information to be retrieved with a single request.

```
POST /graphql

↓

Single Query

↓

Single Response
```

This reduces latency and network overhead.

---

# REST vs GraphQL

REST

```
Multiple Endpoints

↓

Fixed Responses

↓

Over-fetching Possible
```

GraphQL

```
Single Endpoint

↓

Flexible Queries

↓

Exact Data Returned
```

---

# GraphQL Architecture

```
                Client

                   │

          GraphQL Query

                   ▼

          GraphQL Server

                   │

              Resolvers

                   │

     ┌─────────────┼─────────────┐

     ▼             ▼             ▼

 User DB      Product DB    Payment DB

                   │

                   ▼

          GraphQL Response
```

The GraphQL server processes queries using **Resolvers**, which retrieve data from one or more data sources.

---

# GraphQL Components

A GraphQL system consists of:

- Schema
- Types
- Queries
- Mutations
- Subscriptions
- Resolvers
- Scalars
- Directives

Each component contributes to the overall functionality of the API.

---

# GraphQL Schema

The schema defines everything the API supports.

It specifies:

- Available data types
- Queries
- Mutations
- Relationships
- Fields

The schema acts as the contract between clients and the server.

Example

```
Schema

│

├────────► User

├────────► Product

├────────► Order

└────────► Payment
```

---

# GraphQL Type System

GraphQL is strongly typed.

Example

```graphql
type User {

    id: ID!

    name: String!

    email: String!

}
```

Common scalar types include:

- String
- Int
- Float
- Boolean
- ID

Applications can also define custom types.

---

# Object Types

Objects represent business entities.

Example

```graphql
type Product {

    id: ID!

    name: String!

    price: Float!

}
```

Objects can reference other objects.

Example

```
User

↓

Orders

↓

Products
```

This enables rich relationships between entities.

---

# GraphQL Queries

Queries retrieve data.

Example

```graphql
query {

    user(id: 100) {

        name

        email

    }

}
```

Response

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com"
    }
  }
}
```

Queries should not modify server data.

---

# GraphQL Mutations

Mutations modify data.

Example

```graphql
mutation {

    createUser(

        name:"Alice"

    ) {

        id

    }

}
```

Typical operations:

- Create
- Update
- Delete

Mutations are conceptually similar to:

```
POST

PUT

PATCH

DELETE
```

in REST.

---

# GraphQL Subscriptions

Subscriptions enable real-time communication.

Architecture

```
Client

 │

Subscribe

 ▼

GraphQL Server

 │

Real-Time Events

 ▼

Client
```

Typical use cases:

- Chat applications
- Live dashboards
- Stock prices
- Notifications
- IoT monitoring

Subscriptions commonly use WebSockets instead of HTTP polling.

---

# GraphQL Resolvers

Resolvers execute business logic.

Example

```
Query

↓

Resolver

↓

Database

↓

Response
```

Each requested field may invoke one or more resolvers.

Resolvers are responsible for:

- Fetching data
- Validation
- Authorization
- Business logic
- Error handling

Poorly designed resolvers are a common source of GraphQL vulnerabilities.

---

# GraphQL Execution Flow

```
Client

 │

GraphQL Query

 ▼

Schema Validation

 │

Authorization

 │

Resolver Execution

 │

Database

 │

Generate Response

 ▼

Client
```

Each stage provides opportunities for validation and security enforcement.

---

# GraphQL Request Example

```http
POST /graphql

Content-Type: application/json
```

Body

```json
{
  "query": "{ user(id:100){ name email } }"
}
```

The entire GraphQL query is transmitted within the request body.

---

# GraphQL Response Example

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com"
    }
  }
}
```

Unlike REST, GraphQL always returns a response object with structured data and, when applicable, an `errors` field.

---

# Advantages of GraphQL

Benefits include:

- Single endpoint
- Flexible queries
- Reduced bandwidth usage
- Strong type system
- Self-documenting schema
- Efficient mobile applications
- Better developer experience
- Reduced over-fetching
- Reduced under-fetching

These characteristics make GraphQL attractive for modern applications.

---

# Disadvantages of GraphQL

Challenges include:

- Complex authorization
- Difficult caching
- Query complexity attacks
- Deep nesting attacks
- Resource exhaustion
- Increased monitoring complexity
- Larger attack surface
- More difficult rate limiting

Security controls must account for these characteristics.

---

# Enterprise Example

A global e-commerce platform exposes a GraphQL API.

```
Customer

     │

GraphQL Query

     ▼

GraphQL Gateway

     │

Resolvers

     │

 ┌────┼────────────┐

 ▼    ▼            ▼

Users Orders Products

     │

     ▼

GraphQL Response
```

Instead of calling three REST endpoints, the client retrieves all required information using one GraphQL query.

---

# Key Takeaways

- GraphQL is a query language and runtime for APIs.
- It exposes a single endpoint instead of multiple REST endpoints.
- Clients request exactly the data they require.
- The schema defines the API contract.
- Queries retrieve data, mutations modify data, and subscriptions enable real-time communication.
- Resolvers execute business logic and are central to GraphQL processing.
- GraphQL improves flexibility but introduces unique security challenges that require specialized protections.

---

# GraphQL Schema Design

A GraphQL schema defines the complete structure of a GraphQL API.

It specifies:

- Available object types
- Fields
- Relationships
- Queries
- Mutations
- Subscriptions
- Input types
- Scalar types
- Enums
- Interfaces
- Unions

The schema acts as the contract between clients and servers.

Unlike REST, where documentation is often external, GraphQL APIs are largely self-describing through their schemas.

---

# GraphQL Schema Architecture

```
                 GraphQL Schema

                       │

     ┌─────────────────┼─────────────────┐

     ▼                 ▼                 ▼

   Types            Operations       Relationships

     │                 │                 │

     ▼                 ▼                 ▼

 Objects          Query/Mutation     Nested Objects
```

Every GraphQL request is validated against the schema before execution.

---

# Root Types

Every GraphQL schema begins with one or more root operation types.

```
Schema

│

├────────► Query

├────────► Mutation

└────────► Subscription
```

These act as entry points into the GraphQL API.

---

# Query Root

The Query root exposes read operations.

Example

```graphql
type Query {

    user(id: ID!): User

    product(id: ID!): Product

    orders: [Order]

}
```

Clients begin all read operations here.

---

# Mutation Root

Mutations perform write operations.

Example

```graphql
type Mutation {

    createUser(input: UserInput!): User

    updateUser(id: ID!): User

    deleteUser(id: ID!): Boolean

}
```

Mutations should change application state.

---

# Subscription Root

Subscriptions provide real-time communication.

Example

```graphql
type Subscription {

    orderCreated: Order

}
```

Applications receive updates whenever subscribed events occur.

---

# Scalar Types

GraphQL includes built-in scalar types.

| Scalar | Description |
|----------|-------------|
| Int | Integer |
| Float | Decimal Number |
| String | Text |
| Boolean | True/False |
| ID | Unique Identifier |

Example

```graphql
type User {

    id: ID!

    age: Int

    salary: Float

}
```

---

# Custom Scalars

Applications often define custom scalar types.

Example

```graphql
scalar Date

scalar Email

scalar URL

scalar UUID
```

These improve validation and consistency.

---

# Input Types

Input types define structured data accepted by mutations.

Example

```graphql
input UserInput {

    name: String!

    email: String!

}
```

Mutation

```graphql
createUser(input: UserInput!)
```

Input types improve readability and validation.

---

# Object Relationships

GraphQL naturally models relationships.

Example

```graphql
type User {

    id: ID!

    name: String!

    orders: [Order]

}
```

```
User

 │

 ▼

Orders

 │

 ▼

Products
```

Nested relationships reduce the number of requests required.

---

# One-to-One Relationship

Example

```
User

↓

Profile
```

Schema

```graphql
type User {

    profile: Profile

}
```

---

# One-to-Many Relationship

Example

```
Customer

↓

Orders
```

Schema

```graphql
type Customer {

    orders: [Order]

}
```

---

# Many-to-Many Relationship

Example

```
Student

↓

Courses

↓

Teachers
```

GraphQL handles complex relationships efficiently through nested resolvers.

---

# Nested Queries

One of GraphQL's strengths is retrieving related data in a single request.

Example

```graphql
query {

    user(id:100){

        name

        orders{

            id

            total

        }

    }

}
```

Response

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "orders": [
        {
          "id": 10,
          "total": 500
        }
      ]
    }
  }
}
```

---

# Deeply Nested Queries

GraphQL supports deep nesting.

Example

```
User

↓

Orders

↓

Products

↓

Reviews

↓

Authors
```

While powerful, excessive nesting can create significant performance and security risks.

---

# Fragments

Fragments allow reusable field selections.

Without fragments

```graphql
query {

    user{

        id

        name

        email

    }

}
```

With fragments

```graphql
fragment UserFields on User {

    id

    name

    email

}
```

Used by

```graphql
query{

    user{

        ...UserFields

    }

}
```

Fragments reduce duplication and improve maintainability.

---

# Variables

Variables make GraphQL queries reusable.

Instead of

```graphql
user(id:100)
```

Use

```graphql
query GetUser($id: ID!) {

    user(id:$id){

        name

    }

}
```

Variables

```json
{
  "id":100
}
```

Benefits

- Reusable queries
- Better caching
- Cleaner client code
- Reduced string manipulation

---

# Aliases

Aliases rename returned fields.

Example

```graphql
query {

    customer:user(id:1){

        name

    }

}
```

Response

```json
{
  "data": {
    "customer": {
      "name": "Alice"
    }
  }
}
```

Aliases improve readability when querying similar fields multiple times.

---

# Directives

Directives modify query execution.

Common directives

```
@include

@skip

@deprecated
```

Example

```graphql
query {

    user{

        name

        email @include(if:true)

    }

}
```

Directives allow dynamic query behavior.

---

# Interfaces

Interfaces define common fields shared by multiple object types.

Example

```graphql
interface Person {

    id: ID!

    name: String!

}
```

Implemented by

```
Customer

Employee

Vendor
```

Interfaces encourage consistent API design.

---

# Union Types

Union types allow fields to return multiple object types.

Example

```
Search Result

↓

User

OR

Product

OR

Order
```

This is useful for search functionality and polymorphic responses.

---

# Enums

Enums define a fixed set of allowed values.

Example

```graphql
enum Role {

    ADMIN

    USER

    AUDITOR

}
```

Enums reduce invalid inputs and improve validation.

---

# Schema Validation

Every incoming GraphQL query is validated before execution.

Validation checks include:

- Valid syntax
- Existing fields
- Valid arguments
- Correct types
- Authorization (where implemented)

```
Query

 │

 ▼

Schema Validation

 │

 ├── Valid

 │      ▼

 │   Execute

 │

 └── Invalid

        ▼

     Return Error
```

Validation prevents many malformed requests from reaching business logic.

---

# GraphQL Introspection

One of GraphQL's most powerful features is **Introspection**.

It allows clients to discover:

- Available queries
- Available mutations
- Types
- Fields
- Directives
- Documentation

Example

```graphql
{
  __schema {
    types {
      name
    }
  }
}
```

Tools such as GraphiQL, Apollo Studio, and GraphQL Playground rely on introspection to provide auto-completion and documentation.

---

# Benefits of Introspection

Advantages include:

- Self-documenting APIs
- Automatic client generation
- Developer productivity
- Schema discovery
- IDE support
- API exploration

For internal APIs, introspection greatly improves developer experience.

---

# Risks of Introspection

If exposed in production, introspection may reveal:

- Hidden object types
- Administrative operations
- Internal field names
- Deprecated functionality
- Business relationships
- Sensitive schema details

Example

```
Attacker

 │

Introspection Query

 ▼

Complete Schema

 │

Endpoint Enumeration

 ▼

Targeted Attacks
```

Many organizations disable or restrict introspection in production environments.

---

# Query Execution Process

```
Client

 │

GraphQL Query

 ▼

Parser

 │

Schema Validation

 │

Authentication

 │

Authorization

 │

Resolver Execution

 │

Database Calls

 │

Assemble Response

 ▼

Client
```

Each stage should include appropriate validation and security checks.

---

# Resolver Execution

Resolvers are executed for each requested field.

Example

```
Query

 │

User Resolver

 │

Order Resolver

 │

Product Resolver

 ▼

Response
```

Poorly optimized resolvers can create unnecessary database queries and increase latency.

---

# N+1 Query Problem

One of the most common GraphQL performance issues is the **N+1 Query Problem**.

Example

```
Get 100 Users

↓

For Each User

↓

Query Orders

↓

100 Additional Queries
```

Total

```
101 Database Queries
```

Instead of

```
2 Efficient Queries
```

Solutions include:

- DataLoader
- Batch loading
- Query optimization
- Efficient database joins
- Caching

---

# Enterprise GraphQL Architecture

```
                 Internet

                     │

                     ▼

                Load Balancer

                     │

                     ▼

                API Gateway

                     │

                     ▼

              Authentication

                     │

                     ▼

              GraphQL Server

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

 User Service   Product Service  Order Service

      │              │              │

      └──────────────┼──────────────┘

                     ▼

                Databases

                     │

                     ▼

            Logging & Monitoring

                     │

                     ▼

                 SIEM / SOC
```

This architecture enables centralized security, routing, and observability while supporting distributed backend services.

---

# Enterprise Best Practices

Schema Design

- Keep schemas simple and intuitive.
- Use descriptive type names.
- Prefer reusable input types.
- Minimize deeply nested relationships.
- Deprecate fields instead of removing them abruptly.

Performance

- Batch resolver calls.
- Cache frequently accessed data.
- Limit query depth.
- Limit query complexity.
- Paginate large collections.

Security

- Validate all inputs.
- Enforce authentication.
- Authorize every resolver.
- Restrict introspection in production when appropriate.
- Monitor resolver execution times.

---

# Common Mistakes

Avoid:

- Exposing unnecessary fields
- Unlimited query depth
- Missing input validation
- Weak authorization checks
- Excessive resolver logic
- Unrestricted introspection
- Poor naming conventions
- Ignoring N+1 query problems
- Returning sensitive internal errors

---

# Key Takeaways

- The GraphQL schema defines the complete API contract.
- Root types provide entry points for queries, mutations, and subscriptions.
- Object relationships enable powerful nested data retrieval.
- Fragments, variables, aliases, and directives improve flexibility and maintainability.
- Introspection makes GraphQL self-documenting but should be carefully managed in production.
- Efficient resolver design and query optimization are essential for performance and security.

---

# GraphQL Authentication

Authentication verifies the identity of the client before allowing access to GraphQL resources.

Unlike REST, GraphQL typically exposes a **single endpoint**, meaning authentication must be enforced consistently regardless of which query or mutation is executed.

Common authentication mechanisms include:

- JWT (JSON Web Token)
- OAuth 2.0
- OpenID Connect (OIDC)
- API Keys
- Session Cookies
- Mutual TLS (mTLS)

---

# Authentication Flow

```
Client

   │

Login

   │

   ▼

Identity Provider

   │

Generate Token

   ▼

Client

   │

Authorization Header

   ▼

GraphQL Server

   │

Validate Token

   ▼

Authenticated Request
```

Authentication occurs before GraphQL query execution.

---

# JWT Authentication

JWT is the most common authentication mechanism.

Example

```
Authorization:

Bearer eyJhbGciOi...
```

Workflow

```
User Login

    │

Generate JWT

    │

Store Token

    │

Include in Every Request

    │

Server Validation

    ▼

Execute Query
```

JWTs should:

- Have short expiration times
- Use secure signing algorithms
- Be validated on every request
- Be transmitted only over HTTPS

---

# Session-Based Authentication

Some enterprise applications still use sessions.

```
Client

 │

Login

 ▼

Session Cookie

 │

Every Request

 ▼

GraphQL Server
```

Advantages

- Easy session invalidation
- Mature ecosystem
- Widely supported

Disadvantages

- Stateful infrastructure
- Session storage required

---

# API Key Authentication

Applications sometimes authenticate using API keys.

Example

```
X-API-Key:

abc123xyz456
```

API keys identify applications rather than individual users.

Best practices

- Rotate regularly
- Store securely
- Apply rate limits
- Monitor usage
- Restrict by IP where appropriate

---

# OAuth 2.0

OAuth allows delegated authorization.

```
User

 │

Login

 ▼

Authorization Server

 │

Access Token

 ▼

GraphQL API
```

OAuth is commonly used for:

- Mobile applications
- Third-party integrations
- Enterprise SSO
- Cloud applications

---

# Authentication Middleware

Authentication should occur before GraphQL execution.

```
Incoming Request

      │

Authentication Middleware

      │

 ├── Invalid

 │      ▼

 │   Reject Request

 │

 └── Valid

        ▼

Schema Validation

        ▼

Resolvers
```

Unauthenticated requests should never reach sensitive business logic.

---

# Authorization

Authentication identifies the user.

Authorization determines what that user is allowed to access.

Every GraphQL resolver should perform authorization checks.

```
Authenticated User

        │

Permission Check

        │

Allowed?

   ┌────┴────┐

  Yes       No

   │         │

Execute    Reject
```

Authorization must be enforced even if authentication succeeds.

---

# Why Authorization Is Critical

Consider this query.

```graphql
query {

    user(id:100){

        name

        salary

        ssn

    }

}
```

Authentication alone is insufficient.

The resolver must determine whether the requester is authorized to access:

- Salary
- Social Security Number
- Financial information
- Administrative fields

---

# Resolver-Level Authorization

Every resolver should verify permissions.

Example

```
Query

 │

Resolver

 │

Authorization Check

 │

Database

 ▼

Response
```

Authorization should not rely solely on frontend controls.

---

# Role-Based Access Control (RBAC)

Roles determine accessible operations.

Example

```
Administrator

↓

Full Access
```

```
Manager

↓

Department Access
```

```
Customer

↓

Own Data Only
```

Resolvers should verify roles before returning data.

---

# Attribute-Based Access Control (ABAC)

Authorization decisions may depend on multiple attributes.

Examples

- Department
- Country
- Clearance Level
- Time of Day
- Device Type
- Project Membership

Example

```
Employee

+

Finance Department

+

Business Hours

↓

Approve Payment
```

ABAC enables fine-grained authorization.

---

# Field-Level Authorization

One of GraphQL's biggest security challenges is field-level authorization.

Example

```graphql
query{

    employee{

        name

        email

        salary

    }

}
```

The resolver must determine which fields the requester can access.

Example

```
HR

↓

Salary Visible
```

```
Employee

↓

Salary Hidden
```

Authorization decisions may differ for each field.

---

# Object-Level Authorization

Users should access only permitted objects.

Example

Incorrect

```
User A

↓

Reads User B Account
```

Correct

```
User A

↓

Own Account Only
```

Resolvers should verify ownership before returning objects.

---

# Broken Object Level Authorization (BOLA)

BOLA is one of the most common GraphQL vulnerabilities.

Example

```graphql
query{

    order(id:500){

        total

    }

}
```

If the server checks only authentication,

```
Attacker

↓

Change ID

↓

Read Another Customer's Order
```

Proper ownership validation prevents this attack.

---

# Broken Function Level Authorization (BFLA)

Example

```graphql
mutation{

    deleteUser(id:100)
}
```

If any authenticated user can execute this mutation,

```
Regular User

↓

Administrative Mutation

↓

Unauthorized Action
```

Resolvers must verify privileges before executing sensitive operations.

---

# GraphQL Introspection Security

Introspection provides valuable documentation but may expose sensitive information.

Example

```graphql
{
    __schema{
        types{
            name
        }
    }
}
```

Attackers can discover:

- Administrative mutations
- Hidden object types
- Internal fields
- Business relationships
- Deprecated operations

---

# Restricting Introspection

Development

```
Introspection

↓

Enabled
```

Production

```
Public APIs

↓

Restricted or Disabled
```

Many organizations disable introspection for public production environments while keeping it enabled internally for trusted developers.

---

# GraphQL Playground Security

GraphQL Playground, GraphiQL, and Apollo Sandbox provide interactive interfaces.

Benefits

- Auto-completion
- Documentation
- Query testing
- Developer productivity

Risks

- Endpoint discovery
- Schema enumeration
- Administrative operation discovery
- Easier attacker reconnaissance

Interactive tools should not be publicly exposed without proper authentication.

---

# Query Complexity Attacks

One of GraphQL's unique attack vectors is excessive query complexity.

Example

```
User

↓

Orders

↓

Products

↓

Reviews

↓

Authors

↓

Comments

↓

Likes

↓

Profiles
```

A single request may trigger hundreds or thousands of backend operations.

---

# Query Depth Attack

Attackers intentionally create deeply nested queries.

Example

```
User

↓

Orders

↓

Products

↓

Reviews

↓

Author

↓

Orders

↓

Products

↓

Reviews
```

This recursive structure can consume excessive CPU and memory.

---

# Query Cost Analysis

Modern GraphQL servers often calculate query cost before execution.

```
Incoming Query

 │

Cost Calculator

 │

 ├── Cost < Limit

 │        ▼

 │    Execute

 │

 └── Cost > Limit

          ▼

      Reject Query
```

This prevents expensive operations from overwhelming backend services.

---

# Query Depth Limiting

Depth limiting prevents excessive nesting.

Example

```
Maximum Depth

=

10 Levels
```

Request

```
Depth

=

25 Levels

↓

Rejected
```

Depth limits reduce denial-of-service risks.

---

# Alias Abuse

Aliases allow multiple requests within a single GraphQL query.

Example

```graphql
query{

    user1:user(id:1){name}

    user2:user(id:2){name}

    user3:user(id:3){name}

}
```

Large numbers of aliases may generate many resolver executions.

Mitigation

- Alias limits
- Query cost analysis
- Rate limiting

---

# Batching Attacks

Some GraphQL servers accept batched requests.

Example

```
Request

↓

500 Queries

↓

Single HTTP Request
```

Attackers may use batching to bypass traditional rate limiting.

Mitigations

- Disable unnecessary batching
- Apply per-operation limits
- Rate limit at resolver level
- Monitor unusual query volume

---

# Denial-of-Service (DoS)

GraphQL DoS attacks commonly exploit:

- Deep nesting
- Expensive resolvers
- Large responses
- Recursive queries
- Alias abuse
- Batching
- Complex filtering

```
Attacker

 │

Expensive Query

 ▼

Resolvers

 ▼

Database

 ▼

Resource Exhaustion
```

---

# Secure Resolver Design

Resolvers should:

- Validate input
- Enforce authorization
- Limit returned fields
- Use parameterized queries
- Batch database requests
- Handle errors safely
- Log security events
- Avoid unnecessary computation

Resolvers represent the primary security boundary within GraphQL.

---

# Input Validation

Validate every argument.

Example

```graphql
query{

    user(id:"abc")
}
```

Validation should verify:

- Type
- Length
- Format
- Range
- Allowed values

Never trust client-provided input.

---

# Error Handling

Avoid exposing internal implementation details.

Incorrect

```json
{
    "errors":[
        {
            "message":"SQL Exception in UserResolver.java line 152"
        }
    ]
}
```

Correct

```json
{
    "errors":[
        {
            "message":"Unable to process request."
        }
    ]
}
```

Detailed errors should be logged internally rather than returned to clients.

---

# Logging and Monitoring

Security-relevant events should be logged.

Examples

Authentication

- Failed logins
- Token validation failures

Authorization

- Access denied
- Privilege escalation attempts

GraphQL

- Expensive queries
- Deep queries
- Alias abuse
- Introspection attempts
- Batch requests

Infrastructure

- High latency
- Server errors
- Resource exhaustion

These logs support detection engineering and incident response.

---

# Detection Engineering

Security teams should monitor for:

| Detection | Indicator |
|-----------|-----------|
| Excessive Query Depth | Nested queries beyond policy |
| High Query Cost | Queries exceeding complexity thresholds |
| Alias Abuse | Large number of aliases in a request |
| Introspection Attempts | Repeated `__schema` or `__type` queries |
| Authentication Failures | Repeated invalid tokens |
| Authorization Failures | Multiple denied resolver executions |
| Batch Abuse | Excessive operations in a single request |
| DoS Activity | High CPU, memory, or resolver latency |

Alerts should be correlated with source IPs, user identities, and application logs.

---

# SIEM Integration

Typical GraphQL events forwarded to a SIEM include:

```
Authentication Logs

        │

Authorization Logs

        │

Resolver Execution Logs

        │

GraphQL Audit Logs

        │

Infrastructure Metrics

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

Useful detection rules include:

- Multiple failed authentication attempts
- High-frequency introspection queries
- Repeated authorization failures
- Abnormally expensive queries
- Sudden spikes in mutation execution
- Large-scale data extraction patterns

---

# Enterprise GraphQL Security Architecture

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

          Authentication Middleware

                      │

                      ▼

             GraphQL Server

                      │

        Query Cost & Depth Analysis

                      │

          Resolver Authorization

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

 User Service    Product Service   Order Service

                      │

                      ▼

                 Databases

                      │

                      ▼

            Logging & Monitoring

                      │

                      ▼

                 SIEM / SOC
```

This layered architecture helps protect GraphQL APIs against both application-layer attacks and infrastructure abuse.

---

# Enterprise Best Practices

Authentication

- Enforce HTTPS.
- Validate tokens on every request.
- Use short-lived access tokens.
- Rotate secrets regularly.

Authorization

- Verify permissions in every resolver.
- Implement object-level and field-level authorization.
- Follow the principle of least privilege.

Performance

- Limit query depth.
- Enforce query complexity limits.
- Cache frequently accessed data.
- Batch resolver operations.

Operations

- Disable or restrict introspection where appropriate.
- Secure developer tools.
- Monitor expensive queries.
- Log all security-relevant events.
- Perform regular security testing.

---

# Common Security Mistakes

Avoid:

- Missing resolver authorization
- Broken object-level authorization (BOLA)
- Unlimited query depth
- Unlimited query complexity
- Public introspection in production
- Exposed GraphQL Playground
- Returning verbose error messages
- Missing rate limiting
- Excessive resolver database calls
- Lack of monitoring and alerting

---

# Key Takeaways

- Authentication verifies identity, while authorization determines permitted actions.
- Authorization must be enforced at the resolver, object, and field levels.
- GraphQL introduces unique attack vectors such as introspection abuse, query complexity attacks, deep nesting, alias abuse, and batching attacks.
- Query cost analysis and depth limiting are essential security controls.
- Secure resolver design, comprehensive logging, and SIEM integration are critical for enterprise GraphQL deployments.

---

**Next:** GraphQL Vulnerability Assessment, Penetration Testing Methodology, Common Exploitation Techniques, Secure Development Practices, Hands-on Labs, Troubleshooting, Interview Questions, and Chapter Summary.