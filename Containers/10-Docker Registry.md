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

