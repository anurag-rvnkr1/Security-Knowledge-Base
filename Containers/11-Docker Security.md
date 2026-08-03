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

