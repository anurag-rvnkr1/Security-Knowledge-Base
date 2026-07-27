# 08-Reverse-Proxies-and-Load-Balancers.md

# Part 1 — Introduction to Reverse Proxies, Forward Proxies, Load Balancers, Architecture, Request Flow, and Enterprise Fundamentals

> **"Reverse proxies and load balancers sit between users and applications. They improve security, scalability, availability, and performance while hiding backend infrastructure from the Internet."**

---

# Learning Objectives

After completing this part, you will understand:

- What is a Proxy?
- Forward Proxy
- Reverse Proxy
- Load Balancer
- Reverse Proxy Architecture
- Enterprise Request Flow
- Benefits of Reverse Proxies
- Benefits of Load Balancers
- Types of Load Balancers
- Enterprise Deployment Models
- Security Overview

---

# Introduction

A user visiting a website rarely communicates directly with the application server.

Instead, the request usually follows this path:

```
User

↓

Internet

↓

Reverse Proxy

↓

Load Balancer

↓

Application Server

↓

Database

↓

Response
```

In modern enterprise environments:

- Applications are hidden from the Internet.
- Reverse proxies protect backend servers.
- Load balancers distribute requests.
- Multiple backend servers improve availability.

---

# What is a Proxy?

A **Proxy** is an intermediary that receives requests and forwards them to another system.

```
Client

↓

Proxy

↓

Destination
```

A proxy acts on behalf of one side of the communication.

There are two major categories:

- Forward Proxy
- Reverse Proxy

---

# Proxy Types

```
                    Proxy

                 /          \

        Forward Proxy    Reverse Proxy
```

Although both forward requests, they serve different purposes.

---

# What is a Forward Proxy?

A **Forward Proxy** represents the client.

```
User

↓

Forward Proxy

↓

Internet

↓

Website
```

The destination website primarily sees the proxy rather than the original client.

---

# Forward Proxy Responsibilities

- Hide client identity
- Filter outbound traffic
- Enforce browsing policies
- Cache content
- Monitor Internet usage
- Apply organizational restrictions

---

# Enterprise Forward Proxy Example

```
Employees

↓

Corporate Forward Proxy

↓

Internet

↓

External Websites
```

Typical use cases:

- Schools
- Universities
- Enterprises
- Government networks

---

# Forward Proxy Benefits

- Internet filtering
- Malware blocking
- User monitoring
- Bandwidth optimization
- Centralized policy enforcement
- Outbound access control

---

# What is a Reverse Proxy?

A **Reverse Proxy** represents the server.

```
Client

↓

Reverse Proxy

↓

Backend Server
```

Clients never communicate directly with backend servers.

---

# Reverse Proxy Responsibilities

A reverse proxy commonly performs:

- TLS termination
- Request routing
- Load balancing
- Authentication
- Compression
- Caching
- Logging
- Security filtering
- Rate limiting

---

# Reverse Proxy Architecture

```
Internet

↓

Reverse Proxy

│

├── Web Server A

├── Web Server B

└── Web Server C
```

The reverse proxy decides which backend server should process each request.

---

# Client Perspective

From the client's viewpoint:

```
Browser

↓

example.com

↓

Response
```

The client usually does not know:

- Backend server count
- Internal IP addresses
- Internal network topology

---

# Backend Perspective

Backend servers trust the reverse proxy as the entry point.

```
Reverse Proxy

↓

Application Servers

↓

Database
```

This simplifies security and traffic management.

---

# Reverse Proxy Request Flow

```
Browser

↓

HTTPS Request

↓

Reverse Proxy

↓

Authentication

↓

Routing

↓

Application

↓

Response

↓

Browser
```

Every request passes through the proxy first.

---

# Reverse Proxy vs Forward Proxy

| Forward Proxy | Reverse Proxy |
|---------------|---------------|
| Represents clients | Represents servers |
| Protects users | Protects servers |
| Used inside organizations | Used by websites |
| Controls outbound traffic | Controls inbound traffic |
| Client config required | Usually transparent to clients |

---

# Why Organizations Use Reverse Proxies

Reasons include:

- Improved security
- Scalability
- High availability
- TLS offloading
- Centralized logging
- Easier maintenance
- Backend isolation

---

# What is a Load Balancer?

A **Load Balancer** distributes client requests across multiple backend servers.

```
Clients

↓

Load Balancer

↓

Server Pool
```

Instead of sending all traffic to one server, requests are shared.

---

# Why Load Balancing?

Without a load balancer:

```
1000 Users

↓

One Server

↓

Overloaded
```

With a load balancer:

```
1000 Users

↓

Load Balancer

↓

Server A

Server B

Server C
```

Traffic is distributed, reducing overload.

---

# Basic Load Balancer Architecture

```
                 Users

                   │

                   ▼

             Load Balancer

         ┌────────┼────────┐

         ▼        ▼        ▼

     Server A  Server B  Server C
```

---

# Reverse Proxy and Load Balancer Together

In many environments, one product performs both roles.

```
Internet

↓

Reverse Proxy

↓

Load Balancer

↓

Application Cluster
```

Products such as Nginx, HAProxy, and cloud-managed services often provide both capabilities.

---

# Reverse Proxy Advantages

| Feature | Benefit |
|----------|----------|
| TLS Termination | Offloads encryption work |
| Routing | Directs traffic intelligently |
| Caching | Improves performance |
| Compression | Reduces bandwidth usage |
| Authentication | Centralizes access control |
| Logging | Simplifies monitoring |
| Security Filtering | Blocks malicious requests |

---

# Load Balancer Advantages

| Feature | Benefit |
|----------|----------|
| Scalability | Add backend servers easily |
| High Availability | Removes single points of failure |
| Fault Tolerance | Routes around failed servers |
| Performance | Shares workload efficiently |
| Maintenance | Enables rolling updates |
| Reliability | Improves uptime |

---

# Enterprise Deployment

```
Internet

↓

Firewall

↓

Reverse Proxy

↓

Load Balancer

↓

Application Cluster

↓

Database Cluster
```

Each layer has a specific responsibility.

---

# Reverse Proxy Security

The reverse proxy is often the first application-layer defense.

Responsibilities include:

- Blocking malicious requests
- Enforcing HTTPS
- Applying rate limits
- Validating headers
- Hiding backend information
- Logging requests

---

# Backend Isolation

Instead of exposing:

```
App Server

↓

Internet
```

Use:

```
Internet

↓

Reverse Proxy

↓

App Server
```

Backend servers remain on private networks.

---

# Reverse Proxy and TLS

Instead of every backend server managing certificates:

```
Browser

↓

HTTPS

↓

Reverse Proxy

↓

HTTP or HTTPS

↓

Backend
```

The reverse proxy commonly handles TLS termination, though some environments also encrypt traffic between the proxy and backend servers.

---

# Enterprise Example

A banking application serves millions of users.

```
Customers

↓

Internet

↓

Reverse Proxy Cluster

↓

Load Balancer

↓

Application Servers

↓

Authentication Service

↓

Database
```

Benefits:

- Secure public access
- Backend protection
- High availability
- Easier scaling
- Centralized monitoring

---

# Real-World Products

Common reverse proxy and load balancing solutions include:

| Product | Primary Use |
|----------|-------------|
| Nginx | Reverse proxy, load balancer, web server |
| HAProxy | High-performance load balancing |
| Apache HTTP Server | Reverse proxy and web server |
| Traefik | Dynamic routing for containers |
| Envoy Proxy | Cloud-native service proxy |
| Caddy | Reverse proxy with automatic HTTPS |

Cloud providers also offer managed load balancing services.

---

# Hands-on Lab (Conceptual)

Using Nginx or HAProxy in a lab:

1. Configure two backend web servers.
2. Place a reverse proxy in front of them.
3. Access the proxy instead of the backend servers.
4. Stop one backend server.
5. Observe whether requests continue reaching the remaining healthy server.

---

# Interview Questions

1. What is a proxy?
2. What is the difference between a forward proxy and a reverse proxy?
3. Why are reverse proxies commonly used in enterprises?
4. What is a load balancer?
5. Why shouldn't backend servers be directly exposed to the Internet?
6. What functions can a reverse proxy perform?
7. How does load balancing improve availability?
8. Can a reverse proxy also perform load balancing?
9. Why is TLS often terminated at the reverse proxy?
10. Give examples of popular reverse proxy solutions.

---

# Best Practices

- Keep backend servers on private networks.
- Terminate TLS using modern configurations.
- Enable centralized logging.
- Configure health checks for backend servers.
- Apply rate limiting and request filtering.
- Remove unnecessary response headers.
- Regularly update proxy software.

---

# Common Mistakes

- Exposing backend application servers directly.
- Trusting client-supplied headers without validation.
- Running without health checks.
- Using weak TLS configurations.
- Not logging proxy requests.
- Creating single points of failure with only one reverse proxy.

---

# Key Takeaways

- A proxy is an intermediary between communicating systems.
- Forward proxies represent clients, while reverse proxies represent servers.
- Reverse proxies improve security, scalability, and operational flexibility.
- Load balancers distribute traffic across multiple backend servers to improve performance and availability.
- Modern enterprise architectures almost always place reverse proxies and load balancers in front of application servers.

```
# 08-Reverse-Proxies-and-Load-Balancers.md

# Part 2 — Load Balancing Algorithms, Health Checks, TLS Termination, Session Persistence, Reverse Proxy Routing, and Enterprise Traffic Management

> **"The true power of reverse proxies and load balancers lies in intelligent traffic management. Instead of simply forwarding requests, they continuously evaluate backend health, optimize routing decisions, terminate encrypted connections, and ensure applications remain available even during failures."**

---

# Learning Objectives

After completing this part, you will understand:

- Request routing
- Layer 4 vs Layer 7 Load Balancing
- Load balancing algorithms
- Health checks
- Active vs Passive health monitoring
- Session Persistence (Sticky Sessions)
- TLS Termination
- TLS Passthrough
- Connection Pooling
- Keep-Alive Connections
- Enterprise traffic management
- High Availability (HA)

---

# Recap

In Part 1, we learned:

```
Internet

↓

Reverse Proxy

↓

Load Balancer

↓

Application Servers
```

Now we'll explore **how requests are intelligently routed**.

---

# Request Routing

Every incoming request must reach an appropriate backend.

```
Client

↓

Reverse Proxy

↓

Routing Decision

↓

Backend Server
```

The routing decision depends on configured rules.

---

# Routing Criteria

Reverse proxies may route based on:

- Hostname
- URL Path
- HTTP Method
- Headers
- Cookies
- Query Parameters
- Client IP
- Geographic Region

---

# Host-Based Routing

Different domains can reach different applications.

```
portal.company.com

↓

Application A

────────────

api.company.com

↓

Application B

────────────

shop.company.com

↓

Application C
```

---

# Host-Based Routing Diagram

```
Internet

↓

Reverse Proxy

│

├── portal.company.com

│      ↓

│   Portal Cluster

│

├── api.company.com

│      ↓

│    API Cluster

│

└── shop.company.com

       ↓

   E-Commerce Cluster
```

---

# Path-Based Routing

Routing can depend on the URL path.

Example:

```
example.com/api

↓

API Servers

────────────

example.com/images

↓

Image Server

────────────

example.com/admin

↓

Admin Application
```

---

# Path Routing Flow

```
Incoming Request

↓

URL Analysis

↓

Route Selection

↓

Correct Backend
```

---

# Layer 4 Load Balancing

Layer 4 operates using:

- TCP
- UDP
- IP Address
- Port

```
Client

↓

TCP Connection

↓

Load Balancer

↓

Server
```

It does **not** inspect HTTP content.

---

# Layer 7 Load Balancing

Layer 7 understands application protocols.

It can inspect:

- HTTP Headers
- Cookies
- URL Paths
- HTTP Methods
- Host Header
- Query Strings

```
HTTP Request

↓

Analyze Content

↓

Select Backend
```

---

# Layer 4 vs Layer 7

| Layer 4 | Layer 7 |
|----------|----------|
| Operates on TCP/UDP | Operates on HTTP/HTTPS |
| Faster | More intelligent routing |
| Cannot inspect URLs | Can inspect requests |
| Lower overhead | More features |
| Suitable for generic traffic | Ideal for web applications |

---

# Load Balancing Algorithms

The load balancer decides where each request should go.

Common algorithms include:

- Round Robin
- Weighted Round Robin
- Least Connections
- Least Response Time
- IP Hash
- Random
- Consistent Hashing

---

# Round Robin

Requests are distributed sequentially.

```
Request 1

↓

Server A

────────────

Request 2

↓

Server B

────────────

Request 3

↓

Server C

────────────

Request 4

↓

Server A
```

Simple and widely used.

---

# Weighted Round Robin

Servers receive different traffic volumes.

Example:

```
Server A

Weight = 5

────────────

Server B

Weight = 2

────────────

Server C

Weight = 1
```

Powerful servers receive more requests.

---

# Weighted Example

```
Requests

↓

A

↓

A

↓

B

↓

A

↓

C

↓

A

↓

B

↓

A
```

Distribution follows assigned weights.

---

# Least Connections

The next request goes to the server handling the fewest active connections.

```
Server A

15 Connections

────────────

Server B

4 Connections

↓

Next Request

↓

Server B
```

Useful when request duration varies.

---

# Least Response Time

The load balancer measures server responsiveness.

```
Server A

18 ms

────────────

Server B

42 ms

↓

Next Request

↓

Server A
```

This helps optimize user experience.

---

# IP Hash

The client's IP determines the backend.

```
Client IP

↓

Hash Function

↓

Server Selection
```

The same client generally reaches the same backend.

---

# Consistent Hashing

Useful for:

- Distributed caches
- Stateful services
- Microservices

Advantages:

- Minimal redistribution when servers are added or removed
- Better cache efficiency

---

# Health Checks

Load balancers continuously verify backend availability.

```
Health Check

↓

Backend Alive?

↓

Yes

↓

Continue Routing

────────────

No

↓

Remove From Pool
```

---

# Active Health Checks

The load balancer periodically sends requests.

Example:

```
GET /health

↓

HTTP 200

↓

Healthy
```

---

# Passive Health Checks

Instead of sending probes:

```
Real Traffic

↓

Errors Detected

↓

Server Marked Unhealthy
```

Passive monitoring relies on production traffic.

---

# Health Check Types

| Type | Purpose |
|------|----------|
| TCP | Connection availability |
| HTTP | Web application status |
| HTTPS | TLS-enabled application |
| Custom URL | Application-specific checks |
| API Endpoint | Microservice health |

---

# Health Check Example

```
Every 10 Seconds

↓

GET /health

↓

200 OK

↓

Healthy

────────────

500 Error

↓

Unhealthy
```

---

# Removing Failed Servers

```
Server Failure

↓

Health Check Fails

↓

Remove Server

↓

Route Traffic Elsewhere
```

Users continue accessing healthy servers.

---

# Automatic Recovery

```
Failed Server

↓

Recovered

↓

Health Check Passes

↓

Rejoin Pool
```

Recovery is automatic after successful checks.

---

# Session Persistence (Sticky Sessions)

Some applications store user session data locally.

```
Login

↓

Server B

↓

Future Requests

↓

Server B
```

The user consistently reaches the same backend.

---

# Why Sticky Sessions?

Without persistence:

```
Login

↓

Server A

↓

Next Request

↓

Server C

↓

Session Missing
```

Unless session data is shared, the user may need to authenticate again.

---

# Sticky Session Methods

Common methods:

- Cookie-based
- Source IP
- Session ID
- Custom header

---

# TLS Termination

TLS encryption is commonly handled by the reverse proxy.

```
Browser

↓

HTTPS

↓

Reverse Proxy

↓

Decrypt

↓

HTTP or HTTPS

↓

Backend
```

Benefits:

- Simplified certificate management
- Reduced backend CPU usage
- Centralized TLS configuration

---

# TLS Passthrough

Sometimes encrypted traffic is forwarded without decryption.

```
Browser

↓

HTTPS

↓

Load Balancer

↓

HTTPS

↓

Backend
```

The backend performs TLS termination.

---

# TLS Termination vs TLS Passthrough

| TLS Termination | TLS Passthrough |
|-----------------|-----------------|
| Decrypts at proxy | Encryption reaches backend |
| Easier inspection | End-to-end encryption |
| Simpler certificate management | Backend manages certificates |
| Supports Layer 7 routing | Mostly Layer 4 routing |

---

# Connection Pooling

Reverse proxies reuse backend connections.

Without pooling:

```
1000 Requests

↓

1000 Connections
```

With pooling:

```
1000 Requests

↓

20 Persistent Connections
```

This reduces connection overhead.

---

# Keep-Alive Connections

Persistent connections reduce repeated TCP handshakes.

```
Client

↓

Connection Open

↓

Request 1

↓

Request 2

↓

Request 3

↓

Close
```

Benefits:

- Lower latency
- Reduced CPU usage
- Faster page loading

---

# Request Queue

If all backend servers are busy:

```
Incoming Requests

↓

Queue

↓

Server Available

↓

Process Request
```

Queue limits help protect the infrastructure.

---

# Failover

If one server fails:

```
Server A

↓

Offline

↓

Traffic

↓

Server B
```

Users experience little or no disruption.

---

# High Availability Cluster

```
Internet

↓

Load Balancer A

↓

Load Balancer B

↓

Application Cluster
```

Even the load balancers are deployed redundantly.

---

# Enterprise Architecture

```
Internet

↓

Firewall

↓

Reverse Proxy Cluster

↓

Layer 7 Load Balancer

↓

Application Cluster

↓

Redis Cache

↓

Database Cluster
```

Each component contributes to scalability and resilience.

---

# Real Enterprise Example

A streaming platform experiences heavy evening traffic.

```
Users

↓

Reverse Proxy

↓

Load Balancer

↓

Server Pool

↓

Media Service

↓

Storage
```

When traffic doubles:

```
New Servers Added

↓

Load Balancer Updates Pool

↓

Traffic Redistributed

↓

Service Remains Available
```

Horizontal scaling allows capacity to grow without interrupting users.

---

# Hands-on Lab (Conceptual)

Using **Nginx** or **HAProxy**:

1. Configure three backend servers.
2. Enable Round Robin load balancing.
3. Refresh the application repeatedly.
4. Observe requests reaching different servers.
5. Stop one backend server.
6. Verify that health checks remove it from the rotation.

---

# Interview Questions

1. What is the difference between Layer 4 and Layer 7 load balancing?
2. Explain Round Robin load balancing.
3. What is Weighted Round Robin?
4. When is Least Connections preferred?
5. What is a health check?
6. Compare active and passive health checks.
7. What are Sticky Sessions?
8. What is TLS Termination?
9. What is TLS Passthrough?
10. Why are Keep-Alive connections beneficial?

---

# Best Practices

- Prefer Layer 7 load balancing for modern web applications when application-aware routing is required.
- Configure active health checks for all critical services.
- Use TLS termination with strong cipher suites unless end-to-end encryption requirements dictate otherwise.
- Enable connection pooling and Keep-Alive where appropriate.
- Deploy redundant load balancers to avoid single points of failure.
- Continuously monitor backend health and response times.

---

# Common Mistakes

- Routing traffic to unhealthy backend servers.
- Using sticky sessions without planning for server failures.
- Disabling health checks.
- Creating a single load balancer with no redundancy.
- Using outdated TLS configurations.
- Ignoring backend response time metrics.

---

# Key Takeaways

- Reverse proxies use intelligent routing rules to direct traffic based on hosts, paths, headers, and other request attributes.
- Layer 4 load balancers operate on network information, while Layer 7 load balancers understand HTTP/HTTPS.
- Health checks ensure traffic is sent only to healthy backend servers.
- Sticky sessions maintain session continuity for stateful applications.
- TLS termination, connection pooling, and Keep-Alive significantly improve performance and simplify enterprise operations.

```text id="jid720"
**Next:** Part 3
```