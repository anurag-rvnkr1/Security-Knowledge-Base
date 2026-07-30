# 18 - API Input Validation

# Introduction

Input validation is the process of verifying that data received by an API conforms to expected formats, types, lengths, ranges, and business rules before it is processed.

Every API should assume that **all external input is untrusted** until validated.

Improper input validation is one of the leading causes of security vulnerabilities, including:

- SQL Injection
- NoSQL Injection
- Command Injection
- XML Injection
- LDAP Injection
- XPath Injection
- Server-Side Template Injection (SSTI)
- Path Traversal
- Cross-Site Scripting (XSS)
- Buffer-related issues
- Business logic abuse

Robust input validation significantly reduces the attack surface of an API.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand input validation fundamentals.
- Identify trust boundaries.
- Learn server-side validation techniques.
- Understand canonicalization.
- Apply allowlist validation.
- Validate data types and formats.
- Validate lengths and ranges.
- Implement schema validation.
- Prevent common injection attacks.
- Design enterprise validation strategies.

---

# Why Input Validation Matters

Without validation

```
Attacker

     │

Malicious Input

     │

Application

     │

Database

     ▼

Compromise
```

With validation

```
Attacker

     │

Malicious Input

     │

Validation Layer

     │

Reject

     ▼

Protected Application
```

---

# Trust Boundaries

A trust boundary separates trusted and untrusted data.

```
Internet

     │

Untrusted Data

     │

API Gateway

     │

Application

     │

Database
```

Everything entering from outside the application's trust boundary must be validated.

---

# Sources of Untrusted Input

Common sources include:

- URL parameters
- Query parameters
- HTTP headers
- JSON request bodies
- XML payloads
- GraphQL variables
- Multipart uploads
- Cookies
- WebSockets
- Third-party APIs
- Message queues

Never assume any external source is trustworthy.

---

# Validation Principles

Effective validation should be:

- Server-side
- Consistent
- Centralized where practical
- Deterministic
- Least permissive
- Independent of client-side validation

---

# Client-Side vs Server-Side Validation

| Client-Side | Server-Side |
|-------------|-------------|
| Improves usability | Provides security |
| Can be bypassed | Required for protection |
| Runs in browser | Runs on server |
| Optional | Mandatory |

Client-side validation enhances user experience but must never replace server-side validation.

---

# Validation Workflow

```
Incoming Request

       │

Parse Input

       │

Validate

       │

Normalize

       │

Business Rules

       │

Process Request
```

Validation should occur before business logic executes.

---

# Fail Securely

If validation fails,

the application should reject the request immediately.

```
Input

 │

Valid?

┌────┴─────┐

▼          ▼

Yes       No

▼          ▼

Process   Reject
```

Avoid attempting to "fix" untrusted input automatically.

---

# Positive Validation (Allowlisting)

Allowlisting defines exactly what is permitted.

Example

```
Username

Allowed

A-Z

a-z

0-9

_

-
```

Everything else is rejected.

Allowlisting is the preferred validation strategy.

---

# Negative Validation (Blocklisting)

Blocklisting rejects known bad values.

Example

```
Reject

<

>

'

"

--
```

Advantages

- Easy to implement

Disadvantages

- Easy to bypass
- Impossible to enumerate every malicious payload

Blocklisting should supplement—not replace—allowlisting.

---

# Allowlist vs Blocklist

| Allowlist | Blocklist |
|-----------|-----------|
| Defines acceptable input | Defines forbidden input |
| More secure | Easier to bypass |
| Recommended | Supplementary |
| Predictable | Incomplete by nature |

---

# Canonicalization

Attackers often encode input to bypass validation.

Examples

```
%2e%2e/

%252e%252e/

UTF-8 Variants

Unicode Encoding
```

Applications should canonicalize input before validation.

---

# Canonicalization Workflow

```
Incoming Data

      │

Decode

      │

Normalize

      │

Validate

      ▼

Process
```

Validation should occur after canonicalization to ensure all equivalent representations are treated consistently.

---

# Data Type Validation

Every field should have an expected type.

Examples

| Field | Expected Type |
|--------|---------------|
| Age | Integer |
| Price | Decimal |
| Email | String |
| Created Date | Date |
| Active | Boolean |

Reject values that do not match the expected type.

---

# Format Validation

Examples

```
Email

user@example.com

-------------------

UUID

550e8400-e29b

-------------------

Phone Number

Country Format
```

Validate using established standards where possible.

---

# Required Fields

```
Request

 │

Missing Required Field?

 │

Yes

 ▼

Reject
```

Mandatory data should never be assumed or silently generated.

---

# Optional Fields

Optional fields should still be validated when present.

Example

```
Middle Name

Optional

↓

If Present

↓

Validate
```

---

# String Length Validation

Example

| Field | Minimum | Maximum |
|--------|---------|---------|
| Username | 3 | 30 |
| Password | 12 | 128 |
| Product Name | 1 | 255 |
| Comment | 1 | 5000 |

Reject overly short or excessively long input.

---

# Numeric Range Validation

Example

```
Age

0

↓

120
```

Example

```
Quantity

1

↓

100
```

Ensure values remain within expected business limits.

---

# Date Validation

Examples

- Valid calendar dates
- Time zone awareness
- Future date restrictions
- Historical limits

Reject malformed or impossible dates.

---

# Enumeration Validation

Some values should come from predefined options.

Example

```
Role

Admin

User

Auditor
```

Unexpected values should be rejected.

---

# Boolean Validation

Expected values

```
true

false
```

Avoid accepting arbitrary representations that may introduce ambiguity.

---

# Regular Expressions

Regular expressions are useful for structured formats.

Examples

- Email addresses
- Phone numbers
- ZIP or postal codes
- Product identifiers

Poorly designed regular expressions may introduce performance issues, including Regular Expression Denial of Service (ReDoS).

---

# Schema Validation

Schemas define the expected structure of input.

```
Incoming JSON

        │

Schema Validation

        │

Valid?

┌───────┴────────┐

▼                ▼

Yes             No

▼                ▼

Process       Reject
```

Schema validation improves consistency and maintainability.

---

# JSON Schema Validation

A schema may define:

- Required properties
- Data types
- Length limits
- Numeric ranges
- Enumerated values
- Nested object structures

Schema validation is commonly used for REST APIs accepting JSON payloads.

---

# XML Schema Validation

XML payloads should be validated against an approved schema before processing.

Benefits

- Structural validation
- Type validation
- Reduced parser ambiguity
- Better interoperability

---

# GraphQL Input Validation

GraphQL schemas define:

- Field types
- Arguments
- Required fields
- Enumerations
- Input objects

Additional business rule validation is still required after schema validation.

---

# File Upload Validation

Uploaded files require validation of:

- File type
- File extension
- MIME type
- File size
- Content where appropriate
- Malware scanning
- Storage location

Never trust the filename or extension alone.

---

# HTTP Header Validation

Validate headers including:

- Authorization
- Content-Type
- Accept
- Custom headers
- Host

Reject unexpected or malformed values.

---

# Query Parameter Validation

Examples

```
limit

1-100

-------------------

page

Positive Integer

-------------------

sort

Allowed Fields Only
```

---

# Path Parameter Validation

Example

```
/users/{id}
```

Validate

- Type
- Length
- Format
- Authorization
- Existence when required

---

# Cookie Validation

Validate

- Cookie format
- Length
- Signature
- Expiration
- Integrity

Never trust client-modified cookie values.

---

# Enterprise Validation Pipeline

```
Internet

     │

API Gateway

     │

Authentication

     │

Input Validation

     │

Business Validation

     │

Authorization

     │

Application Logic

     │

Database
```

Multiple validation layers reduce the likelihood of a single control failure.

---

# Best Practices

Architecture

- Validate all external input.
- Validate as early as practical.
- Centralize reusable validation logic.
- Apply the principle of least privilege.

Development

- Prefer allowlists.
- Use strong data types.
- Validate against schemas.
- Reject invalid input consistently.

Operations

- Log validation failures.
- Monitor abnormal input patterns.
- Review validation rules regularly.
- Include validation tests in CI/CD pipelines.

---

# Common Mistakes

Avoid

- Trusting client-side validation
- Using only blocklists
- Missing length limits
- Ignoring canonicalization
- Weak schema definitions
- Accepting unexpected fields
- Silent correction of invalid data
- Inconsistent validation across services

---

# Key Takeaways

- All external input is untrusted until validated.
- Server-side validation is mandatory.
- Allowlists are generally more secure than blocklists.
- Canonicalization should precede validation.
- Schema validation improves API consistency and security.
- Input validation forms the foundation for preventing many injection attacks.

---

**Next:** Advanced validation techniques, business rule validation, injection prevention, detection engineering, SIEM integration, hands-on labs, troubleshooting, and interview questions.