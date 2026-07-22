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