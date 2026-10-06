# Cybersecurity Labs

## Overview

This section organizes hands-on exercises for controlled security learning, investigation, detection validation, and experimentation. Existing in-depth labs remain in their domain chapters; this section provides reusable templates, focused exercises, and a navigation layer.

## Objectives

- Practice with controlled systems and synthetic or intentionally vulnerable data.
- Connect technical observations to defensive controls and detections.
- Document repeatable setup, expected results, cleanup, and lessons learned.

## Lab Categories

- [Web Security](./Web-Security/README.md)
- [Network Security](./Network-Security/README.md)
- [Linux Security](./Linux-Security/README.md)
- [Windows Security](./Windows-Security/README.md)
- [Active Directory](./Active-Directory/README.md)
- [Cloud Security](./Cloud-Security/README.md)
- [Detection Engineering](./Detection-Engineering/README.md)
- [Threat Hunting](./Threat-Hunting/README.md)
- [Digital Forensics](./Digital-Forensics/README.md)
- [Malware Analysis](./Malware-Analysis/README.md)
- [Incident Response](./Incident-Response/README.md)
- [SIEM](./SIEM/README.md)
- [Security Automation](./Security-Automation/README.md)

## Recommended Learning Paths

- **SOC:** Linux and Windows logs → SIEM investigation → detection engineering → threat hunting → incident response.
- **Application security:** web fundamentals → API security → secure development → isolated web testing.
- **DFIR:** evidence handling → endpoint artifacts → timeline analysis → incident response.
- **Cloud defense:** cloud identity and logging → cloud detections → investigation and containment.

## Lab Environment

Prefer disposable virtual machines, local containers, synthetic logs, and vendor training tenants. Isolate intentionally vulnerable targets from production networks and the public internet. Review provider terms before using hosted environments.

## Safety Requirements

Obtain authorization, define scope, use test data, keep secrets out of notes, avoid uncontrolled malware execution, and plan cleanup before starting. Do not expose vulnerable services publicly.

## Documentation Standard

Use [LAB-TEMPLATE.md](./LAB-TEMPLATE.md). Include objective, prerequisites, architecture, setup, steps, expected results, evidence, detection/defense, cleanup, and references. Mark optional or environment-dependent steps.

## Tools

Common tools include virtual machines, containers, packet analyzers, endpoint telemetry, log platforms, and scripting languages. Use tools only within the defined lab boundary.

## Skills Covered

Asset and log analysis, protocol understanding, hypothesis testing, detection design, incident triage, evidence preservation, and security communication.

## Responsible Use

Labs are for authorized learning in controlled environments. Testing a system outside the lab requires explicit permission from its owner.

## References

- [NIST NICE Framework](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CISA Cybersecurity Training & Exercises](https://www.cisa.gov/resources-tools/training)
- [Existing Kubernetes labs](../Kubernetes/86-Hands-on-Labs.md)
- [Existing container labs](../Containers/19-Hands-on-Labs.md)
