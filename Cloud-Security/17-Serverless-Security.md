# Serverless Security

## Overview

Serverless Security is the practice of protecting serverless applications, functions, APIs, event sources, identities, data, and cloud services throughout their entire lifecycle.

Serverless computing allows developers to build and deploy applications without managing servers or underlying infrastructure. Cloud providers automatically handle infrastructure provisioning, scaling, operating system maintenance, and availability, enabling developers to focus solely on application logic.

Although infrastructure management is delegated to the cloud provider, customers remain responsible for securing:

- Application code
- Function configuration
- Identity and Access Management (IAM)
- APIs
- Secrets
- Event sources
- Dependencies
- Data
- Monitoring
- Compliance

Serverless applications are highly event-driven and commonly integrate with multiple cloud services, making identity management, permission control, and secure application design essential.

Popular serverless platforms include:

- AWS Lambda
- Azure Functions
- Google Cloud Functions
- Google Cloud Run
- Oracle Cloud Functions
- IBM Cloud Functions
- Cloudflare Workers

Serverless Security focuses on reducing risks associated with:

- Over-privileged functions
- Vulnerable dependencies
- Event injection
- API abuse
- Secret exposure
- Insecure configurations
- Supply chain attacks
- Data leakage
- Misconfigured permissions

Effective security requires a combination of secure development practices, cloud-native security controls, continuous monitoring, and automated policy enforcement.

---

## Why It Matters

Serverless computing powers many modern applications, including:

- REST APIs
- Mobile backends
- Authentication systems
- Payment processing
- AI/ML inference
- Event processing
- IoT platforms
- Data transformation pipelines
- File processing
- Business automation

Because serverless functions often process sensitive information and interact with numerous cloud services, they present attractive targets for attackers.

A compromised function may allow attackers to:

- Access sensitive data
- Abuse cloud resources
- Escalate privileges
- Invoke internal services
- Execute malicious code
- Steal credentials
- Modify business logic
- Exfiltrate information

Poor serverless security may result in:

- Financial loss
- Service disruption
- Compliance violations
- Data breaches
- Reputation damage
- Cloud account compromise

Strong Serverless Security helps organizations:

- Secure cloud-native applications
- Reduce operational risk
- Improve application resilience
- Protect sensitive workloads
- Enable secure automation
- Strengthen DevSecOps
- Meet regulatory requirements
- Improve incident detection and response

Security should be embedded into every stage of the serverless application lifecycle.

---

## Architecture

A secure serverless architecture consists of multiple interconnected security layers protecting requests, identities, functions, data, and cloud services.

```
                 Client / Application

                         │

                         ▼

                    API Gateway

                         │

                         ▼

              Identity Authentication

                         │

                         ▼

               Authorization (IAM)

                         │

                         ▼

              Serverless Function

                         │

       ┌─────────────────┼─────────────────┐

       ▼                 ▼                 ▼

   Secrets          Cloud Storage      Database

       │                 │                 │

       └─────────────────┼─────────────────┘

                         ▼

              Logging • Monitoring

                         ▼

                    SIEM / SOC
```

Each layer should enforce authentication, authorization, encryption, monitoring, and least-privilege access.

---

## Key Concepts

### Serverless Function

A serverless function is a small, stateless unit of code that executes in response to an event.

Examples include:

- HTTP requests
- File uploads
- Database changes
- Queue messages
- Scheduled tasks
- IoT events

```
Event

↓

Function

↓

Response
```

Functions should remain lightweight, modular, and secure.

---

### Event-Driven Execution

Unlike traditional applications, serverless workloads execute only when triggered by specific events.

Common event sources include:

- API Gateway
- Object storage
- Message queues
- Event buses
- Databases
- Scheduled timers

```
Event

↓

Trigger

↓

Function Execution
```

Every event source should be validated and authenticated where applicable.

---

### API Gateway

The API Gateway serves as the entry point for HTTP-based serverless applications.

Responsibilities include:

- Authentication
- Authorization
- Rate limiting
- Request validation
- Logging
- Routing

A properly configured API Gateway significantly reduces the attack surface.

---

### Identity and Access Management (IAM)

IAM controls which identities can invoke functions and access cloud resources.

Permissions should be granted using the Principle of Least Privilege.

```
User / Service

↓

IAM Policy

↓

Function Access
```

Avoid broad wildcard permissions whenever possible.

---

### Execution Role

Every serverless function executes using an identity (execution role or service identity).

The execution role determines what the function can access.

Examples:

- Storage buckets
- Databases
- Message queues
- Secrets
- Logging services

Restrict execution roles to only the permissions required.

---

### Stateless Computing

Serverless functions are designed to be stateless.

This means:

- No persistent local storage
- No long-running sessions
- No reliance on previous executions

Persistent data should be stored in managed storage services.

---

### Cold Start

A cold start occurs when the cloud provider initializes a new execution environment for a function.

Although primarily a performance concern, secure initialization is important to ensure:

- Proper secret retrieval
- Secure configuration loading
- Correct identity assignment

---

### Function Timeout

Functions should have reasonable execution time limits.

Benefits include:

- Reduced abuse
- Controlled resource usage
- Lower denial-of-service risk
- Improved cost management

Long-running functions increase operational and security risk.

---

### Secrets Management

Serverless functions frequently require:

- API keys
- Database credentials
- Encryption keys
- OAuth tokens
- Certificates

Secrets should be retrieved securely from dedicated secrets management services rather than embedded in source code or configuration files.

---

### Dependency Management

Serverless applications commonly rely on third-party libraries.

Dependencies should be:

- Regularly updated
- Vulnerability scanned
- Verified for integrity
- Limited to necessary packages

Outdated dependencies are a common source of compromise.

---

### Logging

Every function execution should generate appropriate logs.

Useful log information includes:

- Invocation time
- Request identifiers
- Errors
- Authentication events
- Authorization failures
- Execution duration

Sensitive information should never be logged.

---

### Monitoring

Continuous monitoring provides visibility into:

- Function invocations
- Errors
- Latency
- Resource usage
- Failed authentication
- Unexpected execution patterns

Monitoring supports rapid threat detection and operational reliability.

---

### Encryption

Protect sensitive data by enabling encryption:

- In transit
- At rest
- During backup

Encryption should also be applied to secrets, storage, and databases associated with serverless workloads.

---

### Least Privilege

Every serverless function should receive only the permissions necessary to perform its intended task.

```
Function

↓

Minimal IAM Role

↓

Required Resources
```

Limiting permissions reduces the impact of compromised functions.

---

### Software Supply Chain Security

Protect the development pipeline by ensuring:

- Trusted package repositories
- Signed artifacts
- Vulnerability scanning
- Dependency verification
- Secure CI/CD pipelines

Software supply chain security is essential for modern serverless applications.

---

## How It Works

Serverless Security protects applications by securing every stage of the function lifecycle—from development and deployment to execution, monitoring, and retirement. Unlike traditional infrastructure, security focuses less on operating systems and more on identities, permissions, code, APIs, event sources, and cloud service interactions.

Every serverless request should pass through multiple security controls before business logic is executed.

A secure serverless workflow generally includes:

1. Authenticate the caller
2. Authorize access
3. Validate the request
4. Invoke the function
5. Securely retrieve secrets
6. Access cloud resources using least privilege
7. Log execution
8. Continuously monitor behavior

This layered approach helps prevent unauthorized access, privilege escalation, and abuse of cloud resources.

---

## Serverless Security Workflow

```
               User / Application

                        │

                        ▼

                 Authentication

                        │

                        ▼

                 Authorization

                        │

                        ▼

                  API Gateway

                        │

                        ▼

              Serverless Function

                        │

        ┌───────────────┼───────────────┐

        ▼               ▼               ▼

   Secrets Manager   Database      Object Storage

        │               │               │

        └───────────────┼───────────────┘

                        ▼

            Logging • Monitoring • SIEM
```

Each request is evaluated before sensitive resources are accessed.

---

## Step 1 – Receive the Event

A serverless function begins execution only after receiving an event.

Common triggers include:

- HTTP requests
- File uploads
- Queue messages
- Database updates
- Scheduled jobs
- Event bus notifications

```
Event

↓

Trigger

↓

Function
```

All incoming events should be validated before processing.

---

## Step 2 – Authenticate the Caller

Authentication verifies the identity of the user, application, or service initiating the request.

Authentication methods include:

- OAuth
- OpenID Connect (OIDC)
- Cloud IAM
- API Keys
- JWT Tokens

```
Client

↓

Authentication

↓

Verified Identity
```

Unauthenticated requests should be rejected immediately.

---

## Step 3 – Authorize the Request

After authentication, authorization determines whether the caller may invoke the function.

```
Identity

↓

IAM Policy

↓

Allowed?

↓

Yes / No
```

Authorization should enforce least-privilege access.

---

## Step 4 – Validate the Request

Before business logic executes, the application should validate:

- Input format
- Content type
- Request size
- Required fields
- Allowed values

Input validation reduces risks such as:

- Injection attacks
- Malformed requests
- Resource exhaustion
- Unexpected application behavior

---

## Step 5 – Execute the Function

Once validated, the serverless platform initializes the execution environment and runs the function.

```
Cloud Platform

↓

Execution Environment

↓

Application Code
```

The function should execute only the code necessary to complete its task.

---

## Step 6 – Retrieve Secrets Securely

Applications often require credentials during execution.

Instead of embedding them into source code:

```
Function

↓

Secrets Manager

↓

Authorized Secret

↓

Application
```

Secrets should be:

- Encrypted
- Rotated regularly
- Retrieved only when required

---

## Step 7 – Access Cloud Resources

The function may interact with:

- Databases
- Storage
- Message queues
- Notification services
- APIs

```
Function

↓

IAM Role

↓

Cloud Resource
```

Access should be limited to only the required resources.

---

## Step 8 – Generate Logs

Every invocation should produce logs that include:

- Timestamp
- Request identifier
- Execution duration
- Success or failure
- Errors
- Security events

Avoid logging:

- Passwords
- Tokens
- API keys
- Personally Identifiable Information (PII)

---

## Step 9 – Monitor Runtime Behavior

Continuous monitoring detects unusual activity such as:

- Excessive invocations
- Unexpected outbound connections
- Repeated authentication failures
- Permission errors
- Long-running executions

```
Function

↓

Monitoring

↓

Threat Detection
```

Behavioral monitoring provides visibility into attacks that bypass preventive controls.

---

## Step 10 – Send Security Events to SIEM

Security-relevant events should be centralized for analysis.

```
Cloud Logs

↓

SIEM

↓

Correlation

↓

SOC Investigation
```

Centralized logging improves incident response and compliance reporting.

---

## Serverless Application Lifecycle

```
Develop

↓

Code Review

↓

Dependency Scan

↓

Build

↓

Deploy

↓

Invoke

↓

Monitor

↓

Update

↓

Retire
```

Security checks should be integrated into every phase of the lifecycle.

---

## Secure Invocation Flow

```
Client

↓

Authentication

↓

Authorization

↓

API Gateway

↓

Function

↓

Database

↓

Response
```

Only authenticated and authorized requests should reach application logic.

---

## Secrets Access Workflow

```
Function Starts

↓

Request Secret

↓

Secrets Manager

↓

Authorized Retrieval

↓

Continue Execution
```

Secrets should never be stored permanently within the execution environment.

---

## Practical Example

### Example 1 – Secure File Processing

A user uploads a document to cloud storage.

```
File Upload

↓

Storage Event

↓

Serverless Function

↓

Virus Scan

↓

Store Metadata
```

Security controls include:

- IAM permissions
- Input validation
- Malware scanning
- Logging

---

### Example 2 – Payment API

A payment API invokes a serverless function.

```
Client

↓

JWT Authentication

↓

API Gateway

↓

Payment Function

↓

Database
```

Only authenticated users may process transactions.

---

### Example 3 – Secure Secret Retrieval

A reporting function requires database credentials.

```
Function

↓

Secrets Manager

↓

Temporary Credential

↓

Database Connection
```

No credentials are embedded in source code.

---

### Example 4 – Blocking Unauthorized Invocation

An attacker attempts to invoke an administrative function.

```
Unauthorized Request

↓

IAM Evaluation

↓

Access Denied
```

Least-privilege IAM policies prevent unauthorized execution.

---

### Example 5 – Dependency Vulnerability Detection

A CI/CD pipeline detects a vulnerable third-party package before deployment.

```
Dependency Scan

↓

Known CVE

↓

Deployment Blocked
```

Preventive scanning reduces software supply chain risk.

---

## Serverless Security Components

| Component | Purpose |
|-----------|---------|
| API Gateway | Secure request entry point |
| IAM | Authentication and authorization |
| Serverless Function | Executes business logic |
| Secrets Manager | Secure credential storage |
| Cloud Storage | Persistent object storage |
| Database | Persistent application data |
| Monitoring | Performance and security visibility |
| Logging | Audit and forensic records |
| SIEM | Centralized security analytics |
| CI/CD Pipeline | Automated secure deployment |

---

## Indicators of Serverless Compromise (Detection)

Continuous monitoring is essential because serverless functions are short-lived, event-driven, and automatically scaled.

---

### Excessive Function Invocations

A sudden increase in invocation frequency may indicate:

- Denial-of-Service (DoS)
- Credential abuse
- Automated attacks
- Event flooding

```
Unexpected Traffic

↓

Function Invocations

↓

Security Alert
```

---

### Unusual IAM Activity

Monitor for:

- Unexpected role changes
- Permission escalation
- New execution roles
- Unauthorized policy modifications

Identity abuse is a common attack vector in serverless environments.

---

### Unauthorized Secret Access

Unexpected retrieval of secrets may indicate:

- Compromised functions
- Stolen credentials
- Insider threats
- Malicious automation

All secret access should be logged and reviewed.

---

### Unexpected Outbound Connections

Serverless functions rarely require unrestricted internet access.

Unexpected outbound traffic may indicate:

- Data exfiltration
- Command-and-control communication
- Malware
- Cryptomining

Restrict outbound connectivity whenever possible.

---

### Function Configuration Changes

Monitor changes to:

- Environment variables
- Memory allocation
- Timeout settings
- Execution roles
- Trigger configuration

Unauthorized modifications may introduce security risks.

---

### Dependency Integrity Violations

Detect:

- Unsigned packages
- Unexpected dependency updates
- Vulnerable libraries
- Failed integrity verification

Supply chain attacks often target application dependencies.

---

### Authentication Failures

Repeated failed authentication attempts may indicate:

- Credential stuffing
- Brute-force attacks
- Misconfigured clients

Investigate unusual authentication patterns promptly.

---

### API Abuse

Monitor for:

- Excessive requests
- Invalid parameters
- Repeated authorization failures
- Rate-limit violations

API monitoring helps identify abuse before service availability is affected.

---

### Logging and Audit Monitoring

Continuously analyze:

- Invocation logs
- IAM events
- Secret access
- Configuration changes
- API Gateway logs
- Storage access
- Database activity
- Deployment events

Forward logs to the organization's SIEM for correlation and alerting.

---

## Detection Best Practices

- Enable detailed function logging.
- Monitor IAM role and policy changes.
- Alert on excessive invocation rates.
- Audit secret retrieval events.
- Validate dependency integrity before deployment.
- Monitor outbound network activity.
- Analyze API Gateway access logs.
- Forward serverless logs to the SIEM.
- Establish behavioral baselines for normal function execution.
- Continuously review cloud audit logs for suspicious activity.

---

## Prevention

Preventing attacks against serverless applications requires securing identities, application code, event sources, APIs, dependencies, secrets, and cloud resources. Since the underlying infrastructure is managed by the cloud provider, organizations must focus on securing everything they build, configure, and deploy.

A strong Serverless Security strategy should protect:

- Application code
- Serverless functions
- APIs
- Event sources
- IAM identities
- Execution roles
- Secrets
- Dependencies
- Databases
- Storage
- Logging
- Monitoring

Security should be incorporated into the Software Development Life Cycle (SDLC), CI/CD pipelines, and cloud governance processes.

---

# Defense-in-Depth for Serverless

```
                Users / Applications

                        │

                        ▼

                Authentication

                        │

                        ▼

                Authorization

                        │

                        ▼

                  API Gateway

                        │

                        ▼

              Serverless Function

                        │

        ┌───────────────┼───────────────┐

        ▼               ▼               ▼

   Secrets Manager   Databases     Cloud Storage

                        │

                        ▼

           Monitoring • Logging • SIEM

                        │

                        ▼

             Incident Response Team
```

Each security layer reduces the likelihood of unauthorized access and limits the impact of a successful attack.

---

# Enforce Least-Privilege IAM

Every serverless function should execute using a dedicated identity with only the permissions required for its specific task.

Recommendations:

- Create separate execution roles
- Avoid wildcard permissions
- Restrict access to required resources
- Review IAM policies regularly
- Remove unused identities

```
Function

↓

Minimal IAM Role

↓

Required Resources
```

Least Privilege significantly reduces the blast radius of compromised functions.

---

# Protect APIs

Most serverless applications expose functionality through APIs.

Secure APIs by enabling:

- Authentication
- Authorization
- TLS encryption
- Input validation
- Rate limiting
- Request throttling
- Web Application Firewall (WAF) integration

Proper API protection prevents abuse and unauthorized access.

---

# Validate Every Input

Never trust incoming data.

Validate:

- Request format
- File type
- Input length
- Allowed characters
- Required parameters

Input validation helps prevent:

- Injection attacks
- Malformed requests
- Resource exhaustion
- Logic manipulation

---

# Secure Secrets

Credentials should never be embedded in:

- Source code
- Environment variables (unless securely managed)
- Git repositories
- Configuration files

Use dedicated secrets management services.

```
Function

↓

Secrets Manager

↓

Temporary Secret

↓

Application
```

Rotate secrets regularly and audit all access.

---

# Secure Dependencies

Third-party libraries are a major attack surface.

Recommendations:

- Use trusted repositories
- Remove unused packages
- Scan dependencies for vulnerabilities
- Verify package integrity
- Update libraries regularly

Supply chain security should be part of every deployment.

---

# Encrypt Sensitive Data

Enable encryption:

- In transit
- At rest
- During backup

Encrypt:

- Databases
- Object storage
- Secrets
- Logs containing sensitive metadata

Protect encryption keys using an appropriate Key Management Service (KMS).

---

# Secure Event Sources

Event sources should be authenticated and authorized where possible.

Examples include:

- API Gateway
- Message queues
- Event buses
- Storage events
- Database triggers

Validate that only trusted services can trigger sensitive functions.

---

# Limit Function Permissions

Functions should access only the cloud services necessary for business operations.

Avoid granting permissions such as:

- Full storage access
- Administrative database permissions
- Broad IAM management
- Unrestricted network access

Permission reviews should be part of routine security assessments.

---

# Implement Logging and Monitoring

Enable centralized monitoring for:

- Function invocations
- Authentication events
- Authorization failures
- Secret access
- Configuration changes
- Runtime errors
- API activity

```
Cloud Logs

↓

SIEM

↓

Correlation

↓

Security Alert
```

Continuous visibility enables faster detection of attacks.

---

# Protect the CI/CD Pipeline

Serverless security begins before deployment.

Secure the pipeline by implementing:

- Code reviews
- Static Application Security Testing (SAST)
- Dependency scanning
- Secret scanning
- Artifact signing
- Infrastructure validation

Only verified artifacts should be deployed.

---

# Apply Resource Limits

Configure reasonable limits for:

- Execution timeout
- Memory allocation
- Concurrent executions
- Retry behavior

Resource limits reduce the impact of denial-of-service attacks and uncontrolled costs.

---

# Continuously Update Functions

Maintain serverless applications by:

- Updating dependencies
- Removing deprecated APIs
- Applying security patches
- Rebuilding deployment packages

Regular updates reduce exposure to known vulnerabilities.

---

## Best Practices

### 1. Follow the Principle of Least Privilege

Grant each function only the permissions required to complete its intended task.

Review IAM policies periodically.

---

### 2. Authenticate and Authorize Every Request

Require strong authentication before function invocation.

Use modern identity standards such as OAuth 2.0 and OpenID Connect (OIDC) where appropriate.

---

### 3. Protect APIs

Implement:

- TLS
- Rate limiting
- Authentication
- Authorization
- Request validation
- API logging

APIs should never trust unauthenticated clients.

---

### 4. Secure Secrets

Store credentials using managed secrets services.

Rotate secrets frequently and monitor retrieval activity.

---

### 5. Scan Dependencies Continuously

Automatically detect:

- Vulnerable packages
- Malicious dependencies
- Outdated libraries
- License issues

Integrate dependency scanning into CI/CD pipelines.

---

### 6. Encrypt Sensitive Information

Protect:

- Databases
- Object storage
- Backups
- Secrets
- Communication channels

Encryption should be enabled by default whenever supported.

---

### 7. Monitor Every Function Invocation

Monitor:

- Invocation frequency
- Execution duration
- Error rates
- Authentication failures
- Permission denials
- Outbound network activity

Behavioral baselines help identify anomalies.

---

### 8. Enable Comprehensive Logging

Record:

- Function executions
- API requests
- IAM activity
- Secret access
- Configuration changes
- Deployment events

Forward logs to the organization's SIEM for centralized analysis.

---

### 9. Secure the Development Pipeline

Adopt DevSecOps practices by integrating:

- Static code analysis
- Dynamic testing where applicable
- Dependency scanning
- Secret detection
- Automated policy validation

Prevent vulnerabilities from reaching production.

---

### 10. Review Configurations Regularly

Periodically assess:

- IAM roles
- Execution permissions
- API configurations
- Environment variables
- Event triggers
- Monitoring settings

Routine configuration reviews strengthen the overall security posture.

---

## Common Mistakes

Serverless platforms simplify infrastructure management, but they do not eliminate security responsibilities. Most serverless security incidents are caused by insecure application design, excessive permissions, poor secret management, and inadequate monitoring rather than vulnerabilities in the cloud provider's platform.

Recognizing these common mistakes helps organizations strengthen the security of their serverless workloads.

---

### 1. Granting Excessive IAM Permissions

One of the most frequent mistakes is assigning broad permissions to function execution roles.

Examples include:

- Full storage access
- Administrator privileges
- Wildcard (`*`) permissions
- Unrestricted database access

```
Function

↓

Administrator Role

↓

Entire Cloud Environment
```

Every function should receive only the permissions necessary to perform its intended task.

---

### 2. Hardcoding Secrets

Embedding credentials directly into:

- Source code
- Configuration files
- Deployment packages
- Environment variables without protection

creates long-term security risks.

```
API Key

↓

Source Code

↓

Repository

↓

Credential Exposure
```

Use managed secrets services instead of storing credentials within the application.

---

### 3. Trusting User Input

Failing to validate incoming requests may result in:

- Injection attacks
- Logic manipulation
- Resource exhaustion
- Malformed requests
- Unauthorized operations

Every input should be validated before processing.

---

### 4. Ignoring Dependency Security

Serverless applications commonly rely on numerous third-party libraries.

Using outdated or vulnerable dependencies may introduce:

- Known CVEs
- Malware
- Supply chain attacks
- Remote code execution vulnerabilities

Dependencies should be scanned continuously.

---

### 5. Exposing APIs Without Authentication

Public APIs that lack authentication or authorization controls are common attack targets.

Consequences include:

- Unauthorized function execution
- Data exposure
- Service abuse
- Automated attacks

Protect APIs with strong authentication and authorization mechanisms.

---

### 6. Using Shared Execution Roles

Multiple functions sharing the same execution role increases security risk.

Problems include:

- Excessive permissions
- Reduced accountability
- Larger attack surface

Assign dedicated execution roles to individual functions whenever possible.

---

### 7. Logging Sensitive Information

Sensitive data should never appear in logs.

Avoid logging:

- Passwords
- API keys
- OAuth tokens
- Database credentials
- Personally Identifiable Information (PII)

Logs should contain only information necessary for monitoring and troubleshooting.

---

### 8. Ignoring Function Timeouts

Functions without appropriate execution limits may:

- Consume excessive resources
- Increase operational costs
- Be abused during attacks
- Delay failure detection

Configure reasonable timeout values for every function.

---

### 9. Poor Event Source Validation

Not every event should automatically trigger business logic.

Validate:

- Event origin
- Event format
- Event authenticity
- Authorization

Only trusted event sources should invoke sensitive functions.

---

### 10. Insufficient Monitoring

Without continuous monitoring, organizations may fail to detect:

- Excessive invocations
- Credential abuse
- Configuration changes
- Suspicious outbound traffic
- Authentication failures

Visibility is essential for timely threat detection.

---

### 11. Ignoring API Rate Limiting

Unlimited request rates increase the risk of:

- Denial-of-Service (DoS)
- Cost amplification attacks
- Resource exhaustion
- Automated abuse

Implement throttling and rate-limiting controls at the API Gateway.

---

### 12. Leaving Functions Outdated

Running obsolete deployment packages may expose applications to:

- Known vulnerabilities
- Deprecated dependencies
- Unsupported runtimes
- Compatibility issues

Rebuild and redeploy functions regularly using current runtime versions.

---

### 13. Weak CI/CD Security

An insecure deployment pipeline may allow attackers to introduce malicious code or artifacts.

Common issues include:

- Missing code reviews
- No dependency scanning
- Unsigned deployment artifacts
- Inadequate access controls

Secure the software supply chain from development through deployment.

---

### 14. Assuming the Cloud Provider Secures Everything

Under the Shared Responsibility Model, cloud providers secure the underlying infrastructure, while customers remain responsible for:

- Application code
- IAM policies
- Secrets
- APIs
- Dependencies
- Configuration
- Monitoring
- Compliance

Misunderstanding these responsibilities often leads to security gaps.

---

### 15. Treating Serverless as "Set and Forget"

Serverless applications require ongoing maintenance.

Organizations should regularly:

- Update dependencies
- Rotate credentials
- Review IAM policies
- Test security controls
- Monitor logs
- Patch application code

Continuous security is essential for long-term resilience.

---

## Serverless Security Checklist

| Control | Status |
|---------|--------|
| Least-Privilege IAM Applied | ✓ |
| APIs Protected with Authentication | ✓ |
| Secrets Stored Securely | ✓ |
| Dependencies Continuously Scanned | ✓ |
| Input Validation Implemented | ✓ |
| Encryption Enabled | ✓ |
| Logging Configured | ✓ |
| Monitoring Enabled | ✓ |
| API Rate Limiting Configured | ✓ |
| Dedicated Execution Roles | ✓ |
| CI/CD Security Integrated | ✓ |
| Function Timeouts Configured | ✓ |
| Artifact Integrity Verified | ✓ |
| SIEM Integration Enabled | ✓ |
| Regular Security Reviews Performed | ✓ |

---

## References

### Standards

- NIST SP 800-204A – Building Secure Microservices-Based Applications
- NIST SP 800-53 Rev. 5 – Security and Privacy Controls for Information Systems and Organizations
- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001
- ISO/IEC 27002
- CIS Controls v8
- Cloud Security Alliance (CSA) Security Guidance

---

### Serverless Platform Documentation

#### Amazon Web Services

- AWS Lambda Documentation
- AWS Lambda Security Best Practices
- Amazon API Gateway Documentation
- AWS IAM Documentation
- AWS Secrets Manager Documentation

#### Microsoft Azure

- Azure Functions Documentation
- Azure API Management Documentation
- Microsoft Entra ID Documentation
- Azure Key Vault Documentation

#### Google Cloud Platform

- Google Cloud Functions Documentation
- Cloud Run Documentation
- Google Cloud IAM Documentation
- Secret Manager Documentation

#### Oracle Cloud Infrastructure

- Oracle Cloud Functions Documentation

#### IBM Cloud

- IBM Cloud Functions Documentation

#### Cloudflare

- Cloudflare Workers Documentation

---

### Security Frameworks

- Zero Trust Architecture
- Defense in Depth
- Principle of Least Privilege (PoLP)
- DevSecOps
- Secure Software Supply Chain
- Identity and Access Management (IAM)
- Continuous Monitoring
- Vulnerability Management
- Secure Configuration Management

---

### Recommended Learning Resources

- OWASP Serverless Top 10
- OWASP API Security Top 10
- MITRE ATT&CK Framework
- MITRE D3FEND
- Cloud Native Computing Foundation (CNCF) Security Whitepapers
- CIS Benchmarks
- SANS Cloud Security Resources
- Cloud Security Alliance Research Publications

---

**End of Chapter 17 – Serverless Security**

---