# A01:2021 – Broken Access Control

---

# Overview

**Broken Access Control** is the **#1 risk in the OWASP Top 10 (2021)** and one of the most common and dangerous vulnerabilities found in modern web applications.

Access control determines **who is allowed to access specific resources** and **what actions they are permitted to perform** after authentication.

When access control is improperly implemented or completely absent, attackers can bypass authorization checks and gain access to data or functionality they should never be able to reach.

Unlike **authentication**, which answers **"Who are you?"**, **authorization** answers **"What are you allowed to do?"**

Broken Access Control occurs when the application fails to correctly enforce authorization policies, allowing users to perform unauthorized actions.

Examples include:

- Viewing another user's profile
- Downloading confidential documents
- Modifying another user's account
- Deleting records without permission
- Accessing administrator pages
- Reading internal application files
- Changing application settings

OWASP reports that **Broken Access Control appears in more applications than any other OWASP category**, making it the most prevalent web security risk.

---

# Why It Matters

Improper access control can completely compromise an application's security.

An attacker may not need sophisticated exploits such as SQL Injection or Remote Code Execution. Instead, they simply manipulate requests to access resources that the server fails to protect.

The impact can include:

- Unauthorized data disclosure
- Financial fraud
- Account takeover
- Administrative access
- Privacy violations
- Regulatory non-compliance
- Business logic abuse
- Reputation damage

For example:

Imagine an online banking application where account statements are retrieved using:

```
GET /statement?id=1001
```

If changing the request to:

```
GET /statement?id=1002
```

returns another customer's statement without authorization checks, the application suffers from **Broken Access Control**, specifically an **Insecure Direct Object Reference (IDOR)**.

---

# Authentication vs Authorization

Many beginners confuse these concepts.

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Verifies permissions |
| "Who are you?" | "What can you do?" |
| Login | Access Control |
| Username & Password | Roles & Permissions |
| Session Creation | Permission Validation |

Example:

```
User:
Alice

Authentication:
✔ Logged in successfully

Authorization:
✔ Can view her profile
✔ Can edit her profile
✘ Cannot delete users
✘ Cannot access admin dashboard
```

Authentication happens **before** authorization.

A user can be successfully authenticated while still having very limited permissions.

---

# Access Control Fundamentals

Access control consists of rules that determine whether a request should be allowed.

Every request should answer three questions:

```
Who is making the request?

↓

What resource is being requested?

↓

Does this user have permission?
```

If any authorization check is skipped, Broken Access Control becomes possible.

---

# Authorization Flow

```
           Client
              │
              │
      Login Request
              │
              ▼
+--------------------------+
| Authentication Service   |
+--------------------------+
              │
       Identity Verified
              │
              ▼
+--------------------------+
| Authorization Layer      |
+--------------------------+
              │
     Permission Check
              │
      ┌───────┴────────┐
      │                │
      ▼                ▼
 Allowed           Access Denied
      │
      ▼
 Requested Resource
```

A secure application performs authorization checks **on every protected request**, not only during login.

---

# Architecture / Diagram

## Example Secure Architecture

```
             User
               │
               ▼
         Login Request
               │
               ▼
     Authentication Server
               │
        Valid Credentials
               │
               ▼
      Authorization Engine
               │
        Check Permissions
               │
      ┌────────┴─────────┐
      │                  │
      ▼                  ▼
 Allowed             Forbidden
      │
      ▼
 Application Resource
```

---

## Insecure Architecture

```
User
 │
 ▼
Login

 │
 ▼
Application

 │
 ▼
Sensitive Resource

(No Authorization Check)

Result:

Every authenticated user
can access sensitive data.
```

This is one of the most common design mistakes in web applications.

---

# Key Concepts

Understanding Broken Access Control requires familiarity with several authorization concepts.

---

## Subject

The entity requesting access.

Examples:

- User
- Administrator
- Service Account
- API Client
- Mobile Application

---

## Object

The resource being accessed.

Examples:

- Profile
- Order
- Invoice
- API Endpoint
- Image
- Database Record
- Configuration File

---

## Action

The operation requested.

Examples:

- Read
- Write
- Update
- Delete
- Execute
- Upload
- Download

---

## Policy

The rule defining who can perform which action.

Example:

```
Customer

Can:
✔ View own orders

Cannot:
✘ Delete products
✘ Manage users
```

---

## Permission

A permission represents a specific capability.

Examples:

```
VIEW_PROFILE

EDIT_PROFILE

DELETE_POST

CREATE_USER

EXPORT_REPORT

READ_INVOICE
```

Applications often combine multiple permissions into roles.

---

## Role

A role is a collection of permissions.

Example:

```
Admin

├── Create Users
├── Delete Users
├── Manage Products
├── View Reports
├── Configure System
└── Reset Passwords
```

```
Customer

├── View Profile
├── Edit Profile
├── Place Order
└── View Orders
```

---

## Principle of Least Privilege

One of the most important security principles.

Users should receive **only the minimum permissions required** to perform their tasks.

Instead of:

```
Employee

Everything Allowed
```

Use:

```
Employee

✔ Read Documents

✔ Submit Requests

✔ Update Own Profile

✘ Access Payroll

✘ Delete Employees

✘ Change System Settings
```

Least privilege significantly reduces the impact of compromised accounts.

---

# Common Indicators of Broken Access Control

Security testers often look for patterns such as:

- Sequential numeric IDs (`/user/1001`, `/user/1002`)
- Hidden admin URLs
- Client-side role checks only
- Missing authorization middleware
- Direct object references
- Predictable resource identifiers
- File path manipulation
- Parameter tampering
- JWT role modification
- API endpoints lacking permission validation

These indicators often suggest authorization weaknesses that require further testing.

---

# Key Takeaways

- Broken Access Control is the **#1 OWASP Top 10 (2021)** risk.
- Authentication verifies **identity**, while authorization verifies **permissions**.
- Every request to a protected resource must be authorized.
- Roles, permissions, and policies work together to enforce access control.
- Applying the **Principle of Least Privilege** is one of the most effective ways to reduce authorization-related risks.
- Missing or inconsistent authorization checks can lead to data exposure, privilege escalation, and full application compromise.

# Types of Broken Access Control

Broken Access Control can appear in many different forms. Although the root cause is always the same—**the application fails to properly enforce authorization**—the way attackers exploit it varies.

Understanding these attack patterns is essential for penetration testers, developers, and security engineers.

---

# 1. Vertical Privilege Escalation

## Overview

Vertical Privilege Escalation occurs when a lower-privileged user gains access to functionality reserved for higher-privileged users.

The attacker moves **up** the privilege hierarchy.

For example:

```
Guest
   │
   ▼
Customer
   │
   ▼
Manager
   │
   ▼
Administrator
```

A normal user should never be able to reach administrator functions.

---

## Example

Application roles:

```
Admin

├── Add Users
├── Delete Users
├── View Reports
└── Manage Payments
```

```
Normal User

├── View Profile
├── Edit Profile
└── Place Orders
```

Suppose the admin dashboard is available at:

```
https://example.com/admin
```

A regular user manually enters:

```
https://example.com/admin
```

If the page loads successfully, the application suffers from **Vertical Privilege Escalation**.

---

## Example HTTP Request

```
GET /admin HTTP/1.1
Host: example.com
Cookie: session=user123
```

Expected Response:

```
HTTP/1.1 403 Forbidden
```

Vulnerable Response:

```
HTTP/1.1 200 OK

Welcome Administrator
```

---

## Impact

An attacker may gain the ability to:

- Delete users
- Reset passwords
- View confidential records
- Modify system settings
- Access financial information
- Disable security controls

---

# 2. Horizontal Privilege Escalation

## Overview

Horizontal Privilege Escalation occurs when a user accesses another user’s resources while remaining at the same privilege level.

The attacker moves **sideways**, not upward.

Example:

```
Alice  →  Bob
```

Both are ordinary users.

Neither should access the other's information.

---

## Example

Alice logs in.

Profile request:

```
GET /profile?id=1001
```

She changes the request:

```
GET /profile?id=1002
```

If Bob's profile appears:

```
Alice

↓

Changes ID

↓

Bob's Profile
```

This is Horizontal Privilege Escalation.

---

## Impact

Possible consequences include:

- Reading private messages
- Viewing invoices
- Accessing medical records
- Downloading documents
- Modifying another user's account
- Deleting another user's data

---

# 3. Insecure Direct Object Reference (IDOR)

## Overview

IDOR is one of the most common forms of Broken Access Control.

The application exposes internal object identifiers and fails to verify ownership.

Examples of identifiers include:

- User IDs
- Order IDs
- Invoice numbers
- File names
- Employee IDs
- UUIDs (if ownership isn't checked)

---

## Vulnerable Example

Alice requests:

```
GET /invoice/5001
```

Response:

```
Invoice belongs to Alice
```

She changes:

```
GET /invoice/5002
```

Server responds:

```
Invoice belongs to Bob
```

No authorization check was performed.

---

## Secure Logic

Instead of trusting the ID:

```
Invoice ID

↓

Check

↓

Does logged-in user own it?

↓

Yes → Return Invoice

No → 403 Forbidden
```

Never assume that an object ID alone proves authorization.

---

# 4. Forced Browsing

## Overview

Forced Browsing occurs when users directly request hidden URLs that are not linked in the application's interface.

Developers sometimes believe that hiding a link is enough to protect a resource.

It is not.

---

## Example

Visible pages:

```
/

↓

/products

↓

/contact
```

Hidden page:

```
/admin/dashboard
```

Attacker guesses:

```
https://example.com/admin/dashboard
```

If the server does not enforce authorization, the attacker gains access.

---

## Common Discovery Methods

Attackers use:

- Directory brute forcing
- Search engines
- Robots.txt
- JavaScript files
- Browser history
- Source code
- Burp Suite
- ffuf
- Gobuster
- dirsearch

---

# 5. Parameter Tampering

## Overview

Applications often rely on parameters such as:

```
role=user

user_id=10

price=100

account=1001
```

If these values determine authorization without server-side validation, attackers can modify them.

---

## Example

Original request:

```
POST /profile

role=user
```

Modified request:

```
POST /profile

role=admin
```

If accepted, the application has failed to validate authorization.

---

## Another Example

```
GET /download?file=report.pdf
```

Attacker changes:

```
GET /download?file=salary.xlsx
```

Without validation, confidential files become accessible.

---

# 6. File Access Vulnerabilities

Applications often store files using predictable names.

Example:

```
resume1.pdf

resume2.pdf

resume3.pdf
```

An attacker may request:

```
GET /uploads/resume2.pdf
```

If ownership isn't checked, private documents become public.

---

## Secure Workflow

```
Request File

↓

Check Authentication

↓

Check Ownership

↓

Allow or Deny
```

Never rely solely on file names or paths for authorization.

---

# 7. HTTP Method Manipulation

Some applications secure only one HTTP method.

Example:

```
GET /admin/deleteUser
```

Blocked.

However:

```
POST /admin/deleteUser
```

Allowed.

Or:

```
PUT

PATCH

DELETE
```

Developers sometimes forget to secure all supported methods.

Every HTTP method accessing a protected resource must enforce the same authorization rules.

---

# 8. JWT Role Manipulation

Applications using JSON Web Tokens (JWTs) may include user roles in the token payload.

Example payload:

```json
{
  "user": "alice",
  "role": "user"
}
```

If the application:

- Accepts unsigned tokens (`alg: none`)
- Uses weak signing keys
- Fails to verify signatures

an attacker may change:

```json
{
  "role": "admin"
}
```

If the modified token is accepted, the attacker gains elevated privileges.

**Important:** Merely changing the payload is **not sufficient** when JWTs are correctly signed and verified. The vulnerability arises from improper token validation or insecure implementation.

---

# 9. API Authorization Issues

Modern APIs are frequent targets of Broken Access Control.

Example:

```
GET /api/users/1001
```

Attacker changes:

```
GET /api/users/1002
```

If another user's data is returned:

```
Broken Object Level Authorization (BOLA)
```

This is one of the most common API vulnerabilities and is a major focus of the **OWASP API Security Top 10**.

---

# Attack Flow

```
Attacker

      │

      ▼

Login

      │

      ▼

Intercept Request

      │

      ▼

Modify ID

      │

      ▼

Server Receives Request

      │

(No Ownership Check)

      ▼

Sensitive Data Returned
```

---

# Common Root Causes

Broken Access Control often results from:

- Missing server-side authorization checks
- Trusting client-side validation
- Exposing predictable object identifiers
- Inconsistent permission enforcement
- Hidden functionality without access checks
- Weak role validation
- Missing ownership verification
- Insecure default configurations
- Improper API authorization

---

# Key Takeaways

- **Vertical Privilege Escalation** allows a user to gain higher-level privileges.
- **Horizontal Privilege Escalation** allows a user to access another user's resources.
- **IDOR** is one of the most common manifestations of Broken Access Control.
- Hidden URLs are **not** secure unless protected by server-side authorization.
- Client-supplied parameters must never be trusted for authorization decisions.
- Every request to a protected resource should undergo authentication (if required) **and** authorization checks.
- Modern APIs require strict object-level and function-level authorization to prevent unauthorized access.

# Real-World Examples of Broken Access Control

Understanding how Broken Access Control has been exploited in real systems helps illustrate why it is the highest-ranked OWASP risk.

---

# Example 1: Insecure Direct Object Reference (IDOR)

## Scenario

An e-commerce application allows users to download invoices.

Request:

```http
GET /invoice/1025 HTTP/1.1
Host: shop.example.com
Cookie: session=abc123
```

The application responds:

```
Invoice #1025
Owner: Alice
```

An attacker changes the URL:

```http
GET /invoice/1026 HTTP/1.1
```

The server responds:

```
Invoice #1026
Owner: Bob
```

The application failed to verify that the authenticated user actually owns invoice **1026**.

---

## Root Cause

The application trusted the object identifier.

Instead of checking:

```
Current User

↓

Does user own invoice 1026?

↓

Yes → Return

No → 403 Forbidden
```

it simply queried:

```sql
SELECT * FROM invoices
WHERE id = 1026;
```

without validating ownership.

---

## Impact

Possible exposure:

- Customer information
- Addresses
- Payment details
- Purchase history
- Tax documents

---

# Example 2: Admin Panel Exposure

Suppose an administrator dashboard exists at:

```
https://example.com/admin
```

The application hides the link from regular users.

However, hiding a link does **not** secure the resource.

A user manually browses to:

```
https://example.com/admin
```

If the server returns:

```
HTTP 200 OK
```

instead of

```
HTTP 403 Forbidden
```

the application is vulnerable.

---

# Example 3: API Authorization Failure

Modern applications expose REST APIs.

Example request:

```http
GET /api/orders/5001
Authorization: Bearer <JWT>
```

Attacker changes:

```http
GET /api/orders/5002
```

If order **5002** belongs to another customer but is still returned, the API lacks object-level authorization.

This is commonly referred to as **Broken Object Level Authorization (BOLA)**.

---

# Example 4: File Download Vulnerability

Application:

```
GET /download?file=resume.pdf
```

Attacker changes:

```
GET /download?file=salary.xlsx
```

If confidential files are downloaded without authorization, access control has failed.

---

# Example 5: Role Manipulation

Suppose an application sends:

```json
{
    "role":"user"
}
```

The frontend hides the "Admin" button.

However, the attacker directly sends:

```
POST /admin/deleteUser
```

If the backend performs **no server-side role verification**, administrative functionality becomes available.

Remember:

> **Never rely on the client (browser, mobile app, or JavaScript) to enforce authorization.**

---

# Detecting Broken Access Control

Broken Access Control often cannot be discovered through automated scanners alone.

Manual testing is essential.

A tester should attempt to perform actions that should **not** be allowed.

---

# Detection Methodology

```
Login

↓

Capture Request

↓

Modify Request

↓

Replay Request

↓

Observe Response

↓

Unauthorized Access?

↓

Yes → Vulnerable
```

---

# Manual Testing Checklist

## 1. Test Object IDs

Original request:

```
GET /profile?id=1001
```

Modify:

```
GET /profile?id=1002
```

Questions:

- Can another user's data be viewed?
- Can another user's data be modified?
- Can another user's data be deleted?

---

## 2. Test Hidden URLs

Examples:

```
/admin

/dashboard

/config

/manage

/internal

/debug

/console
```

Expected:

```
403 Forbidden
```

---

## 3. Test HTTP Methods

Original:

```
GET /users/delete
```

Try:

```
POST

PUT

PATCH

DELETE
```

Some applications secure only one method.

---

## 4. Test Role Changes

Login as:

```
Regular User
```

Attempt to:

- Delete users
- View reports
- Access admin APIs
- Export sensitive data

---

## 5. Test API Endpoints

Example:

```
GET /api/user/10
```

Modify:

```
GET /api/user/11
```

Observe:

- Status code
- Returned JSON
- Error messages

---

# Using Burp Suite

Burp Suite is one of the best tools for testing authorization.

---

## Step 1

Configure browser proxy.

```
Browser

↓

Burp Proxy

↓

Application
```

---

## Step 2

Login normally.

---

## Step 3

Capture requests.

Example:

```
GET /profile?id=25
```

---

## Step 4

Send request to Repeater.

```
Proxy

↓

Right Click

↓

Send to Repeater
```

---

## Step 5

Modify values.

Examples:

```
id=26

↓

id=27

↓

id=28
```

Observe responses.

---

## Step 6

Test privileges.

Login as:

```
User A
```

Capture request.

Replace session cookie with:

```
User B
```

Observe differences.

---

# Burp Suite Features

Useful modules:

- Proxy
- Repeater
- Intruder
- Comparer
- Decoder

Repeater is especially valuable for authorization testing because it allows controlled modification of requests.

---

# Detection Using OWASP WSTG

The OWASP Web Security Testing Guide recommends testing:

- Directory traversal permissions
- Forced browsing
- IDOR
- Authorization bypass
- Role validation
- Session handling
- File permissions
- Administrative functions
- API authorization
- Business logic restrictions

---

# Automated Detection

Automated scanners can help identify potential authorization issues but often produce false positives or miss complex business logic flaws.

Tools that may assist include:

- OWASP ZAP
- Burp Suite Scanner (Professional)
- Nessus (limited for application logic)
- Nuclei (specific templates)
- Custom API security tests

Manual verification is always required.

---

# Common Indicators

Watch for:

- Sequential IDs
- UUIDs accepted without ownership checks
- Hidden admin pages
- Missing `403 Forbidden` responses
- Access based solely on client-side controls
- Sensitive endpoints lacking authorization middleware
- Excessive data returned by APIs
- Predictable file names

---

# Security Testing Tips

- Test with multiple user accounts.
- Compare responses between different privilege levels.
- Verify every sensitive endpoint individually.
- Test both the web interface and underlying APIs.
- Do not assume hidden functionality is protected.
- Re-test after authentication state changes (login/logout, role changes).

---

# Key Takeaways

- Broken Access Control is primarily identified through **manual authorization testing**.
- Changing object identifiers, URLs, HTTP methods, roles, and session tokens are common testing techniques.
- Burp Suite Repeater is one of the most effective tools for validating authorization controls.
- Automated tools can assist, but they cannot replace careful manual analysis of application behavior.

# Prevention

Preventing Broken Access Control requires implementing authorization as a **server-side security mechanism** rather than relying on client-side restrictions.

A secure application should enforce authorization checks for **every request** to protected resources.

---

# Core Security Principles

## 1. Deny by Default

The safest approach is to deny access unless it is explicitly permitted.

❌ Insecure

```
if(user != null)
    allow();
```

✅ Secure

```
if(user.hasPermission("VIEW_REPORT"))
    allow();
else
    deny();
```

---

## 2. Verify Authorization on Every Request

Never assume that because a user has logged in once, every future request is authorized.

Every request should follow this flow:

```
Client Request
       │
       ▼
Authentication
       │
       ▼
Authorization
       │
       ▼
Resource
```

Skipping the authorization step creates security vulnerabilities.

---

## 3. Never Trust the Client

Everything coming from the browser can be modified.

Never trust:

- Hidden fields
- Cookies
- JavaScript variables
- User IDs
- Role values
- API parameters
- HTTP headers

Example:

```
role=admin
```

The server must independently verify the user's actual role instead of trusting the request.

---

## 4. Enforce Ownership Checks

When accessing user-specific resources:

❌ Vulnerable

```sql
SELECT * FROM invoices
WHERE invoice_id = 1001;
```

✅ Secure

```sql
SELECT *
FROM invoices
WHERE invoice_id = 1001
AND owner_id = CURRENT_USER;
```

Even if an attacker changes the invoice ID, the query returns only records they own.

---

## 5. Use Role-Based Access Control (RBAC)

Instead of checking permissions everywhere manually, assign permissions through roles.

Example:

```
Administrator

├── Create User
├── Delete User
├── Manage Roles
└── View Reports
```

```
Manager

├── View Reports
├── Edit Orders
└── Approve Requests
```

```
Customer

├── View Orders
├── Edit Profile
└── Checkout
```

---

## 6. Apply the Principle of Least Privilege

Grant users only the permissions required for their responsibilities.

Avoid giving broad administrative rights when limited permissions are sufficient.

---

# Secure Coding Examples

## Python (Django)

```python
from django.http import HttpResponseForbidden

def view_invoice(request, invoice_id):
    invoice = Invoice.objects.filter(
        id=invoice_id,
        owner=request.user
    ).first()

    if not invoice:
        return HttpResponseForbidden("Access Denied")

    return render(request, "invoice.html", {
        "invoice": invoice
    })
```

The query automatically ensures that users can access only their own invoices.

---

## Java (Spring Boot)

```java
@GetMapping("/invoice/{id}")
public ResponseEntity<?> getInvoice(
        @PathVariable Long id,
        Principal principal) {

    Invoice invoice =
        invoiceRepository.findById(id);

    if(invoice == null)
        return ResponseEntity.notFound().build();

    if(!invoice.getOwner()
        .equals(principal.getName())) {

        return ResponseEntity
            .status(HttpStatus.FORBIDDEN)
            .build();
    }

    return ResponseEntity.ok(invoice);
}
```

---

## Node.js (Express)

```javascript
app.get("/invoice/:id", async (req, res) => {

    const invoice =
        await Invoice.findById(req.params.id);

    if(!invoice)
        return res.sendStatus(404);

    if(invoice.owner !== req.user.id)
        return res.sendStatus(403);

    res.json(invoice);

});
```

---

# Best Practices

✔ Validate authorization on every request.

✔ Use centralized authorization middleware.

✔ Follow the Principle of Least Privilege.

✔ Implement Role-Based Access Control (RBAC).

✔ Consider Attribute-Based Access Control (ABAC) for complex systems.

✔ Never expose sensitive functionality without authentication and authorization.

✔ Validate ownership of every user-specific resource.

✔ Log unauthorized access attempts.

✔ Review access control rules during code reviews.

✔ Perform regular penetration testing.

✔ Test APIs separately from the web interface.

✔ Remove unused administrative endpoints.

✔ Protect internal APIs.

✔ Return appropriate HTTP status codes (`401`, `403`, `404`).

✔ Regularly audit roles and permissions.

---

# Useful Commands

## Directory Enumeration

```bash
ffuf -u https://example.com/FUZZ \
-w /usr/share/wordlists/dirb/common.txt
```

---

## Gobuster

```bash
gobuster dir \
-u https://example.com \
-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

---

## cURL

```bash
curl \
-H "Authorization: Bearer TOKEN" \
https://example.com/api/user/10
```

---

## Compare Different Users

```bash
curl \
-H "Cookie: session=userA"
```

Compare with

```bash
curl \
-H "Cookie: session=userB"
```

---

# Practical Lab

## Objective

Identify an IDOR vulnerability using **OWASP Juice Shop**.

---

## Steps

### Step 1

Log in as a normal user.

---

### Step 2

Open Burp Suite.

Enable proxy interception.

---

### Step 3

Navigate to:

```
Order History
```

Capture the request.

---

### Step 4

Send the request to **Repeater**.

---

### Step 5

Modify:

```
Order ID
```

or

```
User ID
```

Observe whether another user's data is returned.

---

### Step 6

Record:

- Original request
- Modified request
- Response
- Impact
- Mitigation

---

## Expected Learning Outcomes

You should understand:

- How authorization works
- Why object ownership matters
- How Burp Suite assists manual testing
- Why server-side validation is essential

---

# Interview Questions

## Beginner

### What is Broken Access Control?

**Answer:**

A vulnerability where users can access resources or perform actions beyond their intended permissions because authorization checks are missing or improperly implemented.

---

### Difference between Authentication and Authorization?

Authentication verifies identity.

Authorization determines permissions.

---

### What is IDOR?

IDOR (Insecure Direct Object Reference) occurs when an application exposes object identifiers and fails to verify that the requesting user is authorized to access the referenced object.

---

### What is Vertical Privilege Escalation?

A lower-privileged user gains access to higher-privileged functionality, such as an admin dashboard.

---

### What is Horizontal Privilege Escalation?

A user accesses another user's resources while remaining at the same privilege level.

---

## Intermediate

### Why is Broken Access Control ranked #1 in OWASP Top 10 (2021)?

Because it is one of the most widespread vulnerabilities across modern applications and can lead to severe consequences, including data breaches, privilege escalation, and unauthorized access.

---

### How would you test for Broken Access Control?

- Test different user roles.
- Modify object IDs.
- Browse hidden endpoints.
- Manipulate HTTP methods.
- Test API authorization.
- Use Burp Suite Repeater for request modification.
- Verify that unauthorized requests receive appropriate responses (e.g., `403 Forbidden`).

---

### Why is client-side authorization insecure?

Because attackers can modify client-side code, requests, and parameters. Authorization decisions must always be enforced on the server.

---

## Advanced

### Explain RBAC and ABAC.

**RBAC (Role-Based Access Control):** Permissions are grouped into roles (e.g., Admin, Manager, User), and users inherit permissions based on their assigned role.

**ABAC (Attribute-Based Access Control):** Access decisions are made dynamically using attributes such as user role, department, location, time of day, resource sensitivity, or device type. ABAC offers finer-grained and more flexible control than RBAC.

---

### How can microservices complicate access control?

Each service must consistently enforce authorization. If one service omits or incorrectly implements access checks, attackers may bypass controls through internal APIs or service-to-service communication.

---

### How do JWTs relate to Broken Access Control?

JWTs can carry user identity and role information. If the server fails to validate JWT signatures, trusts client-modified claims, or makes authorization decisions based solely on unverified token contents, attackers may gain unauthorized privileges.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP Web Security Testing Guide (WSTG)
- OWASP Application Security Verification Standard (ASVS)
- OWASP Cheat Sheet Series
- OWASP Juice Shop
- OWASP WebGoat

## MITRE

- CWE-284: Improper Access Control
- CWE-639: Authorization Bypass Through User-Controlled Key
- CWE-285: Improper Authorization

## Standards

- NIST SP 800-53
- NIST Cybersecurity Framework (CSF)
- ISO/IEC 27001
- CIS Controls

---

# Summary

Broken Access Control is the most prevalent and impactful web application security risk in the OWASP Top 10 (2021). It arises when applications fail to properly enforce authorization, allowing users to access resources or perform actions beyond their intended permissions.

By implementing server-side authorization checks, validating resource ownership, applying the Principle of Least Privilege, using RBAC or ABAC, and conducting regular security testing, organizations can significantly reduce the risk of unauthorized access and protect sensitive data.