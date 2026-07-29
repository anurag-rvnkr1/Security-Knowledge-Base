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

# Rate Limiting

Rate limiting controls how many requests a client can send within a specified time period.

It protects APIs against:

- Denial-of-Service (DoS)
- Brute-force attacks
- Credential stuffing
- API abuse
- Resource exhaustion
- Unexpected traffic spikes

Without rate limiting, a single client could overwhelm backend services.

---

# Why Rate Limiting Matters

Without Rate Limiting

```
Attacker

    │

100,000 Requests

    │

    ▼

API Gateway

    │

Backend Overloaded

    ▼

Service Failure
```

With Rate Limiting

```
Attacker

    │

100,000 Requests

    │

    ▼

API Gateway

    │

Requests Exceed Limit?

    │

    ▼

Reject Excess Requests

    ▼

Backend Protected
```

---

# Rate Limiting Workflow

```
Client

   │

API Request

   ▼

Gateway

   │

Identify Client

   │

Check Limit

   │

Allowed?

 ┌───┴────┐

 ▼        ▼

Yes      No

 ▼        ▼

Forward  HTTP 429
```

---

# Rate Limiting Components

```
Client Identity

       │

       ▼

Counter

       │

Time Window

       │

Decision Engine

       │

Allow / Reject
```

---

# Client Identification

Clients may be identified using:

- IP Address
- API Key
- JWT Subject (`sub`)
- OAuth Client ID
- User ID
- Device ID
- Mutual TLS Certificate

Choosing the correct identifier is critical for effective rate limiting.

---

# Rate Limit Dimensions

Limits may be enforced per:

- User
- API Key
- Endpoint
- Organization
- Tenant
- Region
- IP Address
- Authentication Level

Example

```
100 Requests

Per Minute

Per User
```

---

# Rate Limiting Policies

Examples

```
100 Requests / Minute
```

```
1000 Requests / Hour
```

```
50 Login Attempts / Hour
```

```
5 Password Reset Requests / Day
```

Different endpoints often require different limits.

---

# HTTP 429

When limits are exceeded,

the gateway typically returns:

```
HTTP/1.1 429

Too Many Requests
```

The response may include retry information.

Example headers

```
Retry-After: 60
```

```
X-RateLimit-Limit: 100
```

```
X-RateLimit-Remaining: 0
```

---

# Fixed Window Algorithm

The Fixed Window algorithm counts requests within a fixed time interval.

```
Minute 1

██████████

100 Requests

----------------

Minute 2

Counter Reset
```

Advantages

- Simple
- Fast
- Easy to implement

Limitations

- Traffic bursts at window boundaries

---

# Fixed Window Example

```
Limit

100 Requests

──────────────

12:00 - 12:01

Counter = 100

──────────────

12:01

Counter Reset
```

A client may effectively send nearly double the configured rate around the reset boundary.

---

# Sliding Window Algorithm

The Sliding Window algorithm continuously evaluates requests over the previous time interval.

```
Previous 60 Seconds

██████████████

Moving Window

██████████████
```

Advantages

- Smoother request distribution
- Fairer enforcement
- Better burst protection

---

# Sliding Window Workflow

```
New Request

      │

Check Previous

60 Seconds

      │

Within Limit?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject
```

---

# Token Bucket Algorithm

A bucket contains tokens.

Each request consumes one token.

Tokens refill over time.

```
Bucket

██████████

10 Tokens

      │

Request

      ▼

9 Tokens

      │

Refill

      ▼

10 Tokens
```

---

# Token Bucket Characteristics

Advantages

- Allows controlled bursts
- Efficient
- Widely used
- Flexible refill rates

Ideal for APIs with intermittent traffic spikes.

---

# Leaky Bucket Algorithm

Requests enter a queue.

The queue processes requests at a constant rate.

```
Incoming Requests

████████████

       │

 Leaky Bucket

       │

Constant Output

████
```

Advantages

- Smooth traffic
- Prevent sudden bursts
- Predictable backend load

---

# Token Bucket vs Leaky Bucket

| Token Bucket | Leaky Bucket |
|--------------|--------------|
| Allows bursts | Smooths bursts |
| Flexible | Constant output |
| Tokens replenish | Queue drains |
| Popular for APIs | Popular for traffic shaping |

---

# Distributed Rate Limiting

Large deployments require shared counters across multiple gateway instances.

```
Gateway A

      │

Gateway B

      │

Gateway C

      │

Shared Counter Store

      │

Decision
```

Common shared stores

- Redis
- Distributed Cache
- Cloud-managed key-value stores

---

# Rate Limiting in Kubernetes

```
Internet

     │

Ingress Controller

     │

API Gateway

     │

Redis Counter Store

     │

Pods
```

Shared counters ensure consistent enforcement across replicas.

---

# Authentication-Aware Rate Limiting

Authenticated users may receive higher limits.

Example

| Client Type | Requests/Minute |
|-------------|----------------:|
| Anonymous | 30 |
| Authenticated | 300 |
| Premium | 1000 |
| Internal Service | 5000 |

---

# Endpoint-Specific Limits

Different endpoints require different policies.

| Endpoint | Recommended Limit |
|-----------|------------------:|
| Login | 5/minute |
| Password Reset | 3/hour |
| User Search | 100/minute |
| Public API | 500/minute |
| Payment API | 20/minute |

Sensitive endpoints should have stricter limits.

---

# Adaptive Rate Limiting

Adaptive rate limiting adjusts thresholds based on current conditions.

Factors

- CPU utilization
- Memory usage
- Backend latency
- Error rate
- Active sessions

```
System Healthy

      │

Higher Threshold

---------------------

System Busy

      │

Lower Threshold
```

---

# Quotas

Quotas define long-term usage limits.

Examples

```
100,000 Requests

Per Month
```

```
1,000 API Calls

Per Day
```

Quotas differ from short-term rate limits.

---

# Rate Limiting vs Quotas

| Rate Limiting | Quotas |
|---------------|---------|
| Short-term | Long-term |
| Protects infrastructure | Controls consumption |
| Seconds or minutes | Days or months |
| Limits bursts | Limits total usage |

---

# Burst Control

Controlled bursts improve user experience.

```
Configured Rate

100/minute

Burst Capacity

20 Requests
```

Burst allowances should remain within backend capacity.

---

# Traffic Shaping

Traffic shaping controls how requests are processed.

Examples

- Queue requests
- Delay requests
- Prioritize requests
- Reject requests

```
Incoming Traffic

        │

Traffic Shaper

        │

Priority Queue

        ▼

Backend
```

---

# Request Prioritization

```
Premium Users

       │

Highest Priority

---------------------

Authenticated Users

---------------------

Anonymous Users
```

Critical business operations may receive preferential treatment.

---

# Circuit Breaker Pattern

Circuit breakers prevent repeated requests to failing services.

```
Gateway

 │

Backend Failure

 │

Open Circuit

 │

Reject Requests

 │

Recovery Check

 │

Close Circuit
```

Benefits

- Protects backend systems
- Reduces cascading failures
- Improves resilience

---

# Circuit Breaker States

```
Closed

   │

Failures

   ▼

Open

   │

Recovery Timeout

   ▼

Half-Open

   │

Success?

 ┌──┴────┐

 ▼       ▼

Yes      No

 ▼       ▼

Closed  Open
```

---

# Retry Policies

Gateways may retry transient failures.

Best practices

- Retry idempotent operations
- Use exponential backoff
- Apply retry limits
- Avoid retry storms

Retries should never amplify outages.

---

# Timeout Management

Appropriate timeout values prevent resource exhaustion.

```
Client Timeout

      │

Gateway Timeout

      │

Backend Timeout
```

Timeouts should be coordinated across all layers.

---

# Web Application Firewall (WAF) Integration

Many enterprise deployments position a WAF before the API Gateway.

```
Internet

     │

     ▼

Web Application Firewall

     │

API Gateway

     │

Backend APIs
```

The WAF blocks malicious traffic before it reaches the gateway.

---

# WAF Responsibilities

Examples

- SQL Injection detection
- Cross-Site Scripting detection
- Bot mitigation
- IP reputation
- Geo-blocking
- Request normalization
- Virtual patching

---

# WAF and API Gateway Comparison

| WAF | API Gateway |
|-----|-------------|
| Detects web attacks | Routes API traffic |
| Blocks malicious payloads | Authenticates clients |
| Virtual patching | Authorizes requests |
| Threat intelligence | Rate limiting |
| Bot protection | API transformations |

They complement each other rather than replace one another.

---

# Enterprise API Security Architecture

```
                  Internet

                      │

                      ▼

            DDoS Protection

                      │

                      ▼

         Web Application Firewall

                      │

                      ▼

               API Gateway

      ┌─────────┼──────────┬───────────┐

      ▼         ▼          ▼

 Authentication Authorization Rate Limiting

      │         │          │

      └─────────┼──────────┘

                ▼

         Service Mesh

                │

      ┌─────────┼─────────┐

      ▼         ▼         ▼

  User API  Order API  Payment API

                │

                ▼

            Databases
```

---

# Best Practices

Rate Limiting

- Use endpoint-specific limits.
- Apply adaptive policies.
- Protect authentication endpoints.
- Monitor rejected requests.
- Test policies under load.

Gateway

- Enable distributed counters.
- Use shared storage for limits.
- Configure circuit breakers.
- Apply reasonable timeouts.
- Integrate with a WAF.

Operations

- Review limits periodically.
- Monitor API growth.
- Tune burst capacity.
- Document gateway policies.

---

# Common Security Mistakes

Avoid

- Using identical limits for every endpoint
- Applying limits only by IP address
- Ignoring authenticated identities
- Missing distributed synchronization
- Unlimited retry attempts
- No timeout configuration
- No circuit breaker
- Missing WAF integration
- Excessively permissive burst limits
- Lack of monitoring for HTTP 429 events

---

# Key Takeaways

- Rate limiting protects APIs from abuse and resource exhaustion.
- Fixed Window, Sliding Window, Token Bucket, and Leaky Bucket are common algorithms.
- Distributed rate limiting is essential for horizontally scaled gateways.
- Circuit breakers and retries improve resilience when implemented correctly.
- WAFs and API Gateways work together to provide layered API security.

---

**Next:** Logging, Monitoring, Observability, Distributed Tracing, Metrics, Detection Engineering, SIEM Integration, Hands-on Labs, Troubleshooting, Interview Questions, and Enterprise API Gateway Operations.