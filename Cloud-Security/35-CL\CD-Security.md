# CI/CD Security

## Overview

CI/CD Security is the practice of protecting Continuous Integration (CI) and Continuous Delivery/Deployment (CD) pipelines against unauthorized access, malicious code, supply chain attacks, credential theft, and insecure software releases.

Modern organizations deploy applications multiple times per day using automated pipelines. These pipelines compile source code, execute tests, scan for vulnerabilities, build artifacts, package containers, deploy infrastructure, and release applications into production.

Because CI/CD pipelines have privileged access to source code, secrets, infrastructure, and production environments, they are one of the most attractive targets for attackers.

CI/CD Security integrates security controls throughout the software delivery lifecycle to ensure that every build, artifact, and deployment is secure, verified, and compliant.

A mature CI/CD Security program includes:

- Secure source code management
- Identity and access management
- Pipeline hardening
- Secrets management
- Dependency security
- Infrastructure as Code (IaC) validation
- Container image scanning
- Artifact integrity verification
- Policy as Code
- Runtime monitoring
- Supply chain security
- Continuous compliance

By embedding security into every pipeline stage, organizations can accelerate software delivery without compromising security.

---

## Why It Matters

Modern cloud-native environments rely heavily on CI/CD automation.

A compromised pipeline can allow attackers to:

- Inject malicious code
- Steal secrets
- Deploy backdoors
- Modify production infrastructure
- Bypass security controls
- Distribute compromised software
- Access sensitive customer data
- Disrupt business operations

Since CI/CD systems often possess elevated privileges, a single pipeline compromise can affect multiple applications and cloud environments.

Implementing CI/CD Security helps organizations:

- Protect software supply chains
- Prevent unauthorized deployments
- Detect malicious code early
- Secure production releases
- Reduce human error
- Improve compliance
- Strengthen auditability
- Accelerate secure software delivery

---

## Architecture

The following illustrates a secure CI/CD pipeline.

```
Developer

     │

     ▼

Source Code Repository

     │

     ▼

Pull Request Review

     │

     ▼

Continuous Integration

     │

 ┌───┼───────────────────────────────┐
 │   │                               │
 ▼   ▼                               ▼

SAST   Secrets Scan          Dependency Scan

 │      │                      │

 └──────┼───────────────┬──────┘
        │               │
        ▼               ▼

Container Scan     IaC Security Scan

        │

        ▼

Policy Validation

        │

        ▼

Artifact Signing

        │

        ▼

Artifact Repository

        │

        ▼

Continuous Delivery Pipeline

        │

        ▼

Deployment Approval

        │

        ▼

Production

        │

        ▼

Continuous Monitoring
```

Every stage contains security controls that reduce the likelihood of introducing vulnerabilities into production.

---

## Key Concepts

### Continuous Integration (CI)

Continuous Integration is the automated process of frequently merging code changes into a shared repository.

Typical CI activities include:

- Code compilation
- Unit testing
- Static code analysis
- Dependency validation
- Security scanning
- Artifact generation

CI enables rapid feedback and early defect detection.

---

### Continuous Delivery (CD)

Continuous Delivery prepares validated software for release through automated deployment pipelines.

Deployment may require manual approval before production.

Benefits include:

- Reliable releases
- Reduced deployment risk
- Repeatable deployment processes
- Improved software quality

---

### Continuous Deployment

Continuous Deployment automatically releases validated software into production without manual approval.

This approach requires:

- Mature testing
- Strong security controls
- Comprehensive monitoring
- Reliable rollback mechanisms

Continuous Deployment is best suited for organizations with advanced DevSecOps practices.

---

### Pipeline Security

CI/CD pipelines should be protected using multiple security controls.

Key controls include:

- Strong authentication
- Multi-Factor Authentication (MFA)
- Least privilege access
- Pipeline isolation
- Secure runners
- Audit logging
- Immutable build environments

Protecting the pipeline is essential because it orchestrates the entire software delivery process.

---

### Secure Source Code Management

Repositories should enforce:

- Branch protection
- Mandatory pull requests
- Peer reviews
- Signed commits
- Role-based access control
- Audit logging

Secure repository management reduces the risk of unauthorized code changes.

---

### Secrets Management

Pipelines require credentials to interact with cloud resources and external services.

Sensitive information includes:

- API keys
- Cloud credentials
- Database passwords
- Certificates
- Access tokens
- SSH keys

Secrets should never be stored in source code or pipeline configuration files.

---

### Static Application Security Testing (SAST)

SAST analyzes application source code for vulnerabilities before execution.

Typical findings include:

- SQL Injection
- Cross-Site Scripting (XSS)
- Hardcoded secrets
- Weak cryptography
- Input validation issues
- Authentication flaws

SAST supports early vulnerability detection during development.

---

### Software Composition Analysis (SCA)

Modern applications rely heavily on third-party libraries.

SCA identifies:

- Known vulnerabilities
- Outdated dependencies
- License issues
- Unsupported packages
- Malicious components

Dependency security is a critical aspect of software supply chain protection.

---

### Infrastructure as Code Security

CI/CD pipelines should validate infrastructure definitions before deployment.

Validation includes:

- Encryption settings
- IAM permissions
- Network security
- Compliance policies
- Resource configuration
- Secrets detection

This prevents insecure infrastructure from being provisioned.

---

### Container Security

If applications are containerized, CI/CD pipelines should validate container images.

Checks include:

- Base image verification
- Vulnerability scanning
- Malware detection
- Root user detection
- Image signing
- Configuration validation

Secure containers improve workload resilience.

---

### Artifact Integrity

Pipeline-generated artifacts should be protected against tampering.

Recommended controls include:

- Digital signatures
- Cryptographic hashing
- Trusted artifact repositories
- Integrity verification
- Provenance tracking

Artifact integrity helps prevent software supply chain attacks.

---

### Policy as Code

Security and compliance requirements should be enforced automatically.

Example policies include:

- No critical vulnerabilities
- Encryption enabled
- Mandatory approvals
- Approved deployment regions
- Resource tagging
- Signed artifacts only

Policy enforcement ensures consistent governance across all deployments.

---

### CI/CD Security Lifecycle

| Phase | Security Activities |
|--------|---------------------|
| Plan | Security requirements, threat modeling |
| Develop | Secure coding, peer reviews |
| Build | SAST, SCA, secrets scanning |
| Validate | IaC scanning, policy checks, compliance validation |
| Package | Container scanning, artifact signing |
| Release | Deployment approvals, integrity verification |
| Deploy | Secure automated deployment, audit logging |
| Operate | Monitoring, incident detection, continuous compliance |

---

### Benefits of CI/CD Security

| Benefit | Description |
|----------|-------------|
| Faster Secure Releases | Automated security throughout the pipeline |
| Reduced Human Error | Standardized deployment processes |
| Early Vulnerability Detection | Security testing during development |
| Supply Chain Protection | Secured dependencies and artifacts |
| Compliance | Automated policy enforcement |
| Auditability | Complete deployment history |
| Consistency | Repeatable and reliable software releases |
| Operational Resilience | Improved reliability and recovery |

CI/CD Security enables organizations to deliver software rapidly while maintaining strong security, governance, and compliance across the entire software delivery lifecycle.

---

## How It Works

CI/CD Security integrates automated security controls into every stage of the software delivery pipeline. Rather than treating security as a separate activity before production deployment, security becomes an integral part of building, testing, packaging, and releasing applications.

Every code change is automatically validated against security, quality, and compliance requirements before deployment.

---

# Secure CI/CD Workflow

```
Developer Commit

        │

        ▼

Source Code Repository

        │

        ▼

Pull Request Review

        │

        ▼

Continuous Integration

        │

 ┌──────┼─────────────────────────────────────┐
 │      │             │            │          │
 ▼      ▼             ▼            ▼          ▼

SAST  Secrets Scan  SCA Scan   Unit Tests  IaC Scan

 │      │             │            │          │
 └──────┴─────────────┴────────────┴──────────┘

                     │

                     ▼

Policy Validation

                     │

                     ▼

Container Build

                     │

                     ▼

Container Security Scan

                     │

                     ▼

Artifact Signing

                     │

                     ▼

Artifact Repository

                     │

                     ▼

Deployment Approval

                     │

                     ▼

Production Deployment

                     │

                     ▼

Continuous Monitoring
```

Each stage introduces automated controls that reduce the likelihood of insecure software reaching production.

---

## Step 1 – Developer Commits Code

Developers submit code changes to a version-controlled repository.

Recommended controls include:

- Multi-Factor Authentication (MFA)
- Branch protection
- Signed commits
- Least privilege access
- Mandatory pull requests
- Audit logging

These controls protect the integrity of the source code.

---

## Step 2 – Pull Request Review

Infrastructure and application code undergo peer review before merging.

Reviewers verify:

- Secure coding practices
- Authentication logic
- Authorization controls
- Error handling
- Logging
- Compliance requirements
- Infrastructure definitions

Peer reviews improve software quality and identify security concerns early.

---

## Step 3 – Continuous Integration

Once approved, the CI pipeline automatically executes.

Typical activities include:

- Source retrieval
- Compilation
- Dependency installation
- Automated testing
- Build generation
- Security validation

CI ensures that every code change is evaluated consistently.

---

## Step 4 – Static Application Security Testing (SAST)

Automated SAST tools analyze source code without executing it.

Common findings include:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Weak cryptography
- Hardcoded credentials
- Authentication flaws

Developers remediate vulnerabilities before the build progresses.

---

## Step 5 – Secrets Scanning

Repositories and pipeline configurations are scanned for exposed secrets.

Typical detections include:

- API keys
- Cloud credentials
- Database passwords
- Private keys
- OAuth tokens
- Certificates

Secrets scanning helps prevent credential leakage.

---

## Step 6 – Software Composition Analysis (SCA)

Dependencies are analyzed for security and compliance.

Checks include:

- Known CVEs
- Outdated packages
- Unsupported libraries
- License compatibility
- Malicious packages

Organizations should update or replace vulnerable dependencies before release.

---

## Step 7 – Infrastructure as Code Validation

Infrastructure definitions are scanned for security misconfigurations.

Validation includes:

- Encryption settings
- IAM permissions
- Firewall rules
- Public resource exposure
- Logging configuration
- Compliance requirements

Infrastructure security is validated before provisioning.

---

## Step 8 – Policy Validation

Policy as Code engines automatically evaluate security requirements.

Example policies:

- Critical vulnerabilities prohibited
- Encryption required
- Mandatory resource tags
- Approved deployment regions only
- Signed container images
- Approved base images

Pipeline execution stops if policy violations are detected.

---

## Step 9 – Build and Scan Container Images

For containerized applications, the pipeline builds and validates images.

Security checks include:

- Vulnerability scanning
- Malware detection
- Base image verification
- Root user detection
- Configuration validation
- Image signing

Only trusted images should be promoted to production.

---

## Step 10 – Artifact Signing

Build outputs are cryptographically signed.

Protected artifacts include:

- Application binaries
- Container images
- Infrastructure packages
- Deployment bundles

Artifact signing ensures authenticity and integrity throughout the software supply chain.

---

## Step 11 – Deployment Approval

Organizations may require approvals before production deployment.

Approval criteria include:

- Successful testing
- Security scan completion
- Compliance validation
- Change management approval
- Release readiness

Approval workflows reduce deployment risk.

---

## Step 12 – Continuous Monitoring

After deployment, continuously monitor:

- Application health
- Infrastructure changes
- Security events
- Authentication activity
- Network traffic
- Policy compliance
- Runtime anomalies

Continuous monitoring detects threats that may emerge after release.

---

## Practical Example

### Example 1 – Secure Web Application Deployment

Scenario:

A development team submits a new feature for a cloud-hosted web application.

Pipeline activities:

- Source code review
- SAST scan
- Secrets scan
- Dependency validation
- Unit testing
- Container image build
- Image vulnerability scan
- Artifact signing
- Deployment approval
- Production deployment

Outcome:

- Secure application release
- Automated compliance validation
- Reduced deployment risk

---

### Example 2 – Vulnerable Dependency Detection

Scenario:

A developer introduces a library containing a high-severity vulnerability.

Pipeline actions:

- Software Composition Analysis identifies the vulnerable dependency.
- The build fails automatically.
- Developers update the package.
- The pipeline executes successfully after remediation.

Outcome:

- Vulnerable software never reaches production.
- Supply chain security is strengthened.

---

### Example 3 – Secret Detection

Scenario:

A developer accidentally commits a cloud access key.

Pipeline actions:

- Secrets scanning identifies the exposed credential.
- The pipeline stops.
- The credential is revoked and rotated.
- The repository is cleaned before deployment resumes.

Outcome:

- Credential exposure is contained before production deployment.

---

### Example 4 – Policy Violation

Scenario:

A deployment attempts to provision cloud storage without encryption.

Policy engine response:

- Encryption policy fails.
- Deployment is blocked.
- Security notification is generated.
- Infrastructure is corrected.
- Deployment resumes successfully.

Outcome:

- Organizational security policies remain consistently enforced.

---

## Detection

Continuous detection provides visibility into pipeline activity, software integrity, and potential security threats.

---

### Source Code Detection

Monitor repositories for:

- Unauthorized commits
- Force pushes
- Suspicious branches
- Repository permission changes
- Unexpected administrative actions

Repository monitoring protects software integrity.

---

### Pipeline Detection

Detect:

- Failed authentication attempts
- Unauthorized pipeline execution
- Runner compromise
- Unexpected configuration changes
- Privilege escalation
- Build manipulation

Pipeline monitoring reduces the likelihood of CI/CD compromise.

---

### Secrets Detection

Continuously identify:

- API keys
- Database credentials
- Private keys
- Cloud credentials
- OAuth tokens
- Certificates

Secrets should be removed and rotated immediately upon detection.

---

### Dependency Detection

Monitor for:

- Newly disclosed CVEs
- Unsupported packages
- License violations
- Malicious dependencies
- Outdated libraries

Regular dependency analysis improves supply chain resilience.

---

### Artifact Detection

Verify:

- Digital signatures
- Cryptographic hashes
- Provenance metadata
- Repository integrity
- Unauthorized modifications

Artifact verification prevents tampered software from being deployed.

---

### Runtime Detection

Monitor deployed applications for:

- Suspicious network activity
- Unauthorized access
- Privilege escalation
- Unexpected process execution
- Policy violations
- Configuration drift

Runtime monitoring complements pre-deployment security validation.

---

### Detection Best Practices

- Require security validation for every pipeline execution.
- Continuously scan source code and dependencies.
- Monitor CI/CD runners and build environments.
- Enforce artifact signing and integrity verification.
- Detect exposed secrets before code is merged.
- Continuously validate Infrastructure as Code templates.
- Integrate CI/CD events into centralized SIEM platforms.
- Alert on unauthorized pipeline configuration changes.
- Regularly review repository access and pipeline permissions.
- Investigate all failed security checks before approving releases.

---

## Prevention

Preventing CI/CD security incidents requires protecting every stage of the software delivery lifecycle, from source code creation to production deployment. Preventive controls should be automated wherever possible to ensure consistent, repeatable, and scalable security.

A defense-in-depth strategy should secure developers, repositories, pipelines, artifacts, infrastructure, deployment environments, and runtime workloads.

---

# CI/CD Security Prevention Lifecycle

```
Developer

     │

     ▼

Secure Source Repository

     │

     ▼

Protected Branches

     │

     ▼

Peer Review

     │

     ▼

Automated Security Validation

     │

     ▼

Policy as Code

     │

     ▼

Secure Build Environment

     │

     ▼

Artifact Signing

     │

     ▼

Controlled Deployment

     │

     ▼

Continuous Monitoring

     │

     ▼

Continuous Improvement
```

Security controls should be implemented throughout the lifecycle rather than concentrated at the final deployment stage.

---

## Secure Source Code Repositories

Protect repositories using multiple layers of security.

Recommended controls include:

- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)
- Branch protection
- Mandatory pull requests
- Signed commits
- Repository audit logging
- Least privilege permissions

Repositories should serve as trusted sources for software delivery.

---

## Implement Secure Coding Practices

Developers should follow secure software engineering principles.

Examples include:

- Input validation
- Output encoding
- Strong authentication
- Secure session management
- Parameterized queries
- Secure error handling
- Proper cryptographic implementation

Secure coding reduces vulnerabilities before they enter the pipeline.

---

## Enforce Automated Security Testing

Every pipeline execution should automatically perform:

- Static Application Security Testing (SAST)
- Software Composition Analysis (SCA)
- Secrets scanning
- Infrastructure as Code (IaC) scanning
- Container image scanning
- Policy validation

```
Code Commit

      │

      ▼

Automated Security Checks

      │

 ┌────┴────┐

 │         │

Pass      Fail

 │         │

 ▼         ▼

Deploy   Remediate
```

Automated validation ensures that insecure code cannot progress through the pipeline.

---

## Secure Build Environments

Build environments should be isolated and hardened.

Recommended protections include:

- Ephemeral build runners
- Minimal operating system images
- Restricted network access
- Strong authentication
- Immutable build environments
- Continuous patch management

Ephemeral runners reduce persistence opportunities for attackers.

---

## Protect Secrets

Sensitive credentials should never be stored in:

- Source code
- Pipeline definitions
- Build scripts
- Configuration files
- Container images

Instead:

- Use centralized secrets management.
- Rotate credentials regularly.
- Grant temporary credentials where possible.
- Audit secret usage continuously.

---

## Strengthen Identity and Access Management

Restrict permissions across the pipeline.

Apply:

- Least Privilege
- Just-In-Time (JIT) access where supported
- Role separation
- Service account isolation
- Short-lived credentials
- Continuous access reviews

Strong identity management reduces the impact of credential compromise.

---

## Secure Third-Party Dependencies

Verify all external software before use.

Recommended controls:

- Trusted package repositories
- Dependency pinning
- Signature verification
- Continuous vulnerability monitoring
- License validation
- Dependency inventory management

Supply chain security should extend to every external component.

---

## Protect Build Artifacts

Every generated artifact should be:

- Digitally signed
- Integrity verified
- Stored in trusted repositories
- Protected by access controls
- Versioned
- Audited

Artifact integrity ensures software authenticity throughout deployment.

---

## Enforce Policy as Code

Automate security governance using policy engines.

Example policies:

- No critical vulnerabilities permitted
- Encryption required
- Approved base images only
- Signed artifacts mandatory
- Mandatory deployment approvals
- Restricted production access

Policy automation improves consistency and compliance.

---

## Secure Deployment Processes

Production deployments should require:

- Verified artifacts
- Security validation
- Approved change requests
- Deployment approvals
- Rollback procedures
- Deployment audit logs

Controlled releases reduce operational and security risks.

---

## Continuously Monitor the Pipeline

Monitor for:

- Unauthorized repository access
- Suspicious build activity
- Artifact tampering
- Privilege escalation
- Secrets exposure
- Pipeline configuration changes
- Unusual deployment behavior

Continuous monitoring enables rapid detection and response.

---

## Best Practices

### 1. Adopt a Shift-Left Security Strategy

Integrate security as early as possible within the development lifecycle.

Early validation reduces remediation costs and shortens feedback cycles.

---

### 2. Secure Every Pipeline Stage

Every stage should include appropriate security controls.

Protect:

- Source repositories
- Build environments
- Dependencies
- Containers
- Infrastructure
- Deployment processes
- Production workloads

End-to-end security minimizes attack opportunities.

---

### 3. Automate Security Validation

Security testing should execute automatically for every code change.

Recommended automated checks include:

- SAST
- SCA
- Secrets scanning
- IaC scanning
- Container scanning
- Policy evaluation

Automation improves consistency and scalability.

---

### 4. Use Immutable Build Environments

Prefer short-lived, disposable build runners.

Benefits include:

- Reduced persistence
- Consistent builds
- Lower attack surface
- Simplified maintenance

Immutable infrastructure strengthens build security.

---

### 5. Protect the Software Supply Chain

Secure:

- Source code
- Dependencies
- Build systems
- Artifacts
- Deployment mechanisms

Supply chain protection reduces the risk of malicious software distribution.

---

### 6. Apply Least Privilege Everywhere

Restrict permissions for:

- Developers
- Build runners
- Service accounts
- Deployment systems
- Production environments

Excessive permissions should be removed promptly.

---

### 7. Continuously Verify Artifact Integrity

Ensure every artifact is:

- Signed
- Verified
- Traceable
- Stored securely
- Protected against unauthorized modification

Artifact integrity is fundamental to trustworthy deployments.

---

### 8. Integrate with Security Operations

CI/CD Security should work closely with:

- DevSecOps teams
- Security Operations Centers (SOC)
- Incident Response teams
- Vulnerability Management teams
- Cloud Security teams
- Governance, Risk, and Compliance (GRC) teams

Cross-functional collaboration improves organizational resilience.

---

### 9. Measure Security Performance

Track metrics such as:

- Pipeline success rate
- Security scan coverage
- Mean Time to Detect (MTTD)
- Mean Time to Remediate (MTTR)
- Critical vulnerability count
- Secrets detected
- Artifact verification rate
- Deployment failure rate

Metrics support continuous improvement.

---

### 10. Continuously Improve the Pipeline

Regularly:

- Update security tools
- Patch build environments
- Review access permissions
- Improve policies
- Enhance pipeline automation
- Conduct security exercises

Continuous improvement helps pipelines adapt to evolving threats and technologies.

---

## Common Mistakes

CI/CD pipelines are among the most privileged systems in modern cloud environments. A single security weakness can allow attackers to compromise source code, inject malicious software, steal secrets, or gain access to production infrastructure.

Many organizations automate software delivery successfully but overlook critical security controls. The following are the most common CI/CD security mistakes and how they impact organizational security.

---

### 1. Hardcoding Secrets in Pipelines

One of the most common mistakes is storing secrets directly inside:

- Source code
- Pipeline configuration files
- Environment variables
- Shell scripts
- Dockerfiles
- Infrastructure templates

Examples include:

- Cloud access keys
- Database passwords
- API keys
- SSH private keys
- OAuth tokens
- Encryption keys

```
Developer

     │

     ▼

Pipeline Configuration

     │

     ▼

Hardcoded Secret

     │

     ▼

Credential Exposure

     │

     ▼

Cloud Compromise
```

Secrets should always be managed through dedicated secrets management systems.

---

### 2. Excessive Pipeline Permissions

CI/CD pipelines frequently operate with administrator privileges.

Common issues include:

- Administrator service accounts
- Wildcard IAM permissions
- Shared deployment accounts
- Broad cloud access
- Long-lived credentials

Pipelines should receive only the permissions required to complete specific tasks.

---

### 3. Skipping Security Scanning

Some organizations prioritize deployment speed over security validation.

Missing security checks may include:

- Static Application Security Testing (SAST)
- Software Composition Analysis (SCA)
- Secrets scanning
- Container image scanning
- Infrastructure as Code (IaC) scanning
- Policy validation

Skipping automated security testing allows vulnerabilities to reach production.

---

### 4. Using Untrusted Third-Party Dependencies

Modern software depends heavily on external packages and libraries.

Risks include:

- Vulnerable packages
- Malicious dependencies
- Abandoned projects
- License violations
- Supply chain attacks

Dependencies should be continuously monitored and verified.

---

### 5. Weak Repository Protection

Source code repositories without proper protections are attractive attack targets.

Common weaknesses include:

- Direct commits to production branches
- Disabled branch protection
- Missing peer reviews
- Weak authentication
- Excessive repository permissions

Repository security forms the foundation of CI/CD security.

---

### 6. Ignoring Artifact Integrity

Unsigned or unverified build artifacts may be modified after compilation.

Risks include:

- Artifact tampering
- Malicious binary replacement
- Supply chain compromise
- Unauthorized software distribution

Artifacts should always be digitally signed and verified before deployment.

---

### 7. Insecure Build Environments

Long-lived build servers often accumulate:

- Outdated software
- Cached credentials
- Sensitive artifacts
- Unpatched vulnerabilities
- Unnecessary services

Organizations should prefer isolated, ephemeral build runners.

---

### 8. Weak Identity Management

Poor identity management increases the risk of unauthorized pipeline access.

Examples include:

- Shared administrator accounts
- Missing Multi-Factor Authentication (MFA)
- Unused privileged accounts
- Long-lived service credentials
- Infrequent permission reviews

Identity governance should extend across all CI/CD systems.

---

### 9. Bypassing Deployment Controls

Manual deployments outside approved pipelines bypass important security mechanisms such as:

- Automated testing
- Policy validation
- Audit logging
- Deployment approvals
- Artifact verification

Production deployments should occur exclusively through controlled CI/CD pipelines.

---

### 10. Ignoring Runtime Security

Pre-deployment validation alone cannot detect every threat.

Organizations should continue monitoring for:

- Runtime attacks
- Unauthorized configuration changes
- Privilege escalation
- Suspicious application behavior
- Unexpected network communication

Runtime monitoring complements pipeline security.

---

### 11. Poor Logging and Audit Trails

Insufficient logging limits visibility into security events.

Important events to record include:

- Repository access
- Pipeline executions
- Build failures
- Deployment approvals
- Administrative actions
- Artifact downloads
- Configuration changes

Comprehensive audit logs support investigations and compliance.

---

### 12. Lack of Pipeline Segmentation

Using a single pipeline for all environments increases operational risk.

Separate pipelines or stages should exist for:

- Development
- Testing
- Staging
- Production

Environment isolation limits the impact of failures and compromises.

---

### 13. Ignoring Compliance Validation

Pipelines that do not enforce organizational policies may deploy non-compliant resources.

Examples include:

- Missing encryption
- Weak IAM policies
- Unapproved deployment regions
- Missing resource tags
- Disabled logging

Compliance validation should execute automatically before deployment.

---

### 14. Treating CI/CD Security as a One-Time Setup

Security controls require continuous maintenance.

Regular activities include:

- Updating security tools
- Reviewing IAM permissions
- Rotating credentials
- Updating policies
- Patching build environments
- Reviewing dependency inventories

Continuous improvement keeps pipelines resilient against evolving threats.

---

### 15. Viewing CI/CD Security as Solely a DevOps Responsibility

CI/CD Security requires collaboration across multiple teams.

Key stakeholders include:

- Developers
- DevOps engineers
- DevSecOps engineers
- Security Operations Center (SOC)
- Cloud Security teams
- Platform engineers
- Governance, Risk, and Compliance (GRC) teams
- Incident Response teams

Shared responsibility strengthens software delivery security.

---

## CI/CD Security Checklist

| Control | Status |
|---------|--------|
| Multi-Factor Authentication (MFA) Enabled | ✓ |
| Branch Protection Configured | ✓ |
| Mandatory Pull Request Reviews | ✓ |
| Least Privilege IAM Implemented | ✓ |
| Secrets Stored Securely | ✓ |
| SAST Integrated into Pipeline | ✓ |
| Software Composition Analysis (SCA) Enabled | ✓ |
| Infrastructure as Code (IaC) Scanning Enabled | ✓ |
| Container Image Scanning Automated | ✓ |
| Policy as Code Implemented | ✓ |
| Artifact Signing Enabled | ✓ |
| Artifact Integrity Verification Performed | ✓ |
| Secure Build Runners Used | ✓ |
| Continuous Monitoring Enabled | ✓ |
| Regular Security Reviews Conducted | ✓ |

---

## References

### International Standards

- ISO/IEC 27001 — Information Security Management Systems (ISMS)
- ISO/IEC 27002 — Information Security Controls
- ISO/IEC 27034 — Application Security
- ISO/IEC 29147 — Vulnerability Disclosure
- ISO/IEC 5230 (OpenChain) — Open Source License Compliance

---

### NIST Publications

- NIST Secure Software Development Framework (SSDF) SP 800-218
- NIST Cybersecurity Framework (CSF) 2.0
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls
- NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management
- NIST SP 800-204 Series — Microservices Security

---

### OWASP Resources

- OWASP Top 10
- OWASP CI/CD Security Guidance
- OWASP Software Assurance Maturity Model (SAMM)
- OWASP Application Security Verification Standard (ASVS)
- OWASP Cheat Sheet Series

---

### Supply Chain Security

- SLSA (Supply-chain Levels for Software Artifacts)
- in-toto Framework
- Sigstore
- SPDX Specification
- CycloneDX Specification
- Software Bill of Materials (SBOM)

---

### Cloud-Native Security

- Cloud Native Computing Foundation (CNCF) Software Supply Chain Best Practices
- Kubernetes Security Best Practices
- Open Policy Agent (OPA)
- SPIFFE and SPIRE

---

### Cloud Provider Documentation

#### Amazon Web Services (AWS)

- AWS CodePipeline
- AWS CodeBuild
- AWS CodeDeploy
- AWS CodeArtifact
- AWS Inspector
- AWS Security Hub

#### Microsoft Azure

- Azure DevOps
- Azure Pipelines
- Azure Artifacts
- Microsoft Defender for Cloud
- Azure Policy

#### Google Cloud Platform (GCP)

- Cloud Build
- Artifact Registry
- Binary Authorization
- Security Command Center
- Cloud Deploy

---

### Recommended Learning Resources

- NIST Computer Security Resource Center (CSRC)
- Cloud Security Alliance (CSA) Research
- CIS Benchmarks
- Official AWS, Microsoft Azure, Google Cloud, GitHub Actions, GitLab CI/CD, Jenkins, and CNCF documentation

---

**End of Chapter 35 – CI/CD Security**


---