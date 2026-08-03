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

