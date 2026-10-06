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

# GraphQL Vulnerability Assessment

GraphQL security assessments differ significantly from traditional REST API testing.

Because GraphQL exposes a single endpoint with a flexible query language, security testing focuses on:

- Schema discovery
- Authentication
- Authorization
- Resolver security
- Query complexity
- Introspection
- Business logic
- Input validation
- Data exposure

A comprehensive assessment should evaluate both the GraphQL engine and the underlying business logic.

---

# GraphQL Security Assessment Methodology

A structured methodology improves consistency and coverage.

```
Reconnaissance

      │

      ▼

Endpoint Discovery

      │

      ▼

Schema Enumeration

      │

      ▼

Authentication Testing

      │

      ▼

Authorization Testing

      │

      ▼

Input Validation

      │

      ▼

Business Logic Testing

      │

      ▼

DoS Testing

      │

      ▼

Reporting
```

Each phase builds upon the previous one.

---

# Phase 1 – Endpoint Discovery

Unlike REST APIs with multiple endpoints, GraphQL commonly exposes one endpoint.

Common endpoint names

```
/graphql

/api/graphql

/graphql/v1

/api

/query

/gql
```

Discovery methods include:

- Public documentation
- Mobile applications
- JavaScript source code
- Network traffic
- Browser Developer Tools
- API documentation
- Reverse engineering

---

# Phase 2 – Identify GraphQL

Indicators include:

HTTP Request

```http
POST /graphql
```

JSON Body

```json
{
    "query":"{__typename}"
}
```

Typical response

```json
{
    "data":{
        "__typename":"Query"
    }
}
```

This confirms GraphQL support.

---

# Phase 3 – Introspection Testing

Determine whether introspection is enabled.

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

Possible outcomes

```
Success

↓

Schema Exposed
```

or

```
Access Denied

↓

Introspection Restricted
```

If enabled, enumerate:

- Queries
- Mutations
- Types
- Fields
- Directives
- Input Objects
- Enums

---

# Phase 4 – Schema Enumeration

Collect information such as:

```
User

Admin

Product

Payment

Invoice

Customer
```

Document:

- Object types
- Relationships
- Administrative operations
- Deprecated fields
- Sensitive objects

This helps identify high-value attack targets.

---

# Phase 5 – Authentication Testing

Verify whether authentication is required.

Test:

- Anonymous queries
- Expired tokens
- Invalid JWTs
- Missing tokens
- Session handling
- API keys

Example

```
Authorization

↓

Missing

↓

401 Unauthorized
```

Unexpected success indicates a serious security issue.

---

# Phase 6 – Authorization Testing

Authorization is one of the highest-risk areas.

Test whether users can access:

- Other users' records
- Administrative fields
- Sensitive mutations
- Internal objects
- Restricted reports

Example

```graphql
query{

    user(id:200){

        salary

    }

}
```

Determine whether ownership and permissions are enforced.

---

# Broken Object Level Authorization (BOLA)

GraphQL is susceptible to BOLA when resolvers fail to validate ownership.

Attack

```
Customer A

↓

Order ID 100
```

Modify

```
Order ID 101
```

Possible result

```
Customer B Order
```

Expected behavior

```
403 Forbidden
```

or equivalent authorization error.

---

# Broken Function Level Authorization (BFLA)

Administrative mutations should be restricted.

Example

```graphql
mutation{

    deleteUser(id:100)

}
```

Verify that only authorized roles can execute sensitive operations.

---

# Phase 7 – Input Validation Testing

Test every argument.

Examples

```
Very Long Strings

Negative Numbers

Special Characters

Unicode

Null Values

Unexpected Types

Boundary Values
```

Goal

Determine whether validation occurs before resolver execution.

---

# SQL Injection Testing

Resolvers frequently interact with databases.

Test inputs such as:

```
'

"

--

OR 1=1

UNION
```

Applications should use:

- Parameterized queries
- ORM protections
- Input validation

Never concatenate user input directly into SQL statements.

---

# NoSQL Injection Testing

Applications using MongoDB or similar databases require separate testing.

Example payloads

```json
{
    "$ne": null
}
```

or

```json
{
    "$gt":""
}
```

Verify that resolvers reject malicious operators where appropriate.

---

# Command Injection Testing

Resolvers may invoke operating system commands.

Example payload

```
;

&&

|

`

$()
```

Secure applications avoid passing untrusted input to system commands.

---

# XML Injection

If GraphQL integrates with SOAP or XML-based services, test for:

- XML Injection
- XXE
- XPath Injection

Input validation and secure XML parser configuration are essential.

---

# Server-Side Request Forgery (SSRF)

Resolvers sometimes fetch external resources.

Example

```graphql
mutation{

    importURL(url:"https://example.com")

}
```

Potential attack

```
Attacker

↓

Internal URL

↓

Cloud Metadata

↓

Sensitive Information
```

Validate URLs and restrict outbound network access.

---

# File Upload Testing

Some GraphQL implementations support file uploads.

Verify:

- File type validation
- File size limits
- Malware scanning
- Filename sanitization
- Storage security

Large uploads should be rate limited.

---

# Query Depth Testing

Attempt progressively deeper queries.

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

Followers
```

Expected result

```
Depth Limit

Exceeded

↓

Rejected
```

Unlimited nesting may lead to resource exhaustion.

---

# Query Complexity Testing

Construct increasingly expensive queries.

```
Single Query

↓

Hundreds of Resolvers

↓

Database Calls

↓

High CPU

↓

High Memory
```

Servers should reject overly expensive requests.

---

# Alias Abuse Testing

Aliases can multiply resolver executions.

Example

```graphql
query{

    u1:user(id:1){name}

    u2:user(id:2){name}

    u3:user(id:3){name}

}
```

Attempt large numbers of aliases to determine whether server-side limits exist.

---

# Batch Request Testing

Some implementations allow multiple operations per request.

```
One HTTP Request

↓

500 Operations

↓

Server Load
```

Verify:

- Batch size limits
- Authentication enforcement
- Rate limiting
- Logging

---

# Denial-of-Service Testing

Assess resource exhaustion risks.

Potential vectors

- Deep queries
- Recursive queries
- Large responses
- Alias abuse
- Batch abuse
- Expensive filters
- Complex sorting

Testing should be carefully controlled in authorized environments to avoid disrupting production systems.

---

# Business Logic Testing

Business logic flaws cannot be detected automatically.

Examples

- Purchase negative quantities
- Skip payment steps
- Reuse discount codes
- Bypass workflow approval
- Modify completed orders
- Cancel shipped products
- Access hidden discounts

These issues often have significant business impact.

---

# Sensitive Data Exposure

Review responses for unnecessary information.

Potential exposure

- Password hashes
- API keys
- JWT secrets
- Internal IDs
- Email addresses
- Financial records
- Debug messages
- Stack traces

GraphQL responses should contain only the fields requested and authorized.

---

# Error Handling Assessment

Incorrect

```json
{
    "errors":[
        {
            "message":"SQL Exception in UserResolver.java line 250"
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

Detailed diagnostics belong in server logs rather than client responses.

---

# Logging Assessment

Verify that the application logs:

Authentication

- Successful logins
- Failed logins
- Token validation failures

Authorization

- Access denied
- Privilege violations

GraphQL

- Introspection attempts
- Expensive queries
- Alias abuse
- Batch requests

Infrastructure

- CPU utilization
- Memory utilization
- Database latency

Comprehensive logging supports incident response and forensic analysis.

---

# Detection Engineering

Recommended detection rules

| Detection | Indicator |
|-----------|-----------|
| Introspection Abuse | Repeated `__schema` or `__type` queries |
| High Query Cost | Cost exceeds configured threshold |
| Deep Nesting | Query depth beyond policy |
| Alias Abuse | Excessive aliases in one request |
| Batch Abuse | Large number of operations per request |
| Authorization Failures | Repeated access denials |
| SSRF Attempts | Requests targeting internal or metadata addresses |
| File Upload Abuse | Repeated oversized or unsupported uploads |

Detection rules should be tuned to reduce false positives while identifying genuine attacks.

---

# SIEM Integration

Security telemetry should include:

```
Authentication Logs

        │

Authorization Logs

        │

GraphQL Query Logs

        │

Resolver Metrics

        │

Infrastructure Metrics

        ▼

SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

High-value alerts include:

- Excessive failed authentication attempts
- Introspection from untrusted sources
- High-cost query spikes
- Repeated authorization failures
- Unusual mutation activity
- Resource exhaustion indicators

---

# Enterprise Assessment Workflow

```
Planning

    │

Reconnaissance

    │

Schema Discovery

    │

Authentication Review

    │

Authorization Testing

    │

Input Validation

    │

Business Logic Review

    │

Performance Testing

    │

Risk Assessment

    │

Reporting

    ▼

Remediation
```

A structured workflow improves repeatability and reporting quality.

---

# Hands-on Lab 1 – Identify a GraphQL Endpoint

Objective

Identify and verify a GraphQL endpoint in an authorized testing environment.

Steps

1. Inspect application network traffic.
2. Locate requests sent to a GraphQL endpoint.
3. Confirm GraphQL by sending a simple query such as retrieving `__typename` where permitted.
4. Record endpoint behavior, authentication requirements, and response format.

Learning Outcomes

- GraphQL endpoint discovery
- Basic protocol identification
- Request and response analysis

---

# Hands-on Lab 2 – Authorization Review

Objective

Verify object-level and field-level authorization.

Steps

1. Authenticate as a standard user.
2. Request only resources that should be accessible to that user.
3. Verify that administrative fields and other users' data remain inaccessible.
4. Document any unexpected access.

Learning Outcomes

- Resolver authorization analysis
- Ownership verification
- Least-privilege validation

---

# Hands-on Lab 3 – Query Limit Verification

Objective

Confirm that query depth and complexity protections are implemented.

Steps

1. Review server documentation or configuration where available.
2. Send increasingly nested but authorized queries within acceptable testing limits.
3. Observe when requests are rejected based on depth or complexity.
4. Record configured thresholds and server behavior.

Learning Outcomes

- Query depth controls
- Complexity analysis
- Resource protection mechanisms

---

# Common Security Mistakes

Avoid:

- Public introspection in production
- Missing resolver authorization
- Unlimited query depth
- Unlimited query complexity
- Excessive alias usage
- Missing rate limiting
- Weak input validation
- Verbose error messages
- Exposed developer tools
- Missing security monitoring

---

# Troubleshooting

## Authentication Failure

Possible causes

- Missing token
- Invalid signature
- Expired token
- Incorrect authentication scheme

---

## Authorization Failure

Possible causes

- Missing role
- Incorrect ownership checks
- Resolver authorization logic
- Policy misconfiguration

---

## Query Rejected

Possible causes

- Query depth exceeded
- Query cost exceeded
- Validation error
- Unsupported field

---

## Slow Query Execution

Possible causes

- N+1 query problem
- Inefficient resolvers
- Missing caching
- Database latency

---

## File Upload Failure

Possible causes

- Unsupported file type
- File size limit exceeded
- Storage permissions
- Validation failure

---

# Interview Questions

## Fundamental

1. What is GraphQL?
2. How does GraphQL differ from REST?
3. What is a GraphQL schema?
4. What are resolvers?
5. What is introspection?
6. What are queries, mutations, and subscriptions?
7. Why is field-level authorization important?
8. What is query complexity?
9. What is query depth?
10. Why is GraphQL more susceptible to BOLA?

---

## Intermediate

11. How would you secure a GraphQL API?
12. Explain resolver-level authorization.
13. How would you prevent alias abuse?
14. What is the N+1 query problem?
15. How would you implement query cost analysis?
16. Why should introspection be restricted in production?
17. How would you test GraphQL authentication?
18. How would you detect GraphQL abuse in a SIEM?
19. Explain GraphQL batching attacks.
20. What are common GraphQL business logic vulnerabilities?

---

## Scenario-Based

**Scenario 1**

A production GraphQL API experiences a sudden increase in CPU utilization.

- Which GraphQL-specific attack vectors would you investigate first?
- Which logs and metrics would help determine whether the cause is expensive queries, deep nesting, or alias abuse?

---

**Scenario 2**

During an assessment, you discover that an authenticated user can retrieve another customer's order by modifying an object identifier.

- Which OWASP API Security risk does this represent?
- How would you verify and remediate the issue?

---

**Scenario 3**

Your organization is deploying a public GraphQL API.

- Which controls would you implement before production release?
- How would you balance developer usability with production security?

---

# Chapter Summary

In this chapter, we examined GraphQL security assessment methodologies and common attack vectors.

We covered:

- GraphQL assessment methodology
- Endpoint discovery
- Schema enumeration
- Authentication testing
- Authorization testing
- Input validation
- Query depth and complexity testing
- Alias and batching abuse
- Business logic assessment
- Error handling
- Logging
- Detection engineering
- SIEM integration
- Hands-on exercises
- Troubleshooting
- Interview preparation

GraphQL's flexibility offers significant benefits but also introduces unique security challenges. Effective security requires strong authentication, fine-grained authorization, query validation, resolver hardening, comprehensive monitoring, and continuous testing.

---

# Chapter Review

You should now be able to answer:

- How do you identify and assess a GraphQL endpoint?
- How should authentication and authorization be tested?
- What are GraphQL-specific attack vectors?
- Why are query depth and complexity limits important?
- How do alias abuse and batching attacks work?
- How should GraphQL APIs be monitored?
- Which events should be forwarded to a SIEM?
- How would you perform an enterprise GraphQL security assessment?

If you can confidently answer these questions, you are ready to continue with **Chapter 06 – gRPC Security**, where you'll explore modern high-performance APIs built on HTTP/2 and Protocol Buffers.

---

# References

## Standards

- GraphQL Specification
- GraphQL over HTTP Specification
- Protocol Buffers Language Guide (for comparison)
- RFC 9110 – HTTP Semantics

## Security Standards

- OWASP API Security Top 10
- OWASP ASVS
- OWASP Web Security Testing Guide (WSTG)
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53
- NIST SP 800-204

## Further Reading

- GraphQL Best Practices
- Apollo Security Documentation
- GraphQL Foundation Documentation
- DataLoader Documentation

---

# What's Next?

➡️ **Chapter 06 – gRPC Security**

In the next chapter, we will explore:

- gRPC architecture
- Protocol Buffers (Protobuf)
- HTTP/2 fundamentals
- Unary and streaming RPCs
- Service definitions
- Authentication and authorization
- TLS and mTLS
- gRPC attack surface
- Security best practices
- Enterprise deployments
- Hands-on labs and interview questions