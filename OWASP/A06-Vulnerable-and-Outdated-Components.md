# A06:2021 – Vulnerable and Outdated Components

---

# Overview

Modern applications rarely consist entirely of custom-written code.

Instead, they are built upon a large ecosystem of:

- Open-source libraries
- Third-party packages
- Frameworks
- Runtime environments
- Operating systems
- Containers
- Web servers
- Databases
- APIs
- Cloud SDKs

These components accelerate development, reduce costs, and provide reusable functionality. However, they also introduce security risks when they contain known vulnerabilities or are no longer maintained.

A06:2021 – Vulnerable and Outdated Components focuses on the risks associated with using software components that have known security flaws, unsupported versions, or insecure dependencies.

---

# Why It Matters

A modern web application may contain thousands of software dependencies.

Example:

```
Application

│

├── Django

│     ├── requests
│     ├── urllib3
│     ├── cryptography
│     └── SQL Driver

│
├── Redis Client
├── JWT Library
├── Logging Library
├── Cloud SDK
└── Monitoring Agent
```

A vulnerability in **any one** of these components may compromise the entire application.

---

# What is a Software Component?

A software component is any reusable piece of software that provides functionality.

Examples include:

Application Frameworks

- Django
- Flask
- Spring Boot
- Express.js
- Laravel

Programming Libraries

- OpenSSL
- Log4j
- NumPy
- Pandas
- React
- jQuery

Infrastructure

- Nginx
- Apache
- Docker
- Kubernetes

Databases

- PostgreSQL
- MySQL
- MongoDB
- Redis

Operating Systems

- Ubuntu
- Windows Server
- Red Hat Enterprise Linux

Cloud SDKs

- AWS SDK
- Azure SDK
- Google Cloud SDK

---

# Why Do Vulnerabilities Exist?

Software is developed by humans.

Every software project contains bugs.

Some bugs become security vulnerabilities.

Example:

```
Developer

↓

Coding Error

↓

Software Bug

↓

Security Researcher

↓

CVE Published

↓

Patch Released
```

If organizations fail to apply updates, attackers can exploit publicly known vulnerabilities.

---

# Understanding the Software Supply Chain

Applications depend on many upstream components.

```
Your Application

↓

Framework

↓

Library

↓

Another Library

↓

Operating System

↓

Kernel
```

A weakness anywhere in the supply chain may affect your application.

This is known as the **software supply chain**.

---

# Dependency Chain

Example:

```
Your App

↓

Django

↓

urllib3

↓

OpenSSL

↓

Operating System
```

Even if your application code is secure, vulnerabilities in lower-level dependencies can still be exploited.

---

# Types of Components

## Direct Dependencies

Packages explicitly installed by developers.

Example:

```
pip install django
```

---

## Transitive Dependencies

Packages installed automatically because another package depends on them.

Example:

```
Application

↓

Django

↓

urllib3

↓

certifi
```

Developers may not even realize these packages exist.

---

# Supported vs Unsupported Software

Supported software:

✔ Receives updates

✔ Receives security patches

✔ Maintained by developers

Unsupported software:

✘ No updates

✘ No bug fixes

✘ No security patches

Using unsupported software significantly increases risk.

---

# What Makes a Component Vulnerable?

Common causes include:

- Buffer overflows
- Deserialization flaws
- Authentication bypass
- Memory corruption
- Remote Code Execution (RCE)
- Privilege escalation
- Information disclosure
- Insecure default configuration
- Weak cryptography

---

# Root Causes

Organizations often become vulnerable because they:

- Do not maintain an inventory of components.
- Ignore security updates.
- Use unsupported software.
- Install unnecessary packages.
- Do not monitor security advisories.
- Fail to scan dependencies.
- Do not verify package integrity.

---

# Example Attack Flow

```
Public CVE Released

↓

Patch Available

↓

Organization Delays Update

↓

Attacker Scans Internet

↓

Finds Vulnerable Version

↓

Exploits Vulnerability

↓

Remote Code Execution

↓

System Compromise
```

---

# Real-World Example

Suppose an organization deploys:

```
Apache Log4j 2.14
```

Months later:

```
Critical Remote Code Execution

↓

CVE Published

↓

Patch Released
```

The organization continues running the vulnerable version.

Attackers exploit the known vulnerability to execute arbitrary code on the server.

The application's own code may contain no vulnerabilities—the compromise results entirely from an outdated third-party component.

---

# Why Updating Isn't Always Simple

Organizations cannot always apply updates immediately.

Challenges include:

- Compatibility issues
- Legacy applications
- Third-party integrations
- Downtime requirements
- Change management processes
- Vendor certification

Therefore, effective vulnerability management involves:

- Risk assessment
- Testing
- Patch prioritization
- Compensating controls
- Scheduled deployments

---

# Software Lifecycle

Every component follows a lifecycle.

```
Development

↓

Release

↓

Maintenance

↓

Security Updates

↓

End of Support

↓

End of Life (EOL)
```

Once a component reaches End of Life, security fixes are typically no longer provided.

---

# Business Impact

Using vulnerable or outdated components may lead to:

- Remote Code Execution
- Data breaches
- Credential theft
- Ransomware deployment
- Privilege escalation
- Service disruption
- Regulatory penalties
- Financial loss
- Reputational damage

---

# Security Responsibility

Developers are responsible for:

- Selecting trusted packages.
- Removing unused dependencies.
- Updating components.

Security teams are responsible for:

- Monitoring advisories.
- Performing vulnerability assessments.
- Reviewing Software Bills of Materials (SBOMs).
- Managing patch priorities.

Operations teams are responsible for:

- Deploying updates.
- Validating configurations.
- Monitoring production systems.

---

# Shared Responsibility

Managing vulnerable components requires collaboration.

```
Developers

↓

Security Team

↓

DevSecOps

↓

Operations

↓

Management
```

Each group plays an important role in reducing software supply chain risk.

---

# Key Takeaways

- Modern applications rely heavily on third-party software components.
- Vulnerabilities in dependencies can compromise otherwise secure applications.
- Both direct and transitive dependencies must be managed.
- Unsupported software should be replaced or isolated.
- Effective vulnerability management includes inventory, monitoring, scanning, patching, and continuous review.