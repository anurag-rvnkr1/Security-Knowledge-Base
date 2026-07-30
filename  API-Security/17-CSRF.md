# 17 - Cross-Site Request Forgery (CSRF) in APIs

# Introduction

Cross-Site Request Forgery (CSRF) is a web security attack in which a victim's browser is tricked into sending unintended authenticated requests to a trusted application.

Unlike many attacks that exploit software vulnerabilities, CSRF exploits the trust a web application places in a user's authenticated browser session.

CSRF primarily affects applications that rely on:

- Session cookies
- Browser authentication
- Automatic credential transmission

Modern APIs using stateless authentication (such as properly implemented Bearer Tokens in Authorization headers) are generally less susceptible, but CSRF remains an important risk for browser-based APIs.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand CSRF fundamentals.
- Learn how browsers automatically send credentials.
- Understand session cookies.
- Identify CSRF attack prerequisites.
- Learn common CSRF attack techniques.
- Understand modern CSRF defenses.
- Learn SameSite cookie protection.
- Implement anti-CSRF tokens.
- Assess CSRF risks in REST and GraphQL APIs.

---

# What is CSRF?

A CSRF attack forces a victim's authenticated browser to perform actions without the user's intention.

```
Attacker Website

        │

Victim Visits

        │

Malicious Request

        │

Victim Browser

        │

Automatically Sends Cookies

        │

Trusted API

        ▼

Action Performed
```

---

# Why CSRF Works

Browsers automatically attach certain credentials to requests.

Examples include

- Session cookies
- HTTP authentication
- Client certificates

If the server cannot distinguish legitimate user actions from forged requests, the attack succeeds.

---

# Browser Trust Model

```
User

 │

Logs In

 │

Receives Session Cookie

 │

Visits Malicious Website

 │

Browser Automatically Sends Cookie

 ▼

Authenticated Request
```

The browser behaves correctly according to web standards—the server must validate the legitimacy of the request.

---

# CSRF Attack Prerequisites

A successful CSRF attack typically requires:

- Victim is authenticated.
- Browser automatically sends credentials.
- Attacker can cause the browser to issue a request.
- Target endpoint lacks CSRF protection.
- Request performs a state-changing action.

---

# Typical CSRF Targets

Examples

- Password changes
- Email changes
- Money transfers
- Profile updates
- Account deletion
- Administrative actions
- Purchase requests

---

# CSRF Attack Flow

```
Victim

    │

Logs Into Bank

    │

Session Cookie Stored

    │

Visits Malicious Website

    │

Hidden Request Generated

    │

Browser Sends Cookie

    │

Bank API

    ▼

Transaction Executes
```

---

# Example Scenario

```
Victim

↓

Authenticated Session

↓

Attacker Email

↓

Clicks Malicious Link

↓

Hidden Form Submitted

↓

Sensitive Action
```

---

# Why APIs Can Be Vulnerable

REST APIs are vulnerable when:

- Browser clients use cookies.
- Session authentication is used.
- State-changing operations lack CSRF validation.

APIs using Authorization headers with manually supplied Bearer Tokens are generally not vulnerable to classic CSRF because browsers do not automatically attach these headers across origins.

---

# CSRF vs XSS

| CSRF | XSS |
|------|-----|
| Exploits user trust | Executes attacker-controlled scripts |
| Requires authenticated victim | May not require authentication |
| Browser sends credentials automatically | JavaScript executes in trusted origin |
| Targets state-changing actions | Can steal data, sessions, or modify pages |

---

# CSRF vs CORS

| CSRF | CORS |
|------|------|
| Request forgery attack | Browser security mechanism |
| Exploits authenticated sessions | Controls cross-origin access |
| Server-side protection required | Browser-enforced policy |

CORS does **not** prevent CSRF attacks by itself.

---

# Session Cookies

```
User Login

      │

Server

      │

Set-Cookie

      ▼

Browser Storage

      │

Future Requests

      ▼

Cookie Automatically Included
```

This automatic behavior is the core reason CSRF attacks are possible.

---

# Stateful Authentication

```
Browser

     │

Session Cookie

     ▼

Server Session

     ▼

Authenticated User
```

CSRF primarily affects stateful authentication models.

---

# Stateless Authentication

```
Browser

     │

Authorization Header

     ▼

JWT Validation

     ▼

API
```

Since browsers do not automatically attach Authorization headers to cross-origin requests, stateless authentication significantly reduces classic CSRF risk.

---

# Safe vs Unsafe HTTP Methods

Safe methods

- GET
- HEAD
- OPTIONS

Unsafe methods

- POST
- PUT
- PATCH
- DELETE

CSRF protection should focus on state-changing operations.

---

# Why GET Should Not Modify State

Incorrect

```
GET

/deleteUser

```

Correct

```
DELETE

/users/{id}
```

GET requests should remain idempotent and free of side effects.

---

# HTML Form CSRF

An attacker-controlled page may automatically submit a hidden form.

```
Victim Browser

        │

Hidden Form

        │

POST Request

        │

Cookies Attached

        ▼

Server Executes Action
```

---

# Image-Based CSRF

Historically, some applications exposed state-changing actions via GET requests.

Example concept

```
<img src="/deleteAccount">
```

If the endpoint modifies state, the browser may trigger unintended actions.

State-changing operations must never rely on GET requests.

---

# Auto-Submitting Forms

```
Hidden Form

      │

JavaScript

      │

Submit()

      │

Browser

      ▼

Authenticated Request
```

The victim often sees no visible indication.

---

# API Gateway Perspective

```
Browser

     │

Authenticated Request

     ▼

API Gateway

     │

Forward Request

     ▼

Backend API
```

Without CSRF validation, the gateway cannot distinguish legitimate and forged requests.

---

# Modern Browser Security

Modern browsers include several protections.

Examples

- SameSite cookies
- Secure cookies
- Improved origin handling
- Mixed content restrictions

However, applications must still implement server-side defenses.

---

# Best Practices

Authentication

- Prefer stateless Bearer Tokens for APIs.
- Minimize cookie-based authentication where appropriate.
- Protect session cookies.

Design

- Use proper HTTP methods.
- Separate read and write operations.
- Validate all state-changing requests.

Operations

- Test CSRF protections regularly.
- Monitor sensitive endpoints.
- Review browser compatibility.

---

# Common Mistakes

Avoid

- State-changing GET requests
- No CSRF validation
- Overreliance on CORS
- Assuming HTTPS prevents CSRF
- Missing cookie protections
- Ignoring browser behavior
- Weak session management
- Exposing administrative actions without additional verification

---

# Key Takeaways

- CSRF exploits automatic browser credential transmission.
- Cookie-based authentication is the primary risk factor.
- Properly implemented Bearer Token authentication significantly reduces classic CSRF exposure.
- CORS is not a CSRF defense.
- Secure API design minimizes opportunities for request forgery.

---

**Next:** Anti-CSRF tokens, SameSite cookies, Origin and Referer validation, double-submit cookies, detection engineering, SIEM integration, hands-on labs, troubleshooting, and interview questions.