# 63-Web-Security-Architecture.md

# Part 1 — Introduction to Web Security Architecture, Security Principles, Trust Boundaries, Security Layers, and Enterprise Foundations

> **"Web Security Architecture is the structured design of security controls, technologies, policies, and processes that collectively protect web applications, users, data, and infrastructure throughout the application lifecycle."**

---

# Learning Objectives

After completing this part, you will understand:

- What Web Security Architecture Is
- Why Security Architecture Matters
- Security Architecture Goals
- Security Principles
- Security Layers
- Trust Boundaries
- Attack Surface (Conceptual)
- Secure Design Principles
- Enterprise Security Architecture
- Shared Responsibility

---

# What is Web Security Architecture?

Web Security Architecture is the blueprint that defines how security controls are integrated into web applications, infrastructure, networks, and operational processes.

```
Business Requirements

↓

Security Architecture

↓

Secure Design

↓

Implementation

↓

Monitoring

↓

Continuous Improvement
```

Security architecture provides a structured approach to protecting business-critical web applications.

---

# Why Security Architecture Matters

Modern web applications consist of numerous interconnected components.

A well-designed security architecture helps organizations:

- Reduce organizational risk
- Protect sensitive information
- Improve application resilience
- Support compliance
- Standardize security controls
- Improve operational efficiency
- Enable secure growth
- Support business continuity

---

# Objectives of Security Architecture

```
Security Architecture

│

├── Confidentiality

├── Integrity

├── Availability

├── Reliability

├── Resilience

├── Governance

├── Compliance

└── Continuous Improvement
```

These objectives guide architectural decisions throughout the application lifecycle.

---

# Evolution of Web Security

```
Basic Web Applications

↓

Perimeter Security

↓

Secure Development

↓

Cloud Security

↓

Zero Trust

↓

Enterprise Security Architecture
```

Security has evolved from isolated controls to integrated enterprise-wide architectures.

---

# Core Security Principles

```
Security Principles

│

├── Least Privilege

├── Defense in Depth

├── Separation of Duties

├── Fail Secure

├── Secure by Design

├── Zero Trust

├── Continuous Verification

└── Risk-Based Decisions
```

These principles provide the foundation for secure architectural design.

---

# Confidentiality

Confidentiality ensures that information is accessible only to authorized individuals and systems.

```
Sensitive Data

↓

Access Controls

↓

Authorized Users
```

Appropriate identity and access management supports confidentiality.

---

# Integrity

Integrity ensures that information remains accurate, complete, and protected from unauthorized modification.

```
Business Data

↓

Integrity Controls

↓

Trusted Information
```

Integrity supports reliable business operations and decision-making.

---

# Availability

Availability ensures that authorized users can access applications and services when required.

```
Users

↓

Web Application

↓

Reliable Services

↓

Business Operations
```

Availability contributes to customer satisfaction and operational continuity.

---

# Defense in Depth

Defense in Depth uses multiple security layers to reduce organizational risk.

```
Users

↓

Identity

↓

Application

↓

Network

↓

Infrastructure

↓

Monitoring
```

No single security control should be relied upon as the sole protection mechanism.

---

# Security Layers

```
Security Layers

│

├── Physical Security

├── Network Security

├── Infrastructure Security

├── Platform Security

├── Application Security

├── Identity Security

├── Data Security

└── Monitoring & Governance
```

Each layer contributes to the organization's overall security posture.

---

# Trust Boundaries

Trust boundaries separate systems or components with different security assumptions.

```
Internet

│

▼

Public Zone

────────────── Trust Boundary ──────────────

Internal Services

────────────── Trust Boundary ──────────────

Sensitive Data
```

Crossing a trust boundary should involve appropriate verification and security controls.

---

# Security Domains

```
Enterprise Security Domains

│

├── Users

├── Web Applications

├── APIs

├── Databases

├── Identity Services

├── Infrastructure

├── Monitoring

└── Business Systems
```

Security controls should be applied consistently across each domain.

---

# Attack Surface (Conceptual)

The attack surface represents the collection of entry points and interfaces that require protection.

```
Web Application

│

├── User Interface

├── APIs

├── Authentication

├── Administrative Functions

├── Network Interfaces

├── Data Storage

└── Third-Party Integrations
```

Organizations should continuously identify, review, and reduce unnecessary exposure.

---

# Secure by Design

Security should be incorporated throughout system design rather than added after deployment.

```
Requirements

↓

Architecture

↓

Design

↓

Development

↓

Testing

↓

Deployment

↓

Operations
```

Security decisions made early reduce operational complexity later.

---

# Shared Responsibility

Security architecture requires collaboration across multiple teams.

```
Architecture Team

        │

Development Team

        │

Infrastructure Team

        │

Operations Team

        │

Security Team

        │

Business Stakeholders
```

Each team contributes to maintaining a secure architecture.

---

# Enterprise Security Architecture

```
                 Users

                   │

                   ▼

        Identity & Access Layer

                   │

                   ▼

         Web Applications & APIs

                   │

                   ▼

        Business Services Layer

                   │

                   ▼

          Data & Storage Layer

                   │

                   ▼

 Infrastructure • Monitoring • Governance
```

This layered architecture supports secure communication, operational visibility, and business resilience.

---

# Enterprise Example

A multinational retail organization delivers customer portals, mobile applications, payment services, and internal management systems.

```
Customers

↓

Identity Services

↓

Web Applications

↓

Business Services

↓

Databases

↓

Monitoring Platform
```

Security architects define trust boundaries, implement layered security controls, document governance requirements, and coordinate with development and operations teams to maintain a secure enterprise architecture.

---

# Benefits of Security Architecture

```
Benefits

│

├── Reduced Risk

├── Consistent Security

├── Better Governance

├── Improved Reliability

├── Stronger Compliance

├── Operational Efficiency

├── Scalable Growth

└── Business Resilience
```

---

# Hands-on Lab (Conceptual)

1. Draw a layered security architecture for an enterprise web application.
2. Identify trust boundaries between users, applications, APIs, and databases.
3. Map security principles to each architectural layer.
4. Document the major security domains within an enterprise application.
5. Review the conceptual attack surface and identify opportunities to reduce unnecessary exposure.

> Perform all activities only in environments where you have explicit authorization. Focus on secure architecture, governance, and defensive design principles.

---

# Interview Questions

1. What is Web Security Architecture?
2. Why is security architecture important?
3. What are the objectives of security architecture?
4. What is Defense in Depth?
5. What is a trust boundary?
6. Why should security be integrated during system design?
7. What is meant by the application attack surface?
8. What are the primary security layers in an enterprise architecture?
9. Why is shared responsibility important?
10. How does security architecture improve business resilience?

---

# Best Practices

- Integrate security from the earliest design stages.
- Apply Defense in Depth across all architectural layers.
- Clearly define trust boundaries.
- Reduce unnecessary attack surface.
- Standardize security controls across applications.
- Align architecture with business objectives.
- Maintain architecture documentation.
- Review security architecture regularly as systems evolve.

---

# Common Mistakes

- Treating security as a deployment-only activity.
- Relying on a single security control.
- Ignoring trust boundaries.
- Maintaining undocumented architecture.
- Allowing inconsistent security standards across applications.
- Expanding systems without updating security architecture.
- Neglecting continuous architectural reviews.

---

# Key Takeaways

- Web Security Architecture provides the blueprint for protecting enterprise web applications.
- Layered security, trust boundaries, and secure design principles form the foundation of resilient architectures.
- Security should be integrated throughout the application lifecycle.
- Collaboration between architecture, development, operations, and security teams is essential.
- Mature security architectures continuously evolve through governance, monitoring, and improvement.

# 63-Web-Security-Architecture.md

# Part 2 — Identity Architecture, Authentication, Authorization, Secure Network Design, Data Protection, and Security Control Layers

> **"A secure web architecture is built upon strong identity management, layered access control, protected data flows, secure network segmentation, and standardized security controls that work together throughout the application lifecycle."**

---

# Learning Objectives

After completing this part, you will understand:

- Identity Security Architecture
- Authentication
- Authorization
- Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Least Privilege
- Secure Network Architecture
- Security Zones
- Data Protection Architecture
- Security Control Categories

---

# Identity Security Architecture

Identity is the primary security boundary in modern web applications.

```
Users

↓

Identity Provider

↓

Authentication

↓

Authorization

↓

Web Application

↓

Business Services
```

Every request should be associated with a verified identity before access decisions are made.

---

# Identity Components

```
Identity Architecture

│

├── Users

├── Service Accounts

├── Applications

├── APIs

├── Administrators

├── Identity Provider

├── Access Policies

└── Audit Logging
```

Identity management should be centralized and governed consistently.

---

# Authentication

Authentication confirms the identity of a user or service before granting access.

```
Identity

↓

Authentication

↓

Verified Identity

↓

Application Access
```

Authentication mechanisms should align with organizational security policies.

---

# Authentication Factors

```
Authentication Factors

│

├── Knowledge Factors

├── Possession Factors

├── Inherence Factors

├── Device Verification

├── Risk Evaluation

├── Session Validation

├── Identity Verification

└── Continuous Monitoring
```

Combining multiple authentication factors strengthens identity assurance.

---

# Authorization

Authorization determines what an authenticated identity is permitted to access.

```
Verified Identity

↓

Policy Evaluation

↓

Permission Decision

↓

Resource Access
```

Authorization decisions should follow documented access control policies.

---

# Identity and Access Management (IAM)

IAM governs the lifecycle of identities and their permissions.

```
Identity Creation

↓

Role Assignment

↓

Access Approval

↓

Usage Monitoring

↓

Periodic Review

↓

Deprovisioning
```

IAM supports consistent access management across enterprise systems.

---

# Role-Based Access Control (RBAC)

RBAC simplifies permission management by assigning permissions through predefined roles.

```
Identity

↓

Assigned Role

↓

Permissions

↓

Application Resources
```

Roles should align with business functions rather than individual users.

---

# Principle of Least Privilege

Every identity should receive only the minimum permissions necessary for its responsibilities.

```
Identity

↓

Business Role

↓

Minimum Permissions

↓

Authorized Resources
```

Applying least privilege reduces organizational risk and limits the impact of compromised accounts.

---

# Access Governance

```
Access Governance

│

├── Access Requests

├── Approval Workflow

├── Role Assignment

├── Periodic Reviews

├── Audit Logging

├── Compliance Reviews

├── Revocation

└── Continuous Improvement
```

Governance ensures access remains appropriate throughout the identity lifecycle.

---

# Secure Network Architecture

Secure network architecture separates systems into logical security zones.

```
Internet

↓

Edge Services

↓

Web Layer

↓

Application Layer

↓

Data Layer

↓

Management Services
```

Each layer should have clearly defined communication paths and security controls.

---

# Network Security Zones

```
Security Zones

│

├── Public Zone

├── Web Tier

├── Application Tier

├── Database Tier

├── Management Zone

├── Monitoring Zone

├── Backup Zone

└── Administrative Zone
```

Segmentation limits unnecessary communication between systems.

---

# Network Segmentation

```
Public Users

↓

Web Servers

──────── Trust Boundary ────────

Application Services

──────── Trust Boundary ────────

Databases
```

Trust boundaries should enforce appropriate authentication, authorization, and monitoring.

---

# Secure Communication

Applications should communicate using secure, authenticated channels.

```
Application A

↓

Secure Communication

↓

Application B

↓

Business Service
```

Secure communication protects confidentiality and integrity during data exchange.

---

# Data Protection Architecture

Data protection should be integrated throughout the application lifecycle.

```
Data

↓

Classification

↓

Storage

↓

Access Control

↓

Monitoring

↓

Retention

↓

Secure Disposal
```

Data protection policies should reflect business and regulatory requirements.

---

# Data Classification

```
Business Data

│

├── Public

├── Internal

├── Confidential

├── Restricted

├── Financial

├── Customer

├── Operational

└── Audit Data
```

Classification determines the level of protection applied to information.

---

# Data Lifecycle

```
Creation

↓

Processing

↓

Storage

↓

Sharing

↓

Archiving

↓

Retention

↓

Disposal
```

Security controls should be applied consistently throughout the lifecycle.

---

# Security Control Categories

```
Security Controls

│

├── Administrative Controls

├── Technical Controls

├── Physical Controls

├── Preventive Controls

├── Detective Controls

├── Corrective Controls

├── Compensating Controls

└── Recovery Controls
```

Organizations typically combine multiple categories of controls to strengthen overall security.

---

# Layered Security Controls

```
Users

↓

Identity Controls

↓

Application Controls

↓

Network Controls

↓

Infrastructure Controls

↓

Monitoring Controls

↓

Governance Controls
```

Layered controls provide resilience even if one control becomes ineffective.

---

# Enterprise Security Workflow

```
Business Requirement

↓

Architecture Design

↓

Identity Design

↓

Network Design

↓

Application Development

↓

Deployment

↓

Continuous Monitoring
```

Security architecture should evolve alongside business and technical requirements.

---

# Enterprise Example

A multinational healthcare provider delivers patient portals, internal clinical systems, and partner APIs.

```
Patients

↓

Identity Services

↓

Web Applications

↓

Application Services

↓

Medical Databases

↓

Monitoring Platform
```

Security architects establish identity governance, secure communication pathways, role-based access control, network segmentation, and data protection standards. Operational teams continuously review identity activity, architecture changes, and monitoring dashboards to maintain a secure enterprise environment.

---

# Operational Metrics

| Metric | Purpose |
|---------|----------|
| Identity Review Completion | Access governance |
| Authentication Success Rate | Identity reliability |
| Authorization Policy Coverage | Access consistency |
| Role Review Completion | Governance maturity |
| Network Segmentation Coverage | Architectural security |
| Data Classification Coverage | Data governance |
| Secure Communication Coverage | Protection of service interactions |
| Access Audit Completion | Compliance and accountability |

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Identity sprawl | Centralized IAM |
| Excessive permissions | Apply least privilege and periodic reviews |
| Flat network architecture | Implement logical segmentation |
| Inconsistent access policies | Standardized RBAC |
| Unclassified data | Enterprise-wide data classification |
| Rapid business growth | Regular architecture reviews and governance |

---

# Hands-on Lab (Conceptual)

1. Design an identity architecture for an enterprise web application.
2. Map user roles to RBAC permissions.
3. Draw trust boundaries between the web, application, and database tiers.
4. Classify business data according to organizational policies.
5. Identify administrative, technical, preventive, and detective controls for each architectural layer.

> Perform all activities only in environments where you have explicit authorization. Focus on secure architecture, governance, and defensive design rather than offensive testing.

---

# Interview Questions

1. Why is identity considered the primary security boundary?
2. What is the difference between authentication and authorization?
3. How does IAM improve enterprise security?
4. Why is RBAC widely used?
5. What is the Principle of Least Privilege?
6. Why is network segmentation important?
7. What are trust boundaries?
8. Why should data be classified?
9. What are the major categories of security controls?
10. How does layered security improve resilience?

---

# Best Practices

- Centralize identity and access management.
- Apply least privilege to every identity.
- Use standardized RBAC models.
- Clearly define trust boundaries.
- Segment networks according to business functions.
- Classify and protect business data throughout its lifecycle.
- Apply multiple layers of complementary security controls.
- Review architecture and access policies regularly.

---

# Common Mistakes

- Granting excessive permissions.
- Maintaining undocumented access policies.
- Allowing unrestricted communication between security zones.
- Ignoring data classification.
- Treating identity management as a one-time activity.
- Using inconsistent security controls across applications.
- Failing to review architectural changes after deployments.

---

# Key Takeaways

- Identity architecture is the foundation of modern web security.
- Authentication, authorization, IAM, RBAC, and least privilege provide strong access control.
- Secure network architecture uses trust boundaries and segmentation to reduce risk.
- Data protection must span the complete information lifecycle.
- Layered security controls and continuous governance strengthen enterprise resilience.

# 63-Web-Security-Architecture.md

# Part 3 — Secure Architecture Patterns, Zero Trust, Security Governance, Monitoring Integration, Risk Management, and Operational Resilience

> **"Enterprise Web Security Architecture extends beyond technical controls by integrating governance, Zero Trust principles, operational monitoring, risk management, and continuous security validation throughout the application lifecycle."**

---

# Learning Objectives

After completing this part, you will understand:

- Secure Architecture Patterns
- Zero Trust Architecture
- Defense in Depth Implementation
- Security Monitoring Integration
- Security Architecture Governance
- Risk Management
- Secure Configuration Management
- Compliance Integration
- Operational Resilience
- Continuous Security Improvement

---

# Secure Architecture Patterns

Security architecture patterns provide reusable approaches for designing secure web applications.

```
Business Requirements

↓

Architecture Pattern

↓

Security Controls

↓

Implementation

↓

Monitoring

↓

Continuous Improvement
```

Standardized architecture patterns improve consistency, scalability, and maintainability.

---

# Common Architecture Patterns

```
Architecture Patterns

│

├── Layered Architecture

├── Multi-Tier Architecture

├── Microservices Architecture

├── API-Centric Architecture

├── Event-Driven Architecture

├── Service-Oriented Architecture

├── Cloud-Native Architecture

└── Hybrid Architecture
```

Each pattern introduces unique security considerations while sharing common security principles.

---

# Layered Security Architecture

```
Users

↓

Presentation Layer

↓

Application Layer

↓

Business Logic Layer

↓

Data Access Layer

↓

Database Layer

↓

Monitoring & Governance
```

Each layer should validate requests and enforce security controls appropriate to its responsibilities.

---

# Zero Trust Architecture

Zero Trust is based on the principle of **"Never Trust, Always Verify."**

```
User

↓

Identity Verification

↓

Policy Evaluation

↓

Device Validation

↓

Application Access

↓

Continuous Monitoring
```

Trust should be continuously evaluated rather than assumed.

---

# Zero Trust Principles

```
Zero Trust

│

├── Verify Identity

├── Least Privilege

├── Continuous Validation

├── Explicit Authorization

├── Secure Communication

├── Continuous Monitoring

├── Risk-Based Decisions

└── Governance
```

These principles reduce implicit trust across enterprise environments.

---

# Defense in Depth Implementation

Defense in Depth combines multiple independent security layers.

```
Users

↓

Identity Controls

↓

Application Controls

↓

Network Controls

↓

Infrastructure Controls

↓

Monitoring

↓

Governance
```

Multiple protective layers improve resilience against failures and misconfigurations.

---

# Security Control Placement

```
Security Controls

│

├── Edge Controls

├── Identity Controls

├── Application Controls

├── API Controls

├── Data Controls

├── Monitoring Controls

├── Administrative Controls

└── Recovery Controls
```

Controls should be placed where they provide the greatest protection and visibility.

---

# Secure Configuration Management

Configuration consistency is essential for maintaining a secure architecture.

```
Architecture Standards

↓

Configuration

↓

Validation

↓

Deployment

↓

Monitoring

↓

Review
```

Changes should follow approved organizational procedures.

---

# Configuration Governance

```
Configuration Governance

│

├── Version Control

├── Documentation

├── Change Approval

├── Validation

├── Deployment

├── Monitoring

├── Audit Trail

└── Rollback Planning
```

Governance reduces configuration drift and operational risk.

---

# Security Monitoring Integration

Monitoring should be integrated into every architectural layer.

```
Applications

↓

Infrastructure

↓

Identity Services

↓

Monitoring Platform

↓

Dashboards

↓

Operations Center
```

Integrated monitoring improves visibility across the enterprise.

---

# Monitoring Architecture

```
Monitoring

│

├── Metrics

├── Logs

├── Traces

├── Audit Records

├── Dashboards

├── Alerts

├── Reports

└── Operational Analytics
```

These components collectively support observability and operational awareness.

---

# Risk Management Integration

Security architecture should align with enterprise risk management.

```
Business Objectives

↓

Risk Assessment

↓

Security Controls

↓

Implementation

↓

Monitoring

↓

Risk Review
```

Architectural decisions should consider both technical and business risks.

---

# Risk Categories

```
Enterprise Risks

│

├── Operational Risk

├── Technology Risk

├── Business Risk

├── Compliance Risk

├── Availability Risk

├── Data Risk

├── Third-Party Risk

└── Strategic Risk
```

Risk assessments should be reviewed periodically as systems evolve.

---

# Compliance Integration

Security architecture supports compliance by embedding governance into operational processes.

```
Policies

↓

Architecture

↓

Security Controls

↓

Monitoring

↓

Evidence

↓

Audit Readiness
```

Compliance becomes more effective when incorporated into everyday operations.

---

# Architecture Documentation

Documentation is a critical component of enterprise security architecture.

```
Architecture

↓

Design Documents

↓

Diagrams

↓

Standards

↓

Operational Guides

↓

Review
```

Documentation should remain accurate and reflect the current environment.

---

# Operational Resilience

Operational resilience ensures that critical business services remain dependable under changing conditions.

```
Architecture

↓

Monitoring

↓

Operational Review

↓

Improvements

↓

Reliable Services
```

Resilience is strengthened through continuous monitoring and governance.

---

# Enterprise Architecture Workflow

```
Business Requirements

↓

Architecture Design

↓

Security Review

↓

Implementation

↓

Deployment

↓

Monitoring

↓

Continuous Improvement
```

Each phase contributes to maintaining a secure and resilient architecture.

---

# Enterprise Security Architecture

```
                Users

                  │

                  ▼

      Identity & Access Services

                  │

                  ▼

      Web Applications & APIs

                  │

                  ▼

      Business Services Layer

                  │

                  ▼

       Data & Storage Services

                  │

                  ▼

 Monitoring • Governance • Compliance

                  │

                  ▼

     Continuous Improvement Program
```

This architecture demonstrates how governance and monitoring integrate with technical controls.

---

# Enterprise Example

A multinational financial services organization operates customer banking portals, mobile applications, partner APIs, and internal administration systems.

```
Users

↓

Identity Platform

↓

Web Applications

↓

Business Services

↓

Databases

↓

Monitoring & SOC

↓

Governance
```

Security architects define enterprise standards for identity, secure communications, layered security controls, monitoring integration, and governance. Development, infrastructure, operations, and security teams collaborate to maintain consistent architectural practices while continuously reviewing risks and operational metrics.

---

# Operational Metrics

| Metric | Purpose |
|---------|----------|
| Architecture Review Completion | Governance maturity |
| Security Control Coverage | Protection effectiveness |
| Configuration Review Completion | Configuration governance |
| Monitoring Coverage | Operational visibility |
| Compliance Assessment Completion | Audit readiness |
| Risk Review Completion | Risk management |
| Documentation Currency | Architectural accuracy |
| Operational Availability | Business resilience |

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Rapid technology changes | Periodic architecture reviews |
| Configuration drift | Standardized configuration management |
| Multiple technology stacks | Common security architecture standards |
| Inconsistent governance | Enterprise-wide governance framework |
| Expanding business services | Scalable architecture patterns |
| Compliance complexity | Integrated governance and monitoring |

---

# Hands-on Lab (Conceptual)

1. Design a layered enterprise security architecture for a multi-tier web application.
2. Identify trust boundaries and appropriate security controls.
3. Create a configuration governance workflow.
4. Map enterprise risks to architectural controls.
5. Review an architecture diagram and identify opportunities to improve monitoring integration and operational resilience.

> Perform all activities only in environments where you have explicit authorization. Focus on secure architecture, governance, defensive design, and operational excellence.

---

# Interview Questions

1. What are secure architecture patterns?
2. What is Zero Trust Architecture?
3. How does Defense in Depth improve security?
4. Why should monitoring be integrated into architecture?
5. What is configuration governance?
6. Why is risk management important during architectural design?
7. How does security architecture support compliance?
8. Why is documentation important for enterprise architecture?
9. What is operational resilience?
10. Why should security architecture evolve continuously?

---

# Best Practices

- Adopt standardized architecture patterns.
- Apply Zero Trust principles consistently.
- Layer security controls throughout the environment.
- Integrate monitoring into every architectural layer.
- Maintain documented architecture standards.
- Regularly review risks and governance processes.
- Keep configuration management under formal change control.
- Continuously improve architecture using operational feedback.

---

# Common Mistakes

- Relying on perimeter security alone.
- Treating architecture documentation as static.
- Ignoring monitoring during design.
- Allowing uncontrolled configuration changes.
- Failing to review architectural risks regularly.
- Building inconsistent security controls across applications.
- Neglecting governance as the architecture evolves.

---

# Key Takeaways

- Secure architecture patterns provide reusable, scalable security designs.
- Zero Trust and Defense in Depth strengthen enterprise resilience.
- Monitoring, governance, and configuration management should be integrated into every architectural layer.
- Risk management and compliance are fundamental architectural considerations.
- Mature security architectures evolve continuously through governance, operational feedback, and ongoing improvement.

```text id="rrks28"
**Next:** Part 4
```