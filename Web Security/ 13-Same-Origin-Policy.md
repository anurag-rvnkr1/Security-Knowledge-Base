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

# 13-Same-Origin-Policy.md

# Part 2 — SOP Enforcement, Cross-Origin Resource Access, Browser Behavior, Cross-Origin Communication, and Enterprise Web Architecture

> **"The Same-Origin Policy does not prohibit all cross-origin interactions. Instead, browsers carefully control *what* can be shared, *how* it can be shared, and *under which security rules* it may occur."**

---

# Learning Objectives

After completing this part, you will understand:

- How SOP is Enforced
- Browser Resource Isolation
- Cross-Origin Requests
- Cross-Origin Reads
- Cross-Origin Writes
- Cross-Origin Embedding
- Cross-Origin Communication
- Browser Security Decisions
- Enterprise Multi-Origin Applications
- Modern Browser Architecture

---

# SOP Enforcement Model

Whenever JavaScript attempts to access a resource, the browser evaluates the request.

```
JavaScript

↓

Resource Request

↓

Origin Comparison

↓

Same Origin?

↓

Yes

↓

Allow

──────────────

No

↓

Apply Browser Security Rules
```

---

# Browser Security Decisions

The browser evaluates several factors before granting access.

```
Request

↓

Origin

↓

Resource Type

↓

Security Policy

↓

Decision
```

Different resource types follow different browser rules.

---

# Three Types of Cross-Origin Activity

Cross-origin interactions can be broadly grouped into:

```
Cross-Origin Activity

│

├── Reads

├── Writes

└── Embedding
```

Each category is treated differently by browsers.

---

# Cross-Origin Reads

A cross-origin read attempts to obtain data from another origin.

Conceptually:

```
Website A

↓

Read Data

↓

Website B
```

The browser generally restricts JavaScript from directly reading sensitive responses across origins unless explicit mechanisms permit it.

---

# Cross-Origin Writes

Examples include:

- Submitting a form
- Navigating to another website
- Redirecting the browser

Conceptually:

```
Website A

↓

Send Request

↓

Website B
```

Cross-origin writes have historically been more common on the web than unrestricted cross-origin reads.

---

# Cross-Origin Embedding

Browsers allow certain resources to be embedded.

Examples include:

- Images
- Stylesheets
- Fonts
- Audio
- Video

Conceptually:

```
Website A

↓

Embed Resource

↓

Website B
```

Embedding does **not** necessarily grant JavaScript access to the embedded content.

---

# Browser Isolation

Even when resources are embedded:

```
Embedded Resource

↓

Displayed

↓

JavaScript Access?

↓

Restricted
```

Rendering content is different from allowing programmatic access.

---

# Reading vs Displaying

These are different operations.

```
Display Image

↓

Allowed

──────────────

Read Image Data

↓

Browser Rules Apply
```

The browser distinguishes between displaying content and exposing its underlying data to scripts.

---

# Navigation Between Origins

Users regularly navigate between websites.

```
Website A

↓

User Clicks Link

↓

Website B
```

Navigation itself is a normal browser behavior and is distinct from unrestricted cross-origin scripting.

---

# Forms and Cross-Origin Submission

Traditional HTML forms can submit data to another origin.

```
Form

↓

Submit

↓

Different Website
```

However, this does not automatically allow the originating page to read the response.

---

# Iframes

A webpage may embed another webpage.

```
Website A

↓

Iframe

↓

Website B
```

Although the embedded page is visible, browser isolation still applies between different origins.

---

# Cross-Origin Iframe Access

```
Parent Page

↓

Access Iframe DOM

↓

Origin Check

↓

Blocked (if different origin)
```

Direct DOM interaction between different origins is generally restricted.

---

# Same-Origin Iframes

If both pages share the same origin:

```
Parent

↓

Iframe

↓

Same Origin

↓

DOM Access Allowed
```

The browser treats them as part of the same security boundary.

---

# JavaScript Execution

Scripts execute within their own origin.

```
Origin A

↓

JavaScript

↓

Origin A Resources
```

Scripts do not automatically gain access to resources belonging to other origins.

---

# Storage Separation

Each origin maintains independent storage.

```
Origin A

│

├── Cookies

├── Local Storage

├── Session Storage

└── IndexedDB

──────────────

Origin B

↓

Separate Storage
```

This isolation prevents accidental data sharing.

---

# Cookie Isolation

Conceptually:

```
shop.example

↓

Cookies

↓

shop.example

──────────────

news.example

↓

No Automatic Access
```

Cookie behavior also depends on attributes such as `Domain`, `Secure`, `HttpOnly`, and `SameSite`.

---

# Service Isolation

Modern browsers isolate many services per origin.

```
Origin

│

├── Storage

├── JavaScript

├── IndexedDB

├── Cache

└── Service Worker
```

Origin isolation improves security and reliability.

---

# Enterprise Multi-Origin Applications

Large organizations often separate applications.

```
portal.company.com

finance.company.com

support.company.com

mail.company.com
```

Each application has its own origin and browser security boundary.

---

# Enterprise Example

A company hosts:

```
https://portal.company.com

↓

Employee Dashboard

──────────────

https://finance.company.com

↓

Payroll System
```

Although both belong to the same organization, the browser considers them different origins because the hosts differ.

---

# Browser Origin Matrix

| Resource | Same Origin | Cross Origin |
|----------|-------------|--------------|
| DOM Access | Allowed | Restricted |
| Local Storage | Allowed | Isolated |
| Session Storage | Allowed | Isolated |
| IndexedDB | Allowed | Isolated |
| JavaScript Objects | Allowed | Restricted |

Actual behavior depends on browser security policies and the specific APIs involved.

---

# Why SOP Uses Origins

Origins provide a simple and consistent security boundary.

```
Protocol

+

Host

+

Port

↓

Origin

↓

Security Boundary
```

This model allows browsers to isolate unrelated websites.

---

# Browser Process Isolation (Conceptual)

Modern browsers increasingly isolate websites internally.

```
Browser

│

├── Process A

│      ↓

│   Origin A

├── Process B

│      ↓

│   Origin B

└── Process C

       ↓

    Origin C
```

Process isolation complements the Same-Origin Policy by reducing the impact of browser vulnerabilities.

---

# Enterprise Browser Architecture

```
                 Browser

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

 HR Portal     CRM Portal    Finance Portal

      │             │             │

  Origin A      Origin B      Origin C

      │             │             │

 Independent Browser Security Boundaries
```

---

# Browser Decision Flow

```
JavaScript

↓

Cross-Origin Access

↓

Browser

↓

Origin Match?

↓

Yes

↓

Allow

──────────────

No

↓

Evaluate Browser Rules

↓

Permit Limited Interaction

OR

Restrict Access
```

---

# Common Misunderstandings

| Misunderstanding | Correct Explanation |
|------------------|---------------------|
| SOP blocks every cross-origin request | Different resource types have different browser behaviors. |
| Displaying a resource means JavaScript can read it | Rendering and programmatic access are separate concepts. |
| Iframes bypass SOP | Different-origin iframes remain isolated. |
| Same company means same origin | Browser decisions depend on protocol, host, and port—not ownership. |

---

# Hands-on Lab (Conceptual)

Using two different websites:

1. Open Developer Tools.
2. Compare the origins of both sites.
3. Inspect Local Storage for each origin.
4. Observe that browser storage is separated.
5. Embed an image from another website (where permitted) and observe that displaying it does not automatically provide script access to its underlying data.
6. Compare same-origin and cross-origin iframe behavior conceptually.

---

# Interview Questions

1. How does the browser enforce the Same-Origin Policy?
2. What is the difference between cross-origin reads and writes?
3. Why are embedded resources treated differently from DOM access?
4. Can two subdomains directly access each other's DOM?
5. Why is browser storage isolated by origin?
6. Does embedding a webpage bypass SOP?
7. Why are forms historically able to submit across origins?
8. What is the difference between displaying and reading a resource?
9. Why do enterprise applications often use multiple origins?
10. How does browser process isolation complement SOP?

---

# Best Practices

- Design applications with clear origin boundaries.
- Keep sensitive applications isolated.
- Understand the distinction between navigation, embedding, and script access.
- Avoid assuming organizational ownership affects browser origin checks.
- Test applications in multi-origin deployment environments.
- Review browser security behavior during application design.

---

# Common Mistakes

- Assuming embedded resources can always be accessed by JavaScript.
- Confusing navigation with unrestricted data access.
- Assuming iframes bypass browser security.
- Treating different subdomains as a single browser origin.
- Forgetting that browser storage is isolated by origin.

---

# Key Takeaways

- SOP evaluates requests based on origin and resource type.
- Cross-origin reads, writes, and embedding are handled differently by browsers.
- Displaying external resources does not automatically grant JavaScript access to their contents.
- Browser storage, DOM objects, and JavaScript execution remain isolated across different origins.
- Modern enterprise applications rely on SOP as a core browser security boundary.

```text id="jid720"
**Next:** Part 3
```