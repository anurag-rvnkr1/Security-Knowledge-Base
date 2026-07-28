# 45-Host-Header-Attacks.md

# Part 1 — Introduction to HTTP Host Header Attacks, Host Headers, Virtual Hosting, and Secure Request Routing

> **"HTTP Host Header attacks arise when applications make security-sensitive decisions based on an untrusted Host header without appropriate validation. Secure applications validate host information, use trusted configuration, and avoid relying on client-controlled headers for critical functionality."**

---

# Learning Objectives

After completing this part, you will understand:

- What the HTTP Host Header Is
- Why the Host Header Exists
- Virtual Hosting
- HTTP Request Routing
- Reverse Proxies and Load Balancers
- Trust Boundaries
- Host Header Attacks (High-Level)
- Enterprise Architecture
- Secure Design Principles

---

# What is the HTTP Host Header?

The **Host** header is an HTTP request header that identifies the intended destination host for a request.

Conceptually:

```
Browser

↓

HTTP Request

↓

Host Header

↓

Web Server
```

The Host header allows multiple websites to share the same server or IP address while enabling the server to determine which application should receive the request.

---

# Why the Host Header Exists

Modern web servers frequently host multiple websites on the same infrastructure.

Without the Host header:

```
Client

↓

Shared Server

↓

?

↓

Application
```

With the Host header:

```
Client

↓

Host Header

↓

Web Server

↓

Correct Website
```

The server can route the request to the appropriate application.

---

# Basic HTTP Request Structure

A simplified HTTP request contains:

```
HTTP Request

│

├── Request Line

├── Headers

│    ├── Host

│    ├── User-Agent

│    ├── Accept

│    └── Others

└── Message Body (Optional)
```

Each header provides additional information to the receiving server.

---

# Virtual Hosting

Virtual hosting enables multiple websites to operate from a single server.

```
Internet

↓

Web Server

│

├── Site A

├── Site B

├── Site C

└── Site D
```

The Host header helps identify which virtual host should process an incoming request.

---

# High-Level Request Routing

```
Client

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Virtual Host

↓

Application
```

Every routing layer should follow trusted configuration rather than making security-sensitive assumptions about unvalidated client input.

---

# Reverse Proxy Integration

Many enterprise deployments place reverse proxies in front of applications.

```
Client

↓

Load Balancer

↓

Reverse Proxy

↓

Application
```

Reverse proxies often perform routing, TLS termination, logging, and traffic management.

---

# Enterprise Request Flow

```
Client

↓

DNS

↓

CDN

↓

Load Balancer

↓

Reverse Proxy

↓

Application

↓

Database
```

Each layer contributes to reliable request routing and secure application delivery.

---

# Trust Boundary

```
Client Request

──────── Trust Boundary ────────

Application

↓

Business Logic
```

The Host header originates from the client request and should therefore be treated as untrusted until validated.

---

# High-Level Host Header Attack Concept

Host Header attacks occur when applications make important decisions based on untrusted Host header values.

Conceptually:

```
Incoming Request

↓

Host Header

↓

Application Logic

↓

Unexpected Behavior
```

This chapter focuses on defensive architecture, validation, and secure configuration rather than offensive techniques.

---

# Why Host Header Issues Occur

These issues commonly arise because of:

- Missing validation
- Inconsistent routing logic
- Legacy application behavior
- Incorrect proxy configuration
- Overreliance on client-controlled headers

```
Client Header

↓

Application Trust

↓

Business Logic
```

Applications should validate and normalize request information before using it.

---

# Sensitive Functions

Host-related information may influence:

- URL generation
- Password reset workflows
- Email notifications
- Redirect generation
- Reverse proxy routing
- Multi-tenant applications
- Administrative portals

Security-sensitive operations should avoid relying solely on untrusted request headers.

---

# Host Header Validation

Applications should validate host information before using it.

```
Incoming Request

↓

Validation

↓

Approved Host

↓

Business Logic
```

Validation should be based on trusted configuration rather than assumptions.

---

# Enterprise Architecture

```
Internet

↓

CDN

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Application

↓

Database
```

Host validation may occur at multiple layers depending on architecture.

---

# Defense in Depth

Host validation should complement other application security controls.

```
Input Validation

↓

Host Validation

↓

Authentication

↓

Authorization

↓

Business Logic

↓

Monitoring
```

No single control should be relied upon exclusively.

---

# Secure Design Principles

```
Secure Host Handling

│

├── Trusted Configuration

├── Validation

├── Normalization

├── Least Trust

├── Logging

├── Monitoring

├── Documentation

└── Continuous Review
```

Host-related decisions should be deterministic and policy-driven.

---

# Enterprise Example

A multinational software company hosts several customer portals behind a shared reverse proxy.

```
Customer

↓

CDN

↓

Load Balancer

↓

Reverse Proxy

↓

Customer Portal
```

The organization validates incoming host information against centrally managed configuration before routing requests or generating application URLs.

---

# Components Involved

```
Host Processing

│

├── Browser

├── DNS

├── CDN

├── Load Balancer

├── Reverse Proxy

├── Web Server

├── Application

└── Monitoring
```

Every component contributes to secure request handling.

---

# Secure Host Handling Goals

Applications should provide:

- Trusted routing
- Deterministic request handling
- Consistent validation
- Approved hostnames
- Operational visibility
- Secure defaults

---

# Hands-on Lab (Conceptual)

1. Draw the request-routing architecture of an enterprise web application.
2. Identify where Host header information is processed.
3. Mark trust boundaries between client requests and application logic.
4. Document approved hostnames used by the application.
5. Review where absolute URLs are generated within business workflows.

> Perform all activities only in environments where you have explicit authorization. Focus on architecture review, validation, governance, and defensive request handling.

---

# Interview Questions

1. What is the HTTP Host header?
2. Why was the Host header introduced?
3. What is virtual hosting?
4. Why should Host header values be treated as untrusted?
5. What is a reverse proxy?
6. Which business functions commonly use host information?
7. Why is validation important?
8. How does defense in depth improve request handling?
9. What is a trust boundary?
10. Why should routing decisions be centrally governed?

---

# Best Practices

- Treat Host header values as untrusted input.
- Validate hostnames against trusted configuration.
- Centralize host validation logic.
- Document approved hostnames.
- Review proxy configurations regularly.
- Include host handling in architecture reviews.
- Monitor host-related operational events.
- Standardize request-routing behavior across environments.

---

# Common Mistakes

- Trusting client-controlled Host header values.
- Using inconsistent validation rules.
- Allowing configuration drift across environments.
- Overlooking reverse proxy behavior.
- Generating security-sensitive URLs from unvalidated host information.
- Failing to document approved hostnames.

---

# Key Takeaways

- The Host header enables virtual hosting and request routing.
- Host header values originate from the client and should be validated.
- Reverse proxies, load balancers, and applications all participate in request processing.
- Secure routing depends on trusted configuration, deterministic validation, and layered controls.
- Centralized governance and continuous review improve enterprise resilience against Host header-related issues.

```text id="rrks28"
**Next:** Part 2
```