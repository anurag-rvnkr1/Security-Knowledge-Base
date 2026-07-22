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

