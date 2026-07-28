# 43-Clickjacking.md

# Part 1 — Introduction to Clickjacking, UI Redressing, Browser Security, and Defensive Design

> **"Clickjacking is a user interface security issue where users are tricked into interacting with web content different from what they perceive. Secure applications defend against clickjacking by controlling how their pages can be embedded, implementing browser security mechanisms, and designing trustworthy user interfaces."**

---

# Learning Objectives

After completing this part, you will understand:

- What Clickjacking Is
- UI Redressing
- Browser Rendering Fundamentals
- Frames and Iframes
- How Clickjacking Works (High-Level)
- Trust Boundaries
- Browser Security Controls
- Enterprise Architecture
- Defensive Design Principles

---

# What is Clickjacking?

**Clickjacking** is a web security issue where a user is deceived into clicking or interacting with an interface element that is different from what appears on the screen.

Rather than targeting servers directly, clickjacking targets the **user interface (UI)** and user perception.

```
User

↓

Visible Interface

↓

Hidden or Embedded Interface

↓

Unexpected Action
```

The focus of this chapter is on **defensive architecture and secure browser behavior**, not offensive techniques.

---

# Why Clickjacking Matters

Modern web applications expose many sensitive actions through graphical interfaces.

Examples include:

- Profile updates
- Account settings
- Payment confirmations
- Permission grants
- Administrative actions
- File operations
- Workflow approvals

Protecting these interfaces helps preserve user intent.

---

# UI Redressing

Clickjacking is often described as a **UI Redressing** problem.

```
User

↓

Visual Interface

↓

Perceived Action

↓

Actual Action
```

The security objective is to ensure that the action the user believes they are performing matches the action actually executed.

---

# Browser Rendering

Browsers render multiple resources to create a webpage.

```
HTML

↓

CSS

↓

JavaScript

↓

Rendering Engine

↓

Visible Web Page
```

Some browser features allow one webpage to embed another under controlled circumstances.

---

# Frames

A **frame** allows one web document to display another web document.

```
Browser Window

│

├── Main Page

└── Embedded Page
```

Frames improve interoperability for some legitimate business scenarios.

---

# Iframes

The most common modern framing mechanism is the **iframe**.

```
Browser

↓

Parent Page

↓

Iframe

↓

Embedded Content
```

Organizations should carefully control which pages are allowed to be embedded.

---

# Legitimate Uses of Iframes

Iframes have many valid uses.

Examples include:

- Payment widgets
- Maps
- Embedded videos
- Internal dashboards
- Documentation portals
- Partner integrations

Security controls should distinguish between legitimate embedding and unauthorized embedding.

---

# Browser Trust Boundary

```
Internet

──────── Trust Boundary ────────

Browser

↓

Rendered Interface

↓

User
```

The browser is responsible for enforcing several security mechanisms related to framing.

---

# High-Level Clickjacking Workflow

Conceptually:

```
User

↓

Rendered Interface

↓

Browser

↓

Protected Application
```

Defensive controls ensure that sensitive pages cannot be embedded or interacted with in unintended contexts.

---

# Why Clickjacking Occurs

Clickjacking generally results from:

- Pages being embeddable when they should not be
- Missing browser security headers
- Inadequate UI protection
- Legacy browser behavior
- Insufficient security reviews

```
Application

↓

Browser

↓

Rendered UI

↓

User Interaction
```

---

# Sensitive User Actions

Applications should pay particular attention to interfaces involving:

- Authentication
- Authorization changes
- Financial transactions
- Account management
- Administrative functions
- Security settings
- Consent dialogs

These actions benefit from additional browser protections.

---

# Browser Security Controls

Modern browsers provide multiple mechanisms that help defend against clickjacking.

```
Browser Protection

│

├── Framing Policy

├── Security Headers

├── Rendering Restrictions

├── Origin Checks

└── UI Isolation
```

These mechanisms work together to reduce UI-related risks.

---

# Trust Relationships

```
User

↓

Browser

↓

Application

↓

Business Logic
```

Applications should preserve trust between user intent and application behavior.

---

# Enterprise Architecture

```
Client

↓

Browser

↓

Web Server

↓

Application

↓

Business Logic

↓

Database
```

Clickjacking defenses are primarily enforced at the browser and web server layers.

---

# Defense in Depth

No single control completely addresses UI security.

```
Security Headers

↓

Browser Enforcement

↓

Authentication

↓

Authorization

↓

Application Logic

↓

Monitoring
```

Layered defenses improve resilience.

---

# Secure UI Design Principles

```
Secure UI

│

├── User Awareness

├── Browser Protection

├── Clear Interaction

├── Trusted Navigation

├── Sensitive Action Protection

├── Monitoring

└── Continuous Review
```

Applications should minimize opportunities for misleading user interactions.

---

# Enterprise Example

An online banking portal provides pages for transferring funds and changing account settings.

```
Customer

↓

Browser

↓

Banking Portal

↓

Transaction Service
```

The organization ensures that sensitive pages cannot be embedded in unauthorized contexts and continuously reviews browser security policies during application releases.

---

# Components Involved

```
Clickjacking Protection

│

├── Browser

├── Web Server

├── Security Headers

├── Authentication

├── Application

├── Logging

└── Monitoring
```

Every component contributes to protecting user interactions.

---

# Secure Design Goals

A secure application should provide:

- Trusted user interactions
- Controlled page embedding
- Browser-enforced protections
- Clear visual interfaces
- Secure defaults
- Operational visibility

---

# Hands-on Lab (Conceptual)

1. Draw the browser rendering pipeline for a web application.
2. Identify pages that contain sensitive user actions.
3. Determine which pages should never be embedded.
4. Identify trust boundaries between browser, application, and user.
5. Document browser security controls used by the application.

> Perform all activities only in environments where you have explicit authorization. Focus on secure browser behavior, defensive design, and UI protection rather than offensive techniques.

---

# Interview Questions

1. What is Clickjacking?
2. What is UI Redressing?
3. What is an iframe?
4. Why are iframes used legitimately?
5. Which application pages require additional UI protection?
6. Why are browser security controls important?
7. What is the browser's role in preventing clickjacking?
8. What is meant by defense in depth for UI security?
9. Why should trust boundaries be documented?
10. Why should organizations review browser security policies regularly?

---

# Best Practices

- Identify sensitive user interfaces during design.
- Restrict page embedding where unnecessary.
- Use modern browser security mechanisms.
- Review browser behavior during security testing.
- Apply layered security controls.
- Document trusted embedding relationships.
- Monitor browser-related security events.
- Include UI security in architecture reviews.

---

# Common Mistakes

- Allowing unrestricted page embedding.
- Assuming browsers always provide sufficient defaults.
- Ignoring UI security during application design.
- Failing to review browser security headers.
- Overlooking sensitive administrative interfaces.
- Treating clickjacking solely as a browser problem.

---

# Key Takeaways

- Clickjacking is a user interface security issue rather than a server-side vulnerability.
- The objective is to protect user intent and prevent unintended interactions.
- Browser security mechanisms play a central role in mitigating clickjacking.
- Sensitive pages require stronger protection than ordinary informational pages.
- Secure UI design, browser protections, and defense in depth provide effective enterprise mitigation.

```text id="rrks28"
**Next:** Part 2
```