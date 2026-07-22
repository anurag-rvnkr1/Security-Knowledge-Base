# A10:2021 – Server-Side Request Forgery (SSRF)

# Part 1 — Foundations, Architecture, Attack Flow, and Core Concepts

---

# Overview

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to force a server-side application to send unintended requests to internal or external resources.

Instead of the attacker communicating directly with the target, the vulnerable application becomes the proxy.

```
Attacker
    │
    │ URL Input
    ▼
Vulnerable Web Application
    │
    │ Makes Request
    ▼
Internal Network / Cloud Metadata / APIs
```

Because the request originates from the trusted application, SSRF can bypass network restrictions, firewalls, IP filtering, and access controls.

---

# Why SSRF Matters

Many organizations expose only a few public-facing services while protecting critical infrastructure behind firewalls.

Example:

```
Internet

      │

      ▼

+----------------------+
| Public Web Server    |
+----------------------+
          │
          │ Trusted Network
          ▼

+----------------------+
| Internal API         |
+----------------------+

+----------------------+
| Database             |
+----------------------+

+----------------------+
| Admin Dashboard      |
+----------------------+
```

Normally, external users cannot directly access internal systems.

However, if the public server is vulnerable to SSRF, an attacker may leverage it to reach internal resources.

---

# What Makes SSRF Dangerous?

Unlike many web vulnerabilities, SSRF targets the **server's trust relationships** rather than the user's browser.

Potential consequences include:

- Internal network reconnaissance
- Cloud credential theft
- Access to internal APIs
- Authentication bypass
- Firewall bypass
- Sensitive data exposure
- Remote service interaction
- Lateral movement
- Remote code execution (in certain scenarios)

---

# High-Level SSRF Workflow

```
Attacker

↓

Supplies Malicious URL

↓

Application Accepts URL

↓

Server Sends HTTP Request

↓

Internal Resource Responds

↓

Application Returns Response

↓

Attacker Reads Sensitive Data
```

---

# Example Vulnerable Feature

Many web applications retrieve remote resources.

Examples include:

- Image fetching
- PDF generation
- Webhook validation
- URL previews
- RSS readers
- Avatar import
- File conversion
- Video thumbnail generation

Example API:

```
POST /fetch

{
    "url":"https://example.com/image.png"
}
```

If the application fails to validate the destination, attackers may provide arbitrary URLs.

---

# Basic SSRF Example

Normal request:

```
POST /fetch

url=https://example.com/logo.png
```

Server:

```
GET https://example.com/logo.png
```

Everything functions as intended.

---

Attacker request:

```
POST /fetch

url=http://127.0.0.1/admin
```

Server:

```
GET http://127.0.0.1/admin
```

The attacker cannot normally reach `127.0.0.1`, but the server can.

---

# Trust Relationships

```
Internet User

        X

Cannot Reach

↓

Internal API
```

However:

```
Internet User

↓

Web Application

↓

Internal API
```

The application already trusts the internal API.

SSRF abuses this trust.

---

# SSRF Request Flow

```
Attacker

↓

URL Parameter

↓

Application

↓

HTTP Client

↓

Target Server

↓

Response

↓

Application

↓

Attacker
```

The application unknowingly acts as the attacker's proxy.

---

# Real-World SSRF Entry Points

Common features vulnerable to SSRF include:

### Image Upload by URL

```
Import Profile Picture

↓

Server Downloads Image
```

---

### PDF Generator

```
Generate PDF

↓

Render Remote Content
```

---

### Webhooks

```
Webhook Validation

↓

Server Connects
```

---

### URL Preview

```
Paste Link

↓

Server Retrieves Metadata
```

---

### XML Processors

```
XML Input

↓

External Resource Resolution
```

(When external entity processing is enabled.)

---

### API Integrations

```
CRM

↓

Internal API

↓

External API
```

Improper validation may enable SSRF through integration endpoints.

---

# Types of SSRF

SSRF is commonly categorized into two broad types.

---

## Basic SSRF

The attacker receives the server's response.

```
Attacker

↓

Application

↓

Internal Server

↓

Response

↓

Attacker
```

Example:

```
GET http://127.0.0.1/admin
```

The attacker directly observes the returned content.

---

## Blind SSRF

The attacker cannot see the response but can still trigger server-side requests.

```
Attacker

↓

Application

↓

Internal Service
```

Possible evidence includes:

- DNS lookups
- External callbacks
- Timing differences
- Out-of-band interactions
- Log entries

Blind SSRF is often identified using out-of-band testing techniques.

---

# Common SSRF Targets

```
Internal Admin Panels

↓

Cloud Metadata Services

↓

Redis

↓

Docker API

↓

Kubernetes API

↓

Elasticsearch

↓

Jenkins

↓

Prometheus

↓

Grafana

↓

Internal REST APIs

↓

Service Discovery Systems
```

---

# Localhost Attacks

Many applications trust localhost.

Common targets include:

```
127.0.0.1

localhost

::1
```

Potential services:

- Admin interfaces
- Monitoring dashboards
- Internal APIs
- Local databases
- Metrics endpoints

---

# Internal Network Attacks

Attackers may attempt requests such as:

```
http://10.0.0.5

http://172.16.0.10

http://192.168.1.20
```

The objective is to discover internal services that are not exposed externally.

---

# Cloud Metadata Services

Cloud providers expose instance metadata services for legitimate administrative purposes.

Examples:

```
AWS

169.254.169.254
```

```
Azure

169.254.169.254
```

```
Google Cloud

169.254.169.254
```

If accessible through SSRF, these services may reveal sensitive instance metadata or temporary credentials unless additional protections are in place.

---

# Internal Service Discovery

An attacker may attempt requests to:

```
http://10.0.0.5:8080

↓

Response?

↓

Port Open?
```

Different response behaviors can help infer:

- Open ports
- Running services
- Internal applications
- Network topology

---

# Why Firewalls May Not Help

Traditional firewalls often restrict incoming traffic from the Internet.

```
Internet

X

Internal API
```

However, SSRF requests originate from the trusted application.

```
Application

↓

Internal API
```

Since the application is already authorized to communicate internally, network controls may permit the request.

---

# SSRF vs Client-Side Request

### Browser Request

```
User Browser

↓

Website
```

Originates from the user's device.

---

### SSRF

```
Server

↓

Target
```

Originates from the application server.

This distinction is fundamental to understanding SSRF.

---

# Common Root Causes

SSRF vulnerabilities typically arise when applications:

- Accept arbitrary URLs from users.
- Fetch remote resources without validation.
- Trust all outbound destinations.
- Lack outbound network restrictions.
- Permit access to internal addresses.
- Follow redirects without verification.
- Do not validate protocols or hostnames.

---

# Business Impact

Successful SSRF attacks may enable:

- Exposure of sensitive internal data.
- Discovery of internal network architecture.
- Theft of cloud credentials.
- Unauthorized access to administrative interfaces.
- Bypass of perimeter defenses.
- Pivoting to additional internal systems.
- Service disruption.
- Escalation to broader infrastructure compromise.

---

# Key Takeaways

- SSRF occurs when an application makes unintended server-side requests using attacker-controlled input.
- The vulnerability abuses the server's trust relationships rather than the client's browser.
- Internal services, localhost, cloud metadata endpoints, and private APIs are common targets.
- Basic SSRF returns the server's response, while Blind SSRF relies on indirect indicators such as DNS or timing.
- Preventing SSRF requires careful validation of outbound requests, network segmentation, and least-privilege access for server-side components.