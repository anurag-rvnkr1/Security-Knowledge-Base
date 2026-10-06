# CTF Writeups

## Overview

This section documents challenge-solving approaches, evidence, tools, and lessons learned from Capture The Flag (CTF) competitions and deliberately vulnerable training environments.

## Purpose

Writeups help learners explain their reasoning and help defenders recognize security failures. They are intended for authorized CTFs, security labs, educational environments, defensive learning, and security research. They are not permission to test real systems.

## Categories

- [Web](./Web/README.md) — web application behavior and security flaws.
- [Network](./Network/README.md) — protocols, packet analysis, and network services.
- [Linux](./Linux/README.md) — Linux host and service challenges.
- [Windows](./Windows/README.md) — Windows artifacts and host security challenges.
- [Active Directory](./Active-Directory/README.md) — directory services and identity labs.
- [Cryptography](./Cryptography/README.md) — cryptographic concepts and puzzle analysis.
- [Forensics](./Forensics/README.md) — file, disk, memory, and network evidence.
- [Steganography](./Steganography/README.md) — hidden data in media and file formats.
- [Reverse Engineering](./Reverse-Engineering/README.md) — authorized analysis of challenge binaries.
- [OSINT](./OSINT/README.md) — public-data puzzles and source validation.
- [Miscellaneous](./Misc/README.md) — challenges that span or do not fit other areas.

Use the [writeup template](./WRITEUP-TEMPLATE.md) as a starting point, adapting or omitting sections that do not apply.

## Recommended Learning Path

Start with web, Linux, and network fundamentals; then practice forensics and Windows; progress to Active Directory, reverse engineering, cryptography, and multi-stage challenges. Record the evidence and reasoning at each step.

## Writeup Structure

A useful writeup states the challenge scope, objective, environment, method, key evidence, result, defensive implications, and lessons learned. Redact credentials, tokens, personal data, and sensitive platform details. Do not publish flags where competition rules prohibit it.

## Methodology

1. Read the rules and confirm the authorized target and scope.
2. Record the challenge prompt, constraints, and starting artifacts.
3. Enumerate methodically and preserve useful observations.
4. Form and test hypotheses using the least risky approach.
5. Validate the result, explain the reasoning, and note alternatives.
6. Add defensive observations and cite references.

## Tools

Typical tools include a browser and developer tools, Wireshark, `file`, `strings`, CyberChef, a hex viewer, GDB, Python, and platform-provided consoles. Use only tools appropriate to the permitted challenge scope.

## Skills Developed

Structured problem solving, protocol and artifact analysis, scripting, evidence handling, technical writing, and translating attack behavior into defensive controls and detections.

## Responsible Use

Stay within the event rules and authorized lab boundary. Do not reuse techniques against public or third-party systems, disclose real secrets, or publish sensitive information. Follow responsible disclosure for issues discovered outside a CTF.

## References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [NIST Computer Security Resource Center](https://csrc.nist.gov/)
- [CISA Secure Our World](https://www.cisa.gov/secure-our-world)
