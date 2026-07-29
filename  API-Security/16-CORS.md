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

**Next:** CORS misconfigurations, exploitation techniques, credentialed requests, browser behavior, detection engineering, SIEM integration, hands-on labs, troubleshooting, and interview questions.