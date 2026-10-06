# 🛡️ Security Knowledge Base

<p align="center">
  <img src="https://img.shields.io/badge/Cybersecurity-Knowledge%20Base-63f28a?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Cybersecurity Knowledge Base">
  <img src="https://img.shields.io/badge/Focus-Blue%20Team%20%7C%20AppSec%20%7C%20Cloud%20%7C%20Threat%20Research-111814?style=for-the-badge" alt="Security Focus">
  <img src="https://img.shields.io/badge/Content-674%2B%20Markdown%20Documents-111814?style=for-the-badge&logo=markdown" alt="Markdown Documents">
  <img src="https://img.shields.io/badge/License-MIT-111814?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  <strong>A connected cybersecurity knowledge system for learning, research, detection, investigation, and defensive security engineering.</strong>
</p>

<p align="center">
  <a href="https://anurag-rvnkr1.github.io/Security-Knowledge-Base/">
    <img src="https://img.shields.io/badge/🚀%20EXPLORE%20THE%20LIVE%20PORTAL-63f28a?style=for-the-badge&labelColor=07100b&color=63f28a" alt="Explore Live Portal">
  </a>
  <a href="https://github.com/anurag-rvnkr1/Security-Knowledge-Base">
    <img src="https://img.shields.io/badge/VIEW%20REPOSITORY-111814?style=for-the-badge&logo=github&logoColor=white" alt="View Repository">
  </a>
</p>

---

## 🌐 Explore the Knowledge Base

> ### **The repository is the knowledge. The website is the experience.**

<p align="center">
  <a href="https://anurag-rvnkr1.github.io/Security-Knowledge-Base/">
    <img src="https://img.shields.io/badge/OPEN%20SECURITY%20KNOWLEDGE%20BASE-Visit%20Portfolio%20Site-63f28a?style=for-the-badge&labelColor=0a100c" alt="Open Portfolio Site">
  </a>
</p>

🔗 **Live Website:**  
**https://anurag-rvnkr1.github.io/Security-Knowledge-Base/**

🔗 **GitHub Repository:**  
**https://github.com/anurag-rvnkr1/Security-Knowledge-Base**

The live portal provides a professional interface for exploring the underlying knowledge base, including:

- 🔎 Client-side search
- 🛡️ Security domain explorer
- 📚 Markdown documentation viewer
- 🧪 Practical labs
- 🚩 CTF writeups
- ⚡ Cheatsheets
- 🎯 Learning paths
- 🧭 Threat-hunting and detection material
- 💻 Code and command references
- 🔗 Direct source links to GitHub

---

# 01 — What Is This?

**Security Knowledge Base** is a continuously evolving cybersecurity learning and reference platform.

It brings together foundational security concepts, defensive operations, security engineering, application security, cloud security, threat intelligence, detection engineering, threat hunting, digital forensics, malware analysis, practical labs, CTF writeups, and technical reference material.

The objective is simple:

> **Understand the technology → understand the risk → understand the attack surface → understand the telemetry → detect the behavior → investigate the evidence → improve the defense.**

Rather than treating cybersecurity topics as isolated subjects, this repository connects them into an operational security model.

---

# 02 — The Security Mindset

Cybersecurity is rarely about knowing one tool or memorizing one command.

A strong security practitioner needs to understand how different layers interact.

```text
                         ┌─────────────────────┐
                         │   THREAT ACTORS     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ ATTACK TECHNIQUES   │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
           Endpoint             Identity             Network
                 │                  │                  │
                 └──────────────────┼──────────────────┘
                                    ▼
                              TELEMETRY
                                    │
                                    ▼
                              ┌──────────┐
                              │   SIEM   │
                              └────┬─────┘
                                   │
                                   ▼
                         DETECTION ENGINEERING
                                   │
                                   ▼
                           THREAT HUNTING
                                   │
                                   ▼
                         INCIDENT RESPONSE
                                   │
                                   ▼
                           DIGITAL FORENSICS
                                   │
                                   ▼
                       ARCHITECTURE & HARDENING
```

This repository is designed around those connections.

---

# 03 — Knowledge Domains

## 🔐 Core Security Foundations

| Domain | Focus |
|---|---|
| [OWASP](./OWASP) | Application security principles and common vulnerabilities |
| [Web Security](./Web-Security) | Web application attack surface and defense |
| [API Security](./API-Security) | API threats, authentication, authorization and testing |
| [Networking](./Networking) | Network fundamentals and protocols |
| [Network Security](./Network-Security) | Network defense, monitoring and architecture |
| [Linux](./Linux) | Linux administration and security |
| [Windows](./Windows) | Windows security, logging and administration |
| [Active Directory](./Active-Directory) | Identity infrastructure and enterprise Windows security |
| [Cryptography](./Cryptography) | Cryptographic concepts and secure communication |

---

## 🛡️ Defensive Operations

| Domain | Focus |
|---|---|
| [SIEM](./SIEM) | Security monitoring, analytics and log investigation |
| [SOC](./SOC) | Security operations and analyst workflows |
| [Detection Engineering](./Detection-Engineering) | Detection logic, telemetry and rule development |
| [Threat Hunting](./Threat-Hunting) | Hypothesis-driven investigation |
| [Incident Response](./Incident-Response) | Detection, containment, investigation and recovery |
| [Digital Forensics](./Digital-Forensics) | Evidence and artifact analysis |
| [Endpoint Security](./Endpoint-Security) | Endpoint visibility and protection |
| [Email Security](./Email-Security) | Phishing, email threats and defensive controls |
| [Malware Analysis](./Malware-Analysis) | Malware behavior and artifact analysis |

---

## 🕵️ Threat Intelligence & Research

- [Threat Intelligence](./Threat-Intelligence)
- [MITRE ATT&CK](./MITRE-ATTACK)
- [OSINT](./OSINT)
- [Reverse Engineering](./Reverse-Engineering)

These areas connect adversary behavior, intelligence collection, technical analysis, ATT&CK mapping, hunting hypotheses, and defensive improvement.

---

## ☁️ Security Engineering

- [Cloud Security](./Cloud-Security)
- [Containers](./Containers)
- [Kubernetes](./Kubernetes)
- [DevSecOps](./DevSecOps)
- [Security Architecture](./Security-Architecture)
- [Identity & Access Management](./Identity-and-Access-Management)
- [Vulnerability Management](./Vulnerability-Management)
- [Security Automation](./Security-Automation)

---

# 04 — Practical Security

Knowledge becomes useful when it can be applied.

The repository therefore includes:

### 🧪 Labs

Hands-on security exercises covering practical technologies, workflows, and defensive concepts.

→ [Explore Labs](./Labs/)

### 🚩 CTF Writeups

Practical challenge analysis involving reconnaissance, exploitation, privilege escalation, enumeration, cryptography, forensics, OSINT, reverse engineering, and other security techniques.

→ [Explore CTF Writeups](./CTF-Writeups/)

### ⚡ Cheatsheets

Quick technical references for commands, concepts, workflows, and security operations.

→ [Explore Cheatsheets](./Cheatsheets/)

### 📚 Resources

Curated references, documentation, learning material, tools, standards, and security research.

→ [Explore Resources](./Resources/)

---

# 05 — Connected Learning Paths

The knowledge base can be approached from different professional directions.

## 🛡️ Blue Team

```text
Linux
   ↓
Windows
   ↓
Networking
   ↓
Endpoint Security
   ↓
SIEM
   ↓
Detection Engineering
   ↓
MITRE ATT&CK
   ↓
Threat Hunting
   ↓
Incident Response
   ↓
Digital Forensics
```

## 🚨 SOC Analyst

```text
Networking
      ↓
Windows / Linux
      ↓
Log Analysis
      ↓
SIEM
      ↓
Alert Triage
      ↓
Threat Intelligence
      ↓
Detection Tuning
      ↓
Investigation
      ↓
Escalation & Response
```

## 🎯 Detection Engineer

```text
Telemetry
   ↓
Data Sources
   ↓
Detection Logic
   ↓
Rule Authoring
   ↓
Testing
   ↓
MITRE ATT&CK Mapping
   ↓
Tuning
   ↓
Detection-as-Code
   ↓
Continuous Improvement
```

## 🔎 Threat Hunter

```text
Threat Intelligence
        ↓
Hypothesis
        ↓
Telemetry
        ↓
Query & Investigation
        ↓
Behavior Analysis
        ↓
ATT&CK Mapping
        ↓
Detection Validation
        ↓
Hunting Feedback Loop
```

## 🌐 Application Security

```text
Networking
    ↓
Web Security
    ↓
OWASP
    ↓
API Security
    ↓
Secure SDLC
    ↓
DevSecOps
    ↓
Cloud Security
```

## ☁️ Cloud Security

```text
Cloud Fundamentals
        ↓
IAM
        ↓
Network Security
        ↓
Logging & Observability
        ↓
Containers
        ↓
Kubernetes
        ↓
DevSecOps
        ↓
Supply Chain Security
```

## 🧬 Security Research

```text
OSINT
 ↓
Threat Intelligence
 ↓
IOC Research
 ↓
Malware Analysis
 ↓
Reverse Engineering
 ↓
Adversary Tracking
 ↓
Research-driven Defense
```

---

# 06 — Detection Engineering

Detection engineering is treated as an engineering discipline rather than simply writing alerts.

The knowledge base explores concepts around:

```text
Data Sources
     ↓
Telemetry Coverage
     ↓
Detection Hypothesis
     ↓
Detection Logic
     ↓
Rule Development
     ↓
Testing
     ↓
ATT&CK Mapping
     ↓
Tuning
     ↓
Deployment
     ↓
Monitoring
     ↓
Continuous Improvement
```

This creates a connection between:

**telemetry → analytics → detection → investigation → response**

---

# 07 — Threat Hunting

Threat hunting focuses on proactively searching for suspicious behavior that may not yet have triggered a detection.

Core concepts include:

- hypothesis-driven hunting
- endpoint telemetry
- network telemetry
- identity telemetry
- cloud telemetry
- adversary behavior
- ATT&CK mapping
- anomaly investigation
- detection validation
- hunting-to-detection feedback loops

The objective is not simply to find an indicator.

> **The objective is to understand behavior.**

---

# 08 — MITRE ATT&CK as a Common Language

MITRE ATT&CK provides a common framework connecting multiple parts of the repository.

It can be used to connect:

```text
Threat Intelligence
       ↓
Adversary Behavior
       ↓
ATT&CK Techniques
       ↓
Detection Opportunities
       ↓
Threat Hunting
       ↓
Incident Investigation
       ↓
Security Architecture
```

This makes ATT&CK useful not just as a reference catalogue, but as a bridge between offensive behavior and defensive engineering.

---

# 09 — Repository Architecture

```text
Security-Knowledge-Base/
│
├── OWASP/
├── Web-Security/
├── API-Security/
│
├── Networking/
├── Network-Security/
├── Linux/
├── Windows/
├── Active-Directory/
├── Cryptography/
│
├── SIEM/
├── SOC/
├── Detection-Engineering/
├── Threat-Hunting/
├── Incident-Response/
├── Digital-Forensics/
├── Endpoint-Security/
├── Email-Security/
├── Malware-Analysis/
│
├── Threat-Intelligence/
├── MITRE-ATTACK/
├── OSINT/
├── Reverse-Engineering/
│
├── Cloud-Security/
├── Containers/
├── Kubernetes/
├── DevSecOps/
├── Security-Architecture/
├── Identity-and-Access-Management/
├── Vulnerability-Management/
├── Security-Automation/
│
├── CTF-Writeups/
├── Labs/
├── Cheatsheets/
├── Resources/
│
├── assets/
├── docs/
│
├── index.html
├── site/
├── scripts/
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
└── CHANGELOG.md
```

The repository currently contains **674+ Markdown documents**, making the GitHub Pages portal the preferred way to navigate the knowledge base.

---

# 10 — The Portfolio Experience

The repository is backed by a dedicated static cybersecurity portal.

### 🌐 Security Knowledge Base Portal

**https://anurag-rvnkr1.github.io/Security-Knowledge-Base/**

The website transforms the repository from a conventional GitHub documentation tree into an interactive knowledge platform.

### Portal features

```text
┌──────────────────────────────────────────────┐
│          SECURITY KNOWLEDGE BASE              │
│                                              │
│  Search XSS, Kerberos, SIEM, KQL, Malware…  │
│                                              │
│  [ Explore ]        [ GitHub Repository ]   │
└──────────────────────────────────────────────┘

              ↓

      DOMAIN EXPLORER
              ↓
    ┌─────────┼─────────┐
    │         │         │
   SOC      AppSec    Cloud
    │         │         │
    └─────────┼─────────┘
              ↓
        DOCUMENT VIEWER
              ↓
       SEARCH + TOC + CODE
              ↓
       ORIGINAL MARKDOWN
```

### Built with

- HTML5
- CSS3
- Vanilla JavaScript
- Markdown rendering
- DOM sanitization
- Static GitHub Pages
- Client-side search

No backend or database is required.

---

# 11 — Security Documentation Philosophy

Each topic should answer more than:

> **"What is this?"**

Where appropriate, the knowledge base aims to answer:

```text
What is it?
     ↓
Why does it matter?
     ↓
How does it work?
     ↓
Where does it appear?
     ↓
How can it be abused?
     ↓
What telemetry does it generate?
     ↓
How can defenders detect it?
     ↓
How can it be investigated?
     ↓
How can the risk be reduced?
```

This approach helps connect theoretical knowledge with practical security operations.

---

# 12 — Operational Areas

The repository connects knowledge across:

### Security Operations

- SIEM
- SOC
- EDR / XDR concepts
- alert triage
- log analysis
- case investigation
- incident response

### Detection & Analytics

- detection engineering
- detection logic
- telemetry
- rule testing
- tuning
- ATT&CK mapping
- hunting

### Threat Intelligence

- threat actors
- indicators
- infrastructure
- intelligence enrichment
- OSINT
- adversary behavior

### Security Engineering

- cloud security
- IAM
- network security
- secure architecture
- vulnerability management
- DevSecOps
- automation

### Application Security

- OWASP
- web security
- API security
- secure SDLC
- application testing
- cloud-native security

---

# 13 — References & Standards

The repository connects its learning material with authoritative sources including:

- [MITRE ATT&CK](https://attack.mitre.org/)
- [NIST](https://www.nist.gov/cybersecurity)
- [CISA](https://www.cisa.gov/)
- [OWASP](https://owasp.org/)
- [Microsoft Learn](https://learn.microsoft.com/)
- [AWS Security](https://aws.amazon.com/security/)
- [Google Cloud Security](https://cloud.google.com/security)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [CIS](https://www.cisecurity.org/)
- [FIRST](https://www.first.org/)

---

# 14 — Documentation & Contribution

This project is intended to evolve continuously.

Contributions that improve:

- technical accuracy
- defensive relevance
- clarity
- organization
- documentation quality
- practical usefulness
- security rigor

are welcome.

Before contributing, review:

- [Contributing Guide](./CONTRIBUTING.md)
- [Security Policy](./SECURITY.md)
- [Documentation Guides](./docs/)
- [Responsible Use](./docs/Responsible-Use.md)

---

# 15 — Responsible Use

This repository contains security concepts and techniques that may be dual-use.

All offensive testing, exploitation, enumeration, reverse engineering, malware analysis, and security research should be performed only within:

- authorized labs
- CTF environments
- controlled research environments
- defensive testing engagements
- systems for which explicit authorization exists

Always comply with applicable laws, organizational policies, and scope restrictions.

---

# 16 — Roadmap

The knowledge base is continuously evolving.

### Current direction

- Expand security domain coverage
- Improve cross-domain connections
- Expand practical labs
- Develop more detection engineering material
- Improve threat-hunting workflows
- Expand DFIR references
- Improve cloud and Kubernetes security coverage
- Build stronger learning paths
- Maintain technical references
- Improve the GitHub Pages experience
- Keep documentation synchronized with the underlying repository

---

# 17 — Why This Repository Exists

Cybersecurity is too interconnected to learn as isolated command lists.

A suspicious PowerShell process can become:

```text
Endpoint Activity
      ↓
Windows Telemetry
      ↓
SIEM Event
      ↓
Detection Rule
      ↓
ATT&CK Technique
      ↓
Threat Hunt
      ↓
Incident Investigation
      ↓
Forensic Evidence
      ↓
Containment
      ↓
Architecture Improvement
```

The purpose of this knowledge base is to make those connections visible.

> **Learn the technology. Understand the threat. Read the telemetry. Build the detection. Investigate the evidence. Improve the defense.**

---

# 18 — Explore

<p align="center">

### 🚀 Start with the interactive portal

<a href="https://anurag-rvnkr1.github.io/Security-Knowledge-Base/">
<img src="https://img.shields.io/badge/OPEN%20SECURITY%20KNOWLEDGE%20BASE-63f28a?style=for-the-badge&labelColor=07100b" alt="Open Security Knowledge Base">
</a>

<br><br>

<a href="https://github.com/anurag-rvnkr1/Security-Knowledge-Base">
<img src="https://img.shields.io/badge/EXPLORE%20THE%20SOURCE%20REPOSITORY-111814?style=for-the-badge&logo=github" alt="Explore Repository">
</a>

</p>

---

## 📌 Repository

**GitHub:**  
https://github.com/anurag-rvnkr1/Security-Knowledge-Base

**Portfolio / Knowledge Portal:**  
https://anurag-rvnkr1.github.io/Security-Knowledge-Base/

---

<p align="center">
  <strong>Security Knowledge Base</strong>
  <br>
  Learn • Research • Detect • Hunt • Investigate • Defend
  <br><br>
  <sub>Built as an evolving cybersecurity learning and technical reference project.</sub>
</p>
