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

# HTTP Security Headers

Security headers instruct browsers how to securely process web content.

Unlike authentication or authorization mechanisms, security headers primarily provide **client-side protections** against common web attacks.

They help defend against:

- Cross-Site Scripting (XSS)
- Clickjacking
- MIME type confusion
- Protocol downgrade attacks
- Data leakage
- Cross-origin abuse
- Session hijacking

Security headers should be considered a mandatory part of every production web application and API deployment.

---

# Security Header Architecture

```
                 Client

                    │

             HTTP Request

                    │

                    ▼

               Web Server

                    │

        Security Response Headers

                    │

                    ▼

                 Browser

                    │

     Browser Security Enforcement
```

The browser enforces most security headers automatically.

---

# Common Security Headers

| Header | Purpose |
|---------|----------|
| Strict-Transport-Security | Force HTTPS |
| Content-Security-Policy | Restrict resource loading |
| X-Content-Type-Options | Prevent MIME sniffing |
| X-Frame-Options | Prevent clickjacking |
| Referrer-Policy | Control Referer information |
| Permissions-Policy | Restrict browser features |
| Cross-Origin-Resource-Policy | Resource isolation |
| Cross-Origin-Embedder-Policy | Secure embedding |
| Cross-Origin-Opener-Policy | Window isolation |

---

# Strict-Transport-Security (HSTS)

HSTS forces browsers to communicate only over HTTPS.

Example

```
Strict-Transport-Security:

max-age=31536000;

includeSubDomains;

preload
```

Workflow

```
Browser

 │

HTTPS Visit

 ▼

Receive HSTS

 │

Future Requests

 ▼

HTTPS Only
```

Benefits

- Prevents protocol downgrade
- Reduces SSL stripping attacks
- Enforces encrypted communication

---

# HSTS Attack Prevention

Without HSTS

```
Browser

 │

HTTP

 ▼

Attacker

 │

Intercept

 ▼

Server
```

With HSTS

```
Browser

 │

HTTPS Required

 ▼

Server
```

The browser refuses insecure HTTP connections after learning the HSTS policy.

---

# Content Security Policy (CSP)

Content Security Policy controls which resources the browser may load.

Example

```
Content-Security-Policy:

default-src 'self';

script-src 'self';

img-src https:;
```

CSP helps mitigate

- XSS
- Malicious scripts
- Data exfiltration
- Untrusted third-party resources

---

# CSP Architecture

```
Browser

 │

Load Script

 │

Allowed?

 ┌──────┴──────┐

Yes           No

 │             │

Execute     Block
```

Only resources matching the policy are executed.

---

# CSP Directives

Common directives

| Directive | Purpose |
|-----------|----------|
| default-src | Default resource policy |
| script-src | JavaScript sources |
| style-src | CSS sources |
| img-src | Image sources |
| connect-src | API endpoints |
| frame-src | Embedded frames |
| object-src | Plugins |
| font-src | Fonts |

---

# X-Content-Type-Options

This header prevents browsers from guessing MIME types.

Example

```
X-Content-Type-Options:

nosniff
```

Without this protection,

```
Image

↓

Interpreted

↓

JavaScript
```

may become possible under certain conditions.

Always use

```
nosniff
```

for production deployments.

---

# MIME Sniffing

Without protection

```
File

↓

Unknown Type

↓

Browser Guess

↓

Unexpected Execution
```

With `nosniff`

```
File

↓

Declared Type

↓

Validation

↓

Safe Handling
```

---

# X-Frame-Options

Prevents clickjacking attacks.

Example

```
X-Frame-Options:

DENY
```

Other values

```
SAMEORIGIN
```

Clickjacking example

```
Attacker Site

 │

Hidden Frame

 ▼

Bank Website

 ▼

Victim Clicks
```

X-Frame-Options prevents unauthorized framing.

---

# Clickjacking Protection

```
Browser

 │

Frame Request

 │

Allowed?

 ┌──────┴──────┐

No            Yes

 │             │

Blocked     Rendered
```

Modern applications often combine this with CSP's `frame-ancestors` directive.

---

# Referrer-Policy

Controls information sent in the `Referer` header.

Example

```
Referrer-Policy:

strict-origin-when-cross-origin
```

Possible values

- no-referrer
- same-origin
- origin
- strict-origin
- strict-origin-when-cross-origin

Benefits

- Reduced information leakage
- Improved privacy
- Better control over outbound requests

---

# Permissions-Policy

Controls browser features available to web pages.

Example

```
Permissions-Policy:

camera=(),

microphone=(),

geolocation=()
```

This limits unnecessary browser capabilities.

---

# Cross-Origin-Resource-Policy (CORP)

Restricts which origins may access resources.

Example

```
Cross-Origin-Resource-Policy:

same-origin
```

Benefits

- Better resource isolation
- Reduced cross-origin abuse
- Improved browser security

---

# Cross-Origin-Embedder-Policy (COEP)

Controls embedding of cross-origin resources.

Example

```
Cross-Origin-Embedder-Policy:

require-corp
```

Helps isolate documents and reduces certain cross-origin risks.

---

# Cross-Origin-Opener-Policy (COOP)

Separates browsing contexts.

Example

```
Cross-Origin-Opener-Policy:

same-origin
```

Benefits

- Process isolation
- Reduced cross-window attacks
- Improved browser security

---

# Cookie Security

Cookies frequently contain authentication sessions.

Secure cookie attributes are essential.

---

# Secure Attribute

Example

```
Set-Cookie:

SESSIONID=abc123;

Secure
```

The cookie is transmitted only over HTTPS.

---

# HttpOnly Attribute

Example

```
Set-Cookie:

SESSIONID=abc123;

HttpOnly
```

JavaScript cannot directly access the cookie.

This significantly reduces session theft through XSS.

---

# SameSite Attribute

Controls cross-site cookie behavior.

Example

```
SameSite=Strict
```

Other values

```
Lax

None
```

Benefits

- Reduces CSRF risk
- Limits cross-site cookie transmission

---

# Secure Cookie Example

```
Set-Cookie:

SESSIONID=abc123;

Secure;

HttpOnly;

SameSite=Strict
```

This combination provides strong baseline protection for session cookies.

---

# CORS Response Headers

Common CORS headers include:

| Header | Purpose |
|---------|----------|
| Access-Control-Allow-Origin | Allowed origins |
| Access-Control-Allow-Methods | Allowed HTTP methods |
| Access-Control-Allow-Headers | Allowed request headers |
| Access-Control-Allow-Credentials | Cookie support |
| Access-Control-Max-Age | Cache preflight |

Proper CORS configuration is critical for browser-based APIs.

---

# Access-Control-Allow-Origin

Example

```
Access-Control-Allow-Origin:

https://portal.company.com
```

Avoid

```
*
```

when sensitive authenticated resources are involved.

---

# Access-Control-Allow-Methods

Example

```
Access-Control-Allow-Methods:

GET,

POST,

PUT,

DELETE
```

Only required methods should be exposed.

---

# Access-Control-Allow-Headers

Example

```
Access-Control-Allow-Headers:

Authorization,

Content-Type
```

Limit accepted headers to those genuinely required.

---

# Access-Control-Allow-Credentials

Example

```
Access-Control-Allow-Credentials:

true
```

When enabled,

- Cookies
- Client certificates
- Authentication headers

may be included in cross-origin requests where permitted.

---

# Access-Control-Max-Age

Example

```
Access-Control-Max-Age:

3600
```

Browsers cache successful preflight responses, reducing unnecessary OPTIONS requests.

---

# Security Header Assessment

During an assessment verify:

```
HTTPS

↓

HSTS

↓

CSP

↓

X-Frame-Options

↓

nosniff

↓

Cookie Security

↓

CORS

↓

Referrer Policy
```

Missing headers should be documented with associated risks.

---

# Header Injection

Header injection occurs when untrusted input influences HTTP headers.

Example

```
User Input

↓

Response Header

↓

Unexpected Header
```

Improper validation may lead to:

- Response splitting
- Cache poisoning
- Open redirects
- Information disclosure

---

# HTTP Response Splitting

Attack

```
User Input

↓

CRLF Injection

↓

Additional Header

↓

Modified Response
```

Applications should reject carriage return (`CR`) and line feed (`LF`) characters in header values.

---

# Host Header Injection

If applications trust the Host header,

```
Host:

attacker.example
```

may influence:

- Password reset links
- Redirects
- Absolute URLs
- Email generation

Always validate expected hostnames.

---

# HTTP Request Smuggling

Request smuggling exploits inconsistencies between intermediaries.

Example

```
Proxy

 │

Content-Length

 ▼

Backend

 │

Transfer-Encoding

 ▼

Different Interpretation
```

Potential impacts

- Cache poisoning
- Authentication bypass
- Request confusion
- Session hijacking

Proper proxy configuration and protocol compliance reduce this risk.

---

# Security Testing Checklist

Verify

- HSTS enabled
- CSP configured
- Secure cookies
- HttpOnly cookies
- SameSite cookies
- CORS restrictions
- Referrer policy
- Permissions policy
- No sensitive headers
- Correct cache directives

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Missing HSTS | HTTPS response without HSTS |
| Missing CSP | HTML responses lacking CSP |
| Weak Cookies | Missing Secure, HttpOnly, or SameSite |
| Host Header Abuse | Unexpected Host values |
| Header Injection | CRLF characters in header values |
| Excessive OPTIONS | High preflight request volume |
| TRACE Requests | TRACE observed in production |
| CORS Abuse | Repeated disallowed Origin values |

Detection rules should be validated against expected application behavior.

---

# SIEM Integration

Useful telemetry

```
Web Server Logs

        │

Proxy Logs

        │

API Gateway Logs

        │

Authentication Logs

        │

Security Header Validation

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Dashboard
```

Recommended alerts

- Missing security headers
- Host header anomalies
- Header injection attempts
- Repeated CORS failures
- Excessive preflight requests
- TRACE requests
- Cookie security violations

---

# Enterprise Security Architecture

```
                   Internet

                       │

                       ▼

              Load Balancer

                       │

                       ▼

             Web Application Firewall

                       │

                       ▼

                 API Gateway

                       │

                       ▼

              Application Server

                       │

        Security Response Headers

                       │

                       ▼

                   Browser

                       │

          Browser Security Controls

                       ▼

                 Protected User
```

Security headers complement—not replace—server-side security controls.

---

# Hands-on Lab 1 – Security Header Review

**Objective**

Review HTTP response headers in an authorized environment.

**Steps**

1. Send a request to the application.
2. Record all response headers.
3. Verify the presence of:
   - HSTS
   - CSP
   - X-Frame-Options
   - X-Content-Type-Options
   - Referrer-Policy
4. Document missing or misconfigured headers.

**Learning Outcomes**

- Security header identification
- Baseline security assessment
- Browser protection analysis

---

# Hands-on Lab 2 – Cookie Configuration Review

**Objective**

Assess session cookie security.

**Steps**

1. Authenticate to the application.
2. Inspect the `Set-Cookie` response header.
3. Verify:
   - Secure
   - HttpOnly
   - SameSite
4. Document any missing protections.

**Learning Outcomes**

- Cookie analysis
- Session security assessment
- Secure cookie configuration

---

# Hands-on Lab 3 – CORS Configuration Review

**Objective**

Review CORS policy.

**Steps**

1. Inspect CORS response headers.
2. Verify allowed origins, methods, and headers.
3. Confirm that credentials are permitted only when appropriate.
4. Record observations and recommendations.

**Learning Outcomes**

- CORS assessment
- Cross-origin policy analysis
- Header validation

---

# Common Security Mistakes

Avoid:

- Missing HSTS
- Missing CSP
- Missing Secure cookies
- Missing HttpOnly
- Missing SameSite
- Overly permissive CORS
- Trusting Host headers
- Verbose Server headers
- Missing Referrer-Policy
- Ignoring header injection risks

---

# Troubleshooting

## Mixed Content Warning

Possible causes

- HTTP resources on HTTPS pages
- Missing HSTS
- Incorrect resource URLs

---

## CSP Violations

Possible causes

- Blocked scripts
- Missing allowed domains
- Incorrect directives

---

## CORS Failure

Possible causes

- Invalid origin
- Missing response headers
- Incorrect preflight handling

---

## Session Cookie Not Sent

Possible causes

- Missing Secure
- SameSite restrictions
- Domain mismatch
- Path mismatch

---

## Missing Security Headers

Possible causes

- Reverse proxy configuration
- Web server configuration
- Application middleware
- CDN configuration

---

# Interview Questions

## Fundamental

1. What are HTTP headers?
2. What is the purpose of HSTS?
3. What does Content Security Policy protect against?
4. Why is `X-Content-Type-Options: nosniff` important?
5. What is clickjacking?
6. Why should cookies use the HttpOnly attribute?
7. What is the purpose of the SameSite cookie attribute?
8. What does the Origin header represent?
9. Why is the Host header security-sensitive?
10. What is CORS?

---

## Intermediate

11. Explain the difference between HSTS and HTTPS.
12. How would you secure session cookies?
13. What are the risks of `Access-Control-Allow-Origin: *`?
14. Explain Host Header Injection.
15. What is HTTP Response Splitting?
16. How would you assess security headers during a penetration test?
17. Which headers are essential for browser security?
18. How would you detect header injection attempts?
19. What events related to HTTP headers should be forwarded to a SIEM?
20. Explain how HTTP Request Smuggling can arise from inconsistent header parsing.

---

## Scenario-Based

**Scenario 1**

A penetration test finds that the application returns authenticated session cookies without the `HttpOnly` attribute.

- What attacks become more feasible?
- How would you remediate the issue?

---

**Scenario 2**

A production API responds with:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

- Why is this configuration dangerous?
- What changes would you recommend?

---

**Scenario 3**

Your SOC detects repeated requests with unexpected Host header values.

- Which attacks could this indicate?
- Which logs and infrastructure components would you investigate?

---

# Chapter Summary

In this chapter, we explored HTTP headers and their role in application security.

We covered:

- Request headers
- Response headers
- Security headers
- Cookie security
- CORS headers
- Header injection
- Host Header Injection
- HTTP Request Smuggling
- Detection engineering
- SIEM integration
- Hands-on exercises
- Troubleshooting
- Interview preparation

Correct use of HTTP headers strengthens browser security, protects user sessions, improves API resilience, and provides valuable telemetry for enterprise monitoring.

---

# Chapter Review

You should now be able to answer:

- Which HTTP headers are security-critical?
- How do HSTS and CSP improve browser security?
- Why should session cookies include Secure, HttpOnly, and SameSite?
- How can Host Header Injection affect an application?
- Why is proper CORS configuration important?
- Which HTTP header anomalies should be monitored in a SIEM?
- How would you evaluate HTTP security headers during a security assessment?

If you can confidently answer these questions, you are ready to continue with **Chapter 09 – Authentication**, where you'll explore identity verification mechanisms, password security, multi-factor authentication, API keys, tokens, enterprise identity providers, and authentication attacks.

---

# References

## Standards

- RFC 9110 – HTTP Semantics
- RFC 6797 – HTTP Strict Transport Security (HSTS)
- Content Security Policy Level 3
- Fetch Standard (CORS)

## Security Standards

- OWASP ASVS
- OWASP API Security Top 10
- OWASP Secure Headers Project
- NIST SP 800-63 Digital Identity Guidelines
- NIST Cybersecurity Framework (CSF)

## Further Reading

- Mozilla Web Security Guidelines
- OWASP Cheat Sheet Series
- Web Application Security Best Practices

---

# What's Next?

➡️ **Chapter 09 – Authentication**

In the next chapter, we will explore:

- Authentication fundamentals
- Identity and trust
- Authentication factors
- Password-based authentication
- Multi-Factor Authentication (MFA)
- API Keys
- Certificates
- Enterprise Identity Providers
- Authentication attacks
- Detection engineering
- Hands-on labs
- Interview questions