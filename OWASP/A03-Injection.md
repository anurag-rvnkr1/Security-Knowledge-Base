# A03:2021 – Injection

---

# Overview

Injection vulnerabilities occur when an application sends untrusted user input to an interpreter without proper validation or sanitization. The interpreter treats the malicious input as commands or part of a query, causing unintended execution.

Injection flaws remain one of the most dangerous web application vulnerabilities because they can lead to:

- Authentication bypass
- Database compromise
- Remote Code Execution (RCE)
- Data theft
- Server compromise
- Full application takeover

Injection attacks exist wherever user-controlled input reaches an interpreter.

Common interpreters include:

- SQL Database
- Operating System Shell
- LDAP Server
- XML Parser
- NoSQL Database
- Template Engine
- GraphQL Resolver
- XPath Processor

---

# Why It Matters

Modern web applications continuously process user input.

Examples include:

- Login forms
- Search boxes
- URL parameters
- Cookies
- HTTP Headers
- API Requests
- File Uploads
- Chat Applications
- Admin Panels

If this input is incorporated into commands without proper handling, attackers may execute unintended operations.

Example:

```
User Input

↓

Application

↓

Database Query

↓

Database
```

If the input is malicious:

```
User Input

↓

' OR 1=1 --

↓

Database

↓

Returns Entire Table
```

---

# What is an Interpreter?

An interpreter is software that reads and executes instructions.

Examples:

```
SQL Server
```

Interprets SQL queries.

```
Linux Bash
```

Interprets shell commands.

```
PowerShell
```

Interprets PowerShell commands.

```
LDAP Server
```

Interprets LDAP queries.

```
Template Engine
```

Interprets template expressions.

If attackers manipulate the instructions being interpreted, they may execute unintended commands.

---

# General Injection Flow

```
Attacker

      │

Malicious Input

      │

Application

      │

Interpreter

      │

Malicious Command Executes
```

The vulnerability exists because the application mixes:

- User input
- Application logic

without separating them securely.

---

# Safe Processing Flow

```
User Input

↓

Validation

↓

Parameterized Query

↓

Interpreter

↓

Safe Execution
```

The interpreter receives data separately from commands, preventing user input from changing application behavior.

---

# Root Cause

Injection vulnerabilities usually occur due to:

- Dynamic query construction
- String concatenation
- Missing input validation
- Missing parameterized queries
- Unsafe API usage
- Poor input encoding
- Excessive trust in client-side validation

---

# Real-World Example

Imagine a login form.

```
Username:

_________

Password:

_________
```

Application code:

```sql
SELECT *
FROM users
WHERE username='admin'
AND password='password';
```

Now suppose an attacker enters:

Username

```
admin' --
```

Password

```
anything
```

The resulting query becomes:

```sql
SELECT *
FROM users
WHERE username='admin' --'
AND password='anything';
```

Everything after `--` is treated as a comment.

The database executes:

```sql
SELECT *
FROM users
WHERE username='admin';
```

The password check is ignored, potentially allowing unauthorized access.

---

# Types of Injection

OWASP groups several injection vulnerabilities under this category.

Major types include:

```
Injection

├── SQL Injection
├── NoSQL Injection
├── OS Command Injection
├── LDAP Injection
├── XPath Injection
├── XML Injection
├── Server-Side Template Injection (SSTI)
├── Expression Language Injection
├── GraphQL Injection
└── CRLF Injection
```

Each targets a different interpreter but exploits the same fundamental weakness: untrusted input being treated as executable instructions.

---

# SQL Injection (SQLi)

Targets relational databases.

Examples:

- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle
- SQLite

Example payload:

```sql
' OR 1=1 --
```

Impact:

- Read database contents
- Modify data
- Delete records
- Bypass authentication
- Execute administrative operations (depending on database permissions)

---

# NoSQL Injection

Targets NoSQL databases such as:

- MongoDB
- CouchDB
- Cassandra

Example (MongoDB):

```json
{
  "username": {
    "$ne": null
  },
  "password": {
    "$ne": null
  }
}
```

Improper query construction can cause authentication checks to succeed unexpectedly.

---

# OS Command Injection

Occurs when user input is passed to operating system commands.

Example:

```python
os.system("ping " + user_input)
```

Attacker input:

```
127.0.0.1 && whoami
```

Executed command:

```bash
ping 127.0.0.1 && whoami
```

Impact:

- Execute arbitrary commands
- Read sensitive files
- Install malware
- Gain remote access
- Escalate privileges

---

# LDAP Injection

Applications using LDAP for authentication or directory lookups may build LDAP queries insecurely.

Example:

```
(&(uid=user)(password=pass))
```

Manipulated input may alter the LDAP filter and bypass intended restrictions.

---

# XPath Injection

XPath queries retrieve information from XML documents.

Example:

```xpath
//user[name='admin']
```

Unsafely concatenated user input may allow attackers to retrieve unintended XML data.

---

# Server-Side Template Injection (SSTI)

Occurs when user input is interpreted by a server-side template engine.

Examples:

- Jinja2
- Twig
- Freemarker
- Velocity
- Thymeleaf

Example payload:

```
{{7*7}}
```

If evaluated by the template engine:

```
49
```

Advanced SSTI vulnerabilities may lead to Remote Code Execution.

---

# Expression Language Injection

Some Java frameworks evaluate expressions dynamically.

Example:

```
${7*7}
```

If evaluated instead of treated as text, attackers may manipulate application logic or execute unauthorized operations.

---

# Common Attack Surfaces

Injection vulnerabilities commonly appear in:

- Login forms
- Search functionality
- URL parameters
- File names
- Report generation
- REST APIs
- GraphQL APIs
- Mobile backend APIs
- Administrative interfaces
- Import/export features
- Search filters
- Sorting parameters

---

# Business Impact

Successful injection attacks can result in:

- Complete database compromise
- Customer data exposure
- Credential theft
- Financial fraud
- Regulatory penalties
- Service disruption
- Intellectual property theft
- Reputation damage
- Remote server compromise

---

# Key Takeaways

- Injection occurs when untrusted input is interpreted as executable commands.
- The root cause is unsafe handling of user-controlled input.
- SQL Injection is the most well-known form, but many other interpreters are vulnerable.
- Parameterized queries, input validation, and context-aware encoding are fundamental defenses.
- Preventing injection requires separating user data from executable commands rather than attempting to filter malicious input alone.

# SQL Injection (SQLi)

## Overview

SQL Injection (SQLi) is one of the oldest and most dangerous web application vulnerabilities. It occurs when an application constructs SQL queries using untrusted user input without proper separation between **code** and **data**.

Instead of treating user input as data, the database interpreter treats it as part of the SQL command.

As a result, attackers may:

- Bypass authentication
- Read sensitive data
- Modify records
- Delete information
- Execute administrative functions
- In some environments, achieve Remote Code Execution (RCE)

---

# Understanding SQL

SQL (Structured Query Language) is the language used to communicate with relational databases.

Common relational databases include:

- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle Database
- MariaDB
- SQLite

Applications use SQL to:

- Retrieve data
- Insert records
- Update records
- Delete records
- Create tables
- Manage permissions

---

# How Applications Communicate with Databases

A typical request flow:

```
User

   │

Login Form

   │

Backend Application

   │

SQL Query

   │

Database

   │

Response

   │

User
```

The application creates a SQL query using user input and sends it to the database.

---

# Vulnerable Login Example

Suppose a login form asks for:

```
Username

Password
```

The developer writes:

```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "';"
```

If the user enters:

```
Username:
alice

Password:
Password123
```

The query becomes:

```sql
SELECT *
FROM users
WHERE username='alice'
AND password='Password123';
```

This works correctly.

---

# The Problem

Now imagine the attacker enters:

Username:

```
' OR '1'='1
```

Password:

```
anything
```

The query becomes:

```sql
SELECT *
FROM users
WHERE username=''
OR '1'='1'
AND password='anything';
```

Since `'1'='1'` is always true, the WHERE clause may evaluate to true for many or all rows, potentially bypassing authentication depending on the application's logic and the database.

---

# Why This Happens

The application directly concatenates user input into SQL commands.

```
Developer

↓

SQL Query

↓

User Input

↓

Database
```

The database cannot distinguish between:

- SQL syntax
- User-provided data

because both are combined into one string.

---

# Secure Approach

Parameterized queries separate SQL instructions from user input.

```
SQL Command

↓

Placeholder

↓

Parameter

↓

Database
```

The database always treats the parameter as data—not executable SQL.

---

# SQL Injection Attack Flow

```
Attacker

      │

Malicious Payload

      │

Web Application

      │

Unsafe SQL Query

      │

Database Executes Payload

      │

Sensitive Data Returned
```

---

# Common SQL Injection Types

```
SQL Injection

├── Authentication Bypass
├── Error-Based
├── UNION-Based
├── Boolean-Based Blind
├── Time-Based Blind
├── Out-of-Band
├── Second-Order
└── Stacked Queries
```

Each type exploits the same underlying flaw but extracts information differently.

---

# 1. Authentication Bypass

The attacker attempts to bypass the login process by altering the SQL logic.

Example vulnerable query:

```sql
SELECT *
FROM users
WHERE username='admin'
AND password='password';
```

Malicious input:

```
admin' --
```

Resulting query:

```sql
SELECT *
FROM users
WHERE username='admin' --'
AND password='password';
```

The comment marker (`--`) causes the password check to be ignored in many SQL dialects, which may allow login as the specified user if the application is vulnerable.

---

# 2. Error-Based SQL Injection

Some applications display raw database errors.

Example:

```
Database Error

Unknown column

Syntax error

Invalid table name
```

These messages reveal valuable information, such as:

- Database type
- Table names
- Column names
- Query structure
- SQL syntax

Attackers use these clues to craft more effective payloads.

---

# Example

Instead of:

```
Invalid Username
```

The application returns:

```
MySQL Error:

Unknown column 'username'
```

The attacker now knows:

- MySQL is in use.
- The application's query structure is leaking internal details.

---

# 3. UNION-Based SQL Injection

The SQL `UNION` operator combines the results of two compatible `SELECT` statements.

Attackers abuse this to retrieve additional data if the application returns query results.

Example concept:

```sql
SELECT product_name
FROM products

UNION

SELECT username
FROM users;
```

If the application is vulnerable and column counts/types align, data from another table may be returned.

Attackers typically determine:

- Number of columns
- Data types
- Visible output locations

before using UNION.

---

# UNION Attack Flow

```
Original Query

↓

Products

↓

Attacker Adds UNION

↓

Users Table

↓

Application Displays Both
```

---

# 4. Boolean-Based Blind SQL Injection

Some applications suppress errors and do not display query results.

Instead, attackers infer information based on differences in application behavior.

Example approach:

Condition evaluates to **true**:

```
Application behaves normally.
```

Condition evaluates to **false**:

```
Application responds differently.
```

By asking a series of true/false questions, attackers can infer information one bit or one character at a time.

---

# Example Logic

The attacker asks questions such as:

- Does the first character equal "A"?
- Is the database version greater than 10?
- Does the current user have administrative privileges?

The application's responses gradually reveal hidden information.

---

# 5. Time-Based Blind SQL Injection

If the application always returns identical pages, attackers may rely on response timing.

Conceptually:

```
If condition is true

↓

Delay response

↓

Otherwise

↓

Respond immediately
```

By measuring response times, attackers can infer answers to true/false questions even without visible output.

---

# 6. Out-of-Band (OOB) SQL Injection

Some database systems can initiate outbound network requests under certain configurations.

If direct responses are unavailable, attackers may trigger the database to communicate with an external system they control.

Conceptually:

```
Application

↓

Database

↓

External DNS / HTTP Request

↓

Attacker Observes Request
```

This technique is useful in highly restricted environments but depends on database features and network configuration.

---

# 7. Second-Order SQL Injection

In second-order SQL Injection, malicious input is stored safely at first but becomes dangerous later when reused in another SQL query without proper parameterization.

Example flow:

```
Attacker Input

↓

Stored in Database

↓

Administrator Opens Record

↓

Unsafe SQL Construction

↓

Injection Executes
```

These vulnerabilities can be difficult to detect because exploitation occurs long after the original input.

---

# 8. Stacked Queries

Some database engines allow multiple SQL statements in a single request.

Conceptually:

```
Statement 1

;

Statement 2

;

Statement 3
```

If the application and database permit stacked queries, an attacker may execute additional SQL statements beyond the intended one.

Whether this is possible depends on the database engine and application configuration.

---

# Common Developer Mistakes

❌ Building SQL queries using string concatenation.

❌ Trusting client-side validation.

❌ Displaying raw database errors.

❌ Granting excessive database privileges.

❌ Using administrator database accounts for the application.

❌ Failing to validate and parameterize all user-controlled input.

---

# SQL Injection vs Broken Access Control

| SQL Injection | Broken Access Control |
|---------------|----------------------|
| Manipulates SQL queries | Bypasses authorization rules |
| Targets the database interpreter | Targets authorization logic |
| Can expose or modify database contents | Can expose resources without proper permissions |
| Root cause: unsafe query construction | Root cause: missing or incorrect access checks |

---

# Key Takeaways

- SQL Injection occurs when user input is incorporated into SQL commands without proper separation of code and data.
- Parameterized queries are the primary defense against SQL Injection.
- SQL Injection has multiple forms, including authentication bypass, error-based, UNION-based, blind, out-of-band, second-order, and stacked query attacks.
- Error messages, timing differences, and application behavior can all reveal sensitive information to attackers.
- Eliminating SQL Injection requires secure coding practices, least-privilege database accounts, proper error handling, and comprehensive input handling—not simple keyword filtering.

# Other Injection Vulnerabilities

While SQL Injection is the most well-known injection attack, many modern applications use technologies such as NoSQL databases, operating system commands, template engines, LDAP directories, GraphQL APIs, and XML processors. Each of these can become vulnerable if untrusted input is interpreted as executable instructions.

---

# 1. NoSQL Injection

## Overview

NoSQL Injection targets applications using NoSQL databases instead of traditional relational databases.

Common NoSQL databases include:

- MongoDB
- CouchDB
- Cassandra
- Redis (certain use cases)
- Firebase Firestore (query misuse scenarios)

Unlike SQL databases, NoSQL databases often use JSON-like query structures.

---

## Typical Architecture

```
User

   │

Web Application

   │

MongoDB Driver

   │

MongoDB Database
```

If user input is inserted directly into the query object, attackers may manipulate the query logic.

---

## Vulnerable Example

Imagine an application builds a MongoDB query directly from user input.

Conceptually:

```
User Input

↓

Application

↓

MongoDB Query

↓

Database
```

If the application fails to validate the structure of incoming JSON, an attacker may inject operators such as comparison operators instead of simple values, potentially altering the intended query.

---

## Common Causes

- Trusting JSON input
- Dynamic query construction
- Missing schema validation
- Lack of input type checking

---

## Potential Impact

- Authentication bypass
- Data disclosure
- Unauthorized record access
- Privilege escalation
- Database manipulation

---

# Prevention

- Validate input types.
- Use strict schemas.
- Reject unexpected JSON operators.
- Build queries using safe APIs rather than directly accepting client-supplied query objects.
- Apply least privilege to database accounts.

---

# 2. OS Command Injection

## Overview

OS Command Injection occurs when an application executes operating system commands using user-controlled input.

Instead of attacking the database, the attacker targets the underlying operating system.

---

## Architecture

```
User

↓

Application

↓

Shell

↓

Operating System
```

If user input is concatenated into shell commands, attackers may execute unintended system commands.

---

## Common Sources

- Network diagnostic tools
- Ping utilities
- File management features
- Backup scripts
- Image processing pipelines
- Administrative utilities

---

## Example (Conceptual)

An application allows users to test connectivity by supplying a host.

Unsafe design:

```
Application

↓

Build Shell Command

↓

Execute
```

If user input is not handled safely, it may alter the command being executed.

---

## Possible Impact

- Remote Code Execution (RCE)
- File disclosure
- System reconnaissance
- Malware installation
- Privilege escalation
- Full server compromise

---

## Prevention

- Avoid shell execution when native APIs are available.
- If shell execution is unavoidable, avoid invoking a shell interpreter and pass arguments safely through language-specific process APIs.
- Validate and whitelist acceptable input.
- Run services with minimal operating system privileges.
- Log and monitor command execution.

---

# 3. LDAP Injection

## Overview

LDAP (Lightweight Directory Access Protocol) is commonly used for:

- Active Directory
- Enterprise authentication
- User directories
- Corporate identity management

Applications often build LDAP filters to authenticate users or search directory information.

---

## Architecture

```
User

↓

Application

↓

LDAP Query

↓

Active Directory
```

Improper construction of LDAP filters may allow attackers to alter search conditions.

---

## Risks

- Authentication bypass
- User enumeration
- Unauthorized directory access
- Information disclosure

---

## Prevention

- Escape special LDAP characters.
- Use framework-provided LDAP APIs.
- Validate input.
- Restrict directory permissions.
- Apply least privilege.

---

# 4. XPath Injection

## Overview

XPath is a query language used to retrieve information from XML documents.

Applications that dynamically construct XPath expressions from user input may become vulnerable.

---

## Architecture

```
User

↓

Application

↓

XPath Query

↓

XML Document
```

If user input changes the query logic, unauthorized XML data may be retrieved.

---

## Example Use Cases

- Legacy web applications
- XML configuration systems
- SOAP services
- XML authentication systems

---

## Prevention

- Use parameterized XPath APIs where available.
- Escape reserved characters.
- Validate user input.
- Avoid dynamic XPath construction.

---

# 5. Server-Side Template Injection (SSTI)

## Overview

Modern web frameworks often use server-side template engines to generate HTML dynamically.

Popular template engines include:

- Jinja2 (Python)
- Twig (PHP)
- Freemarker (Java)
- Velocity
- Thymeleaf
- Smarty
- Handlebars (server-side usage)

If untrusted input is interpreted as template syntax instead of plain text, attackers may execute template expressions.

---

## Architecture

```
User Input

↓

Template Engine

↓

HTML Response
```

Instead of treating input as text, the template engine evaluates it.

---

## Typical Impact

Depending on the template engine:

- Information disclosure
- File access
- Remote Code Execution
- Server compromise

---

## Prevention

- Never render user input directly as templates.
- Separate template code from user-controlled data.
- Use sandboxing where supported.
- Keep template engines updated.

---

# 6. Expression Language (EL) Injection

## Overview

Several Java frameworks evaluate expression languages dynamically.

Examples include:

- Jakarta Expression Language
- Spring Expression Language (SpEL)
- OGNL (Object Graph Navigation Language)

Improper evaluation of user-controlled expressions may lead to:

- Authorization bypass
- Information disclosure
- Remote Code Execution

---

## Prevention

- Disable unnecessary expression evaluation.
- Never evaluate user-controlled expressions.
- Restrict accessible objects and methods.
- Keep frameworks updated.

---

# 7. GraphQL Injection

## Overview

GraphQL allows clients to request exactly the data they need.

If GraphQL queries, filters, or resolvers fail to validate input correctly, injection-style vulnerabilities may arise.

---

## Common Risks

- Excessive data exposure
- Unauthorized field access
- Resolver manipulation
- Denial of Service through expensive queries
- Backend injection into downstream systems

---

## Prevention

- Validate input.
- Implement authorization at the resolver level.
- Limit query depth and complexity.
- Disable introspection in production where appropriate.
- Rate limit API requests.

---

# Comparing Injection Types

| Injection Type | Target Interpreter | Typical Impact |
|----------------|-------------------|----------------|
| SQL Injection | SQL Database | Data theft, authentication bypass |
| NoSQL Injection | NoSQL Database | Unauthorized queries |
| OS Command Injection | Operating System Shell | Remote Code Execution |
| LDAP Injection | LDAP Directory | Authentication bypass |
| XPath Injection | XML Processor | XML data disclosure |
| SSTI | Template Engine | Remote Code Execution |
| EL Injection | Expression Engine | Code execution, privilege escalation |
| GraphQL Injection | GraphQL Resolver | Unauthorized data access |

---

# Detection Methodology

During a penetration test, evaluate every location where user input reaches an interpreter.

Common attack surfaces include:

- URL parameters
- POST bodies
- JSON payloads
- XML requests
- GraphQL queries
- HTTP headers
- Cookies
- File names
- Search fields
- Authentication forms

Testing should determine:

- Is user input reflected?
- Does application behavior change unexpectedly?
- Are interpreter errors exposed?
- Are queries dynamically constructed?
- Are unexpected operators accepted?
- Can application logic be altered?

---

# General Prevention Strategy

Regardless of the interpreter involved, the security principles remain consistent:

1. Treat all user input as untrusted.
2. Validate input against expected formats.
3. Use safe APIs that separate code from data.
4. Escape data only when appropriate for the target context.
5. Avoid dynamic command or query construction.
6. Apply least privilege to backend services.
7. Hide detailed error messages from users.
8. Log suspicious requests and monitor for repeated attack patterns.
9. Keep frameworks and libraries updated.
10. Perform regular code reviews and security testing.

---

# Key Takeaways

- Injection vulnerabilities are not limited to SQL databases.
- Any interpreter that processes untrusted input can become an attack target.
- The root cause across all injection types is the same: user-controlled input being interpreted as executable instructions.
- Secure APIs, parameterization, input validation, and least privilege are the most effective defenses.
- Modern penetration tests should assess SQL, NoSQL, operating system commands, template engines, LDAP, GraphQL, XML, and other interpreters as part of a comprehensive application security review.

# Detection

Injection vulnerabilities should be identified through a combination of manual testing, automated scanning, secure code review, and architecture analysis. Automated tools can discover common issues, but manual verification is essential to understand the root cause and confirm exploitability.

---

# Manual Testing

## 1. Identify User-Controlled Input

Locate every place where the application accepts external input, including:

- URL parameters
- Query strings
- POST bodies
- JSON requests
- XML requests
- GraphQL queries
- Cookies
- HTTP headers
- File uploads
- Search forms

Trace how this input flows through the application.

---

## 2. Observe Application Behavior

Check whether unexpected input causes:

- Different responses
- Error messages
- Delays
- Authentication bypass
- Missing authorization checks
- Unexpected output

Unexpected behavior often indicates that user input is reaching an interpreter.

---

## 3. Review Error Messages

Examples include:

```
SQL syntax error
```

```
MongoDB query failed
```

```
LDAP Exception
```

```
Template rendering error
```

```
Command execution failed
```

Detailed error messages may reveal:

- Database type
- Query structure
- Table names
- Framework information
- Template engine
- Operating system

---

## 4. Review Source Code

Look for:

- String concatenation
- Dynamic query generation
- Shell execution
- Template rendering of user input
- Unsafe evaluation functions

Examples:

```python
query = "SELECT * FROM users WHERE id=" + user_input
```

```javascript
exec("ping " + host)
```

```python
Template(user_input)
```

These patterns deserve careful review.

---

# Automated Detection

Automation helps identify common injection points but should always be followed by manual validation.

---

## Burp Suite

Useful modules:

- Proxy
- Repeater
- Intruder
- Comparer
- Logger

Typical workflow:

```
Browser

↓

Burp Proxy

↓

Capture Request

↓

Send to Repeater

↓

Modify Input

↓

Analyze Response
```

Burp Suite helps identify:

- SQL Injection
- SSTI
- LDAP Injection
- XPath Injection
- Command Injection
- Header Injection

---

## sqlmap

`sqlmap` automates SQL Injection detection and exploitation.

Typical workflow:

```
Captured Request

↓

sqlmap

↓

Database Analysis

↓

Verification
```

Use sqlmap only against systems you own or have explicit authorization to test.

---

## ffuf

Useful for discovering:

- Hidden endpoints
- Backup files
- Administrative interfaces

Additional attack surface often leads to previously unknown injection opportunities.

---

## Static Application Security Testing (SAST)

SAST tools inspect source code for patterns such as:

- Dynamic SQL
- Unsafe template rendering
- Shell execution
- Hardcoded credentials
- Dangerous API usage

Examples include:

- Semgrep
- SonarQube
- CodeQL

---

## Dynamic Application Security Testing (DAST)

DAST evaluates a running application.

Typical tools:

- OWASP ZAP
- Burp Suite Professional
- Invicti
- Acunetix

---

# Prevention

Preventing injection requires secure software design rather than relying on input filtering alone.

---

## 1. Parameterized Queries

Always use prepared statements or parameterized queries.

Instead of combining SQL code and user input into a single string, send them separately to the database.

This prevents user input from changing the query structure.

---

## 2. Input Validation

Accept only expected input.

Examples:

- Integer IDs
- Email format
- UUID format
- Specific dates
- Enumerated values

Reject unexpected characters and data types whenever possible.

---

## 3. Avoid Dynamic Command Construction

Avoid constructing:

- SQL queries
- Shell commands
- LDAP filters
- XPath expressions
- Template code

using string concatenation.

---

## 4. Context-Aware Escaping

Where parameterization is unavailable, apply escaping appropriate for the target interpreter.

Escaping alone should not replace parameterization.

---

## 5. Least Privilege

Backend services should use accounts with only the permissions they require.

Examples:

Application account:

✔ Read Orders

✔ Update Orders

✘ Drop Database

✘ Create Users

---

## 6. Secure Error Handling

Users should receive generic error messages.

Instead of:

```
SQL Error

Unknown column
```

Return:

```
An unexpected error occurred.
```

Detailed errors should be logged securely for administrators.

---

## 7. Keep Components Updated

Regularly update:

- Database drivers
- Frameworks
- Template engines
- Libraries
- ORM components

Many injection vulnerabilities arise from outdated software.

---

# Secure Coding Examples

## Python (Django ORM)

```python
user = User.objects.filter(
    username=username
).first()
```

The ORM generates parameterized queries internally, reducing the risk of SQL Injection when used correctly.

---

## Java (Spring)

```java
PreparedStatement stmt =
connection.prepareStatement(
    "SELECT * FROM users WHERE id = ?"
);
```

Prepared statements separate SQL instructions from user data.

---

## Node.js (Parameterized Query)

```javascript
db.query(
    "SELECT * FROM users WHERE id = ?",
    [userId]
);
```

The placeholder ensures the input is treated as data rather than executable SQL.

---

## PHP (PDO)

```php
$stmt = $pdo->prepare(
    "SELECT * FROM users WHERE id = ?"
);

$stmt->execute([$id]);
```

PDO prepared statements are the recommended approach for preventing SQL Injection.

---

# Best Practices

✔ Use parameterized queries everywhere.

✔ Validate all user input.

✔ Apply allow-list validation where practical.

✔ Avoid dynamic SQL generation.

✔ Never execute shell commands with raw user input.

✔ Escape data only for the appropriate context.

✔ Run applications using least-privileged accounts.

✔ Hide implementation details from end users.

✔ Perform regular code reviews.

✔ Integrate SAST and DAST into the CI/CD pipeline.

✔ Conduct periodic penetration testing.

✔ Monitor logs for repeated injection attempts.

---

# Useful Commands

## Nmap Service Detection

```bash
nmap -sV example.com
```

---

## Enumerate Hidden Content

```bash
ffuf -u https://example.com/FUZZ \
-w wordlist.txt
```

---

## Test HTTP Requests

```bash
curl https://example.com
```

---

## Inspect Responses

```bash
curl -i https://example.com
```

---

# Practical Lab

## Objective

Identify and remediate injection vulnerabilities in a deliberately vulnerable application.

---

## Recommended Labs

### OWASP Juice Shop

Practice:

- SQL Injection
- NoSQL Injection
- SSTI
- Authentication bypass

---

### DVWA (Damn Vulnerable Web Application)

Practice:

- SQL Injection
- Command Injection
- File Inclusion
- Authentication flaws

---

### WebGoat

Practice:

- SQL Injection
- XPath Injection
- LDAP Injection
- Secure coding exercises

---

## Suggested Workflow

1. Intercept requests using Burp Suite.
2. Identify user-controlled parameters.
3. Test application behavior with unexpected input.
4. Confirm whether an interpreter is processing user input unsafely.
5. Identify the root cause in the application code.
6. Recommend parameterization, validation, or safer APIs.
7. Retest after remediation.

---

# Interview Questions

## Beginner

### What is an Injection vulnerability?

Injection occurs when untrusted user input is interpreted as executable commands by an interpreter.

---

### Why is SQL Injection dangerous?

Because it may allow attackers to read, modify, or delete database data, bypass authentication, or perform administrative actions.

---

### What is the best defense against SQL Injection?

Parameterized queries (prepared statements), combined with input validation and least privilege.

---

### What is Command Injection?

Command Injection occurs when user input is incorporated into operating system commands without proper handling, allowing unintended command execution.

---

## Intermediate

### What is the difference between SQL Injection and NoSQL Injection?

SQL Injection targets relational database query languages, while NoSQL Injection targets query mechanisms used by NoSQL databases. Both stem from unsafe handling of user-controlled input.

---

### Why is input validation alone insufficient?

Validation reduces attack surface but cannot guarantee protection against every injection technique. Safe APIs and parameterization are still required.

---

### What is Server-Side Template Injection?

SSTI occurs when user input is evaluated by a server-side template engine instead of being treated as plain text, potentially leading to information disclosure or code execution.

---

## Advanced

### How would you identify an Injection vulnerability during a penetration test?

A systematic approach includes:

- Mapping user-controlled inputs.
- Understanding backend technologies.
- Testing how input reaches interpreters.
- Observing differences in responses, errors, and timing.
- Reviewing application behavior with malformed input.
- Confirming findings manually.
- Assessing business impact.
- Providing secure remediation guidance.

---

### Why are ORMs generally safer than dynamic SQL?

ORMs typically generate parameterized queries automatically, separating SQL logic from user input. However, unsafe raw query APIs within an ORM can still introduce SQL Injection if misused.

---

### What role does least privilege play in mitigating Injection?

Even if an injection vulnerability exists, limiting database or operating system permissions reduces the potential impact by preventing unauthorized administrative actions.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP SQL Injection Prevention Cheat Sheet
- OWASP Query Parameterization Cheat Sheet
- OWASP Web Security Testing Guide (WSTG)
- OWASP ASVS
- OWASP Juice Shop
- OWASP WebGoat

## MITRE CWE

- CWE-89: SQL Injection
- CWE-77: Command Injection
- CWE-74: Injection
- CWE-90: LDAP Injection
- CWE-91: XML Injection
- CWE-917: Expression Language Injection

## Standards

- NIST Secure Software Development Framework (SSDF)
- NIST SP 800-53
- CIS Secure Software Development Controls

## Additional Resources

- PortSwigger Web Security Academy
- PostgreSQL Documentation
- MySQL Documentation
- MongoDB Security Documentation

---

# Summary

Injection vulnerabilities arise when applications allow untrusted input to influence interpreters such as SQL databases, operating system shells, LDAP directories, template engines, or GraphQL resolvers. The root cause is almost always the same: failure to clearly separate executable instructions from user-supplied data.

Modern defenses rely on parameterized queries, safe framework APIs, strong input validation, least privilege, secure error handling, and continuous security testing. By combining secure development practices with regular code reviews and penetration testing, organizations can significantly reduce the risk and impact of injection attacks.