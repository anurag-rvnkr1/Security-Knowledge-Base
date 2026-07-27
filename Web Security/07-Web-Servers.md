# 07-Web-Servers.md

# Part 1 — Introduction to Web Servers, Architecture, Request Processing, Server Components, and Enterprise Web Server Fundamentals

> **"A web server is the backbone of every web application. It receives client requests, processes them, serves resources, communicates with applications, and enforces critical security controls before any webpage reaches the user's browser."**

---

# Learning Objectives

After completing this part, you will understand:

- What a Web Server is
- Evolution of Web Servers
- Static vs Dynamic Content
- Web Server Architecture
- Request Processing Lifecycle
- Components of a Web Server
- Common Web Servers
- Enterprise Web Server Deployment
- Web Server Responsibilities
- Web Server Security Overview

---

# Introduction

Whenever you open a website:

```
https://example.com
```

the browser sends an HTTP request.

```
Browser

↓

Internet

↓

Web Server

↓

Application

↓

Database

↓

Response

↓

Browser
```

The **Web Server** is the first system that receives the request.

---

# What is a Web Server?

A **Web Server** is software (and sometimes the underlying hardware) that accepts HTTP/HTTPS requests, processes them or forwards them to applications, and returns responses to clients.

A web server can:

- Serve static files
- Reverse proxy requests
- Terminate TLS
- Compress responses
- Cache content
- Authenticate users
- Log requests
- Enforce security policies

---

# Physical vs Software Web Server

The term **Web Server** may refer to:

```
Physical Server

↓

Runs

↓

Web Server Software
```

Example:

```
Dell PowerEdge

↓

Ubuntu Linux

↓

Nginx

↓

Website
```

---

# Static Content

Static content is delivered exactly as stored.

Examples:

- HTML
- CSS
- JavaScript
- Images
- PDFs
- Videos

```
Browser

↓

GET /logo.png

↓

Web Server

↓

logo.png

↓

Browser
```

No application logic is required.

---

# Dynamic Content

Dynamic content is generated at runtime.

```
Browser

↓

GET /dashboard

↓

Web Server

↓

Application

↓

Database

↓

Generated HTML

↓

Browser
```

The response depends on user data or application logic.

---

# Static vs Dynamic Content

| Static Content | Dynamic Content |
|----------------|-----------------|
| Pre-existing files | Generated on demand |
| Faster delivery | Requires application processing |
| No database needed | Often uses databases |
| Low CPU usage | Higher CPU usage |
| Easy to cache | Selective caching |

---

# Responsibilities of a Web Server

A modern web server performs many tasks.

```
Receive Request

↓

Validate Request

↓

TLS Processing

↓

Authentication

↓

Routing

↓

Static File Handling

↓

Reverse Proxy

↓

Compression

↓

Logging

↓

Response
```

---

# High-Level Web Server Architecture

```
                Browser
                   │
                   ▼
           Internet / Network
                   │
                   ▼
            Web Server (Nginx)
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Static Content        Application Server
                               │
                               ▼
                           Database
```

---

# Request Lifecycle

A request follows several stages.

```
User

↓

Browser

↓

DNS

↓

TCP

↓

TLS

↓

HTTP Request

↓

Web Server

↓

Application

↓

Database

↓

HTTP Response

↓

Browser
```

---

# Web Server Components

A web server contains multiple modules.

```
Web Server

│

├── Listener

├── Request Parser

├── Routing

├── TLS Module

├── Static File Handler

├── Reverse Proxy

├── Compression Module

├── Logging Module

└── Cache
```

---

# Listener

The Listener waits for incoming network connections.

```
Port 80

↓

HTTP Listener

────────────

Port 443

↓

HTTPS Listener
```

When a client connects, the request enters the processing pipeline.

---

# Request Parser

The parser extracts information from incoming requests.

Example:

```
GET /login HTTP/1.1

Host: example.com

User-Agent: Chrome
```

The parser identifies:

- HTTP Method
- URL
- Headers
- Cookies
- Body
- Protocol Version

---

# Routing

The web server determines where the request should go.

Example:

```
GET /images/logo.png

↓

Static File
```

```
GET /dashboard

↓

Application
```

Routing rules define this behavior.

---

# Static File Handler

Handles requests for stored files.

```
Client

↓

GET style.css

↓

Web Server

↓

style.css

↓

Response
```

Static file delivery is highly optimized.

---

# Reverse Proxy

Modern web servers commonly act as reverse proxies.

```
Client

↓

Web Server

↓

Application Server

↓

Response
```

The client communicates only with the web server.

---

# Why Reverse Proxy?

Advantages include:

- Security
- Load balancing
- TLS termination
- Request filtering
- Central logging
- Caching

---

# Reverse Proxy Example

```
Internet

↓

Nginx

├── App Server 1

├── App Server 2

└── App Server 3
```

Requests are distributed among backend servers.

---

# Compression Module

Responses can be compressed before transmission.

```
HTML

↓

Compression

↓

Smaller Response

↓

Browser
```

Benefits:

- Faster downloads
- Lower bandwidth usage
- Improved page load time

Common algorithms include Gzip and Brotli.

---

# Caching

Frequently requested resources may be cached.

```
Request

↓

Cache Hit?

↓

Yes

↓

Cached Response

────────────

No

↓

Application

↓

Cache

↓

Response
```

Caching improves scalability and reduces backend load.

---

# Logging Module

Every request can be recorded.

Example log fields:

- Timestamp
- Client IP
- Method
- URL
- Status Code
- Bytes Sent
- User Agent
- Response Time

Logs support:

- Monitoring
- Troubleshooting
- Incident Response
- Compliance

---

# Popular Web Servers

| Web Server | Description |
|-------------|-------------|
| Nginx | High-performance web server and reverse proxy |
| Apache HTTP Server | Feature-rich and highly configurable |
| Microsoft IIS | Integrated with Windows Server |
| Caddy | Automatic HTTPS support |
| LiteSpeed | Commercial high-performance server |

---

# Apache HTTP Server

Characteristics:

- Open source
- Module-based
- Mature ecosystem
- Flexible configuration
- Broad compatibility

Common uses:

- Enterprise applications
- Legacy systems
- Shared hosting

---

# Nginx

Characteristics:

- Event-driven architecture
- Low memory usage
- Excellent concurrency
- Reverse proxy support
- Load balancing

Widely used for:

- Cloud deployments
- APIs
- Microservices
- High-traffic websites

---

# Microsoft IIS

Runs on Windows Server.

Common enterprise integrations:

- Active Directory
- ASP.NET
- Windows Authentication
- Microsoft ecosystem

---

# Caddy

Known for:

- Automatic TLS certificate management
- Simple configuration
- HTTP/2 support
- Modern defaults

Popular for smaller deployments and development environments.

---

# Enterprise Deployment Example

```
Internet

↓

Firewall

↓

Load Balancer

↓

Web Server Cluster

↓

Application Servers

↓

Database Cluster
```

Multiple web servers improve availability and scalability.

---

# Web Server Security Responsibilities

A web server is the first line of defense.

Responsibilities include:

- TLS enforcement
- Security headers
- Access control
- Request validation
- Rate limiting
- Logging
- Reverse proxy protection

---

# Real Enterprise Example

An employee opens:

```
https://portal.company.com
```

Flow:

```
Browser

↓

DNS

↓

Firewall

↓

Load Balancer

↓

Nginx

↓

Authentication Service

↓

Application

↓

Database

↓

Response

↓

Browser
```

The web server validates and routes every request before it reaches the application.

---

# Hands-on Lab (Conceptual)

Install a web server such as **Nginx** or **Apache** in a lab environment.

Practice:

1. Start the web server.
2. Place an `index.html` file in the document root.
3. Visit `http://localhost`.
4. Observe the response.
5. Review the access log after refreshing the page multiple times.

---

# Interview Questions

1. What is a Web Server?
2. What is the difference between static and dynamic content?
3. What are the primary responsibilities of a web server?
4. What is a reverse proxy?
5. Why is caching important?
6. What information is stored in web server logs?
7. Compare Apache and Nginx.
8. Why is TLS often terminated at the web server?
9. What is the purpose of a request parser?
10. Why are web servers critical for web application security?

---

# Best Practices

- Keep web server software updated.
- Disable unnecessary modules.
- Serve static assets efficiently.
- Enable HTTPS by default.
- Implement centralized logging.
- Use reverse proxies for backend protection.
- Configure appropriate caching policies.
- Restrict administrative interfaces.

---

# Common Mistakes

- Exposing backend application servers directly to the Internet.
- Running outdated web server software.
- Leaving default configurations unchanged.
- Disabling logging.
- Serving sensitive files from public directories.
- Misconfiguring TLS settings.

---

# Key Takeaways

- A web server receives, processes, and responds to HTTP/HTTPS requests.
- Modern web servers handle routing, caching, compression, logging, TLS termination, and reverse proxying.
- Static content is served directly, while dynamic content is generated by backend applications.
- Enterprise deployments commonly place web servers behind firewalls and load balancers.
- Understanding web server architecture is fundamental for web development, penetration testing, and cybersecurity.

```text id="jid720"
**Next:** Part 2
```