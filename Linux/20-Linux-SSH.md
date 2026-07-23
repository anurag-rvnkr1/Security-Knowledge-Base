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

# 20 - Linux SSH

# Part 3 — SSH Port Forwarding, SSH Tunneling, Agent Forwarding, Multiplexing, Hardening, Monitoring, and Troubleshooting

---

# Introduction

SSH is much more than a remote login protocol.

Enterprise administrators use SSH for:

- Secure tunneling
- Port forwarding
- Remote application access
- Database administration
- Secure file transfers
- DevOps automation
- Infrastructure management
- Incident response

Understanding these advanced capabilities is essential for Linux administrators and cybersecurity professionals.

---

# SSH Advanced Features

```text
SSH

├── Remote Login
├── File Transfer
├── Local Port Forwarding
├── Remote Port Forwarding
├── Dynamic Port Forwarding
├── Agent Forwarding
├── Connection Multiplexing
├── Command Execution
└── Secure Tunneling
```

---

# SSH Tunneling

SSH tunneling securely transports network traffic through an encrypted SSH connection.

```text
Application

↓

SSH Tunnel

↓

Encrypted Network

↓

Remote Server
```

Benefits:

- Protects traffic over untrusted networks
- Encrypts otherwise unencrypted protocols
- Bypasses insecure intermediate networks
- Enables secure administrative access

---

# Types of Port Forwarding

SSH supports three primary forwarding methods.

| Type | Purpose |
|------|----------|
| Local Port Forwarding | Local machine accesses remote service |
| Remote Port Forwarding | Remote system accesses local service |
| Dynamic Port Forwarding | SOCKS proxy |

---

# Local Port Forwarding

Local forwarding redirects a local port to a service on the remote network.

```text
Browser

↓

localhost:8080

↓

SSH Tunnel

↓

Remote Web Server

↓

Port 80
```

Example:

```bash
ssh -L 8080:localhost:80 user@server
```

After connecting:

```text
http://localhost:8080
```

accesses the remote web service securely.

---

# Enterprise Example

Database access:

```text
Administrator Laptop

↓

SSH Tunnel

↓

Database Server

↓

3306
```

Instead of exposing the database to the Internet, administrators access it through an encrypted tunnel.

---

# Remote Port Forwarding

Remote forwarding exposes a local service through the remote server.

```text
Local Service

↓

SSH Tunnel

↓

Remote Server

↓

Accessible Remotely
```

Example:

```bash
ssh -R 9090:localhost:8080 user@server
```

Common use cases:

- Remote support
- Development
- Demonstrations
- Temporary service exposure

Only enable remote forwarding where organizational policy permits.

---

# Dynamic Port Forwarding

Dynamic forwarding creates a SOCKS proxy.

```text
Browser

↓

SOCKS Proxy

↓

SSH Tunnel

↓

Internet
```

Example:

```bash
ssh -D 1080 user@server
```

Applications configured to use the SOCKS proxy send their traffic through the encrypted tunnel.

---

# Port Forwarding Comparison

| Type | Purpose |
|------|----------|
| Local (-L) | Access remote services locally |
| Remote (-R) | Expose local services remotely |
| Dynamic (-D) | General-purpose SOCKS proxy |

---

# Secure Tunneling Workflow

```text
Client

↓

Encrypted Tunnel

↓

SSH Server

↓

Protected Service
```

---

# Executing Remote Commands

Run a command:

```bash
ssh user@server "hostname"
```

Check uptime:

```bash
ssh user@server "uptime"
```

Check disk usage:

```bash
ssh user@server "df -h"
```

This is commonly used by:

- Automation tools
- Monitoring systems
- Configuration management platforms

---

# Running Multiple Commands

Example:

```bash
ssh user@server "hostname && uptime && who"
```

Useful for quick diagnostics.

---

# Agent Forwarding

SSH Agent Forwarding allows a remote system to use authentication from the local SSH agent without copying the private key.

```text
Laptop

↓

SSH Agent

↓

Remote Server

↓

Second Server
```

Example:

```bash
ssh -A user@server
```

---

# Agent Forwarding Considerations

Advantages:

- No private key copied
- Convenient for jump hosts
- Supports administrative workflows

Risks:

- If the intermediate host is compromised, forwarded authentication may be abused during the active session.

Best Practice:

Use agent forwarding only when necessary and only through trusted systems.

---

# Connection Multiplexing

SSH can reuse an existing connection.

Benefits:

- Faster subsequent connections
- Reduced authentication overhead
- Improved automation performance

---

# Multiplexing Workflow

```text
First SSH Session

↓

Master Connection

↓

Second Session

↓

Reuse Existing Connection
```

---

# Example Client Configuration

```text
Host *

ControlMaster auto
ControlPersist 10m
ControlPath ~/.ssh/cm-%r@%h:%p
```

Benefits:

- Faster repeated connections
- Reduced login delays
- Improved scripting performance

---

# Keepalive Messages

Client keepalive:

```text
ServerAliveInterval 60
```

Server keepalive:

```text
ClientAliveInterval 300
```

These settings help detect broken connections and clean up stale sessions.

---

# SSH Hardening

A secure SSH deployment typically includes:

- Public key authentication
- Strong cryptographic algorithms
- Restricted administrative access
- Firewall protection
- Monitoring
- Logging
- Multi-factor authentication (where supported)

---

# SSH Hardening Workflow

```text
Install

↓

Configure

↓

Restrict Access

↓

Disable Weak Authentication

↓

Monitor

↓

Audit
```

---

# Common Hardening Measures

| Measure | Benefit |
|----------|----------|
| Disable direct root login | Reduces privileged attack surface |
| Use public keys | Stronger authentication |
| Limit users | Reduces unauthorized access |
| Restrict groups | Simplifies access control |
| Limit authentication attempts | Mitigates brute-force attacks |
| Use firewalls | Limits network exposure |
| Monitor logs | Detects suspicious activity |

---

# SSH Logging

SSH events are typically written to:

Ubuntu/Debian:

```text
/var/log/auth.log
```

RHEL-family:

```text
/var/log/secure
```

Using `journalctl` on systems with systemd:

```bash
journalctl -u ssh
```

or

```bash
journalctl -u sshd
```

depending on the distribution.

---

# Monitoring Failed Logins

Ubuntu:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL:

```bash
grep "Failed password" /var/log/secure
```

Look for:

- Repeated failures
- Unknown usernames
- Unusual source IP addresses
- Activity outside normal maintenance windows

---

# Common SSH Problems

| Problem | Possible Cause |
|----------|----------------|
| Connection refused | SSH service not running or firewall blocking access |
| Permission denied | Authentication failure |
| Host key changed | Server replacement or possible impersonation |
| Timeout | Network or firewall issue |
| Key ignored | Incorrect permissions or configuration |

---

# Troubleshooting Workflow

```text
Cannot Connect

↓

Ping

↓

SSH Service Running?

↓

Port Listening?

↓

Firewall Rules?

↓

Authentication?

↓

Logs

↓

Resolved
```

---

# Useful Troubleshooting Commands

Check service:

```bash
systemctl status ssh
```

or

```bash
systemctl status sshd
```

Check listening ports:

```bash
ss -tulpn | grep ssh
```

Verbose client output:

```bash
ssh -vvv user@server
```

Inspect logs:

```bash
journalctl -u ssh
```

or:

```bash
journalctl -u sshd
```

---

# Host Key Changes

When connecting, you may receive a warning similar to:

```text
WARNING:
REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Possible reasons:

- Server reinstalled
- Host keys regenerated
- DNS points to a different server
- Possible man-in-the-middle attack

Always verify the new host key through a trusted channel before accepting it.

---

# SSH Security Risks

Attackers commonly target SSH using:

- Brute-force attacks
- Password spraying
- Credential theft
- Compromised private keys
- Exploitation of weak configurations

Defensive controls include:

- Strong authentication
- Network restrictions
- Logging
- Multi-factor authentication
- Key rotation

---

# Enterprise SSH Architecture

```text
Administrator

↓

VPN

↓

Bastion Host

↓

Production SSH Gateway

↓

Application Servers

↓

Database Servers
```

Benefits:

- Centralized administration
- Auditability
- Reduced exposure
- Easier access control

---

# Secure Administrative Workflow

```text
Administrator

↓

VPN

↓

SSH Key Authentication

↓

Bastion

↓

Production Server

↓

Audit Logs
```

---

# DevOps and Automation

SSH is widely used by:

- Ansible
- Git
- CI/CD pipelines
- Backup systems
- Monitoring platforms
- Configuration management tools

Automation generally relies on key-based authentication rather than interactive passwords.

---

# Cybersecurity Perspective

SSH is one of the most frequently targeted services on Internet-facing Linux servers.

Proper hardening:

- Limits brute-force attacks
- Protects administrator credentials
- Reduces attack surface
- Supports secure incident response
- Enables secure automation

---

# Business Impact

Secure SSH administration helps organizations:

- Protect critical infrastructure
- Enable secure remote operations
- Reduce credential compromise
- Improve compliance
- Support business continuity
- Simplify operational management

---

# Enterprise Best Practices

- Use public key authentication instead of passwords where organizational policy permits.
- Restrict SSH access using firewalls and trusted networks.
- Disable direct root logins.
- Review authentication logs regularly.
- Protect private keys with strong passphrases.
- Rotate SSH keys periodically.
- Use bastion hosts for production systems.
- Enable multi-factor authentication where supported.
- Limit access to authorized users and groups.
- Audit SSH configurations on a regular schedule.

---

# Key Takeaways

- SSH tunneling securely transports application traffic.
- Local, remote, and dynamic port forwarding serve different use cases.
- Agent forwarding should be used carefully and only with trusted hosts.
- Connection multiplexing improves efficiency for repeated connections.
- Logging and monitoring are essential for detecting unauthorized access attempts.
- SSH hardening significantly strengthens enterprise Linux security.

---


# 20 - Linux SSH

# Part 4 — Practical Labs, Enterprise Case Studies, Chapter Summary, Interview Questions, and References

---

# Introduction

SSH is one of the most frequently used services in Linux administration.

Enterprise administrators use SSH every day to:

- Manage servers
- Deploy applications
- Transfer files
- Troubleshoot systems
- Perform incident response
- Automate administration
- Access cloud infrastructure
- Maintain production environments

Because SSH often provides privileged administrative access, it must be configured, monitored, and audited carefully.

---

# Enterprise SSH Lifecycle

```text
Plan

↓

Deploy

↓

Configure

↓

Harden

↓

Monitor

↓

Audit

↓

Respond

↓

Improve
```

---

# Practical Lab 1 — Verify SSH Installation

Check SSH client version:

```bash
ssh -V
```

Check SSH server package (Ubuntu/Debian):

```bash
dpkg -l | grep openssh
```

RHEL-family:

```bash
rpm -qa | grep openssh
```

Objectives:

- Verify OpenSSH installation
- Confirm installed components

---

# Practical Lab 2 — Check SSH Service

Ubuntu:

```bash
systemctl status ssh
```

RHEL-family:

```bash
systemctl status sshd
```

Verify automatic startup:

```bash
systemctl is-enabled ssh
```

or

```bash
systemctl is-enabled sshd
```

Objectives:

- Verify service status
- Confirm boot-time startup

---

# Practical Lab 3 — Verify Listening Port

Display listening sockets:

```bash
ss -tulpn | grep ssh
```

Alternative:

```bash
ss -tulpn | grep :22
```

Objectives:

- Verify SSH is listening
- Identify configured port

---

# Practical Lab 4 — Generate SSH Keys

Generate an Ed25519 key pair:

```bash
ssh-keygen -t ed25519
```

Verify generated files:

```bash
ls ~/.ssh
```

Objectives:

- Create a key pair
- Understand key storage

---

# Practical Lab 5 — Install Public Key

Using OpenSSH:

```bash
ssh-copy-id user@server
```

Verify:

```bash
ssh user@server
```

Objectives:

- Configure key authentication
- Validate successful login

---

# Practical Lab 6 — Review SSH Configuration

Display configuration:

```bash
grep -v "^#" /etc/ssh/sshd_config
```

Review:

- Port
- Authentication
- User restrictions
- Timeouts

Objectives:

- Understand active configuration
- Identify hardening opportunities

---

# Practical Lab 7 — Validate SSH Configuration

Before restarting SSH:

```bash
sudo sshd -t
```

Objectives:

- Detect configuration errors
- Prevent service outages

---

# Practical Lab 8 — Configure SSH Client

Create:

```text
~/.ssh/config
```

Example:

```text
Host production

HostName 203.0.113.10

User admin

IdentityFile ~/.ssh/id_ed25519
```

Connect:

```bash
ssh production
```

Objectives:

- Simplify connections
- Standardize client configuration

---

# Practical Lab 9 — Transfer Files Securely

Copy local file:

```bash
scp report.txt user@server:/tmp/
```

Retrieve file:

```bash
scp user@server:/tmp/report.txt .
```

Objectives:

- Practice secure file transfer
- Verify SCP functionality

---

# Practical Lab 10 — Use SFTP

Connect:

```bash
sftp user@server
```

Useful commands:

```text
ls
pwd
put
get
mkdir
bye
```

Objectives:

- Navigate remote directories
- Upload and download files securely

---

# Practical Lab 11 — Execute Remote Commands

Check hostname:

```bash
ssh user@server "hostname"
```

Check uptime:

```bash
ssh user@server "uptime"
```

Check disk usage:

```bash
ssh user@server "df -h"
```

Objectives:

- Execute remote commands
- Practice command automation

---

# Practical Lab 12 — Create a Local SSH Tunnel

Example:

```bash
ssh -L 8080:localhost:80 user@server
```

Open:

```text
http://localhost:8080
```

Objectives:

- Understand local port forwarding
- Securely access internal services

---

# Practical Lab 13 — Review SSH Logs

Ubuntu:

```bash
grep ssh /var/log/auth.log
```

RHEL:

```bash
grep ssh /var/log/secure
```

Or:

```bash
journalctl -u ssh
```

Objectives:

- Identify successful logins
- Identify failed authentication attempts

---

# Practical Lab 14 — Audit SSH Keys

Review:

```text
~/.ssh/authorized_keys
```

Questions:

- Which keys are active?
- Are unused keys present?
- Are former administrators' keys removed?

Objectives:

- Review access
- Improve security hygiene

---

# Practical Lab 15 — Troubleshoot SSH

Scenario:

Unable to connect.

Workflow:

```text
Network

↓

Ping

↓

SSH Service

↓

Listening Port

↓

Firewall

↓

Authentication

↓

Logs

↓

Resolved
```

Useful commands:

```bash
ping server
```

```bash
ss -tulpn
```

```bash
systemctl status ssh
```

```bash
ssh -vvv user@server
```

---

# Enterprise Case Study 1

# Secure Cloud Administration

Architecture:

```text
Administrator

↓

VPN

↓

Bastion Host

↓

Cloud Instances
```

Benefits:

- Centralized administration
- Reduced exposure
- Auditable access

---

# Enterprise Case Study 2

# Brute-Force SSH Attack

Observed:

```text
Thousands of Failed Logins

↓

Authentication Logs

↓

Firewall Review

↓

Access Restrictions

↓

Monitoring
```

Recommended actions:

- Restrict SSH access to trusted networks.
- Prefer key-based authentication.
- Consider multi-factor authentication where supported.
- Monitor repeated authentication failures.

---

# Enterprise Case Study 3

# Lost Private Key

Incident:

Administrator reports a missing laptop containing SSH keys.

Response:

```text
Identify Keys

↓

Remove Public Keys

↓

Generate New Keys

↓

Deploy Replacement

↓

Verify Access

↓

Document Incident
```

Lesson:

Treat lost private keys as potentially compromised.

---

# Enterprise Case Study 4

# Production SSH Configuration Error

Problem:

Modified `sshd_config` prevents new logins.

Recovery:

```text
Existing Session

↓

Validate Configuration

↓

Correct Error

↓

Reload SSH

↓

Verify

↓

Close Existing Session
```

Lesson:

Always keep an active administrative session open while testing remote configuration changes.

---

# Enterprise Case Study 5

# Bastion Host Deployment

Environment:

```text
Internet

↓

VPN

↓

Bastion

↓

Production

↓

Database
```

Benefits:

- Centralized authentication
- Session logging
- Reduced attack surface
- Easier compliance

---

# SSH Security Audit Checklist

| Control | Status |
|----------|--------|
| SSH service running | ✓ |
| Key-based authentication enabled | ✓ |
| Direct root login restricted | ✓ |
| Firewall rules reviewed | ✓ |
| Authorized keys audited | ✓ |
| SSH logs monitored | ✓ |
| Idle session timeout configured | ✓ |
| SSH configuration validated | ✓ |
| Administrative access documented | ✓ |
| Configuration backed up | ✓ |

---

# Common SSH Mistakes

| Mistake | Risk | Better Practice |
|----------|------|-----------------|
| Using weak passwords | Credential compromise | Prefer key-based authentication |
| Sharing private keys | Unauthorized access | Keep keys confidential |
| Leaving unused keys | Persistent access | Remove stale keys |
| Allowing unrestricted SSH access | Larger attack surface | Restrict by firewall and user policy |
| Ignoring logs | Missed attacks | Monitor authentication events |
| Restarting SSH without validation | Administrative lockout | Validate configuration first |
| Disabling all authentication methods accidentally | Loss of access | Test changes incrementally |

---

# Enterprise SSH Dashboard

```text
SSH Dashboard

├── Successful Logins

├── Failed Logins

├── Active Sessions

├── Authorized Keys

├── Bastion Activity

├── SSH Configuration

├── Security Alerts

├── Authentication Trends

├── Key Rotation Status

└── Compliance
```

---

# Cybersecurity Perspective

SSH is frequently targeted because it grants administrative access.

Security teams should:

- Monitor authentication events
- Restrict administrative access
- Rotate keys periodically
- Remove inactive accounts
- Review SSH configuration regularly
- Investigate abnormal login patterns

---

# Business Impact

Secure SSH administration enables organizations to:

- Protect production infrastructure
- Support secure remote work
- Improve operational efficiency
- Reduce credential-related incidents
- Meet compliance requirements
- Maintain business continuity

---

# Enterprise Best Practices

- Use modern SSH key algorithms approved by organizational policy.
- Validate `sshd_config` before reloading the service.
- Restrict administrative access through firewalls and bastion hosts.
- Protect private keys with strong passphrases.
- Audit `authorized_keys` regularly.
- Remove inactive users and obsolete keys promptly.
- Enable centralized logging for SSH authentication events.
- Implement multi-factor authentication where feasible.
- Maintain documented SSH access procedures.
- Periodically review SSH hardening against current security guidance.

---

# Chapter Summary

In this chapter, you learned:

- SSH fundamentals
- SSH architecture
- OpenSSH components
- Public key authentication
- Host keys
- SSH client and server configuration
- `sshd_config`
- SCP
- SFTP
- SSH agent
- SSH tunneling
- Port forwarding
- Agent forwarding
- Connection multiplexing
- SSH hardening
- Monitoring
- Troubleshooting
- Enterprise SSH deployment

---

# Interview Questions

## Beginner

1. What is SSH?
2. Why is SSH more secure than Telnet?
3. What is the default SSH port?
4. What is `sshd`?
5. What is the purpose of `authorized_keys`?
6. What is the difference between public and private keys?
7. What is SCP?
8. What is SFTP?
9. Where is `sshd_config` located?
10. Why are host keys important?

---

## Intermediate

1. Compare password authentication and public key authentication.
2. Explain how SSH key-based authentication works.
3. What is SSH agent forwarding?
4. Describe local, remote, and dynamic port forwarding.
5. How would you troubleshoot SSH connectivity issues?
6. Why is `sshd -t` useful?
7. Explain the purpose of a bastion host.
8. How would you audit SSH access on a Linux server?
9. What are the risks of unrestricted SSH access?
10. How can SSH improve automation?

---

## Advanced

1. Design a secure SSH architecture for a multi-tier production environment.
2. Explain SSH hardening for Internet-facing servers.
3. Describe an enterprise SSH key lifecycle.
4. How would you respond to a compromised private key?
5. Design a bastion host architecture for cloud infrastructure.
6. Explain how SSH integrates with DevOps automation.
7. How would you implement centralized SSH auditing?
8. Describe secure SSH access for Kubernetes worker nodes.
9. What controls help protect SSH from brute-force attacks?
10. How would you manage SSH access for thousands of servers?

---

# Key Takeaways

- SSH is the industry standard for secure remote administration.
- Public key authentication is generally preferred over passwords.
- `sshd_config` controls SSH server behavior.
- SSH tunneling securely transports application traffic.
- Regular auditing, monitoring, and key management are essential for enterprise security.
- Bastion hosts provide controlled administrative access to production systems.

---

# References

## Official Documentation

- `man ssh`
- `man sshd`
- `man ssh_config`
- `man sshd_config`
- `man ssh-keygen`
- `man ssh-copy-id`
- `man scp`
- `man sftp`
- `man ssh-agent`
- `man ssh-add`

## Standards & Best Practices

- OpenSSH Project Documentation
- Linux Foundation Documentation
- Red Hat Enterprise Linux Security Guide
- Ubuntu Server Guide
- CIS Benchmarks for Linux
- NIST SP 800-53 (Security and Privacy Controls)
- NIST Cybersecurity Framework (CSF)
- MITRE ATT&CK Framework
- OWASP Cheat Sheet Series

---

# Next Chapter

➡️ **21-Linux-Automation.md**

## Topics Covered

- Automation Fundamentals
- Scheduling Jobs with `cron` and `at`
- Cron Expressions
- Systemd Timers
- Task Automation
- Backup Automation
- Log Rotation
- Automated Monitoring
- Automation Security
- Enterprise Automation Best Practices
- Practical Labs
- Interview Questions
- References