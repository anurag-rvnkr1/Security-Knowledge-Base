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

# Software Supply Chain Security

## Overview

Modern software is rarely built entirely from custom code.

A typical application may depend on hundreds or even thousands of third-party components downloaded from public package repositories.

Example:

```
Application

↓

Framework

↓

Libraries

↓

Dependencies

↓

Transitive Dependencies

↓

Operating System

↓

Compiler

↓

Container Image
```

Every dependency becomes part of the application's **software supply chain**.

If any component in this chain is compromised, the application itself may also become compromised.

---

# What is a Supply Chain Attack?

A supply chain attack targets the software development or distribution process instead of attacking the application directly.

Rather than exploiting your code, attackers compromise something you trust.

Example:

```
Developer

↓

Downloads Trusted Package

↓

Package is Malicious

↓

Application Built

↓

Production Deployment

↓

Attacker Gains Access
```

---

# Common Supply Chain Attack Techniques

```
Software Supply Chain

├── Dependency Confusion
├── Typosquatting
├── Malicious Packages
├── Dependency Hijacking
├── Compromised Maintainer Accounts
├── Build Pipeline Compromise
├── Signed Package Abuse
├── Container Image Poisoning
├── Compromised Updates
└── Repository Compromise
```

---

# Dependency Confusion

## Overview

Many organizations use both:

- Internal package repositories
- Public repositories

If dependency resolution prefers the public repository, an attacker may publish a package with the same name as an internal package.

---

## Example

Internal package:

```
company-utils
```

Attacker uploads:

```
company-utils
```

to a public package repository.

Build process:

```
Developer

↓

Install Dependencies

↓

Public Repository

↓

Malicious Package Installed
```

The attacker gains code execution during the build or deployment process.

---

## Prevention

- Use private package namespaces.
- Configure package manager priorities.
- Verify package sources.
- Restrict public package resolution.

---

# Typosquatting

## Overview

Attackers publish packages with names similar to legitimate packages.

Example:

Legitimate:

```
requests
```

Malicious:

```
requestss
```

or

```
requsets
```

Developers accidentally install the malicious package.

---

## Example

```
pip install requsets
```

instead of

```
pip install requests
```

The malicious package executes attacker-controlled code.

---

## Prevention

- Review package names carefully.
- Use dependency allowlists.
- Verify package maintainers.
- Automate dependency validation.

---

# Malicious Packages

## Overview

Some packages are intentionally created with malicious functionality.

Examples include:

- Credential theft
- Cryptocurrency miners
- Reverse shells
- Environment variable theft
- SSH key exfiltration

---

## Example Attack Flow

```
Developer

↓

pip install package

↓

Post-install Script

↓

Read Environment Variables

↓

Send Secrets

↓

Attacker
```

---

## Common Targets

Sensitive information often targeted includes:

- AWS credentials
- Azure credentials
- GitHub tokens
- API keys
- SSH keys
- Database passwords

---

# Dependency Hijacking

## Overview

Instead of publishing a new malicious package, attackers compromise an existing dependency.

Example:

```
Trusted Package

↓

Maintainer Account Compromised

↓

Malicious Update

↓

Millions Download Update
```

Organizations unknowingly install malware through normal updates.

---

# Compromised Maintainer Accounts

Open-source projects often rely on volunteers.

If a maintainer account is compromised:

```
Maintainer

↓

Account Compromised

↓

Publish New Version

↓

Trusted Users Install Update
```

The package remains trusted while containing malicious code.

---

# Repository Compromise

Attackers may compromise:

- Package repositories
- Mirrors
- Build infrastructure

Result:

```
Package Repository

↓

Modified Package

↓

Automatic Downloads

↓

Organization Compromised
```

---

# Build Pipeline Compromise

CI/CD pipelines have access to:

- Secrets
- Signing keys
- Cloud credentials
- Deployment systems

Attack flow:

```
Attacker

↓

CI/CD Pipeline

↓

Modify Build

↓

Malicious Release

↓

Customers Install
```

---

# Container Image Poisoning

Containers often begin with public base images.

Example:

```
FROM ubuntu:latest
```

If an attacker compromises or replaces the image source:

```
Container

↓

Malicious Base Image

↓

Production Deployment
```

---

## Prevention

- Use trusted registries.
- Pin image versions.
- Scan container images.
- Verify image signatures.

---

# Signed vs Unsigned Packages

Package signing helps verify authenticity.

Unsigned package:

```
Download

↓

No Integrity Verification
```

Signed package:

```
Download

↓

Verify Digital Signature

↓

Install
```

Digital signatures reduce the risk of tampering but do not guarantee that the package itself is free from vulnerabilities.

---

# Lock Files

Dependency versions should be fixed using lock files.

Examples:

Python

```
requirements.txt
poetry.lock
```

Node.js

```
package-lock.json
```

Yarn

```
yarn.lock
```

Go

```
go.sum
```

These files ensure consistent dependency versions across environments.

---

# Why Lock Files Matter

Without lock files:

```
Developer A

↓

Library v1.2
```

```
Developer B

↓

Library v1.5
```

Different versions may contain different vulnerabilities or behavior.

Lock files improve reproducibility and reduce unexpected updates.

---

# Package Repositories

Common package ecosystems include:

Python

- PyPI

Node.js

- npm

Java

- Maven Central

.NET

- NuGet

Ruby

- RubyGems

Go

- Go Modules

These repositories should be treated as external dependencies and monitored accordingly.

---

# Real-World Case Studies

## Log4Shell (2021)

Affected:

```
Apache Log4j
```

Impact:

- Remote Code Execution
- Widespread exploitation
- Global emergency patching efforts

---

## SolarWinds (2020)

Attackers compromised the software build process.

Result:

```
Legitimate Update

↓

Backdoor

↓

Thousands of Customers
```

This demonstrated how trusted software updates can become attack vectors.

---

## XZ Utils (2024)

Attackers inserted a backdoor into a widely used compression library after gaining influence over the project's maintenance process.

The malicious code targeted authentication workflows in specific environments before being discovered prior to broad deployment.

---

## event-stream (npm)

A widely used npm package was compromised after maintainership changed hands.

Malicious code targeted cryptocurrency wallet users.

---

## ua-parser-js

A compromised release of the package included malware capable of installing cryptocurrency miners and credential-stealing software.

---

## Codecov

Attackers modified the Codecov Bash uploader script.

Result:

```
CI/CD Pipeline

↓

Environment Variables

↓

Credentials Stolen
```

---

# Supply Chain Security Best Practices

- Maintain an inventory of all dependencies.
- Use trusted package repositories.
- Verify package signatures where supported.
- Pin dependency versions.
- Review new dependencies before adoption.
- Remove unused packages.
- Monitor security advisories.
- Scan dependencies continuously.
- Protect CI/CD pipelines.
- Use the principle of least privilege for build systems.
- Generate and maintain SBOMs.
- Regularly review transitive dependencies.

---

# Key Takeaways

- Software supply chain attacks target trusted dependencies rather than your application's own code.
- Dependency confusion, typosquatting, malicious packages, and compromised maintainers are common attack techniques.
- Lock files and trusted repositories improve dependency integrity and reproducibility.
- CI/CD pipelines and container images are high-value targets that require strong security controls.
- Continuous dependency monitoring, SBOMs, and secure build practices are essential for modern application security.

# Detection

Identifying vulnerable and outdated components requires continuous visibility into all software assets and dependencies.

Unlike traditional penetration testing, vulnerability management is an ongoing process rather than a one-time activity.

Typical detection methods include:

- Software inventory
- Dependency scanning
- Container image scanning
- Operating system vulnerability scanning
- Cloud workload scanning
- SBOM analysis
- Security advisory monitoring
- Manual verification

---

# Vulnerability Management Lifecycle

A mature vulnerability management program follows a structured process.

```
Asset Inventory

↓

Component Identification

↓

Vulnerability Detection

↓

Risk Assessment

↓

Prioritization

↓

Remediation

↓

Verification

↓

Continuous Monitoring
```

This lifecycle repeats continuously as new vulnerabilities are discovered.

---

# Dependency Scanning

Dependency scanners inspect application packages and compare them against known vulnerability databases.

Typical workflow:

```
Source Code

↓

Dependency Files

↓

Scanner

↓

CVE Database

↓

Security Report
```

Examples of dependency files:

Python

```
requirements.txt

poetry.lock
```

Node.js

```
package.json

package-lock.json
```

Java

```
pom.xml

build.gradle
```

---

# Container Image Scanning

Container images often contain:

- Operating system packages
- Runtime libraries
- Language packages
- Configuration files

Scanning should occur:

```
Image Build

↓

Vulnerability Scan

↓

Policy Validation

↓

Deployment
```

Never deploy unscanned production images.

---

# Operating System Scanning

Review:

- Installed packages
- Kernel version
- Security updates
- Running services
- End-of-life software

Outdated operating systems often expose well-known vulnerabilities.

---

# Cloud Workload Assessment

Review cloud workloads for:

- Unsupported operating systems
- Outdated container images
- Vulnerable virtual machines
- Unpatched managed services
- Deprecated runtimes

---

# Software Bill of Materials (SBOM) Analysis

SBOMs enable rapid impact assessment.

Example:

```
New CVE Released

↓

Search SBOM

↓

Affected Applications

↓

Prioritize Patching
```

Without an SBOM, organizations may spend significant time determining where vulnerable components are used.

---

# Security Advisory Monitoring

Organizations should continuously monitor:

- Vendor advisories
- Open-source project announcements
- Operating system updates
- Cloud provider bulletins
- National vulnerability databases

Timely awareness shortens remediation time.

---

# Patch Management Lifecycle

Applying patches safely requires planning.

```
Vendor Releases Patch

↓

Review Advisory

↓

Assess Business Impact

↓

Test in Non-Production

↓

Approval

↓

Production Deployment

↓

Verification

↓

Documentation
```

Emergency patches may require an accelerated process, but validation remains important.

---

# Risk-Based Prioritization

Not every vulnerability requires the same response.

Consider:

Technical Factors

- CVSS score
- EPSS score
- Known exploitation
- Ease of exploitation

Business Factors

- Internet exposure
- Asset criticality
- Sensitive data
- Regulatory requirements
- Availability requirements

Prioritize based on overall risk rather than severity alone.

---

# Common Detection Tools

| Tool | Primary Purpose |
|------|-----------------|
| OWASP Dependency-Check | Detect vulnerable application dependencies |
| Trivy | Scan containers, file systems, repositories, and IaC |
| Snyk | Identify and remediate dependency vulnerabilities |
| Dependabot | Automated dependency update suggestions |
| osv-scanner | Scan projects using the Open Source Vulnerability database |
| Syft | Generate Software Bills of Materials (SBOMs) |
| Grype | Scan SBOMs and container images for vulnerabilities |
| GitHub Code Scanning | Security analysis integrated with GitHub repositories |

---

# Prevention

Effective prevention combines secure development practices with continuous monitoring.

---

## 1. Maintain a Software Inventory

Know exactly which:

- Libraries
- Frameworks
- Operating systems
- Containers
- Third-party services

are used throughout the environment.

An accurate inventory is the foundation of vulnerability management.

---

## 2. Remove Unused Components

Unused software increases attack surface.

Regularly remove:

- Obsolete libraries
- Legacy frameworks
- Unused plugins
- Deprecated APIs
- Test packages

---

## 3. Keep Components Updated

Adopt a regular update schedule.

Balance:

- Security
- Stability
- Compatibility

Avoid remaining on unsupported versions without a documented business justification.

---

## 4. Verify Package Integrity

Before installing packages:

- Confirm the package source.
- Verify checksums or signatures where available.
- Review maintainers for unfamiliar projects.
- Prefer official repositories.

---

## 5. Secure the Software Supply Chain

Protect:

- Source repositories
- Build systems
- CI/CD pipelines
- Artifact repositories
- Deployment infrastructure

Compromising any of these can affect downstream software.

---

## 6. Generate and Maintain SBOMs

An SBOM should be generated for each release.

Benefits include:

- Faster incident response
- Easier compliance
- Improved dependency visibility
- Simplified vulnerability tracking

---

## 7. Continuous Monitoring

Security does not end after deployment.

Continuously monitor:

- New CVEs
- Vendor advisories
- Dependency updates
- End-of-life announcements
- Threat intelligence

---

# Best Practices

✔ Maintain complete asset inventories.

✔ Remove unused software.

✔ Update dependencies regularly.

✔ Scan applications during development.

✔ Scan containers before deployment.

✔ Generate SBOMs.

✔ Monitor security advisories.

✔ Use trusted repositories.

✔ Protect CI/CD pipelines.

✔ Apply risk-based prioritization.

✔ Validate patches before production deployment.

✔ Automate dependency updates where appropriate.

---

# Practical Lab

## Objective

Assess an application for vulnerable and outdated components.

---

## Scenario

Application stack:

- Ubuntu Server
- Docker
- Nginx
- Python
- Django
- PostgreSQL

---

## Tasks

1. Inventory installed components.
2. Generate an SBOM.
3. Scan dependencies for known vulnerabilities.
4. Scan the container image.
5. Identify outdated software.
6. Prioritize findings based on business risk.
7. Recommend remediation.
8. Produce a vulnerability management report.

---

## Expected Learning Outcomes

After completing this lab, you should be able to:

- Identify vulnerable components.
- Understand dependency relationships.
- Interpret CVE and CVSS information.
- Prioritize remediation activities.
- Recommend secure update strategies.

---

# Interview Questions

## Beginner

### What is a vulnerable component?

A software library, framework, operating system, container image, or other dependency that contains a known security vulnerability.

---

### What is a CVE?

A Common Vulnerabilities and Exposures (CVE) identifier is a unique identifier assigned to a publicly disclosed security vulnerability.

---

### What is an SBOM?

A Software Bill of Materials is an inventory of all software components and dependencies used within an application.

---

## Intermediate

### What is the difference between CVE and CWE?

A CVE identifies a specific publicly disclosed vulnerability, while a CWE describes the general class of software weakness that can lead to vulnerabilities.

---

### Why are transitive dependencies important?

Applications may indirectly include vulnerable packages through other libraries. These transitive dependencies can introduce security risks even when developers did not explicitly install them.

---

### Why shouldn't organizations always apply every update immediately?

Updates may introduce compatibility issues or operational risks. Mature organizations assess risk, test changes, and deploy updates through a controlled patch management process.

---

## Advanced

### How would you build a vulnerability management program?

A comprehensive program includes:

1. Asset inventory.
2. Dependency inventory.
3. Continuous vulnerability scanning.
4. SBOM generation.
5. Risk-based prioritization.
6. Patch management.
7. Verification.
8. Continuous monitoring and reporting.

---

### Explain how you would respond to a critical zero-day affecting a widely used library.

A structured response includes:

1. Identify affected assets using inventories and SBOMs.
2. Assess exposure and business impact.
3. Apply temporary mitigations if available.
4. Test vendor patches or workarounds.
5. Deploy fixes according to emergency change procedures.
6. Verify remediation.
7. Monitor for signs of exploitation.
8. Document lessons learned and improve response processes.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP Dependency-Check
- OWASP CycloneDX

## NIST

- NIST Secure Software Development Framework (SSDF)
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53

## CISA

- Known Exploited Vulnerabilities (KEV) Catalog
- Secure by Design Guidance

## OpenSSF

- OpenSSF Scorecard
- OpenSSF Best Practices

## Supply Chain Security

- CycloneDX
- SPDX
- Sigstore

---

# Summary

Vulnerable and Outdated Components remain one of the most significant risks in modern software because applications rely extensively on third-party libraries, frameworks, operating systems, containers, and cloud services. Effective management requires maintaining accurate inventories, generating Software Bills of Materials (SBOMs), continuously monitoring security advisories, scanning dependencies, protecting the software supply chain, and applying risk-based patch management.

Organizations that integrate vulnerability management into the Secure Software Development Lifecycle (SSDLC) are better positioned to reduce exposure, respond quickly to newly disclosed vulnerabilities, and maintain resilient software systems.