# Shared Responsibility Model

## Introduction

Cloud computing fundamentally changes how organizations build, deploy, and operate technology solutions. Unlike traditional on-premises environments, where organizations are responsible for every aspect of the infrastructure, cloud computing introduces a **shared security and operational responsibility** between the cloud service provider (CSP) and the customer.

This concept is known as the **Shared Responsibility Model (SRM)**.

The Shared Responsibility Model is one of the **most important concepts in cloud security** and serves as the foundation for understanding security, compliance, governance, risk management, and operational accountability in cloud environments.

A common misconception is:

> **"If my applications are hosted in the cloud, the cloud provider secures everything."**

This assumption is incorrect.

Cloud providers secure the cloud infrastructure, but customers remain responsible for securing their workloads, applications, identities, configurations, and data.

Failure to understand this division of responsibility has resulted in numerous real-world cloud security incidents involving:

- Publicly exposed storage buckets
- Overly permissive IAM policies
- Stolen API keys
- Misconfigured databases
- Unpatched virtual machines
- Insecure APIs
- Data breaches
- Compliance violations
- Ransomware attacks

Understanding exactly **who is responsible for what** is essential for every:

- Cloud Security Engineer
- Cloud Architect
- DevOps Engineer
- DevSecOps Engineer
- Site Reliability Engineer
- Security Analyst
- Compliance Officer
- Risk Manager
- Application Developer

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the Shared Responsibility Model.
- Learn why shared responsibility exists.
- Differentiate provider and customer responsibilities.
- Understand responsibility across IaaS, PaaS, and SaaS.
- Learn the security responsibilities of cloud customers.
- Understand provider obligations.
- Analyze real-world responsibility scenarios.
- Identify common misconceptions.
- Apply the model during cloud security assessments.
- Understand compliance implications.

---

# What is the Shared Responsibility Model?

The Shared Responsibility Model is a security framework that clearly defines which security and operational responsibilities belong to the **Cloud Service Provider (CSP)** and which belong to the **Customer**.

Instead of transferring all security responsibilities to the provider, cloud computing distributes them between both parties.

```
                 Cloud Security

                       │

        ┌──────────────┴──────────────┐

        ▼                             ▼

 Cloud Provider                Customer

(Security OF Cloud)      (Security IN Cloud)
```

Both parties must fulfill their responsibilities to achieve a secure cloud environment.

---

# Why Does Shared Responsibility Exist?

Cloud providers own and operate massive global infrastructures that serve thousands or millions of customers.

It would be impractical—and undesirable—for providers to manage every customer's:

- Applications
- Business logic
- User accounts
- Sensitive data
- Internal policies
- Regulatory requirements

Similarly, customers cannot control the provider's:

- Physical data centers
- Hypervisors
- Networking backbone
- Hardware lifecycle
- Environmental controls

The Shared Responsibility Model creates a clear boundary between these areas of control.

---

# Security of the Cloud vs Security in the Cloud

One of the simplest ways to understand the model is by separating responsibilities into two categories.

## Security **of** the Cloud

This refers to protecting the infrastructure that delivers cloud services.

Examples include:

- Physical security
- Data centers
- Server hardware
- Storage hardware
- Networking equipment
- Hypervisors
- Core cloud services
- Availability Zones
- Physical access controls

These responsibilities belong primarily to the cloud provider.

---

## Security **in** the Cloud

This refers to everything customers deploy, configure, and manage inside the cloud.

Examples include:

- Virtual machines
- Applications
- Databases
- Identity and Access Management (IAM)
- Encryption configuration
- Firewall rules
- Operating system patching (IaaS)
- Secrets management
- Customer data
- Compliance settings

These responsibilities belong primarily to the customer.

---

# Visualizing the Responsibility Boundary

```
                    Cloud Service

┌─────────────────────────────────────────────┐

       Customer Responsibilities

       • Data

       • Identity

       • Applications

       • Configurations

       • Operating Systems*

       • Network Rules*

─────────────────────────────────────────────

       Provider Responsibilities

       • Physical Security

       • Hardware

       • Networking

       • Storage Infrastructure

       • Hypervisor

       • Data Centers

└─────────────────────────────────────────────┘

*Depends on the cloud service model.
```

---

# Why This Model Matters

Organizations that misunderstand responsibility boundaries often assume the provider secures everything.

This misconception frequently leads to:

- Weak IAM policies
- Publicly accessible storage
- Unpatched virtual machines
- Poor key management
- Misconfigured security groups
- Data leaks
- Compliance failures

A cloud provider cannot prevent many of these issues because they occur within the customer's area of responsibility.

---

# Core Principles of the Shared Responsibility Model

Every cloud provider follows similar high-level principles.

## Principle 1 – Ownership Determines Responsibility

The party that controls a resource is generally responsible for securing it.

Example:

```
Cloud Provider

↓

Physical Server

↓

Provider Responsibility

----------------------------

Customer

↓

Application

↓

Customer Responsibility
```

---

## Principle 2 – Responsibility Changes with Service Model

Customer responsibilities vary depending on whether the organization uses:

- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)
- Software as a Service (SaaS)

As managed services increase, customer infrastructure responsibilities decrease.

---

## Principle 3 – Security is Collaborative

Security is not owned exclusively by either party.

```
Cloud Provider

        +

Customer

        =

Secure Cloud Environment
```

Weaknesses on either side can impact the overall security posture.

---

# Shared Responsibility Across Service Models

Responsibility shifts depending on the level of abstraction.

```
More Customer Control
        │
        ▼

Infrastructure as a Service (IaaS)

Platform as a Service (PaaS)

Software as a Service (SaaS)

        ▲
        │

More Provider Management
```

Understanding these shifts is essential when designing secure cloud architectures.

---

# Enterprise Example

A company deploys an online banking application.

The cloud provider secures:

- Physical servers
- Storage hardware
- Networking
- Hypervisor
- Data center facilities

The bank secures:

- Customer accounts
- MFA policies
- Databases
- Application code
- Encryption keys
- Firewall rules
- Virtual machines (if using IaaS)
- Compliance controls

Both organizations contribute to the application's overall security.

---

# Common Misconceptions

## "The cloud provider patches my virtual machines."

Not always.

In Infrastructure as a Service, customers are generally responsible for operating system updates.

---

## "My cloud storage is automatically private."

Incorrect.

Customers typically configure storage permissions and access policies.

Misconfigured storage remains one of the most common causes of cloud data exposure.

---

## "Compliance is handled entirely by the provider."

Incorrect.

While providers obtain certifications for their infrastructure, customers remain responsible for operating compliant workloads and handling regulated data appropriately.

---

## "Using cloud services eliminates cybersecurity risks."

Cloud computing changes risk—it does not eliminate it.

Organizations must continue implementing:

- Identity management
- Encryption
- Logging
- Monitoring
- Incident response
- Vulnerability management
- Secure application development

---

# Benefits of Understanding the Shared Responsibility Model

Organizations that correctly implement the model gain:

- Clear accountability
- Better governance
- Improved compliance
- Reduced security gaps
- Faster incident response
- Better audit readiness
- Lower operational risk
- Improved cloud architecture
- Stronger Zero Trust implementation
- Better security investments

---

# Best Practices

- Clearly document provider and customer responsibilities.
- Train engineering teams on shared responsibility concepts.
- Continuously review cloud configurations.
- Apply the Principle of Least Privilege.
- Enable centralized logging and monitoring.
- Regularly review IAM policies.
- Patch customer-managed resources promptly.
- Understand responsibility changes before adopting new cloud services.
- Incorporate the model into security reviews and risk assessments.
- Validate controls through regular audits and penetration testing.

---

# Common Mistakes

Avoid the following pitfalls:

- Assuming the cloud provider secures customer applications.
- Ignoring customer-managed identity and access controls.
- Leaving cloud resources with default or overly permissive configurations.
- Misunderstanding responsibilities when moving from IaaS to PaaS or SaaS.
- Treating compliance certifications as complete security coverage.
- Failing to document ownership of cloud resources.
- Neglecting continuous monitoring of customer-managed assets.
- Assuming cloud-native services require no security configuration.

---

# Key Takeaways

- The Shared Responsibility Model defines how security and operational responsibilities are divided between the cloud provider and the customer.
- Providers focus on securing the cloud infrastructure, while customers secure the workloads, identities, applications, configurations, and data they deploy.
- Responsibility boundaries shift depending on the cloud service model.
- Understanding the model reduces security gaps, improves compliance, and establishes clear operational accountability.
- Every successful cloud security program begins with a thorough understanding of the Shared Responsibility Model.

---

## Shared Responsibility Across IaaS, PaaS, and SaaS

One of the most important aspects of the Shared Responsibility Model is that **customer responsibilities change depending on the cloud service model** being used.

Many cloud security incidents occur because organizations incorrectly assume that moving from Infrastructure as a Service (IaaS) to Platform as a Service (PaaS) or Software as a Service (SaaS) completely removes their security obligations.

While cloud providers assume more operational responsibility as services become increasingly managed, **customers always retain responsibility for protecting their data, identities, configurations, and business processes.**

Understanding these differences is essential for designing secure cloud environments.

---

# Learning Objectives

After completing this section, you will be able to:

- Understand how responsibilities differ across cloud service models.
- Compare IaaS, PaaS, and SaaS security responsibilities.
- Identify customer-managed and provider-managed components.
- Understand operational ownership.
- Learn security implications of managed services.
- Analyze enterprise deployment examples.
- Understand responsibility transitions during cloud adoption.
- Identify common mistakes made in each service model.

---

# Responsibility Progression

As cloud services become more managed, provider responsibilities increase while customer infrastructure responsibilities decrease.

```
Customer Responsibility

██████████████████████████

Infrastructure as a Service

███████████████

Platform as a Service

██████

Software as a Service

↓

Provider Responsibility Increases
```

This shift only affects infrastructure management—not ownership of business data.

---

# Understanding the Layers

Most cloud environments can be viewed as a stack of components.

```
Applications

Data

Identity & Access

Operating System

Runtime

Middleware

Virtualization

Servers

Storage

Networking

Physical Data Center
```

Responsibility for each layer depends on the service model.

---

# Infrastructure as a Service (IaaS)

## Overview

Infrastructure as a Service provides customers with virtualized computing resources while allowing them significant control over the operating environment.

The cloud provider supplies the infrastructure.

The customer manages almost everything above virtualization.

Examples include:

- Virtual Machines
- Virtual Networks
- Block Storage
- Load Balancers
- Virtual Firewalls

IaaS offers maximum flexibility but also carries the highest customer security responsibility.

---

# IaaS Responsibility Diagram

```
Infrastructure as a Service

────────────────────────────────────

Customer Manages

✔ Applications

✔ Data

✔ Identity

✔ Network Configuration

✔ Firewalls

✔ Operating System

✔ Middleware

✔ Runtime

────────────────────────────────────

Provider Manages

✔ Virtualization

✔ Physical Servers

✔ Storage Hardware

✔ Networking Hardware

✔ Data Centers
```

---

# Customer Responsibilities in IaaS

The customer is responsible for securing:

- Operating systems
- Virtual machine hardening
- Security patches
- Installed software
- User accounts
- IAM policies
- Firewalls
- Security groups
- Network ACLs
- Application security
- Data encryption
- Backup configuration
- Endpoint protection
- Vulnerability management
- Logging and monitoring

Failure in any of these areas can expose cloud workloads despite secure infrastructure.

---

# Provider Responsibilities in IaaS

The provider secures:

- Physical facilities
- Building access
- Hardware lifecycle
- Power systems
- Cooling
- Physical networking
- Hypervisors
- Hardware replacement
- Infrastructure availability
- Core cloud services

Customers generally have no direct control over these components.

---

# IaaS Example

A company launches virtual machines hosting an online retail application.

```
Customer

↓

Deploy Virtual Machine

↓

Install Linux

↓

Configure Firewall

↓

Install Web Server

↓

Deploy Application

↓

Manage Updates
```

Meanwhile, the cloud provider maintains:

- Physical servers
- Storage devices
- Hypervisors
- Data centers

---

# Security Risks in IaaS

Common customer mistakes include:

- Unpatched operating systems
- Weak SSH configurations
- Open management ports
- Default credentials
- Excessive IAM permissions
- Public storage exposure
- Poor key management
- Disabled logging
- Weak backup strategies

These issues remain customer responsibilities.

---

# Platform as a Service (PaaS)

## Overview

Platform as a Service abstracts much of the underlying infrastructure.

Instead of managing operating systems and middleware, customers focus primarily on developing and deploying applications.

Typical PaaS services include:

- Managed databases
- Application hosting platforms
- Container platforms
- Serverless runtimes
- Managed Kubernetes services (shared responsibilities vary)

PaaS accelerates development while reducing infrastructure management.

---

# PaaS Responsibility Diagram

```
Platform as a Service

────────────────────────────────────

Customer Manages

✔ Applications

✔ Data

✔ Identity

✔ Access Policies

✔ Configuration

────────────────────────────────────

Provider Manages

✔ Runtime

✔ Middleware

✔ Operating System

✔ Virtualization

✔ Servers

✔ Storage

✔ Networking

✔ Physical Infrastructure
```

---

# Customer Responsibilities in PaaS

Customers remain responsible for:

- Application code
- Secure coding practices
- Authentication
- Authorization
- API security
- Secrets management
- Encryption configuration
- Business logic
- IAM
- Data classification
- Compliance
- Logging configuration
- Access reviews

Although infrastructure management decreases, application security becomes even more critical.

---

# Provider Responsibilities in PaaS

The provider manages:

- Runtime updates
- Middleware
- Operating system patches
- Infrastructure scaling
- High availability
- Storage systems
- Networking
- Hypervisors
- Physical hardware

This reduces operational overhead for customers.

---

# Enterprise Example

A software company deploys a web application using a managed application platform.

Customer responsibilities:

- Develop application
- Secure APIs
- Configure authentication
- Protect customer data

Provider responsibilities:

- Patch operating systems
- Manage runtime
- Replace failed hardware
- Scale infrastructure
- Maintain availability

---

# Security Risks in PaaS

Typical mistakes include:

- Hardcoded API keys
- Weak authentication
- Vulnerable application code
- Insecure APIs
- Excessive privileges
- Improper secret management
- Missing encryption
- Poor application logging

Infrastructure security alone cannot protect vulnerable applications.

---

# Software as a Service (SaaS)

## Overview

Software as a Service provides complete applications over the internet.

Customers consume the application without managing infrastructure, operating systems, or application deployments.

Examples include:

- Email platforms
- CRM systems
- Office productivity suites
- Collaboration tools
- HR platforms
- Accounting software

The provider manages almost the entire technology stack.

---

# SaaS Responsibility Diagram

```
Software as a Service

────────────────────────────────────

Customer Manages

✔ Users

✔ Identity

✔ Access Permissions

✔ Data

✔ Information Sharing

✔ Compliance Configuration

────────────────────────────────────

Provider Manages

✔ Applications

✔ Runtime

✔ Middleware

✔ Operating System

✔ Virtualization

✔ Servers

✔ Storage

✔ Networking

✔ Physical Infrastructure
```

---

# Customer Responsibilities in SaaS

Although SaaS requires the least infrastructure management, customers still control critical security areas.

Responsibilities include:

- User lifecycle management
- MFA enforcement
- Password policies
- Role assignments
- Data ownership
- Sharing permissions
- Information classification
- Compliance configuration
- Third-party integrations
- Security awareness training

These responsibilities directly affect organizational security.

---

# Provider Responsibilities in SaaS

The provider manages:

- Entire application
- Infrastructure
- Updates
- Feature deployment
- Bug fixes
- Platform availability
- Runtime
- Operating systems
- Storage infrastructure
- Physical security

Customers generally cannot modify these components.

---

# Enterprise Example

An organization adopts a cloud-based email service.

Provider responsibilities:

- Operate email platform
- Patch servers
- Maintain infrastructure
- Provide availability

Customer responsibilities:

- Enable MFA
- Configure spam policies
- Manage user accounts
- Assign permissions
- Classify sensitive information
- Configure data retention policies

---

# Responsibility Comparison Matrix

| Component | IaaS | PaaS | SaaS |
|------------|------|------|------|
| Data | Customer | Customer | Customer |
| Identity & Access | Customer | Customer | Customer |
| Applications | Customer | Customer | Provider |
| Runtime | Customer | Provider | Provider |
| Middleware | Customer | Provider | Provider |
| Operating System | Customer | Provider | Provider |
| Virtualization | Provider | Provider | Provider |
| Physical Servers | Provider | Provider | Provider |
| Storage Hardware | Provider | Provider | Provider |
| Physical Networking | Provider | Provider | Provider |
| Data Center | Provider | Provider | Provider |

---

# Responsibility Shift Visualization

```
Physical Infrastructure

Provider
██████████████████████████

────────────────────────────

Virtualization

Provider
██████████████████████████

────────────────────────────

Operating System

IaaS → Customer

PaaS → Provider

SaaS → Provider

────────────────────────────

Applications

IaaS → Customer

PaaS → Customer

SaaS → Provider

────────────────────────────

Data

Customer

Across All Models
```

Notice that **data ownership remains with the customer in every service model**.

---

# Real-World Scenario

Consider an employee whose SaaS account is compromised because Multi-Factor Authentication (MFA) was disabled.

```
Attacker

↓

Stolen Password

↓

Login Successful

↓

Sensitive Data Access
```

Who is responsible?

The SaaS provider successfully secured:

- Infrastructure
- Servers
- Application

However, the customer failed to:

- Enforce MFA
- Monitor account activity
- Review user permissions

This incident falls within the customer's area of responsibility.

---

# Responsibility During Cloud Migration

Organizations often migrate through multiple service models.

```
Traditional Data Center

↓

Infrastructure as a Service

↓

Platform as a Service

↓

Software as a Service
```

At each stage:

- Infrastructure management decreases.
- Application responsibility changes.
- Operational complexity shifts.
- Identity and data remain customer responsibilities.

Migration planning should account for these transitions.

---

# Common Misunderstandings

### "The provider patches everything."

Only true for managed components.

Customer-managed virtual machines still require patching.

---

### "Managed database means I don't secure it."

Incorrect.

Customers still manage:

- Database accounts
- Access policies
- Encryption settings
- Backup policies (depending on service)
- Sensitive data

---

### "SaaS means no security work."

Incorrect.

Identity, permissions, information governance, compliance, and user education remain customer responsibilities.

---

# Best Practices

- Identify responsibilities before deploying workloads.
- Document ownership for every cloud resource.
- Train teams on service-model differences.
- Implement least-privilege access across all environments.
- Continuously monitor customer-managed assets.
- Review provider documentation for managed services.
- Apply encryption and strong identity controls consistently.
- Include shared responsibility reviews during architecture assessments.
- Validate responsibilities during security audits.
- Regularly reassess responsibilities as services evolve.

---

# Common Mistakes

Avoid the following pitfalls:

- Assuming managed services eliminate security obligations.
- Neglecting IAM because infrastructure is provider-managed.
- Forgetting to patch customer-managed virtual machines.
- Misconfiguring managed storage services.
- Ignoring SaaS permission reviews.
- Confusing provider compliance certifications with customer compliance.
- Leaving customer data unencrypted.
- Failing to understand responsibility boundaries before cloud migration.

---

# Key Takeaways

- Customer responsibilities decrease as organizations move from IaaS to PaaS and SaaS, but they never disappear.
- In IaaS, customers manage operating systems, applications, identities, configurations, and data.
- In PaaS, infrastructure management shifts largely to the provider, while customers remain responsible for applications, identities, and data.
- In SaaS, providers manage the complete application platform, but customers continue to own user management, access control, data protection, and compliance.
- Regardless of the service model, protecting identities, configurations, and business data remains a fundamental customer responsibility.

---

## Next Section

The next section explores **Detailed Customer Responsibilities**, covering Identity and Access Management (IAM), data protection, encryption, operating system security, application security, network security, vulnerability management, logging, monitoring, incident response, compliance, and governance in enterprise cloud environments.