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

## Next Section

Intermediate Labs

Advanced Security Labs

DevSecOps Labs

Incident Response Labs

Forensics Labs

Production Challenge Labs

---