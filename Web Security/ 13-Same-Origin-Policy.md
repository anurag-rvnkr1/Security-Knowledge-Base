# 13-Same-Origin-Policy.md

# Part 1 — Same-Origin Policy Fundamentals, Origins, Browser Security Model, Cross-Origin Interactions, and Enterprise Web Isolation

> **"The Same-Origin Policy (SOP) is one of the most important security mechanisms in web browsers. It prevents one website from freely accessing the sensitive data of another website, forming the foundation of modern web security."**

---

# Learning Objectives

After completing this part, you will understand:

- What the Same-Origin Policy (SOP) Is
- Why SOP Exists
- Browser Security Model
- Origin
- Components of an Origin
- Same-Origin vs Cross-Origin
- SOP Enforcement
- Browser Isolation
- Enterprise Browser Security
- Real-World Examples

---

# What is the Same-Origin Policy (SOP)?

The **Same-Origin Policy (SOP)** is a browser security mechanism that restricts how documents or scripts loaded from one origin can interact with resources from another origin.

```
Browser

↓

Loads Website

↓

Checks Origin

↓

Allow

OR

Block
```

SOP helps prevent unauthorized access to sensitive information across websites.

---

# Why SOP Exists

Imagine two websites:

```
bank.com

shopping.com
```

Without SOP:

```
shopping.com

↓

Reads

↓

bank.com Account Data

↓

Sensitive Information Exposed
```

With SOP:

```
shopping.com

↓

Browser Checks Origin

↓

Blocked
```

The browser prevents unauthorized cross-origin access.

---

# Browser Security Model

Modern browsers isolate websites from one another.

```
Browser

│

├── Website A

├── Website B

├── Website C

└── Website D
```

Each website executes within its own security boundary.

---

# Security Boundary

```
Origin

↓

Security Boundary

↓

Protected Resources
```

The browser uses the **origin** as the primary security boundary.

---

# What is an Origin?

An origin consists of three components:

```
Protocol (Scheme)

+

Host (Domain)

+

Port
```

All three must match for two URLs to have the same origin.

---

# Origin Components

Example:

```
https://example.com:443
```

| Component | Value |
|-----------|-------|
| Protocol | HTTPS |
| Host | example.com |
| Port | 443 |

---

# Origin Comparison

```
https://example.com

↓

HTTPS

↓

example.com

↓

443
```

Compared with:

```
https://example.com

↓

HTTPS

↓

example.com

↓

443
```

Result:

```
Same Origin
```

---

# Different Protocol

```
http://example.com

↓

HTTP
```

vs

```
https://example.com

↓

HTTPS
```

Result:

```
Different Origins
```

Different protocols create different origins.

---

# Different Host

```
https://example.com
```

vs

```
https://admin.example.com
```

Result:

```
Different Origins
```

Subdomains are separate origins.

---

# Different Port

```
https://example.com:443
```

vs

```
https://example.com:8443
```

Result:

```
Different Origins
```

Different ports also produce different origins.

---

# Same-Origin Rule

Two URLs are same-origin **only if**:

```
Protocol

AND

Host

AND

Port

↓

All Match
```

Otherwise:

```
Cross-Origin
```

---

# Examples

| URL A | URL B | Same Origin? |
|--------|--------|--------------|
| https://example.com | https://example.com | Yes |
| http://example.com | https://example.com | No |
| https://example.com | https://admin.example.com | No |
| https://example.com:443 | https://example.com:8443 | No |
| https://store.example.com | https://store.example.com | Yes |

---

# Browser Origin Check

```
Page Requests Resource

↓

Browser Compares Origins

↓

Same?

↓

Yes

↓

Allow

──────────────

No

↓

Apply SOP Rules
```

---

# Resources Protected by SOP

SOP protects access to many browser-controlled resources, including:

- DOM
- Cookies (subject to browser rules)
- Local Storage
- Session Storage
- IndexedDB
- JavaScript objects
- Many network responses

Different resource types have different browser behaviors.

---

# DOM Isolation

Without SOP:

```
Website A

↓

Reads DOM

↓

Website B
```

With SOP:

```
Website A

↓

DOM Access

↓

Blocked
```

One origin cannot freely inspect or modify another origin's DOM.

---

# JavaScript Isolation

Each origin runs independently.

```
Website A

↓

JavaScript

↓

Own Resources

──────────────

Website B

↓

Separate JavaScript

↓

Own Resources
```

This isolation prevents direct cross-origin script access.

---

# Cookie Isolation

Conceptually:

```
bank.com

↓

Cookies

↓

Accessible

↓

bank.com

──────────────

shopping.com

↓

Blocked
```

Cookie behavior is also influenced by cookie attributes such as `SameSite`, `Secure`, and `HttpOnly`.

---

# Storage Isolation

Browser storage is isolated by origin.

```
Origin A

↓

Local Storage A

──────────────

Origin B

↓

Local Storage B
```

Data stored for one origin is generally unavailable to another.

---

# IndexedDB Isolation

```
Origin A

↓

IndexedDB A

──────────────

Origin B

↓

IndexedDB B
```

Each origin has its own database namespace.

---

# Why Isolation Matters

Consider an authenticated banking session.

```
User

↓

bank.com

↓

Logged In

↓

Cookies

↓

Sensitive Data
```

A different website should not be able to directly access that information through browser APIs.

---

# Cross-Origin

Cross-origin simply means:

```
Different Origin

↓

Different Security Boundary
```

Cross-origin communication is **not automatically allowed**.

---

# Same-Origin

```
Origin

↓

Same Protocol

↓

Same Host

↓

Same Port

↓

Access Allowed
```

Browser APIs are generally more permissive within the same origin.

---

# Enterprise Browser Architecture

```
                  Browser

                     │

     ┌───────────────┼───────────────┐

     ▼               ▼               ▼

  HR Portal      Finance App      CRM Portal

     │               │               │

 Own Origin     Own Origin     Own Origin

     │               │               │

 Browser Isolation Enforced
```

Each application is isolated according to browser security rules.

---

# Enterprise Example

A company hosts:

```
https://hr.company.com

https://finance.company.com

https://crm.company.com
```

Each application is considered a separate origin because the hosts differ.

The browser isolates these applications unless explicit mechanisms allow controlled cross-origin communication.

---

# Browser Enforcement

```
JavaScript Request

↓

Browser

↓

Origin Check

↓

Allowed

OR

Blocked
```

The browser—not the web server—primarily enforces the Same-Origin Policy.

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| SOP blocks all cross-origin requests | No. Different resource types have different rules. |
| Subdomains always share an origin | No. Different hosts are different origins. |
| HTTPS and HTTP are the same origin | No. Different protocols create different origins. |
| SOP is enforced by servers | Browsers primarily enforce SOP for web content. |

---

# Enterprise Benefits of SOP

- Protects authenticated sessions
- Isolates browser storage
- Prevents unauthorized DOM access
- Limits exposure of sensitive application data
- Forms the foundation for other browser security mechanisms
- Reduces the impact of many client-side attacks

---

# Hands-on Lab (Conceptual)

Using your browser:

1. Open Developer Tools.
2. Visit two different websites.
3. Observe their URLs and identify protocol, host, and port.
4. Determine whether they are same-origin or cross-origin.
5. Inspect browser storage for each origin.
6. Observe that storage is maintained separately for different origins.

---

# Interview Questions

1. What is the Same-Origin Policy?
2. Why is SOP important?
3. What are the three components of an origin?
4. When are two URLs considered the same origin?
5. Does changing the protocol change the origin?
6. Does changing the port change the origin?
7. Does changing a subdomain change the origin?
8. What browser resources are protected by SOP?
9. Who enforces the Same-Origin Policy?
10. Why is browser isolation important?

---

# Best Practices

- Design applications with clear origin boundaries.
- Use HTTPS consistently.
- Understand how protocol, host, and port affect origins.
- Keep sensitive data isolated by origin.
- Do not assume subdomains share browser privileges.
- Test applications in realistic multi-origin environments.

---

# Common Mistakes

- Assuming all subdomains belong to the same origin.
- Confusing websites with browser origins.
- Assuming SOP blocks every type of cross-origin interaction.
- Forgetting that protocol differences create different origins.
- Ignoring port differences during development and testing.

---

# Key Takeaways

- The Same-Origin Policy is a fundamental browser security mechanism.
- An origin consists of **protocol + host + port**.
- Different protocols, hosts, or ports create different origins.
- SOP isolates browser resources such as the DOM and client-side storage.
- Browser-enforced origin isolation forms the foundation for many modern web security controls.

```text id="jid720"
**Next:** Part 2
```