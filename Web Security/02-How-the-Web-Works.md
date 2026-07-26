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

```text id="jid720"
**Next:** Part 3
```