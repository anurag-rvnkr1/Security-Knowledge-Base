# Chapter 10 – Docker Registry & Docker Hub

## Overview

A **Docker Registry** is a storage and distribution system for container images. Instead of manually copying images between systems, Docker registries provide a centralized repository where images can be stored, versioned, shared, and retrieved.

Whenever you execute a command such as:

```bash
docker pull nginx
```

or

```bash
docker push username/myapp:v1
```

Docker communicates with a registry.

The most widely used public registry is **Docker Hub**, but organizations also deploy private registries for internal applications and confidential workloads.

Docker registries play a critical role in:

- DevOps
- DevSecOps
- CI/CD Pipelines
- Kubernetes
- Cloud Computing
- Microservices
- Enterprise Software Delivery

Without registries, distributing container images across development, testing, and production environments would be extremely difficult.

---

# Why It Matters

Consider a software development team.

```
Developer

↓

Build Image

↓

Registry

↓

Testing

↓

Production
```

Instead of rebuilding the application on every server, a single image is built once and stored in a registry.

Every environment retrieves the exact same image.

Benefits include:

- Consistency
- Faster deployments
- Version control
- Simplified collaboration
- Easier rollback
- Centralized image management

---

# What is a Docker Registry?

A Docker Registry stores container images.

```
Image

↓

Push

↓

Registry

↓

Pull

↓

Container
```

A registry provides:

- Image storage
- Image distribution
- Version management
- Access control
- Authentication
- Image metadata

Registries can be:

- Public
- Private
- Self-hosted
- Cloud-managed

---

# Docker Hub

Docker Hub is Docker's official public registry.

It provides:

- Official images
- Community images
- Private repositories
- Public repositories
- Automated builds (depending on plan/features)
- Team collaboration

Example:

```bash
docker pull ubuntu
```

Docker automatically downloads the Ubuntu image from Docker Hub if it is not available locally.

---

# Registry Architecture

```
Developer

      │

docker push

      │

Registry

      │

docker pull

      │

Developer

      │

Production

      │

Kubernetes
```

The registry serves as the central source of container images.

---

# Registry Workflow

```
Dockerfile

      │

docker build

      │

Container Image

      │

docker tag

      │

docker push

      │

Registry

      │

docker pull

      │

Run Container
```

The registry becomes the distribution point for application images.

---

# Public Registries

Common public registries include:

| Registry | Provider |
|----------|----------|
| Docker Hub | Docker |
| GitHub Container Registry (GHCR) | GitHub |
| Amazon Elastic Container Registry (ECR) | AWS |
| Azure Container Registry (ACR) | Microsoft Azure |
| Google Artifact Registry | Google Cloud |
| Quay | Red Hat |

Public registries are often used for open-source software and publicly available images.

---

# Private Registries

Organizations frequently use private registries.

Advantages:

- Internal applications
- Better security
- Controlled access
- Regulatory compliance
- Enterprise governance

Private registries help protect proprietary software and sensitive workloads.

---

# Repository

A repository stores related versions of an image.

Example:

```
myapp

↓

v1

↓

v2

↓

v3
```

Each version is identified by a tag.

---

# Image Tags

Tags identify specific image versions.

Example:

```
myapp:1.0

myapp:2.0

myapp:3.0
```

Avoid relying solely on:

```
latest
```

Versioned tags provide predictable deployments and easier rollback.

---

# Image Digest

Every image also has a unique cryptographic digest.

Example:

```
sha256:xxxxxxxx...
```

A digest uniquely identifies the image content.

Unlike tags, a digest does not change for the same image.

Digests are useful when exact image integrity is required.

---

# Authentication

Before pushing images:

```bash
docker login
```

Docker authenticates with the registry.

Example workflow:

```
Username

↓

Password or Access Token

↓

Registry

↓

Authenticated Session
```

Many registries now recommend personal access tokens instead of passwords.

---

# Image Lifecycle

```
Dockerfile

      │

Build

      │

Image

      │

Tag

      │

Push

      │

Registry

      │

Pull

      │

Run
```

This lifecycle enables consistent software delivery across environments.

---

# Registry vs Repository

| Registry | Repository |
|-----------|------------|
| Stores many repositories | Stores related image versions |
| Example: Docker Hub | Example: nginx |
| Enterprise service | Individual project |

Example:

```
Docker Hub

↓

nginx

↓

1.27

↓

1.28

↓

latest
```

---

# Key Concepts

## Centralized Image Storage

Registries provide a single location for storing and distributing container images.

---

## Version Control

Tags and digests help manage image versions and support controlled deployments.

---

## Image Distribution

Registries allow developers, CI/CD systems, and production environments to retrieve identical images.

---

## Security

Authentication and authorization help protect private images from unauthorized access.

---

## Portability

Container images can be pulled from registries and executed on any compatible Docker environment.

---

## Integration

Registries integrate seamlessly with:

- Docker
- Docker Compose
- Kubernetes
- CI/CD pipelines
- Cloud platforms

---

## How It Works

A Docker Registry acts as a centralized image repository that enables developers, CI/CD systems, testing environments, and production servers to share the same container images. Instead of rebuilding applications on every machine, an image is built once, uploaded (pushed) to a registry, and later downloaded (pulled) wherever it is needed.

Docker automatically communicates with registries whenever image-related commands such as `docker pull`, `docker push`, or `docker search` are executed.

---

# Docker Registry Workflow

```
Application Source Code

          │

          ▼

Dockerfile

          │

          ▼

docker build

          │

          ▼

Container Image

          │

          ▼

docker tag

          │

          ▼

docker login

          │

          ▼

docker push

          │

          ▼

Docker Registry

          │

          ▼

docker pull

          │

          ▼

Run Container
```

The registry serves as the central distribution point for container images.

---

# Step 1 – Build the Image

A developer builds the application image.

Example:

```bash
docker build -t myapp:v1 .
```

Workflow:

```
Dockerfile

↓

Docker Build

↓

Container Image
```

The image is stored locally after the build completes.

---

# Step 2 – Tag the Image

Before uploading, the image is tagged with the registry and repository information.

Example:

```bash
docker tag myapp:v1 username/myapp:v1
```

Structure:

```
Registry

↓

Repository

↓

Tag
```

Example:

```
docker.io/anurag/myapp:v1
```

Tags identify different versions of an image.

---

# Step 3 – Authenticate

Before pushing images to a private repository:

```bash
docker login
```

Workflow:

```
Username

↓

Access Token / Password

↓

Registry

↓

Authenticated
```

After successful authentication, Docker stores credentials securely according to the configured credential helper or local configuration.

---

# Step 4 – Push the Image

Example:

```bash
docker push username/myapp:v1
```

Workflow:

```
Local Image

↓

Upload Layers

↓

Registry

↓

Image Stored
```

Docker uploads only the layers that are not already present in the registry.

This reduces upload time and bandwidth usage.

---

# Step 5 – Store Image Layers

Container images are layer-based.

Example:

```
Application

────────────

Dependencies

────────────

Python Runtime

────────────

Ubuntu Base
```

The registry stores each layer separately.

If another image already contains the Ubuntu base layer, Docker reuses it instead of uploading it again.

Benefits:

- Reduced storage
- Faster uploads
- Faster downloads

---

# Step 6 – Pull the Image

Another system downloads the image.

Example:

```bash
docker pull username/myapp:v1
```

Workflow:

```
Registry

↓

Download Missing Layers

↓

Assemble Image

↓

Store Locally
```

Docker downloads only layers that are not already available locally.

---

# Step 7 – Run the Image

After downloading:

```bash
docker run username/myapp:v1
```

Workflow:

```
Image

↓

Container

↓

Application Running
```

Every environment now runs the exact same application image.

---

# Step 8 – Version Management

Suppose a new release is created.

```
myapp:v1

↓

myapp:v2

↓

myapp:v3
```

Each version remains available.

Rollback becomes simple:

```bash
docker pull username/myapp:v1
```

---

# Step 9 – CI/CD Integration

Modern CI/CD pipelines automate the registry workflow.

```
Git Push

↓

CI Pipeline

↓

Build Image

↓

Run Tests

↓

Security Scan

↓

Push Registry

↓

Deployment

↓

Production
```

The registry becomes the single source of truth for application images.

---

# Practical Examples

## Example 1 – Uploading an Nginx Image

Commands:

```bash
docker pull nginx

docker tag nginx username/nginx-demo:v1

docker push username/nginx-demo:v1
```

Workflow:

```
Docker Hub

↓

Local Image

↓

Retag

↓

Push

↓

Personal Repository
```

---

## Example 2 – Team Collaboration

Developer A:

```
Build Image

↓

Push Registry
```

Developer B:

```
Pull Image

↓

Run Application
```

Both developers work with the same application version.

---

## Example 3 – Production Deployment

```
Developer

↓

Registry

↓

Kubernetes

↓

Production Pods
```

Kubernetes pulls the image directly from the registry during deployment.

---

## Example 4 – Image Rollback

Suppose version 3 introduces a bug.

```
v3

↓

Issue Found

↓

Deploy v2

↓

Application Restored
```

Image versioning simplifies rollback procedures.

---

# Hands-on Commands

## Login

```bash
docker login
```

Authenticates with a registry.

---

## Logout

```bash
docker logout
```

Ends the authenticated session.

---

## Search Images

```bash
docker search nginx
```

Searches Docker Hub for available images.

---

## Pull an Image

```bash
docker pull nginx
```

Downloads the latest Nginx image.

---

## Pull a Specific Version

```bash
docker pull nginx:1.27
```

Downloads a specific tagged version.

---

## Tag an Image

```bash
docker tag nginx username/nginx:v1
```

Creates a new image tag.

---

## Push an Image

```bash
docker push username/nginx:v1
```

Uploads the tagged image to the registry.

---

## View Local Images

```bash
docker images
```

Lists images stored locally.

---

## Inspect an Image

```bash
docker inspect nginx
```

Displays image metadata, tags, layers, and configuration.

---

## Remove an Image

```bash
docker rmi nginx
```

Deletes the local copy of the image.

---

# Best Practices

### 1. Use Versioned Tags

Instead of:

```
latest
```

prefer:

```
1.0

1.1

2.0
```

Versioned tags make deployments predictable and simplify rollbacks.

---

### 2. Authenticate Securely

Use:

- Personal Access Tokens (PATs)
- Short-lived credentials
- Cloud IAM integration (where available)

Avoid embedding passwords in scripts or configuration files.

---

### 3. Keep Images Small

Smaller images:

- Upload faster
- Download faster
- Consume less storage
- Reduce the attack surface

---

### 4. Scan Images Before Pushing

Integrate vulnerability scanning into the build pipeline before publishing images to a registry.

---

### 5. Remove Old Image Versions

Regularly clean unused or obsolete image tags to reduce storage consumption and simplify repository management.

---

### 6. Protect Private Repositories

Apply the principle of least privilege:

- Limit push permissions
- Separate developer and deployment roles
- Enable multi-factor authentication where supported

---

### 7. Integrate Registries with CI/CD

Automate:

- Build
- Test
- Security scan
- Push
- Deployment

This ensures consistent, repeatable software delivery.

---

