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

# Business Rule Validation

Technical validation ensures that data is syntactically correct.

Business rule validation ensures that data is logically correct according to organizational requirements.

Example

```
Age = 25

↓

Valid Integer

↓

Technical Validation Passed

────────────────────────────

Minimum Age = 18

↓

Business Rule Passed
```

Both validation layers are necessary.

---

# Technical Validation vs Business Validation

| Technical Validation | Business Validation |
|----------------------|---------------------|
| Data type | Business policy |
| String length | User permissions |
| Numeric range | Account balance |
| JSON structure | Product availability |
| Required fields | Organizational workflow |

Technical validation alone cannot prevent business logic abuse.

---

# Validation Layers

```
Incoming Request

        │

Syntax Validation

        │

Schema Validation

        │

Business Validation

        │

Authorization

        │

Application Logic

        ▼

Database
```

Each layer protects against different classes of attacks.

---

# Business Rule Examples

Examples include:

- Account balance cannot become negative.
- Discount cannot exceed approved limits.
- User cannot approve their own expense.
- Order quantity cannot exceed inventory.
- Withdrawal cannot exceed daily limit.
- Administrator cannot delete the final administrator account.

---

# Example: Banking API

```
Transfer Request

        │

Amount = ₹50,000

        │

Account Balance

₹30,000

        ▼

Reject
```

Although the amount is a valid number,

the transaction violates business rules.

---

# Example: Inventory API

```
Order Quantity

↓

500

↓

Inventory

↓

120 Available

↓

Reject
```

---

# Example: Employee Leave System

```
Requested Leave

20 Days

↓

Remaining Balance

10 Days

↓

Reject
```

Business validation prevents inconsistent application state.

---

# Example: Role Assignment

```
Current User

Employee

        │

Assign Role

Administrator

        ▼

Reject
```

Authorization and business validation often work together.

---

# Business Logic Abuse

Attackers increasingly target application logic instead of software vulnerabilities.

Examples

- Coupon reuse
- Loyalty point abuse
- Inventory hoarding
- Reward manipulation
- Pricing manipulation
- Workflow bypass

```
Legitimate Feature

        │

Unexpected Usage

        │

Business Loss
```

---

# Duplicate Request Validation

Repeated requests may create unintended actions.

```
Payment

↓

Retry

↓

Duplicate Charge
```

Applications should identify duplicate transactions where appropriate.

---

# Idempotency

Certain operations should produce the same result when repeated.

```
Client

      │

POST

      │

Idempotency Key

      ▼

API

      │

Already Processed?

 ┌────┴─────┐

 ▼          ▼

Yes        No

 ▼          ▼

Return     Process
Existing
```

Idempotency keys help prevent accidental duplicate processing.

---

# Replay Protection

Attackers may replay legitimate requests.

```
Captured Request

       │

Replay

       │

API

       ▼

Unauthorized Duplicate Action
```

Mitigations include

- Nonces
- Timestamps
- Idempotency keys
- Short-lived tokens

---

# Input Normalization

Equivalent values should be normalized before validation.

Examples

```
ADMIN

Admin

admin
```

↓

```
admin
```

Normalization reduces inconsistencies.

---

# Unicode Considerations

Unicode introduces multiple representations of visually similar characters.

Example

```
Latin A

Α

Cyrillic А

A
```

Applications should normalize Unicode where appropriate before validation and comparison.

---

# Null Handling

Applications should explicitly define how null values are treated.

Example

```
Email

NULL

↓

Allowed?

↓

Decision
```

Implicit assumptions frequently create logic errors.

---

# Empty Values

Different values may not be equivalent.

```
NULL

≠

""

≠

Whitespace
```

Each should be handled intentionally.

---

# Nested Object Validation

Complex JSON structures require recursive validation.

```
Order

 │

Customer

 │

Address

 │

Country

 │

Postal Code
```

Every nested field should be validated independently.

---

# Array Validation

Validate

- Maximum size
- Minimum size
- Element types
- Duplicate values
- Business limits

Example

```
Items

↓

Maximum

100 Entries
```

---

# Unexpected Fields

Reject unnecessary fields whenever possible.

Example

Expected

```
username

email

password
```

Unexpected

```
isAdmin=true
```

Rejecting unknown fields helps prevent mass assignment vulnerabilities.

---

# Mass Assignment Protection

Mass assignment occurs when clients control fields that should be managed by the server.

```
Client

↓

"isAdmin": true

↓

ORM

↓

Database
```

Mitigations

- Explicit allowlists
- DTOs (Data Transfer Objects)
- Ignore unknown properties
- Separate internal and external models

---

# Numeric Precision

Financial applications require careful handling of numeric precision.

Example

```
Price

₹199.99
```

Floating-point precision errors may affect calculations.

Prefer fixed-precision or decimal data types for financial values.

---

# Overflow and Underflow

Validate numerical boundaries.

```
Maximum

↓

Allowed Integer

↓

Overflow?

↓

Reject
```

Unexpected numeric behavior may produce security or stability issues.

---

# File Path Validation

Applications should never trust user-supplied paths.

Example

```
../../../etc/passwd
```

Validate

- Allowed directories
- Canonical paths
- File ownership
- Access permissions

---

# Content-Type Validation

Validate incoming content types.

Expected

```
application/json
```

Unexpected

```
text/html

application/xml

multipart/*
```

Reject unsupported media types.

---

# Accept Header Validation

Applications should only produce supported response formats.

```
Accept

↓

application/json
```

Unexpected or unsupported formats should return an appropriate error.

---

# Secure Parsing

Before validation,

input must be parsed safely.

Examples

- JSON parser
- XML parser
- Multipart parser
- YAML parser

Parser configuration should disable unsafe features where applicable.

---

# Parser Security

Secure parser configuration should:

- Reject malformed input
- Limit recursion depth
- Limit nesting
- Limit payload size
- Prevent excessive memory usage

---

# Resource Exhaustion

Validation should protect against oversized input.

```
100 MB JSON

↓

Validation Layer

↓

Reject

↓

Application Protected
```

Maximum payload sizes should be enforced before parsing where possible.

---

# Validation Error Handling

Applications should provide consistent error responses.

Example

```
HTTP 400

Bad Request
```

Avoid exposing

- Stack traces
- SQL queries
- Framework internals
- File paths

---

# Secure Error Response

Example

```
HTTP/1.1 400 Bad Request

{
  "error": "Invalid request.",
  "code": "VALIDATION_FAILED"
}
```

Detailed diagnostic information should remain in server logs rather than client responses.

---

# Logging Validation Failures

Useful information includes

- Timestamp
- Source IP
- User identifier
- Endpoint
- Validation rule
- Request ID
- Correlation ID

Do not log sensitive data such as passwords or authentication tokens.

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Excessive Validation Failures | Repeated HTTP 400 responses |
| Type Confusion Attempts | Invalid data types across multiple fields |
| Oversized Payloads | Requests exceeding configured limits |
| Unexpected Fields | Unknown JSON properties submitted repeatedly |
| Invalid Content Types | Unsupported media types |
| Enumeration Attempts | Sequential invalid identifiers |
| Path Traversal Attempts | Directory traversal patterns |
| Malformed JSON | High volume of parsing failures |
| Schema Violations | Repeated schema validation failures |
| Business Rule Abuse | Repeated rejected business transactions |

---

# SIEM Integration

Collect logs from

- API Gateway
- Validation Framework
- Application Server
- Authentication Service
- WAF
- Reverse Proxy

```
Incoming Requests

        │

Validation Events

        │

Structured Logs

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
Repeated Validation Failures

        │

Path Traversal Patterns

        │

Authentication Attempts

        ▼

Potential Reconnaissance
```

Rule 2

```
Oversized Payload

        │

JSON Parsing Failure

        │

Repeated Requests

        ▼

Potential DoS Attempt
```

Rule 3

```
Unexpected Fields

        │

Privilege Escalation Attempt

        │

Authorization Failure

        ▼

Mass Assignment Investigation
```

---

# Enterprise Validation Architecture

```
                   Internet

                      │

                      ▼

               DDoS Protection

                      │

                      ▼

             Web Application Firewall

                      │

                      ▼

                 API Gateway

          ┌───────────┼────────────┐

          ▼           ▼            ▼

 Authentication  Rate Limiting  Logging

                      │

                      ▼

             Validation Framework

      ┌───────────────┼────────────────┐

      ▼               ▼                ▼

 Syntax         Schema Validation  Business Rules

                      │

                      ▼

                Authorization

                      │

                      ▼

               Application Logic

                      │

                      ▼

                  Database

                      │

                      ▼

                 SIEM / SOC
```

---

# Hands-on Lab 1 – Schema Validation

**Objective**

Evaluate JSON schema validation.

**Steps**

1. Submit a valid JSON request.
2. Remove required properties.
3. Change data types.
4. Observe validation responses.
5. Review application logs.

**Learning Outcomes**

- Schema validation
- Type enforcement
- Error handling

---

# Hands-on Lab 2 – Business Rule Validation

**Objective**

Verify business rule enforcement.

**Steps**

1. Submit a valid transaction.
2. Attempt to exceed defined business limits.
3. Review validation results.
4. Confirm that invalid requests are rejected without affecting application state.

**Learning Outcomes**

- Business rule validation
- Transaction integrity
- Secure application behavior

---

# Hands-on Lab 3 – Mass Assignment Review

**Objective**

Evaluate protection against unexpected fields.

**Steps**

1. Identify an endpoint accepting JSON input.
2. Submit expected fields only.
3. Repeat the request with additional privileged fields.
4. Verify that unexpected fields are ignored or rejected.
5. Review server logs.

**Learning Outcomes**

- Mass assignment prevention
- Allowlist validation
- Secure object mapping

---

# Troubleshooting

## Valid Requests Rejected

Possible causes

- Incorrect schema definition
- Business rule mismatch
- Validation order issues
- Canonicalization errors

---

## Unexpected Fields Accepted

Possible causes

- Weak object mapping
- Missing allowlist
- ORM auto-binding
- Incomplete validation

---

## Parsing Failures

Possible causes

- Malformed JSON
- Unsupported media type
- Character encoding issues
- Payload truncation

---

## High CPU During Validation

Possible causes

- Large payloads
- Inefficient regular expressions
- Excessive nesting
- Recursive validation overhead

---

## Duplicate Transactions

Possible causes

- Missing idempotency keys
- Replay attacks
- Client retry logic
- Race conditions

---

# Interview Questions

## Fundamental

1. Why is server-side validation mandatory?
2. What is the difference between technical validation and business validation?
3. What is canonicalization?
4. Why are allowlists preferred over blocklists?
5. What is schema validation?
6. Why should unknown fields be rejected?
7. What is mass assignment?
8. Why should GET requests not modify application state?
9. What is idempotency?
10. Why should validation occur before business logic?

---

## Intermediate

11. How would you design a centralized validation framework?
12. Explain the risks of trusting client-side validation.
13. How would you validate nested JSON objects?
14. Why are fixed-precision data types preferred for financial values?
15. How would you defend against replay attacks?
16. What indicators suggest business logic abuse?
17. How would you detect mass assignment attempts?
18. Why should validation failures be logged?
19. What security risks arise from weak parser configuration?
20. How should validation events be integrated into a SIEM?

---

## Scenario-Based

**Scenario 1**

A payment API accepts additional JSON fields not defined in its public documentation, including administrative attributes.

- What vulnerability might this indicate?
- What controls should be implemented?
- How would you verify the remediation?

---

**Scenario 2**

Security monitoring reports a large increase in malformed JSON requests followed by oversized payload submissions.

- What attack techniques might explain this activity?
- Which telemetry would you review?
- How would you prioritize response actions?

---

**Scenario 3**

A retail API allows repeated order submissions after client-side timeouts, resulting in duplicate purchases.

- How could idempotency keys mitigate this issue?
- Which server-side validation changes would you recommend?
- How would you test the solution?

---

# Chapter Summary

In this chapter, we expanded API input validation beyond syntax checking to include business logic, schema enforcement, secure parsing, and enterprise validation strategies.

We covered:

- Technical vs business validation
- Validation layers
- Canonicalization
- Allowlists and blocklists
- Schema validation
- Mass assignment prevention
- Idempotency
- Replay protection
- Secure parsing
- Validation logging
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

A mature validation strategy combines syntax checks, schema validation, business rules, secure parsing, and continuous monitoring to significantly reduce the risk of injection attacks, business logic abuse, and application compromise.

---

# Chapter Review

You should now be able to answer:

- Why are business rules as important as syntax validation?
- How does canonicalization improve validation accuracy?
- What is the purpose of idempotency keys?
- How do mass assignment vulnerabilities occur?
- Why should validation precede authorization and business logic?
- Which validation events are most valuable for SIEM monitoring?
- How would you design an enterprise-wide validation framework for APIs?

If you can confidently answer these questions, you are ready to continue with **Chapter 19 – OWASP API Security Top 10**, where you'll explore the most critical API security risks, real-world attack scenarios, defensive strategies, detection engineering, and enterprise implementation guidance.

---

# References

## Standards

- RFC 9110 – HTTP Semantics
- JSON Schema Specification
- OpenAPI Specification

## Security Standards

- OWASP API Security Top 10
- OWASP ASVS
- OWASP Input Validation Cheat Sheet
- NIST SP 800-53
- NIST Secure Software Development Framework (SSDF)

## Further Reading

- JSON Schema Documentation
- OpenAPI Initiative
- CWE Top 25 Most Dangerous Software Weaknesses

---

# What's Next?

➡️ **Chapter 19 – OWASP API Security Top 10**

Topics include:

- Overview of the OWASP API Security Top 10
- API1 through API10 risks
- Real-world attack scenarios
- Detection engineering
- SIEM integration
- Enterprise architecture
- Mitigation strategies
- Hands-on labs
- Interview questions