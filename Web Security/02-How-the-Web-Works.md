# 02-How-the-Web-Works.md

# Part 1 — What Happens When You Type a URL in Your Browser?

> **"Before you can secure a web application, you must understand exactly how it works. Every web attack targets one or more stages of the request-response lifecycle."**

---

# Learning Objectives

After completing this part, you will understand:

- How the web works from start to finish
- Client-Server architecture
- URLs and their components
- Browser request lifecycle
- DNS resolution
- TCP/IP communication
- HTTP request flow
- HTTPS overview
- Web page rendering
- Enterprise web infrastructure

---

# Introduction

Whenever you visit a website, hundreds of operations happen within milliseconds.

Example:

```
https://www.example.com
```

It may seem like a simple action, but internally the browser performs:

- URL parsing
- DNS lookup
- TCP connection
- TLS handshake (HTTPS)
- HTTP request
- Server processing
- Database queries
- Response generation
- Browser rendering

Understanding this lifecycle is essential because **every stage can introduce security risks**.

---

# The Complete Web Request Lifecycle

```
User

↓

Browser

↓

URL Parsing

↓

DNS Resolution

↓

TCP Connection

↓

TLS Handshake (HTTPS)

↓

HTTP Request

↓

Web Server

↓

Application

↓

Database

↓

Application Response

↓

HTTP Response

↓

Browser Rendering

↓

User Sees Website
```

---

# What is the Web?

The **World Wide Web (WWW)** is a system of interconnected resources that are accessed using browsers over the Internet.

The web consists of:

- Clients (Browsers)
- Servers
- Web Applications
- APIs
- Networks
- Protocols

---

# Client-Server Architecture

The web follows the **Client-Server Model**.

```
          Client

     (Web Browser)

           │

    HTTP / HTTPS

           │

           ▼

       Web Server

           │

           ▼

     Database / APIs
```

---

# What is a Client?

A **client** is any device or application that requests information.

Examples:

- Chrome
- Firefox
- Edge
- Safari
- Mobile Browser
- Mobile App
- Desktop Application

Responsibilities:

- Send requests
- Display responses
- Execute client-side JavaScript
- Store cookies
- Manage sessions

---

# What is a Server?

A **server** receives requests, processes them, and returns responses.

Responsibilities include:

- Authentication
- Authorization
- Business Logic
- Database Operations
- API Processing
- File Storage
- Logging

---

# Example

Customer opens:

```
https://shop.example.com
```

Browser sends:

```
GET /

Host: shop.example.com
```

Server returns:

```
HTML

CSS

JavaScript

Images
```

Browser renders the website.

---

# Understanding URLs

Example:

```
https://shop.example.com:443/products?id=15#reviews
```

---

# URL Structure

```
https://shop.example.com:443/products?id=15#reviews

│       │             │      │         │
│       │             │      │         └── Fragment
│       │             │      └──────────── Query String
│       │             └────────────────── Path
│       └──────────────────────────────── Host
└──────────────────────────────────────── Scheme
```

---

# URL Components

| Component | Example | Purpose |
|-----------|---------|---------|
| Scheme | https | Protocol |
| Host | shop.example.com | Server location |
| Port | 443 | Network service |
| Path | /products | Requested resource |
| Query | id=15 | Additional data |
| Fragment | reviews | Browser navigation |

---

# HTTP vs HTTPS

| HTTP | HTTPS |
|------|-------|
| Plain text | Encrypted |
| Port 80 | Port 443 |
| No confidentiality | TLS encryption |
| Vulnerable to interception | Protected in transit |

HTTPS is the standard for modern web applications.

---

# The Journey Begins

Imagine typing:

```
https://www.example.com
```

The browser first determines:

- Which protocol?
- Which server?
- Which port?
- Which resource?

---

# Step 1 — URL Parsing

The browser breaks the URL into components.

```
URL

↓

Scheme

↓

Host

↓

Port

↓

Path

↓

Parameters

↓

Fragment
```

---

# Step 2 — Check Browser Cache

The browser first checks whether it already has:

- DNS cache
- Images
- CSS
- JavaScript
- HTML
- Certificates

If available and still valid, it may avoid downloading them again.

---

# Step 3 — DNS Resolution

The browser must determine the server's IP address.

```
www.example.com

↓

DNS Resolver

↓

IP Address

↓

203.0.113.20
```

Without DNS, users would have to remember IP addresses instead of domain names.

---

# DNS Flow (Simplified)

```
Browser

↓

Operating System Cache

↓

Recursive DNS Resolver

↓

Authoritative DNS Server

↓

IP Address

↓

Browser
```

We will study DNS in detail in a dedicated chapter.

---

# Step 4 — TCP Connection

The browser establishes a reliable connection using TCP.

```
Browser

↓

SYN

↓

Server

↓

SYN-ACK

↓

Browser

↓

ACK
```

This process is called the **TCP Three-Way Handshake**.

---

# Why TCP?

TCP provides:

- Reliable delivery
- Ordered packets
- Error detection
- Retransmission
- Connection management

---

# Step 5 — HTTPS (Overview)

If HTTPS is used:

```
TCP

↓

TLS Handshake

↓

Encrypted Connection

↓

HTTP Communication
```

Encryption protects data while it travels across networks.

---

# Step 6 — Browser Sends HTTP Request

Example:

```
GET / HTTP/1.1

Host: www.example.com
```

The request may also include:

- Cookies
- Headers
- Language preferences
- Compression support
- Authentication tokens

---

# Step 7 — Request Reaches the Web Server

```
Browser

↓

Internet

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server
```

Enterprise environments often include multiple infrastructure components before the application itself.

---

# Step 8 — Application Processing

The application may:

- Authenticate the user
- Validate input
- Check permissions
- Execute business logic
- Query databases
- Call APIs
- Generate HTML or JSON

---

# Step 9 — Database Query

```
Application

↓

Database

↓

Customer Data

↓

Application
```

Most dynamic websites retrieve or update data before generating a response.

---

# Step 10 — HTTP Response

Example:

```
HTTP/1.1 200 OK

Content-Type: text/html
```

The response may contain:

- HTML
- JSON
- CSS
- Images
- JavaScript
- Files

---

# Step 11 — Browser Rendering

The browser:

- Parses HTML
- Downloads CSS
- Downloads JavaScript
- Requests images
- Builds the page
- Displays content to the user

---

# Complete Browser Workflow

```
User

↓

Browser

↓

URL

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

HTML

↓

CSS

↓

JavaScript

↓

Rendered Page
```

---

# Dynamic vs Static Websites

| Static | Dynamic |
|---------|----------|
| Fixed content | Generated on demand |
| No database required | Database-backed |
| Simple HTML | Server-side logic |
| Faster to host | More interactive |

---

# Enterprise Example

A customer logs into an online banking portal.

```
Customer

↓

Browser

↓

DNS

↓

HTTPS

↓

Load Balancer

↓

Web Server

↓

Authentication Service

↓

Database

↓

Account Dashboard
```

At each stage, security controls such as encryption, authentication, authorization, logging, and monitoring help protect sensitive financial data.

---

# Hands-on Lab (Conceptual)

Open your browser's **Developer Tools** (Network tab):

1. Visit a website.
2. Reload the page.
3. Observe the requests made.
4. Identify:
   - Initial HTML request
   - CSS files
   - JavaScript files
   - Images
   - API requests
   - HTTP status codes

Notice how a single webpage often requires dozens or even hundreds of network requests.

---

# Interview Questions

1. What happens when you type a URL into a browser?
2. What is Client-Server Architecture?
3. What is the difference between a client and a server?
4. What are the components of a URL?
5. Why is DNS required?
6. Why does TCP use a three-way handshake?
7. What is the purpose of HTTPS?
8. What is the role of a web server?
9. What is the difference between a static and dynamic website?
10. Why is understanding the request lifecycle important for Web Security?

---

# Best Practices

- Use HTTPS for all web traffic.
- Minimize unnecessary requests.
- Validate all user input on the server.
- Protect sensitive data during transmission.
- Understand every stage of the request lifecycle before studying vulnerabilities.

---

# Common Mistakes

- Assuming browsers communicate directly with databases.
- Believing HTTPS secures the application against all attacks.
- Ignoring intermediate components like load balancers and reverse proxies.
- Confusing DNS resolution with HTTP communication.

---

# Key Takeaways

- Every web request follows a structured lifecycle from the browser to the server and back.
- URLs contain multiple components that identify the requested resource.
- DNS translates domain names into IP addresses.
- TCP establishes reliable communication before HTTP data is exchanged.
- HTTPS adds encryption through TLS.
- Modern enterprise applications include multiple infrastructure layers before requests reach the application.

```
# 02-How-the-Web-Works.md

# Part 2 — DNS Resolution, TCP/IP, TLS Handshake, HTTP Request Journey, and Enterprise Network Flow

> **"Before a web application can process a request, the browser must locate the correct server, establish a reliable connection, negotiate encryption, and only then exchange application data."**

---

# Learning Objectives

After completing this part, you will understand:

- DNS resolution in detail
- IP addresses
- Ports
- TCP/IP fundamentals
- TCP Three-Way Handshake
- TLS Handshake
- HTTP request journey
- Enterprise network path
- Firewalls
- Load Balancers
- Reverse Proxies
- Security implications of each layer

---

# Recap

In Part 1 we learned:

```
Browser

↓

URL

↓

DNS

↓

TCP

↓

TLS

↓

HTTP

↓

Server

↓

Database

↓

Response
```

Now we'll explore each networking stage in much greater detail.

---

# What is DNS?

**DNS (Domain Name System)** translates human-readable domain names into IP addresses.

Example:

```
www.example.com

↓

93.184.216.34
```

Humans remember names.

Computers communicate using IP addresses.

---

# Why Do We Need DNS?

Imagine remembering every website like this:

```
https://142.250.190.78
```

instead of

```
https://www.google.com
```

DNS makes the Internet practical and user-friendly.

---

# DNS Analogy

Think of DNS as a phonebook.

```
Person Name

↓

Phonebook

↓

Phone Number

↓

Call
```

Similarly,

```
Domain Name

↓

DNS

↓

IP Address

↓

Connection
```

---

# Types of DNS Servers

```
Browser

↓

Local Cache

↓

Operating System Cache

↓

Recursive Resolver

↓

Root Server

↓

TLD Server

↓

Authoritative Server

↓

IP Address
```

---

# DNS Resolution Process

### Step 1

User enters:

```
https://shop.example.com
```

---

### Step 2

Browser checks:

- Browser DNS cache

---

### Step 3

Operating System checks:

- Local DNS cache

---

### Step 4

If not found:

Recursive Resolver performs DNS lookup.

---

### Step 5

Resolver contacts:

```
Root DNS Server
```

---

### Step 6

Root server replies:

```
Ask the .com server.
```

---

### Step 7

Resolver contacts:

```
.com TLD Server
```

---

### Step 8

TLD replies:

```
Ask example.com's authoritative server.
```

---

### Step 9

Resolver contacts:

```
Authoritative DNS Server
```

---

### Step 10

Authoritative server replies:

```
shop.example.com

↓

203.0.113.50
```

---

### Step 11

Browser receives:

```
203.0.113.50
```

Now the browser knows where to connect.

---

# Complete DNS Flow

```
Browser

↓

Browser Cache

↓

OS Cache

↓

Recursive Resolver

↓

Root DNS

↓

TLD DNS

↓

Authoritative DNS

↓

IP Address

↓

Browser
```

---

# Security Perspective

Attackers may target DNS through:

- DNS Cache Poisoning
- DNS Hijacking
- Malicious DNS Records
- DNS Amplification
- Domain Takeover

Defenders use:

- DNSSEC
- Monitoring
- Secure DNS configuration
- Access controls
- Logging

---

# What is an IP Address?

Every device connected to a network has an IP address.

Example:

```
203.0.113.50
```

or

```
2001:db8::1
```

---

# IPv4 vs IPv6

| IPv4 | IPv6 |
|------|-------|
| 32-bit | 128-bit |
| Limited address space | Vast address space |
| Example: 203.0.113.50 | Example: 2001:db8::1 |

---

# What is a Port?

A single server can host multiple services.

Ports identify the destination service.

Example:

```
Server

↓

Port 80 → HTTP

Port 443 → HTTPS

Port 22 → SSH

Port 53 → DNS
```

---

# Common Ports

| Port | Service |
|------|----------|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |

---

# What is TCP?

TCP stands for:

```
Transmission Control Protocol
```

It provides:

- Reliable communication
- Ordered delivery
- Error recovery
- Flow control

---

# Why Not Send Data Immediately?

The client and server must first agree to communicate.

TCP establishes this connection using the **Three-Way Handshake**.

---

# TCP Three-Way Handshake

```
Client                     Server

SYN ---------------------->

     <---------------- SYN-ACK

ACK ----------------------->
```

Connection established.

---

# Step 1 — SYN

Client says:

> "I want to communicate."

---

# Step 2 — SYN-ACK

Server replies:

> "I received your request."

---

# Step 3 — ACK

Client confirms:

> "Let's begin."

The TCP connection is now established.

---

# Why TCP Matters for Security

Reliable communication supports:

- Authentication
- Secure sessions
- Data integrity
- Application reliability

While TCP itself is not an encryption protocol, it provides the dependable transport layer used by higher-level protocols like TLS.

---

# HTTPS Connection

After TCP is established:

```
TCP

↓

TLS Handshake

↓

Encrypted Connection

↓

HTTP Requests
```

---

# What is TLS?

**TLS (Transport Layer Security)** encrypts communication between the client and server.

Benefits:

- Confidentiality
- Integrity
- Server authentication

---

# Simplified TLS Handshake

```
Client

↓

Client Hello

↓

Server Hello

↓

Certificate

↓

Key Exchange

↓

Session Keys

↓

Encrypted Communication
```

---

# Why Certificates Matter

Certificates help the browser verify that it is communicating with the intended server.

Example:

```
Browser

↓

Certificate Validation

↓

Trusted Certificate Authority

↓

Secure Connection
```

---

# Enterprise Network Flow

A typical enterprise request may follow this path:

```
Browser

↓

Internet

↓

Firewall

↓

CDN

↓

Web Application Firewall

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Application Server

↓

Database
```

---

# Why Use a Firewall?

A firewall filters network traffic.

It can:

- Allow trusted traffic
- Block unwanted connections
- Enforce network policies

---

# Why Use a CDN?

A **Content Delivery Network (CDN)** caches content closer to users.

Benefits:

- Faster delivery
- Reduced latency
- Lower server load
- Basic DDoS mitigation

---

# Why Use a Web Application Firewall (WAF)?

A WAF helps inspect HTTP requests before they reach the application.

It can detect or block common attack patterns such as malformed requests or suspicious payloads, providing an additional layer of defense alongside secure coding.

---

# Why Use a Load Balancer?

Instead of one server:

```
Users

↓

One Server
```

Enterprise applications often use:

```
Users

↓

Load Balancer

↓

Server 1

Server 2

Server 3
```

Benefits:

- High availability
- Scalability
- Fault tolerance

---

# Why Use a Reverse Proxy?

A reverse proxy sits between clients and backend servers.

Responsibilities:

- Forward requests
- Hide internal servers
- TLS termination (in some architectures)
- Caching
- Compression
- Routing

---

# Enterprise Architecture Example

```
Internet

↓

Firewall

↓

CDN

↓

WAF

↓

Load Balancer

↓

Reverse Proxy

↓

Application Cluster

↓

API Layer

↓

Database Cluster
```

---

# Where Can Attacks Occur?

```
Browser

↓

DNS

↓

Network

↓

TLS

↓

HTTP

↓

Web Server

↓

Application

↓

Database
```

Each stage has different security considerations, which will be explored in later chapters.

---

# Hands-on Lab (Conceptual)

Choose any website and answer:

1. Does it use HTTPS?
2. What IP address does its domain resolve to?
3. Which port is used?
4. Can you identify if it uses a CDN from the response headers?
5. Open the browser's Network tab and observe:
   - Initial request
   - Status code
   - Response headers
   - Additional resources loaded

---

# Interview Questions

1. What is DNS?
2. Why is DNS required?
3. What is an IP address?
4. What is a network port?
5. Explain the TCP Three-Way Handshake.
6. What is TLS?
7. Why is HTTPS more secure than HTTP?
8. What is the purpose of a Load Balancer?
9. What is a Reverse Proxy?
10. Why do enterprises deploy Web Application Firewalls?

---

# Best Practices

- Use HTTPS for all web traffic.
- Configure DNS securely and monitor changes.
- Keep TLS configurations updated.
- Place applications behind firewalls and reverse proxies.
- Use load balancers for resilience and scalability.
- Monitor network traffic for unusual activity.

---

# Common Mistakes

- Assuming DNS is inherently secure.
- Exposing backend servers directly to the Internet.
- Using outdated TLS versions or weak cipher suites.
- Running production services without a firewall.
- Believing a WAF can replace secure application development.

---

# Key Takeaways

- DNS translates domain names into IP addresses through a hierarchical resolution process.
- TCP establishes a reliable connection before application data is exchanged.
- TLS encrypts communication and authenticates servers.
- Enterprise web traffic typically passes through multiple infrastructure components before reaching the application.
- Each networking layer has unique security responsibilities and potential attack vectors.

```

# 02-How-the-Web-Works.md

# Part 3 — HTTP Request Processing, Web Servers, Application Servers, Databases, Browser Rendering, and Complete Request Lifecycle

> **"The network delivers your request to the server, but the application decides what happens next. Understanding this processing pipeline is essential for understanding modern web security."**

---

# Learning Objectives

After completing this part, you will understand:

- HTTP request processing
- Web server responsibilities
- Application server responsibilities
- Dynamic content generation
- Database interaction
- Browser rendering process
- Static vs Dynamic resources
- Browser caching
- Sessions and cookies (overview)
- Security checkpoints throughout the request lifecycle

---

# Recap

So far we have learned:

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
```

Now we will explore what happens **after the request reaches the server**.

---

# Complete Request Processing

```
Browser

↓

Firewall

↓

WAF

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Application

↓

Authentication

↓

Authorization

↓

Business Logic

↓

Database

↓

Response

↓

Browser Rendering
```

---

# What is an HTTP Request?

An HTTP request is a message sent from a client to a server requesting a resource.

Example:

```http
GET /products HTTP/1.1
Host: shop.example.com
```

A request tells the server:

- Which resource is needed
- Which method is being used
- Additional information through headers

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

Example:

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "username":"alice",
  "password":"********"
}
```

---

# Common HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Submit data |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Remove a resource |
| HEAD | Retrieve headers only |
| OPTIONS | Discover supported methods |

Each method has a different purpose and should be used appropriately.

---

# HTTP Headers

Headers provide additional information.

Examples include:

- Host
- User-Agent
- Accept
- Authorization
- Cookie
- Content-Type
- Content-Length
- Cache-Control

Example:

```http
User-Agent: Mozilla/5.0
```

---

# HTTP Body

The body usually contains data sent by the client.

Example:

```
Login Form

↓

Username

Password

↓

HTTP Body

↓

Server
```

Typical body formats:

- JSON
- XML
- HTML
- Form data
- Multipart form data

---

# Request Reaches the Web Server

```
Client

↓

HTTP Request

↓

Web Server
```

Popular web servers include:

- Apache HTTP Server
- Nginx
- Microsoft IIS
- Caddy

---

# Responsibilities of a Web Server

A web server typically:

- Accepts client connections
- Serves static files
- Handles HTTPS (depending on architecture)
- Routes requests
- Logs requests
- Passes dynamic requests to the application

---

# Static Resources

Static resources do not change for each user.

Examples:

- HTML files
- CSS files
- Images
- Fonts
- JavaScript files
- Videos

```
Browser

↓

Web Server

↓

Image.jpg
```

No database lookup is required.

---

# Dynamic Resources

Dynamic resources are generated at request time.

Examples:

- User profile
- Shopping cart
- Dashboard
- Account balance
- Search results

```
Browser

↓

Application

↓

Database

↓

Generated Response
```

---

# Web Server vs Application Server

| Web Server | Application Server |
|------------|--------------------|
| Serves static content | Executes business logic |
| Handles HTTP connections | Processes application code |
| Efficient with files | Generates dynamic responses |
| Routes requests | Interacts with databases |

---

# What is an Application Server?

The application server contains the application's logic.

Responsibilities include:

- Authentication
- Authorization
- Input validation
- Business rules
- API processing
- Database interaction
- Response generation

---

# Example Request Flow

Customer requests:

```
/account
```

Application workflow:

```
Receive Request

↓

Validate Session

↓

Authenticate User

↓

Authorize Access

↓

Retrieve Account Data

↓

Generate HTML

↓

Return Response
```

---

# Business Logic

Business logic defines how an application behaves.

Examples:

- Calculate discounts
- Validate orders
- Process payments
- Generate invoices
- Check inventory
- Enforce access rules

---

# Database Interaction

Many web applications store information in databases.

```
Application

↓

SQL Query

↓

Database

↓

Result

↓

Application
```

Typical data stored:

- Users
- Products
- Orders
- Sessions
- Logs
- Payments

---

# Database Types

## Relational Databases

Examples:

- PostgreSQL
- MySQL
- Microsoft SQL Server
- Oracle Database

---

## NoSQL Databases

Examples:

- MongoDB
- Redis
- Cassandra

Different applications choose different databases based on their requirements.

---

# Example Login Workflow

```
User

↓

Login Form

↓

Application

↓

Database Lookup

↓

Password Verification

↓

Session Creation

↓

Dashboard
```

---

# Response Generation

After processing the request, the application creates a response.

Possible formats:

- HTML
- JSON
- XML
- PDF
- Images
- Files

---

# HTTP Response

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

The response consists of:

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

# Common HTTP Status Codes

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 302 | Temporary Redirect |
| 304 | Not Modified |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

---

# Browser Receives Response

The browser processes:

```
HTML

↓

CSS

↓

JavaScript

↓

Fonts

↓

Images

↓

Videos

↓

Rendered Page
```

---

# Browser Rendering Process

```
Download HTML

↓

Parse HTML

↓

Build DOM

↓

Download CSS

↓

Build CSSOM

↓

Execute JavaScript

↓

Combine DOM + CSSOM

↓

Render Tree

↓

Layout

↓

Paint

↓

Display Page
```

---

# What is the DOM?

The **Document Object Model (DOM)** is the browser's internal representation of an HTML document.

Example:

```
HTML

↓

DOM Tree

↓

JavaScript Interaction
```

JavaScript can modify the DOM dynamically, allowing pages to update without a full reload.

---

# Additional Browser Requests

A single HTML page often references many additional resources.

Example:

```
index.html

├── style.css

├── app.js

├── logo.png

├── profile.jpg

├── font.woff2

└── api/user
```

The browser sends separate HTTP requests for many of these resources.

---

# Browser Cache

Browsers cache resources to improve performance.

```
First Visit

↓

Download Resource

↓

Cache Resource

↓

Future Visit

↓

Reuse Cached Copy (if valid)
```

Benefits:

- Faster page loads
- Reduced bandwidth
- Lower server load

---

# Cookies (Overview)

Cookies are small pieces of data stored by the browser.

Typical uses:

- Session identifiers
- User preferences
- Language settings
- Shopping carts

A dedicated chapter will explore cookies in depth.

---

# Sessions (Overview)

A session allows the server to recognize multiple requests as belonging to the same user.

Example:

```
Login

↓

Session Created

↓

User Browsing

↓

Server Recognizes User
```

---

# Security Checkpoints

A secure application performs checks throughout the request lifecycle.

```
Request

↓

Authentication

↓

Authorization

↓

Input Validation

↓

Business Rules

↓

Database Access

↓

Output Generation

↓

Logging

↓

Response
```

Security should not rely on a single checkpoint.

---

# Enterprise Example

A customer views an order history page.

```
Customer

↓

HTTPS Request

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Application

↓

Validate Session

↓

Authorize User

↓

Database Query

↓

Generate HTML

↓

Browser Render
```

Each step contributes to the overall security and reliability of the application.

---

# Hands-on Lab (Conceptual)

Using your browser's Developer Tools:

1. Open the **Network** tab.
2. Visit a dynamic website.
3. Observe:
   - Initial HTML request
   - CSS files
   - JavaScript files
   - Images
   - API calls
   - Response status codes
4. Compare the size and timing of different resources.

Think about which requests contain sensitive information and which should require authentication.

---

# Interview Questions

1. What is the difference between a web server and an application server?
2. What is an HTTP request?
3. What is an HTTP response?
4. Explain common HTTP methods.
5. What are HTTP headers?
6. What is business logic?
7. What is the DOM?
8. What is browser caching?
9. Why are sessions needed?
10. What are common HTTP status codes?

---

# Best Practices

- Separate static and dynamic content efficiently.
- Validate all incoming data before processing.
- Return appropriate HTTP status codes.
- Cache static resources responsibly.
- Minimize unnecessary HTTP requests.
- Log important application events without exposing sensitive information.

---

# Common Mistakes

- Returning overly detailed error messages.
- Trusting client-side validation alone.
- Misusing HTTP methods.
- Exposing internal application details in responses.
- Ignoring caching behavior for sensitive content.

---

# Key Takeaways

- Web servers receive requests and serve static resources, while application servers execute business logic.
- Dynamic pages often require database access before generating a response.
- HTTP requests and responses consist of structured components such as headers and bodies.
- Browsers parse HTML, build the DOM, load additional resources, and render pages.
- Security checks should occur throughout the request lifecycle rather than at a single point.

```

# 02-How-the-Web-Works.md

# Part 4 — Complete End-to-End Request Lifecycle, Modern Web Architectures, Security Perspective, and Chapter Summary

> **"Understanding how the web works is the foundation of Web Security. Every vulnerability, defense, and security control exists somewhere in the request lifecycle."**

---

# Learning Objectives

After completing this final part, you will understand:

- Complete end-to-end request lifecycle
- Modern web architectures
- Monolithic vs Microservices
- APIs in modern applications
- Browser security checkpoints
- Enterprise request flow
- Security controls at every layer
- Common misconceptions
- Final revision
- Chapter summary

---

# Complete End-to-End Request Lifecycle

The following diagram summarizes everything you've learned in this chapter.

```
                    USER

                      │

              Types URL / Clicks Link

                      │

                   Browser

                      │

                 URL Parsing

                      │

               Browser Cache

                      │

                 DNS Lookup

                      │

                TCP Handshake

                      │

                 TLS Handshake

                      │

               HTTP Request

                      │

                  Firewall

                      │

                     CDN

                      │

          Web Application Firewall

                      │

               Load Balancer

                      │

              Reverse Proxy

                      │

                Web Server

                      │

           Application Server

                      │

        Authentication & Authorization

                      │

             Business Logic

                      │

                 Database

                      │

               HTTP Response

                      │

          HTML + CSS + JavaScript

                      │

            Browser Rendering

                      │

                User Sees Page
```

Every stage has specific performance and security responsibilities.

---

# Where Security Controls Exist

```
Browser

↓

HTTPS

↓

Firewall

↓

WAF

↓

Authentication

↓

Authorization

↓

Input Validation

↓

Business Logic

↓

Database Security

↓

Logging

↓

Monitoring
```

Security is distributed across multiple layers.

---

# Traditional Monolithic Architecture

Earlier web applications were often built as a single application.

```
Browser

↓

Web Server

↓

Application

↓

Database
```

Advantages:

- Simpler deployment
- Easier initial development

Disadvantages:

- Harder to scale individual components
- Single application grows large over time
- Tighter coupling between modules

---

# Microservices Architecture

Modern enterprise applications often use microservices.

```
               Browser

                  │

            API Gateway

      ┌───────────┼───────────┐

      │           │           │

 User Service  Order Service  Payment Service

      │           │           │

      └───────────┼───────────┘

            Shared Infrastructure

                  │

              Databases
```

Benefits:

- Independent deployment
- Better scalability
- Technology flexibility
- Fault isolation

Challenges:

- More complex communication
- Service authentication
- Monitoring
- Distributed tracing

---

# What is an API?

An **Application Programming Interface (API)** allows software systems to communicate.

Example:

```
Browser

↓

API Request

↓

Application

↓

JSON Response
```

Modern websites often rely heavily on APIs for dynamic content.

---

# Browser and API Interaction

Instead of loading an entirely new page, many applications request data asynchronously.

```
Browser

↓

API Call

↓

JSON

↓

JavaScript Updates Page
```

This improves responsiveness and user experience.

---

# Browser Storage (Overview)

Browsers can store data in several ways.

| Storage Type | Typical Purpose |
|--------------|-----------------|
| Cookies | Session identifiers, preferences |
| Local Storage | Persistent client-side data |
| Session Storage | Temporary tab-specific data |
| Cache | Performance optimization |

These mechanisms will be explored in dedicated chapters.

---

# Authentication Flow (Overview)

```
User

↓

Login Request

↓

Application

↓

Verify Credentials

↓

Create Session / Token

↓

Access Protected Resources
```

---

# Authorization Flow (Overview)

```
Authenticated User

↓

Permission Check

↓

Access Decision

↓

Resource
```

Authentication identifies the user; authorization determines what they can access.

---

# Browser Security Responsibilities

Modern browsers provide many built-in protections, including:

- Certificate validation
- Same-Origin Policy
- Sandboxing
- Content isolation
- Secure cookie handling
- Safe browsing features

These protections reduce risk but do not eliminate application vulnerabilities.

---

# Enterprise Infrastructure Example

An online banking application may include:

```
Internet

↓

DNS

↓

CDN

↓

Firewall

↓

WAF

↓

Load Balancer

↓

Reverse Proxy

↓

Authentication Service

↓

API Gateway

↓

Microservices

↓

Database Cluster

↓

Logging

↓

Monitoring

↓

Backup Systems
```

Each component contributes to resilience, scalability, and security.

---

# Performance vs Security

Enterprise systems must balance performance with protection.

| Performance Technique | Security Consideration |
|-----------------------|------------------------|
| Caching | Avoid caching sensitive data |
| Compression | Review security implications |
| CDN | Protect origin servers |
| Load Balancing | High availability |
| Reverse Proxy | Hide backend infrastructure |
| API Gateway | Centralized authentication and routing |

---

# Common Misconceptions

| Myth | Reality |
|------|----------|
| The browser talks directly to the database | Requests are processed by application logic before reaching the database. |
| HTTPS prevents all attacks | HTTPS protects data in transit but does not fix application flaws. |
| A WAF makes secure coding unnecessary | A WAF complements, not replaces, secure development. |
| Only login pages require security | Every endpoint, API, and resource requires appropriate protection. |

---

# Security Perspective

As a security professional, analyze every request by asking:

- Where does the request originate?
- Is the connection encrypted?
- Who is making the request?
- Is the user authenticated?
- Is the action authorized?
- Is the input validated?
- Is sensitive data protected?
- Is the activity logged?
- How would abnormal behavior be detected?

---

# End-to-End Security Checklist

```
✓ DNS Resolution

↓

✓ Secure TLS

↓

✓ Authentication

↓

✓ Authorization

↓

✓ Input Validation

↓

✓ Business Logic

↓

✓ Secure Database Access

↓

✓ Secure Response

↓

✓ Logging

↓

✓ Monitoring
```

---

# Real Enterprise Scenario

A customer purchases an item from an e-commerce platform.

```
Customer

↓

HTTPS Request

↓

CDN

↓

WAF

↓

Load Balancer

↓

Application

↓

Validate Session

↓

Authorize Purchase

↓

Inventory Check

↓

Payment Processing

↓

Order Database

↓

Confirmation Response

↓

Browser Displays Receipt
```

Security controls are applied throughout the transaction to protect customer information and business operations.

---

# Hands-on Lab (Conceptual)

Open the Network tab in your browser and inspect a modern web application.

Identify:

- Initial HTML request
- CSS files
- JavaScript bundles
- Image requests
- API calls
- HTTP methods
- Response codes
- Response headers
- Content types

Then draw a simple diagram showing the likely path from the browser to the backend services.

---

# Interview Questions

1. Explain the complete lifecycle of a web request.
2. What is the role of DNS?
3. Why is the TCP handshake necessary?
4. What does TLS provide?
5. What is the difference between a web server and an application server?
6. What is an API?
7. What is the difference between a monolithic application and microservices?
8. Why is authorization different from authentication?
9. Why shouldn't browsers communicate directly with databases?
10. Where should security controls be applied during request processing?

---

# Best Practices

- Understand the complete request lifecycle before studying web attacks.
- Encrypt all traffic using HTTPS.
- Authenticate users before granting access.
- Authorize every sensitive action.
- Validate input on the server.
- Log important security events.
- Monitor application behavior continuously.
- Keep infrastructure components updated and securely configured.

---

# Common Mistakes

- Assuming all requests are trustworthy.
- Treating APIs differently from other application endpoints.
- Ignoring browser-side security mechanisms.
- Exposing backend services directly to the Internet.
- Focusing only on network security while neglecting application security.

---

# Quick Revision

Remember the request lifecycle:

```
URL

↓

DNS

↓

TCP

↓

TLS

↓

HTTP Request

↓

Infrastructure

↓

Application

↓

Database

↓

HTTP Response

↓

Browser Rendering
```

---

# Chapter Summary

In this chapter, you learned:

- How a browser processes a URL
- DNS resolution
- TCP and TLS handshakes
- HTTP request and response structure
- Web server and application server responsibilities
- Database interaction
- Browser rendering process
- Static vs dynamic content
- Modern enterprise web architectures
- APIs and microservices
- Security controls throughout the request lifecycle

This understanding forms the foundation for every topic that follows. In the next chapter, we will study the **HTTP Protocol** in depth, including request methods, headers, status codes, caching, content negotiation, persistent connections, and the security implications of HTTP.

```
