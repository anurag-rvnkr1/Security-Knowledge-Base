# 22-Insecure-Design.md

# Part 1 — Fundamentals of Insecure Design, Secure Design Principles, Threat Modeling, and Enterprise Architecture

> **"A secure application cannot be built by fixing code alone. If the design itself is insecure, every implementation built on top of it inherits that insecurity."**

---

# Learning Objectives

After completing this part, you will understand:

- What Insecure Design Is
- Design vs Implementation
- Secure Design Principles
- Security by Design
- Secure Development Lifecycle (SSDLC)
- Threat Modeling
- Attack Surface
- Business Logic
- Enterprise Architecture
- Defense in Depth

---

# What is Insecure Design?

**Insecure Design** refers to weaknesses that originate from poor architectural decisions, missing security requirements, or flawed business logic rather than coding mistakes.

Unlike implementation bugs, insecure design cannot usually be fixed with a simple patch or configuration change. It often requires redesigning part of the application or business process.

---

# Why OWASP Introduced Insecure Design

OWASP introduced **Insecure Design** as a separate category to emphasize that many security issues begin long before developers write code.

```
Business Requirements

↓

Architecture

↓

Design

↓

Implementation

↓

Testing

↓

Deployment
```

Security decisions made early have the greatest long-term impact.

---

# Design vs Implementation

| Design | Implementation |
|---------|----------------|
| Defines *what* the system should do | Defines *how* the system is built |
| Architectural decisions | Coding decisions |
| Security requirements | Secure coding practices |
| Business workflows | Program logic |
| Long-term foundation | Technical realization |

Both are essential, but they solve different problems.

---

# Security by Design

Security should be incorporated from the beginning.

```
Requirements

↓

Threat Modeling

↓

Secure Design

↓

Implementation

↓

Testing

↓

Deployment

↓

Monitoring
```

Security should never be treated as a feature added at the end of development.

---

# Real-World Analogy

Consider a building.

```
Blueprint

↓

Construction

↓

Building
```

If the blueprint omits emergency exits, perfect construction cannot compensate for the missing design.

Similarly:

```
Secure Design

↓

Secure Code

↓

Secure Application
```

---

# Characteristics of Insecure Design

```
Insecure Design

│

├── Missing Security Requirements

├── Weak Business Logic

├── Poor Trust Decisions

├── Excessive Functionality

├── Missing Abuse Controls

├── Weak Access Model

└── Poor Data Protection Strategy
```

---

# Design Lifecycle

```
Business Need

↓

Requirements

↓

Architecture

↓

Design Review

↓

Implementation

↓

Verification
```

Every stage should include security considerations.

---

# Business Logic

Business logic defines how an application operates.

Examples include:

- Order processing
- User registration
- Password reset
- Loan approval
- Shopping cart
- Booking systems
- Payroll approval

Business logic should enforce security requirements as well as functional requirements.

---

# Secure Business Logic

```
User Request

↓

Validation

↓

Business Rules

↓

Authorization

↓

Processing

↓

Response
```

Security should be integrated into the workflow rather than added afterward.

---

# Attack Surface

Every application exposes entry points.

```
Attack Surface

│

├── Login

├── Registration

├── APIs

├── File Upload

├── Search

├── Password Reset

├── Admin Portal

└── Mobile APIs
```

Reducing unnecessary functionality reduces the attack surface.

---

# Trust Boundaries

Applications frequently communicate across trust boundaries.

```
Browser

↓

Internet

↓

Web Server

↓

Application

↓

Database
```

Each boundary requires verification rather than assumptions.

---

# Enterprise Architecture

```
                Users

                  │

                  ▼

          Web Application

      ┌───────────┼───────────┐

      ▼           ▼           ▼

 Authentication  Business Logic  Logging

      │           │           │

      └───────────┼───────────┘

                  ▼

          Authorization Layer

                  │

                  ▼

              Database
```

Security should be designed into every architectural layer.

---

# Secure Design Principles

```
Secure Design

│

├── Least Privilege

├── Defense in Depth

├── Secure Defaults

├── Fail Securely

├── Minimize Attack Surface

├── Separation of Duties

├── Simplicity

└── Complete Mediation
```

These principles guide architects toward more resilient systems.

---

# Secure Defaults

Applications should start in the safest possible configuration.

```
Default Configuration

↓

Least Privilege

↓

Restricted Access

↓

Explicit Permission

↓

Operation Allowed
```

Security should require explicit approval rather than implicit trust.

---

# Complete Mediation

Every access request should be verified.

```
Request

↓

Authentication

↓

Authorization

↓

Business Rules

↓

Resource
```

Applications should not assume previous checks remain valid indefinitely.

---

# Minimize Attack Surface

```
Application

│

├── Required Features

└── Remove Unused Features
```

Every unnecessary feature increases complexity and potential risk.

---

# Fail Securely

```
Unexpected Error

↓

Secure Handling

↓

Controlled Response

↓

Logging
```

Applications should fail in a manner that protects sensitive information and maintains security controls.

---

# Defense in Depth

```
Authentication

↓

Authorization

↓

Input Validation

↓

Encryption

↓

Logging

↓

Monitoring
```

Multiple coordinated security layers provide stronger protection than any single control.

---

# Enterprise Example

An online banking application:

```
Customer

↓

Transfer Funds

↓

Authentication

↓

Authorization

↓

Business Rules

↓

Transaction

↓

Audit Log
```

Each stage contributes to the overall security of the process.

---

# Common Causes of Insecure Design

| Cause | Example |
|--------|----------|
| Missing security requirements | No fraud prevention workflow |
| Weak business rules | Unlimited high-value transactions |
| Poor trust assumptions | Trusting all internal requests |
| Missing approval processes | Sensitive actions require only one approval |
| Inadequate architecture | No separation between user and administrative functions |
| Insufficient threat analysis | Security risks identified too late |

---

# Enterprise Workflow

```
Business Requirement

↓

Security Requirement

↓

Threat Modeling

↓

Architecture

↓

Design Review

↓

Implementation

↓

Security Testing
```

Security requirements should evolve alongside functional requirements.

---

# Hands-on Lab (Conceptual)

1. Select a sample web application.
2. List its primary business processes.
3. Identify trust boundaries.
4. Identify the application's attack surface.
5. Discuss where secure design principles should be applied.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is Insecure Design?
2. How does Insecure Design differ from insecure implementation?
3. Why did OWASP introduce this category?
4. What is Security by Design?
5. What is a trust boundary?
6. What is an attack surface?
7. What is complete mediation?
8. Why are secure defaults important?
9. What is defense in depth?
10. Why should security requirements be defined during system design?

---

# Best Practices

- Define security requirements alongside functional requirements.
- Incorporate threat modeling early in the project.
- Apply secure design principles consistently.
- Minimize unnecessary functionality.
- Review architecture before implementation begins.
- Validate assumptions about trust boundaries.
- Integrate security into every stage of the SSDLC.

---

# Common Mistakes

- Treating security as a post-development activity.
- Assuming secure code compensates for poor design.
- Ignoring business logic security.
- Trusting internal components without verification.
- Expanding application functionality without reassessing risk.
- Delaying architecture reviews until after implementation.

---

# Key Takeaways

- Insecure Design originates from flawed architecture, missing security requirements, or weak business logic.
- Secure applications begin with secure requirements and architecture.
- Security by Design integrates protection throughout the development lifecycle.
- Trust boundaries, attack surface, and business logic are central to secure design.
- Secure design principles provide the foundation for resilient enterprise applications.


# 22-Insecure-Design.md

# Part 2 — Threat Modeling, Abuse Cases, Secure Design Patterns, Risk Assessment, and Business Logic Security

> **"The objective of secure design is not to predict every attack, but to build systems that remain secure even when unexpected situations occur."**

---

# Learning Objectives

After completing this part, you will understand:

- Threat Modeling
- Assets
- Threat Actors
- Attack Surface Analysis
- Abuse Cases
- Misuse Cases
- Business Logic Security
- Risk Assessment
- Secure Design Patterns
- Enterprise Security Reviews

---

# Threat Modeling

Threat modeling is a structured process used to identify potential security risks **before implementation begins**.

```
Business Requirements

↓

Architecture

↓

Threat Modeling

↓

Risk Identification

↓

Security Controls

↓

Implementation
```

The earlier risks are identified, the less costly they are to address.

---

# Why Threat Modeling Matters

Without threat modeling:

```
Requirements

↓

Development

↓

Deployment

↓

Security Problems
```

With threat modeling:

```
Requirements

↓

Threat Analysis

↓

Secure Design

↓

Implementation

↓

Reduced Risk
```

Threat modeling encourages proactive rather than reactive security.

---

# Components of Threat Modeling

```
Threat Modeling

│

├── Assets

├── Trust Boundaries

├── Entry Points

├── Threat Actors

├── Threats

├── Risks

└── Security Controls
```

Each component contributes to a complete security assessment.

---

# Identify Assets

Assets are resources that require protection.

Examples include:

```
Assets

│

├── Customer Data

├── Credentials

├── Payment Information

├── Source Code

├── API Keys

├── Business Documents

├── Financial Records

└── Audit Logs
```

Understanding assets helps prioritize security efforts.

---

# Identify Entry Points

Applications receive input through multiple interfaces.

```
Entry Points

│

├── Login

├── Registration

├── REST APIs

├── GraphQL APIs

├── Mobile APIs

├── File Upload

├── Search

└── Administrative Portal
```

Each entry point should be evaluated independently.

---

# Identify Trust Boundaries

```
Browser

↓

Internet

↓

Load Balancer

↓

Application

↓

Database
```

Whenever information crosses a trust boundary, validation and security checks should occur.

---

# Threat Actors

Threat actors are entities capable of interacting with the system.

```
Threat Actors

│

├── Customers

├── Administrators

├── Employees

├── Third-Party Services

├── Automated Systems

└── Unauthorized Parties
```

Different actors require different security controls.

---

# Threat Modeling Workflow

```
Identify Assets

↓

Identify Entry Points

↓

Identify Trust Boundaries

↓

Identify Threats

↓

Evaluate Risks

↓

Select Controls

↓

Review Design
```

Threat modeling should be repeated whenever significant architectural changes occur.

---

# Abuse Cases

An abuse case describes how a system **could be intentionally misused**.

Example:

```
Feature

↓

Normal Usage

↓

Potential Misuse

↓

Required Security Control
```

Thinking about misuse helps uncover missing protections.

---

# Misuse Cases

A misuse case focuses on **undesired system behavior**.

```
Business Feature

↓

Improper Use

↓

Potential Impact

↓

Mitigation
```

Designers should consider both intended and unintended behavior.

---

# Business Logic Security

Business logic defines organizational rules.

Example workflow:

```
Customer

↓

Place Order

↓

Inventory Check

↓

Payment Verification

↓

Order Approval

↓

Shipping
```

Each step should include appropriate validation and authorization.

---

# Secure Business Workflow

```
User

↓

Authentication

↓

Authorization

↓

Business Validation

↓

Fraud Checks

↓

Transaction

↓

Audit Logging
```

Security should be integrated into the workflow itself.

---

# Business Rules

Business rules enforce organizational policies.

Examples:

- Maximum transaction limits
- Age verification
- Purchase restrictions
- Approval workflows
- Daily usage limits
- Account ownership validation

These rules reduce business risk in addition to technical risk.

---

# Risk Assessment

Each identified threat should be evaluated.

```
Threat

↓

Likelihood

↓

Impact

↓

Risk Level

↓

Mitigation
```

Risk assessment helps prioritize limited security resources.

---

# Example Risk Matrix

| Likelihood | Impact | Priority |
|------------|--------|----------|
| High | High | Critical |
| High | Medium | High |
| Medium | Medium | Moderate |
| Low | High | Moderate |
| Low | Low | Low |

Organizations may customize risk ratings according to their governance processes.

---

# Secure Design Patterns

Secure design patterns provide reusable architectural approaches.

```
Secure Patterns

│

├── Authentication Layer

├── Authorization Layer

├── Validation Layer

├── Audit Logging

├── Error Handling

├── Secure Session Management

└── Encryption
```

Patterns encourage consistency across applications.

---

# Layered Architecture

```
Presentation Layer

↓

Application Layer

↓

Business Logic Layer

↓

Data Access Layer

↓

Database
```

Separating responsibilities improves maintainability and security.

---

# Separation of Responsibilities

```
Authentication

↓

Authorization

↓

Validation

↓

Business Logic

↓

Database Access
```

Each component should perform a clearly defined function.

---

# Security Design Reviews

Architectural reviews should examine:

```
✓ Trust Boundaries

✓ Authentication

✓ Authorization

✓ Input Validation

✓ Logging

✓ Encryption

✓ Session Management

✓ Business Logic

✓ Third-Party Integrations
```

Reviews are most effective before implementation begins.

---

# Enterprise Example

An online loan application:

```
Applicant

↓

Application Submission

↓

Identity Verification

↓

Eligibility Validation

↓

Risk Assessment

↓

Approval Workflow

↓

Loan Issuance

↓

Audit Log
```

Every stage incorporates both functional and security requirements.

---

# Secure Decision Flow

```
Request

↓

Authenticate

↓

Authorize

↓

Validate

↓

Business Rules

↓

Risk Checks

↓

Execute

↓

Audit
```

Security decisions should occur before sensitive operations.

---

# Common Design Weaknesses

| Weakness | Potential Impact |
|----------|------------------|
| Missing approval workflow | Unauthorized business actions |
| Weak business rules | Business process abuse |
| Excessive trust | Unauthorized operations |
| Missing validation | Incorrect processing |
| No audit trail | Difficult investigations |
| Inconsistent architecture | Uneven security controls |

---

# Enterprise Workflow

```
Requirements

↓

Architecture

↓

Threat Modeling

↓

Security Review

↓

Implementation

↓

Testing

↓

Deployment

↓

Monitoring
```

Threat modeling should be revisited whenever significant changes occur.

---

# Hands-on Lab (Conceptual)

1. Select a sample enterprise application.
2. Identify its key assets.
3. Draw trust boundaries.
4. List potential abuse cases.
5. Create a simple risk matrix for identified threats.
6. Recommend secure design improvements.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is threat modeling?
2. Why should threat modeling occur before implementation?
3. What is an asset?
4. What is an abuse case?
5. What is the purpose of a trust boundary?
6. Why are business rules important for security?
7. What is risk assessment?
8. Why are layered architectures considered more secure?
9. What should be reviewed during a security design review?
10. Why should threat modeling be repeated after major architectural changes?

---

# Best Practices

- Perform threat modeling during system design.
- Identify and classify critical assets.
- Document trust boundaries clearly.
- Develop abuse and misuse cases alongside functional requirements.
- Apply layered architecture and separation of responsibilities.
- Conduct formal security design reviews.
- Update threat models whenever the architecture changes.

---

# Common Mistakes

- Beginning implementation before evaluating threats.
- Focusing only on technical vulnerabilities while ignoring business logic.
- Treating all risks as equally important.
- Ignoring third-party integrations during design.
- Failing to document architectural assumptions.
- Never revisiting threat models after significant changes.

---

# Key Takeaways

- Threat modeling is a proactive approach to identifying security risks during design.
- Assets, trust boundaries, entry points, and threat actors form the foundation of secure architecture reviews.
- Abuse cases help identify how legitimate functionality might be intentionally misused.
- Business logic security is as important as technical security controls.
- Secure design patterns, layered architecture, and regular design reviews improve long-term application security.

# 22-Insecure-Design.md

# Part 3 — Secure Design Methodologies, Security Architecture, Zero Trust, Design Reviews, and Enterprise Governance

> **"Secure design is not about building barriers everywhere—it is about making correct security decisions at every architectural layer."**

---

# Learning Objectives

After completing this part, you will understand:

- Secure Design Methodology
- Security Architecture
- Zero Trust Design
- Defense in Depth
- Secure Design Reviews
- Security Requirements Engineering
- Security Architecture Patterns
- Enterprise Governance
- Design Validation
- Operational Security

---

# Secure Design Methodology

A secure application follows a structured design process.

```
Business Requirements

↓

Security Requirements

↓

Threat Modeling

↓

Architecture

↓

Design Review

↓

Implementation

↓

Security Testing

↓

Deployment

↓

Continuous Monitoring
```

Security decisions should be documented before development begins.

---

# Security Requirements Engineering

Security requirements should be treated like functional requirements.

```
Requirements

│

├── Functional

├── Performance

├── Reliability

└── Security
```

Examples of security requirements include:

- Authentication
- Authorization
- Encryption
- Logging
- Audit trails
- Availability
- Privacy protection

---

# Functional vs Security Requirements

| Functional Requirement | Security Requirement |
|------------------------|----------------------|
| User can log in | Login requires secure authentication |
| User can upload files | Uploaded files must be validated |
| User can reset password | Password reset must verify identity |
| User can download reports | Access requires authorization |
| User can search records | Search requests must be validated |

Security requirements support and protect functional requirements.

---

# Secure Architecture

```
                 Internet

                     │

                     ▼

              Load Balancer

                     │

                     ▼

          Web Application Firewall

                     │

                     ▼

             Web Application

      ┌──────────┼──────────┐

      ▼          ▼          ▼

 Authentication Authorization Validation

      │          │          │

      └──────────┼──────────┘

                 ▼

           Business Logic

                 ▼

          Secure Data Layer

                 ▼

             Database
```

Each architectural layer performs a specific security function.

---

# Layered Security

```
User

↓

Authentication

↓

Authorization

↓

Validation

↓

Business Rules

↓

Logging

↓

Monitoring
```

No single layer should be responsible for all security.

---

# Zero Trust Design

Zero Trust assumes that no request should be trusted automatically.

```
Every Request

↓

Verify Identity

↓

Verify Authorization

↓

Evaluate Context

↓

Allow

OR

Deny
```

Trust is continuously verified rather than assumed.

---

# Zero Trust Principles

```
Zero Trust

│

├── Verify Explicitly

├── Least Privilege

├── Continuous Validation

├── Assume Breach

└── Continuous Monitoring
```

These principles reduce reliance on implicit trust.

---

# Security Zones

Enterprise systems often separate workloads into different security zones.

```
Internet

↓

DMZ

↓

Application Network

↓

Database Network

↓

Management Network
```

Movement between zones should require appropriate security controls.

---

# Segmentation

```
Enterprise

│

├── User Services

├── Administrative Systems

├── Payment Systems

├── Internal APIs

└── Database Services
```

Segmentation limits the impact of individual component failures.

---

# Least Privilege by Design

```
User

↓

Assigned Role

↓

Required Permissions

↓

Business Operation
```

Permissions should be limited to operational needs.

---

# Fail Securely

Unexpected situations should not bypass security controls.

```
Unexpected Event

↓

Controlled Failure

↓

Secure Response

↓

Logging

↓

Alert
```

Applications should deny access safely when required information is unavailable.

---

# Secure Defaults

Applications should begin with restrictive settings.

```
New Feature

↓

Disabled by Default

↓

Configuration Review

↓

Explicit Approval

↓

Production
```

Explicit enablement reduces accidental exposure.

---

# Separation of Duties

Critical business processes should involve independent responsibilities.

```
Employee A

↓

Initiate Action

────────────

Employee B

↓

Approve Action
```

This reduces the likelihood of fraud and operational errors.

---

# Security Architecture Patterns

```
Patterns

│

├── Authentication Service

├── Authorization Service

├── Validation Layer

├── Audit Service

├── Secrets Management

├── API Gateway

└── Monitoring Platform
```

Reusable patterns improve consistency across applications.

---

# Security Design Review

A design review examines architecture before implementation.

Checklist:

```
✓ Authentication

✓ Authorization

✓ Trust Boundaries

✓ Data Classification

✓ Encryption

✓ Logging

✓ Monitoring

✓ Third-Party Integrations

✓ Business Logic

✓ Availability
```

Review findings should be documented and tracked.

---

# Design Validation

```
Architecture

↓

Threat Modeling

↓

Design Review

↓

Risk Assessment

↓

Approval

↓

Development
```

Validation confirms that security objectives have been addressed before coding begins.

---

# Enterprise Governance

```
Security Policy

↓

Architecture Standards

↓

Secure Coding Standards

↓

Design Reviews

↓

Compliance

↓

Continuous Improvement
```

Governance promotes consistent security practices across teams.

---

# Design Documentation

Architectural documentation should include:

- Security objectives
- Trust boundaries
- Data flows
- Security controls
- Assumptions
- Risks
- Design decisions
- Review history

Good documentation supports future maintenance and audits.

---

# Enterprise Example

A healthcare management system:

```
Patient

↓

Authentication

↓

Authorization

↓

Appointment Request

↓

Business Validation

↓

Medical Records

↓

Audit Logging

↓

Monitoring
```

Each component contributes to maintaining confidentiality and integrity.

---

# Operational Security

After deployment:

```
Deployment

↓

Monitoring

↓

Logging

↓

Metrics

↓

Review

↓

Improvement
```

Secure design is an ongoing operational responsibility.

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Rapid feature delivery | Integrate security reviews into development workflows |
| Multiple development teams | Standardize architecture and coding standards |
| Legacy systems | Prioritize modernization based on risk |
| Third-party integrations | Perform architectural and security assessments |
| Growing cloud environments | Apply consistent security architecture across environments |

---

# Enterprise Security Checklist

```
✓ Security Requirements Defined

✓ Threat Modeling Completed

✓ Trust Boundaries Identified

✓ Secure Defaults Configured

✓ Least Privilege Applied

✓ Zero Trust Principles Considered

✓ Design Review Approved

✓ Documentation Completed

✓ Monitoring Planned

✓ Governance Requirements Met
```

---

# Hands-on Lab (Conceptual)

1. Select a sample enterprise application.
2. Draw its high-level architecture.
3. Identify trust boundaries and security zones.
4. Define security requirements alongside functional requirements.
5. Conduct a conceptual design review using the checklist above.
6. Recommend architectural improvements.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is the purpose of security requirements engineering?
2. Why should security be incorporated during architecture rather than after deployment?
3. What are the principles of Zero Trust?
4. Why are secure defaults important?
5. What is separation of duties?
6. Why should organizations perform design reviews?
7. What information belongs in security design documentation?
8. How does segmentation improve enterprise security?
9. What is meant by "fail securely"?
10. Why is governance important for secure design?

---

# Best Practices

- Define security requirements during project planning.
- Apply Zero Trust principles throughout the architecture.
- Use layered security and segmentation.
- Conduct formal design reviews before implementation.
- Maintain comprehensive security documentation.
- Standardize architectural patterns across projects.
- Continuously review and improve designs after deployment.

---

# Common Mistakes

- Designing first and considering security later.
- Relying solely on implementation controls.
- Assuming internal systems are inherently trusted.
- Omitting documentation of trust boundaries.
- Allowing excessive privileges by default.
- Skipping architecture reviews due to project deadlines.

---

# Key Takeaways

- Secure design begins with clear security requirements and structured architecture.
- Zero Trust, least privilege, segmentation, and secure defaults strengthen enterprise systems.
- Design reviews validate security decisions before implementation.
- Governance and documentation ensure consistency across development teams.
- Secure design is an ongoing process that continues throughout the application's lifecycle.

```text id="rrks28"
**Next:** Part 4
```