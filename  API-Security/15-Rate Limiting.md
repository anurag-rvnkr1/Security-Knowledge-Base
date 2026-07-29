# 15 - Rate Limiting

# Introduction

Rate limiting is a security and traffic management technique that controls how many requests a client can make to an API during a defined time period.

It is one of the most effective defenses against:

- Denial-of-Service (DoS)
- Distributed Denial-of-Service (DDoS)
- Brute-force attacks
- Credential stuffing
- API scraping
- Resource exhaustion
- Abuse of public APIs

Modern API Gateways enforce rate limiting before requests reach backend services, helping maintain availability and predictable performance.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand rate limiting fundamentals.
- Differentiate throttling, quotas, and traffic shaping.
- Learn common rate-limiting algorithms.
- Design distributed rate-limiting systems.
- Understand burst handling.
- Implement adaptive rate limiting.
- Integrate rate limiting with API Gateways.
- Detect abuse using rate-limit telemetry.
- Perform enterprise rate-limit assessments.

---

# What is Rate Limiting?

Rate limiting restricts how frequently a client may access an API.

```
Client

   │

250 Requests

   │

API Gateway

   │

Configured Limit

100 Requests

   │

───────────────

100 Allowed

150 Rejected

   ▼

HTTP 429
```

---

# Why Rate Limiting is Important

Without rate limiting

```
Attacker

      │

500,000 Requests

      │

Backend APIs

      │

CPU Exhausted

      ▼

Service Outage
```

With rate limiting

```
Attacker

      │

500,000 Requests

      │

API Gateway

      │

Allow Only Policy Limit

      ▼

Backend Protected
```

---

# Rate Limiting Workflow

```
Incoming Request

        │

Identify Client

        │

Retrieve Policy

        │

Current Usage

        │

Within Limit?

    ┌───┴────┐

    ▼        ▼

 Allow    Reject

              │

        HTTP 429
```

---

# Core Components

```
          Rate Limiting

                 │

      ┌──────────┼───────────┐

      ▼          ▼           ▼

 Client ID   Counter Store  Policy Engine

                 │

                 ▼

         Allow / Reject
```

---

# Client Identification

Requests can be limited by:

- User ID
- API Key
- OAuth Client ID
- JWT Subject (`sub`)
- IP Address
- Device Identifier
- Organization
- Tenant
- Mutual TLS Certificate

Authenticated identities are generally preferred over IP addresses alone.

---

# Types of Limits

| Limit Type | Example |
|------------|----------|
| Per Second | 50 requests/sec |
| Per Minute | 500 requests/min |
| Per Hour | 10,000 requests/hour |
| Daily | 100,000 requests/day |
| Monthly Quota | 5,000,000 requests/month |

---

# Fixed Window Algorithm

Requests are counted inside fixed time intervals.

```
Minute

┌───────────────┐

Counter

0 → 100

└───────────────┘

Reset

↓

Next Minute
```

Advantages

- Simple
- Fast
- Low overhead

Disadvantages

- Boundary burst problem

---

# Sliding Window Algorithm

The window continuously moves with time.

```
Current Time

        │

Previous 60 Seconds

██████████████████

Count Requests

↓

Decision
```

Advantages

- Fair
- Accurate
- Smooth traffic distribution

Disadvantages

- Higher implementation complexity

---

# Sliding Log Algorithm

Every request timestamp is stored.

```
10:00:01

10:00:07

10:00:15

10:00:23

↓

Count Entries

↓

Apply Limit
```

Advantages

- Precise

Disadvantages

- Higher memory usage

---

# Token Bucket Algorithm

Tokens accumulate over time.

Each request consumes one token.

```
Bucket

██████████

10 Tokens

↓

Request

↓

9 Tokens

↓

Automatic Refill
```

Advantages

- Allows controlled bursts
- Widely deployed
- Efficient

---

# Leaky Bucket Algorithm

Requests enter a queue and leave at a constant rate.

```
Incoming Traffic

██████████████

        │

Leaky Bucket

        │

████

Constant Output
```

Advantages

- Smooth traffic
- Predictable backend load

---

# Algorithm Comparison

| Algorithm | Burst Support | Complexity | Accuracy |
|-----------|---------------|-----------:|----------|
| Fixed Window | Low | Low | Moderate |
| Sliding Window | Medium | Medium | High |
| Sliding Log | High | High | Very High |
| Token Bucket | Excellent | Medium | High |
| Leaky Bucket | Controlled | Medium | High |

---

# Burst Handling

Many APIs permit short bursts while enforcing long-term limits.

```
Normal Rate

100/minute

──────────────

Burst Capacity

20 Requests
```

Benefits

- Better user experience
- Improved responsiveness
- Reduced unnecessary throttling

---

# Throttling

Throttling slows or delays requests instead of immediately rejecting them.

```
Client

 │

High Traffic

 │

Gateway

 │

Delay

 ▼

Backend
```

Useful when temporary congestion occurs.

---

# Quotas

Quotas limit total API consumption over long periods.

Examples

| Plan | Monthly Quota |
|------|---------------:|
| Free | 100,000 |
| Standard | 5,000,000 |
| Enterprise | Unlimited (contract dependent) |

Quotas are primarily used for governance and API monetization.

---

# Rate Limiting vs Throttling vs Quotas

| Feature | Purpose |
|---------|----------|
| Rate Limiting | Control request frequency |
| Throttling | Slow excessive traffic |
| Quotas | Limit total consumption |

---

# Distributed Rate Limiting

In clustered environments, all gateway nodes must enforce the same limits.

```
            Load Balancer

                  │

      ┌───────────┼────────────┐

      ▼           ▼            ▼

 Gateway A   Gateway B   Gateway C

      │           │            │

      └───────────┼────────────┘

                  ▼

        Shared Counter Store

          (Redis / Cache)
```

---

# Rate Limiting in Kubernetes

```
Internet

    │

Ingress Controller

    │

API Gateway

    │

Redis Cluster

    │

Kubernetes Services

    │

Pods
```

Shared counters prevent inconsistent enforcement across replicas.

---

# Multi-Tenant Rate Limiting

Each tenant may have independent policies.

```
Gateway

 │

Tenant A

1000/min

──────────────

Tenant B

100/min

──────────────

Tenant C

5000/min
```

This prevents one tenant from impacting another.

---

# API Monetization

Commercial APIs frequently associate limits with subscription plans.

```
Free

↓

100 Requests/Minute

--------------------

Business

↓

1000 Requests/Minute

--------------------

Enterprise

↓

Custom Policy
```

---

# Priority-Based Traffic

```
Premium Customers

        │

Highest Priority

-------------------------

Business Customers

-------------------------

Free Tier
```

Critical business traffic should receive higher priority during congestion.

---

# Adaptive Rate Limiting

Adaptive systems dynamically adjust limits.

Factors include:

- CPU utilization
- Memory usage
- Backend latency
- Error rates
- Active sessions
- Infrastructure health

```
Normal Load

↓

Higher Limits

-------------------

High Load

↓

Lower Limits
```

---

# HTTP Response Headers

Common headers

```
X-RateLimit-Limit

X-RateLimit-Remaining

X-RateLimit-Reset

Retry-After
```

These help clients implement backoff and retry strategies.

---

# HTTP 429 Response

Example

```
HTTP/1.1 429 Too Many Requests

Retry-After: 60
```

Clients should respect the retry interval instead of immediately retrying.

---

# Enterprise Rate-Limiting Architecture

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

        ┌────────┼─────────┐

        ▼        ▼         ▼

 Authentication Rate Limit Routing

        │

        ▼

 Shared Counter Store

        │

        ▼

 Backend Services
```

---

# Best Practices

Architecture

- Enforce limits at the API Gateway.
- Use distributed counters.
- Separate policies by endpoint.
- Protect authentication endpoints with stricter limits.

Security

- Prefer authenticated identities over IP addresses.
- Monitor HTTP 429 responses.
- Apply adaptive policies during incidents.
- Combine rate limiting with bot detection and WAF rules.

Operations

- Review limits regularly.
- Test policies under load.
- Monitor false positives.
- Document service-specific limits.

---

# Common Mistakes

Avoid

- One policy for every endpoint
- Unlimited anonymous access
- Per-IP limits only
- Ignoring burst traffic
- Missing shared counters in clustered deployments
- Unlimited retries
- No monitoring of rejected requests
- Excessively high limits on authentication endpoints
- Static policies that never change

---

# Key Takeaways

- Rate limiting protects APIs from abuse while maintaining availability.
- Token Bucket and Sliding Window are among the most commonly used algorithms in enterprise environments.
- Distributed enforcement is essential for scalable deployments.
- Adaptive rate limiting improves resilience during traffic spikes.
- Rate limiting, throttling, quotas, and WAF protections work together to defend modern APIs.

---

**Next:** Advanced abuse detection, bot mitigation, rate-limit evasion techniques, Detection Engineering, SIEM integration, hands-on labs, troubleshooting, interview questions, and enterprise case studies.