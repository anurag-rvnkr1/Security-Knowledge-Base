# 27 - API Security Interview Questions

# Introduction

API Security is one of the fastest-growing domains in cybersecurity. Organizations increasingly expect engineers to understand secure API design, authentication, authorization, cloud-native architectures, DevSecOps, monitoring, and incident response.

Interview questions often evaluate:

- Fundamental concepts
- Practical implementation
- Security architecture
- Problem-solving ability
- Hands-on experience
- Incident response knowledge
- Threat modeling
- Communication skills

```
Knowledge

     │

Experience

     │

Problem Solving

     │

Communication

     ▼

Successful Interview
```

---

# Learning Objectives

After completing this chapter, you will be able to:

- Answer common API Security interview questions.
- Explain security concepts clearly.
- Solve architecture scenarios.
- Demonstrate secure development knowledge.
- Discuss incident response workflows.
- Prepare for penetration testing interviews.
- Prepare for DevSecOps and SOC interviews.
- Improve confidence during technical interviews.

---

# Interview Preparation Strategy

Before attending interviews, review:

- HTTP fundamentals
- REST architecture
- GraphQL
- gRPC
- Authentication
- Authorization
- JWT
- OAuth 2.0
- OWASP API Security Top 10
- Secure coding
- Monitoring
- Incident response

Employers often evaluate both conceptual understanding and practical application.

---

# Frequently Tested Areas

| Domain | Importance |
|----------|------------|
| REST APIs | Very High |
| Authentication | Very High |
| Authorization | Very High |
| JWT | High |
| OAuth 2.0 | High |
| OWASP API Top 10 | Very High |
| API Gateway | High |
| Rate Limiting | High |
| Secure Development | Very High |
| Monitoring | High |
| Incident Response | Medium |
| DevSecOps | High |

---

# Fundamental Questions

## 1. What is an API?

**Answer**

An API (Application Programming Interface) is a defined interface that enables different software systems to communicate using standardized requests and responses.

---

## 2. Why are APIs attractive attack targets?

**Answer**

Because APIs often expose:

- Business functionality
- Sensitive data
- Authentication mechanisms
- Administrative operations
- Backend services

Compromising an API can directly affect business operations and user data.

---

## 3. What is REST?

**Answer**

REST is an architectural style based on stateless communication using standard HTTP methods to manipulate resources identified by URIs.

---

## 4. What is stateless communication?

**Answer**

Each request contains all information required for processing.

The server does not depend on previous requests to understand the current request.

---

## 5. What is the difference between REST and SOAP?

| REST | SOAP |
|-------|------|
| HTTP-based | XML protocol |
| Lightweight | More structured |
| JSON commonly used | XML only |
| Faster | Typically heavier |
| Flexible | Strict standards |

---

## 6. What is GraphQL?

**Answer**

GraphQL is a query language and runtime that allows clients to request exactly the data they need through a single endpoint.

---

## 7. What is gRPC?

**Answer**

gRPC is a high-performance RPC framework that uses Protocol Buffers for efficient communication between services.

---

## 8. What is an API Gateway?

**Answer**

An API Gateway acts as a centralized entry point that provides routing, authentication, authorization, rate limiting, monitoring, logging, and policy enforcement.

---

## 9. What is API Versioning?

**Answer**

API versioning allows changes to be introduced without breaking existing clients.

---

## 10. Why is HTTPS mandatory?

**Answer**

HTTPS encrypts data in transit, protecting against interception, tampering, and impersonation attacks.

---

# Authentication Questions

## 11. What is authentication?

Authentication verifies the identity of a user, application, or service.

---

## 12. What is authorization?

Authorization determines what an authenticated identity is permitted to do.

---

## 13. What is the difference?

```
Authentication

Who are you?

──────────────

Authorization

What are you allowed to do?
```

---

## 14. What is Multi-Factor Authentication?

Authentication using two or more independent verification factors.

Examples

- Password
- Authenticator application
- Hardware security key
- Biometrics

---

## 15. What is Single Sign-On (SSO)?

A mechanism allowing users to authenticate once and access multiple applications.

---

## 16. What is JWT?

A JSON Web Token is a signed token commonly used to securely transmit identity and authorization claims.

---

## 17. Should JWTs be encrypted?

Not necessarily.

JWTs are commonly signed for integrity. Encryption is used only when confidentiality of the token contents is required.

---

## 18. What is OAuth 2.0?

OAuth 2.0 is an authorization framework that enables applications to obtain delegated access to protected resources.

---

## 19. What is OpenID Connect?

OpenID Connect (OIDC) extends OAuth 2.0 by adding standardized authentication and identity information.

---

## 20. Why should access tokens expire?

Short-lived tokens reduce the impact if a token is compromised.

---

# Authorization Questions

## 21. What is RBAC?

Role-Based Access Control grants permissions according to assigned roles.

---

## 22. What is ABAC?

Attribute-Based Access Control evaluates attributes such as user, resource, environment, and action before making authorization decisions.

---

## 23. What is Least Privilege?

Every user or service receives only the permissions necessary to perform its required tasks.

---

## 24. What is BOLA?

Broken Object Level Authorization occurs when APIs fail to verify that a user is authorized to access a requested object.

---

## 25. Why should authorization be checked on every request?

Permissions may change between requests, and every protected action must be independently validated.

---

# Secure Development Questions

## 26. Why validate input?

To prevent malformed, malicious, or unexpected data from reaching business logic.

---

## 27. What is allowlist validation?

Only explicitly permitted values are accepted.

Everything else is rejected.

---

## 28. What is output encoding?

Preparing output so it is interpreted safely in its intended context.

---

## 29. Why avoid hard-coded secrets?

Hard-coded secrets are difficult to rotate, easy to leak, and increase the impact of source code exposure.

---

## 30. What is Security by Design?

Security is incorporated during requirements, architecture, implementation, testing, deployment, and operations—not added later.

---

# OWASP API Security Questions

## 31. What is the OWASP API Security Top 10?

A widely recognized list of the most significant API security risks.

---

## 32. Which vulnerability is most common?

Broken Object Level Authorization (BOLA) is one of the most frequently observed and impactful API vulnerabilities.

---

## 33. What causes BFLA?

Broken Function Level Authorization occurs when APIs fail to enforce permissions for specific operations or functions.

---

## 34. What is unrestricted resource consumption?

Failure to properly limit expensive operations, potentially allowing abuse that affects availability.

---

## 35. What is security misconfiguration?

Weak or incorrect configuration that introduces security weaknesses.

---

# API Testing Questions

## 36. What is API fuzzing?

Automatically sending unexpected, malformed, or boundary-case inputs to evaluate API robustness and identify potential vulnerabilities.

---

## 37. Difference between vulnerability scanning and penetration testing?

| Vulnerability Scanning | Penetration Testing |
|------------------------|--------------------|
| Mostly automated | Manual + automated |
| Broad coverage | In-depth validation |
| Finds potential issues | Demonstrates exploitability |
| Regular execution | Periodic assessment |

---

## 38. Why manually verify scanner findings?

Automated tools can produce false positives and false negatives.

Manual validation improves accuracy.

---

## 39. What is contract testing?

Testing that verifies an API implementation conforms to its documented specification.

---

## 40. What is API enumeration?

The process of identifying available API endpoints, methods, versions, and functionality.

---

# Monitoring Questions

## 41. What should be logged?

Security-relevant events such as

- Authentication
- Authorization
- Administrative actions
- Errors
- Configuration changes
- Audit events

---

## 42. What are the three pillars of observability?

- Logs
- Metrics
- Traces

---

## 43. Why use correlation IDs?

To follow a single request across multiple systems during troubleshooting and investigations.

---

## 44. What is SIEM?

A Security Information and Event Management platform that centralizes telemetry, correlates events, and supports threat detection and investigations.

---

## 45. What is detection engineering?

The process of designing, implementing, testing, and continuously improving security detections.

---

# Incident Response Questions

## 46. What is containment?

Actions taken to stop or limit ongoing damage during an incident.

---

## 47. Difference between containment and eradication?

Containment limits the attack.

Eradication removes its root cause.

---

## 48. Why preserve evidence?

Evidence supports investigations, root cause analysis, compliance, and legal processes where applicable.

---

## 49. What is an IOC?

An Indicator of Compromise suggests that a system may have been compromised.

---

## 50. What is an IOA?

An Indicator of Attack describes suspicious attacker behavior that may indicate malicious activity before a confirmed compromise.

---

# Architecture Questions

## 51. Design a secure public API.

Expected discussion

- HTTPS
- API Gateway
- Authentication
- Authorization
- Input validation
- Rate limiting
- Logging
- Monitoring
- WAF
- SIEM
- Secure deployment

---

## 52. Where should rate limiting be enforced?

Preferably at the API Gateway, while applications may implement additional business-specific limits where appropriate.

---

## 53. How would you secure microservices?

Discuss

- Mutual TLS
- Service authentication
- Least privilege
- Network segmentation
- Secrets management
- Monitoring
- Centralized logging

---

## 54. How would you protect sensitive APIs?

Expected controls

- MFA where appropriate
- Strong authorization
- Short-lived tokens
- Audit logging
- Rate limiting
- Monitoring
- Continuous security testing

---

## 55. What makes an API security architecture mature?

Characteristics include

- Layered defenses
- Automation
- Continuous monitoring
- Threat detection
- Secure SDLC
- Incident response readiness
- Continuous improvement

---

**Next:** Advanced scenario-based interviews, whiteboard system design questions, practical penetration testing questions, HR and behavioral questions, and interview tips.