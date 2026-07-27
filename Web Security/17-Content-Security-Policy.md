# 17-Content-Security-Policy.md

# Part 1 — Content Security Policy (CSP) Fundamentals, Browser Security Model, Directives, and Enterprise Overview

> **"Content Security Policy (CSP) is a browser-enforced security mechanism that helps reduce the impact of Cross-Site Scripting (XSS) and other content injection attacks by controlling which resources a web page is allowed to load and execute."**

---

# Learning Objectives

After completing this part, you will understand:

- What Content Security Policy (CSP) Is
- Why CSP Exists
- Browser Trust Model
- CSP Architecture
- How Browsers Enforce CSP
- CSP Directives
- CSP Delivery Methods
- Enterprise Benefits
- Common Misconceptions
- Defense in Depth

---

# What is Content Security Policy (CSP)?

**Content Security Policy (CSP)** is an HTTP response policy that instructs the browser which resources are permitted to load and execute.

```
Web Server

↓

HTTP Response

↓

Content Security Policy

↓

Browser

↓

Evaluate Policy

↓

Allow

OR

Block Resource
```

CSP is enforced by the browser—not by the web server.

---

# Why CSP Exists

Modern web applications load many types of content.

```
Web Page

│

├── HTML

├── CSS

├── JavaScript

├── Images

├── Fonts

├── Media

└── External Resources
```

Without restrictions, unexpected or malicious content may execute if an application becomes vulnerable.

---

# Browser Trust Model

```
Application

↓

HTML Response

↓

Browser

↓

Read CSP

↓

Apply Rules

↓

Render Page
```

The browser evaluates every relevant resource against the policy before loading or executing it.

---

# Why CSP Is Important

CSP helps reduce the impact of vulnerabilities such as:

- Cross-Site Scripting (XSS)
- Content Injection
- Unauthorized Resource Loading
- Malicious Third-Party Scripts
- Some Data Exfiltration Techniques

CSP should complement secure coding practices rather than replace them.

---

# High-Level CSP Workflow

```
Client Request

↓

Server Response

↓

CSP Included

↓

Browser Reads Policy

↓

Resource Requested

↓

Allowed?

↓

Yes → Load

No  → Block
```

---

# Browser Enforcement

The browser acts as the policy enforcement point.

```
Resource Request

↓

Browser

↓

Compare With CSP

↓

Policy Match?

↓

Allow

OR

Block
```

Applications define the policy, but browsers enforce it.

---

# CSP and XSS

```
Application

↓

Unexpected Script

↓

Browser Checks CSP

↓

Allowed?

↓

Block If Policy Disallows
```

A properly configured CSP can significantly reduce the impact of many XSS attacks.

---

# CSP is Not a Replacement

```
Secure Coding

+

Output Encoding

+

Input Validation

+

Authentication

+

Authorization

+

CSP

↓

Layered Security
```

CSP is one component of a defense-in-depth strategy.

---

# CSP Delivery Methods

A CSP can be delivered using:

```
Server

│

├── HTTP Response Header

└── HTML Meta Element
```

In enterprise environments, HTTP response headers are generally preferred because they apply consistently and earlier in page processing.

---

# CSP Architecture

```
                Browser

                   ▲

                   │

         HTTP Response + CSP

                   │

                   ▼

             Web Application

                   │

         Static / Dynamic Content
```

The browser continuously evaluates resource loading decisions against the policy.

---

# Resource Categories

CSP governs multiple resource types.

```
Resources

│

├── Scripts

├── Styles

├── Images

├── Fonts

├── Frames

├── Media

├── Workers

└── Connections
```

Each category can be controlled independently.

---

# CSP Directives

A CSP consists of **directives**.

Conceptually:

```
Content Security Policy

│

├── Script Rules

├── Style Rules

├── Image Rules

├── Font Rules

├── Connection Rules

└── Frame Rules
```

Each directive controls a specific category of browser behavior.

---

# Browser Decision Process

```
Page Requests Resource

↓

Find Applicable Directive

↓

Evaluate Policy

↓

Resource Allowed?

↓

Yes → Load

No  → Block
```

---

# Enterprise Example

```
Corporate Portal

↓

Browser Loads Dashboard

↓

Requests External Script

↓

Browser Checks CSP

↓

Allowed?

↓

Load

OR

Block
```

This reduces the likelihood of unauthorized resources executing within the application.

---

# Common Use Cases

Organizations commonly deploy CSP to:

- Reduce XSS impact
- Restrict third-party JavaScript
- Control external resource loading
- Strengthen browser security
- Improve security monitoring
- Support secure development practices

---

# Browser Security Layers

```
HTTPS

↓

Authentication

↓

Authorization

↓

Output Encoding

↓

Content Security Policy

↓

Monitoring
```

Each layer addresses different security risks.

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| CSP completely prevents XSS | CSP reduces risk but does not eliminate the need for secure coding |
| CSP replaces output encoding | Output encoding remains essential |
| CSP is enforced by the server | CSP is enforced by the browser |
| HTTPS automatically provides CSP | HTTPS and CSP address different security concerns |

---

# Benefits of CSP

| Benefit | Description |
|----------|-------------|
| Reduced XSS Impact | Limits execution of unauthorized content |
| Resource Control | Restricts where resources may load from |
| Browser Enforcement | Policy enforced automatically by browsers |
| Defense in Depth | Complements existing security controls |
| Better Visibility | Supports monitoring through violation reporting |

---

# Secure Design Principle

```
Application

↓

Define Trust Boundaries

↓

Specify Allowed Resources

↓

Browser Enforces Policy
```

Only explicitly trusted resources should be permitted.

---

# Hands-on Lab (Conceptual)

1. Open a web page using browser Developer Tools.
2. Inspect the HTTP response headers.
3. Determine whether a Content Security Policy is present.
4. Identify the resource categories protected by the policy.
5. Draw a high-level diagram of how the browser evaluates resource requests.

> Perform testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is Content Security Policy (CSP)?
2. Why was CSP introduced?
3. Who enforces a Content Security Policy?
4. Does CSP replace secure coding?
5. What types of resources can CSP control?
6. How does CSP help mitigate XSS?
7. What are CSP directives?
8. Why are HTTP response headers generally preferred for CSP delivery?
9. Why is CSP considered a defense-in-depth mechanism?
10. What happens when a browser encounters a resource that violates the policy?

---

# Best Practices

- Deploy CSP alongside secure coding practices.
- Prefer HTTP response headers for policy delivery.
- Restrict resource loading to trusted origins.
- Review CSP whenever application architecture changes.
- Test policies before production deployment.
- Monitor policy violations to identify misconfigurations or attacks.

---

# Common Mistakes

- Treating CSP as a complete replacement for XSS prevention.
- Allowing unnecessary external resources.
- Forgetting to review third-party dependencies.
- Applying inconsistent CSP policies across applications.
- Ignoring browser violation reports.

---

# Key Takeaways

- Content Security Policy is a browser-enforced security mechanism.
- CSP controls which resources may load and execute.
- It significantly reduces the impact of many content injection attacks.
- CSP complements—but does not replace—secure coding and output encoding.
- Enterprise applications should treat CSP as an essential layer in a defense-in-depth strategy.

```text id="jid720"
**Next:** Part 2
```