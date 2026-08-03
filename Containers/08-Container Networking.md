# Chapter 8 – Container Networking

## Overview

Networking is one of the most important aspects of containerized applications. While containers provide isolated execution environments, they rarely operate independently. Modern applications consist of multiple services that must communicate securely and efficiently with each other, external clients, databases, APIs, and cloud services.

Container Networking provides the mechanisms that enable communication:

- Between containers on the same host
- Between containers on different hosts
- Between containers and the host machine
- Between containers and external networks
- Between containers and cloud services

Docker automatically creates virtual networking components that allow containers to communicate while maintaining isolation and security.

Understanding container networking is fundamental for:

- Docker
- Docker Compose
- Kubernetes
- Microservices
- DevOps
- DevSecOps
- Cloud Computing
- Cloud Security

---

# Why It Matters

Consider an online shopping application.

```
Customer

     │

     ▼

Frontend

     │

     ▼

Backend API

     │

     ▼

PostgreSQL

     │

     ▼

Redis
```

Each service runs in a separate container.

Without networking:

- Services cannot communicate.
- APIs cannot reach databases.
- Users cannot access applications.
- Microservices cannot exchange data.

Container networking solves these problems while preserving isolation and scalability.

---

# Container Networking Architecture

```
                    Internet

                        │

                        ▼

                Host Network Interface

                        │

                 Docker Engine

                        │

               Virtual Network

        ┌──────────┼───────────┐

        ▼          ▼           ▼

     Web API     Database    Redis

     Container   Container  Container
```

Containers communicate through virtual networks created and managed by Docker.

---

# How Container Networking Works

Every container receives:

- Network namespace
- Virtual network interface
- IP address
- Routing table
- DNS configuration
- Firewall rules

These components isolate network traffic while enabling controlled communication.

---

# Network Namespace

Every container has its own network namespace.

Example:

```
Container A

eth0

127.0.0.1

192.168.x.x


Container B

eth0

127.0.0.1

192.168.x.x
```

Although both containers have an `eth0` interface and a loopback address (`127.0.0.1`), they exist in separate network namespaces and do not interfere with each other.

---

# Virtual Ethernet (veth)

Docker connects containers to virtual networks using **virtual Ethernet pairs (veth pairs)**.

```
Container

    │

Virtual Ethernet

    │

Docker Bridge

    │

Host Network
```

A veth pair acts like a virtual cable:

- One end resides inside the container.
- The other end connects to the Docker bridge on the host.

---

# Docker Bridge

By default, Docker creates a bridge network named:

```
bridge
```

Architecture:

```
Host

      │

Docker Bridge

 ┌────┼─────┐

 ▼    ▼     ▼

C1   C2    C3
```

Containers connected to the same bridge network can communicate with each other, subject to Docker's networking rules.

---

# Types of Docker Networks

Docker supports several network drivers.

| Network | Purpose |
|----------|---------|
| Bridge | Default single-host networking |
| Host | Shares the host network stack |
| Overlay | Multi-host networking |
| Macvlan | Assigns MAC addresses to containers |
| None | Disables networking |

Each driver serves different deployment requirements.

---

# Bridge Network

The **Bridge** network is the default Docker network.

```
Host

      │

Bridge Network

 ┌────┼─────┐

 ▼    ▼     ▼

Web   API   DB
```

Characteristics:

- Default network driver
- Suitable for single-host deployments
- Supports container-to-container communication
- Provides network isolation from the host by default

Bridge networks are the most common choice for local development.

---

# Host Network

With the **Host** network driver, the container shares the host's network stack.

```
Host Network

     │

Container
```

Characteristics:

- No network namespace isolation
- No virtual bridge
- Higher performance
- Reduced network isolation

Use this mode only when necessary, as it increases exposure and reduces isolation.

---

# Overlay Network

The **Overlay** driver connects containers running on multiple hosts.

```
Host A

     │

Overlay Network

     │

Host B
```

Characteristics:

- Multi-host communication
- Common in orchestration platforms
- Enables distributed microservices

Overlay networks are widely used in Kubernetes and Docker Swarm environments.

---

# Macvlan Network

The **Macvlan** driver assigns a unique MAC address to each container.

```
Switch

   │

 ┌─┼─────────┐

 ▼ ▼         ▼

C1 C2       C3
```

Each container appears as an independent device on the physical network.

Typical use cases include:

- Legacy applications
- Network appliances
- Monitoring tools

---

# None Network

The **None** network disables networking entirely.

```
Container

No Network Interface
```

The container cannot communicate with:

- Other containers
- Host
- Internet

Useful for highly isolated workloads.

---

# Port Mapping

Containers often expose services internally.

Example:

```
Container

Port 80
```

To make the service accessible externally:

```bash
docker run -p 8080:80 nginx
```

Result:

```
Host

8080

 │

 ▼

Container

80
```

Requests to the host's port `8080` are forwarded to port `80` inside the container.

---

# DNS and Service Discovery

Docker provides built-in DNS for user-defined networks.

Instead of:

```
172.18.0.5
```

applications can connect using:

```
database
```

Example:

```
Web

↓

database

↓

PostgreSQL
```

Using service names instead of IP addresses improves portability and reliability.

---

# Key Concepts

## Network Isolation

Each container operates within its own network namespace, isolating interfaces, routing tables, and firewall rules.

---

## Virtual Networking

Docker creates software-defined virtual networks that allow containers to communicate without requiring physical network hardware.

---

## Service Discovery

Containers on the same user-defined network can locate each other using DNS-based service names rather than hardcoded IP addresses.

---

## Port Publishing

Applications become accessible outside the container only when ports are explicitly published (for example, with `-p`).

---

## Multi-Host Networking

Overlay networks enable communication between containers running on different hosts, supporting distributed applications.

---

## Network Drivers

Selecting the appropriate network driver depends on the application's communication, performance, and isolation requirements.

---

## How It Works

Container networking enables communication between containers, the host system, and external networks while maintaining isolation through Linux kernel networking features. Docker automates the creation of virtual networks, assigns IP addresses, configures DNS, and manages routing rules so applications can communicate without manual network configuration.

Internally, Docker uses Linux networking technologies such as:

- Network Namespaces
- Virtual Ethernet (veth) pairs
- Linux Bridges
- iptables / nftables (depending on the host configuration)
- Network Address Translation (NAT)
- Embedded DNS (on user-defined networks)

These components work together to provide secure and efficient networking for containerized applications.

---

# Container Networking Workflow

```
Application

      │

      ▼

Container

      │

Network Namespace

      │

Virtual Ethernet (veth)

      │

Docker Bridge

      │

Host Network

      │

Internet
```

Every network packet follows this path unless a different network driver is used.

---

## Step 1 – Create the Container

When a container starts:

```bash
docker run nginx
```

Docker automatically:

- Creates a network namespace
- Creates a virtual Ethernet pair
- Assigns an IP address
- Configures routing
- Configures DNS
- Connects the container to a Docker network

---

## Step 2 – Create a Network Namespace

Every container receives an isolated network stack.

```
Host

│

├── Container A

│      eth0

│      Routing Table

│      Firewall Rules

│

└── Container B

       eth0

       Routing Table

       Firewall Rules
```

Containers cannot directly access each other's networking configuration.

---

## Step 3 – Create a Virtual Ethernet Pair

Docker creates a **veth pair**.

```
Container

eth0

      │

Virtual Cable

      │

Host veth

      │

Docker Bridge
```

Think of it as plugging the container into a virtual network switch.

---

## Step 4 – Connect to Docker Bridge

By default:

```
docker0
```

acts as a virtual bridge.

```
Host

      │

docker0

 ┌────┼─────┐

 ▼    ▼     ▼

C1   C2    C3
```

Every container connected to the bridge receives:

- IP address
- Default gateway
- DNS configuration

Containers on the same bridge network can communicate with one another according to the network's rules.

---

## Step 5 – Assign an IP Address

Docker assigns an internal IP.

Example:

```
Container A

172.17.0.2


Container B

172.17.0.3
```

These addresses are typically private and managed by Docker.

Applications should generally communicate using service or container names on user-defined networks instead of relying on these IP addresses.

---

## Step 6 – Configure DNS

On user-defined bridge networks, Docker provides an embedded DNS service.

Instead of:

```
172.18.0.5
```

applications use:

```
database
```

Workflow:

```
Web

↓

database

↓

DNS Lookup

↓

172.18.0.5
```

Docker resolves the service name automatically.

---

## Step 7 – Configure Port Mapping

Suppose Nginx listens on:

```
80
```

inside the container.

Run:

```bash
docker run -p 8080:80 nginx
```

Docker configures port forwarding:

```
Internet

      │

Host 8080

      │

Docker NAT

      │

Container 80
```

Users access:

```
http://host:8080
```

Docker forwards requests to the container's port 80.

---

## Step 8 – Communicate Between Containers

Containers attached to the same user-defined network communicate directly.

```
Web

 │

 ▼

API

 │

 ▼

Database
```

Applications simply use service names:

```
database

redis

backend

frontend
```

No manual IP management is required.

---

## Step 9 – Access External Networks

Containers can also access the Internet.

Example:

```
Container

↓

Docker Bridge

↓

Host Network

↓

Router

↓

Internet
```

This allows containers to:

- Download software updates
- Call APIs
- Connect to cloud services
- Access external databases (when permitted)

---

# Practical Examples

## Example 1 – Two Containers

Run:

```bash
docker run --name web nginx
```

Run:

```bash
docker run --name api ubuntu
```

If both are attached to the same user-defined network, they can communicate using:

```
web

api
```

rather than IP addresses.

---

## Example 2 – Docker Compose

Compose file:

```yaml
services:

  web:

    image: nginx

  database:

    image: postgres
```

Docker automatically creates:

```
Compose Network

     │

 ┌───┼────┐

 ▼   ▼    ▼

Web DB Redis
```

Each service is reachable by its service name.

---

## Example 3 – Port Mapping

Command:

```bash
docker run -p 5000:5000 flask-app
```

Network flow:

```
Browser

↓

localhost:5000

↓

Docker

↓

Flask Application
```

The host forwards incoming traffic to the container.

---

## Example 4 – Host Network

Command:

```bash
docker run --network host nginx
```

Result:

```
Container

↓

Uses Host Network Directly
```

No bridge or virtual interface is created for the container's network.

---

# Hands-on Commands

## List Networks

```bash
docker network ls
```

Displays all Docker networks.

---

## Inspect a Network

```bash
docker network inspect bridge
```

Displays:

- Connected containers
- Network driver
- Subnet
- Gateway
- IP assignments

---

## Create a Network

```bash
docker network create mynetwork
```

Creates a user-defined bridge network.

---

## Run a Container on a Network

```bash
docker run --network mynetwork nginx
```

Attaches the container to the specified network.

---

## Connect an Existing Container

```bash
docker network connect mynetwork web
```

Connects a running container to another network.

---

## Disconnect a Container

```bash
docker network disconnect mynetwork web
```

Removes the container from the network.

---

## Remove a Network

```bash
docker network rm mynetwork
```

Deletes an unused network.

---

## View Port Mappings

```bash
docker port web
```

Displays published ports for a container.

---

## Inspect Network Configuration

```bash
docker inspect web
```

Review the **NetworkSettings** section for:

- IP address
- Gateway
- MAC address
- Connected networks
- Port bindings

---

# Best Practices

### 1. Use User-Defined Bridge Networks

Prefer creating your own bridge networks instead of relying on the default `bridge` network.

Benefits include:

- Better DNS-based service discovery
- Improved isolation
- Simpler communication using service names

---

### 2. Publish Only Required Ports

Expose only the services that must be reachable externally.

Keep databases, caches, and internal services on private networks whenever possible.

---

### 3. Use Service Names Instead of IP Addresses

Avoid hardcoded IP addresses.

Prefer:

```
database
```

instead of:

```
172.18.0.4
```

Docker's DNS makes service names stable and portable.

---

### 4. Separate Public and Private Services

Example:

```
Internet

↓

Frontend

↓

Backend

↓

Database
```

Only the frontend should generally be exposed to external users.

---

### 5. Avoid Host Networking Unless Necessary

The host network driver reduces isolation.

Use it only when specific performance or networking requirements justify the trade-off.

---

### 6. Document Port Usage

Clearly document:

- Container ports
- Published host ports
- Internal service ports

This simplifies troubleshooting and maintenance.

---

### 7. Monitor Network Connectivity

Regularly verify:

- Container communication
- DNS resolution
- Port mappings
- Firewall rules
- Network performance

Early monitoring helps detect configuration issues before they impact applications.

---


