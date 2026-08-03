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

## How It Works

Docker Compose automates the deployment and management of multi-container applications. Instead of manually creating networks, volumes, and containers one at a time, Docker Compose reads a declarative YAML configuration file and performs all required operations automatically.

When the command:

```bash
docker compose up
```

is executed, Docker Compose:

1. Reads the Compose file.
2. Validates the configuration.
3. Builds images (if required).
4. Pulls missing images.
5. Creates networks.
6. Creates volumes.
7. Creates containers.
8. Starts services.
9. Connects services together.

This allows an entire application stack to be deployed using a single command.

---

# Docker Compose Workflow

```
compose.yaml

       │

       ▼

docker compose up

       │

Read Configuration

       │

Build Images (Optional)

       │

Pull Images (If Needed)

       │

Create Networks

       │

Create Volumes

       │

Create Containers

       │

Start Services

       │

Application Running
```

Each stage is handled automatically by Docker Compose.

---

## Step 1 – Read the Compose File

Docker Compose first searches for:

```
compose.yaml
```

(or the legacy `docker-compose.yml`)

The YAML file describes:

- Services
- Networks
- Volumes
- Environment variables
- Restart policies
- Dependencies

Compose validates the syntax before proceeding.

---

## Step 2 – Build or Pull Images

For each service:

```
Image Specified?

      │

 ┌────┴─────┐

 │          │

Yes        No

 │          │

 ▼          ▼

Pull      Build
Image     Image
```

Example:

```yaml
services:

  api:

    build: .
```

Docker builds the image from the Dockerfile.

Example:

```yaml
services:

  web:

    image: nginx
```

Docker downloads the image if it is not available locally.

---

## Step 3 – Create Networks

Docker Compose creates a default network automatically.

```
Compose Network

        │

 ┌──────┼────────┐

 ▼      ▼        ▼

Web     API   Database
```

Every service joins this network unless configured otherwise.

Services communicate using service names.

Example:

```
database

instead of

172.18.0.4
```

This greatly simplifies service communication.

---

## Step 4 – Create Volumes

Persistent volumes are created before containers start.

Example:

```yaml
volumes:

  db_data:
```

Workflow:

```
Volume

     │

Database Container

     │

Persistent Storage
```

Data remains available even if the container is recreated.

---

## Step 5 – Create Containers

Compose creates containers for every defined service.

Example:

```
compose.yaml

↓

Web Service

↓

Database Service

↓

Redis Service

↓

Worker Service
```

Each service becomes one or more Docker containers.

---

## Step 6 – Configure Networking

Compose automatically:

- Assigns IP addresses
- Configures DNS
- Creates routing
- Connects containers

Example:

```
Web

 │

 ▼

API

 │

 ▼

Database
```

Containers communicate using service names.

---

## Step 7 – Apply Environment Variables

Compose injects configured environment variables.

Example:

```yaml
environment:

  APP_ENV: production
```

The application reads:

```
APP_ENV=production
```

during startup.

Environment variables allow the same image to behave differently across environments.

---

## Step 8 – Start Services

Docker starts every container.

```
Database

↓

API

↓

Web
```

If dependencies are defined:

```yaml
depends_on:
  - database
```

Docker Compose starts the database container before the API container.

Remember that this controls startup order but does not ensure application readiness.

---

## Step 9 – Monitor Running Services

The application stack remains active.

Useful commands:

```bash
docker compose ps

docker compose logs

docker compose top
```

These commands provide visibility into running services.

---

# Practical Examples

## Example 1 – Web Server + Database

Compose file:

```yaml
services:

  web:

    image: nginx

  database:

    image: postgres
```

Deployment:

```
docker compose up

↓

Nginx Running

↓

PostgreSQL Running

↓

Shared Network
```

Both services can communicate immediately.

---

## Example 2 – Flask + Redis

```
Flask

↓

Redis

↓

Compose Network

↓

Application Running
```

The Flask application connects to Redis using:

```
redis
```

instead of an IP address.

---

## Example 3 – Development Environment

One Compose file launches:

```
Frontend

↓

Backend

↓

Database

↓

Redis

↓

RabbitMQ
```

Every developer starts the complete environment using:

```bash
docker compose up
```

No manual configuration is required.

---

## Example 4 – Local Testing

Before deploying to production:

```
Git Clone

↓

docker compose up

↓

Entire Stack Ready
```

Compose enables consistent local testing that closely mirrors production architecture.

---

# Hands-on Commands

## Start Services

```bash
docker compose up
```

Creates and starts the application stack.

---

## Start in Detached Mode

```bash
docker compose up -d
```

Runs all services in the background.

---

## Stop Services

```bash
docker compose stop
```

Stops running containers without removing them.

---

## Restart Services

```bash
docker compose restart
```

Restarts all services.

---

## View Running Services

```bash
docker compose ps
```

Lists Compose-managed containers.

---

## View Logs

```bash
docker compose logs
```

Displays logs from all services.

---

## Follow Logs

```bash
docker compose logs -f
```

Streams logs in real time.

---

## Build Images

```bash
docker compose build
```

Builds images for services using the `build` directive.

---

## Pull Images

```bash
docker compose pull
```

Downloads newer versions of referenced images.

---

## Remove the Stack

```bash
docker compose down
```

Stops containers and removes:

- Containers
- Networks

Volumes are retained by default.

---

## Remove Everything Including Volumes

```bash
docker compose down -v
```

Also removes named volumes.

Use this carefully because persistent data will be deleted.

---

## Best Practices

### 1. Store the Compose File in Version Control

Treat `compose.yaml` as application infrastructure code.

Track changes using Git alongside the application source code.

---

### 2. Use Service Names for Communication

Instead of hardcoding IP addresses:

```
database
```

is preferable to:

```
172.18.0.4
```

Docker Compose provides automatic DNS resolution between services.

---

### 3. Separate Configuration from Images

Use:

- Environment variables
- `.env` files
- Secrets management

instead of modifying images for different environments.

---

### 4. Use Named Volumes for Persistent Data

Applications such as PostgreSQL, MySQL, and Redis should store important data in named volumes rather than the container filesystem.

---

### 5. Pin Image Versions

Instead of:

```yaml
image: postgres:latest
```

prefer:

```yaml
image: postgres:17
```

Version pinning provides reproducible deployments.

---

### 6. Organize Large Compose Files

Group related configuration logically:

- Services
- Networks
- Volumes
- Environment variables

Consistent formatting improves readability and maintainability.

---

### 7. Validate Before Deployment

Before deploying, verify:

- YAML syntax
- Image tags
- Port mappings
- Volume definitions
- Environment variables
- Network configuration

Validation reduces deployment failures.

---

