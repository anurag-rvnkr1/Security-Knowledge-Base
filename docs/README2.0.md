# Security Knowledge Base

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Portal-63f28a?style=flat-square&logo=github)](https://anurag-rvnkr1.github.io/Security-Knowledge-Base/)
[![License](https://img.shields.io/badge/License-MIT-63f28a?style=flat-square)](LICENSE)

> A structured, evolving cybersecurity knowledge base covering security foundations, application and cloud security, defensive operations, threat research, practical labs, cheatsheets, and technical reference.

**Live portal:** https://anurag-rvnkr1.github.io/Security-Knowledge-Base/

**Repository:** https://github.com/anurag-rvnkr1/Security-Knowledge-Base

## Mission

This repository is a practical learning and reference system. Its Markdown documents are authoritative. The GitHub Pages application is a presentation, search, navigation, and document-viewing layer over those source files.

## Knowledge Domains

The repository currently contains dedicated collections for API Security, Active Directory, Cloud Security, Containers, Cryptography, Detection Engineering, DevSecOps, Digital Forensics, Email Security, Endpoint Security, Identity and Access Management, Incident Response, Kubernetes, Linux, MITRE ATT&CK, Malware Analysis, Network Security, Networking, OSINT, OWASP, Reverse Engineering, Security Architecture, Security Automation, SIEM, SOC, Threat Hunting, Threat Intelligence, Vulnerability Management, Web Security, and Windows.

It also contains CTF Writeups, Labs, Cheatsheets, Resources, reusable assets, and documentation guides.

## Repository Structure

```text
Security-Knowledge-Base/
├── index.html
├── assets/
│   ├── css/style.css
│   ├── js/app.js
│   ├── diagrams/
│   ├── images/
│   ├── icons/
│   └── templates/
├── site/content.json
├── scripts/build-content-index.py
├── docs/
├── CTF-Writeups/
├── Labs/
├── Cheatsheets/
├── Resources/
└── security-domain collections/
```

## Learning Paths

Existing guidance connects Cybersecurity Fundamentals, SOC Analyst, Blue Team, Application Security, Cloud Security, and DFIR paths. See [docs/Learning-Paths.md](docs/Learning-Paths.md).

## Website Architecture

The portal is deliberately static:

- HTML5
- CSS3
- Vanilla JavaScript
- `site/content.json`
- `marked` for Markdown parsing
- `DOMPurify` for sanitization
- GitHub Pages from `main / (root)`

No Node.js, React, Vue, backend server, database, or Jekyll plugin is required.

The viewer uses query-string state such as:

```text
index.html?doc=Active-Directory%2F01-Introduction-to-Active-Directory.md
```

This keeps refresh and browser history usable on GitHub Pages.

## Maintaining the Content Index

When Markdown files are added, removed, or renamed, run from the repository root:

```bash
python scripts/build-content-index.py
```

Review `site/content.json`, then commit it with the source changes. The script uses only the Python standard library and preserves spaces and punctuation in real repository paths.

## Local Testing

```bash
python -m http.server 8000
```

Open http://localhost:8000/.

Do not use a `file://` URL because the site uses browser `fetch()` for its content index and Markdown documents.

## Practical Material

- **CTF Writeups:** challenge material for authorized environments.
- **Labs:** controlled practical exercises and worksheets.
- **Cheatsheets:** compact technical references.
- **Resources:** courses, tools, standards, research and practice platforms.
- **Detection Engineering / Threat Hunting / DFIR:** defensive operational knowledge and workflows.

## Responsible Use

Security testing and offensive techniques are intended only for authorized labs, CTF environments, controlled research, defensive testing, and systems where permission exists. Read [docs/Responsible-Use.md](docs/Responsible-Use.md).

## Contributing

See [Contributing.md](Contributing.md) and the documentation guides under [docs/](docs/).

## Roadmap

- Continue expanding the knowledge collections.
- Keep practical material organized by domain.
- Improve cross-domain learning paths.
- Keep the portal index synchronized with Markdown.
- Continue improving accessibility, search, and documentation UX.

## License

[MIT License](LICENSE)

## Disclaimer

This is a learning and reference project. It does not claim professional certification, employment experience, or permission to test third-party systems. Always obtain appropriate authorization before security testing.
