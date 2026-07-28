# 47-Server-Side-Template-Injection.md

# Part 1 — Introduction to Server-Side Template Injection (SSTI), Template Engines, Rendering Pipelines, and Secure Template Design

> **"Server-Side Template Injection (SSTI) is a server-side application security issue that can arise when untrusted input influences template rendering without appropriate validation or separation. Secure applications separate data from template logic, use trusted templates, and enforce strict rendering policies."**

---

# Learning Objectives

After completing this part, you will understand:

- What Server-Side Template Injection (SSTI) Is
- Why Template Engines Exist
- Server-Side Rendering
- Template Rendering Lifecycle
- Template Engines
- Data vs Template Logic
- Trust Boundaries
- Enterprise Rendering Architecture
- Secure Template Design Principles

---

# What is Server-Side Template Injection?

Server-Side Template Injection (SSTI) is a **server-side template rendering issue** that occurs when application logic allows untrusted input to influence how server-side templates are interpreted.

Conceptually:

```
Client

↓

Application

↓

Template Engine

↓

Rendered Output
```

Secure applications ensure that user-supplied data is treated as **data**, not as template instructions.

---

# Why Template Engines Exist

Template engines help developers generate dynamic content efficiently.

Typical use cases include:

- HTML pages
- Email templates
- Reports
- Documents
- Notifications
- Dashboards
- Administrative portals

```
Application Data

↓

Template Engine

↓

Rendered Content
```

Templates separate presentation from application logic.

---

# What is a Template?

A template is a predefined structure used to generate dynamic output.

Conceptually:

```
Template

+

Application Data

↓

Rendered Output
```

The template defines presentation while application data supplies the values.

---

# Server-Side Rendering

In server-side rendering, the server prepares the final content before sending it to the client.

```
Client Request

↓

Application

↓

Template Engine

↓

HTML Response

↓

Browser
```

The browser receives already-rendered content.

---

# Rendering Lifecycle

```
Request

↓

Business Logic

↓

Retrieve Data

↓

Render Template

↓

Generate Response

↓

Client
```

Rendering should always occur using trusted templates.

---

# Template Engine Overview

Template engines provide features such as:

```
Template Engine

│

├── Variable Substitution

├── Conditional Rendering

├── Loops

├── Layouts

├── Reusable Components

├── Escaping

└── Formatting
```

Applications should use these features within well-defined security boundaries.

---

# Data vs Template Logic

A secure design separates template logic from user-controlled data.

```
Trusted Template

        +

Validated Data

↓

Template Engine

↓

Rendered Output
```

The template itself should remain under application control.

---

# Trust Boundary

```
External Input

──────── Trust Boundary ────────

Application

↓

Template Rendering

↓

Response
```

External input should never become trusted template code.

---

# Sources of Rendering Data

```
Application Data

│

├── Form Input

├── API Requests

├── Database Records

├── User Profiles

├── Configuration

├── Internal Services

└── Business Logic
```

Every external source should be validated before being used during rendering.

---

# Secure Rendering Workflow

```
Incoming Request

↓

Validation

↓

Business Logic

↓

Trusted Template

+

Validated Data

↓

Rendered Response
```

Trusted templates and validated data should remain separate throughout processing.

---

# Enterprise Rendering Architecture

```
Client

↓

Load Balancer

↓

Web Server

↓

Application

↓

Template Engine

↓

Rendered Response
```

Rendering should occur only after application validation and authorization.

---

# Defense in Depth

Template security should complement broader application security controls.

```
Input Validation

↓

Authorization

↓

Business Logic

↓

Template Validation

↓

Output Encoding

↓

Monitoring
```

Multiple layers reduce dependence on any single safeguard.

---

# Secure Template Design Principles

```
Secure Template Design

│

├── Trusted Templates

├── Data Separation

├── Input Validation

├── Output Encoding

├── Least Privilege

├── Logging

├── Monitoring

└── Continuous Review
```

Templates should remain predictable and centrally managed.

---

# Enterprise Example

A multinational e-commerce platform renders order confirmations, invoices, and customer dashboards.

```
Customer

↓

Application

↓

Business Logic

↓

Trusted Template

↓

Rendered HTML
```

Customer information is validated before rendering, while templates remain centrally managed through version control and change approval processes.

---

# Components Involved

```
Rendering Pipeline

│

├── Client

├── Web Server

├── Application

├── Template Engine

├── Business Logic

├── Database

└── Monitoring
```

Every component contributes to secure rendering.

---

# Secure Rendering Goals

Applications should provide:

- Trusted templates
- Validated data
- Predictable rendering
- Consistent output
- Secure defaults
- Operational visibility

---

# Hands-on Lab (Conceptual)

1. Draw the rendering pipeline of a web application.
2. Identify where templates are stored.
3. Mark trust boundaries between user input and rendering.
4. Document how application data reaches the template engine.
5. Review where validation occurs before rendering.

> Perform all activities only in environments where you have explicit authorization. Focus on secure architecture, rendering workflows, and defensive application design.

---

# Interview Questions

1. What is Server-Side Template Injection?
2. Why do applications use template engines?
3. What is server-side rendering?
4. Why should templates remain trusted?
5. What is the difference between template logic and application data?
6. What is a trust boundary?
7. Why is validation important before rendering?
8. How does defense in depth improve template security?
9. Which application components participate in rendering?
10. Why should templates be centrally managed?

---

# Best Practices

- Treat all external rendering data as untrusted.
- Keep templates under application control.
- Separate data from template logic.
- Validate data before rendering.
- Maintain version-controlled templates.
- Review rendering architecture regularly.
- Monitor rendering-related events.
- Apply secure coding standards consistently.

---

# Common Mistakes

- Mixing user-controlled data with template logic.
- Allowing templates to be modified through untrusted input.
- Skipping validation before rendering.
- Inconsistent rendering behavior across applications.
- Poor documentation of rendering workflows.
- Failing to review template architecture during security assessments.

---

# Key Takeaways

- SSTI is fundamentally a template rendering and trust-boundary issue.
- Templates define presentation, while application data supplies values.
- Trusted templates should remain separate from untrusted input.
- Secure rendering relies on validation, centralized template management, and predictable workflows.
- Enterprise governance, monitoring, and standardized rendering practices improve application resilience.

```text id="rrks28"
**Next:** Part 2
```