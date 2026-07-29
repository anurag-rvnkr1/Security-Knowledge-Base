# 14 - API Gateways

# Introduction

An API Gateway is a centralized entry point that manages, secures, and routes API requests between clients and backend services.

Instead of exposing every backend service directly to the Internet, clients communicate with the API Gateway, which performs authentication, authorization, routing, monitoring, and other cross-cutting concerns before forwarding requests.

API Gateways are fundamental components of:

- Microservices
- Cloud-native applications
- Kubernetes
- Enterprise APIs
- Mobile backends
- SaaS platforms
- Zero Trust architectures

A properly configured API Gateway improves:

- Security
- Scalability
- Performance
- Observability
- Reliability
- Governance

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand API Gateway fundamentals.
- Learn gateway architecture.
- Understand request routing.
- Explore authentication and authorization.
- Learn rate limiting.
- Understand caching.
- Explore request transformation.
- Learn load balancing.
- Understand service discovery.
- Perform API Gateway security assessments.

---

# What is an API Gateway?

An API Gateway acts as the front door for API traffic.

```
Client

   │

   ▼

API Gateway

   │

 ┌─┼─────────────┐

 ▼ ▼             ▼

Service A    Service B    Service C
```

The gateway becomes the single entry point for all client requests.

---

# Why Use an API Gateway?

Without an API Gateway

```
Client

 │

 ├────────────► Service A

 ├────────────► Service B

 ├────────────► Service C

 └────────────► Service D
```

Problems

- Multiple public endpoints
- Duplicate security logic
- Inconsistent authentication
- Difficult monitoring
- Increased attack surface

---

# With an API Gateway

```
Client

 │

 ▼

API Gateway

 │

 ├────────► Service A

 ├────────► Service B

 ├────────► Service C

 └────────► Service D
```

Benefits

- Centralized security
- Unified authentication
- Simplified routing
- Better observability
- Easier policy management

---

# API Gateway Responsibilities

Primary responsibilities include:

- Request routing
- Authentication
- Authorization
- SSL/TLS termination
- Rate limiting
- Request validation
- Response transformation
- Load balancing
- Caching
- Logging
- Monitoring

---

# API Gateway Architecture

```
                 Internet

                    │

                    ▼

              API Gateway

       ┌────────┼─────────┐

       ▼        ▼         ▼

 Authentication Routing Policies

       │        │         │

       └────────┼─────────┘

                ▼

          Backend Services

                │

                ▼

             Databases
```

---

# Request Lifecycle

```
Client

 │

HTTPS Request

 ▼

API Gateway

 │

Authentication

 │

Authorization

 │

Routing

 │

Backend Service

 │

Response

 ▼

Client
```

Every request passes through the gateway before reaching backend services.

---

# Request Routing

Routing determines which backend service receives a request.

Example

```
/users

↓

User Service
```

```
/orders

↓

Order Service
```

```
/payments

↓

Payment Service
```

Routing policies should be deterministic and easy to maintain.

---

# Path-Based Routing

```
/users/*

↓

User Service
```

```
/inventory/*

↓

Inventory Service
```

```
/billing/*

↓

Billing Service
```

One of the most common routing strategies.

---

# Host-Based Routing

Example

```
api.company.com

↓

Core API
```

```
admin.company.com

↓

Administration API
```

Useful for separating business domains.

---

# Header-Based Routing

Headers can influence routing decisions.

Example

```
Version: v2

↓

API Version 2
```

or

```
Region: Asia

↓

Asia Cluster
```

---

# Method-Based Routing

Requests may be routed according to the HTTP method.

Example

```
GET

↓

Read Cluster
```

```
POST

↓

Write Cluster
```

Useful for read/write separation.

---

# Authentication at the Gateway

The gateway commonly performs authentication before forwarding requests.

Supported methods

- JWT
- OAuth 2.0
- OpenID Connect
- API Keys
- Mutual TLS
- Basic Authentication (legacy)

---

# Authentication Flow

```
Client

 │

JWT

 ▼

API Gateway

 │

Validate Signature

 │

Authenticated

 ▼

Backend Service
```

Backend services can trust authenticated requests forwarded by the gateway.

---

# Authorization

The gateway may perform authorization checks.

Examples

- Scope validation
- Role validation
- API subscription validation
- IP restrictions
- Tenant validation

```
JWT

 │

Scopes

 │

Permission Check

 ▼

Allow / Deny
```

---

# API Key Validation

```
Request

 │

API Key

 ▼

Gateway

 │

Lookup

 │

Valid?

 ┌────┴─────┐

 ▼          ▼

Yes        No

 ▼          ▼

Route     Reject
```

API keys should be rotated periodically.

---

# Mutual TLS (mTLS)

API Gateways often support mutual TLS.

```
Client

 │

Client Certificate

 ▼

Gateway

 │

Certificate Validation

 ▼

Backend
```

mTLS is common in service-to-service communication.

---

# SSL/TLS Termination

Many gateways terminate TLS connections.

```
Client

 │

HTTPS

 ▼

Gateway

 │

Decrypt

 │

Internal Network

 ▼

Service
```

Internal communication may also remain encrypted depending on organizational requirements.

---

# Load Balancing

The gateway distributes requests across backend instances.

```
             Gateway

                │

     ┌──────────┼──────────┐

     ▼          ▼          ▼

 Instance1  Instance2  Instance3
```

Benefits

- High availability
- Better utilization
- Fault tolerance

---

# Load Balancing Algorithms

Common algorithms

| Algorithm | Description |
|-----------|-------------|
| Round Robin | Sequential distribution |
| Least Connections | Fewest active connections |
| Weighted Round Robin | Capacity-aware routing |
| Random | Random selection |
| Hash-Based | Consistent routing |

Choice depends on workload characteristics.

---

# Health Checks

Gateways monitor backend availability.

```
Gateway

 │

Health Check

 │

Healthy?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Route    Remove Instance
```

Unhealthy services should not receive traffic.

---

# Service Discovery

Dynamic environments require automatic service discovery.

```
Gateway

 │

Service Registry

 │

Current Instances

 ▼

Route Request
```

Common in Kubernetes and cloud-native platforms.

---

# Static vs Dynamic Routing

| Static Routing | Dynamic Routing |
|----------------|-----------------|
| Manual configuration | Automatic discovery |
| Simpler | Scalable |
| Less flexible | Cloud-native |
| Suitable for small deployments | Preferred for microservices |

---

# API Versioning

Gateways often manage API versions.

Examples

```
/v1/users
```

```
/v2/users
```

or

```
Header

API-Version: 2
```

Versioning minimizes disruption while introducing new features.

---

# Request Transformation

Gateways can modify incoming requests.

Examples

- Add headers
- Remove headers
- Rewrite URLs
- Normalize payloads
- Inject correlation IDs

---

# Response Transformation

Responses may also be modified.

Examples

- Remove internal fields
- Standardize error messages
- Convert data formats
- Add response headers
- Compress payloads

---

# Protocol Translation

Gateways can bridge different protocols.

```
REST Client

      │

API Gateway

      │

gRPC Service
```

or

```
REST

↓

SOAP
```

This simplifies client integration.

---

# Caching

Frequently requested responses may be cached.

```
Client

 │

Gateway Cache

 │

Cache Hit?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Return   Backend
```

Caching reduces latency and backend load.

---

# Cache Benefits

Advantages

- Lower latency
- Reduced backend traffic
- Improved scalability
- Better user experience
- Reduced infrastructure cost

Only cache responses that are appropriate for reuse.

---

# Enterprise API Gateway Architecture

```
                    Internet

                        │

                        ▼

                 Web Application Firewall

                        │

                        ▼

                    API Gateway

      ┌───────────┼──────────────┐

      ▼           ▼              ▼

 Authentication Authorization Rate Limiting

      │           │              │

      └───────────┼──────────────┘

                  ▼

            Load Balancer

                  │

        ┌─────────┼─────────┐

        ▼         ▼         ▼

   User API   Order API  Payment API

                  │

                  ▼

              Databases
```

---

# Best Practices

Architecture

- Use the gateway as the single public entry point.
- Separate internal and external APIs.
- Apply Zero Trust principles.
- Use service discovery for dynamic environments.

Security

- Enforce HTTPS.
- Validate JWTs.
- Enable mTLS where appropriate.
- Rotate API keys.
- Validate input before forwarding.

Operations

- Monitor gateway health.
- Enable structured logging.
- Configure health checks.
- Test failover regularly.

---

# Common Security Mistakes

Avoid

- Exposing backend services directly
- Skipping authentication
- Missing authorization checks
- Trusting client headers without validation
- Weak TLS configuration
- Missing health checks
- Unlimited request sizes
- Inconsistent routing rules
- Lack of monitoring
- Hardcoded gateway secrets

---

# Key Takeaways

- API Gateways centralize API security and traffic management.
- Authentication and authorization are commonly enforced at the gateway.
- Gateways support routing, caching, load balancing, and protocol translation.
- Service discovery enables dynamic routing in cloud-native environments.
- Centralized governance improves scalability, visibility, and security.

---

**Next:** Rate Limiting, Traffic Shaping, Throttling, Quotas, Circuit Breakers, Web Application Firewall (WAF) Integration, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.