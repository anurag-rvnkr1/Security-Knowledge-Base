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

# 15-CSRF.md

# Part 2 — CSRF Attack Vectors, HTTP Methods, Browser Behavior, CSRF Tokens, SameSite Cookies, Origin Validation, and Enterprise Defenses

> **"Modern CSRF protection does not rely on a single control. Secure applications combine CSRF tokens, browser protections, cookie attributes, origin validation, and secure application design to defend against forged requests."**

---

# Learning Objectives

After completing this part, you will understand:

- CSRF Attack Vectors
- Browser Request Behavior
- State-Changing Requests
- CSRF Tokens
- Synchronizer Token Pattern
- Double Submit Cookie Pattern
- SameSite Cookies
- Origin and Referer Validation
- Enterprise CSRF Protection
- Defense in Depth

---

# Browser Request Behavior

Browsers automatically attach authentication information when making requests to a website.

```
User Logged In

↓

Browser Stores Session

↓

Future Request

↓

Session Cookie Attached

↓

Server Receives Request
```

This automatic behavior is the primary reason CSRF attacks are possible.

---

# State-Changing Requests

CSRF primarily targets operations that modify server-side data.

Examples include:

- Change password
- Update profile
- Delete account
- Create user
- Transfer funds
- Submit orders
- Change email
- Modify permissions

```
Authenticated User

↓

Modify Data

↓

Server State Changes
```

---

# Read vs Write Operations

```
Read Data

↓

Generally Lower Risk

──────────────

Modify Data

↓

Higher CSRF Risk
```

State-changing requests should always receive stronger protection.

---

# Common Attack Flow

```
Victim

↓

Authenticated

↓

Visits Malicious Site

↓

Hidden Request Generated

↓

Browser Sends Session

↓

Application Processes Request
```

The browser behaves normally—the application must determine whether the request is legitimate.

---

# Hidden Form Submission

A malicious page could attempt to submit a hidden form automatically.

Conceptually:

```
Malicious Page

↓

Hidden Form

↓

Browser Submission

↓

Target Application
```

Without proper protections, the server may treat the request as legitimate.

---

# Image-Based Requests

Historically, attackers attempted to trigger requests through embedded resources.

```
Malicious Page

↓

Embedded Resource

↓

Browser Sends Request
```

Modern browser protections have reduced many historical attack techniques, but applications should not rely solely on browser behavior.

---

# CSRF Protection Strategy

Modern applications typically combine multiple defenses.

```
Authentication

+

CSRF Token

+

SameSite Cookies

+

Origin Validation

+

Authorization

↓

Protected Request
```

---

# CSRF Tokens

A **CSRF token** is a server-generated value associated with the user's session or request.

```
User

↓

Server

↓

Generate Token

↓

Browser

↓

Return Token

↓

Server Validation
```

The server verifies the token before processing sensitive requests.

---

# Synchronizer Token Pattern

One common approach is the Synchronizer Token Pattern.

```
Session Created

↓

Unique Token Generated

↓

Embedded in Form

↓

User Submits Form

↓

Server Compares Token

↓

Valid?

↓

Accept

OR

Reject
```

The token should be difficult to predict and generated securely.

---

# Token Validation

```
Incoming Request

↓

Token Present?

↓

Yes

↓

Token Valid?

↓

Yes

↓

Process Request

──────────────

No

↓

Reject Request
```

Missing or invalid tokens should result in request rejection.

---

# Why Tokens Work

An attacker can often cause the browser to send a request.

However:

```
Attacker

↓

Cannot Predict

↓

Valid CSRF Token

↓

Server Rejects Request
```

The token demonstrates that the request originated from the legitimate application workflow.

---

# Token Lifecycle

```
User Login

↓

Session Created

↓

Token Generated

↓

User Request

↓

Token Verified

↓

Continue Session
```

Applications may generate tokens per session or per request depending on their design.

---

# Double Submit Cookie Pattern

Another approach is the **Double Submit Cookie Pattern**.

Conceptually:

```
Browser

↓

Cookie Value

↓

Request Value

↓

Server Compares

↓

Match?

↓

Accept

OR

Reject
```

The server validates that both values match before processing the request.

---

# SameSite Cookies

Modern browsers support the **SameSite** cookie attribute.

Conceptually:

```
Cookie

↓

SameSite Policy

↓

Browser

↓

Cross-Site Request

↓

Evaluate Rules
```

SameSite reduces the likelihood that cookies will be automatically included in certain cross-site requests.

---

# Common SameSite Modes

| Mode | High-Level Behavior |
|------|----------------------|
| Strict | Strongest cross-site restrictions |
| Lax | Allows some navigation scenarios while restricting many cross-site requests |
| None | Cross-site usage permitted when configured appropriately |

Exact browser behavior depends on standards and browser implementation.

---

# SameSite Concept

```
Cross-Site Request

↓

Browser

↓

Cookie Policy

↓

Cookie Included?

↓

Depends On SameSite Rules
```

SameSite provides an important browser-side mitigation but should not replace server-side CSRF defenses.

---

# Origin Validation

Applications may verify the request's origin.

Conceptually:

```
Incoming Request

↓

Origin Header

↓

Trusted?

↓

Yes

↓

Continue

──────────────

No

↓

Reject
```

Origin validation helps detect unexpected cross-site requests.

---

# Referer Validation

Some applications also examine the `Referer` header.

```
Incoming Request

↓

Referer

↓

Expected?

↓

Yes

↓

Continue

──────────────

No

↓

Investigate

OR

Reject
```

Referer validation is typically used as an additional layer rather than the sole defense.

---

# Layered Defense

```
Authenticated Session

↓

CSRF Token

↓

SameSite Cookie

↓

Origin Validation

↓

Authorization

↓

Sensitive Operation
```

Multiple independent controls improve resilience.

---

# Enterprise Architecture

```
                  Browser

                     │

            Authenticated Session

                     │

                     ▼

               Load Secure Form

                     │

          Receive CSRF Token

                     │

                     ▼

             Submit Request

                     │

                     ▼

                API Gateway

                     │

     Validate Token & Origin

                     │

                     ▼

              Business Service

                     │

                     ▼

                 Database
```

---

# Enterprise Example

An enterprise HR application protects profile updates using:

- Session authentication
- CSRF token validation
- SameSite cookies
- Origin verification
- Authorization checks
- Audit logging

Only requests that satisfy all required security checks are processed.

---

# Security Checklist

```
✓ Session Authentication

✓ CSRF Tokens

✓ SameSite Cookies

✓ Origin Validation

✓ Authorization Checks

✓ HTTPS

✓ Logging

✓ Monitoring
```

---

# Hands-on Lab (Conceptual)

1. Identify state-changing requests in an application.
2. Observe whether forms contain a CSRF token.
3. Inspect cookies using Developer Tools.
4. Review SameSite attributes conceptually.
5. Compare requests with and without CSRF protection in a controlled environment.
6. Document the application's layered defense strategy.

> Perform testing only in systems where you have explicit authorization.

---

# Interview Questions

1. Why are CSRF tokens effective?
2. What is the Synchronizer Token Pattern?
3. What is the Double Submit Cookie Pattern?
4. What is the purpose of the SameSite cookie attribute?
5. Why shouldn't SameSite replace CSRF tokens?
6. What is Origin validation?
7. What is the role of the Referer header in CSRF protection?
8. Why should multiple CSRF defenses be combined?
9. Which requests require CSRF protection?
10. Why are state-changing operations the primary CSRF target?

---

# Best Practices

- Protect every state-changing endpoint with CSRF defenses.
- Generate cryptographically secure CSRF tokens.
- Validate tokens on the server.
- Use appropriate SameSite cookie settings.
- Validate request origins where applicable.
- Continue enforcing authentication and authorization independently.
- Periodically review CSRF protections during security assessments.

---

# Common Mistakes

- Protecting login pages but not profile updates.
- Treating SameSite as a complete replacement for CSRF tokens.
- Accepting missing or invalid tokens.
- Trusting only the Referer header.
- Forgetting to protect newly added API endpoints or forms.
- Assuming HTTPS alone prevents CSRF.

---

# Key Takeaways

- CSRF exploits authenticated browser sessions, not authentication itself.
- CSRF tokens are a primary server-side defense against forged requests.
- SameSite cookies add an important browser-level mitigation.
- Origin and Referer validation provide additional layers of protection.
- A defense-in-depth strategy offers the strongest protection against CSRF attacks.

# 15-CSRF.md

# Part 3 — Advanced CSRF, Modern Browser Protections, APIs, OAuth Considerations, Security Testing, Enterprise Architecture, and Secure Design

> **"Modern browsers have significantly reduced CSRF risk through features like SameSite cookies, but secure applications must still implement server-side defenses because browser behavior alone cannot guarantee protection."**

---

# Learning Objectives

After completing this part, you will understand:

- Modern Browser Protections
- CSRF and APIs
- CSRF in Single Page Applications (SPAs)
- OAuth and CSRF Considerations
- Login CSRF
- Logout CSRF
- CSRF Security Testing
- Enterprise API Architecture
- Secure Design Principles
- Common Misconfigurations

---

# Modern Browser Defenses

Today's browsers provide several built-in protections.

```
Browser Security

│

├── SameSite Cookies

├── Origin Header

├── Fetch Metadata

├── HTTPS

└── Secure Cookie Handling
```

These protections reduce risk but should complement—not replace—application-level defenses.

---

# Defense in Depth

A secure application combines multiple security controls.

```
HTTPS

↓

Authentication

↓

Authorization

↓

CSRF Token

↓

SameSite Cookies

↓

Origin Validation

↓

Logging

↓

Monitoring
```

No single protection should be considered sufficient on its own.

---

# CSRF in APIs

Traditional browser-based applications commonly use cookies for authentication.

```
Browser

↓

Cookie

↓

Authenticated API Request
```

If authentication relies on automatically included cookies, CSRF protections remain important.

---

# Browser-Based APIs

```
Frontend

↓

JavaScript

↓

Authenticated Request

↓

API

↓

Server Validation
```

The API should validate both authentication and CSRF protections where applicable.

---

# Single Page Applications (SPAs)

Many modern applications are built as SPAs.

```
Browser

↓

Single Page Application

↓

API Calls

↓

Backend Services
```

The application may make many asynchronous requests after login.

---

# SPA Security

Even in SPAs:

```
Authenticated Session

↓

Sensitive Request

↓

CSRF Protection Required
```

The application architecture changes, but the security principles remain the same.

---

# Token-Based Authentication

Some applications authenticate requests using tokens sent explicitly by JavaScript instead of automatically included session cookies.

Conceptually:

```
JavaScript

↓

Authentication Token

↓

Request

↓

Server Validation
```

Whether CSRF protection is required depends on **how authentication credentials are transmitted** and the application's overall design.

---

# Cookies vs Explicit Tokens

| Authentication Method | Browser Automatically Includes Credentials? |
|-----------------------|---------------------------------------------|
| Session Cookies | Generally Yes |
| Explicitly Added Authorization Header | Typically Added by Application Code |

This distinction affects CSRF risk but does not eliminate the need for secure application design.

---

# Login CSRF

Applications should also consider login workflows.

Conceptually:

```
Attacker

↓

Forces Login Request

↓

Victim Browser

↓

Unexpected Session
```

Proper validation during authentication flows helps reduce this risk.

---

# Logout CSRF

Similarly, applications should evaluate logout operations.

```
Authenticated User

↓

Unexpected Logout Request

↓

Session Ends
```

While generally less severe than unauthorized state changes, unexpected logout behavior may still impact users.

---

# Password Change Example

```
User

↓

Authenticated Session

↓

Password Change Request

↓

CSRF Validation

↓

Authorized?

↓

Process Request
```

Sensitive account-management operations should always be protected.

---

# Administrative Operations

High-risk operations include:

- User creation
- User deletion
- Role assignment
- Permission changes
- System configuration
- Billing modifications

These operations require robust authentication, authorization, and CSRF protections.

---

# OAuth Considerations

Applications using OAuth or OpenID Connect often involve multiple browser redirects.

```
Application

↓

Identity Provider

↓

Authentication

↓

Return

↓

Application
```

These workflows include additional protections against request forgery, which are specific to the authentication protocol.

---

# Request Validation

Every sensitive request should undergo multiple checks.

```
Incoming Request

↓

Authentication

↓

Authorization

↓

CSRF Validation

↓

Business Rules

↓

Database Update
```

---

# Fetch Metadata (Conceptual)

Modern browsers may provide metadata about how requests originated.

Conceptually:

```
Browser

↓

Request Metadata

↓

Server Evaluation

↓

Additional Validation
```

This information can serve as another layer of defense.

---

# Enterprise API Gateway

```
                Browser

                   │

          Authenticated Request

                   │

                   ▼

             API Gateway

                   │

   Authentication Validation

                   │

        CSRF Validation

                   │

       Authorization Check

                   │

                   ▼

            Backend Services
```

The gateway may centralize common security controls.

---

# Enterprise Security Pipeline

```
Incoming Request

↓

TLS

↓

Authentication

↓

CSRF Validation

↓

Authorization

↓

Input Validation

↓

Business Logic

↓

Audit Logging

↓

Database
```

Each stage contributes to overall application security.

---

# Security Testing

During an assessment, verify:

```
✓ State-Changing Requests

✓ CSRF Token Validation

✓ SameSite Cookies

✓ Origin Validation

✓ Sensitive APIs

✓ Administrative Functions

✓ Authentication Flow

✓ Session Management
```

Testing must always be conducted with proper authorization.

---

# Logging

Applications should record:

- CSRF validation failures
- Invalid tokens
- Missing tokens
- Origin validation failures
- Administrative actions
- Authentication events

Logs support incident response and forensic analysis.

---

# Monitoring

Useful metrics include:

| Metric | Purpose |
|---------|----------|
| Invalid CSRF tokens | Detect potential attacks or client issues |
| Missing tokens | Identify implementation problems |
| Origin validation failures | Detect unexpected request sources |
| Authentication failures | Monitor account security |
| Sensitive operation frequency | Detect unusual behavior |

---

# Enterprise Example

A multinational healthcare organization protects patient record updates using:

```
User

↓

HTTPS

↓

Authentication

↓

CSRF Token

↓

SameSite Cookie

↓

Origin Validation

↓

Authorization

↓

Electronic Medical Records
```

Every update request passes multiple independent security checks.

---

# Common Misconfigurations

| Misconfiguration | Risk |
|------------------|------|
| Missing CSRF protection on profile updates | Unauthorized state changes |
| Relying only on SameSite cookies | Reduced defense in depth |
| Accepting missing tokens | Forged requests may succeed |
| Protecting only admin pages | Regular user functions remain exposed |
| Inconsistent validation across APIs | Uneven security posture |

---

# Hands-on Lab (Conceptual)

1. Map all state-changing endpoints.
2. Identify where CSRF tokens are validated.
3. Review cookie attributes.
4. Observe authenticated requests in Developer Tools.
5. Verify that sensitive requests undergo multiple validation steps.
6. Document the application's CSRF protection strategy.

> Perform testing only in systems where you have explicit authorization.

---

# Interview Questions

1. Does a Single Page Application eliminate CSRF risk?
2. Why are state-changing requests prioritized for CSRF protection?
3. What is Login CSRF?
4. Why should logout functionality also be reviewed?
5. How does token-based authentication differ from cookie-based authentication in terms of browser behavior?
6. What additional browser information can support CSRF defenses?
7. Why is CSRF validation performed before business logic?
8. What security controls should surround administrative operations?
9. What events should be logged for CSRF monitoring?
10. Why is defense in depth important for CSRF protection?

---

# Best Practices

- Protect every state-changing operation.
- Use cryptographically secure CSRF tokens.
- Combine CSRF tokens with SameSite cookies and origin validation.
- Review authentication workflows, including login and logout.
- Protect administrative functions with additional safeguards.
- Log and monitor CSRF validation failures.
- Regularly review CSRF protections after architectural changes.

---

# Common Mistakes

- Assuming SPAs are automatically immune to CSRF.
- Protecting only high-profile pages while ignoring ordinary account features.
- Depending solely on browser protections.
- Ignoring login and logout workflows.
- Failing to monitor repeated CSRF validation failures.
- Treating CSRF protection as optional for internal applications.

---

# Key Takeaways

- Modern browsers reduce CSRF risk, but server-side defenses remain essential.
- Both traditional and modern web applications should evaluate CSRF risks based on how authentication is handled.
- Administrative and state-changing operations require strong layered protections.
- Enterprise applications combine authentication, authorization, CSRF validation, logging, and monitoring.
- Defense in depth remains the most effective approach against request forgery.

```text id="jid720"
**Next:** Part 4
```