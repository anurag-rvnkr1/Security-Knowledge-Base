# Container Cheat Sheet

## Overview

This Container Cheat Sheet is a **quick-reference guide** for Docker, containerization, security, monitoring, troubleshooting, incident response, and DevSecOps. It is designed for:

- Technical Interviews
- Daily Operations
- DevOps
- DevSecOps
- Cloud Engineers
- Security Engineers
- Platform Engineers
- Site Reliability Engineers (SRE)
- Students and Beginners

Instead of explaining concepts in depth, this cheat sheet provides concise summaries, diagrams, commands, and best practices for rapid revision.

---

# Container Lifecycle

```
Dockerfile

↓

Build Image

↓

Tag Image

↓

Scan Image

↓

Push Registry

↓

Pull Image

↓

Run Container

↓

Monitor

↓

Update

↓

Rebuild

↓

Redeploy

↓

Remove
```

---

# Docker Architecture

```
Docker Client

↓

Docker Engine

↓

Docker Images

↓

Docker Containers

↓

Docker Registry
```

---

# Container vs Virtual Machine

| Container | Virtual Machine |
|------------|-----------------|
| Shares Host Kernel | Separate Guest OS |
| Lightweight | Heavier |
| Starts in Seconds | Slower Startup |
| Lower Resource Usage | Higher Resource Usage |
| Process Isolation | Hardware Virtualization |

---

# Dockerfile Workflow

```
Dockerfile

↓

docker build

↓

Docker Image

↓

docker run

↓

Running Container
```

---

# Image vs Container

| Image | Container |
|--------|-----------|
| Read-only template | Running instance |
| Static | Dynamic |
| Can create multiple containers | Executes application |

---

# Container Storage

```
Writable Layer

↓

Temporary Data


Docker Volume

↓

Persistent Data


Bind Mount

↓

Host Directory
```

---

# Docker Networking

```
Host

↓

Bridge Network

↓

Container A

↓

Container B
```

Common network types:

- Bridge
- Host
- None
- Overlay
- Macvlan

---

# Container Security Layers

```
Application

↓

Container

↓

Image

↓

Docker Engine

↓

Host OS

↓

Infrastructure
```

Apply security controls at every layer.

---

# Container Security Principles

- Least Privilege
- Defense in Depth
- Immutable Infrastructure
- Zero Trust
- Continuous Monitoring
- Secure by Default

---

# Container Incident Response

```
Preparation

↓

Detection

↓

Analysis

↓

Containment

↓

Eradication

↓

Recovery

↓

Lessons Learned
```

---

# Container Forensics

```
Incident

↓

Preserve Evidence

↓

Collect

↓

Analyze

↓

Timeline

↓

Report
```

Evidence sources:

- Container Logs
- Docker Events
- Images
- Host Logs
- Registry
- Cloud Audit Logs

---

# Container Monitoring

```
Metrics

↓

Logs

↓

Alerts

↓

Dashboards

↓

Response
```

---

# Three Pillars of Observability

```
Metrics

↓

Logs

↓

Traces
```

---

# Golden Signals

```
Latency

↓

Traffic

↓

Errors

↓

Saturation
```

---

# RED Method

```
Rate

↓

Errors

↓

Duration
```

---

# USE Method

```
Utilization

↓

Saturation

↓

Errors
```

---

# Container Vulnerability Management

```
Build

↓

Scan

↓

Identify CVEs

↓

Prioritize

↓

Fix

↓

Rebuild

↓

Deploy
```

---

# Immutable Infrastructure

```
Old Container

↓

New Image

↓

New Container

↓

Old Container Removed
```

Never patch running production containers.

---

# Container Best Practices

- Build small images
- Use trusted base images
- Run as non-root
- Keep images updated
- Scan continuously
- Use version tags
- Avoid hardcoded secrets
- Centralize logging
- Monitor continuously
- Automate deployments
- Use health checks
- Apply resource limits

---

# Docker CLI Cheat Sheet

## Images

Build image

```bash
docker build -t myapp .
```

List images

```bash
docker images
```

Inspect image

```bash
docker inspect image_name
```

Image history

```bash
docker history image_name
```

Remove image

```bash
docker rmi image_name
```

---

## Containers

Run container

```bash
docker run image_name
```

Run detached

```bash
docker run -d image_name
```

List running containers

```bash
docker ps
```

List all containers

```bash
docker ps -a
```

Stop container

```bash
docker stop container_name
```

Start container

```bash
docker start container_name
```

Restart container

```bash
docker restart container_name
```

Remove container

```bash
docker rm container_name
```

---

## Logs

View logs

```bash
docker logs container_name
```

Follow logs

```bash
docker logs -f container_name
```

---

## Resource Monitoring

View resource usage

```bash
docker stats
```

Running processes

```bash
docker top container_name
```

Docker events

```bash
docker events
```

---

## Networks

List networks

```bash
docker network ls
```

Inspect network

```bash
docker network inspect network_name
```

Create network

```bash
docker network create mynetwork
```

---

## Volumes

List volumes

```bash
docker volume ls
```

Inspect volume

```bash
docker volume inspect volume_name
```

Create volume

```bash
docker volume create myvolume
```

---

## Registry

Login

```bash
docker login
```

Pull image

```bash
docker pull nginx
```

Push image

```bash
docker push username/myapp:1.0
```

Tag image

```bash
docker tag myapp username/myapp:1.0
```

---

## Cleanup

Remove stopped containers

```bash
docker container prune
```

Remove unused images

```bash
docker image prune
```

Remove unused volumes

```bash
docker volume prune
```

Remove unused networks

```bash
docker network prune
```

Remove everything unused

```bash
docker system prune
```

---

# Security Checklist

✅ Use official images

✅ Run as non-root

✅ Keep images updated

✅ Scan images

✅ Avoid hardcoded secrets

✅ Limit capabilities

✅ Apply resource limits

✅ Enable logging

✅ Enable monitoring

✅ Rotate credentials

✅ Centralize logs

✅ Secure registries

---

# Incident Response Checklist

```
Detect

↓

Validate

↓

Collect Evidence

↓

Contain

↓

Investigate

↓

Recover

↓

Lessons Learned
```

---

# Forensics Checklist

- Preserve volatile evidence
- Collect container logs
- Review Docker events
- Inspect images
- Review registry activity
- Analyze host logs
- Correlate cloud audit logs
- Build incident timeline
- Document findings

---

# Production Readiness Checklist

- Images scanned
- Secrets secured
- Versioned images
- Resource limits configured
- Health checks enabled
- Logging centralized
- Monitoring active
- Backup strategy verified
- Recovery procedures documented
- CI/CD automated

---

# Common Linux Features Behind Containers

| Feature | Purpose |
|----------|---------|
| Namespaces | Resource isolation |
| cgroups | Resource control |
| OverlayFS | Layered filesystem |
| Capabilities | Fine-grained privileges |
| seccomp | System call filtering |
| AppArmor / SELinux | Mandatory access control |

---

# Most Important Interview Definitions

| Question | One-Line Answer |
|----------|-----------------|
| What is Docker? | Platform for building and running containers. |
| What is a Container? | Isolated runtime instance of an application. |
| What is an Image? | Read-only template used to create containers. |
| What is Dockerfile? | Instructions for building Docker images. |
| What is Docker Compose? | Tool for managing multi-container applications. |
| What is a Volume? | Persistent Docker-managed storage. |
| What is Bind Mount? | Host directory mapped into a container. |
| What is Registry? | Repository for storing container images. |
| What is CVE? | Public identifier for a security vulnerability. |
| What is CVSS? | Standard severity scoring system for vulnerabilities. |
| What is SBOM? | Inventory of software components in an application. |
| What is Immutable Infrastructure? | Replace systems instead of modifying them. |

---

# Complete Container Learning Flow

```
Container Fundamentals
        │
Docker Architecture
        │
Docker Commands
        │
Dockerfile
        │
Docker Images
        │
Docker Containers
        │
Docker Compose
        │
Networking
        │
Storage
        │
Registry
        │
Security
        │
Vulnerability Management
        │
Monitoring & Logging
        │
Incident Response
        │
Forensics
        │
Best Practices
        │
Interview Preparation
        │
Production Deployment
        │
Cloud Native Engineering
```

---

# Final Revision Tips

### Before an Interview

✔ Understand container fundamentals.

✔ Practice Docker CLI commands.

✔ Build a multi-container application.

✔ Learn Docker networking and storage.

✔ Understand image security and vulnerability management.

✔ Practice troubleshooting.

✔ Review monitoring and logging concepts.

✔ Understand incident response and forensics.

✔ Study production best practices.

---

# Golden Rule

```
Build Securely

↓

Scan Continuously

↓

Deploy Immutably

↓

Monitor Continuously

↓

Respond Quickly

↓

Learn Constantly

↓

Improve Continuously
```

---

## Congratulations! 🎉

You have completed the **Container Learning Handbook**.

You now have coverage of:

- Docker Fundamentals
- Docker Architecture
- Docker CLI
- Dockerfile
- Docker Images
- Docker Containers
- Docker Compose
- Networking
- Storage
- Registry
- Security
- Vulnerability Management
- Monitoring & Logging
- Incident Response
- Container Forensics
- Best Practices
- Interview Questions
- Production Operations
- DevSecOps Foundations

This handbook provides a strong foundation for Docker, container security, DevOps, DevSecOps, Cloud Security, Platform Engineering, SRE, and technical interview preparation.

---