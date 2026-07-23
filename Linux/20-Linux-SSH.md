# 20 - Linux SSH

# Part 1 — SSH Fundamentals, SSH Architecture, Authentication, SSH Keys, and Secure Remote Administration

---

# Introduction

One of the most important responsibilities of a Linux System Administrator, DevOps Engineer, Cloud Engineer, SOC Analyst, or Security Engineer is **secure remote administration**.

In the early days of networking, administrators commonly used protocols such as:

- Telnet
- Rlogin
- FTP

These protocols transmitted credentials and data in **plaintext**, making them vulnerable to interception.

To solve this problem, **SSH (Secure Shell)** was developed.

Today, SSH is the industry standard for securely accessing Linux systems over untrusted networks.

---

# Learning Objectives

After completing this chapter, you will understand:

- SSH fundamentals
- SSH architecture
- SSH client and server
- Authentication methods
- SSH encryption
- Public key cryptography
- SSH key-based authentication
- Secure remote administration
- Enterprise SSH concepts

---

# What is SSH?

SSH (Secure Shell) is a cryptographic network protocol used for:

- Secure remote login
- Secure command execution
- File transfer
- Port forwarding
- Tunneling
- Remote system administration

Unlike Telnet, SSH encrypts both authentication and communication.

---

# Why SSH Matters

SSH provides:

- Confidentiality
- Integrity
- Authentication
- Secure administration
- Secure automation
- Secure file transfer

It is widely used across:

- Linux servers
- Cloud environments
- Containers
- Network appliances
- DevOps pipelines
- Enterprise data centers

---

# SSH vs Telnet

| Feature | SSH | Telnet |
|----------|-----|--------|
| Encryption | Yes | No |
| Authentication | Strong | Weak |
| Password Protection | Encrypted | Plaintext |
| Integrity Checking | Yes | No |
| Secure File Transfer | Yes | No |
| Recommended Today | Yes | No |

---

# SSH Workflow

```text
Administrator

↓

SSH Client

↓

Encrypted Network

↓

SSH Server

↓

Linux System
```

---

# SSH Architecture

SSH consists of two primary components.

```text
SSH Client

↓

Network

↓

SSH Server
```

---

# SSH Client

The client initiates the connection.

Common client command:

```bash
ssh username@server
```

Examples:

```bash
ssh admin@192.168.1.10
```

```bash
ssh user@example.com
```

---

# SSH Server

The server accepts secure connections.

The SSH daemon is usually:

```text
sshd
```

It listens for incoming connections and performs:

- Authentication
- Encryption negotiation
- Session management
- Access control

---

# SSH Communication Process

```text
Client

↓

TCP Connection

↓

Key Exchange

↓

Server Authentication

↓

User Authentication

↓

Encrypted Session

↓

Shell Access
```

---

# Default SSH Port

Default port:

```text
22/TCP
```

Although SSH can listen on another port, changing the port alone should not be considered a substitute for proper hardening.

---

# Installing OpenSSH

Ubuntu/Debian:

```bash
sudo apt install openssh-server
```

RHEL/Rocky/AlmaLinux:

```bash
sudo dnf install openssh-server
```

---

# Starting SSH Service

Using systemd:

```bash
sudo systemctl start ssh
```

or, on some distributions:

```bash
sudo systemctl start sshd
```

Enable at boot:

```bash
sudo systemctl enable ssh
```

or:

```bash
sudo systemctl enable sshd
```

Service names vary by distribution.

---

# Checking SSH Status

Ubuntu:

```bash
systemctl status ssh
```

RHEL-family:

```bash
systemctl status sshd
```

---

# Checking Listening Port

Display listening sockets:

```bash
ss -tulpn | grep ssh
```

Or:

```bash
ss -tulpn | grep 22
```

---

# Testing SSH Connectivity

Connect:

```bash
ssh user@server
```

Verbose mode:

```bash
ssh -v user@server
```

More verbose:

```bash
ssh -vv
```

Maximum verbosity:

```bash
ssh -vvv
```

Verbose output is particularly useful when troubleshooting authentication and connection issues.

---

# SSH Protocol Layers

```text
Application

↓

SSH Protocol

↓

TCP

↓

IP

↓

Network
```

SSH typically operates over TCP.

---

# SSH Security Goals

SSH is designed to provide:

```text
Authentication

↓

Encryption

↓

Integrity

↓

Secure Session
```

---

# SSH Authentication Methods

SSH supports multiple authentication methods.

| Method | Description |
|----------|-------------|
| Password Authentication | Username and password |
| Public Key Authentication | Public/private key pair |
| Keyboard-Interactive | Interactive authentication mechanism (often integrated with PAM) |
| Multi-factor Authentication (MFA) | Multiple verification factors |
| Host-Based Authentication | Trust between systems (specialized use cases) |

In enterprise environments, public key authentication is generally preferred over passwords.

---

# Password Authentication

Workflow:

```text
Client

↓

Username

↓

Password

↓

Server

↓

Authentication
```

Advantages:

- Simple
- Easy to configure

Limitations:

- Susceptible to brute-force attacks
- Depends on password strength
- Less suitable for automation

---

# Public Key Authentication

SSH key-based authentication uses asymmetric cryptography.

```text
Private Key

↓

Public Key

↓

Authentication
```

The private key remains with the user.

The public key is installed on the server.

---

# Why Key Authentication?

Advantages include:

- Strong authentication
- No password transmission
- Better automation
- Reduced brute-force risk
- Suitable for large-scale infrastructure

---

# Public Key Cryptography

```text
Private Key

↓

Mathematics

↓

Public Key
```

Properties:

- Public key can be shared.
- Private key must remain secret.
- The server verifies possession of the private key without receiving it.

---

# Generating SSH Keys

Generate a modern key pair:

```bash
ssh-keygen -t ed25519
```

RSA example:

```bash
ssh-keygen -t rsa -b 4096
```

Current recommendations often favor **Ed25519** for general-purpose SSH deployments due to its strong security and performance characteristics.

---

# Key Generation Workflow

```text
ssh-keygen

↓

Private Key

↓

Public Key

↓

Install Public Key

↓

Authenticate
```

---

# Default SSH Key Location

```text
~/.ssh/
```

Typical files:

```text
id_ed25519

id_ed25519.pub
```

or

```text
id_rsa

id_rsa.pub
```

---

# File Purposes

| File | Purpose |
|------|----------|
| Private Key | Secret credential used by the client |
| Public Key | Installed on servers for authentication |
| known_hosts | Stores known server host keys |
| config | Optional client configuration |

---

# Server-Side Authorized Keys

Public keys are stored in:

```text
~/.ssh/authorized_keys
```

Authentication flow:

```text
Client Public Key

↓

Server authorized_keys

↓

Match?

↓

Yes

↓

Login
```

---

# Protecting Private Keys

Private keys should:

- Never be shared
- Be stored securely
- Use restrictive file permissions
- Be protected with a passphrase where appropriate
- Be backed up securely according to organizational policy

---

# SSH Host Keys

Host keys identify the **server**, not the user.

Workflow:

```text
Client

↓

Server Host Key

↓

Verification

↓

Trust Established
```

The client stores trusted host keys in the `known_hosts` file.

---

# Host Key Verification

First connection:

```text
Unknown Server

↓

Display Fingerprint

↓

Administrator Verifies

↓

Trust Stored
```

Subsequent connections compare the stored host key against the server's presented key.

Unexpected changes should be investigated before proceeding.

---

# Known Hosts

Location:

```text
~/.ssh/known_hosts
```

Purpose:

- Store trusted server host keys
- Detect potential man-in-the-middle attacks
- Prevent silent server impersonation

---

# SSH Session Lifecycle

```text
Connect

↓

Negotiate Algorithms

↓

Verify Server

↓

Authenticate User

↓

Open Session

↓

Execute Commands

↓

Disconnect
```

---

# Enterprise SSH Architecture

```text
Administrator Laptop

↓

VPN

↓

Bastion Host

↓

Production Servers
```

Rather than exposing every server directly, many organizations use a **bastion (jump) host** for administrative access.

---

# Bastion Host

A bastion host is a hardened server used as a controlled entry point into protected networks.

Benefits:

- Centralized administration
- Reduced attack surface
- Improved auditing
- Easier access control

---

# Common SSH Use Cases

| Use Case | Example |
|----------|----------|
| Remote Administration | Server management |
| Automation | Configuration management tools |
| Secure File Transfer | SCP/SFTP |
| Git Operations | Repository access |
| Cloud Administration | Virtual machine management |
| DevOps | CI/CD deployments |

---

# Cybersecurity Perspective

Attackers frequently target SSH because it provides remote administrative access.

Common attack techniques include:

- Password guessing
- Credential stuffing
- Brute-force attacks
- Stolen private keys
- Misconfigured access controls

Proper authentication, monitoring, and hardening significantly reduce these risks.

---

# Business Impact

Secure SSH deployment helps organizations:

- Protect administrative access
- Enable secure remote operations
- Support cloud infrastructure
- Reduce credential exposure
- Improve compliance
- Maintain business continuity

---

# Enterprise Best Practices

- Prefer public key authentication over passwords.
- Protect private keys with strong passphrases.
- Verify server host keys before trusting them.
- Restrict SSH access using firewalls and network segmentation.
- Use bastion hosts for administrative access to production environments.
- Monitor SSH authentication logs.
- Rotate keys according to organizational policy.
- Remove unused accounts and stale authorized keys.

---

# Key Takeaways

- SSH is the standard protocol for secure remote administration.
- SSH provides confidentiality, integrity, and authentication.
- Public key authentication is generally preferred in enterprise environments.
- Private keys must remain confidential, while public keys are installed on servers.
- Host keys verify server identity and help prevent impersonation attacks.
- Bastion hosts improve security for production infrastructure.

---

