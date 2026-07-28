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

```text id="rrks28"
**Next:** Part 2
```