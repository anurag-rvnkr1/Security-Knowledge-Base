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

# The Vulnerability Ecosystem

Modern vulnerability management relies on standardized identifiers, scoring systems, and databases.

Instead of every organization inventing its own naming system, the cybersecurity industry uses globally recognized standards to describe vulnerabilities and assess risk.

The most important standards include:

```
Vulnerability Report

↓

CVE

↓

CWE

↓

CVSS

↓

NVD

↓

Vendor Patch

↓

Security Teams

↓

Remediation
```

---

# Common Vulnerabilities and Exposures (CVE)

## Overview

A **Common Vulnerabilities and Exposures (CVE)** identifier is a unique public identifier assigned to a specific publicly disclosed security vulnerability.

A CVE does **not** contain the patch itself or the exploit code. It provides a standardized identifier so vendors, researchers, and organizations can discuss the same vulnerability consistently.

Example format:

```
CVE-2021-44228
```

Where:

- **2021** → Year the CVE was assigned.
- **44228** → Unique identifier.

---

## Example

```
CVE-2021-44228

↓

Apache Log4j

↓

Remote Code Execution
```

Security tools, advisories, and scanners all reference the same CVE ID.

---

# CVE Lifecycle

```
Researcher Discovers Issue

↓

Vendor Notified

↓

CVE Assigned

↓

Patch Developed

↓

Public Disclosure

↓

Organizations Patch Systems
```

Timely patching after disclosure is essential to reduce exposure.

---

# Common Weakness Enumeration (CWE)

## Overview

While a CVE identifies a **specific vulnerability**, a **Common Weakness Enumeration (CWE)** identifies the **underlying class of software weakness** that caused it.

Think of it this way:

- **CVE** = Specific instance.
- **CWE** = General category.

---

## Example

```
CVE-XXXX-YYYY

↓

Caused By

↓

CWE-79

↓

Cross-Site Scripting
```

Multiple CVEs can map to the same CWE because different applications may contain the same type of weakness.

---

## Common CWEs

| CWE | Weakness |
|------|----------|
| CWE-79 | Cross-Site Scripting (XSS) |
| CWE-89 | SQL Injection |
| CWE-22 | Path Traversal |
| CWE-287 | Improper Authentication |
| CWE-352 | Cross-Site Request Forgery (CSRF) |
| CWE-798 | Hardcoded Credentials |
| CWE-918 | Server-Side Request Forgery (SSRF) |

Understanding the associated CWE helps developers address the root cause rather than only fixing a single occurrence.

---

# Common Vulnerability Scoring System (CVSS)

## Overview

Not every vulnerability presents the same level of risk.

The **Common Vulnerability Scoring System (CVSS)** provides a standardized numerical score from **0.0 to 10.0** that estimates the technical severity of a vulnerability.

---

## CVSS Severity Levels

| Score | Severity |
|-------:|----------|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

---

## Example

```
CVE-2021-44228

↓

CVSS 10.0

↓

Critical
```

A high CVSS score indicates significant technical impact, but organizations should also consider business context.

---

# CVSS Base Metrics

CVSS evaluates several characteristics of a vulnerability.

Examples include:

- Attack Vector (Network, Local, Physical)
- Attack Complexity
- Privileges Required
- User Interaction
- Scope
- Confidentiality Impact
- Integrity Impact
- Availability Impact

These metrics determine the overall Base Score.

---

# Common Platform Enumeration (CPE)

## Overview

A **Common Platform Enumeration (CPE)** is a standardized way to identify software, operating systems, and hardware products.

Example:

```
Vendor

↓

Product

↓

Version
```

Security scanners use CPE names to determine whether a system matches software affected by a particular CVE.

---

# National Vulnerability Database (NVD)

## Overview

The **National Vulnerability Database (NVD)** is a publicly available database that enriches CVE records with additional information.

Typical entries include:

- CVSS score
- CWE mappings
- Affected products
- References
- Technical details

Many vulnerability scanners use NVD data to identify known issues.

---

# Exploit Prediction Scoring System (EPSS)

## Overview

A high CVSS score does not necessarily mean a vulnerability will be exploited soon.

The **Exploit Prediction Scoring System (EPSS)** estimates the likelihood that a vulnerability will be exploited in the near future based on observed trends and other signals.

Example:

```
High CVSS

↓

Low EPSS

↓

Technically severe but currently less likely to be exploited
```

or

```
Medium CVSS

↓

High EPSS

↓

Likely to be exploited soon
```

Organizations often use EPSS alongside CVSS to prioritize remediation.

---

# Known Exploited Vulnerabilities (KEV)

## Overview

Some vulnerabilities are actively exploited in the wild.

The **Known Exploited Vulnerabilities (KEV)** catalog identifies vulnerabilities with confirmed real-world exploitation.

Security teams frequently prioritize KEV-listed vulnerabilities because attackers are already using them.

---

# Why CVSS Alone Is Not Enough

Consider two vulnerabilities:

```
Vulnerability A

CVSS 9.8

↓

Internal Test Server
```

```
Vulnerability B

CVSS 7.5

↓

Internet-Facing Payment System

↓

Actively Exploited
```

Although Vulnerability A has a higher technical score, Vulnerability B may require more urgent remediation because of exposure and active exploitation.

Risk-based prioritization considers:

- Technical severity
- Asset value
- Internet exposure
- Business impact
- Exploitation status
- Compensating controls

---

# Software Bill of Materials (SBOM)

## Overview

A **Software Bill of Materials (SBOM)** is an inventory of all software components, libraries, and dependencies used by an application.

Think of it as an ingredient list for software.

---

## Example

```
Online Banking Application

│

├── Spring Boot
├── Log4j
├── Jackson
├── PostgreSQL Driver
├── OpenSSL
└── JWT Library
```

If a vulnerability is disclosed in one component, the SBOM helps identify affected applications quickly.

---

# Benefits of SBOM

- Improved visibility into dependencies.
- Faster impact assessment.
- Easier vulnerability management.
- Better regulatory compliance.
- Enhanced software supply chain security.

---

# Vulnerability Disclosure Process

Responsible disclosure typically follows this sequence:

```
Researcher

↓

Vendor

↓

CVE Assignment

↓

Patch Development

↓

Security Advisory

↓

Public Disclosure

↓

Customer Remediation
```

Coordinated disclosure allows vendors time to develop and distribute fixes before widespread public awareness.

---

# Enterprise Vulnerability Prioritization

Many organizations use a combination of factors to prioritize remediation.

Typical workflow:

```
Asset Inventory

↓

Identify Components

↓

Match Against CVEs

↓

Assess CVSS

↓

Check EPSS

↓

Review KEV

↓

Evaluate Business Impact

↓

Patch Priority
```

This approach balances technical severity with operational and business risk.

---

# Key Takeaways

- CVEs uniquely identify publicly disclosed vulnerabilities.
- CWEs describe the underlying class of weakness that caused a vulnerability.
- CVSS provides a standardized severity score but should not be used in isolation.
- CPEs identify affected software products in a standardized format.
- NVD enriches vulnerability information with technical details and scoring.
- EPSS estimates the likelihood of near-term exploitation.
- KEV highlights vulnerabilities known to be actively exploited.
- SBOMs provide visibility into software dependencies, enabling faster response to newly disclosed vulnerabilities.