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

# Advanced Abuse Detection

Traditional rate limiting blocks excessive request volume.

However,

modern attackers often remain below configured thresholds to avoid detection.

Advanced abuse detection combines behavioral analytics, identity analysis, reputation systems, and machine learning to identify sophisticated attacks.

---

# Modern API Threats

```
                    API Abuse

                        │

      ┌─────────────────┼─────────────────┐

      ▼                 ▼                 ▼

 Credential         Data              Resource

 Stuffing          Scraping         Exhaustion

      │                 │                 │

      ▼                 ▼                 ▼

 Bot Networks     Enumeration      Slow Attacks
```

Traditional rate limiting alone cannot stop every attack.

---

# Types of API Abuse

Common abuse patterns include:

- Credential stuffing
- Password spraying
- Brute-force attacks
- API scraping
- Account enumeration
- Resource exhaustion
- Token replay
- Bot automation
- Business logic abuse
- Inventory hoarding

---

# Credential Stuffing

Attackers reuse stolen username/password combinations.

```
Leaked Credentials

        │

Bot Network

        │

API Login

        │

Thousands of Accounts

        ▼

Successful Compromise
```

Detection indicators

- Large number of login attempts
- Low success ratio
- Requests from many IP addresses
- Repeated usernames

---

# Password Spraying

Instead of attacking one account,

attackers attempt a few common passwords across many users.

```
Password

Spring2026!

        │

User A

User B

User C

User D
```

Detection indicators

- Same password attempt
- Many accounts
- Distributed IP addresses

---

# API Scraping

Scraping extracts large amounts of information.

```
Bot

 │

Sequential Requests

 │

Product API

 │

Entire Catalog

 ▼

Data Theft
```

Detection indicators

- Sequential object access
- High read ratio
- Low interaction diversity
- Constant request timing

---

# Business Logic Abuse

Some attacks exploit intended functionality instead of software vulnerabilities.

Examples

- Coupon abuse
- Reward point manipulation
- Inventory reservation
- Cart hoarding
- Referral fraud

These attacks require behavioral detection rather than signature matching.

---

# API Enumeration

Attackers systematically discover endpoints.

```
/api/v1/users

/api/v1/orders

/api/v1/admin

/api/v1/payments
```

Indicators

- Sequential endpoint requests
- Numerous HTTP 404 responses
- Unusual endpoint discovery patterns

---

# Slow API Attacks

Instead of flooding the API,

attackers deliberately send slow requests.

```
Connection

───────────────

Very Slow Upload

───────────────

Resources Occupied
```

Mitigations

- Request timeouts
- Connection limits
- Reverse proxies
- Load balancers

---

# Distributed Bot Networks

Large attacks often originate from thousands of devices.

```
Bot 1

Bot 2

Bot 3

Bot 4

      │

API Gateway

      ▼

Target API
```

Per-IP rate limiting alone becomes ineffective.

---

# Bot Detection

Modern gateways evaluate multiple signals.

```
Incoming Request

        │

Fingerprint

Behavior

Headers

TLS

Cookies

Timing

        ▼

Bot Score
```

---

# Browser Fingerprinting

Browsers expose characteristics useful for identifying clients.

Examples

- User-Agent
- Screen resolution
- Time zone
- Language
- TLS fingerprint
- Header ordering

These signals assist in identifying automation but should be used with privacy considerations and applicable regulations.

---

# Device Fingerprinting

Applications may identify devices using:

- Device identifiers
- Secure cookies
- Platform information
- Authentication history

Device fingerprints help detect suspicious account activity.

---

# IP Reputation

Gateways may consult threat intelligence.

```
Incoming IP

      │

Threat Feed

      │

Known Malicious?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Block    Continue
```

---

# Geo-Velocity Detection

Impossible travel may indicate compromised accounts.

Example

```
09:00

Bengaluru

↓

09:20

London
```

Detection

```
Travel Speed

>

Physically Possible

↓

Alert
```

---

# User Behavior Analytics (UBA)

UBA builds behavioral baselines.

Examples

- Login times
- Device usage
- Geographic regions
- Request frequency
- API usage patterns

Deviations may indicate compromise.

---

# Behavioral Baselines

```
Normal User

      │

100 Requests

Business Hours

Known Device

──────────────

Abnormal

5000 Requests

Unknown Device

03:00 AM
```

---

# Risk Scoring

Each request receives a calculated risk score.

```
Signals

 │

Location

 │

Device

 │

Token

 │

Behavior

 ▼

Risk Score

 ▼

Allow

Challenge

Block
```

---

# Adaptive Authentication

High-risk requests may require additional verification.

```
Normal Risk

↓

Access Granted

-----------------------

High Risk

↓

Require MFA
```

Adaptive authentication reduces unnecessary user friction.

---

# Token Abuse Detection

Monitor for:

- Token replay
- Unusual token lifetime
- Multiple concurrent locations
- Excessive refresh requests
- Audience mismatches

---

# Refresh Token Abuse

Indicators

```
Refresh Token

 │

Multiple Devices

 │

Repeated Refresh

 ▼

Possible Theft
```

Refresh token reuse detection is a valuable control.

---

# API Key Abuse

Common indicators

- Sudden traffic increase
- Geographic anomalies
- Excessive failures
- Requests outside normal hours
- Unexpected endpoint usage

Compromised API keys should be rotated immediately.

---

# Machine Learning in API Security

Machine learning may identify anomalies such as:

- Unusual request sequences
- Unknown attack patterns
- New bot behaviors
- Behavioral deviations

Machine learning should complement, not replace, deterministic security controls.

---

# Rate-Limit Evasion Techniques

Attackers may attempt to bypass rate limits.

Examples

- IP rotation
- Residential proxies
- VPNs
- Botnets
- Multiple API keys
- Multiple accounts
- Distributed timing

```
Bot

 │

IP1

IP2

IP3

IP4

 ▼

Gateway
```

---

# Defending Against Evasion

Recommended controls

- Identity-based limits
- Device reputation
- Behavioral analytics
- Bot detection
- CAPTCHA where appropriate
- Risk scoring
- Adaptive authentication

Layered defenses are more effective than any single control.

---

# CAPTCHA Integration

Sensitive workflows may require human verification.

Examples

- Login
- Account creation
- Password reset
- Bulk searches

CAPTCHA should be applied selectively to minimize user impact.

---

# Threat Intelligence Integration

```
Threat Intelligence

        │

Known IPs

Known Domains

Known Botnets

        │

API Gateway

        ▼

Decision Engine
```

Threat intelligence improves detection of known malicious infrastructure.

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Credential Stuffing | Many login failures across numerous accounts |
| Password Spraying | Same password attempted for many users |
| API Scraping | Sequential object access with high volume |
| Enumeration | High volume of HTTP 404 responses |
| Bot Activity | Consistent request intervals and fingerprints |
| Token Replay | Same token used from multiple locations |
| Refresh Abuse | Excessive refresh requests |
| Impossible Travel | Authentication from distant regions within unrealistic timeframes |
| API Key Abuse | Sudden increase in requests from a single key |
| Slow API Attack | Long-lived connections consuming resources |

---

# SIEM Integration

Recommended telemetry

```
API Gateway

      │

Authentication Logs

      │

Rate-Limit Events

      │

Threat Intelligence

      │

Identity Provider

      │

Application Logs

      ▼

Enterprise SIEM

      │

Correlation

      ▼

SOC Alerts
```

---

# Correlation Rules

Example Rule 1

```
Failed Logins

        │

Successful Login

        │

New Device

        ▼

High Severity Alert
```

Example Rule 2

```
Token Replay

      │

Impossible Travel

      │

API Key Rotation

      ▼

Incident
```

Example Rule 3

```
High 404 Rate

      │

Endpoint Enumeration

      │

SQL Injection Attempts

      ▼

Reconnaissance Alert
```

---

# Enterprise Abuse Detection Architecture

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

        ┌────────┼─────────┬──────────┐

        ▼        ▼         ▼          ▼

 Authentication Rate Limit Bot Detection Threat Intelligence

                        │

                        ▼

                Risk Scoring Engine

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

       Allow        Challenge       Block

                        │

                        ▼

                 Backend Services

                        │

                        ▼

                    SIEM / SOC
```

---

# Hands-on Lab 1 – Credential Stuffing Detection

**Objective**

Identify credential stuffing activity in an authorized lab.

**Steps**

1. Generate normal login traffic.
2. Simulate repeated failed logins across multiple accounts.
3. Review gateway and authentication logs.
4. Create a detection rule for credential stuffing indicators.

**Learning Outcomes**

- Authentication monitoring
- Detection engineering
- SOC investigation workflow

---

# Hands-on Lab 2 – API Scraping Analysis

**Objective**

Identify scraping behavior.

**Steps**

1. Generate normal browsing activity.
2. Simulate automated sequential API requests.
3. Review request patterns.
4. Compare legitimate and automated behaviors.

**Learning Outcomes**

- Behavioral analysis
- Enumeration detection
- Abuse investigation

---

# Hands-on Lab 3 – Risk-Based Authentication

**Objective**

Evaluate adaptive authentication.

**Steps**

1. Authenticate from a trusted device.
2. Repeat authentication from a new device and location.
3. Review calculated risk signals.
4. Verify that additional authentication is requested for high-risk events.

**Learning Outcomes**

- Risk scoring
- Adaptive authentication
- Identity protection

---

# Troubleshooting

## Excessive False Positives

Possible causes

- Aggressive thresholds
- Shared IP addresses
- Legitimate automation
- Incomplete behavioral baselines

---

## Missed Bot Activity

Possible causes

- Static detection rules
- Weak fingerprinting
- Missing threat intelligence
- No behavioral analysis

---

## Frequent CAPTCHA Challenges

Possible causes

- Misconfigured risk scoring
- Excessively strict policies
- Shared enterprise networks
- Incorrect device reputation

---

## Token Replay Not Detected

Possible causes

- Missing correlation
- Incomplete identity logs
- No geographic analysis
- Short log retention

---

## API Scraping Continues

Possible causes

- No identity-based limits
- Missing bot detection
- Weak rate limiting
- Public endpoints lacking abuse controls

---

# Interview Questions

## Fundamental

1. What is API abuse?
2. How does credential stuffing differ from brute-force attacks?
3. What is API scraping?
4. Why is rate limiting alone insufficient against sophisticated attackers?
5. What is user behavior analytics (UBA)?
6. What is adaptive authentication?
7. What is IP reputation?
8. What is geo-velocity detection?
9. What is risk scoring?
10. Why is threat intelligence useful for API security?

---

## Intermediate

11. How would you detect password spraying?
12. Explain how behavioral analytics identifies API abuse.
13. How would you detect token replay?
14. What indicators suggest API enumeration?
15. How would you defend against rate-limit evasion?
16. What telemetry should be forwarded to a SIEM?
17. How would you reduce false positives in bot detection?
18. Explain identity-based rate limiting.
19. How would you investigate API key abuse?
20. How would you implement adaptive authentication for high-risk API requests?

---

## Scenario-Based

**Scenario 1**

A single user account successfully authenticates from three different countries within one hour using the same access token.

- Which indicators suggest compromise?
- What additional evidence would you collect?
- What immediate containment actions would you recommend?

---

**Scenario 2**

An API experiences a large increase in sequential requests for product records. Traffic stays below configured rate limits.

- What attack might be occurring?
- Which behavioral indicators would help confirm it?
- Which gateway controls would you enable?

---

**Scenario 3**

Multiple API keys begin making requests from infrastructure previously identified in threat intelligence feeds.

- Which correlation rules should trigger?
- How would you prioritize the incident?
- What actions would you take to reduce business impact?

---

# Chapter Summary

In this section, we expanded rate limiting into comprehensive API abuse detection.

We covered:

- Modern API abuse techniques
- Credential stuffing
- Password spraying
- API scraping
- Enumeration
- Bot detection
- Behavioral analytics
- Risk scoring
- Adaptive authentication
- Threat intelligence
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Modern API protection requires layered defenses that combine rate limiting, behavioral analytics, identity-aware controls, threat intelligence, and continuous monitoring.

---

# Chapter Review

You should now be able to answer:

- Why is rate limiting alone insufficient against sophisticated attacks?
- How can behavioral analytics detect API scraping?
- What signals contribute to API risk scoring?
- How does adaptive authentication improve security?
- Which events should trigger abuse-related SIEM alerts?
- How would you investigate credential stuffing or token replay?
- How can organizations defend against rate-limit evasion techniques?

If you can confidently answer these questions, you are ready to continue with **Chapter 16 – Cross-Origin Resource Sharing (CORS)**, where you'll learn browser same-origin policy, CORS headers, preflight requests, credential handling, common misconfigurations, exploitation techniques, detection engineering, and enterprise deployment best practices.

---

# References

## Standards

- RFC 6585 – Additional HTTP Status Codes (HTTP 429)
- RFC 9110 – HTTP Semantics

## Security Standards

- OWASP API Security Top 10
- OWASP Automated Threats to Web Applications
- OWASP Credential Stuffing Prevention Cheat Sheet
- NIST SP 800-61 Rev. 2 – Computer Security Incident Handling Guide

## Further Reading

- MITRE ATT&CK Framework
- OpenTelemetry Documentation
- Enterprise Bot Management Best Practices

---

# What's Next?

➡️ **Chapter 16 – Cross-Origin Resource Sharing (CORS)**

Topics include:

- Same-Origin Policy (SOP)
- CORS fundamentals
- Preflight requests
- CORS request and response headers
- Credentialed requests
- Browser enforcement
- Common CORS misconfigurations
- Exploitation techniques
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions