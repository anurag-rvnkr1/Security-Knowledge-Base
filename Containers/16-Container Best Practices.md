# Chapter 16 – Container Best Practices

## Overview

Container Best Practices are a collection of proven design principles, operational guidelines, and security recommendations that help organizations build, deploy, operate, and maintain reliable, scalable, secure, and efficient containerized applications.

Following best practices improves:

- Security
- Performance
- Reliability
- Scalability
- Maintainability
- Portability
- Compliance
- Operational efficiency

These practices are derived from years of experience across Docker, Kubernetes, DevOps, DevSecOps, Site Reliability Engineering (SRE), and Cloud Security.

Rather than treating containers as lightweight virtual machines, organizations should embrace cloud-native principles such as immutable infrastructure, automation, observability, and least privilege.

---

# Why It Matters

Poorly designed containers often lead to:

```
Large Images

↓

Slow Deployment

↓

Security Risks

↓

Operational Problems

↓

Higher Costs
```

Whereas well-designed containers provide:

```
Small Images

↓

Fast Deployment

↓

Improved Security

↓

Easy Scaling

↓

Reliable Operations
```

Best practices reduce technical debt while improving application resilience.

---

# Container Best Practice Categories

Container best practices span multiple areas.

```
Application Design

        │

Dockerfile

        │

Image Security

        │

Runtime Security

        │

Networking

        │

Storage

        │

Monitoring

        │

CI/CD

        │

Operations
```

Each area contributes to the overall health of the container ecosystem.

---

# 1. Build Small Images

Smaller images offer multiple benefits.

```
Small Image

↓

Faster Build

↓

Faster Pull

↓

Less Storage

↓

Smaller Attack Surface
```

Benefits include:

- Reduced download time
- Faster deployments
- Lower bandwidth usage
- Fewer installed packages
- Reduced vulnerability exposure

Choose minimal base images whenever practical.

---

# 2. Use Trusted Base Images

Always begin with:

- Official images
- Verified publishers
- Enterprise-approved base images

Avoid downloading random images from untrusted sources.

```
Trusted Base Image

↓

Secure Build

↓

Production
```

---

# 3. Run as a Non-Root User

Avoid:

```dockerfile
USER root
```

Prefer:

```dockerfile
RUN useradd appuser

USER appuser
```

Benefits:

- Reduced privileges
- Smaller attack surface
- Better compliance
- Improved isolation

---

# 4. Keep Images Updated

Regularly rebuild images using:

- Updated base images
- Updated operating system packages
- Updated dependencies

Do not rely on images built months or years ago.

---

# 5. One Process Per Container

Containers should typically have one primary responsibility.

Example:

```
Web Server

↓

One Container


Database

↓

Another Container


Redis

↓

Another Container
```

This improves:

- Scalability
- Fault isolation
- Simplicity
- Maintenance

Some specialized workloads may legitimately run multiple tightly related processes, but the general recommendation is to keep containers focused.

---

# 6. Avoid Hardcoding Secrets

Never include:

- Passwords
- API keys
- Access tokens
- Certificates
- Private keys

inside:

- Dockerfiles
- Source code
- Container images

Use dedicated secret management mechanisms instead.

---

# 7. Use Immutable Infrastructure

Instead of:

```
Running Container

↓

Install Updates

↓

Continue
```

Use:

```
Update Image

↓

Build

↓

Deploy New Container

↓

Remove Old Container
```

Immutable deployments improve consistency and simplify rollback.

---

# 8. Limit Container Resources

Define resource limits.

Examples:

- CPU
- Memory
- Storage
- Process limits

Resource controls improve stability and reduce the impact of resource exhaustion.

---

# 9. Use Health Checks

Applications should expose health information.

```
Healthy

↓

Serve Traffic


Unhealthy

↓

Restart

or

Stop Receiving Traffic
```

Health checks improve availability and orchestration decisions.

---

# 10. Use Read-Only Filesystems Where Appropriate

Applications that do not require filesystem writes should use read-only filesystems.

Benefits:

- Reduced attack surface
- Protection against unauthorized modification
- Better security posture

Writable data can be stored in dedicated volumes or temporary storage where required.

---

# 11. Centralize Logging

Avoid storing logs only inside containers.

```
Containers

↓

Log Collector

↓

Central Storage

↓

Search

↓

Analysis
```

Centralized logging supports troubleshooting, compliance, and incident response.

---

# 12. Monitor Everything

Monitor:

- CPU
- Memory
- Network
- Disk
- Container restarts
- Application metrics
- Security events

Monitoring enables proactive detection of operational and security issues.

---

# 13. Automate CI/CD

Automate:

```
Build

↓

Test

↓

Scan

↓

Deploy
```

Automation improves consistency and reduces manual errors.

---

# 14. Scan Images Continuously

Image scanning should occur:

- During development
- During CI/CD
- Before deployment
- Periodically after deployment

New vulnerabilities continue to emerge even in existing images.

---

# 15. Document Everything

Maintain documentation for:

- Dockerfiles
- Compose files
- Deployment procedures
- Recovery procedures
- Monitoring
- Security controls
- Incident response

Good documentation improves maintainability and operational readiness.

---

# Container Best Practices Lifecycle

```
Design

↓

Build

↓

Test

↓

Scan

↓

Deploy

↓

Monitor

↓

Improve
```

Best practices apply throughout the software lifecycle.

---

# Key Principles

## Security by Default

Build secure configurations from the beginning rather than adding security later.

---

## Automation

Automate repetitive tasks to improve consistency and reduce human error.

---

## Observability

Implement metrics, logs, traces, dashboards, and alerts to maintain visibility.

---

## Least Privilege

Grant only the permissions required by users, containers, and applications.

---

## Immutable Infrastructure

Replace containers with newly built images rather than modifying running workloads.

---

## Continuous Improvement

Regularly review architectures, processes, monitoring, and security controls to adapt to evolving requirements and threats.

---

## How It Works

Container Best Practices are applied throughout the Software Development Life Cycle (SDLC), ensuring that security, reliability, performance, and maintainability are considered from development through production. Rather than being a single configuration or tool, best practices represent a collection of engineering decisions that improve the overall quality of containerized applications.

A mature container platform continuously applies these practices during:

- Development
- Image Build
- Security Validation
- Testing
- Deployment
- Runtime Operations
- Monitoring
- Incident Response

Organizations that integrate these practices into their workflows achieve greater consistency, stronger security, and improved operational resilience.

---

# Container Best Practices Workflow

```
Application Development

        │

        ▼

Dockerfile

        │

        ▼

Build Image

        │

        ▼

Security Scan

        │

        ▼

Testing

        │

        ▼

Push Registry

        │

        ▼

Deployment

        │

        ▼

Monitoring

        │

        ▼

Continuous Improvement
```

Every stage contributes to building a secure and reliable container ecosystem.

---

# Step 1 – Design the Application

Good containerization begins during application design.

Recommended architecture:

```
Frontend

↓

Backend API

↓

Database

↓

Cache

↓

Message Queue
```

Each service should have a clearly defined responsibility.

Benefits:

- Independent scaling
- Easier maintenance
- Better fault isolation
- Simpler deployments

---

# Step 2 – Create a Secure Dockerfile

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

CMD ["python", "app.py"]
```

Good practices demonstrated:

- Minimal base image
- Defined working directory
- No package cache retained
- Non-root execution
- Single application entry point

---

# Step 3 – Build the Image

```
Dockerfile

↓

docker build

↓

Container Image
```

The image becomes the deployable artifact used throughout all environments.

Build once and promote the same image through testing and production.

---

# Step 4 – Scan the Image

Before deployment:

```
Image

↓

Security Scanner

↓

Vulnerabilities

↓

Fix

↓

Rebuild
```

Scanning should identify:

- Known CVEs
- Misconfigurations
- Exposed secrets (tool-dependent)
- Outdated dependencies
- Policy violations

---

# Step 5 – Run Automated Tests

CI/CD pipeline:

```
Image

↓

Unit Tests

↓

Integration Tests

↓

Security Tests

↓

Pass

↓

Deploy
```

Testing before deployment reduces operational risk.

---

# Step 6 – Push to Registry

After validation:

```
Image

↓

Registry

↓

Versioned Tag

↓

Production Ready
```

Registry benefits:

- Version control
- Image sharing
- Rollback capability
- Deployment consistency

---

# Step 7 – Deploy Containers

Deploy using:

```
Docker

↓

Docker Compose

↓

Kubernetes

↓

Cloud Platform
```

The same validated image should be deployed across all environments.

---

# Step 8 – Configure Runtime Security

Production containers should use:

```
Non-root User

↓

Resource Limits

↓

Read-only Filesystem

↓

Minimal Capabilities

↓

Private Networking
```

These controls reduce attack surface and improve stability.

---

# Step 9 – Monitor Production

Observe:

```
CPU

↓

Memory

↓

Logs

↓

Errors

↓

Latency

↓

Security Alerts
```

Monitoring provides early detection of:

- Performance degradation
- Application failures
- Resource exhaustion
- Security incidents

---

# Step 10 – Continuous Improvement

Production feedback drives future improvements.

```
Monitoring

↓

Incident Review

↓

Optimization

↓

Rebuild

↓

Redeploy
```

Container best practices evolve continuously as applications and threats change.

---

# Production Architecture Example

```
                    Internet

                        │

                        ▼

                 Load Balancer

                        │

                        ▼

                 Reverse Proxy

                        │

      ┌─────────────────┼─────────────────┐

      ▼                 ▼                 ▼

 Frontend API      Authentication     Background Workers

      │                 │                 │

      └──────────────┬──┴─────────────────┘

                     ▼

                 Database

                     │

                     ▼

                   Storage
```

Supporting components:

```
Monitoring

↓

Logging

↓

Alerting

↓

Backup

↓

Security Scanning
```

Modern production systems continuously observe every component.

---

# Practical Examples

## Example 1 – Minimal Image

Instead of:

```dockerfile
FROM ubuntu
```

Prefer:

```dockerfile
FROM python:3.12-slim
```

Benefits:

- Smaller image
- Faster download
- Reduced attack surface
- Lower storage requirements

---

## Example 2 – Immutable Deployment

Incorrect approach:

```
Running Container

↓

Manual Update
```

Correct approach:

```
Update Dockerfile

↓

Build Image

↓

Deploy New Container

↓

Remove Old Container
```

This ensures repeatable deployments.

---

## Example 3 – Resource Limits

Application:

```
Container

↓

CPU Limit

↓

Memory Limit

↓

Stable Operation
```

Resource limits help prevent a single container from consuming excessive host resources.

---

## Example 4 – Health Monitoring

```
Application

↓

Health Check

↓

Healthy

↓

Receive Traffic
```

If unhealthy:

```
Health Check Failed

↓

Restart

or

Traffic Removed
```

Health checks improve application availability.

---

# Hands-on Validation Commands

## Inspect Running Containers

```bash
docker ps
```

---

## Inspect Container Configuration

```bash
docker inspect container_name
```

Verify:

- User
- Mounts
- Networks
- Restart policy
- Resource configuration

---

## Review Resource Usage

```bash
docker stats
```

Monitor:

- CPU
- Memory
- Network
- Block I/O

---

## View Logs

```bash
docker logs container_name
```

Review application behavior and errors.

---

## Display Running Processes

```bash
docker top container_name
```

Confirm only expected processes are running.

---

## Inspect Image Layers

```bash
docker history image_name
```

Review build history and identify unnecessary layers.

---

## Review Docker Events

```bash
docker events
```

Monitor container lifecycle activity in real time.

---

# Production Readiness Checklist

Before deploying to production, verify:

- Images are scanned.
- Images are versioned.
- Containers run as non-root where feasible.
- Secrets are managed securely.
- Health checks are configured.
- Resource limits are defined.
- Monitoring is enabled.
- Logging is centralized.
- Backups are configured.
- Recovery procedures are documented.

---

# Best Practices Checklist

## Development

- Keep Dockerfiles simple.
- Use official or trusted base images.
- Keep dependencies updated.
- Avoid unnecessary packages.
- Follow secure coding practices.

---

## Build

- Build reproducible images.
- Use version tags.
- Scan images.
- Remove build artifacts.
- Generate an SBOM where appropriate.

---

## Deployment

- Deploy immutable images.
- Use automated CI/CD.
- Validate before production.
- Limit privileges.
- Apply network segmentation.

---

## Operations

- Monitor continuously.
- Rotate credentials when necessary.
- Patch regularly by rebuilding images.
- Review logs.
- Perform periodic security assessments.

---

## Common Mistakes

Container Best Practices are often overlooked because containers are perceived as "lightweight virtual machines." In reality, containers require a different operational mindset centered around immutability, automation, security, and observability.

The following are the most common mistakes observed in containerized environments.

---

# 1. Treating Containers Like Virtual Machines

Incorrect approach:

```
Deploy Container

↓

SSH Into Container

↓

Install Software

↓

Modify Files

↓

Continue Running
```

Problems:

- Configuration drift
- Inconsistent environments
- Difficult troubleshooting
- Unreliable deployments

Correct approach:

```
Update Dockerfile

↓

Build New Image

↓

Deploy New Container

↓

Remove Old Container
```

Containers should be treated as **immutable infrastructure**.

---

# 2. Building Large Images

Example:

```
Ubuntu

+

Unused Packages

+

Development Tools

+

Temporary Files

↓

2 GB Image
```

Large images result in:

- Slower builds
- Slower downloads
- Increased storage usage
- Larger attack surface

Use minimal base images and remove unnecessary software.

---

# 3. Running Everything as Root

Default behavior in many images:

```
Application

↓

Root User
```

Risks:

- Privilege escalation
- Greater impact of exploitation
- Increased security exposure

Always use a non-root user whenever feasible.

---

# 4. Hardcoding Secrets

Never store:

- Passwords
- API keys
- Cloud credentials
- Certificates
- Tokens

inside:

```
Dockerfile

↓

Image

↓

Git Repository
```

Use dedicated secret management solutions.

---

# 5. Using `latest` in Production

Poor practice:

```bash
myapp:latest
```

Problem:

```
latest

↓

Different Image

↓

Unexpected Deployment
```

Instead:

```bash
myapp:2.4.1
```

Version-specific tags improve predictability and simplify rollbacks.

---

# 6. Ignoring Image Scanning

Deploying unscanned images may introduce:

- Known CVEs
- Malware
- Vulnerable packages
- Misconfigurations

Recommended workflow:

```
Build

↓

Scan

↓

Fix

↓

Deploy
```

---

# 7. Not Setting Resource Limits

Without limits:

```
Container

↓

Consumes All Memory

↓

Host Becomes Unstable
```

Resource limits protect both the application and the host.

Define:

- CPU limits
- Memory limits
- Process limits
- Storage limits (where applicable)

---

# 8. Exposing Unnecessary Ports

Example:

```
80

443

3306

5432

6379

27017
```

Every exposed port increases the attack surface.

Expose only services that require external access.

---

# 9. Ignoring Logging

Without centralized logging:

```
Application Failure

↓

No Logs

↓

Unknown Root Cause
```

Logs should be:

- Centralized
- Searchable
- Retained appropriately
- Monitored

---

# 10. Not Monitoring Production

Applications should continuously monitor:

- CPU
- Memory
- Network
- Errors
- Latency
- Restarts

Monitoring enables early detection of issues before users are significantly affected.

---

# 11. Skipping Health Checks

Without health checks:

```
Application Hung

↓

Still Running

↓

Traffic Continues

↓

User Failures
```

Health checks allow orchestration platforms to detect unhealthy workloads and take corrective action.

---

# 12. Manual Production Changes

Avoid:

```
SSH

↓

Modify Container

↓

Restart
```

Instead:

```
Git Commit

↓

CI/CD

↓

Build

↓

Deploy
```

Automated deployments improve consistency and auditability.

---

# 13. Keeping Unused Images

Over time:

```
Old Images

↓

Disk Usage

↓

Storage Problems
```

Regularly remove:

- Obsolete images
- Unused containers
- Unused networks
- Unused volumes

while following organizational retention policies.

---

# 14. No Backup Strategy

Containers are replaceable.

Application data often is not.

Back up:

- Databases
- Persistent volumes
- Configuration
- Secrets (using approved procedures)
- Critical business data

Recovery plans should be tested regularly.

---

# 15. Treating Best Practices as Optional

Organizations sometimes implement:

- Security
- Monitoring
- Logging
- Scanning

only after experiencing an incident.

A better approach is:

```
Design

↓

Build

↓

Secure

↓

Deploy

↓

Monitor

↓

Improve
```

Best practices should be integrated from the beginning of the application lifecycle.

---

# Container Best Practices Quick Revision

## Secure Development Lifecycle

```
Design

↓

Dockerfile

↓

Build

↓

Scan

↓

Test

↓

Deploy

↓

Monitor

↓

Improve
```

---

## Security Principles

```
Least Privilege

↓

Defense in Depth

↓

Immutable Infrastructure

↓

Zero Trust

↓

Continuous Improvement
```

These principles reinforce one another to create a resilient container platform.

---

## Production Readiness

Before deployment:

- Images scanned
- Secrets secured
- Resource limits configured
- Health checks enabled
- Logging centralized
- Monitoring active
- Backups verified
- CI/CD validated

---

## Operational Priorities

```
Automation

↓

Monitoring

↓

Logging

↓

Alerting

↓

Incident Response

↓

Continuous Improvement
```

Automation reduces manual error while improving consistency.

---

## Common Validation Commands

```bash
docker ps

docker inspect

docker logs

docker stats

docker top

docker history

docker events

docker system df
```

These commands help validate the operational state of Docker environments.

---

# Container Best Practices Checklist

| Topic | Status |
|--------|:------:|
| Build Small Images | ✓ |
| Use Trusted Base Images | ✓ |
| Run as Non-Root | ✓ |
| Secure Secrets | ✓ |
| Scan Images | ✓ |
| Version Images | ✓ |
| Use Immutable Infrastructure | ✓ |
| Configure Resource Limits | ✓ |
| Enable Health Checks | ✓ |
| Centralize Logging | ✓ |
| Monitor Continuously | ✓ |
| Automate CI/CD | ✓ |
| Back Up Persistent Data | ✓ |
| Apply Least Privilege | ✓ |
| Follow Continuous Improvement | ✓ |

---

# References

## Docker Documentation

- Docker Best Practices
- Docker Engine Documentation
- Docker Build Documentation
- Docker Security Documentation
- Docker CLI Documentation

---

## CNCF Resources

- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)
- Prometheus Documentation
- OpenTelemetry Documentation
- Falco Documentation

---

## Security Standards

- NIST SP 800-190 — Application Container Security Guide
- NIST Secure Software Development Framework (SSDF)
- CIS Docker Benchmark
- OWASP Docker Security Cheat Sheet
- OWASP Container Security Verification Standard

---

## Supply Chain Security

- Sigstore Documentation
- Notary Documentation
- SPDX Specification
- CycloneDX Specification
- SLSA (Supply-chain Levels for Software Artifacts)

---

## Books

- *Container Security* — Liz Rice
- *Docker Deep Dive* — Nigel Poulton
- *Docker in Action* — Jeff Nickoloff & Stephen Kuenzli
- *The Site Reliability Workbook* — Google

---

## Recommended Learning Resources

- Docker Official Documentation
- Linux Foundation Training
- CNCF Learning Paths
- OWASP Projects
- NIST Computer Security Resource Center (CSRC)
- Google Site Reliability Engineering Resources

---

# Container Best Practices Summary

```
Secure by Design

        │

Automate Everything

        │

Build Small Images

        │

Run as Non-Root

        │

Scan Continuously

        │

Deploy Immutably

        │

Monitor Continuously

        │

Respond Quickly

        │

Continuously Improve
```

These principles form the foundation of modern, production-ready container platforms.

