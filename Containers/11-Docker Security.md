# Chapter 11 – Docker Security

## Overview

Docker Security is the practice of protecting containerized applications, container images, Docker hosts, registries, networks, and the entire container lifecycle from security threats. While containers provide process isolation, they are **not secure by default**. A vulnerable image, misconfigured container, or compromised host can expose the entire application environment.

Container security must be applied throughout the software development lifecycle, from image creation to production deployment.

Docker security encompasses:

- Host Security
- Image Security
- Container Security
- Runtime Security
- Network Security
- Registry Security
- Secrets Management
- Access Control
- Vulnerability Management
- Compliance

Modern organizations integrate Docker security into **DevSecOps**, ensuring security is embedded into every stage of application development and deployment.

---

# Why It Matters

Suppose an attacker compromises a vulnerable container.

```
Internet

↓

Vulnerable Container

↓

Docker Host

↓

Other Containers

↓

Production Systems
```

Without proper security controls, the attacker may:

- Access sensitive data
- Move laterally to other containers
- Exploit kernel vulnerabilities
- Steal secrets
- Disrupt applications

Implementing Docker security significantly reduces these risks.

---

# Docker Security Architecture

```
                Internet

                    │

                    ▼

            Reverse Proxy / Firewall

                    │

                    ▼

            Docker Host Security

                    │

       ┌────────────┼─────────────┐

       ▼            ▼             ▼

 Image Security Container Security Runtime Security

                    │

                    ▼

             Registry Security

                    │

                    ▼

             Monitoring & Logging
```

Security must be applied at every layer of the container ecosystem.

---

# Docker Security Layers

Docker security follows a layered defense approach.

```
Infrastructure

↓

Host Operating System

↓

Docker Engine

↓

Container Image

↓

Running Container

↓

Application
```

Each layer requires its own security controls.

---

# Host Security

The Docker host is the foundation of every container.

Protect the host by:

- Applying operating system updates
- Removing unnecessary software
- Enabling host firewalls
- Restricting SSH access
- Monitoring system activity
- Applying least privilege

A compromised host can affect every container running on it.

---

# Image Security

Container images should be:

- Minimal
- Trusted
- Verified
- Regularly updated
- Scanned for vulnerabilities

Poor image practices include:

- Using outdated packages
- Including unnecessary software
- Hardcoding secrets
- Downloading untrusted images

Always prefer official or trusted images.

---

# Container Security

Running containers should follow security best practices.

Examples:

- Run as non-root users
- Apply resource limits
- Use read-only filesystems where appropriate
- Drop unnecessary Linux capabilities
- Limit network exposure
- Restrict mounted volumes

Containers should have only the permissions they require.

---

# Runtime Security

Security continues after deployment.

Runtime protection includes:

- Process monitoring
- File integrity monitoring
- Anomaly detection
- Behavioral analysis
- Policy enforcement

Runtime monitoring helps detect attacks that occur after deployment.

---

# Registry Security

Container registries should be protected through:

- Authentication
- Authorization
- Access control
- Vulnerability scanning
- Image signing
- Audit logging

Private registries should be accessible only to authorized users and systems.

---

# Secrets Management

Never store secrets inside:

- Dockerfiles
- Images
- Source code
- Public repositories

Examples of secrets:

- API keys
- Database passwords
- Certificates
- Encryption keys
- Access tokens

Use dedicated secret management solutions or secure runtime injection.

---

# Network Security

Reduce the attack surface by:

- Using user-defined networks
- Publishing only required ports
- Segmenting applications
- Applying firewall rules
- Encrypting traffic where appropriate

Internal services should not be exposed directly to the Internet unless necessary.

---

# Access Control

Apply the Principle of Least Privilege.

Restrict:

- Docker daemon access
- Registry permissions
- Container privileges
- Administrative accounts

Only authorized users should manage container infrastructure.

---

# Vulnerability Management

Regularly:

- Scan images
- Update dependencies
- Rebuild images
- Patch base images
- Review security advisories

Security is an ongoing process rather than a one-time activity.

---

# Docker Security Lifecycle

```
Write Dockerfile

        │

Build Image

        │

Scan Image

        │

Push Registry

        │

Deploy Container

        │

Monitor Runtime

        │

Update & Patch

        │

Repeat
```

Security should be integrated into every stage of the lifecycle.

---

# Threats Against Containers

Common threats include:

- Vulnerable images
- Container escape
- Privilege escalation
- Secret exposure
- Supply chain attacks
- Malware
- Misconfigured networking
- Insecure APIs
- Denial of Service (DoS)

Understanding these threats helps organizations implement effective defenses.

---

# Key Concepts

## Defense in Depth

Protect every layer rather than relying on a single security control.

---

## Least Privilege

Grant containers and users only the permissions necessary to perform their tasks.

---

## Immutable Infrastructure

Instead of modifying running containers, rebuild secure images and redeploy.

---

## Continuous Security

Container security must be continuously monitored, updated, and improved.

---

## Secure Supply Chain

Security begins during image creation and continues through registry storage, deployment, and runtime.

---

## DevSecOps

Security should be integrated into CI/CD pipelines rather than added only before production.

---

## How It Works

Docker security is implemented throughout the entire container lifecycle—from writing the Dockerfile to monitoring containers in production. Instead of relying on a single security mechanism, Docker uses a layered security model that combines Linux kernel features, secure image practices, access controls, runtime restrictions, and continuous monitoring.

The objective is to ensure that even if one security layer fails, additional controls continue to protect the application and infrastructure.

---

# Docker Security Lifecycle

```
Developer

      │

Write Secure Dockerfile

      │

Build Image

      │

Vulnerability Scan

      │

Push Registry

      │

Pull Image

      │

Deploy Container

      │

Runtime Monitoring

      │

Logging & Alerting

      │

Update & Patch
```

Security is a continuous process—not a one-time configuration.

---

# Step 1 – Build a Secure Image

A secure deployment begins with the Dockerfile.

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

USER appuser

CMD ["python", "app.py"]
```

Security improvements include:

- Minimal base image
- Non-root user
- Trusted dependencies
- No embedded secrets

---

# Step 2 – Scan the Image

Before publishing an image:

```
Image

↓

Security Scanner

↓

Known Vulnerabilities

↓

Report
```

Scanners compare installed packages against vulnerability databases and identify:

- CVEs (Common Vulnerabilities and Exposures)
- Outdated packages
- Misconfigurations
- Weak dependencies

Images should be scanned before deployment and periodically afterward.

---

# Step 3 – Push to a Secure Registry

Workflow:

```
Image

↓

Authenticated Push

↓

Private/Public Registry

↓

Access Control
```

The registry stores:

- Image layers
- Metadata
- Tags
- Digests

Only authorized users and CI/CD systems should have permission to push images.

---

# Step 4 – Deploy the Container

When a container starts:

```bash
docker run myapp
```

Docker creates:

- Namespaces
- cgroups
- Filesystem isolation
- Network isolation
- Process isolation

These Linux kernel features provide the foundation for container isolation.

---

# Step 5 – Restrict Container Privileges

Containers should run with only the permissions they require.

Example security controls:

```
Container

↓

Non-root User

↓

Limited Capabilities

↓

Read-only Filesystem

↓

Resource Limits
```

Applying the Principle of Least Privilege reduces the impact of potential compromises.

---

# Step 6 – Protect Secrets

Instead of:

```dockerfile
ENV PASSWORD=secret123
```

Use secure runtime injection.

Workflow:

```
Secret Manager

↓

Runtime Injection

↓

Container

↓

Application
```

The image remains free of sensitive information.

---

# Step 7 – Secure Networking

Application architecture:

```
Internet

↓

Load Balancer

↓

Web Container

↓

API Container

↓

Database
```

Only required services are exposed externally.

Internal communication occurs over private container networks.

---

# Step 8 – Runtime Monitoring

After deployment:

```
Container

↓

Runtime Monitor

↓

Logs

↓

Alerts

↓

Incident Response
```

Runtime monitoring can detect:

- Unexpected processes
- Privilege escalation
- Suspicious network activity
- File modifications
- Resource abuse

---

# Step 9 – Patch and Rebuild

Suppose a vulnerability is discovered.

```
Old Base Image

↓

Security Patch

↓

Rebuild Image

↓

Deploy Updated Container
```

Containers are replaced rather than manually modified.

---

# Practical Examples

## Example 1 – Running as a Non-Root User

Dockerfile:

```dockerfile
RUN useradd appuser

USER appuser
```

Benefits:

- Reduced privilege
- Lower impact of exploitation
- Better compliance with security best practices

---

## Example 2 – Read-Only Filesystem

Container:

```
Application

↓

Read-Only Filesystem

↓

Temporary Writes → Volume / tmpfs
```

This limits unauthorized modification of application files.

---

## Example 3 – Minimal Base Image

Instead of:

```dockerfile
FROM ubuntu
```

Use:

```dockerfile
FROM python:3.12-slim
```

Benefits:

- Smaller image
- Fewer packages
- Reduced attack surface
- Faster deployments

---

## Example 4 – Private Registry

Workflow:

```
Developer

↓

CI/CD

↓

Private Registry

↓

Production Cluster
```

Unauthorized users cannot access private application images.

---

# Hands-on Commands

## List Running Containers

```bash
docker ps
```

Review active containers.

---

## Inspect Container Configuration

```bash
docker inspect container_name
```

Check:

- Mounted volumes
- Environment variables
- User
- Network configuration
- Capabilities (where applicable)

---

## Display Running Processes

```bash
docker top container_name
```

Verify the expected processes are running.

---

## View Logs

```bash
docker logs container_name
```

Review application output for errors or suspicious activity.

---

## Display Resource Usage

```bash
docker stats
```

Monitor:

- CPU
- Memory
- Network I/O
- Disk I/O

Unexpected spikes may indicate performance issues or malicious behavior.

---

## Verify Image History

```bash
docker history image_name
```

Review image layers and build history.

---

## Inspect Image Metadata

```bash
docker inspect image_name
```

Examine image configuration and metadata.

---

## Remove Unused Resources

```bash
docker system prune
```

Clean up unused Docker objects to reduce clutter.

Use with caution, particularly on shared or production systems.

---

# Best Practices

### 1. Use Official or Trusted Images

Prefer images published by:

- Official Docker publishers
- Trusted organizations
- Verified maintainers

Avoid unverified images from unknown sources.

---

### 2. Keep Images Minimal

Smaller images contain:

- Fewer packages
- Fewer vulnerabilities
- Faster downloads
- Smaller attack surfaces

---

### 3. Run Containers as Non-Root

Avoid running applications with root privileges unless absolutely necessary.

Use the `USER` instruction in the Dockerfile whenever possible.

---

### 4. Scan Images Regularly

Integrate vulnerability scanning into CI/CD pipelines and repeat scans periodically as new vulnerabilities are disclosed.

---

### 5. Never Store Secrets in Images

Use:

- Secret management systems
- Secure runtime injection
- Environment variables supplied by trusted infrastructure

Never commit secrets to source code or Dockerfiles.

---

### 6. Restrict Network Exposure

Expose only the ports required by external users.

Keep databases, caches, and internal services on private networks.

---

### 7. Monitor Continuously

Monitor:

- Container logs
- Runtime behavior
- Resource usage
- Security alerts
- Image updates

Continuous monitoring improves detection and response to security incidents.

---

## Common Mistakes

Container security is often misunderstood because many users assume Docker automatically secures applications. While Docker provides important isolation mechanisms, security depends on how images, containers, hosts, networks, registries, and deployment pipelines are configured.

The following are the most common Docker security mistakes observed in real-world environments.

---

# 1. Running Containers as Root

By default, many images execute applications as the **root** user.

Example:

```dockerfile
FROM ubuntu

CMD ["python","app.py"]
```

Risk:

```
Application

↓

Root User

↓

High Privileges

↓

Greater Impact if Compromised
```

Recommended:

```dockerfile
RUN useradd appuser

USER appuser
```

Follow the Principle of Least Privilege whenever possible.

---

# 2. Using Untrusted Images

Poor practice:

```
Internet

↓

Unknown Image

↓

Production
```

Risks:

- Malware
- Hidden backdoors
- Cryptocurrency miners
- Outdated software

Prefer:

- Official images
- Verified publishers
- Trusted enterprise registries

---

# 3. Never Updating Images

Old images accumulate vulnerabilities over time.

Example:

```
Ubuntu Image

↓

2 Years Old

↓

Hundreds of Known CVEs
```

Regularly:

- Update base images
- Rebuild images
- Redeploy containers

Security patches are delivered through updated images, not by modifying running containers.

---

# 4. Hardcoding Secrets

Never place secrets in:

```dockerfile
ENV PASSWORD=secret123
```

or

```yaml
environment:

  PASSWORD: secret123
```

or

```
Source Code
```

Use:

- Secret managers
- Docker Secrets
- Kubernetes Secrets
- Cloud secret management services

---

# 5. Exposing Too Many Ports

Poor example:

```
80

443

5432

3306

6379

27017
```

Every exposed port increases the attack surface.

Expose only the services that must be reachable externally.

---

# 6. Ignoring Image Scanning

Many deployments skip vulnerability scanning.

Recommended workflow:

```
Build

↓

Security Scan

↓

Fix Issues

↓

Registry

↓

Deployment
```

Do not deploy images with known high-severity vulnerabilities unless there is a documented and accepted risk.

---

# 7. Assuming Containers Are Virtual Machines

Containers share the host kernel.

```
Host Kernel

↓

Container A

↓

Container B
```

Unlike virtual machines, containers do not provide hardware-level isolation.

Protect the host because its security affects every container.

---

# 8. Running Privileged Containers

Example:

```bash
docker run --privileged
```

This grants extensive access to the host.

Risks include:

- Kernel interaction
- Device access
- Increased potential impact of a container compromise

Avoid privileged mode unless there is a clearly justified requirement.

---

# 9. Ignoring Container Logs

Security events often appear first in application logs.

Monitor:

- Authentication failures
- Unexpected restarts
- Permission errors
- Suspicious commands
- Network anomalies

Logs are a critical source of operational and security insight.

---

# 10. Giving Containers Excessive Permissions

Containers should not receive unnecessary:

- Linux capabilities
- Mounted host directories
- Network access
- Administrative privileges

Restrict permissions to the minimum required for the application.

---

# 11. Forgetting Runtime Security

Security does not end after deployment.

Applications should continue to be monitored for:

- New processes
- Unexpected outbound connections
- File modifications
- Privilege escalation attempts
- Resource abuse

Runtime monitoring complements preventive security controls.

---

# 12. Skipping Host Security

A secure container cannot compensate for an insecure host.

Protect the Docker host by:

- Applying updates
- Limiting administrative access
- Enabling firewalls
- Monitoring activity
- Hardening the operating system

---

# 13. Trusting Every Registry

Not every registry provides the same level of security.

Before using images:

Verify:

- Publisher identity
- Image maintenance
- Security practices
- Reputation

Prefer trusted organizational or official registries.

---

# 14. Forgetting Supply Chain Security

Modern attacks increasingly target the software supply chain.

Secure the entire process:

```
Source Code

↓

Dependencies

↓

Dockerfile

↓

Image

↓

Registry

↓

Deployment
```

Each stage should include security verification.

---

# 15. Treating Security as a Final Step

Traditional workflow:

```
Develop

↓

Deploy

↓

Security
```

Modern DevSecOps workflow:

```
Develop

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
```

Security should be integrated continuously throughout the development lifecycle.

---

# Docker Security Quick Revision

## Defense in Depth

```
Application

↓

Container

↓

Image

↓

Docker Engine

↓

Host

↓

Infrastructure
```

Multiple security layers provide stronger protection than any single control.

---

## Secure Image Workflow

```
Trusted Base Image

↓

Build

↓

Scan

↓

Registry

↓

Deploy
```

---

## Security Controls

- Non-root users
- Minimal images
- Vulnerability scanning
- Secret management
- Private registries
- Network segmentation
- Runtime monitoring
- Logging
- Access control

---

## Common Security Commands

```bash
docker inspect

docker history

docker logs

docker top

docker stats

docker system prune
```

These commands assist with inspection, monitoring, and maintenance. They complement dedicated security tooling but are not substitutes for it.

---

# Docker Security Checklist

| Topic | Status |
|--------|:------:|
| Understand Host Security | ✓ |
| Understand Image Security | ✓ |
| Understand Container Security | ✓ |
| Understand Runtime Security | ✓ |
| Understand Registry Security | ✓ |
| Understand Secrets Management | ✓ |
| Understand Access Control | ✓ |
| Understand Network Security | ✓ |
| Understand Vulnerability Management | ✓ |
| Understand Secure Supply Chain | ✓ |
| Understand DevSecOps Integration | ✓ |
| Understand Least Privilege | ✓ |
| Understand Defense in Depth | ✓ |
| Understand Security Best Practices | ✓ |
| Understand Common Security Mistakes | ✓ |

---

# References

## Docker Documentation

- Docker Security Documentation
- Docker Engine Security Guide
- Docker CLI Documentation
- Docker Build Documentation
- Docker Hardened Images Documentation

---

## OCI Standards

- OCI Image Specification
- OCI Runtime Specification
- OCI Distribution Specification

---

## CNCF Resources

- Kubernetes Security Documentation
- Cloud Native Computing Foundation (CNCF)
- Falco Documentation
- Open Policy Agent (OPA) Documentation

---

## Security Resources

- NIST SP 800-190 — Application Container Security Guide
- OWASP Docker Security Cheat Sheet
- OWASP Container Security Verification Standard
- CIS Docker Benchmark
- MITRE ATT&CK for Containers
- Sigstore Documentation
- Notary Documentation

---

## Books

- *Container Security* — Liz Rice
- *Docker Deep Dive* — Nigel Poulton
- *Docker in Action* — Jeff Nickoloff & Stephen Kuenzli
- *Kubernetes Security* — Liz Rice

---

## Recommended Learning Resources

- Docker Official Documentation
- Docker Labs
- Linux Foundation Training
- CNCF Learning Paths
- Play with Docker
- NIST Computer Security Resource Center (CSRC)
- OWASP Projects

