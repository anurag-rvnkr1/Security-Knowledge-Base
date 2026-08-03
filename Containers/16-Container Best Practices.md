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

