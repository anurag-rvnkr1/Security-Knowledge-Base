# 14-CORS.md

# Part 1 — Cross-Origin Resource Sharing (CORS) Fundamentals, Browser Workflow, Origin Validation, and Enterprise Web APIs

> **"Cross-Origin Resource Sharing (CORS) is not a security feature that relaxes security—it is a controlled mechanism that allows servers to explicitly tell browsers which cross-origin requests may access their resources."**

---

# Learning Objectives

After completing this part, you will understand:

- What CORS Is
- Why CORS Exists
- Relationship Between SOP and CORS
- Browser CORS Workflow
- Origin Validation
- Cross-Origin Requests
- Simple vs Non-Simple Requests (Introduction)
- Server-Controlled Access
- Enterprise API Communication
- Common CORS Misconceptions

---

# What is CORS?

**Cross-Origin Resource Sharing (CORS)** is a browser security mechanism that allows a server to specify whether resources can be shared with web pages from different origins.

```
Browser

↓

Cross-Origin Request

↓

Server Policy

↓

Browser Decision

↓

Allow

OR

Block
```

---

# Why CORS Exists

Modern web applications often separate services.

Example:

```
Frontend

↓

https://app.example.com

↓

Backend API

↓

https://api.example.com
```

Although both belong to the same organization, they are different origins.

Without a controlled mechanism, JavaScript running on the frontend would be unable to read responses from the backend due to the Same-Origin Policy (SOP).

---

# SOP vs CORS

```
Same-Origin Policy

↓

Default Restriction

↓

Cross-Origin Read Blocked

──────────────

CORS

↓

Server Defines Policy

↓

Browser May Allow Response
```

CORS does **not** disable SOP.

Instead, it extends browser behavior in a controlled manner.

---

# Browser Security Model

```
JavaScript

↓

Cross-Origin Request

↓

Browser

↓

Server

↓

CORS Policy

↓

Browser Evaluation

↓

Response Available?

↓

Yes / No
```

The browser remains responsible for enforcing the policy.

---

# Who Controls CORS?

The **server** defines the policy.

The **browser** enforces it.

```
Server

↓

Response Headers

↓

Browser

↓

Policy Enforcement
```

Clients cannot simply "turn off" CORS in normal browsing.

---

# Origin Review

An origin consists of:

```
Protocol

+

Host

+

Port
```

Example:

```
https://api.example.com:443
```

---

# Same-Origin Example

```
https://app.example.com

↓

Request

↓

https://app.example.com

↓

Same Origin

↓

Normal Browser Access
```

---

# Cross-Origin Example

```
https://app.example.com

↓

Request

↓

https://api.example.com

↓

Cross Origin
```

The browser evaluates CORS before exposing the response to JavaScript.

---

# High-Level CORS Flow

```
JavaScript

↓

Cross-Origin Request

↓

Browser

↓

Server

↓

CORS Response Headers

↓

Browser Validation

↓

Allow Response

OR

Restrict Response
```

---

# Why Browsers Need CORS

Without CORS:

```
Website

↓

Cross-Origin Request

↓

Browser

↓

Response Hidden
```

With an appropriate CORS policy:

```
Website

↓

Cross-Origin Request

↓

Browser

↓

Server Approves

↓

Browser Exposes Response
```

---

# Browser Enforcement

Even if the server returns data:

```
Server

↓

Response

↓

Browser

↓

Policy Check

↓

JavaScript Receives Response?

↓

Yes

OR

No
```

The browser may receive the network response but refuse to expose it to the page if CORS validation fails.

---

# Enterprise Architecture

```
                 Browser

                    │

        ┌───────────┼───────────┐

        ▼           ▼           ▼

 Frontend      Authentication      API

 app.company    login.company   api.company

                    │

             Browser Applies SOP

                    │

          CORS Enables Approved Access
```

---

# Why APIs Use CORS

Modern APIs often serve:

- Web applications
- Mobile applications
- Partner portals
- Administrative dashboards
- Customer portals

Controlled cross-origin access allows these systems to communicate securely through browsers.

---

# Request Flow

```
User

↓

Frontend

↓

JavaScript

↓

Browser

↓

Cross-Origin API

↓

Server

↓

CORS Policy

↓

Browser Decision
```

---

# Server Response

The server includes CORS-related HTTP response headers indicating its policy.

Conceptually:

```
Server

↓

Response

↓

CORS Headers

↓

Browser Evaluation
```

The browser checks these headers before exposing the response.

---

# Browser Decision Tree

```
Cross-Origin Request

↓

Receive Response

↓

CORS Policy Valid?

↓

Yes

↓

Expose Response

──────────────

No

↓

Block JavaScript Access
```

---

# Important Principle

CORS protects **browser-based JavaScript**.

It is **not** a general server-side access control mechanism.

For example:

```
Browser

↓

CORS Enforced

──────────────

Server-to-Server Request

↓

CORS Not Applicable
```

Servers must still perform authentication and authorization.

---

# Common CORS Misconceptions

| Myth | Reality |
|------|---------|
| CORS replaces authentication | No |
| CORS protects APIs from attackers | No |
| CORS disables SOP | No |
| Servers enforce CORS for browsers | Browsers enforce the policy using server-provided headers |
| CORS is needed for every HTTP request | No, primarily for browser cross-origin requests |

---

# Enterprise Example

A company hosts:

```
https://portal.company.com

↓

Employee Dashboard

──────────────

https://api.company.com

↓

REST API
```

The portal's JavaScript sends requests to the API.

The API explicitly declares which browser origins are permitted to read responses.

The browser validates that declaration before exposing the response to JavaScript.

---

# CORS Request Lifecycle

```
Page Loaded

↓

JavaScript Executes

↓

Cross-Origin Request

↓

Browser Sends Request

↓

Server Responds

↓

Browser Validates CORS

↓

Expose Response

OR

Restrict Response
```

---

# Security Goals of CORS

CORS aims to:

- Maintain browser isolation
- Permit approved cross-origin communication
- Protect users from unauthorized cross-origin data access
- Support modern distributed web applications
- Preserve the Same-Origin Policy as the default security model

---

# Hands-on Lab (Conceptual)

Using your browser:

1. Open Developer Tools → Network.
2. Visit a web application that communicates with an API hosted on another origin.
3. Observe requests made to the API.
4. Compare the frontend origin with the API origin.
5. Inspect the response headers conceptually and identify CORS-related information.
6. Observe how the browser determines whether the response is available to JavaScript.

---

# Interview Questions

1. What is CORS?
2. Why was CORS introduced?
3. How does CORS relate to the Same-Origin Policy?
4. Who defines the CORS policy?
5. Who enforces the CORS policy?
6. Does CORS replace authentication?
7. Does CORS protect server-to-server requests?
8. Why do modern APIs commonly require CORS?
9. What happens when CORS validation fails?
10. Why is CORS considered a browser security mechanism?

---

# Best Practices

- Keep the Same-Origin Policy as the default security boundary.
- Allow only trusted origins where appropriate.
- Continue enforcing authentication and authorization on the server.
- Document cross-origin communication within your architecture.
- Review CORS policies during security assessments.
- Test browser behavior in production-like environments.

---

# Common Mistakes

- Assuming CORS is an authentication mechanism.
- Believing CORS protects APIs from all attackers.
- Assuming disabling CORS improves security.
- Confusing browser security with server-side authorization.
- Forgetting that browsers—not servers—ultimately enforce CORS behavior.

---

# Key Takeaways

- CORS is a controlled extension to the Same-Origin Policy.
- Servers declare which cross-origin browser requests may access resources.
- Browsers enforce CORS using server-provided response headers.
- CORS applies primarily to browser-based cross-origin JavaScript requests.
- Authentication, authorization, and business logic remain server-side responsibilities.

```text id="jid720"
**Next:** Part 2
```