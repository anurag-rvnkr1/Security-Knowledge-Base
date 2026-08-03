# Chapter 5 – Docker Commands

## Overview

Docker commands are the primary interface for interacting with the Docker platform. They enable users to build images, create and manage containers, configure networking, manage storage, inspect Docker objects, monitor resource usage, and automate application deployment.

The Docker Command-Line Interface (CLI) communicates with the Docker Daemon through the Docker Engine API. Every Docker operation—whether building an image, starting a container, or removing unused resources—is initiated using Docker commands.

Mastering Docker commands is essential for:

- Container Management
- DevOps
- DevSecOps
- Cloud Engineering
- Kubernetes Administration
- Site Reliability Engineering (SRE)
- Cloud Security
- Technical Interviews

This chapter explains the most commonly used Docker commands, their syntax, practical examples, and best practices.

---

# Why It Matters

Although Docker provides graphical interfaces through Docker Desktop, nearly all production environments rely on the Docker CLI.

Knowing Docker commands enables you to:

- Deploy applications rapidly
- Troubleshoot containers
- Manage images
- Monitor resources
- Automate deployments
- Configure networking
- Handle persistent storage
- Integrate with CI/CD pipelines

Docker CLI proficiency is expected in most DevOps, Cloud, and Container-related interviews.

---

# Docker CLI Architecture

```
User

   │

Docker CLI

   │

Docker Engine API

   │

Docker Daemon

   │

Docker Objects

 ┌────┼────┬─────┐

 ▼    ▼    ▼     ▼

Images Containers Networks Volumes
```

Every command issued through the CLI is processed by the Docker Daemon.

---

# Docker Command Categories

Docker commands can be grouped into several functional categories.

| Category | Purpose |
|----------|---------|
| Information | View Docker environment |
| Images | Manage container images |
| Containers | Manage running containers |
| Networks | Configure networking |
| Volumes | Manage persistent storage |
| Build | Create images |
| Logs | Troubleshoot applications |
| Monitoring | Observe resource usage |
| Cleanup | Remove unused resources |
| Registry | Push and pull images |

---

# Information Commands

## Check Docker Version

```bash
docker version
```

Displays:

- Docker Client version
- Docker Engine version
- API version
- Build information

---

## Display Docker Information

```bash
docker info
```

Shows:

- Number of containers
- Number of images
- Storage driver
- Runtime
- CPU
- Memory
- Docker Root Directory
- Security options

Useful for troubleshooting Docker installations.

---

## Display Docker Help

```bash
docker --help
```

Lists all available Docker commands and options.

---

# Image Commands

## List Images

```bash
docker images
```

Displays locally stored images.

Example output:

```
REPOSITORY     TAG      IMAGE ID

nginx          latest   abc123

ubuntu         24.04    xyz456
```

---

## Search Images

```bash
docker search nginx
```

Searches Docker Hub for images.

---

## Pull an Image

```bash
docker pull nginx
```

Downloads the latest Nginx image.

Specify a version:

```bash
docker pull nginx:1.27
```

---

## Remove an Image

```bash
docker rmi nginx
```

Deletes the specified image.

---

## Display Image History

```bash
docker history nginx
```

Shows image layers and build history.

---

## Inspect an Image

```bash
docker inspect nginx
```

Displays detailed image metadata.

---

# Container Commands

## Create and Run a Container

```bash
docker run nginx
```

Creates and starts a new container.

---

## Run in Detached Mode

```bash
docker run -d nginx
```

Runs the container in the background.

---

## Assign a Name

```bash
docker run --name web nginx
```

Creates a container named **web**.

---

## Publish Ports

```bash
docker run -p 8080:80 nginx
```

Maps:

```
Host Port 8080

↓

Container Port 80
```

allowing access to the web server from the host.

---

## Interactive Container

```bash
docker run -it ubuntu bash
```

Starts an interactive Ubuntu shell.

---

## List Running Containers

```bash
docker ps
```

Shows active containers.

---

## List All Containers

```bash
docker ps -a
```

Shows running and stopped containers.

---

## Start a Container

```bash
docker start web
```

Starts an existing container.

---

## Stop a Container

```bash
docker stop web
```

Gracefully stops the container.

---

## Restart a Container

```bash
docker restart web
```

Stops and immediately starts the container.

---

## Pause a Container

```bash
docker pause web
```

Temporarily suspends all processes inside the container.

---

## Unpause a Container

```bash
docker unpause web
```

Resumes a paused container.

---

## Kill a Container

```bash
docker kill web
```

Immediately terminates the container without graceful shutdown.

---

## Remove a Container

```bash
docker rm web
```

Deletes a stopped container.

---

## Force Remove

```bash
docker rm -f web
```

Stops and removes the container.

---

# Container Inspection Commands

## Inspect Container

```bash
docker inspect web
```

Displays:

- Network settings
- Environment variables
- Mounts
- Image information
- IP address
- Labels

---

## View Running Processes

```bash
docker top web
```

Lists processes inside the container.

---

## Execute Commands

```bash
docker exec web ls
```

Runs a command inside the container.

---

## Interactive Shell

```bash
docker exec -it web bash
```

Opens an interactive shell inside a running container.

---

## View Logs

```bash
docker logs web
```

Displays container logs.

---

## Follow Logs

```bash
docker logs -f web
```

Streams logs in real time.

---

## Display Resource Usage

```bash
docker stats
```

Shows:

- CPU usage
- Memory usage
- Network I/O
- Disk I/O
- PIDs

Useful for monitoring running containers.

---

# Build Commands

## Build Image

```bash
docker build -t myapp .
```

Builds an image named **myapp** from the current directory.

---

## Build Specific Dockerfile

```bash
docker build -f Dockerfile.prod -t myapp .
```

Uses a custom Dockerfile.

---

## List Build Cache

```bash
docker builder ls
```

Displays builder instances.

---

# Network Commands

## List Networks

```bash
docker network ls
```

Shows Docker networks.

---

## Inspect Network

```bash
docker network inspect bridge
```

Displays detailed network information.

---

## Create Network

```bash
docker network create mynetwork
```

Creates a custom network.

---

## Connect Container

```bash
docker network connect mynetwork web
```

Connects a container to a network.

---

## Disconnect Container

```bash
docker network disconnect mynetwork web
```

Removes the container from the specified network.

---

# Volume Commands

## List Volumes

```bash
docker volume ls
```

Displays Docker-managed volumes.

---

## Create Volume

```bash
docker volume create myvolume
```

Creates a persistent volume.

---

## Inspect Volume

```bash
docker volume inspect myvolume
```

Displays volume information.

---

## Remove Volume

```bash
docker volume rm myvolume
```

Deletes a volume.

---

# Registry Commands

## Login

```bash
docker login
```

Authenticates with a container registry.

---

## Logout

```bash
docker logout
```

Logs out from the current registry.

---

## Push Image

```bash
docker push username/myapp:v1
```

Uploads an image to a registry.

---

## Pull Image

```bash
docker pull username/myapp:v1
```

Downloads an image from a registry.

---

# Cleanup Commands

## Remove Stopped Containers

```bash
docker container prune
```

Deletes all stopped containers.

---

## Remove Unused Images

```bash
docker image prune
```

Removes dangling images.

---

## Remove Unused Volumes

```bash
docker volume prune
```

Deletes unused volumes.

---

## Remove Unused Networks

```bash
docker network prune
```

Deletes unused networks.

---

## Remove Everything Unused

```bash
docker system prune
```

Removes:

- Stopped containers
- Unused images
- Unused networks
- Build cache

Use with caution in production environments.

---

# Key Concepts

## Docker CLI

The Docker CLI is the primary interface used to communicate with Docker Engine.

---

## Docker Objects

Most Docker commands operate on:

- Images
- Containers
- Networks
- Volumes

---

## Stateless Operations

Docker commands typically create, inspect, or remove immutable objects rather than modifying them in place.

---

## Automation

Docker commands can be integrated into:

- Bash scripts
- CI/CD pipelines
- Infrastructure as Code
- Kubernetes workflows

---

## Next Section

How It Works

Practical Examples

Hands-on Exercises

Best Practices

Common Mistakes

References

---