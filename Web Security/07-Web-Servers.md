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


```

# 07-Web-Servers.md

# Part 2 — Web Server Internals, Connection Handling, Threading Models, Event-Driven Architecture, Virtual Hosts, Reverse Proxy, and Load Balancing

> **"Modern web servers are designed to handle millions of concurrent requests efficiently. Understanding their internal architecture is essential for developers, system administrators, SOC analysts, and penetration testers."**

---

# Learning Objectives

After completing this part, you will understand:

- Web server internals
- Request processing pipeline
- Process-based architecture
- Thread-based architecture
- Event-driven architecture
- Worker processes
- Virtual Hosts
- Name-based vs IP-based Virtual Hosting
- Reverse Proxy architecture
- Load Balancing
- Session persistence
- Enterprise deployment models

---

# Recap

In Part 1, we learned:

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
```

Now we'll explore **how the web server processes requests internally**.

---

# Internal Request Processing

When a request reaches a web server:

```
Incoming Request

↓

TCP Listener

↓

HTTP Parser

↓

Configuration Lookup

↓

Routing

↓

Authentication

↓

Static File?

↓

Yes → Serve File

↓

No

↓

Application Server

↓

Response

↓

Logging

↓

Client
```

Every request passes through multiple stages before a response is sent.

---

# Request Lifecycle Inside the Server

```
Socket Accept

↓

Parse Request

↓

Validate Headers

↓

Match Virtual Host

↓

Security Checks

↓

Route Request

↓

Generate Response

↓

Compress

↓

Log

↓

Send Response
```

---

# Listening Socket

A web server continuously listens for incoming connections.

Example:

```
HTTP

↓

Port 80

────────────

HTTPS

↓

Port 443
```

The operating system notifies the server when a new connection arrives.

---

# Socket Lifecycle

```
Client Connects

↓

TCP Handshake

↓

Socket Created

↓

Request Received

↓

Response Sent

↓

Socket Closed
```

Persistent connections may keep the socket open for additional requests.

---

# Connection Queue

If many clients connect simultaneously:

```
Incoming Clients

↓

Connection Queue

↓

Worker Available?

↓

Yes

↓

Process Request

────────────

No

↓

Wait
```

Proper queue sizing improves reliability during traffic spikes.

---

# Process-Based Architecture

Older web servers often created separate processes.

```
Master Process

│

├── Worker Process 1

├── Worker Process 2

├── Worker Process 3

└── Worker Process 4
```

Each process handles independent requests.

---

# Advantages

- Strong isolation
- Stable
- Simple implementation

---

# Disadvantages

- Higher memory usage
- Slower process creation
- Context switching overhead

---

# Thread-Based Architecture

Some servers use multiple threads.

```
Master Process

│

├── Thread 1

├── Thread 2

├── Thread 3

└── Thread 4
```

Threads share memory within the same process.

---

# Advantages

- Lower memory consumption
- Faster context switching
- Better scalability than multiple processes

---

# Disadvantages

- Shared memory complexity
- Synchronization challenges
- Thread safety concerns

---

# Event-Driven Architecture

Modern high-performance servers (such as Nginx) use an event-driven model.

```
Worker

↓

Event Loop

↓

Connection 1

Connection 2

Connection 3

Connection 10000
```

One worker can manage thousands of simultaneous idle or active connections efficiently.

---

# Event Loop

Instead of waiting for one request:

```
Worker

↓

Check Events

↓

Ready Connection?

↓

Process

↓

Return

↓

Next Event
```

The worker continuously handles available events.

---

# Event-Driven vs Thread-Based

| Event-Driven | Thread-Based |
|--------------|--------------|
| Excellent for high concurrency | Good for moderate concurrency |
| Lower memory usage | Higher memory usage |
| Fewer threads | Many threads |
| Efficient for I/O-heavy workloads | Simpler programming model |

---

# Worker Processes

Many event-driven servers still use multiple workers.

```
Master

│

├── Worker 1

├── Worker 2

├── Worker 3

└── Worker 4
```

The operating system distributes connections among workers.

---

# Master Process

The master process manages:

- Configuration
- Worker creation
- Graceful reloads
- Signal handling
- Process monitoring

Workers handle actual client traffic.

---

# Graceful Reload

Configuration changes can often be applied without downtime.

```
Administrator

↓

Reload Configuration

↓

Start New Workers

↓

Finish Existing Requests

↓

Old Workers Exit
```

This minimizes service interruption.

---

# Virtual Hosting

One server can host multiple websites.

```
Server

│

├── company.com

├── api.company.com

├── blog.company.com

└── shop.company.com
```

Each site can have separate configurations.

---

# Why Virtual Hosts?

Benefits:

- Lower infrastructure costs
- Easier management
- Better resource utilization
- Centralized administration

---

# Name-Based Virtual Hosting

Selection is based on the HTTP `Host` header.

Example:

```
Host: company.com
```

↓

```
Website A
```

```
Host: blog.company.com
```

↓

```
Website B
```

Most modern deployments use this approach.

---

# IP-Based Virtual Hosting

Different websites use different IP addresses.

```
203.0.113.10

↓

Site A

────────────

203.0.113.20

↓

Site B
```

Less common today due to IPv4 scarcity.

---

# Name-Based vs IP-Based Virtual Hosting

| Name-Based | IP-Based |
|------------|-----------|
| Uses Host header | Uses unique IP address |
| Conserves IP addresses | Requires multiple IPs |
| Most common | Less common |
| Flexible | Simpler isolation |

---

# Reverse Proxy Architecture

The reverse proxy sits in front of backend servers.

```
Client

↓

Reverse Proxy

↓

Backend Servers

↓

Response
```

Clients communicate only with the proxy.

---

# Reverse Proxy Responsibilities

- TLS termination
- Authentication
- Routing
- Compression
- Caching
- Logging
- Security filtering
- Load balancing

---

# Reverse Proxy Example

```
Internet

↓

Nginx

│

├── App Server 1

├── App Server 2

└── App Server 3
```

The reverse proxy selects an appropriate backend.

---

# Forward Proxy vs Reverse Proxy

| Forward Proxy | Reverse Proxy |
|---------------|---------------|
| Represents clients | Represents servers |
| Used by users | Used by websites |
| Hides clients | Hides backend servers |
| Common in enterprise networks | Common in web infrastructure |

---

# Load Balancing

Load balancing distributes traffic across multiple servers.

```
Users

↓

Load Balancer

│

├── Server 1

├── Server 2

├── Server 3

└── Server 4
```

---

# Benefits of Load Balancing

- High availability
- Better performance
- Scalability
- Fault tolerance
- Maintenance without downtime

---

# Common Load Balancing Algorithms

| Algorithm | Description |
|-----------|-------------|
| Round Robin | Requests distributed sequentially |
| Least Connections | Server with fewest active connections |
| Weighted Round Robin | Servers receive traffic based on assigned weights |
| IP Hash | Same client tends to reach the same backend |

---

# Round Robin Example

```
Client 1

↓

Server A

────────────

Client 2

↓

Server B

────────────

Client 3

↓

Server C

────────────

Client 4

↓

Server A
```

Traffic is evenly distributed.

---

# Least Connections

Useful when requests vary in duration.

```
Server A

5 Connections

────────────

Server B

2 Connections

↓

Next Request

↓

Server B
```

---

# Session Persistence (Sticky Sessions)

Some applications store session state locally.

```
User

↓

Load Balancer

↓

Server 2

↓

Future Requests

↓

Server 2
```

This ensures continuity but may reduce load distribution flexibility.

---

# Health Checks

Load balancers monitor backend health.

```
Health Check

↓

Server Responding?

↓

Yes

↓

Continue Routing

────────────

No

↓

Remove From Pool
```

Only healthy servers receive new traffic.

---

# Enterprise Architecture

```
Internet

↓

Firewall

↓

Web Application Firewall

↓

Load Balancer

↓

Reverse Proxy Cluster

↓

Application Servers

↓

Cache

↓

Database Cluster
```

Every layer improves scalability, availability, and security.

---

# High Availability

Redundancy prevents single points of failure.

```
Load Balancer

│

├── Web Server A

├── Web Server B

├── Web Server C

└── Web Server D
```

If one server fails, traffic is routed to others.

---

# Enterprise Example

An online banking platform receives 500,000 concurrent users.

Infrastructure:

```
Users

↓

Global Load Balancer

↓

Regional Reverse Proxy

↓

Web Server Cluster

↓

Authentication Service

↓

Application Cluster

↓

Database Cluster
```

This architecture enables secure and highly available services.

---

# Hands-on Lab (Conceptual)

Using Nginx or Apache:

1. Configure two virtual hosts.
2. Create separate home pages.
3. Access each domain using the appropriate `Host` header or local DNS mapping.
4. Observe which site is served.
5. Review access logs to identify requests for each virtual host.

---

# Interview Questions

1. What happens inside a web server after a request arrives?
2. Compare process-based, thread-based, and event-driven architectures.
3. Why is Nginx considered event-driven?
4. What is the role of a master process?
5. What are worker processes?
6. What is a Virtual Host?
7. Compare name-based and IP-based virtual hosting.
8. What is a reverse proxy?
9. What is load balancing?
10. Explain sticky sessions.

---

# Best Practices

- Use event-driven servers for high-concurrency workloads.
- Separate reverse proxies from backend applications.
- Configure health checks for backend servers.
- Use graceful reloads for configuration changes.
- Enable comprehensive logging and monitoring.
- Avoid single points of failure by deploying redundant servers.

---

# Common Mistakes

- Hosting production services on a single web server.
- Exposing backend application servers directly to the Internet.
- Ignoring health checks.
- Misconfiguring virtual hosts.
- Overloading one backend due to poor load balancing.
- Failing to test configuration changes before deployment.

---

# Key Takeaways

- Modern web servers use process-based, thread-based, or event-driven architectures to handle client requests.
- Event-driven servers efficiently support high concurrency with fewer resources.
- Virtual hosting allows multiple websites to share a server.
- Reverse proxies improve security, scalability, and manageability.
- Load balancing distributes traffic, improves availability, and supports enterprise-scale deployments.

```text id="jid720"
**Next:** Part 3
```