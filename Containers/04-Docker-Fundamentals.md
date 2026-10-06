# Chapter 4 – Docker Fundamentals

## Overview

Docker is an open-source containerization platform that enables developers and organizations to build, package, distribute, and run applications inside lightweight, portable containers. Since its introduction in 2013, Docker has become the de facto standard for container-based application development and deployment.

Docker simplifies application delivery by packaging the application together with its dependencies, runtime, libraries, and configuration into a **container image**. This ensures the application behaves consistently across development, testing, staging, and production environments.

Docker abstracts the complexities of Linux container technologies such as namespaces, cgroups, and union file systems, providing a user-friendly interface for creating and managing containers.

Today, Docker plays a central role in:

- Cloud Computing
- DevOps
- DevSecOps
- Microservices
- Continuous Integration / Continuous Deployment (CI/CD)
- Kubernetes
- Edge Computing
- AI/ML Workloads

Understanding Docker is essential for anyone working with modern cloud-native applications.

---

# Why It Matters

Before Docker, developers frequently encountered deployment issues caused by differences between environments.

Typical problems included:

- Different operating systems
- Missing libraries
- Incompatible runtime versions
- Dependency conflicts
- Manual software installation
- Environment-specific configurations

Docker addresses these issues by packaging everything required into a standardized image.

Benefits include:

- Consistent deployments
- Faster software delivery
- Simplified dependency management
- Lightweight execution
- Improved scalability
- Easier collaboration
- Rapid rollback
- Better automation

Docker has significantly accelerated software development and operations workflows.

---

# What is Docker?

Docker is **not** the container itself.

Docker is a **container platform** that provides tools and services to:

- Build images
- Store images
- Pull images
- Run containers
- Manage containers
- Configure networking
- Manage storage
- Automate deployments

Think of Docker as a complete ecosystem for container lifecycle management.

---

# Docker Architecture

The Docker platform consists of multiple components working together.

```
                 Docker Client

                      │

                      ▼

                Docker Engine API

                      │

                      ▼

               Docker Daemon (dockerd)

      ┌──────────┼───────────┐

      ▼          ▼           ▼

 Images      Containers    Networks

      │                      │

      ▼                      ▼

    Volumes           Container Runtime

                      │

                      ▼

                 Linux Kernel

                      │

                      ▼

                 Host Operating System
```

Each component performs a specialized function.

---

# Major Docker Components

## 1. Docker Client

The Docker Client is the command-line interface (CLI) used by users.

Examples:

```bash
docker build

docker run

docker pull

docker push
```

The client sends requests to the Docker Daemon using the Docker Engine API.

---

## 2. Docker Daemon (dockerd)

The Docker Daemon is the background service responsible for managing Docker objects.

Responsibilities:

- Build images
- Pull images
- Run containers
- Manage networks
- Manage volumes
- Handle image storage
- Communicate with registries

The daemon performs the actual work requested by the Docker Client.

---

## 3. Docker Engine

Docker Engine is the core platform that includes:

- Docker Client
- Docker Daemon
- Docker Engine API

It provides the complete runtime environment for Docker containers.

---

## 4. Docker Images

Images are immutable templates used to create containers.

They contain:

- Application code
- Dependencies
- Runtime
- Libraries
- Metadata
- Startup configuration

Images can be:

- Built locally
- Downloaded
- Shared
- Versioned

---

## 5. Docker Containers

Containers are running instances of Docker images.

Each container includes:

- Writable layer
- Running processes
- Network configuration
- Resource limits
- Mounted volumes

Multiple containers can be created from the same image.

---

## 6. Docker Registry

A registry stores Docker images.

Popular registries include:

- Docker Hub
- Amazon ECR
- Azure Container Registry
- Google Artifact Registry
- Harbor
- Quay

Registries enable image distribution across environments.

---

## 7. Docker Networks

Docker networking enables communication between:

- Containers
- Host systems
- External networks

Supported network types include:

- Bridge
- Host
- Overlay
- Macvlan
- None

Networking will be explored in detail in a later chapter.

---

## 8. Docker Volumes

Volumes provide persistent storage.

Without volumes:

```
Container Removed

↓

Application Data Lost
```

With volumes:

```
Container

↓

Docker Volume

↓

Persistent Storage
```

Volumes separate application data from container lifecycle.

---

# Docker Workflow

A typical Docker workflow follows these steps.

```
Developer

      │

      ▼

Write Application

      │

      ▼

Create Dockerfile

      │

      ▼

Build Image

      │

      ▼

Store Image

      │

      ▼

Push to Registry

      │

      ▼

Pull Image

      │

      ▼

Run Container

      │

      ▼

Application Running
```

This workflow enables consistent deployments across environments.

---

# Docker vs Virtual Machines

| Docker | Virtual Machine |
|---------|-----------------|
| Shares host kernel | Includes guest operating system |
| Lightweight | Larger footprint |
| Starts quickly | Slower startup |
| Lower memory usage | Higher memory usage |
| Better application density | Lower density |
| OS-level virtualization | Hardware virtualization |

Docker is generally preferred for cloud-native workloads due to its efficiency.

---

# Docker Editions

Historically, Docker was available in two editions:

### Docker Community Edition (CE)

- Free
- Open source
- Suitable for development and small-scale deployments

---

### Docker Enterprise Edition (EE)

Previously offered enterprise features such as:

- Advanced management
- Security integrations
- Commercial support

Many enterprise capabilities are now available through Docker Business offerings and the broader container ecosystem.

---

# Docker Objects

Docker manages several object types.

| Object | Purpose |
|---------|----------|
| Image | Template used to create containers |
| Container | Running instance of an image |
| Volume | Persistent storage |
| Network | Container communication |
| Registry | Image repository |
| Dockerfile | Image build instructions |
| Compose File | Multi-container application definition |

---

# Docker Lifecycle

```
Dockerfile

      │

      ▼

Build Image

      │

      ▼

Store Image

      │

      ▼

Run Container

      │

      ▼

Start

      │

      ▼

Running

      │

      ▼

Stop

      │

      ▼

Remove
```

Understanding this lifecycle is fundamental to effective Docker usage.

---

# Key Concepts

## Containerization

Docker packages applications with all required dependencies into portable containers.

---

## Image Immutability

Images are never modified after creation.

Updates are performed by creating new images and replacing existing containers.

---

## Layered Images

Each Dockerfile instruction typically creates a new image layer.

This enables:

- Layer reuse
- Faster builds
- Reduced storage
- Efficient downloads

---

## Portability

Docker images can run consistently across:

- Developer laptops
- Test environments
- On-premises servers
- Public clouds
- Hybrid clouds

---

## Isolation

Docker isolates:

- Processes
- Filesystems
- Networks
- Users
- Resources

Isolation enables multiple applications to coexist safely.

---

## Automation

Docker integrates seamlessly with:

- CI/CD pipelines
- Kubernetes
- DevOps workflows
- Infrastructure as Code
- Cloud-native platforms

Automation is one of Docker's greatest strengths.

---

## How It Works

Docker simplifies container creation and management by automating the entire container lifecycle. Instead of manually installing operating systems, libraries, dependencies, and applications on every server, Docker packages everything into an immutable image that can be executed consistently anywhere Docker is available.

Internally, Docker combines several components—including the Docker Client, Docker Daemon, Docker Engine API, container runtime, Linux kernel features, and container images—to create and manage isolated application environments.

---

# Docker Workflow

```
Developer

      │

      ▼

Write Application

      │

      ▼

Create Dockerfile

      │

      ▼

Docker Build

      │

      ▼

Container Image

      │

      ▼

Docker Registry

      │

      ▼

Docker Pull

      │

      ▼

Docker Run

      │

      ▼

Running Container

      │

      ▼

Application Available
```

Each stage contributes to a consistent and repeatable deployment process.

---

## Step 1 – Write the Application

The workflow begins with application development.

Example languages include:

- Python
- Java
- Go
- Node.js
- C#
- PHP

The application may depend on:

- Runtime
- Third-party libraries
- Environment variables
- Configuration files

Docker packages these requirements together.

---

## Step 2 – Create a Dockerfile

The Dockerfile defines how the image should be built.

Example workflow:

```
Select Base Image

↓

Install Packages

↓

Copy Application

↓

Configure Environment

↓

Specify Startup Command
```

The Dockerfile serves as a blueprint for image creation.

---

## Step 3 – Build the Image

The command:

```bash
docker build
```

instructs Docker to:

1. Read the Dockerfile.
2. Download the base image if necessary.
3. Execute each instruction.
4. Create image layers.
5. Generate the final image.

Example:

```
Dockerfile

      │

Docker Build

      │

Image Layers

      │

Final Image
```

The resulting image is immutable and versioned.

---

## Step 4 – Store the Image

Images may remain local or be uploaded to a registry.

```
Local Image

      │

Push

      │

Docker Hub

or

Private Registry
```

Registries simplify image sharing between developers, CI/CD pipelines, and production environments.

---

## Step 5 – Pull the Image

When another system requires the application:

```
docker pull
```

Docker:

- Contacts the registry.
- Downloads missing layers.
- Reuses existing layers when possible.
- Stores the image locally.

Layer reuse minimizes download size and deployment time.

---

## Step 6 – Create the Container

Running:

```bash
docker run
```

causes Docker to:

- Create a writable layer.
- Configure namespaces.
- Apply cgroups.
- Configure networking.
- Mount volumes.
- Allocate resources.

```
Image

     │

Create Container

     │

Apply Isolation

     │

Prepare Runtime
```

The image itself remains unchanged.

---

## Step 7 – Start the Application

Docker starts the application's primary process.

```
Container

     │

PID 1

     │

Application

     │

Listening for Requests
```

The container remains active while the main process continues running.

If the primary process exits, Docker considers the container stopped.

---

## Step 8 – Runtime Management

During execution, Docker manages:

- Process lifecycle
- Networking
- Mounted volumes
- Resource limits
- Logging
- Restart policies
- Health status

Docker continuously interacts with the Linux kernel to maintain isolation and resource control.

---

## Step 9 – Stop and Remove the Container

Containers may be:

```
Running

   │

Stop

   │

Exited

   │

Remove
```

Removing a container:

- Deletes the writable layer.
- Preserves the image.
- Preserves external volumes (unless explicitly removed).

A new container can later be created from the same image.

---

# Practical Examples

## Example 1 – Web Server Deployment

A developer wants to deploy Nginx.

Workflow:

```
docker pull nginx

↓

docker run nginx

↓

Web Server Running
```

No manual installation or dependency configuration is required.

---

## Example 2 – Team Collaboration

Five developers work on the same project.

Without Docker:

- Different package versions
- Different runtimes
- Different operating systems

Result:

> "It works on my machine."

With Docker:

```
Shared Docker Image

        │

Developer A

Developer B

Developer C

Developer D

Developer E
```

All developers use identical environments, eliminating configuration inconsistencies.

---

## Example 3 – CI/CD Pipeline

```
Git Commit

     │

CI Pipeline

     │

Build Docker Image

     │

Push Registry

     │

Deploy Container
```

This enables automated, repeatable deployments across environments.

---

## Example 4 – Scaling an API

Suppose an API experiences increased traffic.

Instead of upgrading a single server:

```
API Image

    │

 ┌──┼──┐

 ▼  ▼  ▼

API API API
```

Multiple containers can be launched from the same image to handle additional requests.

---

# Hands-on Commands

## Display Docker Version

```bash
docker version
```

Displays Docker Client and Docker Engine versions.

---

## Display Docker Information

```bash
docker info
```

Shows:

- Storage driver
- Number of containers
- Number of images
- CPU
- Memory
- Runtime
- Docker Root Directory

---

## Search Docker Hub

```bash
docker search nginx
```

Searches Docker Hub for available images.

---

## Pull an Image

```bash
docker pull nginx
```

Downloads the latest official Nginx image.

---

## List Images

```bash
docker images
```

Displays locally stored images.

---

## Run a Container

```bash
docker run nginx
```

Creates and starts a container.

---

## Run in Detached Mode

```bash
docker run -d nginx
```

Runs the container in the background.

---

## Publish a Port

```bash
docker run -p 8080:80 nginx
```

Maps:

```
Host Port 8080

↓

Container Port 80
```

allowing external access to the web server.

---

## View Running Containers

```bash
docker ps
```

Lists active containers.

---

## View All Containers

```bash
docker ps -a
```

Lists running and stopped containers.

---

## Stop a Container

```bash
docker stop <container_name>
```

Gracefully stops the container.

---

## Remove a Container

```bash
docker rm <container_name>
```

Deletes a stopped container.

---

## Remove an Image

```bash
docker rmi <image_name>
```

Deletes a local image.

---

## View Container Logs

```bash
docker logs <container_name>
```

Displays application output and error logs.

---

## Execute Commands Inside a Container

```bash
docker exec -it <container_name> bash
```

Starts an interactive Bash shell inside the running container.

---

## Inspect Docker Objects

```bash
docker inspect <container_name>
```

Displays detailed JSON information about Docker objects.

---

# Best Practices

### 1. Learn the Docker Workflow

Understand the complete flow:

```
Dockerfile

↓

Image

↓

Registry

↓

Container

↓

Application
```

before learning advanced topics such as Docker Compose and Kubernetes.

---

### 2. Use Official Images

Prefer trusted images maintained by verified publishers.

---

### 3. Version Images

Use explicit tags such as:

```
python:3.12

nginx:1.27

postgres:17
```

instead of relying on `latest`.

---

### 4. Keep Images Small

Use minimal base images to improve security, reduce download size, and speed up deployments.

---

### 5. Avoid Manual Container Changes

Never treat production containers like traditional servers.

Rebuild images instead of modifying running containers.

---

### 6. Separate Configuration from Images

Store configuration outside the image using:

- Environment variables
- Configuration files
- Secrets management

This makes images reusable across environments.

---

### 7. Understand Every Docker Object

Know the purpose of:

- Images
- Containers
- Networks
- Volumes
- Registries
- Dockerfiles

Understanding these relationships simplifies troubleshooting and prepares you for orchestration platforms such as Kubernetes.

---

## Common Mistakes

Docker is designed to simplify application deployment, but incorrect usage can lead to security vulnerabilities, inefficient resource utilization, deployment failures, and operational complexity. Many Docker-related issues stem from misunderstanding Docker's architecture and workflow rather than problems with Docker itself.

The following are some of the most common mistakes made by beginners and professionals.

---

### 1. Confusing Docker with Containers

A common misconception is that Docker **is** the container.

In reality:

```
Docker

      │

Creates

      ▼

Container Images

      │

Runs

      ▼

Containers
```

Docker is a **container platform**, while a **container** is the isolated environment in which an application executes.

---

### 2. Treating Docker as a Virtual Machine

Many beginners expect Docker containers to behave like traditional servers.

Example:

```
Docker Container

↓

Install Packages

↓

SSH Into Container

↓

Modify Files

↓

Save Forever
```

This is not the recommended approach.

Containers should be:

- Disposable
- Immutable
- Reproducible

Instead of repairing containers, rebuild the image and redeploy.

---

### 3. Using the `latest` Tag Everywhere

Example:

```bash
docker pull nginx:latest
```

The `latest` tag is not guaranteed to remain the same.

Potential issues:

- Unexpected upgrades
- Compatibility problems
- Difficult rollbacks

Instead:

```bash
nginx:1.27.0

python:3.12

redis:7.4
```

Pinning versions improves deployment consistency.

---

### 4. Building Large Images

Common causes include:

- Large base images
- Unnecessary packages
- Temporary build files
- Development tools included in production images

Consequences:

- Slower builds
- Longer downloads
- Increased storage usage
- Larger attack surface

Use minimal and purpose-built base images where appropriate.

---

### 5. Running Everything as Root

By default, many containers run as the `root` user.

Risks include:

- Privilege escalation
- Increased impact of vulnerabilities
- Greater consequences if a container escape occurs

Whenever possible, create and use a non-root user inside the container.

---

### 6. Hardcoding Secrets

Avoid storing:

- Passwords
- API keys
- Access tokens
- Certificates
- Database credentials

inside:

- Dockerfiles
- Images
- Source code
- Version control

Use dedicated secrets management solutions instead.

---

### 7. Ignoring Volumes

A common mistake is storing important data inside the container.

```
Container

↓

Database Files

↓

Container Removed

↓

Database Lost
```

Instead:

```
Container

↓

Docker Volume

↓

Persistent Data
```

Volumes ensure important data survives container replacement.

---

### 8. Not Cleaning Up Docker Resources

Over time, systems accumulate:

- Dangling images
- Unused containers
- Unused networks
- Unused volumes

Consequences:

- Disk space exhaustion
- Slower builds
- Operational clutter

Regularly remove unused resources.

---

### 9. Publishing Unnecessary Ports

Incorrect example:

```bash
docker run -p 22:22
```

if SSH is not required.

Only publish ports that must be externally accessible.

Principle:

```
Default

↓

Private

↓

Expose Only Required Services
```

Reducing exposed services minimizes the attack surface.

---

### 10. Ignoring Logs

Containers generate valuable operational information.

Monitor:

- Startup failures
- Application errors
- Warnings
- Health checks
- Runtime exceptions

Centralized logging simplifies troubleshooting and incident response.

---

### 11. Assuming Docker Automatically Provides Security

Docker provides isolation but does not guarantee comprehensive security.

Additional protections include:

- Image scanning
- Least privilege
- Runtime protection
- Secrets management
- Network segmentation
- Security policies
- Continuous monitoring

Security must be intentionally implemented.

---

### 12. Forgetting That Containers Are Ephemeral

Containers should be treated as temporary execution environments.

Incorrect workflow:

```
Fix Running Container

↓

Keep Using It
```

Recommended workflow:

```
Update Source

↓

Build New Image

↓

Deploy New Container

↓

Remove Old Container
```

This approach supports reliable and repeatable deployments.

---

### 13. Skipping Image Scanning

Images may contain:

- Known vulnerabilities
- Outdated packages
- Malware
- Misconfigurations

Scan images regularly before deployment into production.

---

### 14. Learning Only Docker Commands

Memorizing commands such as:

```bash
docker run

docker exec

docker ps

docker logs
```

without understanding:

- Images
- Layers
- Registries
- Runtimes
- Networking
- Volumes

limits your ability to troubleshoot and design containerized systems.

A strong conceptual foundation is more valuable than command memorization alone.

---

### 15. Ignoring Docker Best Practices in CI/CD

Poor practices include:

- Building images directly on production servers
- Using unverified images
- Skipping automated testing
- Deploying without vulnerability scanning
- Lack of image versioning

Modern CI/CD pipelines should automate image building, testing, scanning, and deployment.

---

# Docker Fundamentals Checklist

| Topic | Status |
|--------|:------:|
| Understand Docker Architecture | ✓ |
| Understand Docker Client | ✓ |
| Understand Docker Daemon | ✓ |
| Understand Docker Engine | ✓ |
| Understand Docker Images | ✓ |
| Understand Docker Containers | ✓ |
| Understand Docker Registries | ✓ |
| Understand Docker Networks | ✓ |
| Understand Docker Volumes | ✓ |
| Understand Docker Workflow | ✓ |
| Understand Docker Lifecycle | ✓ |
| Understand Image Layers | ✓ |
| Understand Docker vs Virtual Machines | ✓ |
| Know Essential Docker Commands | ✓ |
| Understand Core Docker Best Practices | ✓ |

---

# References

## Docker Documentation

- Docker Engine Documentation
- Docker CLI Documentation
- Docker Build Documentation
- Docker Hub Documentation
- Docker Compose Documentation
- Docker Desktop Documentation

---

## OCI Standards

- Open Container Initiative (OCI) Image Specification
- Open Container Initiative (OCI) Runtime Specification
- Open Container Initiative (OCI) Distribution Specification

---

## Linux Documentation

- Linux Namespaces
- Linux cgroups
- OverlayFS
- Linux Capabilities

---

## CNCF Resources

- Cloud Native Computing Foundation (CNCF)
- Kubernetes Documentation
- containerd Documentation
- CRI-O Documentation

---

## Security Resources

- NIST SP 800-190 — Application Container Security Guide
- OWASP Docker Security Cheat Sheet
- OWASP Container Security Verification Standard
- CIS Docker Benchmark

---

## Books

- *Docker Deep Dive* — Nigel Poulton
- *Docker in Action* — Jeff Nickoloff & Stephen Kuenzli
- *Container Security* — Liz Rice
- *Kubernetes in Action* — Marko Lukša

---

## Recommended Learning Resources

- Docker Official Documentation
- Docker Labs
- Play with Docker
- Linux Foundation Training
- CNCF Learning Paths
- NIST Computer Security Resource Center (CSRC)

