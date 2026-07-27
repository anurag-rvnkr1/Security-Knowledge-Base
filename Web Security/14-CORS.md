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

# 14-CORS.md

# Part 2 — CORS HTTP Headers, Simple Requests, Preflight Requests, Browser Validation, Credentials, and Enterprise API Design

> **"CORS is implemented through HTTP headers exchanged between the browser and the server. The browser evaluates these headers before deciding whether JavaScript may access a cross-origin response."**

---

# Learning Objectives

After completing this part, you will understand:

- CORS HTTP Headers
- Request Headers
- Response Headers
- Simple Requests
- Preflight Requests
- OPTIONS Requests
- Credentials and Cookies
- Browser Validation
- Enterprise API Design
- Common Configuration Mistakes

---

# How CORS Works

CORS operates through HTTP request and response headers.

```
JavaScript

↓

Browser

↓

HTTP Request

↓

Server

↓

HTTP Response

↓

Browser Validation

↓

Expose Response

OR

Restrict Response
```

---

# CORS Request Lifecycle

```
Page

↓

JavaScript

↓

Cross-Origin Request

↓

Browser

↓

Server

↓

CORS Headers

↓

Browser Decision
```

The browser always performs the final decision.

---

# Important CORS Headers

The most common response headers include:

| Header | Purpose |
|---------|----------|
| `Access-Control-Allow-Origin` | Specifies allowed origin(s) |
| `Access-Control-Allow-Methods` | Lists permitted HTTP methods |
| `Access-Control-Allow-Headers` | Lists permitted request headers |
| `Access-Control-Allow-Credentials` | Indicates whether credentials may be included |
| `Access-Control-Expose-Headers` | Makes selected response headers accessible to JavaScript |
| `Access-Control-Max-Age` | Specifies how long preflight results may be cached |

---

# Access-Control-Allow-Origin

This response header identifies which origin may access the response.

Conceptually:

```
Server

↓

Access-Control-Allow-Origin

↓

Browser

↓

Origin Match?

↓

Yes

↓

Expose Response
```

---

# Example

Frontend:

```
https://app.company.com
```

API:

```
https://api.company.com
```

The API explicitly identifies which origin is permitted to access the response.

---

# Origin Matching

```
Browser Origin

↓

Compare

↓

Allowed Origin

↓

Match?

↓

Yes

↓

Continue

──────────────

No

↓

Restrict Access
```

---

# Wildcard Origin

Some servers use:

```
*
```

Conceptually:

```
Allow

↓

All Origins
```

While this may be appropriate for certain public resources, it is generally **not appropriate for sensitive APIs**.

---

# Access-Control-Allow-Methods

Servers indicate which HTTP methods are permitted.

Examples include:

- GET
- POST
- PUT
- PATCH
- DELETE
- OPTIONS

```
Browser

↓

Requested Method

↓

Server Policy

↓

Allowed?

↓

Yes / No
```

---

# Access-Control-Allow-Headers

Applications sometimes send additional request headers.

Examples:

- Authorization
- Content-Type
- X-Request-ID
- X-Correlation-ID

The server specifies which request headers are acceptable.

---

# Access-Control-Expose-Headers

Browsers do not automatically expose every response header to JavaScript.

The server can explicitly identify additional headers that may be accessed.

```
Server

↓

Response Headers

↓

Expose Selected Headers

↓

JavaScript
```

---

# Access-Control-Allow-Credentials

Some applications require credentials such as cookies or authentication information.

Conceptually:

```
Browser

↓

Credentialed Request

↓

Server Policy

↓

Allowed?

↓

Yes / No
```

Credentialed requests require careful configuration.

---

# Important Credential Rule

Conceptually:

```
Credentials

+

Wildcard Origin

↓

Not Valid Together
```

Sensitive applications should explicitly identify trusted origins when credentials are involved.

---

# Simple Requests

Certain cross-origin requests are considered **simple requests** by browsers.

Conceptually:

```
Simple Request

↓

Browser

↓

Send Request

↓

Evaluate Response
```

Simple requests generally do **not** require a preflight request.

---

# Typical Characteristics

Simple requests generally involve:

- Standard HTTP methods
- Standard request headers
- Browser-defined safe request formats

The browser determines whether a request qualifies as "simple."

---

# Non-Simple Requests

More complex requests require additional validation.

Examples may include:

- Custom request headers
- Certain content types
- Additional HTTP methods

```
Complex Request

↓

Browser

↓

Preflight Required
```

---

# What is a Preflight Request?

A preflight request asks the server whether a future request is permitted.

```
Browser

↓

OPTIONS Request

↓

Server

↓

Policy Response

↓

Browser Decision

↓

Actual Request
```

---

# Why Preflight Exists

Without preflight:

```
Complex Request

↓

Server

↓

Unexpected Operation
```

With preflight:

```
Browser

↓

Permission Check

↓

Server Approval

↓

Actual Request
```

This helps browsers determine whether the cross-origin request is allowed.

---

# Preflight Workflow

```
JavaScript

↓

Complex Request

↓

Browser

↓

OPTIONS

↓

Server

↓

Policy Response

↓

Allowed?

↓

Yes

↓

Actual Request

──────────────

No

↓

Stop
```

---

# OPTIONS Request

The browser automatically generates the preflight request when required.

```
Browser

↓

OPTIONS

↓

Server

↓

Response

↓

Browser Validation
```

Applications generally do not create these requests manually.

---

# Browser Validation

After receiving the preflight response:

```
Browser

↓

Validate

↓

Origin

↓

Method

↓

Headers

↓

Decision
```

If validation succeeds, the browser proceeds with the actual request.

---

# Access-Control-Max-Age

Browsers may cache successful preflight decisions.

```
Successful Preflight

↓

Cache Result

↓

Reuse

↓

Reduce Future Preflight Requests
```

This improves performance by avoiding unnecessary repeated checks.

---

# Enterprise API Example

```
Customer Portal

↓

JavaScript

↓

Browser

↓

OPTIONS

↓

API Gateway

↓

Policy

↓

Browser

↓

GET Request

↓

API

↓

Response
```

The API Gateway commonly centralizes CORS policy management.

---

# Enterprise Multi-Service Architecture

```
                 Browser

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

 Frontend      Identity API    Business API

                    │

             Independent CORS Policies

                    │

            Browser Validation
```

Each service may define its own CORS policy.

---

# Browser Decision Matrix

| Check | Result |
|--------|--------|
| Origin Allowed | Continue |
| Method Allowed | Continue |
| Headers Allowed | Continue |
| Credentials Valid | Continue |
| Validation Failed | Restrict JavaScript Access |

---

# Security Considerations

Proper CORS configuration should:

- Allow only trusted origins
- Permit only necessary HTTP methods
- Limit accepted request headers
- Carefully configure credential support
- Avoid unnecessary wildcard usage

---

# Common Configuration Mistakes

| Mistake | Risk |
|----------|------|
| Wildcard for sensitive APIs | Excessive exposure |
| Allowing unnecessary methods | Larger attack surface |
| Allowing unnecessary headers | Increased risk |
| Poor credential configuration | Authentication issues |
| Inconsistent CORS across services | Operational problems |

---

# Hands-on Lab (Conceptual)

Using Developer Tools:

1. Open the Network tab.
2. Visit an application using a cross-origin API.
3. Observe the request and response headers.
4. Identify:
   - Origin
   - Access-Control-Allow-Origin
   - Access-Control-Allow-Methods
   - Access-Control-Allow-Headers
5. Find an example where an OPTIONS preflight request occurs.
6. Compare the preflight request with the subsequent actual request.

---

# Interview Questions

1. What is the purpose of `Access-Control-Allow-Origin`?
2. What is a simple request?
3. What is a preflight request?
4. Why does the browser send an OPTIONS request?
5. What is `Access-Control-Allow-Methods` used for?
6. What is `Access-Control-Allow-Headers`?
7. What is `Access-Control-Allow-Credentials`?
8. Why is `Access-Control-Max-Age` useful?
9. Why shouldn't sensitive APIs use unrestricted wildcard origins?
10. Who decides whether a cross-origin response is exposed to JavaScript?

---

# Best Practices

- Explicitly allow only trusted origins.
- Minimize allowed HTTP methods.
- Permit only required request headers.
- Review credential usage carefully.
- Centralize CORS policy where practical.
- Test browser behavior after deployment.
- Periodically audit CORS configurations.

---

# Common Mistakes

- Treating CORS as an authentication mechanism.
- Allowing every origin unnecessarily.
- Forgetting to review credential behavior.
- Ignoring preflight requests during debugging.
- Configuring inconsistent CORS policies across multiple APIs.

---

# Key Takeaways

- CORS is implemented through HTTP headers exchanged between browsers and servers.
- The browser validates origins, methods, headers, and credentials before exposing responses.
- Simple requests generally proceed directly, while complex requests require a preflight `OPTIONS` request.
- Proper CORS configuration balances functionality with security.
- Enterprise environments often centralize CORS policies through API gateways or reverse proxies.

# 14-CORS.md

# Part 3 — Advanced CORS, Credentials, Preflight Caching, Security Risks, Misconfigurations, Enterprise Architecture, and Secure Design

> **"Most CORS vulnerabilities are not caused by the browser—they are caused by incorrect server configurations that unintentionally trust untrusted origins."**

---

# Learning Objectives

After completing this part, you will understand:

- Credentialed CORS Requests
- Cookies and Authentication
- Preflight Caching
- Origin Reflection
- Dynamic Origin Validation
- Common CORS Misconfigurations
- CORS Security Risks
- Enterprise API Gateways
- Reverse Proxies and CORS
- Secure CORS Design

---

# Credentialed Requests

Some web applications need to include authentication information when making cross-origin requests.

Examples include:

- Session Cookies
- Authentication Tokens
- Client Certificates (where applicable)

Conceptually:

```
Browser

↓

Cross-Origin Request

↓

Credentials Included

↓

Server Validation

↓

Browser CORS Validation

↓

Response
```

---

# Credentials and Browser Security

Credentialed requests require additional browser validation.

```
Cross-Origin Request

↓

Credentials?

↓

Yes

↓

Additional CORS Rules Apply
```

The browser applies stricter rules before exposing responses.

---

# Authentication Flow

```
User

↓

Login

↓

Session Created

↓

Browser Stores Session

↓

Cross-Origin API Request

↓

Authentication Verified

↓

CORS Evaluated
```

Authentication and CORS are independent security mechanisms.

---

# Important Principle

Authentication answers:

```
Who is the user?
```

Authorization answers:

```
What may the user access?
```

CORS answers:

```
May this browser origin read the response?
```

Each solves a different security problem.

---

# Dynamic Origin Validation

Many enterprise applications allow multiple trusted origins.

Conceptually:

```
Incoming Origin

↓

Trusted Origin List

↓

Match?

↓

Yes

↓

Allow

──────────────

No

↓

Reject
```

The server should validate the origin against an approved allowlist.

---

# Origin Reflection

A dangerous configuration pattern is blindly reflecting the incoming origin.

Conceptually:

```
Request

↓

Origin Header

↓

Copied Directly

↓

Response

↓

Potential Security Risk
```

Servers should validate origins before allowing access.

---

# Secure Origin Validation

```
Incoming Origin

↓

Lookup

↓

Approved List

↓

Found?

↓

Yes

↓

Allow

──────────────

No

↓

Deny
```

Explicit allowlists are significantly safer than unrestricted reflection.

---

# Wildcard Origins

Conceptually:

```
*

↓

Every Origin
```

Suitable only for carefully reviewed public resources that do not expose sensitive information.

Sensitive APIs should generally avoid unrestricted wildcard policies.

---

# Credential Rule

When credentials are involved:

```
Trusted Origin

↓

Explicitly Allowed

↓

Credentials

↓

Browser Validation
```

Explicit origin validation is essential.

---

# Preflight Caching

Browsers may cache successful preflight responses.

```
OPTIONS Request

↓

Success

↓

Cache Policy

↓

Future Requests

↓

Reuse Result
```

Caching reduces unnecessary network traffic.

---

# Preflight Cache Lifecycle

```
First Request

↓

Preflight

↓

Success

↓

Cache

↓

Later Request

↓

Reuse Cache
```

Eventually the cache expires and the browser performs another preflight.

---

# Enterprise API Gateway

Many organizations centralize CORS handling.

```
Browser

↓

API Gateway

↓

CORS Validation

↓

Backend Services
```

Centralized policy management improves consistency.

---

# Reverse Proxy Architecture

```
Browser

↓

Reverse Proxy

↓

CORS Policy

↓

Microservices
```

The reverse proxy may apply consistent CORS headers before forwarding requests.

---

# Microservice Environment

```
Customer Portal

↓

Gateway

│

├── Orders API

├── Payment API

├── Inventory API

└── User API
```

Each backend service should follow consistent organizational CORS policies.

---

# Browser Validation Flow

```
Cross-Origin Request

↓

Origin

↓

Method

↓

Headers

↓

Credentials

↓

Browser Decision
```

Every required validation step must succeed before the response becomes available to JavaScript.

---

# Common Misconfiguration 1

## Allowing Every Origin

```
Everyone

↓

Sensitive API

↓

Response Accessible
```

This unnecessarily broad trust model increases exposure.

---

# Common Misconfiguration 2

## Blind Origin Reflection

```
Attacker Origin

↓

Server Reflects Origin

↓

Browser Accepts

↓

Potential Risk
```

Reflection without validation should be avoided.

---

# Common Misconfiguration 3

## Excessive Allowed Methods

Example:

```
GET

POST

PUT

PATCH

DELETE

OPTIONS

...
```

Allow only methods that the application genuinely requires.

---

# Common Misconfiguration 4

## Excessive Allowed Headers

Allowing unnecessary request headers increases configuration complexity and may broaden the attack surface.

Apply the principle of least privilege.

---

# Common Misconfiguration 5

## Inconsistent Policies

```
API A

↓

Restrictive

──────────────

API B

↓

Permissive
```

Inconsistent CORS behavior creates operational confusion and increases the chance of security mistakes.

---

# Least Privilege for CORS

```
Allow

Only

Required

Origins

Methods

Headers

Credentials
```

The least privilege principle applies to CORS just as it does to authorization.

---

# Enterprise Architecture

```
                     Browser

                        │

                 Cross-Origin Request

                        │

                        ▼

                  API Gateway

                        │

            Validate Origin Policy

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

      User API     Billing API    Orders API

                        │

                  Business Logic

                        │

                     Database
```

---

# Security Review Checklist

```
✓ Approved Origin List

✓ Minimal Methods

✓ Minimal Headers

✓ Credential Review

✓ HTTPS Everywhere

✓ API Gateway Policy

✓ Logging Enabled

✓ Configuration Reviewed
```

---

# Logging

Organizations should log:

- Origin values
- CORS policy decisions
- Failed validations
- Preflight requests
- Configuration changes
- Administrative modifications

Logs assist with troubleshooting and security investigations.

---

# Monitoring

Useful operational metrics include:

| Metric | Purpose |
|---------|----------|
| Failed CORS validations | Detect configuration issues |
| Preflight frequency | Measure API behavior |
| Origin distribution | Identify expected clients |
| Credentialed requests | Monitor authentication usage |
| Configuration changes | Detect unauthorized modifications |

---

# Enterprise Example

A multinational retailer deploys:

```
store.company.com

↓

Customer Portal

──────────────

admin.company.com

↓

Administration

──────────────

api.company.com

↓

REST API

──────────────

identity.company.com

↓

Authentication
```

The API Gateway:

- Validates incoming origins
- Applies centralized CORS policies
- Logs CORS decisions
- Supports approved enterprise applications
- Rejects unknown origins

---

# Hands-on Lab (Conceptual)

Using browser Developer Tools:

1. Open the Network panel.
2. Identify requests using credentials.
3. Observe any preflight `OPTIONS` requests.
4. Compare successful and unsuccessful cross-origin requests.
5. Review CORS-related response headers.
6. Document which origins appear to be trusted.

---

# Interview Questions

1. What is a credentialed CORS request?
2. Why must authentication and CORS be treated separately?
3. What is origin reflection?
4. Why is unrestricted wildcard usage risky for sensitive APIs?
5. Why should servers validate origins against an allowlist?
6. What is the purpose of preflight caching?
7. Why do organizations centralize CORS policies?
8. How can reverse proxies simplify CORS management?
9. What operational metrics are useful for monitoring CORS?
10. How does the principle of least privilege apply to CORS?

---

# Best Practices

- Maintain an explicit allowlist of trusted origins.
- Centralize CORS policies using API gateways or reverse proxies where appropriate.
- Apply least privilege to origins, methods, headers, and credentials.
- Review CORS settings during architecture and security reviews.
- Log CORS validation failures and configuration changes.
- Periodically audit trusted origins and remove obsolete entries.
- Keep authentication, authorization, and CORS as separate security controls.

---

# Common Mistakes

- Blindly reflecting the `Origin` header.
- Using unrestricted wildcard policies for sensitive APIs.
- Allowing unnecessary HTTP methods or request headers.
- Assuming CORS replaces authentication or authorization.
- Applying inconsistent CORS policies across services.
- Ignoring failed preflight requests during troubleshooting.

---

# Key Takeaways

- Credentialed CORS requests require stricter browser validation.
- Dynamic origin validation should rely on explicit allowlists rather than blind reflection.
- API gateways and reverse proxies help centralize CORS management.
- Least privilege should guide CORS configuration for origins, methods, headers, and credentials.
- Most CORS vulnerabilities stem from insecure server configuration rather than flaws in the browser.

```text id="jid720"
**Next:** Part 4
```