# 03-HTTP-Protocol.md

# Part 1 — Introduction to HTTP, HTTP Architecture, Request-Response Model, Methods, and Message Structure

> **"HTTP is the language of the Web. Every browser, API, mobile application, and web server communicates using HTTP or HTTPS."**

---

# Learning Objectives

After completing this part, you will understand:

- What HTTP is
- Why HTTP is important
- Client-Server communication
- HTTP architecture
- HTTP request-response model
- Stateless communication
- HTTP methods
- HTTP message structure
- HTTP headers
- HTTP body
- Enterprise HTTP communication

---

# Introduction

Every time you:

- Visit a website
- Login to an application
- Search on Google
- Watch YouTube
- Shop online
- Use a REST API

HTTP is working behind the scenes.

Without HTTP, modern web applications could not communicate.

---

# What is HTTP?

**HTTP (HyperText Transfer Protocol)** is an application-layer protocol used to exchange information between clients and servers.

It defines:

- How requests are sent
- How responses are returned
- How resources are identified
- How communication is structured

HTTP does **not** define how data travels across networks—that responsibility belongs to lower-layer protocols such as TCP/IP.

---

# Why is HTTP Important?

HTTP provides a standardized way for different systems to communicate.

Examples:

```
Browser

↓

HTTP

↓

Web Server
```

```
Mobile App

↓

HTTP

↓

API Server
```

```
IoT Device

↓

HTTP

↓

Cloud Platform
```

---

# Where HTTP Fits

```
Application Layer

↓

HTTP

↓

TLS (HTTPS)

↓

TCP

↓

IP

↓

Network
```

HTTP operates at the **Application Layer**.

---

# HTTP Communication Model

```
Client

↓

HTTP Request

↓

Server

↓

HTTP Response

↓

Client
```

This is known as the **Request-Response Model**.

---

# Client

The client initiates communication.

Examples:

- Chrome
- Firefox
- Edge
- Safari
- Mobile App
- Desktop Application
- API Client

Responsibilities:

- Create requests
- Send requests
- Receive responses
- Display or process data

---

# Server

The server waits for incoming requests.

Responsibilities:

- Process requests
- Authenticate users
- Execute business logic
- Access databases
- Generate responses

---

# Simple Example

User visits:

```
https://shop.example.com
```

Browser sends:

```http
GET / HTTP/1.1
Host: shop.example.com
```

Server replies:

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

---

# Request-Response Lifecycle

```
Browser

↓

Create Request

↓

Send Request

↓

Server Processes

↓

Generate Response

↓

Browser Receives Response

↓

Render Page
```

---

# HTTP is Stateless

One of HTTP's most important characteristics is that it is **stateless**.

Each request is independent.

```
Request 1

↓

Response

────────────

Request 2

↓

Response
```

The server does **not automatically remember** previous requests.

---

# Why Stateless?

Benefits include:

- Simpler protocol
- Better scalability
- Easier load balancing
- Independent requests

However, applications often need to remember users.

This is achieved using mechanisms such as:

- Cookies
- Sessions
- Tokens

These are built **on top of HTTP**, not into HTTP itself.

---

# Example of Stateless Communication

User requests:

```
GET /profile
```

Server processes the request.

Later:

```
GET /orders
```

Unless additional information (such as a session cookie or token) accompanies the second request, the server treats it as a new request.

---

# Resources

Everything accessed through HTTP is considered a **resource**.

Examples:

```
/

/products

/users

/images/logo.png

/api/orders
```

Resources may represent:

- HTML pages
- Images
- Videos
- JSON data
- Documents
- APIs

---

# URI vs URL

A **URI (Uniform Resource Identifier)** identifies a resource.

A **URL (Uniform Resource Locator)** is a type of URI that specifies where and how to access a resource.

Example:

```
https://example.com/products
```

This is a URL because it specifies:

- Protocol
- Host
- Resource location

---

# HTTP Methods

HTTP methods describe the intended action.

```
Client

↓

HTTP Method

↓

Server Action
```

---

# GET

Purpose:

Retrieve data.

Example:

```http
GET /products
```

Should not modify server data.

---

# POST

Purpose:

Create or submit data.

Example:

```http
POST /orders
```

Often used for:

- Registration
- Login
- Form submission
- Creating resources

---

# PUT

Purpose:

Replace an existing resource.

Example:

```http
PUT /users/15
```

---

# PATCH

Purpose:

Update part of a resource.

Example:

```http
PATCH /users/15
```

---

# DELETE

Purpose:

Remove a resource.

Example:

```http
DELETE /users/15
```

---

# HEAD

Returns only the response headers without the response body.

Useful for:

- Checking resource availability
- Retrieving metadata
- Cache validation

---

# OPTIONS

Used to discover which HTTP methods are supported.

Example:

```
OPTIONS /api/users
```

Often seen in CORS-related communication.

---

# TRACE

Requests that the server return the received request.

Because it can expose diagnostic information, many production systems disable it unless specifically required.

---

# CONNECT

Used to establish a tunnel to another server.

Commonly used by:

- HTTPS proxies
- Forward proxies

---

# HTTP Method Summary

| Method | Purpose | Safe | Idempotent |
|---------|----------|------|------------|
| GET | Retrieve resource | ✓ | ✓ |
| HEAD | Retrieve headers | ✓ | ✓ |
| OPTIONS | Discover capabilities | ✓ | ✓ |
| POST | Create/Submit | ✗ | ✗ |
| PUT | Replace resource | ✗ | ✓ |
| PATCH | Partial update | ✗ | Depends on implementation |
| DELETE | Delete resource | ✗ | ✓ |
| TRACE | Diagnostic | ✓ | ✓ |
| CONNECT | Tunnel | ✗ | No |

---

# Safe Methods

Safe methods should not change server state.

Examples:

- GET
- HEAD
- OPTIONS

---

# Idempotent Methods

A method is **idempotent** if repeating the same request produces the same intended server state.

Example:

```
DELETE /users/10
```

Whether executed once or multiple times, the intended outcome remains that the resource is deleted.

---

# Anatomy of an HTTP Request

```
Request Line

↓

Headers

↓

Blank Line

↓

Body (Optional)
```

---

# Example HTTP Request

```http
POST /login HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Content-Type: application/json

{
  "username":"alice",
  "password":"********"
}
```

---

# Request Line

```
POST /login HTTP/1.1
```

Contains:

- Method
- Target resource
- HTTP version

---

# Headers

Headers provide metadata.

Examples:

- Host
- User-Agent
- Accept
- Authorization
- Cookie
- Content-Type
- Content-Length

---

# Blank Line

Separates the headers from the message body.

---

# Request Body

The body carries data sent to the server.

Common formats:

- JSON
- XML
- HTML forms
- Multipart form-data
- Plain text

---

# Enterprise Example

A banking application receives:

```http
POST /transfer HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "fromAccount":"12345",
  "toAccount":"67890",
  "amount":2500
}
```

The server validates:

- Authentication
- Authorization
- Input
- Business rules
- Account balance

before processing the transfer.

---

# Hands-on Lab (Conceptual)

Open your browser's Developer Tools.

1. Visit a website.
2. Open the **Network** tab.
3. Select the first request.
4. Observe:
   - Request method
   - URL
   - Request headers
   - Request body (if present)
   - Response status

Try comparing a normal page load (GET) with submitting a form (POST).

---

# Interview Questions

1. What is HTTP?
2. Why is HTTP called a stateless protocol?
3. What is the Request-Response model?
4. What is the difference between a client and a server?
5. Explain GET and POST.
6. What is an HTTP resource?
7. What is the difference between a URI and a URL?
8. What is an idempotent HTTP method?
9. What are HTTP headers?
10. Why are cookies and sessions needed if HTTP is stateless?

---

# Best Practices

- Use the correct HTTP method for the intended action.
- Avoid using GET for operations that modify data.
- Keep requests simple and well-structured.
- Validate all client input on the server.
- Use HTTPS to protect HTTP communication.

---

# Common Mistakes

- Assuming HTTP remembers previous requests.
- Sending sensitive information in URLs.
- Misusing POST for every operation.
- Ignoring method semantics.
- Exposing unnecessary request metadata.

---

# Key Takeaways

- HTTP is the application-layer protocol that powers web communication.
- It follows a stateless request-response model.
- Clients initiate requests, and servers generate responses.
- HTTP methods define the intended action on a resource.
- Requests consist of a request line, headers, an optional body, and use standardized message formats.

```

# 03-HTTP-Protocol.md

# Part 2 — HTTP Responses, Status Codes, Headers, Content Types, Cookies, Caching, and Content Negotiation

> **"An HTTP response tells the client not only what happened, but also how to interpret, cache, secure, and display the returned data."**

---

# Learning Objectives

After completing this part, you will understand:

- HTTP response structure
- HTTP status codes
- Response headers
- Content types (MIME types)
- Cookies (overview)
- Caching
- Content negotiation
- Compression
- Redirects
- Enterprise response processing

---

# Recap

The client sends an HTTP request.

```
Client

↓

HTTP Request

↓

Server
```

The server processes the request and returns an HTTP response.

```
Server

↓

HTTP Response

↓

Client
```

---

# HTTP Response Structure

An HTTP response consists of:

```
Status Line

↓

Headers

↓

Blank Line

↓

Response Body
```

---

# Example Response

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 2048

<html>
...
</html>
```

---

# Response Lifecycle

```
Server

↓

Business Logic

↓

Generate Response

↓

Add Headers

↓

Send Response

↓

Browser Processes Response
```

---

# Status Line

The first line contains:

```
HTTP Version

↓

Status Code

↓

Reason Phrase
```

Example:

```http
HTTP/1.1 404 Not Found
```

---

# Why Status Codes Matter

Status codes tell the client:

- Success
- Failure
- Redirect
- Authentication required
- Server problems

Applications, browsers, APIs, and automation tools rely heavily on these codes.

---

# Status Code Categories

| Range | Category |
|--------|----------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Errors |
| 5xx | Server Errors |

---

# 1xx — Informational

These indicate that the request has been received and processing is continuing.

Common examples:

| Code | Meaning |
|------|---------|
|100|Continue|
|101|Switching Protocols|
|103|Early Hints|

These responses are less common in everyday web browsing.

---

# 2xx — Success

The request completed successfully.

Common codes:

| Code | Meaning |
|------|---------|
|200|OK|
|201|Created|
|202|Accepted|
|204|No Content|

---

## 200 OK

Most common success response.

Example:

```http
GET /products

↓

200 OK
```

---

## 201 Created

A new resource has been created.

Example:

```http
POST /users

↓

201 Created
```

---

## 202 Accepted

The request has been accepted for processing but is not yet complete.

Often used for:

- Background jobs
- Asynchronous processing
- Queue-based systems

---

## 204 No Content

Successful request.

No response body is returned.

Commonly used after:

- DELETE
- AJAX updates
- API operations

---

# 3xx — Redirection

The client should perform another action.

Common codes:

| Code | Meaning |
|------|---------|
|301|Moved Permanently|
|302|Found (Temporary Redirect)|
|303|See Other|
|304|Not Modified|
|307|Temporary Redirect|
|308|Permanent Redirect|

---

## 301 Moved Permanently

Used when a resource has permanently moved.

```
Old URL

↓

301

↓

New URL
```

Search engines update their indexes accordingly.

---

## 302 Found

Temporary redirect.

Clients should continue using the original URL for future requests unless instructed otherwise.

---

## 304 Not Modified

Used with caching.

```
Browser Cache

↓

Check Resource

↓

304

↓

Use Cached Version
```

Reduces bandwidth and improves performance.

---

# 4xx — Client Errors

The problem is with the client's request.

Common codes:

| Code | Meaning |
|------|---------|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|405|Method Not Allowed|
|408|Request Timeout|
|409|Conflict|
|410|Gone|
|413|Content Too Large|
|415|Unsupported Media Type|
|422|Unprocessable Content|
|429|Too Many Requests|

---

## 400 Bad Request

The server cannot understand the request.

Possible reasons:

- Invalid JSON
- Missing fields
- Malformed syntax

---

## 401 Unauthorized

Authentication is required or has failed.

Example:

```
Access Protected Resource

↓

No Valid Credentials

↓

401
```

---

## 403 Forbidden

The client is authenticated but lacks permission.

```
User

↓

Admin Page

↓

403 Forbidden
```

---

## 404 Not Found

The requested resource does not exist.

Example:

```
/products/999999

↓

404
```

---

## 405 Method Not Allowed

The requested HTTP method is not permitted.

Example:

```
DELETE /profile

↓

405
```

---

## 409 Conflict

The request conflicts with the current state of the resource.

Example:

- Editing stale data
- Duplicate usernames
- Version conflicts

---

## 415 Unsupported Media Type

Example:

```
Server expects JSON

↓

Client sends XML

↓

415
```

---

## 422 Unprocessable Content

The request format is valid, but the content fails validation.

Example:

```
Email format invalid

↓

422
```

---

## 429 Too Many Requests

The client exceeded rate limits.

Commonly used to help mitigate abuse or excessive automated requests.

---

# 5xx — Server Errors

Something failed on the server.

Common codes:

| Code | Meaning |
|------|---------|
|500|Internal Server Error|
|501|Not Implemented|
|502|Bad Gateway|
|503|Service Unavailable|
|504|Gateway Timeout|

---

## 500 Internal Server Error

Unexpected server failure.

Possible causes:

- Unhandled exceptions
- Database failure
- Programming errors
- Misconfiguration

---

## 502 Bad Gateway

A gateway or proxy received an invalid response from an upstream server.

---

## 503 Service Unavailable

The server is temporarily unavailable.

Reasons:

- Maintenance
- Heavy load
- Resource exhaustion

---

## 504 Gateway Timeout

A gateway or proxy timed out waiting for another server.

---

# Complete Status Code Flow

```
Request

↓

Server

↓

Success?

│

├── Yes → 2xx

│

├── Redirect → 3xx

│

├── Client Error → 4xx

│

└── Server Error → 5xx
```

---

# Response Headers

Response headers provide metadata about the response.

Examples:

- Content-Type
- Content-Length
- Cache-Control
- Set-Cookie
- Location
- ETag
- Last-Modified
- Server

---

# Example Response Headers

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 125
Cache-Control: no-cache
```

---

# Content-Type

Specifies the response format.

Examples:

| Content-Type | Meaning |
|--------------|----------|
|text/html|HTML document|
|text/plain|Plain text|
|text/css|CSS|
|application/json|JSON|
|application/xml|XML|
|application/pdf|PDF|
|image/png|PNG image|
|image/jpeg|JPEG image|

---

# MIME Types

A **MIME (Multipurpose Internet Mail Extensions) type** identifies the format of transmitted content.

Example:

```http
Content-Type: application/json
```

The browser uses this information to correctly process the response.

---

# Content-Length

Indicates the response size.

Example:

```http
Content-Length: 4096
```

---

# Location Header

Used with redirects.

Example:

```http
HTTP/1.1 301 Moved Permanently
Location: https://new.example.com
```

---

# Set-Cookie Header

The server asks the browser to store a cookie.

Example:

```http
Set-Cookie: sessionid=abc123
```

Cookies help maintain user state across multiple requests.

---

# Cache-Control

Controls how responses may be cached.

Examples:

```http
Cache-Control: no-store
```

```http
Cache-Control: max-age=3600
```

Common directives include:

- no-store
- no-cache
- private
- public
- max-age

---

# ETag

An **Entity Tag (ETag)** uniquely identifies a version of a resource.

```
Browser

↓

Send ETag

↓

Server Compares

↓

304 or New Content
```

Helps reduce unnecessary downloads.

---

# Last-Modified

Indicates when a resource last changed.

Example:

```http
Last-Modified: Tue, 22 Jul 2026 10:00:00 GMT
```

Browsers can use this for cache validation.

---

# Cookies (Overview)

Servers use cookies to maintain state.

Example:

```
Login

↓

Server

↓

Set-Cookie

↓

Browser Stores Cookie

↓

Future Requests Include Cookie
```

Cookies are covered in detail in a later chapter.

---

# Response Compression

Large responses may be compressed before being sent.

```
Server

↓

Compress Response

↓

Browser

↓

Decompress

↓

Render
```

Common algorithms:

- gzip
- Brotli

Benefits:

- Reduced bandwidth
- Faster page loading

---

# Content Negotiation

The client tells the server what it can accept.

Example request:

```http
Accept: application/json
```

The server selects the most appropriate representation.

Common negotiation headers:

- Accept
- Accept-Language
- Accept-Encoding

---

# Redirect Workflow

```
Client

↓

GET /old-page

↓

301

↓

GET /new-page

↓

200 OK
```

---

# Enterprise Example

A customer requests:

```
GET /dashboard
```

The application responds:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Cache-Control: no-store
Set-Cookie: sessionid=xyz789
```

The browser:

- Processes headers
- Stores the session cookie
- Applies cache rules
- Renders the HTML

---

# Hands-on Lab (Conceptual)

Using your browser's Developer Tools:

1. Open the **Network** tab.
2. Select any request.
3. Inspect:
   - Status code
   - Response headers
   - Content-Type
   - Cache-Control
   - Content-Length
4. Reload the page and observe whether cached resources return `304 Not Modified`.

---

# Interview Questions

1. What is the structure of an HTTP response?
2. Explain the five HTTP status code categories.
3. What is the difference between 401 and 403?
4. When would a server return 304 Not Modified?
5. What is the purpose of the `Content-Type` header?
6. What is a MIME type?
7. What does the `Set-Cookie` header do?
8. What is the difference between 301 and 302 redirects?
9. Why is `429 Too Many Requests` important?
10. What is content negotiation?

---

# Best Practices

- Return accurate HTTP status codes.
- Use appropriate `Content-Type` headers.
- Disable caching for sensitive responses when appropriate.
- Use redirects correctly.
- Compress large responses to improve performance.
- Include only necessary response headers.

---

# Common Mistakes

- Returning `200 OK` for error conditions.
- Exposing sensitive server information in response headers.
- Caching authenticated pages improperly.
- Using incorrect MIME types.
- Confusing authentication failures (401) with authorization failures (403).

---

# Key Takeaways

- HTTP responses consist of a status line, headers, and an optional body.
- Status codes communicate the outcome of a request.
- Response headers control caching, cookies, redirects, content types, and other behaviors.
- MIME types tell clients how to interpret response data.
- Proper use of caching and content negotiation improves both performance and user experience.

```text id="jid720"
**Next:** Part 3
```