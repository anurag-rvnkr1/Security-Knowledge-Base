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

