# Chapter 7 – Docker Compose

## Overview

Docker Compose is a tool for defining and managing **multi-container Docker applications** using a single YAML configuration file called `compose.yaml` (or the legacy name `docker-compose.yml`). Instead of starting individual containers manually, Docker Compose allows developers to describe an entire application stack—including services, networks, volumes, environment variables, and dependencies—in one file.

With a single command, Docker Compose can:

- Build images
- Create networks
- Create volumes
- Start multiple containers
- Stop applications
- Restart services
- Scale selected services (where supported)
- Simplify local development and testing

Docker Compose is widely used in:

- Local Development
- DevOps
- CI/CD Pipelines
- Microservices
- API Development
- Testing Environments
- Demonstration Environments

While Docker Compose is primarily intended for single-host environments, many of its concepts map directly to container orchestration platforms such as Kubernetes.

---

# Why It Matters

Modern applications rarely consist of a single container.

Consider an e-commerce application:

```
Frontend

↓

Backend API

↓

Authentication Service

↓

Redis Cache

↓

PostgreSQL Database

↓

Message Queue
```

Without Docker Compose, each container would need to be started individually, requiring manual configuration of:

- Networks
- Volumes
- Environment variables
- Port mappings
- Startup order

Docker Compose automates this process and ensures that every developer works with the same application configuration.

Benefits include:

- Simpler deployments
- Reproducible environments
- Reduced manual configuration
- Easier collaboration
- Faster onboarding
- Improved developer productivity

---

# What is Docker Compose?

Docker Compose is a declarative configuration tool.

Instead of executing many Docker commands manually:

```bash
docker network create

docker volume create

docker run ...

docker run ...

docker run ...
```

you define everything in one YAML file.

Example:

```yaml
services:
  web:
    image: nginx

  database:
    image: postgres
```

Then start the application using:

```bash
docker compose up
```

Docker Compose creates and manages the complete application stack automatically.

---

# Docker Compose Architecture

```
Developer

      │

compose.yaml

      │

docker compose

      │

Docker Engine

      │

 ┌────┼───────────┐

 ▼    ▼           ▼

Services Networks Volumes

      │

      ▼

Running Containers
```

The Compose CLI communicates with the Docker Engine, which creates the required Docker objects.

---

# Docker Compose Workflow

```
Developer

      │

Write compose.yaml

      │

docker compose up

      │

Create Networks

      │

Create Volumes

      │

Create Containers

      │

Start Services

      │

Application Ready
```

This workflow replaces multiple manual Docker commands.

---

# Docker Compose File

Modern Docker Compose uses:

```
compose.yaml
```

Legacy projects may still use:

```
docker-compose.yml
```

Both names are commonly recognized, but the modern convention is `compose.yaml`.

---

# Compose File Structure

A Compose file typically contains:

```
Services

↓

Networks

↓

Volumes

↓

Environment Variables

↓

Configurations
```

Not every project requires every section.

---

# Services

A **service** defines a containerized application.

Example:

```yaml
services:

  web:

    image: nginx
```

Each service becomes one or more containers.

Examples:

- Web Server
- API
- Database
- Redis
- Message Queue

---

# Image

A service can reference an existing image.

Example:

```yaml
services:

  web:

    image: nginx:1.27
```

Docker downloads the image if it is not already available locally.

---

# Build

Instead of downloading an image, Docker Compose can build one.

Example:

```yaml
services:

  api:

    build: .
```

Compose reads the Dockerfile and builds the image before starting the container.

---

# Ports

Expose container ports.

Example:

```yaml
ports:

  - "8080:80"
```

Meaning:

```
Host

8080

 │

 ▼

Container

80
```

---

# Environment Variables

Example:

```yaml
environment:

  APP_ENV: production

  PORT: 8000
```

Environment variables configure application behavior without modifying the image.

---

# Volumes

Persistent storage:

```yaml
volumes:

  - postgres_data:/var/lib/postgresql/data
```

Benefits:

- Data persistence
- Easier backups
- Container replacement without data loss

---

# Networks

Docker Compose automatically creates a default network.

Custom example:

```yaml
networks:

  backend:
```

Containers attached to the same network can communicate securely using service names.

---

# Restart Policy

Example:

```yaml
restart: always
```

Common options:

- `no`
- `on-failure`
- `unless-stopped`
- `always`

Restart policies improve application availability.

---

# Depends On

Example:

```yaml
depends_on:

  - database
```

This expresses a startup dependency between services.

**Important:** `depends_on` controls startup order but does **not** guarantee that the dependent service is fully initialized or ready to accept connections.

---

# Complete Example

```yaml
services:

  web:

    image: nginx

    ports:

      - "8080:80"

  database:

    image: postgres

    environment:

      POSTGRES_PASSWORD: password

    volumes:

      - db_data:/var/lib/postgresql/data

volumes:

  db_data:
```

This configuration launches:

- Nginx
- PostgreSQL
- Persistent storage

using a single Compose file.

---

# Docker Compose Lifecycle

```
compose.yaml

      │

docker compose up

      │

Create Objects

      │

Start Services

      │

Application Running

      │

docker compose down

      │

Stop Containers

      │

Remove Network
```

Volumes are preserved by default unless explicitly removed.

---

# Key Concepts

## Declarative Configuration

Compose describes the desired application state instead of requiring manual commands.

---

## Multi-Container Applications

One Compose file can define an entire application stack.

---

## Service Discovery

Containers on the same Compose network can communicate using service names instead of IP addresses.

Example:

```
Web Service

↓

database

↓

PostgreSQL
```

No manual IP configuration is required.

---

## Portability

Compose files can be shared through version control, enabling consistent development environments.

---

## Automation

Compose integrates naturally with:

- Development workflows
- Automated testing
- CI/CD pipelines
- Local demonstrations

---
