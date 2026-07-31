# Cloud Threat Modeling

## Overview

Cloud Threat Modeling is the structured process of identifying, analyzing, prioritizing, and mitigating security threats that may affect cloud-based systems, applications, infrastructure, APIs, data, identities, and workloads throughout their lifecycle.

Rather than reacting to security incidents after deployment, threat modeling enables organizations to proactively discover potential attack paths during the design and development phases. This allows security controls to be incorporated before vulnerabilities become exploitable.

Cloud environments introduce unique challenges compared to traditional on-premises infrastructure, including:

- Dynamic infrastructure
- Elastic workloads
- Multi-cloud environments
- Hybrid cloud deployments
- Shared responsibility
- API-driven architectures
- Serverless computing
- Containers and Kubernetes
- Identity-centric access
- Infrastructure as Code (IaC)

Threat modeling helps organizations answer fundamental security questions such as:

- What are we protecting?
- Who are the potential attackers?
- What assets are most valuable?
- How can an attacker compromise them?
- What is the potential business impact?
- Which security controls reduce the identified risks?

The outcome of threat modeling is a prioritized understanding of risks and actionable mitigation strategies.

---

## Why It Matters

Modern cloud applications are highly interconnected. A single business service may depend on:

- Identity providers
- APIs
- Databases
- Storage services
- Load balancers
- Serverless functions
- Kubernetes clusters
- Third-party SaaS platforms
- CI/CD pipelines
- External integrations

Each dependency expands the attack surface.

Without structured threat modeling, organizations may overlook:

- Identity abuse
- API vulnerabilities
- Misconfigured storage
- Privilege escalation paths
- Lateral movement opportunities
- Supply chain risks
- Insider threats
- Data exposure
- Configuration drift

Threat modeling enables security teams to identify these risks before deployment.

Benefits include:

- Reduced attack surface
- Secure-by-design architectures
- Improved risk management
- Better regulatory compliance
- Lower remediation costs
- Stronger security culture
- Faster incident response planning
- Better prioritization of security investments

Threat modeling shifts security "left" by integrating it into architecture and development rather than treating it as a post-deployment activity.

---

## Architecture

A simplified cloud threat modeling workflow is shown below.

```
            Business Requirements

                     │

                     ▼

           Cloud Architecture Design

                     │

                     ▼

            Identify Critical Assets

                     │

                     ▼

           Identify Trust Boundaries

                     │

                     ▼

          Identify Threat Scenarios

                     │

                     ▼

            Risk Assessment & Ranking

                     │

                     ▼

         Select Security Mitigations

                     │

                     ▼

      Validate Controls & Architecture

                     │

                     ▼

      Continuous Monitoring & Updates
```

Threat modeling is iterative and should be revisited whenever architectures, applications, or business requirements change.

---

## Key Concepts

### Assets

Assets are anything of value that requires protection.

Examples include:

- Customer data
- Databases
- Encryption keys
- Cloud storage
- APIs
- Identity providers
- Virtual Machines
- Containers
- Kubernetes clusters
- Source code
- CI/CD pipelines
- Backups
- Secrets
- Business applications

Asset identification is the first step in effective threat modeling.

---

### Threats

A threat is any potential event or action capable of exploiting a vulnerability and causing harm.

Examples include:

- Credential theft
- Insider abuse
- Data exfiltration
- API attacks
- Ransomware
- Denial-of-Service (DoS)
- Supply chain compromise
- Privilege escalation
- Malware
- Account takeover

Threats may originate from external attackers, malicious insiders, compromised third parties, or automated attacks.

---

### Vulnerabilities

Vulnerabilities are weaknesses that can be exploited by threats.

Examples include:

- Weak authentication
- Misconfigured IAM policies
- Publicly exposed storage
- Insecure APIs
- Missing encryption
- Unpatched software
- Hardcoded secrets
- Excessive permissions
- Insecure network configurations

Threat modeling identifies vulnerabilities before attackers can exploit them.

---

### Attack Surface

The attack surface represents all possible entry points into a cloud environment.

Examples include:

- Public APIs
- Web applications
- Administrative portals
- Cloud consoles
- Storage services
- VPN gateways
- Kubernetes dashboards
- Serverless endpoints
- Third-party integrations

Reducing the attack surface lowers overall security risk.

---

### Trust Boundaries

A trust boundary is a point where data or requests move between components with different trust levels.

Examples include:

```
Internet

↓

API Gateway

↓

Application

↓

Database
```

Crossing a trust boundary requires authentication, authorization, and validation.

Threat modeling focuses heavily on identifying and securing these boundaries.

---

### Data Flow

Data Flow Diagrams (DFDs) help visualize how information moves through a cloud system.

Example:

```
User

↓

Load Balancer

↓

Application

↓

API

↓

Database

↓

Cloud Storage
```

Analyzing data flows helps identify where sensitive information is processed, stored, or transmitted.

---

### Threat Actors

Threat actors are entities capable of attacking cloud resources.

Examples include:

- Cybercriminals
- Nation-state actors
- Hacktivists
- Insider threats
- Competitors
- Third-party vendors
- Automated bots
- Script kiddies

Understanding attacker capabilities improves defensive planning.

---

### STRIDE Threat Model

STRIDE is one of the most widely used threat modeling methodologies.

| Category | Description |
|----------|-------------|
| **S** – Spoofing | Pretending to be another identity |
| **T** – Tampering | Unauthorized modification of data or systems |
| **R** – Repudiation | Denying performed actions without sufficient audit evidence |
| **I** – Information Disclosure | Exposure of confidential information |
| **D** – Denial of Service | Preventing legitimate use of services |
| **E** – Elevation of Privilege | Gaining higher permissions than intended |

STRIDE helps systematically identify threats across different system components.

---

### Risk

Risk is the combination of:

- Likelihood of exploitation
- Potential business impact

A common representation is:

```
Risk = Likelihood × Impact
```

Organizations should prioritize high-risk threats for mitigation.

---

### Mitigations

Mitigations are security controls implemented to reduce identified risks.

Examples include:

- Multi-Factor Authentication (MFA)
- Least Privilege Access
- Encryption
- Network segmentation
- Secure coding practices
- Web Application Firewalls (WAF)
- API gateways
- Continuous monitoring
- Vulnerability management
- Security awareness training

Each mitigation should directly address one or more identified threats.

---

### Assumptions

Threat modeling relies on documented assumptions regarding the environment.

Examples include:

- Cloud provider responsibilities
- Trusted third-party services
- Identity provider availability
- Network architecture
- Compliance requirements

Assumptions should be reviewed regularly because changes may introduce new risks.

---

### Residual Risk

Not every risk can be eliminated.

Residual risk is the level of risk remaining after security controls have been applied.

Organizations may choose to:

- Accept the risk
- Mitigate it further
- Transfer it (e.g., through insurance or contractual agreements)
- Avoid the associated activity

Residual risks should be documented and reviewed periodically.

---

### Continuous Threat Modeling

Threat modeling is not a one-time exercise.

Organizations should revisit threat models when:

- New cloud services are adopted
- Architectures change
- New APIs are introduced
- Business requirements evolve
- Threat intelligence identifies emerging attack techniques
- Major software releases occur
- Compliance requirements change

Continuous threat modeling ensures that security controls remain effective as cloud environments evolve.

---

## How It Works

Cloud Threat Modeling is a systematic process that identifies potential threats before they can be exploited. Instead of waiting for security testing after development, threat modeling evaluates cloud architectures during the design phase, enabling security controls to be integrated from the beginning.

The process is iterative and should be repeated whenever:

- New cloud services are introduced
- Architectures change
- APIs are added or modified
- Infrastructure as Code (IaC) templates change
- Third-party integrations are implemented
- Compliance requirements evolve
- New threat intelligence becomes available

A mature cloud threat modeling process combines architecture review, risk analysis, attacker perspective, and mitigation planning.

---

## Cloud Threat Modeling Workflow

```
      Define System Scope

               │

               ▼

       Identify Assets

               │

               ▼

   Create Architecture Diagram

               │

               ▼

   Identify Trust Boundaries

               │

               ▼

     Map Data Flows

               │

               ▼

    Identify Threats (STRIDE)

               │

               ▼

 Assess Likelihood & Impact

               │

               ▼

      Prioritize Risks

               │

               ▼

 Select Security Controls

               │

               ▼

 Validate & Continuously Review
```

Each stage builds upon the previous one to create a comprehensive understanding of cloud security risks.

---

## Step 1 – Define the Scope

Begin by defining exactly what will be analyzed.

Examples include:

- Cloud applications
- APIs
- Kubernetes clusters
- Serverless workloads
- Virtual Machines
- CI/CD pipelines
- Identity systems
- Multi-cloud environments

Clearly defining the scope prevents important components from being overlooked.

---

## Step 2 – Identify Critical Assets

Determine which resources require protection.

Typical cloud assets include:

- Customer information
- Databases
- Object storage
- Encryption keys
- Secrets
- Source code repositories
- Identity providers
- Administrative consoles
- Business applications
- Container images

Questions to ask:

- What data is sensitive?
- Which systems are business-critical?
- Which assets would attackers target first?

---

## Step 3 – Create an Architecture Diagram

Document how cloud components interact.

Example:

```
Users

↓

Cloud Load Balancer

↓

Web Application

↓

API Gateway

↓

Application Services

↓

Database

↓

Object Storage
```

Architecture diagrams help identify attack paths and trust boundaries.

---

## Step 4 – Identify Trust Boundaries

Trust boundaries represent locations where requests cross different security domains.

Example:

```
Internet

↓

Cloud Firewall

↓

Application

↓

Database
```

Each trust boundary should enforce:

- Authentication
- Authorization
- Encryption
- Input validation
- Logging

Trust boundaries often represent the highest-risk locations.

---

## Step 5 – Map Data Flows

Understand how information moves through the environment.

```
Customer

↓

Web Application

↓

Authentication Service

↓

API

↓

Database

↓

Storage
```

For each data flow, identify:

- Sensitive information
- Encryption requirements
- Authentication mechanisms
- Validation controls
- Logging points

---

## Step 6 – Identify Threats Using STRIDE

Analyze each component using the STRIDE framework.

| Threat Category | Example |
|----------------|---------|
| Spoofing | Credential theft |
| Tampering | Modifying cloud resources |
| Repudiation | Missing audit logs |
| Information Disclosure | Public storage bucket |
| Denial of Service | API flooding |
| Elevation of Privilege | IAM privilege escalation |

STRIDE provides a structured approach for discovering security threats.

---

## Step 7 – Assess Risk

Evaluate each identified threat based on:

- Likelihood
- Business impact
- Technical impact
- Ease of exploitation
- Existing security controls

Example risk matrix:

| Likelihood | Impact | Risk |
|------------|--------|------|
| High | High | Critical |
| High | Medium | High |
| Medium | High | High |
| Medium | Medium | Medium |
| Low | High | Medium |
| Low | Low | Low |

High-risk threats should receive priority during remediation.

---

## Step 8 – Select Security Controls

Choose mitigations that reduce identified risks.

Examples include:

| Threat | Mitigation |
|---------|------------|
| Credential theft | MFA, Conditional Access |
| Data exposure | Encryption, Access Control |
| Privilege escalation | Least Privilege IAM |
| API abuse | API Gateway, Rate Limiting |
| Lateral movement | Microsegmentation |
| Secret leakage | Secrets Management |

Each control should directly address one or more identified threats.

---

## Step 9 – Validate Mitigations

Security controls should be tested before production deployment.

Validation methods include:

- Architecture reviews
- Penetration testing
- Vulnerability scanning
- Secure code review
- Configuration assessments
- Red team exercises
- Purple team exercises

Testing confirms that implemented controls effectively reduce risk.

---

## Step 10 – Continuously Update the Threat Model

Threat models must evolve alongside cloud environments.

Update models when:

- New workloads are deployed
- Infrastructure changes
- IAM policies are modified
- Third-party integrations change
- Compliance requirements are updated
- New attack techniques emerge

Threat modeling is an ongoing process rather than a one-time activity.

---

## Practical Example

### Example 1 – E-Commerce Platform

Architecture:

```
Customer

↓

Cloud Load Balancer

↓

Web Application

↓

Payment API

↓

Database
```

Potential threats:

- Credential stuffing
- SQL injection
- API abuse
- Payment fraud
- Data exfiltration
- Denial-of-Service attacks

Mitigations:

- MFA for administrators
- Web Application Firewall (WAF)
- Parameterized queries
- API authentication
- Encryption
- Continuous monitoring

---

### Example 2 – Kubernetes Cluster

Assets:

- Kubernetes API Server
- Worker Nodes
- Secrets
- Container Images
- Persistent Volumes

Potential threats:

- Privilege escalation
- Compromised container images
- Secret leakage
- Lateral movement
- Insecure RBAC

Mitigations:

- RBAC
- Admission controllers
- Image signing
- Network policies
- Secret management
- Runtime security monitoring

---

### Example 3 – Serverless Application

Architecture:

```
User

↓

API Gateway

↓

Serverless Function

↓

Cloud Database
```

Potential threats:

- Excessive IAM permissions
- API abuse
- Event injection
- Secret exposure
- Function chaining attacks

Mitigations:

- Least Privilege IAM
- API authentication
- Secrets Manager
- Request validation
- Logging and monitoring

---

### Example 4 – Multi-Cloud Environment

Architecture:

```
AWS

↔

Azure

↔

Google Cloud

↓

Central Identity Provider
```

Potential threats:

- Identity synchronization failures
- Misconfigured trust relationships
- Inconsistent security policies
- Cross-cloud privilege escalation

Mitigations:

- Centralized IAM
- Unified logging
- Federated authentication
- Consistent policy enforcement
- Cross-cloud monitoring

---

## Detection

Threat modeling also defines what security events should be monitored to identify attempted or successful attacks.

---

### Identity-Based Threats

Monitor for:

- Multiple failed logins
- Impossible travel
- Privilege escalation
- MFA failures
- New administrator creation
- Suspicious service account activity

Identity anomalies are often early indicators of compromise.

---

### Network-Based Threats

Detect:

- Port scanning
- Unexpected east-west traffic
- Unauthorized inbound connections
- VPN anomalies
- Data exfiltration attempts
- DNS tunneling

Network telemetry provides visibility into attacker movement.

---

### API Threats

Monitor:

- Excessive requests
- Authentication failures
- Injection attempts
- Token misuse
- Rate-limit violations
- Unexpected endpoint access

API security monitoring is critical in cloud-native environments.

---

### Infrastructure Threats

Watch for:

- Unauthorized IAM changes
- Security group modifications
- Firewall rule changes
- Public storage exposure
- Infrastructure drift
- Unapproved deployments

Configuration changes should be continuously audited.

---

### Workload Threats

Detect:

- Suspicious container behavior
- Unexpected process execution
- Cryptocurrency mining
- Unauthorized outbound connections
- Runtime privilege escalation
- Secret access anomalies

Runtime monitoring improves visibility into compromised workloads.

---

### Data Threats

Monitor:

- Large downloads
- Unusual database queries
- Encryption key misuse
- Sensitive file access
- Unexpected backup activity
- Cross-region data transfers

Data-centric monitoring helps identify exfiltration attempts.

---

### Detection Best Practices

- Enable comprehensive cloud audit logging.
- Integrate logs with a centralized SIEM.
- Monitor identity, network, workload, and data events together.
- Use User and Entity Behavior Analytics (UEBA) to identify anomalies.
- Continuously review high-risk architectural components.
- Update detection rules as threat models evolve.
- Validate alerts through regular security exercises.
- Incorporate threat intelligence into monitoring workflows.
- Periodically reassess trust boundaries and attack paths.
- Treat threat modeling as a living security process.

---

