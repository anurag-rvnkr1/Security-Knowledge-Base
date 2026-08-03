# Chapter 19 – Hands-on Labs

# Overview

Theory alone is not enough to become proficient with containers. The best way to understand Docker and container security is by building, breaking, securing, troubleshooting, and recovering real applications.

This chapter provides practical labs that simulate real-world scenarios encountered by:

- Docker Developers
- DevOps Engineers
- DevSecOps Engineers
- Cloud Engineers
- Platform Engineers
- Security Engineers
- Site Reliability Engineers (SRE)
- SOC Analysts

Each lab builds upon previous concepts, progressing from beginner to advanced topics.

---

# Lab Environment

## Recommended Host

| Component | Recommendation |
|-----------|----------------|
| Operating System | Ubuntu 22.04+ / Debian 12+ / Fedora / macOS / Windows (WSL2) |
| RAM | Minimum 8 GB (16 GB Recommended) |
| CPU | 4 Cores or More |
| Disk Space | 40 GB Free |
| Docker | Latest Stable Version |
| Docker Compose | Latest Version |
| Git | Latest Version |

---

# Skills Covered

After completing these labs, you should be comfortable with:

- Docker CLI
- Image Building
- Dockerfile
- Multi-stage Builds
- Docker Compose
- Networking
- Volumes
- Registry
- Container Security
- Vulnerability Scanning
- Monitoring
- Logging
- Incident Response
- Forensics
- Troubleshooting

---

# Lab Structure

Each lab follows the same structure.

```
Objective

↓

Prerequisites

↓

Architecture

↓

Steps

↓

Verification

↓

Expected Outcome

↓

Cleanup

↓

Challenge Exercise
```

---

# Lab 1 – Your First Container

## Objective

Run your first Docker container.

---

## Architecture

```
Docker Engine

↓

Nginx Image

↓

Running Container

↓

Browser
```

---

## Steps

Pull the image:

```bash
docker pull nginx
```

Run the container:

```bash
docker run -d -p 8080:80 --name web nginx
```

Verify:

```bash
docker ps
```

Open:

```
http://localhost:8080
```

---

## Expected Outcome

You should see the default Nginx welcome page.

---

## Verification

```bash
docker logs web
```

---

## Cleanup

```bash
docker stop web

docker rm web
```

---

## Challenge

Run two Nginx containers simultaneously using different host ports.

---

# Lab 2 – Build Your First Docker Image

## Objective

Create and build a custom Docker image.

---

## Project Structure

```
project/

│

├── Dockerfile

└── index.html
```

---

## Dockerfile

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

---

## Build

```bash
docker build -t mywebsite:v1 .
```

---

## Run

```bash
docker run -d -p 8080:80 mywebsite:v1
```

---

## Verify

Visit:

```
http://localhost:8080
```

---

## Cleanup

```bash
docker stop <container_id>

docker rm <container_id>
```

---

## Challenge

Add custom CSS and images to the website.

---

# Lab 3 – Docker Volumes

## Objective

Understand persistent storage.

---

## Architecture

```
Container

↓

Docker Volume

↓

Persistent Data
```

---

## Steps

Create a volume:

```bash
docker volume create mydata
```

Run:

```bash
docker run -it --rm \
-v mydata:/data \
ubuntu bash
```

Inside the container:

```bash
echo "Docker Lab" > /data/test.txt
```

Exit the container.

Start another container using the same volume.

Verify:

```bash
cat /data/test.txt
```

---

## Expected Outcome

The file should still exist.

---

## Cleanup

```bash
docker volume rm mydata
```

---

## Challenge

Create multiple containers sharing the same volume.

---

# Lab 4 – Docker Networking

## Objective

Connect multiple containers.

---

## Architecture

```
Bridge Network

↓

Web Container

↓

Database Container
```

---

## Steps

Create network:

```bash
docker network create labnet
```

Run:

```bash
docker run -d --network labnet --name web nginx
```

Run another container:

```bash
docker run -it --network labnet ubuntu bash
```

Install networking tools if required by your chosen image or use an image that already includes them.

Test connectivity:

```bash
ping web
```

---

## Expected Outcome

Containers communicate using container names.

---

## Cleanup

```bash
docker network rm labnet
```

---

## Challenge

Add a third container.

---

# Lab 5 – Docker Compose

## Objective

Deploy a multi-container application.

---

## Architecture

```
Docker Compose

↓

Web

↓

Database
```

---

## docker-compose.yml

```yaml
services:

  web:
    image: nginx

  db:
    image: postgres
```

---

## Start

```bash
docker compose up -d
```

---

## Verify

```bash
docker compose ps
```

---

## Cleanup

```bash
docker compose down
```

---

## Challenge

Add Redis to the stack.

---

# Lab 6 – Image Versioning

## Objective

Understand image tags.

---

Build:

```bash
docker build -t myapp:v1 .
```

Modify your application.

Build:

```bash
docker build -t myapp:v2 .
```

List:

```bash
docker images
```

---

## Expected Outcome

Two different versions should be available.

---

## Challenge

Roll back from v2 to v1.

---

# Lab 7 – Container Logs

## Objective

View application logs.

---

Run:

```bash
docker logs container_name
```

Stream:

```bash
docker logs -f container_name
```

---

## Challenge

Generate application activity and observe log output in real time.

---

# Lab 8 – Container Monitoring

## Objective

Monitor resource usage.

---

Run:

```bash
docker stats
```

Observe:

- CPU
- Memory
- Network
- Block I/O

---

## Challenge

Run multiple containers and compare their resource consumption.

---

# Lab 9 – Container Cleanup

## Objective

Remove unused resources.

---

Commands:

```bash
docker container prune

docker image prune

docker volume prune

docker network prune

docker system prune
```

---

## Challenge

Determine how much disk space is reclaimed after cleanup.

---

# Lab 10 – Container Security Basics

## Objective

Build a more secure image.

---

Example Dockerfile:

```dockerfile
FROM python:3.12-slim

RUN useradd appuser

USER appuser

WORKDIR /app

COPY . .

CMD ["python","app.py"]
```

---

## Verify

Inspect:

```bash
docker inspect image_name
```

Confirm the image is configured to run as the non-root user.

---

## Challenge

Compare this image with one that runs as root and identify the security differences.

---

# Summary

After completing these ten foundational labs, you will have practical experience with:

- Running containers
- Building images
- Creating Dockerfiles
- Using volumes
- Configuring networks
- Deploying multi-container applications
- Versioning images
- Viewing logs
- Monitoring containers
- Applying basic security practices

---


# Intermediate Hands-on Labs

These labs move beyond basic Docker usage and focus on real-world engineering practices. They introduce image optimization, security scanning, networking, registries, monitoring, troubleshooting, and production-ready workflows.

---

# Lab 11 – Multi-Stage Docker Build

## Objective

Reduce image size using multi-stage builds.

---

## Architecture

```
Source Code

↓

Build Stage

↓

Compiled Application

↓

Runtime Stage

↓

Small Production Image
```

---

## Example Dockerfile

```dockerfile
# Build Stage
FROM golang:1.24 AS builder

WORKDIR /app

COPY . .

RUN go build -o app

# Runtime Stage
FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/app .

CMD ["./app"]
```

---

## Build

```bash
docker build -t go-app:v1 .
```

---

## Verify

```bash
docker images
```

Compare the image size with a single-stage build.

---

## Expected Outcome

- Smaller image
- Faster deployment
- Reduced attack surface

---

## Challenge

Create a multi-stage Dockerfile for a Node.js or Python application.

---

# Lab 12 – Docker Image Scanning

## Objective

Scan container images for vulnerabilities.

---

## Architecture

```
Docker Image

↓

Security Scanner

↓

CVE Report

↓

Remediation
```

---

## Example (Docker Scout)

```bash
docker scout quickview nginx:latest
```

---

## Example (Trivy)

```bash
trivy image nginx:latest
```

---

## Verify

Review:

- Critical vulnerabilities
- High vulnerabilities
- Package versions
- Suggested fixes

---

## Challenge

Compare scan results for two different base images.

---

# Lab 13 – Custom Docker Network

## Objective

Create an isolated application network.

---

## Steps

Create network:

```bash
docker network create secure-net
```

Run:

```bash
docker run -d \
--network secure-net \
--name web nginx
```

Run another container:

```bash
docker run -it \
--network secure-net \
ubuntu bash
```

Verify communication between containers using appropriate networking tools.

---

## Expected Outcome

Containers communicate only within the custom network unless additional networking is configured.

---

## Challenge

Add three containers to the same network and verify connectivity.

---

# Lab 14 – Bind Mounts

## Objective

Share files between the host and a container.

---

## Architecture

```
Host Directory

↓

Bind Mount

↓

Container
```

---

## Example

```bash
docker run -it \
-v $(pwd):/workspace \
ubuntu bash
```

Create a file inside:

```bash
echo "Hello Docker" > /workspace/test.txt
```

Verify that the file appears in the host directory.

---

## Challenge

Modify the file from the host and verify the changes inside the container.

---

# Lab 15 – Environment Variables

## Objective

Pass configuration securely to a container.

---

## Run

```bash
docker run \
-e APP_ENV=production \
-e PORT=8080 \
nginx
```

---

## Verify

```bash
docker inspect container_name
```

Review configured environment variables.

---

## Challenge

Use an `.env` file with Docker Compose.

---

# Lab 16 – Restart Policies

## Objective

Configure automatic restart behavior.

---

## Run

```bash
docker run \
--restart unless-stopped \
nginx
```

Other restart policies include:

- `no`
- `on-failure`
- `always`
- `unless-stopped`

---

## Verify

```bash
docker inspect container_name
```

Review the restart policy.

---

## Challenge

Compare different restart policies in a test environment.

---

# Lab 17 – Health Checks

## Objective

Monitor container health.

---

## Example Dockerfile

```dockerfile
HEALTHCHECK \
CMD curl --fail http://localhost/ || exit 1
```

---

## Verify

```bash
docker ps
```

or

```bash
docker inspect container_name
```

Review health status.

---

## Expected Outcome

The container reports a health status such as:

- starting
- healthy
- unhealthy

---

## Challenge

Create a health check for your own application.

---

# Lab 18 – Image Versioning

## Objective

Practice image tagging.

---

## Build

```bash
docker build -t myapp:v1 .
```

Modify the application.

```bash
docker build -t myapp:v2 .
```

Tag latest version:

```bash
docker tag myapp:v2 myapp:latest
```

---

## Verify

```bash
docker images
```

---

## Challenge

Deploy different versions simultaneously on different ports.

---

# Lab 19 – Docker Registry

## Objective

Push an image to a registry.

---

## Tag

```bash
docker tag myapp:v1 username/myapp:v1
```

---

## Login

```bash
docker login
```

---

## Push

```bash
docker push username/myapp:v1
```

---

## Verify

Pull the image from another machine or environment if available.

---

## Challenge

Create multiple version tags and test pulling specific versions.

---

# Lab 20 – Docker Compose Application

## Objective

Deploy a three-tier application.

---

## Architecture

```
Browser

↓

Frontend

↓

Backend

↓

Database
```

---

## Example Compose File

```yaml
services:

  frontend:
    image: nginx

  backend:
    image: node:22

  database:
    image: postgres
```

---

## Start

```bash
docker compose up -d
```

---

## Verify

```bash
docker compose ps
```

---

## Challenge

Add Redis to the application stack.

---

# Lab 21 – Log Analysis

## Objective

Investigate application logs.

---

## Commands

```bash
docker logs container_name

docker logs -f container_name
```

---

## Tasks

- Generate requests
- Observe log entries
- Identify errors
- Verify timestamps

---

## Challenge

Simulate an application error and locate it in the logs.

---

# Lab 22 – Container Monitoring

## Objective

Monitor multiple running containers.

---

## Commands

```bash
docker stats
```

Observe:

- CPU
- Memory
- Network I/O
- Block I/O

---

## Challenge

Identify the container consuming the most resources.

---

# Lab 23 – Resource Limits

## Objective

Run containers with CPU and memory limits.

---

## Example

```bash
docker run \
--memory=512m \
--cpus=1 \
nginx
```

---

## Verify

```bash
docker inspect container_name
```

Review configured resource limits.

---

## Challenge

Run two containers with different resource limits and compare their behavior under load.

---

# Lab 24 – Image Cleanup

## Objective

Manage Docker storage efficiently.

---

## Commands

List disk usage:

```bash
docker system df
```

Clean up:

```bash
docker system prune
```

---

## Verify

Compare disk usage before and after cleanup.

---

## Challenge

Remove only unused images while preserving active containers.

---

# Lab 25 – Secure Dockerfile Review

## Objective

Review an insecure Dockerfile and improve it.

---

### Insecure Example

```dockerfile
FROM ubuntu

USER root

COPY . .

CMD ["python","app.py"]
```

---

### Improvements

- Use a minimal base image.
- Create and use a non-root user.
- Remove unnecessary packages.
- Pin dependency versions where appropriate.
- Avoid embedding secrets.

---

## Challenge

Rewrite the Dockerfile using security best practices.

---

# Skills Gained

After completing Labs **11–25**, you will have practical experience with:

- Multi-stage builds
- Vulnerability scanning
- Custom networking
- Bind mounts
- Environment variables
- Restart policies
- Health checks
- Image versioning
- Container registries
- Multi-container deployments
- Log analysis
- Monitoring
- Resource management
- Docker cleanup
- Dockerfile hardening

---

