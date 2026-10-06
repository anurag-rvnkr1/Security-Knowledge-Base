# 16 - Cross-Origin Resource Sharing (CORS)

# Introduction

Cross-Origin Resource Sharing (CORS) is a browser security mechanism that allows controlled access to resources hosted on different origins.

By default, web browsers enforce the **Same-Origin Policy (SOP)**, which prevents web pages from making unrestricted requests to different origins.

CORS extends the Same-Origin Policy by allowing servers to explicitly specify which origins are permitted to access their resources.

CORS is one of the most misunderstood areas of API security and is frequently responsible for:

- Sensitive data exposure
- Cross-origin information disclosure
- Authentication bypass (through misconfiguration)
- Excessive trust relationships
- Browser-based API abuse

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the Same-Origin Policy.
- Learn how CORS works.
- Understand origins and cross-origin requests.
- Explore preflight requests.
- Understand CORS headers.
- Learn credentialed requests.
- Identify common CORS misconfigurations.
- Perform CORS security assessments.
- Detect CORS-related attacks.

---

# Same-Origin Policy (SOP)

The Same-Origin Policy is a browser security control that restricts JavaScript from accessing resources belonging to another origin.

An origin consists of:

```
Protocol

+

Hostname

+

Port
```

Example

```
https://api.company.com:443
```

All three components together define an origin.

---

# Same-Origin Policy Example

```
Current Website

https://portal.company.com

            │

            ▼

JavaScript

            │

Can Access?

            │

https://portal.company.com

        YES

────────────────────────

https://api.company.com

         NO

────────────────────────

https://company.com

         NO

────────────────────────

http://portal.company.com

         NO
```

Different protocol, hostname, or port creates a different origin.

---

# What is an Origin?

Examples

| URL | Same Origin? |
|------|--------------|
| https://portal.company.com | Yes |
| https://api.company.com | No |
| http://portal.company.com | No |
| https://portal.company.com:8443 | No |
| https://portal.company.org | No |

---

# Why SOP Exists

Without SOP

```
Victim Browser

       │

Malicious Website

       │

Reads

Online Banking

Email

Cloud Storage

       ▼

Sensitive Data Theft
```

SOP prevents one website from directly reading another website's responses.

---

# Why CORS Exists

Modern applications commonly separate frontend and backend services.

Example

```
Frontend

https://app.company.com

        │

API Request

        ▼

https://api.company.com
```

Although these are different origins,

the request is legitimate.

CORS enables this interaction safely.

---

# CORS Overview

```
Browser

    │

Cross-Origin Request

    │

API Server

    │

CORS Policy

    │

Allow?

┌────┴────┐

▼         ▼

Yes      No

▼         ▼

Browser  Block
Allows
```

The browser—not the server—enforces CORS.

---

# Browser Enforcement

Important

```
Browser

↓

Enforces CORS

----------------------

Server

↓

Returns Headers
```

Servers advertise CORS policies, but browsers decide whether JavaScript can access the response.

---

# Simple Requests

Certain requests do not require a preflight request.

Typical characteristics

- GET
- HEAD
- POST (limited content types)
- Standard headers only

Example

```
GET /api/profile
```

The browser directly sends the request and evaluates the response headers.

---

# Preflight Requests

Complex requests require permission before the actual request is sent.

The browser first sends an HTTP `OPTIONS` request.

```
Browser

     │

OPTIONS

     ▼

Server

     │

Allowed?

     ▼

Actual Request
```

---

# When Preflight Occurs

Examples

- PUT
- DELETE
- PATCH
- Custom Headers
- JSON APIs with non-simple conditions
- Authorization header

---

# Preflight Workflow

```
Browser

      │

OPTIONS Request

      │

Origin

Method

Headers

      ▼

API Server

      │

CORS Response

      ▼

Browser

      │

Policy Approved?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Actual    Block
Request
```

---

# Origin Header

Every cross-origin request includes an `Origin` header.

Example

```
Origin:

https://portal.company.com
```

The server uses this value when evaluating its CORS policy.

---

# Important CORS Headers

| Header | Purpose |
|---------|----------|
| Access-Control-Allow-Origin | Allowed origins |
| Access-Control-Allow-Methods | Allowed HTTP methods |
| Access-Control-Allow-Headers | Allowed request headers |
| Access-Control-Allow-Credentials | Allow cookies/authentication |
| Access-Control-Max-Age | Cache preflight results |
| Access-Control-Expose-Headers | Headers accessible to JavaScript |

---

# Access-Control-Allow-Origin

This header specifies which origin is allowed.

Example

```
Access-Control-Allow-Origin:

https://portal.company.com
```

Only the specified origin may access the response.

---

# Wildcard Origin

Example

```
Access-Control-Allow-Origin:

*
```

This permits any origin to access the resource.

Acceptable for:

- Public documentation
- Public images
- Public APIs without sensitive data

Not recommended for authenticated APIs.

---

# Access-Control-Allow-Methods

Defines permitted HTTP methods.

Example

```
GET

POST

PUT

DELETE
```

Only required methods should be allowed.

---

# Access-Control-Allow-Headers

Specifies which request headers clients may send.

Example

```
Authorization

Content-Type

X-API-Key
```

Avoid unnecessarily broad permissions.

---

# Access-Control-Allow-Credentials

Allows browsers to include credentials.

Example

```
Access-Control-Allow-Credentials:

true
```

Credentials include:

- Cookies
- Client certificates
- HTTP authentication

---

# Credentialed Requests

```
Browser

      │

Cookies

Authorization

      ▼

API Server

      │

Credential Validation

      ▼

Response
```

Credentialed requests require stricter CORS configuration.

---

# Access-Control-Max-Age

Browsers may cache successful preflight responses.

Example

```
Access-Control-Max-Age:

3600
```

This reduces repeated `OPTIONS` requests.

---

# Access-Control-Expose-Headers

By default,

JavaScript cannot access every response header.

Example

```
Access-Control-Expose-Headers:

X-Request-ID
```

Only explicitly exposed headers become accessible.

---

# CORS Request Lifecycle

```
Browser

     │

Origin Header

     ▼

API Gateway

     │

CORS Evaluation

     ▼

Backend API

     │

Response Headers

     ▼

Browser Decision
```

---

# CORS with API Gateways

Many organizations centralize CORS policies within the API Gateway.

```
Browser

     │

API Gateway

     │

CORS Validation

     │

Backend APIs
```

Centralized management improves consistency across services.

---

# Enterprise CORS Architecture

```
                 Browser

                    │

                    ▼

              API Gateway

          ┌─────────┼─────────┐

          ▼         ▼         ▼

   Authentication  CORS  Rate Limiting

          │

          ▼

     Backend Services

          │

          ▼

       Databases
```

---

# Best Practices

Configuration

- Allow only trusted origins.
- Allow only required methods.
- Allow only required headers.
- Review policies regularly.

Security

- Avoid wildcard origins for authenticated APIs.
- Restrict credentialed requests.
- Validate origins exactly.
- Centralize CORS policies at the gateway where possible.

Operations

- Monitor failed preflight requests.
- Log CORS policy violations.
- Document approved origins.
- Test configuration after changes.

---

# Common Security Mistakes

Avoid

- Allowing every origin
- Excessive allowed methods
- Allowing unnecessary headers
- Enabling credentials broadly
- Missing origin validation
- Inconsistent gateway and backend policies
- Ignoring preflight failures
- Treating CORS as an authentication mechanism

---

# Key Takeaways

- Same-Origin Policy protects browser users by default.
- CORS selectively relaxes SOP using server-defined policies.
- Browsers enforce CORS decisions.
- Preflight requests verify permissions before complex requests.
- Secure CORS configurations follow the principle of least privilege.

---

# CORS Misconfigurations

Incorrect CORS configurations are among the most common API security issues.

Unlike many server-side vulnerabilities, CORS issues primarily affect browser-based applications.

A vulnerable CORS policy can expose sensitive API responses to attacker-controlled websites.

---

# Common CORS Misconfigurations

```
               CORS

                 │

     ┌───────────┼─────────────┐

     ▼           ▼             ▼

 Wildcards   Reflection    Credentials

     │           │             │

     ▼           ▼             ▼

 Sensitive Data Exposure   Authentication Risk
```

---

# Wildcard Origin

One of the most common mistakes is allowing every origin.

Example

```
Access-Control-Allow-Origin:

*
```

Consequences

- Any website may access the resource.
- Public APIs become accessible from every browser origin.
- Sensitive APIs become vulnerable if authentication is also improperly configured.

---

# Wildcard with Credentials

The following configuration is invalid and should never be used.

```
Access-Control-Allow-Origin: *

Access-Control-Allow-Credentials: true
```

Modern browsers reject this combination because it would otherwise allow any website to access authenticated resources.

---

# Origin Reflection

Some applications simply copy the incoming `Origin` header into the response.

Example

```
Request

Origin:

https://attacker.example
```

Response

```
Access-Control-Allow-Origin:

https://attacker.example
```

If no validation occurs,

any origin becomes trusted.

---

# Reflection Attack

```
Attacker Website

        │

Origin:

evil.example

        │

API Server

        │

Reflect Origin

        ▼

Browser Grants Access
```

Reflection effectively bypasses the intended origin whitelist.

---

# Weak Origin Validation

Poor validation logic may allow attacker-controlled origins.

Example whitelist

```
company.com
```

Accepted by vulnerable validation

```
company.com.attacker.com
```

Correct validation must perform exact origin matching.

---

# Subdomain Trust Mistakes

Organizations sometimes trust every subdomain.

Example

```
*.company.com
```

Risks

- Forgotten subdomains
- Development systems
- Compromised applications
- Test environments

A compromised trusted subdomain can become a launch point for attacks.

---

# Null Origin

Some requests contain

```
Origin: null
```

Possible sources include

- Local files
- Sandboxed iframes
- Certain browser contexts

Applications should not automatically trust the `null` origin.

---

# Insecure Regular Expressions

Improper regular expressions may unintentionally trust attacker domains.

Example

```
.*company.com
```

This may incorrectly match

```
company.com.attacker.org
```

Use strict validation instead of permissive patterns.

---

# Overly Permissive Methods

Example

```
Access-Control-Allow-Methods

GET

POST

PUT

DELETE

PATCH

OPTIONS
```

Only required methods should be allowed.

Least privilege applies to HTTP methods as well.

---

# Overly Permissive Headers

Example

```
Access-Control-Allow-Headers

*
```

or

```
Authorization

X-*

Everything
```

Only necessary headers should be permitted.

---

# Excessive Header Exposure

Applications sometimes expose internal response headers.

Example

```
Access-Control-Expose-Headers

Server

Internal-Version

Database-ID
```

Only expose headers required by client-side code.

---

# Trusting Development Origins

Example

```
localhost

127.0.0.1

dev.company.local
```

Development origins should not remain enabled in production.

---

# Multiple Trusted Origins

Large organizations often require multiple origins.

Example

```
portal.company.com

mobile.company.com

partners.company.com
```

Each origin should be reviewed individually.

---

# Dynamic Origin Whitelisting

Preferred approach

```
Incoming Origin

        │

Lookup Trusted List

        │

Match?

   ┌────┴────┐

   ▼         ▼

 Yes        No

   ▼         ▼

Allow     Reject
```

---

# Browser Behavior

Even if the server returns data,

JavaScript cannot access the response when CORS validation fails.

```
Server

Returns Response

       │

Browser

Blocks Access

       ▼

JavaScript

Cannot Read
```

This distinction is important during testing.

---

# CORS Does NOT Replace Authentication

Incorrect assumption

```
Allowed Origin

↓

Authenticated User
```

Correct model

```
Authentication

AND

Authorization

AND

CORS
```

CORS is **not** an authentication or authorization mechanism.

---

# CORS Does NOT Protect APIs

API clients such as

- curl
- Postman
- Python
- Go
- Java
- Mobile applications

do not enforce browser CORS rules.

```
Browser

↓

CORS Enforced

------------------------

curl

↓

No CORS Enforcement
```

Server-side security controls remain essential.

---

# CORS and API Gateways

Many enterprise gateways centrally evaluate origins.

```
Browser

     │

API Gateway

     │

Origin Validation

     │

Backend API
```

Benefits

- Centralized configuration
- Consistent enforcement
- Easier auditing

---

# Secure CORS Workflow

```
Browser

     │

Origin Header

     ▼

API Gateway

     │

Trusted Origin?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject

     │

Backend API
```

---

# Secure Origin Validation

Recommended process

```
Incoming Origin

       │

Exact Match

       │

Trusted List

       │

Allow?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject
```

Avoid partial matching.

---

# Credentialed Requests

Credentialed requests require additional care.

```
Browser

      │

Cookie

Session

JWT

      ▼

API

      │

Authentication

      │

Authorization

      │

CORS Validation
```

All three controls should succeed before sensitive data is returned.

---

# Secure Credential Configuration

Recommended

```
Access-Control-Allow-Origin

https://portal.company.com

----------------------------

Access-Control-Allow-Credentials

true
```

Avoid wildcard origins with authenticated sessions.

---

# CORS Testing Methodology

Security reviewers should evaluate:

- Allowed origins
- Reflected origins
- Credential handling
- Preflight behavior
- Allowed methods
- Allowed headers
- Header exposure
- Origin validation logic

Testing should occur in an authorized environment.

---

# Example Assessment Workflow

```
Identify Endpoint

        │

Review Response Headers

        │

Modify Origin

        │

Observe Response

        │

Evaluate Policy

        ▼

Document Findings
```

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Origin Reflection | Reflected arbitrary Origin values |
| Invalid Origin Attempts | Large number of rejected origins |
| Suspicious Origins | Requests from unknown domains |
| Preflight Failures | Elevated HTTP OPTIONS failures |
| Credentialed Cross-Origin Requests | Unexpected authenticated cross-origin traffic |
| New Trusted Origins | Configuration changes adding new origins |
| Excessive OPTIONS Requests | Reconnaissance or scanning activity |
| Wildcard Policies | Public APIs unexpectedly allowing all origins |

---

# SIEM Integration

Collect telemetry from

- API Gateway
- Reverse Proxy
- Web Server
- Web Application Firewall
- Authentication Services
- Configuration Management

```
API Gateway

      │

CORS Logs

      │

Configuration Changes

      │

SIEM

      │

Correlation Rules

      ▼

SOC Alerts
```

---

# Example Correlation Rules

Rule 1

```
Repeated Invalid Origins

        │

Credentialed Requests

        │

Authentication Failures

        ▼

Potential Attack
```

Rule 2

```
New Trusted Origin

       │

Large Data Transfer

       │

Sensitive Endpoint

       ▼

High Priority Alert
```

Rule 3

```
OPTIONS Spike

      │

404 Responses

      │

Sequential Endpoints

      ▼

Reconnaissance Activity
```

---

# Enterprise CORS Architecture

```
                    Browser

                       │

                       ▼

                Web Application Firewall

                       │

                       ▼

                  API Gateway

        ┌──────────┼────────────┐

        ▼          ▼            ▼

 Origin Check Authentication Authorization

        │

        ▼

     Backend APIs

        │

        ▼

 Logging & Monitoring

        │

        ▼

      SIEM / SOC
```

---

# Hands-on Lab 1 – Origin Validation Review

**Objective**

Review CORS origin validation in an authorized environment.

**Steps**

1. Identify API endpoints with CORS enabled.
2. Send requests using approved origins.
3. Repeat using unapproved origins.
4. Verify that only approved origins receive access.

**Learning Outcomes**

- Origin validation
- CORS policy verification
- Secure API configuration

---

# Hands-on Lab 2 – Reflection Testing

**Objective**

Identify origin reflection vulnerabilities.

**Steps**

1. Send requests with modified `Origin` headers.
2. Compare server responses.
3. Determine whether origins are reflected without validation.
4. Document findings.

**Learning Outcomes**

- Reflection detection
- CORS assessment
- Secure validation

---

# Hands-on Lab 3 – Credentialed Requests

**Objective**

Review authenticated cross-origin behavior.

**Steps**

1. Authenticate to a test application.
2. Issue authorized cross-origin requests from an approved origin.
3. Repeat from an unapproved origin.
4. Verify browser enforcement and server configuration.

**Learning Outcomes**

- Credential handling
- Secure CORS implementation
- Browser behavior

---

# Troubleshooting

## Browser Blocks Response

Possible causes

- Origin not trusted
- Missing `Access-Control-Allow-Origin`
- Failed preflight request
- Credential configuration mismatch

---

## Preflight Request Fails

Possible causes

- Method not permitted
- Header not allowed
- Incorrect `OPTIONS` handling
- Missing CORS configuration

---

## Credentialed Requests Fail

Possible causes

- Missing `Access-Control-Allow-Credentials`
- Wildcard origin configuration
- Cookie policy restrictions
- Session expiration

---

## Unexpected Origin Accepted

Possible causes

- Reflection vulnerability
- Weak validation logic
- Insecure regular expression
- Misconfigured whitelist

---

## Browser Works but API Client Also Succeeds

Possible causes

- Expected behavior
- CORS applies only to browsers
- API clients are not restricted by browser CORS enforcement

---

# Interview Questions

## Fundamental

1. What is the Same-Origin Policy?
2. What is CORS?
3. What defines an origin?
4. Why do browsers enforce CORS?
5. What is a preflight request?
6. What is the purpose of the `Origin` header?
7. What does `Access-Control-Allow-Origin` do?
8. Why is `Access-Control-Allow-Credentials` sensitive?
9. Does CORS provide authentication?
10. Does CORS protect APIs from non-browser clients?

---

## Intermediate

11. Explain the CORS request lifecycle.
12. Why is wildcard origin configuration dangerous for authenticated APIs?
13. What is origin reflection?
14. How would you securely validate origins?
15. What are the risks of trusting every subdomain?
16. How would you investigate repeated preflight failures?
17. Which CORS events should be monitored by a SIEM?
18. Why are exact origin matches preferred?
19. How would you review a production CORS policy?
20. How should CORS be implemented at an API Gateway?

---

## Scenario-Based

**Scenario 1**

A production API reflects every incoming `Origin` header and allows credentialed requests.

- What vulnerability does this indicate?
- What business impact could result?
- How would you remediate the configuration?

---

**Scenario 2**

Security monitoring reports a sudden increase in `OPTIONS` requests from previously unseen origins.

- What activities could explain this pattern?
- Which additional logs would you review?
- How would you determine whether it is malicious?

---

**Scenario 3**

An application trusts all `*.company.com` subdomains. A forgotten development subdomain is compromised.

- How could this affect CORS security?
- Which compensating controls would reduce the risk?
- How would you prioritize remediation?

---

# Chapter Summary

In this chapter, we explored Cross-Origin Resource Sharing (CORS) and its role in browser security.

We covered:

- Same-Origin Policy
- Origins
- Browser enforcement
- Simple requests
- Preflight requests
- CORS headers
- Credentialed requests
- Common misconfigurations
- Secure origin validation
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Properly configured CORS policies allow legitimate cross-origin communication while minimizing unnecessary trust relationships and reducing the risk of browser-based attacks.

---

# Chapter Review

You should now be able to answer:

- What is the difference between SOP and CORS?
- Why does the browser, rather than the server, enforce CORS?
- Why are wildcard origins inappropriate for authenticated APIs?
- How does origin reflection create security risks?
- Why can't CORS replace authentication or authorization?
- Which CORS events should be monitored by a SIEM?
- How would you assess and secure a production CORS configuration?

If you can confidently answer these questions, you are ready to continue with **Chapter 17 – CSRF in APIs**, where you'll explore Cross-Site Request Forgery attacks, browser cookie behavior, CSRF defenses, SameSite cookies, anti-CSRF tokens, API-specific considerations, detection engineering, and enterprise security best practices.

---

# References

## Standards

- Fetch Standard (WHATWG)
- RFC 9110 – HTTP Semantics

## Security Standards

- OWASP Cross-Origin Resource Sharing Cheat Sheet
- OWASP API Security Top 10
- OWASP ASVS
- NIST SP 800-53

## Further Reading

- MDN Web Docs – CORS
- W3C Web Security Specifications
- Browser Vendor Security Documentation

---

# What's Next?

➡️ **Chapter 17 – CSRF in APIs**

Topics include:

- Cross-Site Request Forgery (CSRF)
- Browser cookie behavior
- SameSite cookies
- Anti-CSRF tokens
- Double-submit cookie pattern
- Origin and Referer validation
- CSRF in REST APIs
- CSRF in GraphQL APIs
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions