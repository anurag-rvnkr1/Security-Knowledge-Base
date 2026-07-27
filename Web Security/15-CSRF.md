# 15-CSRF.md

# Part 1 — Cross-Site Request Forgery (CSRF) Fundamentals, Browser Trust Model, Attack Flow, and Enterprise Security

> **"Cross-Site Request Forgery (CSRF) exploits the browser's trust in an authenticated session. Instead of stealing credentials, it tricks a user's browser into performing unintended actions on a trusted website."**

---

# Learning Objectives

After completing this part, you will understand:

- What CSRF Is
- Why CSRF Exists
- Browser Trust Model
- CSRF Attack Flow
- Authentication vs Authorization vs CSRF
- Preconditions for CSRF
- Real-World Examples
- Enterprise Impact
- Browser Behavior
- Common Misconceptions

---

# What is CSRF?

**Cross-Site Request Forgery (CSRF)** is a web attack in which an attacker causes a victim's browser to send an unintended request to a web application where the victim is already authenticated.

```
Victim

↓

Logged Into Website

↓

Visits Malicious Website

↓

Browser Sends Request

↓

Trusted Website Processes Request
```

The browser sends the request because it already possesses the user's authenticated session.

---

# Why CSRF Exists

Web browsers automatically include authentication information such as session cookies when communicating with a website.

```
Browser

↓

Request

↓

Automatically Includes

↓

Session Cookie
```

This automatic behavior enables convenient user experiences but can be abused if proper defenses are absent.

---

# Browser Trust Model

```
User

↓

Login

↓

Session Established

↓

Browser Stores Session

↓

Future Requests

↓

Session Automatically Included
```

The browser cannot always distinguish between a legitimate user action and a maliciously induced request.

---

# Authentication vs Authorization vs CSRF

| Concept | Purpose |
|----------|----------|
| Authentication | Verifies who the user is |
| Authorization | Determines what the user may do |
| CSRF Protection | Verifies that the request genuinely originated from the intended application |

These mechanisms complement one another.

---

# What CSRF Does NOT Do

CSRF does **not**:

- Steal passwords directly
- Break encryption
- Guess session IDs
- Bypass authentication
- Execute arbitrary code on the server

Instead, it abuses an already authenticated browser session.

---

# High-Level Attack Flow

```
Victim

↓

Logs Into Bank

↓

Session Active

↓

Visits Malicious Website

↓

Malicious Page Triggers Request

↓

Browser Sends Session Cookie

↓

Bank Receives Authenticated Request
```

---

# Why the Browser Sends Cookies

```
Request

↓

Destination Website

↓

Matching Session Cookie Found

↓

Browser Automatically Includes Cookie
```

This is expected browser behavior and is fundamental to web sessions.

---

# Trust Relationship

```
Website

↓

Trusts Session Cookie

↓

Processes Request
```

If the application validates only the session and not the request origin, unintended actions may occur.

---

# Typical Preconditions

For a CSRF attack to succeed, several conditions commonly exist:

```
User Authenticated

↓

Session Active

↓

Browser Sends Credentials Automatically

↓

Application Lacks CSRF Protection
```

If one or more of these conditions are absent, the attack may fail.

---

# Conceptual Scenario

Imagine a user is logged into:

```
https://bank.example
```

The same user later visits another website.

```
news.example

↓

Hidden Request

↓

bank.example
```

If adequate protections are not present, the browser may automatically attach the authenticated session.

---

# Browser Perspective

The browser simply processes requests according to established rules.

```
User Action

OR

Page Action

↓

HTTP Request

↓

Attach Cookies

↓

Send Request
```

The browser itself does not determine whether the request represents the user's actual intention.

---

# CSRF vs XSS

| Cross-Site Scripting (XSS) | Cross-Site Request Forgery (CSRF) |
|----------------------------|-----------------------------------|
| Injects malicious script | Tricks browser into sending requests |
| Executes JavaScript | Abuses authenticated sessions |
| Often targets users viewing a page | Targets authenticated browser requests |
| May lead to CSRF in some scenarios | Does not require script execution on the target site |

These are different attack classes, although they may interact.

---

# Real-World Examples

Potential targets include:

- Password changes
- Email updates
- Address changes
- Account preferences
- Fund transfer requests
- Administrative actions
- Purchase confirmations
- Profile updates

Any state-changing action should be considered during security design.

---

# Safe vs Unsafe HTTP Methods

Conceptually:

```
Read Operation

↓

Generally Safe

──────────────

Modify Operation

↓

Requires Additional Protection
```

Operations that change server-side state require stronger protection against CSRF.

---

# Enterprise Example

```
Employee Portal

↓

Authenticated User

↓

HR Application

↓

Update Personal Details

↓

Browser Sends Session

↓

Server Processes Request
```

Without proper CSRF defenses, unauthorized state-changing requests could be accepted.

---

# Why Financial Applications Care

```
Authenticated Session

↓

Sensitive Operation

↓

High Business Impact
```

Applications involving payments, healthcare, administration, or identity management require strong CSRF protections.

---

# Browser Session Model

```
Login

↓

Session Cookie

↓

Stored By Browser

↓

Future Requests

↓

Cookie Automatically Included
```

This model enables seamless browsing but requires server-side safeguards.

---

# Browser Security Layers

CSRF is only one aspect of web security.

```
HTTPS

↓

Authentication

↓

Authorization

↓

CSRF Protection

↓

Input Validation

↓

Logging

↓

Monitoring
```

Defense in depth remains essential.

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| CSRF steals passwords | No, it abuses an authenticated session |
| HTTPS prevents CSRF | No, HTTPS protects data in transit but does not stop forged requests |
| Authentication alone prevents CSRF | No, authenticated users can still be targeted |
| Only banks are affected | Any authenticated web application may be vulnerable |

---

# Enterprise Risk

Possible consequences include:

- Unauthorized account changes
- Administrative misuse
- Business workflow manipulation
- Unauthorized transactions
- Data integrity issues
- Compliance violations

The impact depends on the application's functionality and authorization model.

---

# Hands-on Lab (Conceptual)

1. Identify an application requiring authentication.
2. Map actions that modify server-side data.
3. List which requests depend on session cookies.
4. Determine which operations would require CSRF protection.
5. Compare read-only operations with state-changing operations.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is Cross-Site Request Forgery?
2. Why does CSRF occur?
3. Does CSRF steal user passwords?
4. Why are authenticated sessions important to CSRF?
5. What browser behavior enables CSRF attacks?
6. What conditions are generally required for a CSRF attack?
7. How does CSRF differ from XSS?
8. Why are state-changing requests higher risk?
9. Does HTTPS eliminate CSRF?
10. Why are enterprise applications frequent CSRF targets?

---

# Best Practices

- Treat every authenticated state-changing request as potentially exposed to CSRF.
- Design applications using defense in depth.
- Protect sensitive operations with dedicated CSRF mitigations.
- Review session management alongside CSRF defenses.
- Consider browser behavior during application architecture.
- Perform regular security reviews of authenticated workflows.

---

# Common Mistakes

- Assuming authentication alone prevents CSRF.
- Ignoring browser automatic cookie behavior.
- Protecting only administrative functions while leaving user functions exposed.
- Treating HTTPS as a replacement for CSRF protection.
- Forgetting to evaluate newly added state-changing endpoints.

---

# Key Takeaways

- CSRF exploits the browser's automatic handling of authenticated sessions.
- It abuses trust rather than stealing credentials.
- Authentication, authorization, and CSRF protection solve different security problems.
- State-changing operations require dedicated CSRF defenses.
- Understanding browser session behavior is essential for designing secure web applications.

```text id="jid720"
**Next:** Part 2
```