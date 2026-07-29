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

**Next:** GraphQL Schema Design, Relationships, Introspection, Fragments, Variables, Directives, Query Execution, and Enterprise GraphQL Architecture.