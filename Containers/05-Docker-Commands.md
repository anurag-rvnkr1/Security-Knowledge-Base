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


## How It Works

Docker commands are executed through the Docker Command-Line Interface (CLI). Every command entered by the user is sent to the Docker Engine API, which communicates with the Docker Daemon (`dockerd`). The daemon performs the requested operation—such as building an image, creating a container, managing a network, or removing unused resources.

Understanding this flow helps explain why Docker commands behave the way they do and how Docker manages containerized applications behind the scenes.

---

# Docker Command Execution Flow

```
User

  │

  ▼

Docker CLI

  │

  ▼

Docker Engine API

  │

  ▼

Docker Daemon (dockerd)

  │

  ├──────────────┬───────────────┬─────────────┐

  ▼              ▼               ▼             ▼

Images      Containers      Networks      Volumes

  │

  ▼

Linux Kernel

  │

  ▼

Application Running
```

Every Docker command ultimately results in an operation performed by the Docker Daemon.

---

## Step 1 – User Executes a Command

Example:

```bash
docker run nginx
```

The Docker CLI parses the command and sends it to the Docker Engine API.

The CLI itself does **not** create containers—it only communicates with the daemon.

---

## Step 2 – Docker Daemon Receives the Request

The Docker Daemon validates the command.

Example workflow:

```
docker run nginx

        │

Check Image Exists?

        │

   ┌────┴────┐

   │         │

 Yes        No

   │         │

   ▼         ▼

Create    Pull Image

Container

        │

        ▼

Start Container
```

The daemon performs all image and container operations.

---

## Step 3 – Image Retrieval

If the image is unavailable locally:

```
Docker Hub

      │

Download Image

      │

Store Locally

      │

Run Container
```

Docker downloads only missing image layers.

Previously downloaded layers are reused.

---

## Step 4 – Container Creation

The Docker Daemon creates:

- Writable layer
- Namespaces
- cgroups
- Network configuration
- Mounted volumes
- Environment variables

Result:

```
Image

    │

Container

    │

Running Process
```

The image itself remains unchanged.

---

## Step 5 – Application Starts

The container runtime launches the application's primary process.

```
Container

      │

PID 1

      │

Application

      │

Listening for Requests
```

The container remains active while this primary process is running.

---

## Step 6 – Runtime Monitoring

Docker continuously monitors:

- Process status
- Resource usage
- Logs
- Health status
- Restart policy
- Mounted storage

Commands such as:

```bash
docker ps

docker stats

docker logs
```

retrieve this information from the Docker Daemon.

---

## Step 7 – Container Stops

Containers stop when:

- The application exits.
- A user executes:

```bash
docker stop
```

- A failure occurs.
- The host shuts down.

The image remains available for future container creation.

---

# Practical Examples

## Example 1 – Running an Nginx Web Server

Command:

```bash
docker run -d -p 8080:80 nginx
```

Workflow:

```
docker run

      │

Image Available?

      │

Download If Needed

      │

Create Container

      │

Map Port 8080 → 80

      │

Start Nginx

      │

Web Server Running
```

The application is now accessible on port **8080** of the host.

---

## Example 2 – Building an Image

Command:

```bash
docker build -t myapp .
```

Workflow:

```
Dockerfile

      │

Read Instructions

      │

Download Base Image

      │

Execute Commands

      │

Create Layers

      │

Generate Image
```

The final image can be reused multiple times.

---

## Example 3 – Viewing Logs

Command:

```bash
docker logs web
```

Workflow:

```
Container

      │

Application Output

      │

Docker Daemon

      │

CLI

      │

Terminal
```

Logs are invaluable for troubleshooting and monitoring.

---

## Example 4 – Executing a Command Inside a Container

Command:

```bash
docker exec -it web bash
```

Workflow:

```
Running Container

        │

Open Bash

        │

Interactive Terminal
```

This is useful for debugging or inspecting the runtime environment.

---

# Hands-on Exercises

## Exercise 1 – Verify Docker Installation

```bash
docker version
```

Expected result:

- Docker Client version
- Docker Server version

---

## Exercise 2 – Download Ubuntu

```bash
docker pull ubuntu
```

Verify:

```bash
docker images
```

The Ubuntu image should appear in the local image list.

---

## Exercise 3 – Start an Interactive Container

```bash
docker run -it ubuntu bash
```

Inside the container:

```bash
pwd

ls

whoami

hostname
```

Type:

```bash
exit
```

to leave the container.

---

## Exercise 4 – Start Nginx

```bash
docker run -d --name web -p 8080:80 nginx
```

Verify:

```bash
docker ps
```

Then visit:

```
http://localhost:8080
```

You should see the default Nginx welcome page.

---

## Exercise 5 – View Logs

```bash
docker logs web
```

Observe the startup output.

---

## Exercise 6 – Enter the Running Container

```bash
docker exec -it web bash
```

Try:

```bash
ls

pwd

cat /etc/os-release
```

Exit:

```bash
exit
```

---

## Exercise 7 – Stop the Container

```bash
docker stop web
```

Confirm:

```bash
docker ps
```

The container should no longer appear in the running list.

---

## Exercise 8 – Remove the Container

```bash
docker rm web
```

Verify:

```bash
docker ps -a
```

The container should be removed.

---

# Best Practices

### 1. Understand Commands Before Memorizing Them

Instead of memorizing syntax, understand **what each command does** and **how it affects Docker objects**.

---

### 2. Use Explicit Image Versions

Prefer:

```bash
docker pull nginx:1.27
```

over:

```bash
docker pull nginx:latest
```

Version pinning provides predictable deployments.

---

### 3. Name Important Containers

Instead of relying on automatically generated names:

```bash
docker run --name web nginx
```

Named containers are easier to manage.

---

### 4. Monitor Resource Usage

Regularly check:

```bash
docker stats
```

to identify resource bottlenecks.

---

### 5. Review Logs First During Troubleshooting

When a container fails, start with:

```bash
docker logs <container_name>
```

Logs often provide the fastest insight into startup failures.

---

### 6. Clean Up Unused Resources

Periodically remove:

- Stopped containers
- Dangling images
- Unused networks
- Unused volumes

to maintain a clean Docker environment.

---

### 7. Learn Command Categories

Rather than memorizing hundreds of commands individually, group them by purpose:

- Information
- Images
- Containers
- Networks
- Volumes
- Build
- Registry
- Monitoring
- Cleanup

This makes Docker CLI easier to learn and remember.

---

## Common Mistakes

Docker provides hundreds of CLI commands, but many operational problems arise from using the wrong command, misunderstanding command behavior, or failing to understand the relationship between Docker objects. The following are the most common mistakes encountered by beginners and professionals.

---

# 1. Confusing `docker run` with `docker start`

Many users believe these commands perform the same action.

### `docker run`

Creates **and** starts a **new** container.

```
Image

   │

docker run

   │

New Container

   │

Running
```

Example:

```bash
docker run nginx
```

---

### `docker start`

Starts an **existing** stopped container.

```
Stopped Container

        │

docker start

        │

Running Container
```

Example:

```bash
docker start web
```

**Rule to Remember**

- `docker run` → Create + Start
- `docker start` → Start Existing

---

# 2. Forgetting Detached Mode (`-d`)

Running:

```bash
docker run nginx
```

keeps the terminal attached to the container.

Instead, use:

```bash
docker run -d nginx
```

Detached mode allows the container to run in the background.

---

# 3. Not Publishing Required Ports

Example:

```bash
docker run nginx
```

The web server starts successfully, but cannot be accessed from the host.

Correct approach:

```bash
docker run -p 8080:80 nginx
```

```
Host

8080

 │

 ▼

Container

80
```

Without port mapping, services remain inaccessible from outside the container.

---

# 4. Using `docker exec` Instead of `docker run`

Incorrect:

```bash
docker exec ubuntu bash
```

`docker exec` requires an **already running container**.

Correct sequence:

```bash
docker run -it ubuntu bash
```

or

```bash
docker exec -it running_container bash
```

---

# 5. Using `docker kill` Instead of `docker stop`

### `docker stop`

```
SIGTERM

↓

Graceful Shutdown

↓

Application Cleans Up

↓

Container Stops
```

---

### `docker kill`

```
SIGKILL

↓

Immediate Termination
```

`docker stop` is recommended unless immediate termination is necessary.

---

# 6. Forgetting to Name Containers

Without:

```bash
--name
```

Docker generates names such as:

```
happy_lamarr

adoring_turing

nostalgic_newton
```

Instead:

```bash
docker run --name web nginx
```

Named containers simplify management and automation.

---

# 7. Using `latest` Everywhere

Avoid:

```bash
docker pull python:latest
```

Prefer:

```bash
docker pull python:3.12

docker pull nginx:1.27
```

Explicit versions improve reproducibility and simplify rollbacks.

---

# 8. Ignoring Logs During Troubleshooting

Many users restart containers repeatedly without reviewing logs.

Always begin troubleshooting with:

```bash
docker logs <container_name>
```

Logs often reveal:

- Configuration errors
- Missing files
- Permission issues
- Runtime exceptions

---

# 9. Forgetting Cleanup

Repeated testing leaves behind:

- Stopped containers
- Unused images
- Networks
- Volumes

Example cleanup commands:

```bash
docker container prune

docker image prune

docker volume prune

docker network prune
```

Neglecting cleanup can consume significant disk space over time.

---

# 10. Assuming `docker rm` Removes Images

Incorrect assumption:

```bash
docker rm nginx
```

removes the image.

Actual behavior:

```
docker rm

↓

Removes Container Only
```

To remove an image:

```bash
docker rmi nginx
```

---

# 11. Ignoring Image Size

Using unnecessarily large images increases:

- Download time
- Storage usage
- Build time
- Attack surface

Prefer minimal images when suitable.

Examples:

- Alpine
- Debian Slim
- Distroless

---

# 12. Forgetting That Containers Are Ephemeral

Example:

```
Container

↓

Application Writes Data

↓

Container Removed

↓

Data Lost
```

Persistent data should always be stored in volumes or external storage.

---

# 13. Using Root Inside Containers

Many official images default to the `root` user.

Risks:

- Greater impact of vulnerabilities
- Privilege escalation
- Increased attack surface

Create and run applications as non-root users whenever practical.

---

# 14. Memorizing Commands Without Understanding Objects

Many users memorize:

```bash
docker pull

docker run

docker ps

docker stop
```

without understanding the underlying Docker objects:

- Images
- Containers
- Networks
- Volumes
- Registries

Conceptual understanding makes command usage much more intuitive.

---

# 15. Skipping `docker inspect`

When troubleshooting, many users overlook one of Docker's most valuable commands:

```bash
docker inspect <container_name>
```

It provides detailed information including:

- Environment variables
- IP addresses
- Mounted volumes
- Network configuration
- Labels
- Resource limits

Use it before making assumptions about a container's configuration.

---

# Docker Commands Quick Revision

## Information

```bash
docker version

docker info

docker --help
```

---

## Images

```bash
docker images

docker pull

docker push

docker rmi

docker history

docker inspect
```

---

## Containers

```bash
docker run

docker start

docker stop

docker restart

docker kill

docker rm

docker ps

docker ps -a
```

---

## Container Access

```bash
docker exec

docker logs

docker top

docker inspect

docker stats
```

---

## Build

```bash
docker build
```

---

## Networks

```bash
docker network ls

docker network create

docker network inspect

docker network connect

docker network disconnect
```

---

## Volumes

```bash
docker volume ls

docker volume create

docker volume inspect

docker volume rm
```

---

## Cleanup

```bash
docker image prune

docker container prune

docker volume prune

docker network prune

docker system prune
```

---

# Docker Commands Checklist

| Command Category | Status |
|------------------|:------:|
| Information Commands | ✓ |
| Image Commands | ✓ |
| Container Commands | ✓ |
| Build Commands | ✓ |
| Network Commands | ✓ |
| Volume Commands | ✓ |
| Registry Commands | ✓ |
| Monitoring Commands | ✓ |
| Inspection Commands | ✓ |
| Cleanup Commands | ✓ |
| Logging Commands | ✓ |
| Interactive Commands | ✓ |
| Troubleshooting Commands | ✓ |
| Docker Workflow Commands | ✓ |
| Command Best Practices | ✓ |

---

# References

## Docker Documentation

- Docker CLI Documentation
- Docker Engine Documentation
- Docker Build Documentation
- Docker Hub Documentation
- Docker Networking Documentation
- Docker Volumes Documentation

---

## OCI Standards

- Open Container Initiative (OCI) Image Specification
- Open Container Initiative (OCI) Runtime Specification
- Open Container Initiative (OCI) Distribution Specification

---

## Linux Documentation

- Linux Namespaces
- Linux cgroups
- OverlayFS Documentation
- Linux Capabilities Documentation

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

---

## Recommended Learning Resources

- Docker Official Documentation
- Docker Labs
- Play with Docker
- Linux Foundation Training
- CNCF Learning Paths
- NIST Computer Security Resource Center (CSRC)

