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

# Detailed Customer Responsibilities

## Introduction

One of the biggest misconceptions in cloud computing is that once workloads are deployed to the cloud, security becomes the sole responsibility of the cloud provider.

In reality, regardless of whether an organization uses Infrastructure as a Service (IaaS), Platform as a Service (PaaS), or Software as a Service (SaaS), **customers always retain responsibility for securing everything they own, configure, deploy, or control.**

Cloud providers secure the underlying infrastructure, but customers remain responsible for protecting their:

- Data
- Users
- Identities
- Applications
- Configurations
- Access permissions
- Business processes
- Compliance requirements

In most real-world cloud security incidents, investigations reveal that the cloud provider's infrastructure was functioning securely. The breach occurred because customer-managed resources were improperly configured, insufficiently monitored, or inadequately protected.

Understanding customer responsibilities is therefore essential for building a secure cloud environment.

---

# Learning Objectives

After completing this section, you will be able to:

- Understand customer responsibilities within the Shared Responsibility Model.
- Learn Identity and Access Management (IAM) responsibilities.
- Understand data protection obligations.
- Learn encryption responsibilities.
- Understand network security ownership.
- Learn operating system security responsibilities.
- Understand application security obligations.
- Learn vulnerability and patch management.
- Understand logging and monitoring responsibilities.
- Learn compliance and governance responsibilities.
- Analyze enterprise customer security practices.

---

# Overview of Customer Responsibilities

Although responsibilities vary slightly across cloud service models, customers are generally responsible for securing the following areas:

```
Customer Responsibilities

│

├── Identity & Access Management

├── Data Protection

├── Encryption

├── Operating Systems*

├── Applications

├── Network Configuration*

├── Firewalls*

├── Secrets Management

├── Logging

├── Monitoring

├── Vulnerability Management

├── Compliance

├── Governance

├── Backup Strategy

├── Incident Response

└── Security Awareness

*Primarily in IaaS and partially in PaaS.
```

Each area contributes to the organization's overall cloud security posture.

---

# Identity and Access Management (IAM)

## Overview

Identity is the new security perimeter in cloud computing.

Unlike traditional environments that relied heavily on network boundaries, modern cloud platforms primarily depend on **Identity and Access Management (IAM)** to determine who can access resources and what actions they are permitted to perform.

Customers are fully responsible for configuring IAM correctly.

---

# IAM Responsibilities

Customers should manage:

- User accounts
- Service accounts
- Roles
- Groups
- Policies
- Authentication methods
- Authorization rules
- Temporary credentials
- Federated identities
- API credentials

Poor IAM configuration remains one of the leading causes of cloud security incidents.

---

# Least Privilege Principle

Every identity should receive only the minimum permissions required.

```
Developer

↓

Read Source Code

Deploy Application

────────────────────

Not Allowed

Delete Databases

Manage Billing

Modify IAM Policies
```

Excessive permissions increase the impact of compromised accounts.

---

# Multi-Factor Authentication (MFA)

Customers should enable MFA for:

- Administrative accounts
- Privileged users
- Remote access
- Cloud consoles
- Identity providers

```
User

↓

Password

+

MFA

↓

Cloud Console
```

MFA significantly reduces the risk of credential-based attacks.

---

# Identity Lifecycle Management

Organizations should manage user identities throughout their lifecycle.

```
Employee Joins

↓

Account Created

↓

Permissions Assigned

↓

Role Changes

↓

Permissions Updated

↓

Employee Leaves

↓

Account Disabled

↓

Account Removed
```

Inactive accounts present unnecessary security risks.

---

# Data Protection

## Overview

Cloud providers store customer data, but **customers own and are responsible for protecting that data**.

Security responsibilities include:

- Classification
- Access control
- Encryption
- Backup
- Retention
- Secure deletion
- Data lifecycle management

---

# Data Classification

Organizations should classify information according to sensitivity.

Example:

```
Data

│

├── Public

├── Internal

├── Confidential

└── Restricted
```

Different classifications require different protection levels.

---

# Data Access Control

Access should follow business requirements.

```
Finance Records

↓

Finance Team

────────────────────

Engineering Team

↓

Access Denied
```

Access reviews should be conducted regularly.

---

# Data Lifecycle

```
Data Created

↓

Stored

↓

Used

↓

Archived

↓

Deleted Securely
```

Security controls should exist throughout every phase.

---

# Encryption Responsibilities

## Encryption in Transit

Customers should ensure sensitive communications use secure protocols.

Examples include:

- HTTPS
- TLS
- SSH
- VPN tunnels

```
User

↓

TLS Encryption

↓

Cloud Service
```

Unencrypted communication may expose sensitive information.

---

## Encryption at Rest

Stored information should also be encrypted.

Examples:

- Databases
- Object storage
- Virtual disks
- Backups
- Snapshots

Encryption reduces the impact of physical media compromise and unauthorized storage access.

---

## Encryption Key Management

Customers should define:

- Key ownership
- Rotation schedules
- Access permissions
- Backup procedures
- Revocation processes

Poor key management can render encryption ineffective.

---

# Secrets Management

Applications often require sensitive credentials.

Examples include:

- API keys
- Database passwords
- OAuth tokens
- Certificates
- Encryption keys

These secrets should never be:

- Hardcoded
- Stored in source code
- Shared via email
- Embedded in container images

Instead, use dedicated secrets management solutions.

```
Application

↓

Secrets Manager

↓

Credential Retrieved

↓

Secure Connection
```

---

# Operating System Security

*(Primarily applicable to Infrastructure as a Service)*

Customers managing virtual machines are responsible for securing their operating systems.

Responsibilities include:

- OS hardening
- Patch management
- Malware protection
- User management
- Secure configuration
- File permissions
- System auditing

---

# Operating System Hardening

Examples include:

- Disable unnecessary services.
- Remove unused software.
- Restrict administrative access.
- Enable host-based firewalls.
- Configure secure logging.
- Apply secure baseline configurations.

Hardening reduces the attack surface.

---

# Patch Management

Keeping systems updated is a customer responsibility in IaaS.

```
Security Update Released

↓

Testing

↓

Deployment

↓

Verification

↓

Documentation
```

Delaying security patches increases exposure to known vulnerabilities.

---

# Network Security

Customers configure logical network security even though providers manage the physical network.

Responsibilities include:

- Virtual Private Clouds (VPCs)
- Subnets
- Route tables
- Security Groups
- Network ACLs
- VPN configuration
- Private endpoints
- DNS configuration

---

# Network Segmentation

Sensitive systems should be isolated.

```
Internet

↓

Public Subnet

↓

Application Tier

↓

Private Subnet

↓

Database Tier
```

Segmentation limits lateral movement.

---

# Firewall Configuration

Example:

```
Internet

↓

Web Firewall

↓

Application

↓

Database Firewall

↓

Database
```

Only required ports should be opened.

---

# Application Security

Applications remain the customer's responsibility in both IaaS and PaaS.

Responsibilities include:

- Secure coding
- Authentication
- Authorization
- Session management
- Input validation
- API security
- Dependency management
- Secure deployment

---

# Secure Software Development Lifecycle (SSDLC)

```
Requirements

↓

Design

↓

Development

↓

Security Testing

↓

Deployment

↓

Monitoring

↓

Maintenance
```

Security should be integrated throughout the development lifecycle rather than added after deployment.

---

# API Security

Customers should secure APIs using:

- Authentication
- Authorization
- Rate limiting
- Input validation
- TLS encryption
- Logging
- Monitoring
- API gateways

APIs often represent the primary attack surface for cloud-native applications.

---

# Vulnerability Management

Customers should continuously identify and remediate vulnerabilities.

Typical activities include:

- Vulnerability scanning
- Patch verification
- Risk assessment
- Penetration testing
- Configuration reviews
- Dependency scanning

---

# Vulnerability Management Lifecycle

```
Discover

↓

Assess

↓

Prioritize

↓

Remediate

↓

Verify

↓

Monitor
```

This process should be continuous rather than periodic.

---

# Logging Responsibilities

Customers should configure comprehensive logging.

Important logs include:

- Authentication events
- Administrative actions
- API activity
- Network changes
- Database access
- Security alerts
- Application logs
- Audit events

Logs support investigations and compliance.

---

# Monitoring Responsibilities

Monitoring should cover:

- Infrastructure health
- Security events
- User activity
- API traffic
- Resource utilization
- Configuration drift
- Suspicious behavior
- Threat detection

```
Cloud Resources

↓

Monitoring

↓

Alert

↓

Security Team

↓

Response
```

Continuous monitoring enables early detection of malicious activity.

---

# Backup Responsibilities

Even when cloud providers offer backup services, customers remain responsible for defining backup strategies.

Organizations should determine:

- Backup frequency
- Retention periods
- Encryption
- Recovery objectives
- Geographic redundancy
- Restoration testing

A backup that has never been restored cannot be assumed to be usable.

---

# Incident Response

Customers should establish documented incident response procedures.

Typical lifecycle:

```
Preparation

↓

Detection

↓

Analysis

↓

Containment

↓

Eradication

↓

Recovery

↓

Lessons Learned
```

Cloud providers assist with infrastructure availability, but customers respond to incidents affecting their workloads.

---

# Compliance Responsibilities

Organizations remain responsible for meeting regulatory obligations.

Examples include:

- Data residency
- Privacy laws
- Audit evidence
- Access reviews
- Retention policies
- Risk assessments
- Security documentation

Provider certifications do not automatically make customer workloads compliant.

---

# Governance Responsibilities

Cloud governance includes:

- Policy management
- Cost governance
- Resource ownership
- Change management
- Risk management
- Configuration standards
- Security baselines
- Continuous compliance

Governance ensures cloud environments remain secure and consistent over time.

---

# Enterprise Example

A healthcare provider hosts a patient management system in the cloud.

Customer responsibilities include:

- Configuring IAM
- Enforcing MFA
- Encrypting patient records
- Securing APIs
- Managing operating system patches
- Monitoring user activity
- Maintaining compliance documentation
- Performing vulnerability assessments

The cloud provider secures:

- Physical servers
- Storage hardware
- Hypervisors
- Networking infrastructure
- Data center facilities

Both parties must fulfill their responsibilities to maintain a secure environment.

---

# Common Customer Security Failures

Many cloud incidents originate from preventable mistakes.

Examples include:

- Publicly accessible storage buckets
- Weak IAM policies
- Disabled MFA
- Hardcoded secrets
- Unpatched virtual machines
- Exposed management ports
- Poor API authentication
- Missing encryption
- Inadequate logging
- Unmonitored privileged accounts

Most of these failures occur within the customer's area of responsibility.

---

# Best Practices

- Apply the Principle of Least Privilege to every identity.
- Enable MFA for all privileged accounts.
- Encrypt sensitive data in transit and at rest.
- Regularly rotate credentials and encryption keys.
- Harden operating systems and cloud workloads.
- Continuously patch customer-managed resources.
- Secure APIs with strong authentication and authorization.
- Centralize logging and continuous monitoring.
- Perform regular vulnerability assessments and penetration tests.
- Test backup restoration and incident response procedures periodically.

---

# Common Mistakes

Avoid the following pitfalls:

- Assuming cloud providers manage customer identities.
- Granting excessive permissions to users or services.
- Storing secrets in application source code.
- Leaving virtual machines unpatched.
- Ignoring API security controls.
- Disabling logging to reduce storage costs.
- Failing to review backup and recovery processes.
- Treating compliance as a one-time activity rather than a continuous process.

---

# Key Takeaways

- Customers remain responsible for securing everything they deploy, configure, manage, or control within the cloud.
- Identity, data protection, encryption, applications, configurations, logging, monitoring, and governance are core customer responsibilities across all cloud service models.
- In IaaS, customers additionally manage operating systems, middleware, and many network configurations.
- Continuous monitoring, vulnerability management, and incident response are essential for maintaining a strong cloud security posture.
- Understanding and fulfilling customer responsibilities is critical to reducing risk, maintaining compliance, and preventing cloud security incidents.

---

# Detailed Cloud Provider Responsibilities

## Introduction

Cloud Service Providers (CSPs) such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI), IBM Cloud, and others invest billions of dollars every year to build, operate, and secure highly resilient cloud infrastructures.

Within the Shared Responsibility Model, cloud providers are responsible for securing the **cloud itself**—the physical facilities, networking infrastructure, hardware, virtualization layer, managed platform services, and core cloud operations.

Customers benefit from enterprise-grade infrastructure without having to build and maintain their own data centers. However, customers must understand **where the provider's responsibilities begin and where they end**.

It is important to remember that cloud providers secure the foundation upon which customer workloads operate, but they generally do **not** manage customer applications, identities, or business data unless explicitly offered as managed services.

Understanding provider responsibilities helps organizations:

- Design secure architectures
- Conduct cloud security assessments
- Meet compliance requirements
- Interpret provider security documentation
- Reduce operational risk
- Clarify accountability during incidents

---

# Learning Objectives

After completing this section, you will be able to:

- Understand provider responsibilities in the Shared Responsibility Model.
- Learn physical infrastructure security.
- Understand data center security.
- Learn hardware lifecycle management.
- Understand virtualization security.
- Learn cloud network security.
- Understand platform availability.
- Learn provider compliance responsibilities.
- Analyze provider operational controls.
- Differentiate provider-managed and customer-managed security.

---

# Overview of Cloud Provider Responsibilities

Cloud providers are responsible for securing the foundational infrastructure that enables cloud services.

```
Cloud Provider Responsibilities

│

├── Physical Data Centers

├── Physical Security

├── Buildings & Facilities

├── Hardware Security

├── Storage Infrastructure

├── Network Infrastructure

├── Hypervisor Security

├── Virtualization Platform

├── Core Cloud Services

├── Platform Availability

├── Infrastructure Monitoring

├── Hardware Maintenance

├── Disaster Recovery

├── Physical Media Disposal

├── Environmental Controls

└── Compliance Certifications
```

These responsibilities form the security foundation of every cloud environment.

---

# Physical Data Center Security

## Overview

Cloud providers own or operate highly secure data centers distributed across multiple geographic regions.

These facilities are designed to provide:

- Physical protection
- High availability
- Environmental stability
- Operational resilience
- Disaster resistance

Customers generally never have physical access to cloud provider data centers.

---

# Physical Security Controls

Typical controls include:

- Multi-layer perimeter fencing
- Security guards
- Vehicle barriers
- Controlled entrances
- Security checkpoints
- Visitor registration
- Escort policies
- CCTV surveillance
- Intrusion detection systems
- Continuous monitoring

```
Public Road

↓

Perimeter Fence

↓

Security Gate

↓

Identity Verification

↓

Access Control

↓

Secure Building

↓

Server Room
```

Every layer reduces the likelihood of unauthorized physical access.

---

# Biometric Access Controls

Highly sensitive areas often require multiple authentication factors.

Example:

```
Employee Badge

↓

PIN

↓

Fingerprint

↓

Retina Scan

↓

Server Room Access
```

Access is granted only after successful verification.

---

# Environmental Controls

Cloud providers maintain environmental conditions necessary for reliable operation.

Responsibilities include:

- Temperature control
- Humidity management
- Fire suppression
- Smoke detection
- Water leak detection
- Dust control
- Air filtration

These controls protect hardware from environmental damage.

---

# Power Infrastructure

Continuous availability depends on redundant power systems.

```
Utility Power

↓

UPS

↓

Battery Backup

↓

Diesel Generators

↓

Power Distribution

↓

Servers
```

Even if utility power fails, workloads continue operating.

---

# Network Connectivity Redundancy

Cloud providers build highly redundant network infrastructures.

```
Internet Provider A

        │

Internet Provider B

        │

Internet Provider C

        │

────────┼────────

        ▼

Cloud Backbone Network
```

Multiple network paths reduce the impact of outages.

---

# Hardware Security

## Overview

Cloud providers procure, install, monitor, maintain, and replace physical hardware.

Examples include:

- Compute servers
- Storage arrays
- Network switches
- Routers
- Load balancers
- Security appliances
- Fiber infrastructure

Customers are not responsible for maintaining physical hardware.

---

# Hardware Lifecycle Management

```
Procurement

↓

Installation

↓

Configuration

↓

Production

↓

Monitoring

↓

Maintenance

↓

Replacement

↓

Secure Disposal
```

Every phase follows strict operational procedures.

---

# Secure Hardware Disposal

Before retired storage devices leave production environments, providers securely sanitize or destroy them.

Methods may include:

- Cryptographic erasure
- Secure overwrite
- Physical destruction
- Certified disposal procedures

These processes help prevent unauthorized data recovery.

---

# Storage Infrastructure

Cloud providers maintain large-scale distributed storage systems.

Responsibilities include:

- Storage hardware
- Storage replication
- Hardware redundancy
- RAID implementation
- Storage monitoring
- Drive replacement
- Physical encryption support
- Infrastructure availability

Customers remain responsible for configuring logical access permissions.

---

# Network Infrastructure Security

Providers operate extensive global networking infrastructures.

Responsibilities include:

- Backbone networks
- Core routers
- Switches
- Fiber links
- Edge infrastructure
- DDoS mitigation infrastructure
- Network redundancy
- Routing stability

```
Global Backbone

↓

Regional Network

↓

Availability Zone

↓

Customer Resources
```

Customers configure logical network policies within this infrastructure.

---

# Virtualization Security

## Overview

Virtualization enables multiple customers to share physical hardware securely.

The cloud provider manages:

- Hypervisors
- Host operating systems
- VM isolation
- Resource scheduling
- Hardware abstraction

Customers generally cannot access the hypervisor directly.

---

# Hypervisor Architecture

```
Physical Hardware

↓

Hypervisor

──────────────

Virtual Machine A

Virtual Machine B

Virtual Machine C
```

The hypervisor isolates workloads belonging to different customers.

---

# Virtual Machine Isolation

Isolation prevents one customer's virtual machine from directly accessing another customer's workloads.

Provider responsibilities include:

- Memory isolation
- CPU scheduling
- Storage isolation
- Network isolation
- Secure virtualization boundaries

Strong isolation is essential in multi-tenant cloud environments.

---

# Managed Service Operations

Cloud providers also operate many managed cloud services.

Examples include:

- Managed databases
- Object storage
- Messaging services
- Serverless platforms
- Identity platforms
- Monitoring services
- Container platforms

For these services, providers assume additional operational responsibilities.

---

# Platform Availability

Cloud providers design services for high availability.

Typical mechanisms include:

- Redundant hardware
- Multiple Availability Zones
- Automated failover
- Health monitoring
- Capacity management
- Traffic engineering

```
Availability Zone A

↓

Availability Zone B

↓

Availability Zone C

↓

Continuous Service
```

Customers should still architect workloads for resilience.

---

# Infrastructure Monitoring

Cloud providers continuously monitor infrastructure health.

Examples include:

- Hardware failures
- Network outages
- Storage failures
- Hypervisor health
- Platform performance
- Power systems
- Environmental sensors

Monitoring enables rapid operational response.

---

# Disaster Recovery

Cloud providers prepare for infrastructure failures through disaster recovery planning.

Typical capabilities include:

- Geographic redundancy
- Infrastructure replication
- Backup power
- Automated recovery procedures
- Regional failover
- Hardware replacement

These controls improve service resilience.

---

# Capacity Management

Cloud providers continuously forecast and expand infrastructure capacity.

Responsibilities include:

- Hardware procurement
- Storage expansion
- Compute capacity planning
- Network upgrades
- Regional expansion
- Performance optimization

Capacity management helps maintain reliable cloud services during demand growth.

---

# Security Operations

Cloud providers operate dedicated security teams responsible for protecting infrastructure.

Typical activities include:

- Threat monitoring
- Incident response
- Vulnerability management
- Threat intelligence
- Malware analysis
- Security engineering
- Infrastructure hardening
- Continuous monitoring

These teams protect the cloud platform itself.

---

# Vulnerability Management

Providers regularly assess infrastructure for vulnerabilities.

Activities include:

- Internal vulnerability scanning
- Security testing
- Patch validation
- Risk prioritization
- Infrastructure updates
- Configuration reviews

Customers remain responsible for scanning and patching their own workloads where applicable.

---

# Patch Management

Providers patch:

- Hypervisors
- Host operating systems
- Networking equipment
- Managed platform components
- Infrastructure software

Customers generally do not perform these activities.

---

# DDoS Protection

Most cloud providers implement infrastructure-level protections against Distributed Denial-of-Service (DDoS) attacks.

Capabilities may include:

- Traffic filtering
- Network scrubbing
- Traffic engineering
- Rate limiting at the infrastructure level
- Global edge protection

Customers may still need application-level protections depending on workload requirements.

---

# Compliance Responsibilities

Cloud providers obtain numerous independent certifications for their infrastructure.

Examples include:

- ISO/IEC 27001
- ISO/IEC 27017
- ISO/IEC 27018
- SOC 1
- SOC 2
- SOC 3
- PCI DSS (for applicable services)
- CSA STAR
- Various regional and industry certifications

These certifications demonstrate that provider-managed infrastructure has been independently assessed.

However, **customer workloads are not automatically compliant simply because they run on certified infrastructure.**

---

# Audit Responsibilities

Providers conduct and support infrastructure audits through:

- Independent assessors
- Internal security teams
- Continuous compliance programs
- Operational documentation
- Security reports

Customers use these reports as part of their own compliance activities.

---

# Provider Incident Response

When infrastructure incidents occur, providers are responsible for:

```
Incident Detected

↓

Infrastructure Analysis

↓

Containment

↓

Recovery

↓

Service Restoration

↓

Customer Notification (where applicable)

↓

Post-Incident Review
```

Customers remain responsible for incidents affecting their own applications, identities, or configurations.

---

# Enterprise Example

An organization deploys an ERP application on cloud virtual machines.

Provider responsibilities include:

- Physical servers
- Hypervisors
- Networking hardware
- Data centers
- Storage infrastructure
- Facility security
- Platform monitoring
- Infrastructure availability

Customer responsibilities include:

- Operating system configuration
- ERP application
- User accounts
- IAM policies
- Database permissions
- Data encryption
- Backup configuration
- Compliance controls

This clear separation reduces ambiguity during operations and incident response.

---

# Common Misunderstandings

### "The provider secures my application."

Incorrect.

Providers secure the platform, not customer-developed application code.

---

### "Infrastructure compliance makes my application compliant."

Incorrect.

Compliance responsibilities remain shared.

Customers must configure workloads according to applicable regulations.

---

### "The provider backs up all my data."

Not necessarily.

Some services provide backup capabilities, but customers are generally responsible for defining backup policies, retention periods, and recovery objectives.

---

### "Cloud providers prevent all cyberattacks."

Providers implement strong infrastructure protections, but they cannot prevent attacks resulting from:

- Weak passwords
- Misconfigured IAM
- Vulnerable applications
- Exposed APIs
- Customer configuration errors

---

# Best Practices

- Review provider security documentation regularly.
- Understand which controls are provider-managed.
- Verify service-specific responsibility boundaries.
- Leverage provider security features appropriately.
- Design workloads across multiple Availability Zones where appropriate.
- Review compliance reports during vendor assessments.
- Monitor provider service health and advisories.
- Incorporate provider responsibilities into risk assessments.
- Validate backup and disaster recovery strategies rather than assuming default protection.
- Maintain clear documentation of shared operational ownership.

---

# Common Mistakes

Avoid the following pitfalls:

- Assuming provider responsibilities extend to customer applications.
- Ignoring provider documentation for managed services.
- Treating provider certifications as complete compliance coverage.
- Assuming managed services eliminate the need for customer monitoring.
- Confusing infrastructure availability with application availability.
- Failing to understand service-specific operational boundaries.
- Assuming provider-managed encryption automatically satisfies business requirements.
- Neglecting customer-side governance because infrastructure is managed.

---

# Key Takeaways

- Cloud providers are responsible for securing the infrastructure that delivers cloud services, including physical facilities, hardware, networking, virtualization, and managed platform operations.
- Provider responsibilities include physical security, environmental controls, hardware lifecycle management, hypervisor security, infrastructure monitoring, disaster recovery, and compliance certifications.
- Customers benefit from enterprise-grade infrastructure but remain responsible for securing their own identities, data, applications, and configurations.
- Provider certifications demonstrate the security of the underlying cloud platform, not the compliance of customer workloads.
- Understanding provider responsibilities enables organizations to design secure architectures, conduct effective audits, and correctly apply the Shared Responsibility Model.

---

