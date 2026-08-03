# Chapter 6 – Dockerfile

## Overview

A **Dockerfile** is a text file containing a sequence of instructions used by Docker to automatically build a container image. It serves as the blueprint for creating reproducible, portable, and version-controlled container images.

Instead of manually installing operating systems, packages, dependencies, libraries, and applications each time a container is created, developers define the entire build process in a Dockerfile. Docker reads these instructions sequentially and produces an immutable image.

Dockerfiles are a fundamental component of:

- Docker
- Kubernetes
- DevOps
- DevSecOps
- CI/CD Pipelines
- Cloud-Native Applications
- Infrastructure as Code (IaC)

A well-designed Dockerfile produces images that are:

- Smaller
- Faster
- More secure
- Easier to maintain
- Highly reproducible

Understanding Dockerfiles is essential for building production-ready containerized applications.

---

# Why It Matters

Without Dockerfiles, application deployment would require manual installation of:

- Operating system packages
- Programming language runtimes
- Libraries
- Dependencies
- Configuration files
- Application code

Manual deployments are:

- Slow
- Error-prone
- Difficult to reproduce
- Hard to automate

Dockerfiles eliminate these problems by making image creation deterministic and repeatable.

Benefits include:

- Automated image creation
- Consistent environments
- Version-controlled builds
- Easy rollback
- CI/CD integration
- Infrastructure automation
- Improved collaboration

---

# What is a Dockerfile?

A Dockerfile is simply a plain text file.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
```

Docker processes each instruction from top to bottom to build the final image.

---

# Dockerfile Workflow

```
Developer

      │

Write Dockerfile

      │

Docker Build

      │

Execute Instructions

      │

Create Image Layers

      │

Generate Image

      │

Run Container
```

Each instruction contributes to the final image.

---

# Docker Build Process

```
Dockerfile

     │

FROM

     │

RUN

     │

COPY

     │

WORKDIR

     │

EXPOSE

     │

CMD

     │

Final Image
```

Docker executes instructions sequentially.

Most instructions create a new image layer.

---

# Dockerfile Structure

A typical Dockerfile consists of several sections.

```
Base Image

↓

Metadata

↓

Working Directory

↓

Dependencies

↓

Copy Files

↓

Environment Variables

↓

Expose Ports

↓

Startup Command
```

Not every Dockerfile requires every instruction, but this is a common structure.

---

# Dockerfile Instructions

## 1. FROM

The `FROM` instruction specifies the base image.

Example:

```dockerfile
FROM ubuntu:24.04
```

or

```dockerfile
FROM python:3.12
```

Every Dockerfile (except special multi-stage cases using `scratch`) begins with a `FROM` instruction.

---

## 2. LABEL

Adds metadata to an image.

Example:

```dockerfile
LABEL maintainer="security@example.com"

LABEL version="1.0"
```

Common uses:

- Author
- Version
- Description
- Project URL
- License

Labels improve image documentation and management.

---

## 3. WORKDIR

Sets the working directory.

Example:

```dockerfile
WORKDIR /app
```

All subsequent instructions execute relative to this directory.

Equivalent to running:

```bash
cd /app
```

inside the build environment.

---

## 4. COPY

Copies files from the build context into the image.

Example:

```dockerfile
COPY . .
```

or

```dockerfile
COPY requirements.txt .
```

Use `COPY` for local project files.

---

## 5. ADD

Similar to `COPY`, but with additional capabilities.

Example:

```dockerfile
ADD archive.tar.gz /app
```

Features:

- Extracts local tar archives automatically.
- Can fetch remote URLs (though this is generally discouraged for reproducibility).

For most use cases, prefer `COPY` because its behavior is more predictable.

---

## 6. RUN

Executes commands during the image build process.

Example:

```dockerfile
RUN apt update

RUN apt install -y nginx
```

or

```dockerfile
RUN pip install -r requirements.txt
```

Each `RUN` instruction typically creates a new image layer.

---

## 7. ENV

Defines environment variables.

Example:

```dockerfile
ENV APP_ENV=production

ENV PORT=8000
```

Applications can access these variables at runtime.

---

## 8. EXPOSE

Documents the network port used by the application.

Example:

```dockerfile
EXPOSE 80
```

or

```dockerfile
EXPOSE 8000
```

**Important:** `EXPOSE` does **not** publish the port to the host. Port publishing is performed when the container is started (for example, with `docker run -p`).

---

## 9. USER

Specifies the user that should run the application.

Example:

```dockerfile
USER appuser
```

Running applications as a non-root user is a recommended security practice.

---

## 10. CMD

Defines the default command executed when the container starts.

Example:

```dockerfile
CMD ["python", "app.py"]
```

Only one `CMD` instruction is effective in the final image. If multiple `CMD` instructions are present, the last one overrides the previous ones.

---

## 11. ENTRYPOINT

Specifies the primary executable for the container.

Example:

```dockerfile
ENTRYPOINT ["python"]
```

Combined with:

```dockerfile
CMD ["app.py"]
```

Docker executes:

```
python app.py
```

`ENTRYPOINT` is commonly used for containers that should always execute the same program.

---

# Common Dockerfile Instructions Summary

| Instruction | Purpose |
|-------------|---------|
| FROM | Select base image |
| LABEL | Add metadata |
| WORKDIR | Set working directory |
| COPY | Copy local files |
| ADD | Copy files and extract local archives |
| RUN | Execute build commands |
| ENV | Set environment variables |
| EXPOSE | Document application port |
| USER | Set execution user |
| CMD | Default startup command |
| ENTRYPOINT | Primary executable |

---

# Docker Image Layers

Each build instruction generally creates a layer.

```
CMD

──────────────

Application

──────────────

Dependencies

──────────────

Python Runtime

──────────────

Ubuntu Base
```

Benefits of layers:

- Faster builds
- Efficient storage
- Layer caching
- Incremental downloads

Changing one layer does not necessarily require rebuilding all previous layers.

---

# Key Concepts

## Immutable Builds

Docker images should be rebuilt rather than modified manually.

---

## Layer Caching

Docker caches unchanged layers to accelerate subsequent builds.

---

## Reproducibility

The same Dockerfile should produce equivalent images when built with the same inputs and dependencies.

---

## Version Control

Dockerfiles should be stored alongside application source code in version control systems such as Git.

---

## Automation

Dockerfiles integrate naturally with:

- CI/CD pipelines
- Automated testing
- Kubernetes deployments
- Infrastructure as Code workflows

---

## Portability

Images created from Dockerfiles can be deployed consistently across development, testing, and production environments.

---

## How It Works

A Dockerfile acts as a set of instructions that Docker follows to build a container image. During the build process, Docker reads the Dockerfile from top to bottom, executes each instruction, and creates a series of immutable image layers. The completed image can then be used to create one or more containers.

Docker also uses a **layer cache**, which means that unchanged instructions are reused during subsequent builds. This significantly reduces build time and improves development efficiency.

---

# Dockerfile Build Workflow

```
Application Source Code

          │

          ▼

Dockerfile

          │

          ▼

Docker Build

          │

          ▼

Read Instructions

          │

          ▼

Execute Each Instruction

          │

          ▼

Create Image Layers

          │

          ▼

Final Container Image

          │

          ▼

Run Container
```

Every successful build produces an immutable container image.

---

## Step 1 – Write the Dockerfile

The developer creates a file named:

```
Dockerfile
```

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

This file defines exactly how the image should be built.

---

## Step 2 – Execute Docker Build

The image is created using:

```bash
docker build -t myapp .
```

Docker performs the following operations:

```
Read Dockerfile

↓

Validate Instructions

↓

Download Base Image (if needed)

↓

Execute Commands

↓

Create Layers

↓

Generate Image
```

---

## Step 3 – Download the Base Image

Docker checks whether the base image already exists locally.

Example:

```dockerfile
FROM python:3.12
```

Workflow:

```
Base Image Exists?

        │

   ┌────┴────┐

   │         │

 Yes        No

   │         │

   ▼         ▼

Continue  Download Image

              │

              ▼

        Continue Build
```

Only missing base images are downloaded.

---

## Step 4 – Execute Each Instruction

Docker processes the Dockerfile sequentially.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]
```

Execution order:

```
FROM

↓

WORKDIR

↓

COPY

↓

RUN

↓

CMD
```

Each instruction builds upon the previous one.

---

## Step 5 – Create Image Layers

Most Dockerfile instructions create a new image layer.

Example:

```
CMD Layer

──────────────

Application Layer

──────────────

Dependencies Layer

──────────────

Python Runtime

──────────────

Ubuntu Base
```

Docker stores these layers independently.

Advantages:

- Layer reuse
- Smaller downloads
- Faster builds
- Efficient storage

---

## Step 6 – Use Build Cache

Docker compares each instruction with previous builds.

```
Instruction Changed?

       │

  ┌────┴─────┐

  │          │

 No         Yes

  │          │

Reuse Cache Rebuild Layer
```

Only changed layers (and those after them) are rebuilt.

Example:

If only the application source code changes:

```
Base Image

↓

Dependencies

↓

Application Layer ← Rebuilt

↓

CMD
```

The dependency layer is reused, making builds significantly faster.

---

## Step 7 – Generate the Final Image

After all instructions are processed:

```
Dockerfile

↓

Layers

↓

Final Image
```

The image becomes available locally and can be viewed using:

```bash
docker images
```

---

## Step 8 – Run the Image

The image can now be executed:

```bash
docker run myapp
```

Workflow:

```
Image

↓

Container

↓

Application Starts
```

Each container receives:

- Writable layer
- Isolated filesystem
- Networking
- Resource limits

The original image remains unchanged.

---

# Practical Examples

## Example 1 – Python Flask Application

Dockerfile:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

Workflow:

```
Python Base Image

↓

Install Dependencies

↓

Copy Application

↓

Create Image

↓

Run Container
```

The application behaves consistently across development and production.

---

## Example 2 – Nginx Web Server

Dockerfile:

```dockerfile
FROM nginx:1.27

COPY index.html /usr/share/nginx/html
```

Workflow:

```
Nginx Base Image

↓

Copy Website

↓

Create Image

↓

Run Container

↓

Website Available
```

This produces a customized Nginx image serving a static website.

---

## Example 3 – Java Application

```
Application

↓

Dockerfile

↓

OpenJDK Base Image

↓

Build Image

↓

Run Container
```

The Java application can now run identically on any Docker-enabled host.

---

## Example 4 – Multi-Layer Build

Dockerfile:

```dockerfile
FROM ubuntu:24.04

RUN apt update

RUN apt install -y python3

COPY . .

CMD ["python3", "app.py"]
```

Resulting layers:

```
CMD

──────────────

Application

──────────────

Python

──────────────

Ubuntu
```

Each layer is cached independently.

---

# Hands-on Commands

## Build an Image

```bash
docker build -t myapp .
```

Builds an image named **myapp** from the current directory.

---

## Build with a Tag

```bash
docker build -t myapp:v1 .
```

Assigns a version tag during the build.

---

## Use a Custom Dockerfile

```bash
docker build -f Dockerfile.prod -t myapp .
```

Builds using a specified Dockerfile.

---

## List Images

```bash
docker images
```

Displays all locally available images.

---

## Display Build History

```bash
docker history myapp
```

Shows image layers and the instructions that created them.

---

## Inspect the Image

```bash
docker inspect myapp
```

Displays detailed metadata, configuration, and layer information.

---

## Run the Image

```bash
docker run myapp
```

Creates and starts a container from the image.

---

## Tag an Image

```bash
docker tag myapp:v1 username/myapp:v1
```

Prepares the image for pushing to a registry.

---

## Push an Image

```bash
docker push username/myapp:v1
```

Uploads the tagged image to a registry.

---

# Best Practices

### 1. Choose Small Base Images

Prefer minimal, trusted base images whenever possible.

Examples:

- Alpine Linux
- Debian Slim
- Distroless
- Official language runtime images

Smaller images improve build speed and reduce the attack surface.

---

### 2. Order Instructions for Better Caching

Place instructions that change infrequently near the top of the Dockerfile.

Example:

```
FROM

↓

Install Dependencies

↓

Copy Application
```

Since application code changes more often than dependencies, this ordering maximizes cache reuse.

---

### 3. Combine Related `RUN` Instructions

Instead of:

```dockerfile
RUN apt update

RUN apt install -y curl
```

prefer:

```dockerfile
RUN apt update && apt install -y curl
```

Combining related commands reduces image layers and can simplify image management.

---

### 4. Prefer `COPY` Over `ADD`

Use `COPY` unless you specifically need `ADD` features such as automatic extraction of local tar archives.

`COPY` is generally more predictable and easier to understand.

---

### 5. Run as a Non-Root User

Use the `USER` instruction to execute the application with the least privileges required.

This reduces the impact of potential vulnerabilities.

---

### 6. Pin Base Image Versions

Instead of:

```dockerfile
FROM python:latest
```

prefer:

```dockerfile
FROM python:3.12
```

Explicit versions improve reproducibility and prevent unexpected changes.

---

### 7. Keep Dockerfiles Readable

Use logical ordering, comments where appropriate, and consistent formatting.

A well-structured Dockerfile is easier to review, maintain, and troubleshoot.

---

