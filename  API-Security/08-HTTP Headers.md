# 08 - HTTP Headers

# Introduction

HTTP headers are key-value pairs exchanged between clients and servers that provide additional information about an HTTP request or response.

Headers control various aspects of communication, including:

- Authentication
- Content negotiation
- Caching
- Security policies
- Compression
- Connection management
- Cookies
- Proxy behavior

Every HTTP request and response contains a collection of headers that influence how data is transmitted, processed, and secured.

A strong understanding of HTTP headers is essential for:

- API Security
- Penetration Testing
- Secure Software Development
- Detection Engineering
- Digital Forensics
- Incident Response

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand HTTP headers.
- Differentiate request and response headers.
- Learn common HTTP headers.
- Understand security-related headers.
- Learn authentication headers.
- Understand content negotiation.
- Learn caching behavior.
- Identify header-based attacks.
- Perform header security assessments.

---

# What Are HTTP Headers?

Headers provide metadata about an HTTP message.

Example

```
GET /api/users HTTP/1.1

Host: api.company.com

Authorization: Bearer <token>

Accept: application/json

User-Agent: Browser
```

The body contains application data.

Headers describe how that data should be processed.

---

# HTTP Header Structure

Headers follow a simple format.

```
Header-Name: Value
```

Example

```
Content-Type: application/json

Content-Length: 520

Accept: application/json
```

Each header consists of:

- Header name
- Colon (`:`)
- Header value

---

# Request vs Response Headers

```
Client

 │

Request Headers

 ▼

Server

 │

Response Headers

 ▼

Client
```

Request headers describe the client's request.

Response headers describe the server's response.

---

# Header Categories

HTTP headers can be grouped into several categories.

```
HTTP Headers

        │

 ┌──────┼─────────────┬────────────┐

 ▼      ▼             ▼            ▼

General Request    Response    Security
```

Additional categories include:

- Authentication
- Caching
- Proxy
- Entity
- Conditional
- Content Negotiation

---

# General Headers

General headers apply to both requests and responses.

Examples

```
Date

Connection

Cache-Control

Via

Transfer-Encoding
```

These headers influence message handling rather than application data.

---

# Request Headers

Common request headers include:

| Header | Purpose |
|---------|---------|
| Host | Target host |
| User-Agent | Client software |
| Accept | Preferred response type |
| Accept-Language | Preferred language |
| Accept-Encoding | Compression support |
| Authorization | Authentication credentials |
| Referer | Referring page |
| Origin | Request origin |
| Cookie | Session cookies |

---

# Response Headers

Common response headers include:

| Header | Purpose |
|---------|---------|
| Server | Server software |
| Content-Type | Response format |
| Content-Length | Response size |
| Set-Cookie | Create cookies |
| Location | Redirect target |
| ETag | Cache validation |
| Last-Modified | Modification timestamp |
| Cache-Control | Cache policy |

---

# The Host Header

The `Host` header identifies the destination server.

Example

```
Host: api.company.com
```

Virtual hosting relies on this header to route requests.

Incorrect validation may lead to Host Header Injection attacks.

---

# User-Agent Header

The `User-Agent` header identifies the client software.

Example

```
User-Agent:

Mozilla/5.0
```

Servers may use this information for:

- Compatibility
- Analytics
- Logging
- Device detection

User-Agent values should never be trusted for authentication or authorization.

---

# Accept Header

The `Accept` header specifies acceptable response formats.

Example

```
Accept:

application/json
```

Other values include:

```
text/html

application/xml

image/png

*/*
```

Servers use this information during content negotiation.

---

# Accept-Encoding

Indicates supported compression algorithms.

Example

```
Accept-Encoding:

gzip

br

deflate
```

Compression reduces bandwidth usage but requires secure configuration.

---

# Accept-Language

Specifies language preferences.

Example

```
Accept-Language:

en-US
```

Applications may return localized content based on this header.

---

# Authorization Header

The `Authorization` header carries authentication credentials.

Example

```
Authorization:

Bearer eyJhbGci...
```

Other authentication schemes include:

- Basic
- Digest
- Bearer
- Negotiate
- API Tokens

This header is one of the most security-sensitive parts of an HTTP request.

---

# Cookie Header

Cookies maintain session state.

Example

```
Cookie:

SESSIONID=abc123
```

Servers use cookies for:

- Authentication
- Session tracking
- User preferences
- Shopping carts

Session cookies require secure handling.

---

# Origin Header

The `Origin` header identifies where a request originated.

Example

```
Origin:

https://shop.example.com
```

Browsers include this header during Cross-Origin Resource Sharing (CORS) requests.

Servers use it to determine whether cross-origin access should be permitted.

---

# Referer Header

The `Referer` header identifies the previous page.

Example

```
Referer:

https://example.com/dashboard
```

Applications may use it for:

- Analytics
- Navigation
- CSRF validation (supplementary only)

Sensitive information should never appear in URLs because it may be exposed through the Referer header.

---

# Content-Type Header

The `Content-Type` header identifies the media type.

Examples

```
application/json

text/html

application/xml

multipart/form-data

application/pdf
```

Example

```
Content-Type:

application/json
```

Applications should validate expected content types before processing requests.

---

# Content-Length

Indicates message size.

Example

```
Content-Length:

250
```

Servers use this value to determine how much data to read.

Improper handling may contribute to request smuggling vulnerabilities.

---

# Transfer-Encoding

Specifies how the message body is transmitted.

Example

```
Transfer-Encoding:

chunked
```

Chunked transfer encoding allows data to be streamed without knowing the total size in advance.

Proxy inconsistencies involving this header can contribute to HTTP Request Smuggling.

---

# Connection Header

Controls connection behavior.

Examples

```
Connection:

keep-alive
```

```
Connection:

close
```

Persistent connections improve performance by reducing connection overhead.

---

# Cache-Control

Controls caching behavior.

Example

```
Cache-Control:

no-store
```

Other directives

```
no-cache

private

public

max-age=3600
```

Sensitive information should generally not be cached by shared intermediaries.

---

# ETag

ETag uniquely identifies a resource version.

Example

```
ETag:

"abc123"
```

Clients use ETags to determine whether cached content is still valid.

---

# If-None-Match

Conditional requests use ETags.

Example

```
If-None-Match:

"abc123"
```

If the resource has not changed,

```
304 Not Modified
```

is returned.

Conditional requests reduce bandwidth consumption.

---

# Last-Modified

Indicates when a resource was last updated.

Example

```
Last-Modified:

Tue, 15 Jul 2025 10:00:00 GMT
```

Clients may use this value to validate cached resources.

---

# If-Modified-Since

Example

```
If-Modified-Since:

Tue, 15 Jul 2025 10:00:00 GMT
```

If the resource has not changed,

```
304 Not Modified
```

is returned.

---

# Location Header

Used during redirection.

Example

```
HTTP/1.1 302 Found

Location:

https://example.com/login
```

Applications should validate redirect destinations to avoid open redirect vulnerabilities.

---

# WWW-Authenticate

Servers use this header to request authentication.

Example

```
WWW-Authenticate:

Basic realm="Admin"
```

Browsers respond by prompting users for credentials when appropriate.

---

# Allow Header

Indicates supported HTTP methods.

Example

```
Allow:

GET

POST

PUT
```

This header commonly appears in responses to `OPTIONS` requests.

---

# Vary Header

The `Vary` header informs caches which request headers influence the response.

Example

```
Vary:

Accept-Encoding
```

Proper use prevents caches from serving incorrect representations to clients.

---

# Common Enterprise Request Flow

```
Client

 │

Host

Authorization

Accept

User-Agent

Origin

Cookie

 │

 ▼

API Gateway

 │

Authentication

 │

Application

 ▼

Response
```

Each header contributes to routing, authentication, negotiation, or session management.

---

# Enterprise Example

An authenticated API request

```
GET /api/orders/100 HTTP/1.1

Host: api.company.com

Authorization: Bearer <JWT>

Accept: application/json

Origin: https://portal.company.com

User-Agent: Chrome
```

The server evaluates:

- Host routing
- Authentication
- Authorization
- Origin validation
- Content negotiation

before returning the response.

---

# Best Practices

General

- Validate expected headers.
- Reject malformed headers.
- Use HTTPS for all sensitive traffic.
- Normalize header processing.
- Log security-relevant headers.

Authentication

- Protect Authorization headers.
- Rotate tokens regularly.
- Never expose credentials in URLs.

Caching

- Prevent caching of sensitive responses.
- Use ETags appropriately.
- Configure cache directives carefully.

Operations

- Remove unnecessary headers.
- Minimize information disclosure.
- Monitor unusual header values.

---

# Common Mistakes

Avoid:

- Trusting User-Agent values
- Accepting arbitrary Host headers
- Caching authenticated responses improperly
- Exposing sensitive information in Referer URLs
- Ignoring malformed Content-Type values
- Logging sensitive Authorization headers in plaintext
- Returning unnecessary server information

---

# Key Takeaways

- HTTP headers provide metadata that controls request and response processing.
- Request and response headers serve different purposes.
- Authentication, caching, routing, and content negotiation rely heavily on headers.
- Sensitive headers such as `Authorization` and `Cookie` require strong protection.
- Proper validation and monitoring of HTTP headers are essential for secure API deployments.

---

**Next:** HTTP Security Headers, Cookie Security, CORS Headers, CSP, HSTS, Header Injection Attacks, HTTP Request Smuggling, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.