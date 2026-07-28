# 21-Injection.md

# Part 1 — Fundamentals of Injection, Attack Surface, Root Causes, Enterprise Risks, and Secure Design

> **"Injection vulnerabilities occur when untrusted input is interpreted as commands or instructions by another component. The safest approach is to ensure data is always treated as data—not executable instructions."**

---

# Learning Objectives

After completing this part, you will understand:

- What Injection Is
- Why Injection Is Dangerous
- Types of Injection Vulnerabilities
- Injection Attack Surface
- Trusted vs Untrusted Input
- Data Flow
- Root Causes
- Enterprise Business Impact
- Secure Design Principles
- Defense in Depth

---

# What is Injection?

An **Injection vulnerability** occurs when an application sends untrusted input to another component that interprets it as executable commands, queries, or instructions.

Instead of being treated as ordinary data, the input changes how the receiving component behaves.

---

# Why Injection Matters

Modern applications communicate with many backend systems.

```
Web Application

│

├── Database

├── Operating System

├── LDAP Directory

├── XML Parser

├── JSON Parser

├── Search Engine

├── Mail Server

├── API Gateway

└── Cloud Services
```

Whenever applications pass user-controlled input to these components, proper validation and safe handling become essential.

---

# OWASP Perspective

Injection remains one of the most important application security risks because many applications interact with interpreters.

Examples include:

- Database query interpreters
- Operating system command interpreters
- Directory service queries
- Template engines
- Expression evaluators
- XML processing components

---

# General Injection Flow

```
User Input

↓

Application

↓

Interpreter

↓

Execution

↓

Response
```

If user input is incorporated unsafely into instructions, unintended behavior may occur.

---

# Trusted vs Untrusted Input

```
Application

│

├── Trusted Internal Data

└── Untrusted External Input
```

Examples of untrusted input:

- Form fields
- URL parameters
- Cookies
- HTTP headers
- Uploaded files
- API requests
- Mobile applications
- Third-party integrations

Applications should treat all external input as untrusted.

---

# Data Flow

```
Browser

↓

HTTP Request

↓

Application

↓

Validation

↓

Business Logic

↓

Database / Service

↓

Response
```

Validation and safe processing should occur before data reaches sensitive components.

---

# Common Injection Targets

```
Injection Targets

│

├── SQL Databases

├── Operating System

├── LDAP

├── XML

├── NoSQL Databases

├── Search Engines

├── Template Engines

├── APIs

└── Cloud Services
```

Different technologies have different interpreters, but the underlying security principle is the same.

---

# Categories of Injection

```
Injection

│

├── SQL Injection

├── NoSQL Injection

├── LDAP Injection

├── Command Injection

├── XPath Injection

├── XML Injection

├── Template Injection

├── Expression Language Injection

└── Other Interpreter-Based Injection
```

Each category targets a different interpreter.

---

# Root Cause

The primary cause of injection is allowing user input to become part of executable instructions.

Conceptually:

```
User Input

↓

Application

↓

Unsafe Construction

↓

Interpreter

↓

Unexpected Behavior
```

Applications should separate **data** from **commands**.

---

# Secure Design Principle

```
User Input

↓

Validation

↓

Safe Processing

↓

Interpreter

↓

Expected Behavior
```

The application should ensure user input cannot alter intended program logic.

---

# Enterprise Example

An online retail platform:

```
Customer

↓

Search Product

↓

Application

↓

Database Query

↓

Results
```

The application should ensure the search term is treated as search data rather than executable query logic.

---

# Multiple Interpreters

Enterprise applications often communicate with several interpreters.

```
User

↓

Web Application

├──────────────┐

▼              ▼

Database     Search

▼              ▼

Directory     APIs

▼              ▼

Operating System
```

Every integration point should follow secure coding practices.

---

# Injection Attack Surface

Potential entry points include:

```
HTTP GET

HTTP POST

Cookies

Headers

JSON

XML

GraphQL

REST APIs

WebSockets

Uploaded Files
```

Any external input should be validated appropriately.

---

# Business Impact

Injection vulnerabilities may contribute to:

```
Sensitive Data Exposure

↓

Unauthorized Actions

↓

Service Disruption

↓

Loss of Customer Trust

↓

Financial Loss

↓

Compliance Issues

↓

Reputational Damage
```

The specific impact depends on the affected component and application design.

---

# Enterprise Workflow

```
Receive Input

↓

Validate

↓

Normalize

↓

Business Logic

↓

Safe Interpreter Interaction

↓

Response
```

Secure applications consistently validate and safely process user input before interacting with backend systems.

---

# Secure Development Lifecycle

Injection prevention should be considered throughout development.

```
Requirements

↓

Architecture

↓

Threat Modeling

↓

Development

↓

Code Review

↓

Testing

↓

Deployment

↓

Monitoring
```

Security should be integrated into every stage.

---

# Defense in Depth

Injection prevention relies on multiple controls.

```
Input Validation

↓

Safe APIs

↓

Least Privilege

↓

Output Handling

↓

Logging

↓

Monitoring
```

No single control should be relied upon exclusively.

---

# Common Misconceptions

| Myth | Reality |
|------|----------|
| Input validation alone prevents every injection issue | Multiple security controls are required |
| Only databases are affected | Many interpreters can be targeted |
| Internal applications do not require protection | All applications should validate untrusted input |
| Authentication prevents injection | Authentication and input handling solve different problems |

---

# Enterprise Security Checklist

```
✓ Validate Input

✓ Normalize Data

✓ Use Safe APIs

✓ Separate Data from Commands

✓ Apply Least Privilege

✓ Log Security Events

✓ Monitor Anomalies

✓ Review Code

✓ Test Regularly
```

---

# Hands-on Lab (Conceptual)

1. Draw the data flow for a sample web application.
2. Identify every point where external input enters the application.
3. List every backend component that interprets instructions.
4. Determine where validation and safe processing should occur.
5. Document the security controls that protect each interpreter.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is an Injection vulnerability?
2. Why is Injection considered a serious security risk?
3. What is the difference between trusted and untrusted input?
4. What are common injection targets?
5. Why should applications separate data from commands?
6. What are common sources of untrusted input?
7. How does defense in depth help prevent Injection?
8. Why should Injection prevention be considered during system design?
9. What business risks can Injection vulnerabilities introduce?
10. Why is input validation only one part of a complete defense?

---

# Best Practices

- Treat all external input as untrusted.
- Validate and normalize input before processing.
- Use secure APIs that clearly separate data from executable instructions.
- Apply the principle of least privilege to backend services.
- Perform code reviews focused on interpreter interactions.
- Log and monitor unusual application behavior.
- Incorporate Injection testing into the Secure SDLC.

---

# Common Mistakes

- Trusting client-side validation.
- Assuming authenticated users cannot submit malicious input.
- Passing user input directly to backend interpreters.
- Failing to validate API input consistently.
- Ignoring non-database interpreters such as LDAP or XML processors.
- Relying on a single defensive mechanism.

---

# Key Takeaways

- Injection occurs when untrusted input is interpreted as executable instructions.
- Many different backend components—not just databases—can be affected.
- Applications should always treat external input as untrusted.
- Secure design separates user data from executable commands.
- Effective prevention combines validation, safe APIs, least privilege, logging, monitoring, and secure development practices.

# 21-Injection.md

# Part 2 — SQL Injection, NoSQL Injection, LDAP Injection, XPath Injection, Command Injection, and Secure Query Design

> **"The safest way to prevent Injection is to ensure that user input is never interpreted as executable instructions. Data should always remain data."**

---

# Learning Objectives

After completing this part, you will understand:

- SQL Injection (SQLi)
- NoSQL Injection
- LDAP Injection
- XPath Injection
- OS Command Injection
- Server-Side Template Injection (SSTI)
- Expression Language Injection
- Secure Query Design
- Parameterized Queries (Conceptual)
- Enterprise Best Practices

---

# Understanding Interpreters

Applications communicate with various interpreters.

```
Application

│

├── SQL Database

├── NoSQL Database

├── Operating System

├── LDAP Directory

├── XML Processor

├── Template Engine

└── Search Engine
```

Each interpreter expects properly formatted instructions from the application.

---

# SQL Injection (SQLi)

SQL Injection occurs when untrusted input improperly influences SQL query construction.

Conceptually:

```
User Input

↓

Application

↓

SQL Query

↓

Database

↓

Response
```

The risk arises when input becomes part of the query structure instead of remaining ordinary data.

---

# Enterprise Example

```
Customer

↓

Search Product

↓

Application

↓

Database Query

↓

Matching Products
```

The customer's search term should be treated strictly as search data.

---

# Secure Query Design

Applications should clearly separate:

```
Instructions

+

User Data

↓

Safe Execution
```

This separation prevents user input from modifying query logic.

---

# Parameterized Queries (Conceptual)

Instead of embedding user input directly into a query, applications bind user data as parameters.

Conceptually:

```
Application

↓

Prepared Statement

+

User Data

↓

Database
```

The database distinguishes query instructions from supplied values.

---

# Benefits of Parameterized Queries

```
✓ Clear Separation of Data

✓ Consistent Query Structure

✓ Reduced Injection Risk

✓ Easier Maintenance

✓ Improved Reliability
```

Parameterized queries are a foundational defense for database interactions.

---

# NoSQL Injection

Modern applications often use NoSQL databases.

```
Application

↓

NoSQL Query

↓

Database

↓

Response
```

Although query languages differ from SQL, applications should still prevent untrusted input from altering intended query behavior.

---

# Common NoSQL Platforms

```
NoSQL

│

├── Document Databases

├── Key-Value Stores

├── Column Databases

└── Graph Databases
```

Each platform has unique query mechanisms but shares the need for secure input handling.

---

# LDAP Injection

LDAP directories manage identity information.

```
User

↓

Application

↓

LDAP Query

↓

Directory Service

↓

Result
```

Applications should safely construct directory queries using validated input.

---

# Enterprise LDAP Example

```
Employee Login

↓

Identity Service

↓

Directory Lookup

↓

Authentication Result
```

Directory searches should treat user input as directory data rather than query instructions.

---

# XPath Injection

Applications processing XML data may evaluate XPath expressions.

```
Application

↓

XPath Query

↓

XML Document

↓

Matching Nodes
```

Secure query construction prevents user input from changing intended XPath behavior.

---

# XML Processing

```
Application

↓

XML Parser

↓

Business Logic

↓

Response
```

XML processing should include secure parser configuration and proper input handling.

---

# OS Command Injection

Some applications interact with operating system utilities.

```
Application

↓

Operating System

↓

Requested Operation

↓

Result
```

Applications should avoid constructing operating system commands directly from untrusted input.

---

# Safer Design

```
Application

↓

Safe System API

↓

Operating System

↓

Expected Operation
```

Whenever possible, use dedicated APIs instead of command interpreters.

---

# Server-Side Template Injection (SSTI)

Template engines generate dynamic content.

```
Application

↓

Template Engine

↓

Rendered Output
```

Applications should avoid allowing untrusted input to become executable template expressions.

---

# Expression Language Injection

Some frameworks evaluate expressions.

```
User Input

↓

Expression Evaluation

↓

Application Logic
```

Expression evaluation should never process untrusted input directly.

---

# Multiple Injection Points

```
Browser

↓

Application

├─────────────┬─────────────┬─────────────┐

▼             ▼             ▼             ▼

Database    LDAP      XML Parser     Operating System
```

Each integration point requires independent protection.

---

# Secure Input Handling

```
Receive Input

↓

Validate

↓

Normalize

↓

Business Logic

↓

Safe API

↓

Interpreter
```

Validation should occur before data reaches sensitive components.

---

# Allowlist Validation

Whenever appropriate, applications should accept only expected input.

```
User Input

↓

Expected Format?

↓

Yes

↓

Continue

──────────────

No

↓

Reject
```

Allowlisting is generally more predictable than attempting to block every possible invalid input.

---

# Least Privilege

Even with secure coding practices, backend services should operate with only the permissions they require.

```
Application

↓

Limited Database Account

↓

Required Operations Only
```

Limiting privileges reduces the impact of implementation mistakes.

---

# Enterprise Architecture

```
                    Browser

                       │

                       ▼

                 Web Application

         ┌─────────────┼─────────────┐

         ▼             ▼             ▼

 Validation     Business Logic    Logging

         │             │             │

         └─────────────┼─────────────┘

                       ▼

                 Safe Query Layer

         ┌─────────────┼─────────────┐

         ▼             ▼             ▼

      Database      Directory      APIs
```

A dedicated data access layer encourages consistent security controls.

---

# Secure Development Practices

```
✓ Validate Input

✓ Normalize Data

✓ Use Parameterized Queries

✓ Prefer Safe APIs

✓ Apply Least Privilege

✓ Review Interpreter Calls

✓ Log Security Events

✓ Perform Security Testing
```

---

# Common Injection Weaknesses

| Weakness | Potential Impact |
|----------|------------------|
| Direct query construction | Unexpected interpreter behavior |
| Missing validation | Increased attack surface |
| Excessive database privileges | Greater business impact |
| Unsafe OS command construction | System-level risk |
| Inconsistent API usage | Uneven security posture |
| Weak logging | Reduced incident visibility |

---

# Enterprise Workflow

```
User Request

↓

Validation

↓

Business Logic

↓

Safe Data Access

↓

Interpreter

↓

Response

↓

Logging
```

Each layer contributes to reducing Injection risk.

---

# Hands-on Lab (Conceptual)

1. List every interpreter used by a sample web application.
2. Identify where user input reaches each interpreter.
3. Determine where parameterized queries or safe APIs should be used.
4. Review which backend accounts require least privilege.
5. Document security controls for each integration point.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is SQL Injection?
2. How does SQL Injection differ from NoSQL Injection?
3. Why are parameterized queries important?
4. What is LDAP Injection?
5. What is XPath Injection?
6. Why should applications avoid constructing operating system commands from user input?
7. What is Server-Side Template Injection (SSTI)?
8. Why is allowlist validation preferred in many situations?
9. How does least privilege reduce Injection risk?
10. Why should every interpreter interaction be reviewed during code reviews?

---

# Best Practices

- Use parameterized queries for database interactions.
- Validate and normalize all untrusted input.
- Prefer framework-provided APIs over direct interpreter access.
- Apply least privilege to databases and backend services.
- Centralize query and interpreter interactions through reusable components.
- Log interpreter errors and security-relevant events.
- Include Injection testing in every release cycle.

---

# Common Mistakes

- Concatenating user input into queries.
- Assuming only SQL databases are vulnerable.
- Using excessive privileges for application service accounts.
- Ignoring template engines and expression evaluators.
- Depending solely on client-side validation.
- Failing to review non-database interpreter integrations.

---

# Key Takeaways

- Injection vulnerabilities affect many interpreter types, not just SQL databases.
- SQL, NoSQL, LDAP, XPath, command interpreters, and template engines all require secure input handling.
- Parameterized queries conceptually separate instructions from user data.
- Safe APIs, validation, least privilege, and secure architecture work together to reduce Injection risk.
- Consistent security controls across all interpreter interactions are essential for enterprise applications.

```text id="rrks28"
**Next:** Part 3
```