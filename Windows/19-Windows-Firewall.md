# 19-Windows-Firewall.md

# Part 2 — Advanced Firewall Rules, Connection Security Rules, IPsec, PowerShell Firewall Management, Logging, and Enterprise Deployment

---

# Introduction

Enterprise environments require firewall policies that go beyond simply allowing or blocking ports.

Modern Windows Firewall supports:

- Granular application filtering
- User and computer-based rules
- Interface-specific rules
- IPsec integration
- Authentication-based communication
- PowerShell automation
- Centralized deployment
- Comprehensive logging and monitoring

These capabilities allow organizations to build highly secure endpoint communication policies.

---

# Advanced Firewall Rules

A firewall rule can contain multiple conditions.

A rule may specify:

- Program
- Service
- Protocol
- Local Port
- Remote Port
- Local IP Address
- Remote IP Address
- Network Profile
- User
- Computer
- Interface Type

Example:

```text
Allow

Program:
C:\Program Files\App\App.exe

Protocol:
TCP

Local Port:
443

Remote IP:
10.20.0.0/16

Profile:
Domain
```

---

# Rule Components

| Component | Purpose |
|-----------|----------|
| Program | Executable path |
| Service | Windows service |
| Protocol | TCP, UDP, ICMP |
| Ports | Local/Remote |
| IP Address | Local/Remote filtering |
| Profile | Domain, Private, Public |
| Interface | LAN, Wi-Fi, VPN |
| Users | Specific users |
| Computers | Authenticated computers |

---

# Application-Based Filtering

Application rules identify traffic by executable rather than port.

Example:

```text
Allow

chrome.exe

↓

TCP 443
```

Benefits:

- More granular
- Prevents unauthorized applications from using allowed ports
- Easier auditing

---

# Service-Based Filtering

Instead of allowing every application:

```text
Windows Service

↓

Specific Service

↓

Firewall Rule
```

Example:

- DHCP Client
- DNS Client
- Print Spooler

This reduces unnecessary exposure.

---

# IP Address Filtering

Firewall rules may restrict communication based on:

- Local IP
- Remote IP
- Subnet
- IP Range

Example:

```text
Allow

Remote IP

10.10.50.0/24
```

Only systems from the approved subnet may connect.

---

# Interface Types

Rules may apply only to:

- Ethernet
- Wireless
- Remote Access (VPN)

Example:

```text
Allow SMB

↓

Ethernet Only
```

This prevents SMB exposure on public Wi-Fi.

---

# Edge Traversal

Edge Traversal determines whether traffic can pass through NAT devices.

Example:

```text
Internet

↓

NAT

↓

Edge Traversal

↓

Windows Firewall
```

Enable only when explicitly required.

---

# Authentication-Based Firewall Rules

Firewall rules may require authenticated users or computers.

Example:

```text
User

↓

Kerberos Authentication

↓

Firewall Rule

↓

Allow
```

This prevents anonymous connections.

---

# Connection Security Rules

Unlike firewall rules, Connection Security Rules do **not** directly allow or block traffic.

They define how connections should be authenticated and protected.

Common uses:

- IPsec authentication
- Encryption
- Secure server communication

---

# Connection Security Rule Types

Windows supports:

| Rule Type | Purpose |
|-----------|----------|
| Isolation | Secure communication between domain members |
| Authentication Exemption | Exclude selected devices |
| Server-to-Server | Secure specific servers |
| Tunnel | Site-to-site IPsec tunnels |
| Custom | Advanced scenarios |

---

# IPsec Overview

Internet Protocol Security (IPsec) secures IP communication.

Provides:

- Authentication
- Integrity
- Encryption

---

# IPsec Security Services

```text
Computer A

↓

Authenticate

↓

Encrypt

↓

Secure Communication

↓

Computer B
```

---

# IPsec Modes

| Mode | Purpose |
|------|----------|
| Transport Mode | Protects packet payload |
| Tunnel Mode | Protects entire IP packet |

---

# Transport Mode

```text
Original Header

↓

Encrypted Payload
```

Typically used between hosts.

---

# Tunnel Mode

```text
Entire Packet

↓

Encrypted

↓

New Header Added
```

Commonly used for VPNs and gateway-to-gateway communication.

---

# Authentication Methods

Supported methods include:

- Kerberos
- Computer Certificates
- Pre-Shared Keys (testing only)

Enterprise deployments generally prefer Kerberos or certificates.

---

# Firewall and IPsec Integration

Workflow:

```text
Packet

↓

Firewall Rule

↓

Connection Security Rule

↓

Authentication

↓

Encryption

↓

Transmission
```

---

# PowerShell Firewall Management

PowerShell provides comprehensive firewall administration.

Primary module:

```powershell
NetSecurity
```

---

# View Firewall Profiles

```powershell
Get-NetFirewallProfile
```

Displays:

- Enabled status
- Default actions
- Logging settings

---

# Enable Firewall

```powershell
Set-NetFirewallProfile `
-Profile Domain,Private,Public `
-Enabled True
```

---

# Disable Firewall (Testing Only)

```powershell
Set-NetFirewallProfile `
-Profile Public `
-Enabled False
```

Disabling the firewall should be avoided on production systems.

---

# View Firewall Rules

```powershell
Get-NetFirewallRule
```

---

# Search for a Rule

```powershell
Get-NetFirewallRule `
-DisplayName "*Remote Desktop*"
```

---

# Create a Firewall Rule

Example:

```powershell
New-NetFirewallRule `
-DisplayName "Allow HTTPS" `
-Direction Inbound `
-Protocol TCP `
-LocalPort 443 `
-Action Allow
```

---

# Remove a Rule

```powershell
Remove-NetFirewallRule `
-DisplayName "Allow HTTPS"
```

---

# Disable a Rule

```powershell
Disable-NetFirewallRule `
-DisplayName "Allow HTTPS"
```

---

# Enable a Rule

```powershell
Enable-NetFirewallRule `
-DisplayName "Allow HTTPS"
```

---

# Export Firewall Policy

Example:

```powershell
netsh advfirewall export C:\FirewallPolicy.wfw
```

Useful before major configuration changes.

---

# Import Firewall Policy

```powershell
netsh advfirewall import C:\FirewallPolicy.wfw
```

---

# Firewall Logging

Windows Firewall can record:

- Dropped packets
- Successful connections
- Rule activity

Logging supports:

- Troubleshooting
- Incident response
- Compliance
- Threat hunting

---

# Firewall Log Location

Default location:

```text
%SystemRoot%\System32\LogFiles\Firewall\pfirewall.log
```

---

# Firewall Log Fields

Typical entries include:

- Date
- Time
- Source IP
- Destination IP
- Protocol
- Port
- Action

Example:

```text
ALLOW TCP 192.168.1.25 10.0.0.10 51542 443
```

---

# Monitoring Firewall Activity

Administrators should monitor:

- Unexpected outbound traffic
- Blocked administrative ports
- Excessive connection attempts
- Suspicious external IP addresses
- Port scanning behavior

---

# Enterprise Firewall Deployment

Large organizations commonly deploy firewall policies using:

- Group Policy
- Microsoft Intune
- Microsoft Configuration Manager
- Mobile Device Management (MDM)

Centralized management ensures consistent security across endpoints.

---

# Group Policy Deployment

```text
Administrator

↓

Group Policy

↓

Domain Controllers

↓

Windows Endpoints

↓

Firewall Updated
```

---

# Firewall Policy Lifecycle

```text
Design

↓

Test

↓

Approve

↓

Deploy

↓

Monitor

↓

Review

↓

Update
```

---

# Enterprise Example

A financial institution deploys firewall policies that:

- Allow HTTPS outbound
- Restrict RDP to IT administrators
- Block SMB across workstation VLANs
- Require IPsec authentication between application servers
- Log all dropped inbound connections

These controls reduce lateral movement and improve auditability.

---

# Cybersecurity Perspective

Proper firewall configuration helps mitigate:

- Network reconnaissance
- Unauthorized remote access
- Malware command-and-control communication
- Worm propagation
- Lateral movement
- Data exfiltration

Firewall logs are also valuable during incident investigations.

---

# Business Impact

Advanced firewall management provides:

- Improved endpoint security
- Better regulatory compliance
- Reduced attack surface
- Lower incident response costs
- Consistent enterprise policy enforcement
- Enhanced visibility into network activity

---

# Enterprise Best Practices

- Use application-based rules whenever possible.
- Restrict administrative ports to trusted networks.
- Require IPsec authentication for sensitive communications.
- Enable firewall logging on enterprise endpoints.
- Review firewall policies regularly.
- Remove obsolete rules.
- Automate deployment using Group Policy or MDM.
- Test rule changes before production rollout.
- Document exceptions and business justifications.
- Monitor firewall logs within the SIEM.

---

# Practical Labs

## Lab 1 — List Firewall Profiles

Run:

```powershell
Get-NetFirewallProfile
```

Record:

- Enabled status
- Default inbound action
- Default outbound action

---

## Lab 2 — Create a Test Rule

Create an inbound rule allowing TCP port 8443.

Verify that the rule appears in:

```powershell
Get-NetFirewallRule
```

---

## Lab 3 — Review Firewall Logs

Locate:

```text
%SystemRoot%\System32\LogFiles\Firewall\
```

Review recent entries and identify:

- Allowed connections
- Blocked connections

---

## Lab 4 — Export Firewall Configuration

Run:

```powershell
netsh advfirewall export C:\FirewallBackup.wfw
```

Verify that the backup file is created.

---

# Key Takeaways

- Advanced firewall rules support granular filtering based on applications, services, users, IP addresses, and interfaces.
- Connection Security Rules configure IPsec authentication and encryption rather than directly allowing or blocking traffic.
- PowerShell provides complete firewall administration through the NetSecurity module.
- Firewall logging is essential for troubleshooting, auditing, and security investigations.
- Centralized policy deployment ensures consistent enterprise firewall configurations.

---

# Interview Questions

1. What is the difference between a Firewall Rule and a Connection Security Rule?
2. What is IPsec and why is it used?
3. Compare IPsec Transport Mode and Tunnel Mode.
4. What PowerShell module manages Windows Firewall?
5. How do you create a firewall rule using PowerShell?
6. Where are Windows Firewall logs stored?
7. Why are application-based rules generally preferred?
8. How are firewall policies deployed across enterprise environments?
9. What information is recorded in `pfirewall.log`?
10. Why should firewall rules be reviewed periodically?

---

# References

- Microsoft Learn
- Microsoft Windows Defender Firewall Documentation
- Microsoft NetSecurity PowerShell Module Documentation
- Microsoft IPsec Documentation
- Microsoft Windows Filtering Platform Documentation
- NIST SP 800-41 Rev.1 (Guidelines on Firewalls and Firewall Policy)

---

**Next:** **Part 3 — Firewall Troubleshooting, Security Monitoring, Enterprise Hardening, Incident Response, and Best Practices**