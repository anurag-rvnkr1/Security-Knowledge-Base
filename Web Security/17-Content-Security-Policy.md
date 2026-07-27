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

# 17-Content-Security-Policy.md

# Part 2 — CSP Directives, Resource Types, Policy Design, Nonces, Hashes, Reporting, and Enterprise Deployment

> **"An effective Content Security Policy precisely defines what the browser is allowed to load. The principle is simple: explicitly allow only trusted resources and deny everything else."**

---

# Learning Objectives

After completing this part, you will understand:

- CSP Directive Categories
- Resource-Specific Policies
- Default Policy Behavior
- Nonces (Conceptual)
- Hash-Based Policies (Conceptual)
- CSP Reporting
- Policy Design Strategy
- Enterprise Deployment
- Common Misconfigurations
- Defense in Depth

---

# CSP Directive Structure

A Content Security Policy is composed of multiple directives.

```
Content Security Policy

│

├── Default Rules

├── Script Rules

├── Style Rules

├── Image Rules

├── Font Rules

├── Connection Rules

├── Frame Rules

└── Reporting Rules
```

Each directive governs a specific category of browser behavior.

---

# Resource Categories

Browsers load many different resource types.

```
Web Application

│

├── HTML

├── JavaScript

├── CSS

├── Images

├── Fonts

├── Media

├── Frames

└── API Connections
```

CSP allows each category to be managed independently.

---

# Default Policy Concept

A default policy establishes the baseline behavior for resources.

```
Browser Requests Resource

↓

Specific Rule Exists?

↓

Yes

↓

Use Specific Rule

──────────────

No

↓

Apply Default Rule
```

This provides a fallback mechanism for resource evaluation.

---

# Script Resources

JavaScript is one of the highest-risk resource categories.

```
Browser

↓

Load Script

↓

Evaluate CSP

↓

Allowed?

↓

Yes → Execute

No → Block
```

Restricting script execution is one of the primary objectives of CSP.

---

# Style Resources

```
Browser

↓

Load CSS

↓

Policy Check

↓

Allow

OR

Block
```

Style resources should also be restricted to trusted origins.

---

# Image Resources

```
Image Request

↓

Browser

↓

CSP Check

↓

Load

OR

Reject
```

Although images are generally less risky than scripts, they should still be controlled.

---

# Font Resources

```
Browser

↓

Font Request

↓

Policy Evaluation

↓

Allowed?

↓

Load

OR

Block
```

Restricting font sources reduces unnecessary external dependencies.

---

# Network Connections

Modern web applications frequently communicate with APIs.

```
Browser

↓

API Request

↓

CSP Evaluation

↓

Allowed Endpoint?

↓

Yes

↓

Connection Established
```

Only approved endpoints should be permitted.

---

# Frames

Applications may embed or be embedded within other pages.

```
Parent Page

↓

Embedded Content

↓

Browser

↓

Policy Validation
```

Frame-related directives help control these interactions.

---

# Principle of Least Privilege

```
Everything

↓

Blocked By Default

↓

Explicitly Allow

↓

Only Trusted Resources
```

Grant only the minimum permissions necessary for application functionality.

---

# Policy Design Strategy

```
Identify Resources

↓

Classify Trust

↓

Create Policy

↓

Test

↓

Deploy

↓

Monitor

↓

Improve
```

Policies should evolve alongside the application.

---

# Nonces (Conceptual)

A **nonce** is a unique value generated for a page load that allows approved scripts to execute.

Conceptually:

```
Server

↓

Generate Unique Value

↓

Browser Receives Page

↓

Browser Verifies

↓

Approved Script Executes
```

The value should be unpredictable and generated securely.

---

# Why Nonces Help

```
Unexpected Script

↓

No Valid Nonce

↓

Browser

↓

Reject Execution
```

Only scripts associated with the expected nonce are permitted to execute.

---

# Hash-Based Policies (Conceptual)

Another approach allows execution based on the cryptographic hash of approved content.

```
Script

↓

Calculate Hash

↓

Browser

↓

Hash Matches Policy?

↓

Yes → Execute

No → Block
```

This approach is often suitable for static content that rarely changes.

---

# Nonces vs Hashes

| Feature | Nonce | Hash |
|---------|-------|------|
| Generated | Per page/request | Based on script content |
| Suitable For | Dynamic content | Static content |
| Browser Validation | Unique value | Content fingerprint |
| Primary Goal | Authorize trusted scripts | Verify approved script content |

---

# Inline Content

Inline content should be carefully reviewed during CSP design.

```
Inline Content

↓

Policy Evaluation

↓

Trusted?

↓

Allow

OR

Block
```

Reducing unnecessary inline content generally improves security.

---

# Third-Party Resources

Many applications rely on external providers.

```
Application

↓

Third-Party Resource

↓

Browser

↓

Policy Check

↓

Approved?

↓

Load

OR

Reject
```

Every external dependency should be evaluated before inclusion.

---

# CSP Reporting

Browsers can generate reports when policy violations occur.

```
Policy Violation

↓

Browser

↓

Generate Report

↓

Security Monitoring

↓

Investigation
```

Reporting helps organizations identify both attacks and policy configuration issues.

---

# Reporting Workflow

```
Browser

↓

Detect Violation

↓

Generate Event

↓

Security Platform

↓

Review

↓

Improve Policy
```

Monitoring should be an ongoing operational activity.

---

# Enterprise Architecture

```
                  Browser

                     ▲

                     │

          CSP Response Header

                     │

                     ▼

              Web Application

                     │

     Authentication & Authorization

                     │

        Business Logic

                     │

       Resource Generation

                     │

        Content Security Policy

                     │

                     ▼

             Browser Enforcement
```

---

# Enterprise Example

An enterprise HR platform loads:

- Internal JavaScript
- Internal CSS
- Corporate fonts
- Approved API endpoints

The browser evaluates each request against the organization's CSP before allowing it.

---

# Security Review Checklist

```
✓ Scripts Restricted

✓ Styles Restricted

✓ Images Reviewed

✓ Fonts Reviewed

✓ API Endpoints Approved

✓ Third-Party Resources Reviewed

✓ Reporting Enabled

✓ Policy Tested
```

---

# Common Misconfigurations

| Misconfiguration | Risk |
|------------------|------|
| Overly permissive resource rules | Larger attack surface |
| Unnecessary third-party resources | Increased exposure |
| Missing reporting | Reduced visibility |
| Policy not updated after application changes | Broken functionality or security gaps |
| Inconsistent policies across applications | Operational complexity |

---

# Hands-on Lab (Conceptual)

1. Review the application's resource inventory.
2. Classify each resource by type.
3. Identify which resources originate from trusted and external locations.
4. Draw a conceptual CSP covering each resource category.
5. Document where violation reporting would support security operations.

> Perform testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is the purpose of CSP directives?
2. Why is JavaScript considered a high-risk resource?
3. What is the principle of least privilege in CSP?
4. What is a CSP nonce?
5. When are hash-based policies useful?
6. How do browsers enforce CSP?
7. Why should third-party resources be reviewed carefully?
8. What is the purpose of CSP violation reporting?
9. Why should policies evolve with the application?
10. What are the benefits of restricting resource categories independently?

---

# Best Practices

- Apply the principle of least privilege to resource loading.
- Restrict each resource type independently.
- Use nonces or hashes where appropriate instead of broad allowances.
- Review all third-party dependencies regularly.
- Enable CSP violation reporting and integrate it with monitoring.
- Test policy changes before deploying them to production.
- Keep CSP aligned with application architecture changes.

---

# Common Mistakes

- Creating overly permissive policies.
- Trusting every third-party resource by default.
- Ignoring CSP violation reports.
- Treating CSP as a substitute for secure coding.
- Failing to update policies when new resources are introduced.
- Allowing inconsistent CSP configurations across environments.

---

# Key Takeaways

- CSP directives control different categories of browser resources.
- The principle of least privilege should guide CSP policy design.
- Nonces and hashes provide mechanisms to authorize trusted scripts.
- CSP reporting improves visibility into policy violations.
- Enterprise CSP deployment requires continuous review, testing, and monitoring.

```text id="jid720"
**Next:** Part 3
```