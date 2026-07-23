# 26 - Networking Cheat Sheet

> **Quick Revision Guide for Network Engineers, SOC Analysts, System Administrators, Cybersecurity Engineers, Cloud Engineers, and Technical Interviews**

---

# Introduction

This cheat sheet summarizes the most important networking concepts covered throughout this repository. It is designed for rapid revision before interviews, certification exams, troubleshooting sessions, and day-to-day enterprise operations.

---

# 1. OSI Model

| Layer | Name | Common Devices | Example Protocols |
|--------|------|----------------|-------------------|
| 7 | Application | Proxy, WAF | HTTP, HTTPS, DNS, SMTP, FTP |
| 6 | Presentation | SSL/TLS Gateway | TLS, SSL, JPEG, ASCII |
| 5 | Session | Session Gateway | NetBIOS, RPC |
| 4 | Transport | Firewall, Load Balancer | TCP, UDP |
| 3 | Network | Router, Layer 3 Switch | IPv4, IPv6, ICMP, IPsec |
| 2 | Data Link | Switch, Bridge | Ethernet, ARP, VLAN (802.1Q) |
| 1 | Physical | Hub, Cable, Repeater | Fiber, Copper, RF |

---

# 2. TCP/IP Model

| Layer | Protocol Examples |
|--------|-------------------|
| Application | HTTP, HTTPS, DNS, DHCP, SSH, FTP, SMTP |
| Transport | TCP, UDP |
| Internet | IPv4, IPv6, ICMP |
| Network Access | Ethernet, Wi-Fi |

---

# 3. Common Protocols

| Protocol | Port | Transport | Purpose |
|----------|------|-----------|----------|
| HTTP | 80 | TCP | Web traffic |
| HTTPS | 443 | TCP | Secure web traffic |
| DNS | 53 | UDP/TCP | Name resolution |
| DHCP | 67/68 | UDP | IP address assignment |
| FTP | 21 | TCP | File transfer (control) |
| SSH | 22 | TCP | Secure remote administration |
| Telnet | 23 | TCP | Remote terminal (insecure) |
| SMTP | 25 | TCP | Email transfer |
| POP3 | 110 | TCP | Email retrieval |
| IMAP | 143 | TCP | Email synchronization |
| SNMP | 161/162 | UDP | Network monitoring |
| LDAP | 389 | TCP/UDP | Directory services |
| LDAPS | 636 | TCP | Secure LDAP |
| RDP | 3389 | TCP | Remote Desktop |
| SMB | 445 | TCP | File sharing |
| NTP | 123 | UDP | Time synchronization |
| Syslog | 514 | UDP/TCP | Log forwarding |

---

# 4. TCP vs UDP

| Feature | TCP | UDP |
|----------|-----|-----|
| Connection | Yes | No |
| Reliable Delivery | Yes | No |
| Ordering | Guaranteed | Not Guaranteed |
| Error Recovery | Yes | No |
| Speed | Slower | Faster |
| Typical Use | Web, Email, SSH | DNS, VoIP, Streaming |

---

# 5. IPv4 Private Address Ranges

| Network | CIDR |
|----------|------|
| 10.0.0.0 – 10.255.255.255 | /8 |
| 172.16.0.0 – 172.31.255.255 | /12 |
| 192.168.0.0 – 192.168.255.255 | /16 |

---

# 6. Common Subnet Masks

| CIDR | Subnet Mask | Total Addresses | Usable Hosts |
|------|-------------|-----------------|--------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1024 | 1022 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |

---

# 7. IPv6 Quick Facts

- 128-bit addressing
- Hexadecimal notation
- No broadcast (uses multicast)
- Supports SLAAC
- Larger address space than IPv4
- Improved routing efficiency
- Built-in support for IPsec

Example:

```
2001:db8::1
```

---

# 8. Routing Protocols

| Protocol | Type | Typical Use |
|----------|------|-------------|
| RIP | Distance Vector | Small networks |
| OSPF | Link State | Enterprise LAN/WAN |
| EIGRP | Advanced Distance Vector | Cisco environments |
| IS-IS | Link State | Service providers |
| BGP | Path Vector | Internet and hybrid cloud |

---

# 9. VLAN Quick Reference

- Access Port → Single VLAN
- Trunk Port → Multiple VLANs
- Native VLAN → Untagged traffic
- IEEE Standard → 802.1Q
- Inter-VLAN communication requires Layer 3 routing.

---

# 10. STP States (Classic IEEE 802.1D)

- Blocking
- Listening
- Learning
- Forwarding
- Disabled

Purpose: Prevent Layer 2 loops and broadcast storms.

---

# 11. DHCP DORA Process

```
Discover

↓

Offer

↓

Request

↓

Acknowledge
```

---

# 12. TCP Three-Way Handshake

```
SYN

↓

SYN-ACK

↓

ACK
```

---

# 13. TCP Connection Termination

```
FIN

↓

ACK

↓

FIN

↓

ACK
```

---

# 14. DNS Resolution Process

```
Client

↓

Recursive Resolver

↓

Authoritative DNS

↓

IP Address Returned

↓

Connection Established
```

---

# 15. ARP Process

```
ARP Request

↓

Broadcast

↓

ARP Reply

↓

MAC Learned
```

---

# 16. NAT Types

| Type | Purpose |
|------|---------|
| Static NAT | One-to-one mapping |
| Dynamic NAT | Pool-based translation |
| PAT (NAT Overload) | Many-to-one translation |

---

# 17. VPN Types

- Site-to-Site VPN
- Remote Access VPN
- IPsec VPN
- SSL/TLS VPN

---

# 18. Firewall Types

- Packet Filtering Firewall
- Stateful Firewall
- Next-Generation Firewall (NGFW)
- Web Application Firewall (WAF)
- Cloud Firewall

---

# 19. IDS vs IPS

| IDS | IPS |
|------|-----|
| Detects threats | Detects and blocks threats |
| Passive | Inline |
| Generates alerts | Generates alerts and enforces policies |

---

# 20. Network Monitoring Tools

| Tool | Primary Use |
|------|-------------|
| SNMP | Device monitoring |
| Syslog | Centralized logging |
| NetFlow/IPFIX | Traffic flow analysis |
| Wireshark | Packet analysis |
| tcpdump | Command-line packet capture |
| SIEM | Log correlation and alerting |

---

# 21. Common Linux Networking Commands

| Command | Purpose |
|----------|---------|
| `ip addr` | View IP addresses |
| `ip route` | View routing table |
| `ping` | Connectivity test |
| `traceroute` | Path analysis |
| `ss -tuln` | View listening sockets |
| `tcpdump` | Capture packets |
| `dig` | DNS lookup |
| `nslookup` | DNS query |
| `curl` | Test HTTP/HTTPS |
| `journalctl` | View system logs |

---

# 22. Common Windows Networking Commands

| Command | Purpose |
|----------|---------|
| `ipconfig /all` | Display IP configuration |
| `ping` | Connectivity test |
| `tracert` | Trace route |
| `pathping` | Path analysis with packet loss |
| `nslookup` | DNS lookup |
| `arp -a` | Display ARP cache |
| `route print` | Display routing table |
| `netstat -ano` | Display active connections |
| `Get-NetIPConfiguration` (PowerShell) | Network configuration |

---

# 23. Wireshark Display Filters

| Filter | Description |
|----------|-------------|
| `ip.addr == x.x.x.x` | Filter by IP address |
| `tcp` | TCP traffic |
| `udp` | UDP traffic |
| `icmp` | ICMP packets |
| `dns` | DNS traffic |
| `http` | HTTP traffic |
| `tls` | TLS traffic |
| `arp` | ARP packets |
| `tcp.port == 443` | HTTPS traffic |
| `tcp.flags.syn == 1` | SYN packets |

---

# 24. Enterprise Troubleshooting Workflow

```
Identify Problem

↓

Determine Scope

↓

Collect Information

↓

Form Hypothesis

↓

Test Hypothesis

↓

Implement Solution

↓

Verify Functionality

↓

Document Findings
```

---

# 25. Security Concepts

| Concept | Purpose |
|----------|---------|
| CIA Triad | Confidentiality, Integrity, Availability |
| AAA | Authentication, Authorization, Accounting |
| Zero Trust | Never Trust, Always Verify |
| Least Privilege | Minimum required access |
| Defense in Depth | Multiple security layers |
| Network Segmentation | Reduce lateral movement |
| MFA | Stronger authentication |

---

# 26. SIEM Investigation Workflow

```
Alert

↓

Validate

↓

Collect Logs

↓

Correlate Events

↓

Investigate

↓

Contain

↓

Recover

↓

Document
```

---

# 27. Root Cause Analysis (RCA)

1. Identify the issue.
2. Gather evidence.
3. Analyze logs and metrics.
4. Determine the underlying cause.
5. Implement corrective actions.
6. Validate the fix.
7. Document lessons learned.

---

# 28. Interview Revision Checklist

Before an interview, review:

- OSI Model
- TCP/IP Model
- IPv4 & IPv6
- Subnetting
- Routing
- Switching
- VLANs
- STP
- ARP
- DHCP
- DNS
- TCP & UDP
- ICMP
- Firewalls
- VPNs
- Wireless networking
- Cloud networking
- Network monitoring
- SIEM
- Detection Engineering
- Troubleshooting methodologies

---

# 29. Enterprise Best Practices

- Follow structured troubleshooting methodologies.
- Keep network diagrams and documentation up to date.
- Centralize logs for faster investigations.
- Synchronize systems using NTP.
- Implement network segmentation.
- Apply the Principle of Least Privilege.
- Test changes before production deployment.
- Monitor continuously using SNMP, NetFlow, Syslog, and SIEM.
- Perform regular backups of device configurations.
- Conduct post-incident reviews to improve operational resilience.

---

# 30. Final Revision Tips

- Understand concepts rather than memorizing definitions.
- Practice subnetting calculations.
- Become comfortable reading routing tables.
- Learn common packet flows (ARP, DHCP, DNS, TCP).
- Practice troubleshooting in virtual labs.
- Explain technical concepts clearly and logically.
- Relate answers to real-world enterprise environments.
- Stay updated with modern networking and security trends.

---

# Congratulations!

You have completed the **Networking** section of the **Cybersecurity Notes** repository.

You now have a comprehensive foundation in:

- Networking Fundamentals
- Enterprise Networking
- Routing & Switching
- IPv4 & IPv6
- DNS, DHCP, TCP, UDP, ICMP
- Firewalls & VPNs
- Wireless Networking
- Cloud Networking
- Network Security
- Network Monitoring
- Network Troubleshooting
- Detection Engineering
- SIEM & SOC Concepts
- Enterprise Interview Preparation

This knowledge provides a strong base for advanced topics such as Ethical Hacking, Penetration Testing, Incident Response, Digital Forensics, Threat Hunting, Cloud Security, and Detection Engineering.