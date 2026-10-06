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

# Logging and Monitoring

Logging and monitoring are essential capabilities of an API Gateway.

Without proper visibility,

organizations cannot effectively:

- Detect attacks
- Investigate incidents
- Troubleshoot failures
- Measure performance
- Meet compliance requirements

An API Gateway should generate structured, centralized, and searchable logs.

---

# Why Monitoring Matters

Without Monitoring

```
API Failure

     │

Unknown Cause

     │

Extended Downtime

     ▼

Business Impact
```

With Monitoring

```
API Failure

     │

Alert Generated

     │

Root Cause Identified

     │

Rapid Recovery

     ▼

Minimal Impact
```

---

# Observability

Observability is the ability to understand the internal state of a system using external telemetry.

Three pillars of observability

```
             Observability

                  │

      ┌───────────┼────────────┐

      ▼           ▼            ▼

    Metrics      Logs       Traces
```

Together, they provide a complete operational view.

---

# Metrics

Metrics are numerical measurements collected over time.

Examples

- Requests per second (RPS)
- Response time
- Error rate
- CPU utilization
- Memory usage
- Active connections
- Cache hit ratio

Metrics help identify trends and anomalies.

---

# Common Gateway Metrics

| Metric | Purpose |
|---------|----------|
| Requests/sec | Traffic volume |
| Latency | Response performance |
| HTTP 2xx | Successful requests |
| HTTP 4xx | Client errors |
| HTTP 5xx | Server errors |
| Authentication Failures | Identity issues |
| Rate Limit Hits | Abuse detection |
| Cache Hit Ratio | Cache efficiency |

---

# Logs

Logs provide detailed records of events.

Example

```
Request Received

↓

Authentication Success

↓

Authorization Success

↓

Backend Response

↓

Response Returned
```

Logs enable forensic analysis after an incident.

---

# Structured Logging

Preferred format

```json
{
  "timestamp":"2026-07-29T12:00:00Z",
  "client_ip":"203.0.113.25",
  "method":"GET",
  "path":"/api/users",
  "status":200,
  "latency_ms":18
}
```

Structured logs are easier to search and analyze.

---

# Distributed Tracing

Distributed tracing follows a request across multiple services.

```
Client

  │

Gateway

  │

User Service

  │

Inventory Service

  │

Database
```

Every component contributes trace information.

---

# Trace Identifiers

Each request should receive a unique trace identifier.

```
Incoming Request

        │

Generate Trace ID

        │

Forward to Services

        │

Correlate Logs
```

This simplifies end-to-end troubleshooting.

---

# Correlation IDs

Correlation IDs connect logs generated by different components.

```
Gateway

   │

Correlation ID

   │

Service A

   │

Service B

   │

Database
```

Every log entry should include the same identifier.

---

# Health Monitoring

Gateways continuously monitor backend services.

Health checks verify:

- Availability
- Response time
- Error rate
- Resource utilization

```
Gateway

   │

Health Probe

   │

Healthy?

┌───┴────┐

▼        ▼

Yes      No

▼        ▼

Route    Remove
Traffic  Instance
```

---

# Synthetic Monitoring

Synthetic monitoring proactively tests APIs.

```
Monitoring Agent

      │

Scheduled Request

      │

API Gateway

      │

Expected Response?

┌─────┴─────┐

▼           ▼

Yes         No

▼           ▼

Healthy     Alert
```

This detects issues before customers report them.

---

# Service Level Indicators (SLIs)

SLIs measure service performance.

Examples

- Availability
- Latency
- Success rate
- Throughput

```
Availability

99.99%

Latency

35 ms
```

---

# Service Level Objectives (SLOs)

An SLO defines the desired service target.

Example

| Metric | Target |
|---------|--------|
| Availability | 99.95% |
| Latency | <100 ms |
| Error Rate | <0.5% |

SLOs guide operational priorities.

---

# Service Level Agreements (SLAs)

SLAs define contractual commitments to customers.

Example

```
Availability

99.9%

Monthly
```

Failure to meet an SLA may trigger financial or contractual consequences.

---

# Alerting

Monitoring systems generate alerts when thresholds are exceeded.

Examples

- High latency
- Authentication failures
- Elevated HTTP 500 responses
- CPU exhaustion
- Rate-limit spikes

```
Metric

    │

Threshold Exceeded

    │

Alert

    ▼

SOC / Operations
```

---

# Dashboarding

Dashboards provide a real-time operational view.

Typical widgets include

- Request volume
- Success rate
- Top endpoints
- Top clients
- Authentication failures
- Error trends
- Gateway health
- Backend health

---

# API Analytics

Analytics help understand API usage.

Examples

- Most used APIs
- Geographic distribution
- Peak traffic hours
- Consumer growth
- Version adoption
- Error distribution

These insights support capacity planning and product decisions.

---

# Detection Engineering

API Gateway logs are valuable for security monitoring.

Common detections

- Brute-force attacks
- Credential stuffing
- Token replay
- API enumeration
- SQL injection attempts
- Path traversal attempts
- Abnormal request rates
- Unauthorized access
- Suspicious geolocations
- Bot activity

---

# Detection Workflow

```
Gateway Logs

      │

Normalization

      │

Correlation

      │

Detection Rules

      │

Alert

      ▼

SOC Investigation
```

---

# Example Detection Rules

| Detection | Example Indicator |
|-----------|-------------------|
| Brute Force | Numerous failed login attempts |
| Token Replay | Same token used from different IP addresses |
| API Enumeration | Sequential requests to many endpoints |
| Rate Limit Abuse | Large number of HTTP 429 responses |
| SQL Injection | Database query manipulation patterns |
| Path Traversal | Requests containing traversal sequences |
| Authentication Bypass | Access without valid credentials |
| Privilege Escalation | Unexpected access to privileged endpoints |

---

# SIEM Integration

API Gateways should forward logs to a centralized SIEM.

```
               API Gateway

                    │

             Structured Logs

                    │

            Log Aggregation

                    │

                    ▼

                  SIEM

        ┌──────────┼───────────┐

        ▼          ▼           ▼

 Correlation   Detection   Dashboards

        │

        ▼

       SOC
```

---

# Recommended Log Sources

Collect logs from:

- API Gateway
- Web Application Firewall
- Identity Provider
- Reverse Proxy
- Load Balancer
- Kubernetes Ingress
- Application Services
- Databases
- Cloud Audit Logs

Centralized collection improves incident visibility.

---

# Correlation Examples

Example 1

```
Repeated Login Failures

          │

Successful Login

          │

Privilege Escalation

          ▼

SOC Alert
```

Example 2

```
Rate Limit Violations

          │

Token Replay

          │

Multiple Countries

          ▼

High Severity Alert
```

---

# Incident Investigation Workflow

```
Alert

 │

Review Logs

 │

Validate Indicators

 │

Determine Scope

 │

Contain

 │

Recover

 ▼

Lessons Learned
```

---

# Enterprise Monitoring Architecture

```
                 Internet

                     │

                     ▼

        Web Application Firewall

                     │

                     ▼

               API Gateway

                     │

     ┌───────────────┼───────────────┐

     ▼               ▼               ▼

   Metrics          Logs          Traces

     │               │               │

     └───────────────┼───────────────┘

                     ▼

             Observability Platform

                     │

                     ▼

                   SIEM

                     │

                     ▼

               Security Operations
```

---

# Hands-on Lab 1 – Gateway Log Analysis

**Objective**

Review API Gateway logs in an authorized lab.

**Steps**

1. Generate normal API requests.
2. Generate failed authentication attempts.
3. Review structured logs.
4. Identify authentication failures and response codes.

**Learning Outcomes**

- Structured logging
- Gateway visibility
- Security event analysis

---

# Hands-on Lab 2 – Trace Correlation

**Objective**

Follow a request through multiple services.

**Steps**

1. Generate a request with a trace identifier.
2. Locate the trace in gateway logs.
3. Follow the request across backend services.
4. Measure end-to-end latency.

**Learning Outcomes**

- Distributed tracing
- Correlation IDs
- Performance troubleshooting

---

# Hands-on Lab 3 – SIEM Correlation

**Objective**

Create API security detections.

**Steps**

1. Forward gateway logs to a SIEM.
2. Build a rule for repeated authentication failures.
3. Generate test events.
4. Validate that alerts are triggered correctly.

**Learning Outcomes**

- Detection engineering
- SIEM integration
- Alert validation

---

# Troubleshooting

## High Latency

Possible causes

- Backend performance issues
- Network congestion
- Database delays
- Inefficient caching
- Gateway overload

---

## Excessive HTTP 500 Responses

Possible causes

- Backend application failures
- Dependency outages
- Resource exhaustion
- Misconfigured routing

---

## Missing Logs

Possible causes

- Logging disabled
- Incorrect log forwarding
- Storage limitations
- SIEM ingestion failures

---

## Trace Correlation Failure

Possible causes

- Missing correlation IDs
- Trace propagation issues
- Clock synchronization problems
- Inconsistent logging formats

---

## Frequent Rate-Limit Alerts

Possible causes

- Legitimate traffic growth
- Misconfigured thresholds
- Automated clients
- Malicious activity

---

# Interview Questions

## Fundamental

1. What is an API Gateway?
2. Why are logs important?
3. What are the three pillars of observability?
4. What is a correlation ID?
5. What is distributed tracing?
6. What is an SLI?
7. What is an SLO?
8. What is an SLA?
9. Why is structured logging preferred?
10. Why should API Gateway logs be forwarded to a SIEM?

---

## Intermediate

11. How would you investigate API latency?
12. Explain distributed tracing in a microservices environment.
13. Which metrics are most useful for gateway monitoring?
14. How would you detect token replay?
15. How do correlation IDs simplify incident response?
16. What events should trigger gateway alerts?
17. How would you monitor rate-limit abuse?
18. Why is synthetic monitoring valuable?
19. What is the difference between metrics and logs?
20. How would you design an enterprise monitoring architecture for APIs?

---

## Scenario-Based

**Scenario 1**

Your SIEM reports a sharp increase in HTTP 429 responses from a single client over the past 10 minutes.

- What could explain this behavior?
- Which gateway logs and metrics would you review first?
- What containment actions might be appropriate?

---

**Scenario 2**

Customers report intermittent failures, but backend services appear healthy.

- How would distributed tracing help isolate the issue?
- Which telemetry sources would you correlate?

---

**Scenario 3**

A trace identifier appears in gateway logs but is missing from downstream services.

- What implementation issue does this suggest?
- How would you verify and remediate it?

---

# Chapter Summary

In this section, we expanded API Gateway capabilities by covering operational visibility and security monitoring.

We covered:

- Logging
- Monitoring
- Metrics
- Distributed tracing
- Correlation IDs
- Health checks
- Synthetic monitoring
- SLIs, SLOs, and SLAs
- API analytics
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Comprehensive observability enables organizations to detect attacks quickly, troubleshoot distributed systems efficiently, and maintain reliable, secure API operations.

---

# Chapter Review

You should now be able to answer:

- Why are logs, metrics, and traces all necessary for observability?
- How do correlation IDs improve incident investigations?
- Which gateway metrics are most important for security monitoring?
- How can distributed tracing reduce troubleshooting time?
- Which API Gateway events should be forwarded to a SIEM?
- How would you investigate repeated HTTP 429 responses?
- How would you design a monitoring strategy for an enterprise API platform?

If you can confidently answer these questions, you are ready to continue with **Chapter 15 – Rate Limiting**, where you'll explore rate-limiting algorithms, abuse prevention strategies, distributed enforcement, advanced quota management, and enterprise traffic governance in greater depth.

---

# References

## Standards

- OpenTelemetry Specification
- RFC 9110 – HTTP Semantics
- OpenMetrics Specification

## Security Standards

- OWASP API Security Top 10
- OWASP Logging Cheat Sheet
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-92 – Guide to Computer Security Log Management

## Further Reading

- CNCF Observability Landscape
- OpenTelemetry Documentation
- Enterprise SIEM Implementation Best Practices

---

# What's Next?

➡️ **Chapter 15 – Rate Limiting (Advanced)**

Topics include:

- Advanced rate-limiting algorithms
- Distributed quota enforcement
- API monetization
- Consumer plans and quotas
- Burst handling
- Abuse detection
- Adaptive traffic control
- Detection engineering
- SIEM integration
- Hands-on labs
- Enterprise case studies
- Interview questions