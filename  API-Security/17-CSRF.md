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

# Anti-CSRF Tokens

The most widely used defense against CSRF is the anti-CSRF token.

An anti-CSRF token is a cryptographically secure, unpredictable value generated by the server and validated for every state-changing request.

```
User Login

      │

Generate CSRF Token

      │

Browser Stores Token

      │

State-Changing Request

      │

Validate Token

      ▼

Accept Request
```

If the token is missing or invalid, the request is rejected.

---

# Why Anti-CSRF Tokens Work

An attacker can cause the victim's browser to send cookies automatically.

However,

the attacker cannot read or predict the victim's CSRF token due to the browser's Same-Origin Policy.

```
Attacker

      │

Knows Cookies?

      │

No

──────────────

Knows CSRF Token?

      │

No

──────────────

Attack Fails
```

---

# Characteristics of Secure CSRF Tokens

A secure token should be:

- Cryptographically random
- Unpredictable
- Unique per user session
- Resistant to guessing
- Protected from disclosure
- Validated on every state-changing request

Avoid:

- Sequential values
- Static tokens
- Predictable timestamps
- User identifiers as tokens

---

# Synchronizer Token Pattern

The Synchronizer Token Pattern stores the token on the server.

```
Browser

     │

Session Cookie

     │

CSRF Token

     ▼

Application Server

     │

Session Store

     ▼

Validate Token
```

Advantages

- Strong security
- Simple validation
- Widely adopted

Disadvantages

- Requires server-side session storage

---

# Double-Submit Cookie Pattern

Stateless applications commonly use the Double-Submit Cookie pattern.

```
Browser

 │

Cookie

CSRF=abc123

 │

Header

X-CSRF-Token=abc123

 │

Server

 │

Compare Values

 ▼

Valid?
```

If both values match, the request is accepted.

---

# Double-Submit Workflow

```
User

 │

Login

 │

Server Sets Cookie

 │

JavaScript Reads Cookie

 │

Adds Header

 │

Server Compares

 ▼

Accept Request
```

---

# Per-Session vs Per-Request Tokens

| Token Type | Advantages | Disadvantages |
|------------|------------|---------------|
| Per Session | Lower overhead | Longer lifetime |
| Per Request | Better security | More complex implementation |

Many enterprise applications use per-session tokens with periodic rotation.

---

# Token Rotation

Regular token rotation reduces exposure.

```
Login

 │

Generate Token

 │

Use Token

 │

Rotate

 │

Continue Session
```

Rotation is especially useful after authentication events or privilege changes.

---

# Token Validation Process

```
Incoming Request

        │

Session Exists?

        │

Retrieve Expected Token

        │

Compare Tokens

   ┌────┴─────┐

   ▼          ▼

 Match     No Match

   ▼          ▼

Allow      Reject
```

---

# Where Should Tokens Be Sent?

Common approaches

- Custom HTTP header
- Hidden HTML form field
- Request body

For APIs consumed by browser-based JavaScript applications, custom headers are generally preferred.

---

# Custom Request Headers

Example

```
POST /api/profile

X-CSRF-Token:

d7fa92...
```

Custom headers cannot be added by standard HTML forms alone, making them a useful CSRF mitigation when validated correctly.

---

# Hidden Form Fields

Traditional web applications often embed tokens.

```
<form>

<input
type="hidden"
name="csrf"

value="abc123">

</form>
```

The server validates the submitted token before processing the request.

---

# Token Expiration

Tokens should have reasonable lifetimes.

```
Generate

     │

Use

     │

Expire

     │

Generate New
```

Very long-lived tokens increase risk if disclosed.

---

# SameSite Cookies

Modern browsers support the `SameSite` cookie attribute.

It limits when browsers automatically send cookies during cross-site requests.

```
Set-Cookie

SameSite=...
```

This is one of the most effective browser-level CSRF mitigations.

---

# SameSite Modes

| Mode | Behavior |
|------|----------|
| Strict | Cookies sent only for same-site requests |
| Lax | Cookies sent for most top-level navigation but restricted for many cross-site requests |
| None | Cookies allowed in cross-site requests (requires `Secure`) |

---

# SameSite=Strict

```
Browser

     │

Cross-Site Request

     │

Cookie?

     ▼

No
```

Advantages

- Strong CSRF protection

Disadvantages

- May affect user experience for certain navigation flows.

---

# SameSite=Lax

```
Top-Level Navigation

       │

Cookie Sent

──────────────

Background Request

       │

Cookie Not Sent
```

Lax offers a balance between usability and security for many applications.

---

# SameSite=None

```
Cross-Site Requests

        │

Cookies Allowed

        │

Secure Required
```

This mode should be used only when cross-site cookies are genuinely required.

---

# Secure Cookie Attribute

Sensitive cookies should include:

```
Secure
```

```
Set-Cookie:

Secure
```

This instructs browsers to send the cookie only over HTTPS.

---

# HttpOnly Attribute

```
Set-Cookie

HttpOnly
```

Benefits

- Prevents JavaScript from directly reading the cookie.
- Reduces session theft via XSS.

Important

`HttpOnly` helps mitigate XSS-related cookie theft but **does not prevent CSRF** because browsers still send the cookie automatically.

---

# Secure Cookie Configuration

Example

```
Set-Cookie:

Secure

HttpOnly

SameSite=Lax
```

Production deployments should choose the appropriate `SameSite` value based on application requirements.

---

# Origin Validation

Servers can validate the `Origin` header.

```
Incoming Request

       │

Origin Header

       │

Trusted?

 ┌─────┴─────┐

 ▼           ▼

Yes         No

 ▼           ▼

Allow      Reject
```

Origin validation provides an additional layer of protection but should complement—not replace—anti-CSRF tokens.

---

# Referer Validation

Some applications validate the `Referer` header.

```
Referer

https://portal.company.com

        │

Trusted?

        ▼

Decision
```

Considerations

- Some browsers or privacy settings may omit or modify this header.
- It should not be the sole CSRF defense.

---

# Combining Multiple Defenses

A layered approach provides the strongest protection.

```
Browser

      │

SameSite Cookies

      │

CSRF Token

      │

Origin Validation

      │

Authentication

      │

Authorization

      ▼

Protected API
```

---

# CSRF Protection in REST APIs

REST APIs using cookie-based authentication should implement:

- Anti-CSRF tokens
- SameSite cookies
- Origin validation
- Proper HTTP methods

REST APIs using Authorization headers instead of cookies generally have significantly lower exposure to classic CSRF attacks.

---

# CSRF Protection in GraphQL APIs

GraphQL mutations change application state.

Example

```
mutation {

updateProfile

changePassword

deleteAccount

}
```

Mutations authenticated with cookies require the same CSRF protections as REST endpoints.

---

# CSRF and Single Page Applications (SPAs)

Typical workflow

```
Browser

      │

Load SPA

      │

Receive CSRF Token

      │

Store Token

      │

Attach Header

      ▼

API Request
```

The frontend framework automatically includes the token in protected requests.

---

# Enterprise API Gateway Architecture

```
                   Browser

                      │

                      ▼

                API Gateway

          ┌───────────┼────────────┐

          ▼           ▼            ▼

 Authentication  Origin Check  Logging

                      │

                      ▼

                Backend APIs

          ┌───────────┼────────────┐

          ▼           ▼            ▼

 Session      CSRF Token     Authorization

                      │

                      ▼

                  Database
```

The gateway can enforce Origin policies, while the application validates CSRF tokens.

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Missing CSRF Token | State-changing request without token |
| Invalid CSRF Token | Token mismatch or validation failure |
| Token Replay | Same token reused unusually across sessions |
| Suspicious Origin | Unexpected Origin header values |
| Missing Origin | Unexpected absence of Origin for browser requests |
| SameSite Misconfiguration | Sensitive cookies lacking expected attributes |
| High CSRF Validation Failures | Repeated rejected requests |
| Sensitive GET Requests | State-changing behavior on GET endpoints |

---

# SIEM Integration

Collect telemetry from

- API Gateway
- Web Server
- Authentication Service
- Session Store
- Application Logs
- WAF

```
Browser

      │

API Gateway

      │

Application

      │

CSRF Events

      │

SIEM

      │

Detection Rules

      ▼

SOC Investigation
```

---

# Example Correlation Rules

Rule 1

```
Missing CSRF Token

        │

Authenticated Session

        │

Sensitive Endpoint

        ▼

Medium Severity Alert
```

Rule 2

```
Invalid CSRF Token

        │

Multiple Attempts

        │

Different Origins

        ▼

Potential CSRF Attack
```

Rule 3

```
Sensitive GET Request

       │

Authentication Cookie

       │

State Change

       ▼

Critical Alert
```

---

# Hands-on Lab 1 – Token Validation

**Objective**

Verify CSRF token enforcement.

**Steps**

1. Authenticate to a test application.
2. Capture a valid request.
3. Remove the CSRF token.
4. Replay the request.
5. Confirm that the application rejects it.

**Learning Outcomes**

- CSRF validation
- Secure request handling
- Token verification

---

# Hands-on Lab 2 – SameSite Cookie Review

**Objective**

Inspect cookie protection settings.

**Steps**

1. Authenticate to a browser-based application.
2. Review response cookies.
3. Verify `Secure`, `HttpOnly`, and `SameSite` attributes.
4. Document missing protections.

**Learning Outcomes**

- Cookie security
- Browser protections
- Session hardening

---

# Hands-on Lab 3 – Origin Validation

**Objective**

Evaluate Origin validation.

**Steps**

1. Send legitimate requests from trusted origins.
2. Repeat using untrusted origins.
3. Verify server behavior.
4. Review gateway and application logs.

**Learning Outcomes**

- Origin validation
- Defense in depth
- API security assessment

---

# Troubleshooting

## Legitimate Requests Rejected

Possible causes

- Expired CSRF token
- Token not submitted
- Session timeout
- Token rotation mismatch

---

## Browser Not Sending Cookies

Possible causes

- Incorrect `SameSite` setting
- Missing `Secure` attribute over HTTPS
- Browser privacy configuration
- Session expiration

---

## CSRF Protection Bypass Suspected

Possible causes

- Missing validation on specific endpoints
- Inconsistent API implementation
- State-changing GET request
- Disabled Origin validation

---

## Excessive CSRF Validation Failures

Possible causes

- Client implementation bug
- Expired frontend tokens
- Browser caching issue
- Active attack attempts

---

## SPA Requests Failing

Possible causes

- Missing custom header
- Token retrieval failure
- Incorrect frontend configuration
- Session mismatch

---

# Interview Questions

## Fundamental

1. What is Cross-Site Request Forgery (CSRF)?
2. Why are cookie-based applications vulnerable to CSRF?
3. How does an anti-CSRF token work?
4. What is the Synchronizer Token Pattern?
5. What is the Double-Submit Cookie Pattern?
6. What is the purpose of the `SameSite` cookie attribute?
7. Does `HttpOnly` prevent CSRF?
8. Why should GET requests not change application state?
9. What role does the `Origin` header play in CSRF protection?
10. Why doesn't CORS alone stop CSRF attacks?

---

## Intermediate

11. Compare `SameSite=Strict`, `Lax`, and `None`.
12. How would you implement CSRF protection in a SPA?
13. Why are Authorization header-based APIs generally less susceptible to classic CSRF?
14. How should CSRF events be monitored in a SIEM?
15. What are the limitations of Referer validation?
16. Why should anti-CSRF tokens be unpredictable?
17. How would you protect GraphQL mutations?
18. How does token rotation improve security?
19. What indicators suggest an active CSRF attack?
20. How would you design CSRF protection for a browser-based enterprise API?

---

## Scenario-Based

**Scenario 1**

An authenticated banking application uses session cookies but does not validate CSRF tokens.

- What attacks become possible?
- Which controls should be implemented immediately?
- How would you verify the fixes?

---

**Scenario 2**

A production API uses `SameSite=None` for all session cookies.

- What additional cookie attribute is required?
- What risks should be evaluated?
- When is this configuration appropriate?

---

**Scenario 3**

Security monitoring reports a spike in rejected state-changing requests with invalid CSRF tokens from multiple external origins.

- What could this indicate?
- Which logs would you correlate?
- How would you prioritize investigation and response?

---

# Chapter Summary

In this chapter, we explored CSRF attacks against browser-based APIs and applications.

We covered:

- CSRF fundamentals
- Browser credential behavior
- Session cookies
- Anti-CSRF tokens
- Synchronizer Token Pattern
- Double-Submit Cookie Pattern
- SameSite cookies
- Secure cookie attributes
- Origin and Referer validation
- REST and GraphQL considerations
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Modern CSRF protection relies on layered defenses that combine secure cookie configuration, anti-CSRF tokens, Origin validation, and robust authentication and authorization controls.

---

# Chapter Review

You should now be able to answer:

- Why are cookie-based APIs vulnerable to CSRF?
- How do anti-CSRF tokens prevent request forgery?
- What are the differences between Synchronizer Token and Double-Submit Cookie patterns?
- How do `SameSite` cookie settings influence browser behavior?
- Why are Origin validation and anti-CSRF tokens complementary controls?
- Which CSRF-related events should be monitored in a SIEM?
- How would you design enterprise-grade CSRF protection for a browser-based API platform?

If you can confidently answer these questions, you are ready to continue with **Chapter 18 – API Input Validation**, where you'll learn about server-side validation, canonicalization, allowlists, schema validation, secure parsing, injection prevention, detection engineering, and enterprise validation strategies.

---

# References

## Standards

- RFC 6265 – HTTP State Management Mechanism
- RFC 9110 – HTTP Semantics

## Security Standards

- OWASP Cross-Site Request Forgery Prevention Cheat Sheet
- OWASP API Security Top 10
- OWASP ASVS
- NIST SP 800-53

## Further Reading

- Browser Cookie Specifications
- MDN Web Docs – SameSite Cookies
- Enterprise Secure Session Management Guidelines

---

# What's Next?

➡️ **Chapter 18 – API Input Validation**

Topics include:

- Input validation principles
- Trust boundaries
- Server-side validation
- Canonicalization
- Allowlists vs blocklists
- Schema validation
- Type validation
- Length and range validation
- Injection prevention
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions