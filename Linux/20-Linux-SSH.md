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

# 20 - Linux SSH

# Part 2 — SSH Configuration (`sshd_config`), Key Management, SCP, SFTP, SSH Agent, and Client Configuration

---

# Introduction

Installing OpenSSH is only the beginning.

In enterprise environments, SSH servers are carefully configured to:

- Restrict access
- Improve authentication
- Reduce attack surface
- Support automation
- Meet compliance requirements

Most SSH hardening is performed through the SSH server configuration file.

---

# SSH Configuration Files

There are two primary configuration files.

| File | Purpose |
|------|----------|
| `/etc/ssh/sshd_config` | SSH Server Configuration |
| `~/.ssh/config` | Per-user SSH Client Configuration |

---

# SSH Configuration Architecture

```text
Administrator

↓

SSH Client

↓

~/.ssh/config

↓

Network

↓

sshd

↓

/etc/ssh/sshd_config
```

---

# SSH Server Configuration

The SSH daemon reads:

```text
/etc/ssh/sshd_config
```

This file controls:

- Authentication
- Ports
- User access
- Logging
- Cryptographic settings
- Session limits

---

# Viewing Configuration

```bash
sudo cat /etc/ssh/sshd_config
```

Search for active directives:

```bash
grep -v "^#" /etc/ssh/sshd_config
```

---

# Testing Configuration

Before restarting SSH, validate the configuration:

```bash
sudo sshd -t
```

A successful validation produces no output.

---

# Reloading Configuration

Ubuntu:

```bash
sudo systemctl reload ssh
```

RHEL-family:

```bash
sudo systemctl reload sshd
```

If reload is unavailable or appropriate for the change:

```bash
sudo systemctl restart ssh
```

or

```bash
sudo systemctl restart sshd
```

Always ensure an existing administrative session remains open before restarting SSH remotely.

---

# Important Configuration Directives

Some commonly used directives include:

| Directive | Purpose |
|------------|----------|
| Port | Listening port |
| ListenAddress | Network interface |
| PermitRootLogin | Root login policy |
| PasswordAuthentication | Enable/disable passwords |
| PubkeyAuthentication | Enable public keys |
| AllowUsers | Restrict users |
| AllowGroups | Restrict groups |
| ClientAliveInterval | Idle timeout |
| MaxAuthTries | Login attempt limit |
| LoginGraceTime | Authentication timeout |

---

# Changing the SSH Port

Default:

```text
Port 22
```

Example:

```text
Port 2222
```

Changing the port may reduce automated scanning noise, but **it is not a substitute for proper authentication and hardening**.

Remember to update firewall rules if the listening port changes.

---

# ListenAddress

Specify which interface SSH listens on.

Example:

```text
ListenAddress 192.168.1.10
```

Benefits:

- Restrict exposure
- Separate management networks
- Improve security

---

# PermitRootLogin

Controls direct root login.

Possible values include:

```text
yes

no

prohibit-password
```

Many organizations disable direct root logins and require administrators to authenticate as individual users before using privilege escalation tools such as `sudo`.

---

# PasswordAuthentication

Enable:

```text
PasswordAuthentication yes
```

Disable:

```text
PasswordAuthentication no
```

In environments using key-based authentication, password authentication is often disabled after confirming that administrative access remains available.

---

# PubkeyAuthentication

Enable:

```text
PubkeyAuthentication yes
```

Public key authentication should remain enabled when SSH keys are used.

---

# AllowUsers

Restrict login to specific users.

Example:

```text
AllowUsers admin backup
```

Only listed users may authenticate.

---

# AllowGroups

Restrict login by group.

Example:

```text
AllowGroups sshadmins
```

Useful for enterprise access management.

---

# MaxAuthTries

Limit failed authentication attempts.

Example:

```text
MaxAuthTries 3
```

Benefits:

- Reduce brute-force attempts
- Improve security logging

---

# LoginGraceTime

Authentication timeout.

Example:

```text
LoginGraceTime 30
```

Unauthenticated sessions exceeding this period are disconnected.

---

# ClientAliveInterval

Idle session timeout.

Example:

```text
ClientAliveInterval 300
```

Helps remove inactive sessions according to organizational policy.

---

# ClientAliveCountMax

Number of unanswered keepalive messages before disconnecting a client.

Example:

```text
ClientAliveCountMax 2
```

Combined with `ClientAliveInterval`, this controls idle session behavior.

---

# Authentication Workflow

```text
Client

↓

Connect

↓

Server Policy

↓

Authentication

↓

Authorized?

↓

Yes

↓

Shell
```

---

# SSH Key Management

Large organizations manage thousands of SSH keys.

Lifecycle:

```text
Generate

↓

Deploy

↓

Rotate

↓

Audit

↓

Revoke

↓

Replace
```

---

# Generating Keys

Ed25519:

```bash
ssh-keygen -t ed25519
```

RSA:

```bash
ssh-keygen -t rsa -b 4096
```

---

# Copying Public Keys

Using OpenSSH:

```bash
ssh-copy-id user@server
```

This appends the public key to the server's:

```text
~/.ssh/authorized_keys
```

---

# Manual Key Installation

Display public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Append its contents to:

```text
~/.ssh/authorized_keys
```

Ensure appropriate permissions are applied to both the `.ssh` directory and the `authorized_keys` file.

---

# SSH File Permissions

Typical permissions:

| Item | Permission |
|------|------------|
| `~/.ssh` | `700` |
| `authorized_keys` | `600` |
| Private Key | `600` |
| Public Key | `644` (commonly used) |

Improper permissions may cause SSH to refuse key-based authentication.

---

# SSH Agent

The SSH agent stores decrypted private keys in memory.

Workflow:

```text
Private Key

↓

ssh-agent

↓

Memory

↓

SSH Authentication
```

Benefits:

- Avoid repeated passphrase entry
- Support automation
- Improve usability

---

# Starting SSH Agent

```bash
eval "$(ssh-agent -s)"
```

---

# Adding a Key

```bash
ssh-add ~/.ssh/id_ed25519
```

List loaded keys:

```bash
ssh-add -l
```

---

# SSH Client Configuration

Client configuration file:

```text
~/.ssh/config
```

This simplifies connections.

Example:

```text
Host web-prod
    HostName 203.0.113.10
    User admin
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Connect using:

```bash
ssh web-prod
```

---

# Useful Client Options

| Option | Purpose |
|----------|----------|
| Host | Alias |
| HostName | Server address |
| User | Default username |
| Port | SSH port |
| IdentityFile | Private key |
| ForwardAgent | Agent forwarding (use cautiously) |
| ServerAliveInterval | Keepalive messages |
| Compression | Enable compression |

---

# SSH File Transfer

SSH also supports secure file transfer.

Common tools:

- SCP
- SFTP

---

# SCP

Secure Copy Protocol transfers files over SSH.

Copy local file to server:

```bash
scp report.txt user@server:/home/user/
```

Copy from server:

```bash
scp user@server:/home/user/report.txt .
```

Copy directories recursively:

```bash
scp -r project/ user@server:/srv/
```

---

# SFTP

SFTP provides an interactive secure file transfer session.

Connect:

```bash
sftp user@server
```

Common commands:

```text
ls
pwd
cd
lcd
put
get
mkdir
rm
bye
```

---

# SCP vs SFTP

| Feature | SCP | SFTP |
|----------|-----|------|
| Interactive | No | Yes |
| File Browser | No | Yes |
| Recursive Copy | Yes | Yes |
| Uses SSH | Yes | Yes |
| Secure | Yes | Yes |

---

# SSH Compression

Enable compression:

```bash
ssh -C user@server
```

Useful on slower links where bandwidth savings outweigh CPU costs.

---

# Executing Remote Commands

Run a single command:

```bash
ssh user@server "hostname"
```

Another example:

```bash
ssh user@server "uptime"
```

Useful for:

- Automation
- Monitoring
- Configuration management
- Scripts

---

# Batch Administration

Example:

```text
Administrator

↓

SSH

↓

Server A

Server B

Server C

↓

Collect Results
```

Many automation frameworks build on SSH for remote execution.

---

# Enterprise SSH Workflow

```text
Administrator

↓

SSH Key

↓

Bastion Host

↓

Production Server

↓

Audit Logs
```

This centralizes access and improves traceability.

---

# Cybersecurity Perspective

Misconfigured SSH services often expose organizations to:

- Weak authentication
- Excessive administrative access
- Stale SSH keys
- Poor key management
- Unauthorized remote access

Strong configuration and disciplined key management significantly reduce these risks.

---

# Business Impact

Well-managed SSH infrastructure:

- Enables secure administration
- Supports automation
- Improves operational efficiency
- Reduces credential risk
- Supports regulatory compliance
- Simplifies access auditing

---

# Enterprise Best Practices

- Prefer Ed25519 or other organization-approved key types.
- Disable password authentication after verifying key-based access where organizational policy permits.
- Restrict SSH access to authorized users and groups.
- Avoid direct root logins.
- Validate configuration changes before restarting the SSH service.
- Protect private keys with passphrases.
- Audit authorized keys regularly.
- Remove unused keys promptly.
- Use bastion hosts for production environments.
- Log and monitor SSH authentication events.

---

# Key Takeaways

- `sshd_config` controls SSH server behavior.
- Public key authentication is preferred for enterprise environments.
- SSH agents securely cache decrypted keys in memory.
- SCP and SFTP provide encrypted file transfers.
- Client configuration files simplify repeated SSH connections.
- Proper permissions are essential for successful key authentication.

---

