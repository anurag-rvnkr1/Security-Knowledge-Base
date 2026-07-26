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

```text id="jid720"
**Next:** Part 2
```