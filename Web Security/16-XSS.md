# 16-Cross-Site-Scripting-(XSS).md

# Part 1 — Cross-Site Scripting (XSS) Fundamentals, Browser Execution Model, Attack Types, and Enterprise Security

> **"Cross-Site Scripting (XSS) occurs when an application allows untrusted data to become executable content in a user's browser. Instead of attacking the server directly, XSS targets the trust between the browser and the web application."**

---

# Learning Objectives

After completing this part, you will understand:

- What Cross-Site Scripting (XSS) Is
- Why XSS Exists
- Browser Execution Model
- Client-Side Trust
- Types of XSS
- XSS Attack Flow
- Browser Perspective
- Enterprise Impact
- Real-World Examples
- Common Misconceptions

---

# What is Cross-Site Scripting (XSS)?

**Cross-Site Scripting (XSS)** is a vulnerability in which untrusted input is interpreted as executable code by a user's browser.

```
User Input

↓

Application

↓

Unsafe Output

↓

Browser Executes

↓

Unexpected Script Runs
```

Instead of treating the data as plain text, the browser interprets it as active content.

---

# Why XSS Exists

Browsers are designed to execute JavaScript contained in web pages.

```
HTML

↓

Browser

↓

Render Page

↓

JavaScript

↓

Execute Script
```

If an application places untrusted input into the page without appropriate protection, the browser cannot always distinguish between legitimate application code and injected content.

---

# Browser Trust Model

```
Application

↓

HTML Response

↓

Browser

↓

Parse HTML

↓

Execute Scripts

↓

Render Page
```

The browser assumes that the content delivered by the trusted application is intended to execute.

---

# High-Level XSS Flow

```
Attacker Input

↓

Application

↓

Stores or Reflects Input

↓

Victim Opens Page

↓

Browser Executes Script
```

The vulnerable application unintentionally delivers attacker-controlled content.

---

# XSS is a Client-Side Attack

Unlike many server-side vulnerabilities:

```
Application

↓

Sends Response

↓

Browser

↓

Script Executes
```

The code executes inside the victim's browser.

---

# Why It Is Called "Cross-Site" Scripting

Historically, the term referred to scripts executing within the trusted context of another website.

Today, **XSS** is the widely accepted name, even though many attacks occur within a single web application.

---

# Browser Execution Context

```
Web Page

│

├── HTML

├── CSS

├── JavaScript

└── User Data
```

Improper handling of user data can allow it to become executable JavaScript.

---

# Trusted vs Untrusted Data

```
Trusted Application Code

↓

Safe Execution

──────────────

Untrusted User Input

↓

Should Be Treated As Data

↓

Not Code
```

A secure application keeps data separate from executable code.

---

# Types of XSS

The three major categories are:

```
Cross-Site Scripting

│

├── Reflected XSS

├── Stored XSS

└── DOM-Based XSS
```

Each differs in how malicious input reaches the victim.

---

# Reflected XSS (Introduction)

```
Victim Request

↓

Application

↓

Response Immediately Includes Input

↓

Browser Executes
```

The payload is reflected directly in the response.

---

# Stored XSS (Introduction)

```
Attacker Input

↓

Stored

↓

Database

↓

Victim Opens Page

↓

Browser Executes
```

The payload persists until viewed by other users.

---

# DOM-Based XSS (Introduction)

```
Browser

↓

JavaScript

↓

DOM Modification

↓

Unsafe Processing

↓

Script Executes
```

The vulnerability exists primarily within client-side JavaScript.

Detailed coverage will follow in later parts.

---

# Why XSS is Dangerous

Potential impacts include:

- Session theft
- Account takeover
- Unauthorized actions
- User impersonation
- Defacement
- Credential theft
- Phishing within trusted pages
- Client-side malware delivery
- Data exposure

The actual impact depends on application design and browser protections.

---

# Browser Perspective

```
Receive HTML

↓

Parse Document

↓

Execute Allowed Scripts

↓

Display Page
```

If malicious script becomes part of the document, the browser may execute it within the application's origin.

---

# Same-Origin Policy and XSS

```
Trusted Website

↓

Injected Script

↓

Runs As Trusted Website
```

The Same-Origin Policy does **not** protect against XSS occurring within the same trusted origin.

---

# Enterprise Example

```
Customer Portal

↓

User Comment

↓

Application Displays Comment

↓

Browser Executes Unexpected Script
```

Improper output handling could affect every user viewing the page.

---

# Typical Targets

Applications accepting user-generated content are common candidates for review.

Examples:

- Comments
- Reviews
- Chat systems
- Forums
- Ticketing systems
- User profiles
- Administrative dashboards
- Messaging systems

Any feature displaying user-controlled content should be evaluated.

---

# Enterprise Risk

```
Authenticated User

↓

Visits Page

↓

Browser Executes Script

↓

Application Trust Abused
```

Potential consequences include:

- Loss of confidentiality
- Session compromise
- Unauthorized actions
- Business disruption
- Compliance issues

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| XSS attacks the server | XSS primarily executes in the browser |
| JavaScript itself is insecure | The issue is unsafe handling of untrusted input |
| HTTPS prevents XSS | HTTPS protects data in transit, not application output |
| Authentication prevents XSS | Authenticated users may still become victims |

---

# Browser Security Layers

```
HTTPS

↓

Authentication

↓

Authorization

↓

Same-Origin Policy

↓

Content Security

↓

Secure Coding
```

XSS prevention depends heavily on secure application development.

---

# Root Cause

Most XSS vulnerabilities arise when:

```
Untrusted Input

↓

Inserted Into Page

↓

Without Proper Protection

↓

Browser Executes
```

The core issue is improper handling of user-controlled data.

---

# Secure Design Principle

```
User Input

↓

Validate

↓

Store

↓

Encode Before Output

↓

Browser Displays As Data
```

Treat all external input as untrusted unless proven otherwise.

---

# Hands-on Lab (Conceptual)

1. Identify application features accepting user input.
2. Map where the input is later displayed.
3. Determine whether the content appears in HTML, JavaScript, URLs, or attributes.
4. Review how the application distinguishes data from executable content.
5. Document areas requiring secure output handling.

> Perform testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is Cross-Site Scripting (XSS)?
2. Why does XSS occur?
3. Why is XSS considered a client-side vulnerability?
4. What are the three major categories of XSS?
5. What is the difference between trusted and untrusted input?
6. Why doesn't HTTPS prevent XSS?
7. Why doesn't the Same-Origin Policy stop XSS within the same application?
8. What kinds of applications are commonly exposed to XSS risk?
9. Why should all user input be treated as untrusted?
10. What is the primary root cause of XSS vulnerabilities?

---

# Best Practices

- Treat all external input as untrusted.
- Separate executable code from user-controlled data.
- Review every location where user input is rendered.
- Follow secure coding principles throughout the application.
- Perform regular code reviews and security assessments.
- Educate developers about browser execution behavior.

---

# Common Mistakes

- Trusting user input by default.
- Assuming authentication prevents XSS.
- Believing HTTPS eliminates XSS.
- Mixing application code with user-generated content.
- Ignoring client-side rendering during security reviews.

---

# Key Takeaways

- XSS occurs when untrusted input becomes executable content in a browser.
- The browser executes malicious code because it trusts the application's response.
- XSS is primarily a client-side vulnerability.
- The three primary categories are Reflected, Stored, and DOM-Based XSS.
- Secure handling of user input and output is the foundation of XSS prevention.

# 16-Cross-Site-Scripting-(XSS).md

# Part 2 — Reflected XSS, Stored XSS, DOM-Based XSS, Browser Parsing Contexts, and Enterprise Attack Surface

> **"Not every XSS vulnerability is created the same way. The difference lies in how untrusted data reaches the browser and where the browser interprets it as executable content."**

---

# Learning Objectives

After completing this part, you will understand:

- Reflected XSS
- Stored XSS
- DOM-Based XSS
- Browser Parsing Contexts
- Server-Side vs Client-Side XSS
- XSS Sources and Sinks
- Common Injection Locations
- Enterprise Attack Surface
- Secure Design Principles
- Common Misconceptions

---

# XSS Classification

Cross-Site Scripting is generally divided into three primary categories.

```
Cross-Site Scripting

│

├── Reflected XSS

├── Stored XSS

└── DOM-Based XSS
```

Each category follows a different execution path.

---

# Reflected XSS

Reflected XSS occurs when untrusted input is immediately included in the application's response.

```
User Request

↓

Application

↓

Input Reflected

↓

Browser

↓

Script Executes
```

The malicious input is **not** permanently stored by the application.

---

# Reflected XSS Workflow

```
Attacker

↓

Crafted Request

↓

Victim Opens Request

↓

Application Reflects Input

↓

Browser Executes
```

Execution depends on the victim accessing the crafted request.

---

# Characteristics of Reflected XSS

- Input is reflected immediately.
- No database storage is required.
- Usually affects a single request.
- Often depends on user interaction.

---

# Stored XSS

Stored XSS occurs when untrusted input is saved by the application and later displayed to users.

```
Attacker Input

↓

Application

↓

Database

↓

Victim Opens Page

↓

Browser Executes
```

The payload persists until it is removed or sanitized.

---

# Stored XSS Workflow

```
Attacker

↓

Submit Content

↓

Application Stores

↓

Another User Visits Page

↓

Browser Executes
```

Stored XSS can affect many users over time.

---

# Characteristics of Stored XSS

- Payload is persistent.
- Often impacts multiple users.
- Frequently found in collaborative applications.
- Typically has greater business impact than reflected XSS.

---

# DOM-Based XSS

DOM-Based XSS primarily occurs within client-side JavaScript.

```
Browser

↓

JavaScript

↓

Reads Data

↓

Updates DOM Unsafely

↓

Script Executes
```

The vulnerable behavior happens inside the browser rather than during server-side response generation.

---

# DOM-Based Workflow

```
Browser Loads Page

↓

JavaScript Executes

↓

Reads User-Controlled Data

↓

Unsafe DOM Update

↓

Unexpected Script Execution
```

---

# Server vs Browser

```
Reflected XSS

↓

Server Response

↓

Browser Executes

──────────────

Stored XSS

↓

Server Storage

↓

Browser Executes

──────────────

DOM XSS

↓

Browser JavaScript

↓

Browser Executes
```

The execution environment is always the browser, but the source differs.

---

# XSS Sources

A **source** is where untrusted data enters the application.

Conceptually:

```
User Input

↓

URL

↓

Form

↓

Search Box

↓

Cookie

↓

Browser Storage

↓

Source
```

Any external input should be considered untrusted.

---

# XSS Sinks

A **sink** is a location where the application places data into the page.

Conceptually:

```
Application

↓

HTML

↓

Attribute

↓

JavaScript

↓

DOM

↓

Sink
```

Unsafe use of sinks can lead to XSS.

---

# Data Flow

```
Source

↓

Application Processing

↓

Sink

↓

Browser Parsing

↓

Execution?
```

Secure applications ensure that data remains data throughout this process.

---

# Browser Parsing Contexts

Browsers interpret content differently depending on where it appears.

```
HTML Document

│

├── HTML Context

├── HTML Attribute

├── JavaScript

├── CSS

└── URL
```

Each context has different security considerations.

---

# HTML Context

```
Application Output

↓

HTML

↓

Browser Parses

↓

Render Page
```

User input displayed as plain text should remain non-executable.

---

# Attribute Context

```
HTML Element

↓

Attribute

↓

Browser Parses

↓

Different Interpretation
```

Security requirements vary depending on the specific attribute.

---

# JavaScript Context

```
Application

↓

JavaScript

↓

Browser Executes
```

Embedding untrusted data directly into executable JavaScript is especially dangerous.

---

# URL Context

```
Application

↓

URL

↓

Browser Navigation

↓

Processing
```

Applications should carefully validate and safely handle user-controlled URLs.

---

# CSS Context

```
Application

↓

Style Information

↓

Browser

↓

Render
```

Although less common, CSS-related injection scenarios should also be considered during secure design.

---

# Enterprise Attack Surface

Typical locations where user input is displayed include:

- Search results
- User profiles
- Product reviews
- Support tickets
- Comments
- Chat systems
- Administrative dashboards
- Knowledge bases

Each display location represents a potential output context.

---

# Enterprise Example

```
Customer Support Portal

↓

Support Ticket

↓

Database

↓

Support Engineer Opens Ticket

↓

Browser Displays Content
```

If output is not safely handled, injected content could affect anyone viewing the ticket.

---

# Browser Parsing Pipeline

```
HTML Response

↓

Parser

↓

DOM

↓

JavaScript Engine

↓

Render Engine

↓

Displayed Page
```

The browser processes different content types through specialized components.

---

# Secure Data Flow

```
User Input

↓

Validation

↓

Storage

↓

Context-Appropriate Output Encoding

↓

Browser Displays Data
```

Maintaining this separation prevents data from becoming executable content.

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| Stored XSS only affects administrators | Any user viewing the content may be affected |
| DOM XSS is a server vulnerability | It primarily occurs in client-side JavaScript |
| Reflected XSS always requires a database | No, reflected input is usually not stored |
| Every user input field automatically causes XSS | Risk depends on how the data is processed and rendered |

---

# Comparison

| Feature | Reflected | Stored | DOM-Based |
|----------|-----------|---------|-----------|
| Data Stored | No | Yes | Usually No |
| Trigger | Single Request | Future Page Views | Client-Side JavaScript |
| Persistence | Temporary | Persistent | Depends on Client Logic |
| Primary Processing | Server | Server | Browser |

---

# Hands-on Lab (Conceptual)

1. Identify every place where users can submit data.
2. Identify every location where that data is displayed.
3. Classify each display location as:
   - HTML
   - Attribute
   - JavaScript
   - URL
   - CSS
4. Draw a data-flow diagram from source to sink.
5. Mark which locations require context-specific output handling.

> Perform testing only in systems where you have explicit authorization.

---

# Interview Questions

1. What is Reflected XSS?
2. What is Stored XSS?
3. What is DOM-Based XSS?
4. Which XSS type is usually persistent?
5. What is the difference between a source and a sink?
6. Why are browser parsing contexts important?
7. Why is DOM-Based XSS considered client-side?
8. Which XSS category typically has the widest impact?
9. Why should output context be considered during development?
10. What is the secure flow from user input to browser output?

---

# Best Practices

- Identify all user-controlled data sources.
- Understand every browser parsing context.
- Keep executable code separate from user data.
- Review both server-side and client-side rendering.
- Apply context-appropriate output encoding.
- Perform regular security reviews of display functionality.
- Document all trusted and untrusted data flows.

---

# Common Mistakes

- Treating every output context the same.
- Focusing only on server-side rendering while ignoring client-side JavaScript.
- Assuming stored content is automatically safe.
- Forgetting that browser parsing differs between HTML, JavaScript, CSS, attributes, and URLs.
- Mixing user input directly with executable code.

---

# Key Takeaways

- XSS consists of three primary categories: Reflected, Stored, and DOM-Based.
- The execution always occurs in the browser, but the source of the vulnerability differs.
- Sources introduce untrusted data, while sinks render or process it.
- Browser parsing context determines how data is interpreted.
- Secure applications track untrusted data from input through output and apply context-specific protections.

```text id="jid720"
**Next:** Part 3
```