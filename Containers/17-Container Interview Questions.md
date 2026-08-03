# Chapter 17 – Container Interview Questions

## Overview

Container technologies such as **Docker**, **Docker Compose**, **Kubernetes**, and **container security** have become fundamental skills for Software Engineers, DevOps Engineers, DevSecOps Engineers, Cloud Engineers, Site Reliability Engineers (SREs), SOC Analysts, Security Engineers, and Platform Engineers.

This chapter contains carefully selected interview questions ranging from beginner to advanced levels. The questions are designed to evaluate not only factual knowledge but also practical understanding, troubleshooting ability, security awareness, and real-world decision-making.

The questions are grouped into categories commonly used during technical interviews.

---

# Interview Coverage

This chapter covers:

- Container Fundamentals
- Docker Basics
- Docker Architecture
- Dockerfile
- Docker Images
- Docker Containers
- Docker Compose
- Container Networking
- Docker Storage
- Docker Registry
- Docker Security
- Container Vulnerability Management
- Monitoring & Logging
- Incident Response
- Container Forensics
- Best Practices
- Production Scenarios
- Troubleshooting
- DevSecOps Integration

---

# Difficulty Levels

| Level | Description |
|---------|------------|
| Beginner | Basic concepts and commands |
| Intermediate | Practical Docker usage |
| Advanced | Security, architecture, troubleshooting |
| Expert | Production design, incident response, DevSecOps |

---

# Beginner Interview Questions

## Q1. What is a container?

**Answer**

A container is a lightweight, isolated runtime environment that packages an application along with its dependencies, libraries, and configuration so it can run consistently across different environments while sharing the host operating system kernel.

---

## Q2. What problem do containers solve?

**Answer**

Containers eliminate the "it works on my machine" problem by ensuring applications run consistently regardless of the underlying environment.

---

## Q3. What is Docker?

**Answer**

Docker is an open platform for building, packaging, distributing, and running containerized applications.

---

## Q4. Difference between Containers and Virtual Machines?

**Answer**

| Containers | Virtual Machines |
|------------|------------------|
| Share host kernel | Separate guest OS |
| Lightweight | Heavier |
| Faster startup | Slower startup |
| Lower resource usage | Higher resource usage |
| Process isolation | Hardware virtualization |

---

## Q5. What is a Docker Image?

**Answer**

A Docker image is a read-only template containing the application, dependencies, libraries, and configuration required to create one or more containers.

---

## Q6. What is a Docker Container?

**Answer**

A Docker container is a running instance of a Docker image.

---

## Q7. What is Docker Hub?

**Answer**

Docker Hub is Docker's official public registry used to store and distribute container images.

---

## Q8. What is Docker Compose?

**Answer**

Docker Compose is a tool used to define and manage multi-container applications using a YAML configuration file.

---

## Q9. What is a Dockerfile?

**Answer**

A Dockerfile is a text file containing instructions used to build Docker images automatically.

---

## Q10. Why are containers lightweight?

**Answer**

Containers share the host operating system kernel instead of running separate guest operating systems.

---

# Intermediate Interview Questions

## Q11. Explain Docker Architecture.

**Answer**

Docker architecture consists of:

```
Docker Client

↓

Docker Engine

↓

Images

↓

Containers

↓

Registry
```

The Docker client communicates with the Docker Engine, which manages images and containers.

---

## Q12. What is the difference between COPY and ADD?

**Answer**

**COPY**

- Copies files from the local system into the image.
- Preferred for most use cases.

**ADD**

- Supports additional features such as extracting local tar archives and fetching remote URLs (though using URLs in `ADD` is generally discouraged in favor of explicit download commands).

COPY is usually recommended because its behavior is simpler and more predictable.

---

## Q13. What is the difference between CMD and ENTRYPOINT?

**Answer**

**CMD**

Provides default arguments or commands that can be overridden at runtime.

**ENTRYPOINT**

Defines the main executable that always runs unless explicitly overridden.

They are often used together:

```dockerfile
ENTRYPOINT ["python"]

CMD ["app.py"]
```

---

## Q14. What is a Docker Volume?

**Answer**

A Docker volume is Docker-managed persistent storage that exists independently of the container lifecycle.

---

## Q15. What is a Bind Mount?

**Answer**

A bind mount maps a file or directory from the host system directly into a container.

---

## Q16. Why are Volumes preferred over the Writable Layer?

**Answer**

Because data stored in the writable layer is removed when the container is deleted, whereas volumes persist independently.

---

## Q17. What is Port Mapping?

**Answer**

Port mapping exposes a container's internal port through a host port.

Example:

```bash
docker run -p 8080:80 nginx
```

Host port 8080 forwards traffic to port 80 inside the container.

---

## Q18. What is a Docker Registry?

**Answer**

A Docker registry is a repository service used to store and distribute container images.

---

## Q19. What is the purpose of Image Tags?

**Answer**

Tags identify different versions of the same image and simplify version management and rollback.

---

## Q20. Why should production avoid `latest`?

**Answer**

Because `latest` can change over time, making deployments unpredictable.

Version-specific tags provide deterministic deployments.

---

# Advanced Interview Questions

## Q21. What Linux features make containers possible?

**Answer**

Key Linux technologies include:

- Namespaces
- cgroups
- OverlayFS
- Capabilities
- seccomp
- Linux Security Modules (e.g., AppArmor, SELinux)

---

## Q22. Explain Namespaces.

**Answer**

Namespaces isolate system resources such as:

- Processes
- Network
- Mount points
- Hostname
- IPC
- Users (where enabled)

allowing containers to operate independently.

---

## Q23. What are cgroups?

**Answer**

Control Groups (cgroups) limit and account for resource usage such as CPU, memory, and I/O for groups of processes.

---

## Q24. What is OverlayFS?

**Answer**

OverlayFS is a union filesystem that combines multiple image layers into a single unified filesystem presented to the container.

---

## Q25. Why should containers run as non-root?

**Answer**

Running as a non-root user reduces privileges and limits the potential impact of a successful compromise.

---

## Q26. What is Container Escape?

**Answer**

Container escape is a security event where a process breaks out of the container isolation boundary and gains unauthorized access to the host or other containers.

---

## Q27. What is Immutable Infrastructure?

**Answer**

Instead of modifying running systems, immutable infrastructure replaces them with newly built, validated images.

---

## Q28. What is a CVE?

**Answer**

A CVE (Common Vulnerabilities and Exposures) is a publicly assigned identifier for a known security vulnerability.

---

## Q29. What is CVSS?

**Answer**

The Common Vulnerability Scoring System (CVSS) provides a standardized method for assessing the severity of security vulnerabilities.

---

## Q30. Why should images be scanned?

**Answer**

To identify known vulnerabilities, outdated packages, and security issues before deployment.

---

## Quick Oral Interview Questions

These are commonly asked rapid-fire questions during technical interviews.

| Question | Expected Answer |
|----------|-----------------|
| Image vs Container? | Image is a template; container is a running instance. |
| Docker vs VM? | Containers share the kernel; VMs run separate guest OSs. |
| Dockerfile purpose? | Builds Docker images. |
| Docker Compose? | Manages multi-container applications. |
| Docker Hub? | Public container registry. |
| Volume purpose? | Persistent storage. |
| Bind Mount? | Host directory mapped into a container. |
| Port Mapping? | Exposes container ports via host ports. |
| Docker Registry? | Stores container images. |
| Why use tags? | Version management. |
| Why avoid latest? | Unpredictable deployments. |
| Container restart? | Recreate from the image when appropriate. |
| Health Check? | Verifies application health. |
| Non-root user? | Improves security. |
| Immutable Infrastructure? | Replace instead of modifying running containers. |

---
