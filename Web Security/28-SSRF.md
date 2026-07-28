# 28-Server-Side-Request-Forgery-(SSRF).md

# Part 1 — Fundamentals of Server-Side Request Forgery (SSRF), Architecture, Attack Surface, and Enterprise Overview

> **"Server-Side Request Forgery (SSRF) occurs when a server is tricked into making requests to unintended destinations. The real risk is not merely sending requests—it is abusing the server's trust, network position, or access privileges."**

---

# Learning Objectives

After completing this part, you will understand:

- OWASP A10:2021 Overview
- What SSRF is
- SSRF Fundamentals
- SSRF Architecture
- Trust Boundaries
- Internal vs External Requests
- SSRF Attack Surface
- Enterprise Examples
- SSRF Risk Factors
- High-Level Mitigations

---

# What is Server-Side Request Forgery (SSRF)?

Server-Side Request Forgery (SSRF) is a vulnerability in which an application accepts a user-controlled resource reference (such as a URL) and causes the **server** to make a network request on the user's behalf.

Instead of the user's browser making the request:

```
User

↓

Application Server

↓

Remote Resource
```

the application server becomes the requester.

---

# Why SSRF is Dangerous

Servers often have privileges unavailable to external users.

For example, servers may have access to:

- Internal applications
- Private APIs
- Backend services
- Cloud resources
- Internal DNS
- Enterprise management systems

Therefore, requests originating from the server may reach resources that are inaccessible from the public Internet.

---

# SSRF in the OWASP Top 10

```
OWASP Top 10

↓

A10:2021

↓

Server-Side Request Forgery
```

Although SSRF may appear simple, it can have significant security implications depending on the application's architecture.

---

# Understanding Client vs Server Requests

### Normal Request

```
Browser

↓

Public Website
```

---

### Server-Side Request

```
Browser

↓

Application

↓

External Service
```

The server communicates with another service to complete a business function.

---

# Legitimate Server Requests

Applications commonly make server-side requests for valid business purposes.

Examples include:

```
Application

│

├── Payment Gateway

├── Image Retrieval

├── Weather API

├── Email Service

├── Identity Provider

├── Inventory API

└── Shipping Service
```

Server-side requests are normal; SSRF arises when user-controlled input improperly influences the destination.

---

# High-Level SSRF Concept

```
User Input

↓

Application

↓

Server Makes Request

↓

Unexpected Destination
```

The application's trust in user-supplied input creates the security concern.

---

# Enterprise SSRF Architecture

```
              Internet

                  │

                  ▼

         Web Application

          ┌───────────────┐

          ▼               ▼

 External APIs      Internal Network

                          │

                    Private Services
```

The application server often has broader network visibility than external users.

---

# Trust Boundaries

```
Public Internet

↓

Web Server

──────── Trust Boundary ────────

↓

Internal Network

↓

Private Resources
```

Crossing trust boundaries without appropriate validation increases risk.

---

# Internal vs External Resources

| External Resource | Internal Resource |
|-------------------|------------------|
| Public website | Internal application |
| Public API | Private API |
| Public storage | Internal storage |
| Public DNS | Internal DNS |
| Internet service | Enterprise management system |

Servers frequently have access to both environments.

---

# Typical Enterprise Architecture

```
Client

↓

Load Balancer

↓

Web Server

↓

Application

↓

Internal APIs

↓

Database
```

Applications often communicate with multiple backend services.

---

# Why Servers are Trusted

Servers commonly possess:

```
Server Privileges

│

├── Internal Network Access

├── Service Credentials

├── Backend Connectivity

├── API Access

├── DNS Resolution

└── Cloud Permissions
```

These trusted capabilities make SSRF particularly significant.

---

# SSRF Attack Surface

Potential attack surfaces include functionality that accepts user-supplied resource references.

Examples include:

```
Application Features

│

├── URL Preview

├── Image Import

├── File Import

├── Webhook Configuration

├── RSS Feed Import

├── PDF Generation

├── Media Processing

└── Third-Party Integrations
```

Not every feature is vulnerable; proper validation and controls determine security.

---

# Business Features That Use Server Requests

```
User

↓

Application

↓

Business Logic

↓

External Service

↓

Response
```

Examples:

- Fetching profile images
- Integrating payment providers
- Retrieving weather information
- Calling shipping services
- Importing public documents

---

# SSRF Trust Model

```
User

↓

Application Trusts Input

↓

Server Makes Request

↓

Target Resource
```

Applications should carefully validate and control outbound requests.

---

# Direct vs Indirect Requests

### Direct

```
Application

↓

Known Internal Service
```

Destination is predefined by the application.

---

### Indirect

```
Application

↓

User-Influenced Destination
```

User influence over request destinations increases risk and requires additional safeguards.

---

# Enterprise Example

A document management system allows employees to import publicly available images.

```
Employee

↓

Import Feature

↓

Application

↓

Image Server

↓

Display Image
```

If destination validation is insufficient, the application may attempt to access unintended resources.

---

# Common SSRF Risk Factors

| Risk Factor | Description |
|-------------|-------------|
| User-controlled URLs | Users influence outbound requests |
| Broad network access | Server reaches internal services |
| Excessive trust | Requests made without validation |
| Cloud connectivity | Access to cloud services |
| Weak outbound controls | Few restrictions on destinations |
| Limited monitoring | Outbound activity not reviewed |

---

# Enterprise SSRF Workflow

```
User Request

↓

Input Validation

↓

Business Logic

↓

Outbound Request

↓

Destination Verification

↓

Response

↓

Logging
```

Security checks should occur before outbound communication.

---

# High-Level Mitigation Strategy

```
User Input

↓

Validation

↓

Allowlist Verification

↓

Approved Destination

↓

Outbound Request

↓

Monitoring
```

Multiple security layers reduce SSRF risk.

---

# Hands-on Lab (Conceptual)

1. Draw a typical enterprise web application architecture.
2. Identify components that make outbound requests.
3. Mark trust boundaries between public and internal networks.
4. List business features that rely on external services.
5. Identify where request validation should occur.

> Perform all assessments only in environments where you have explicit authorization. This lab focuses on architecture analysis rather than exploitation.

---

# Interview Questions

1. What is Server-Side Request Forgery (SSRF)?
2. Why is SSRF considered dangerous?
3. How does SSRF differ from a normal browser request?
4. What is a trust boundary?
5. Why do application servers often have broader network access?
6. Which business features commonly make outbound server requests?
7. Why is user-controlled input a risk in outbound requests?
8. What is the difference between internal and external resources?
9. Why should outbound requests be monitored?
10. What high-level controls reduce SSRF risk?

---

# Best Practices

- Minimize user influence over outbound request destinations.
- Validate and normalize user-supplied resource references.
- Use allowlists for approved outbound destinations where practical.
- Restrict server access to only required internal and external services.
- Log and monitor outbound network activity.
- Review application features that retrieve remote resources.
- Apply defense in depth through validation, network controls, and monitoring.

---

# Common Mistakes

- Trusting user-supplied URLs without validation.
- Granting servers unnecessary network access.
- Allowing unrestricted outbound connectivity.
- Assuming internal services are unreachable because they are not public.
- Ignoring outbound request logging.
- Treating SSRF solely as an application-layer issue rather than a combination of application and network security.

---

# Key Takeaways

- SSRF occurs when a server makes unintended requests based on insufficiently controlled user input.
- Application servers often have privileged network access, making SSRF impactful.
- Legitimate business features frequently require outbound requests, but those requests must be carefully controlled.
- Trust boundaries and network architecture play a significant role in SSRF risk.
- Validation, destination restrictions, monitoring, and least-privilege network access are fundamental defenses.

```text id="rrks28"
**Next:** Part 2
```