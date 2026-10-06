# Endpoint-Security

## Overview

Endpoint security focuses on protecting workstations, servers, mobile devices, and cloud-connected endpoints from malware, misuse, persistence, and credential theft.

---

## Why It Matters

Endpoint security matters because many incidents begin on endpoints and expand through identity, network, and application layers. Endpoints are both high-value and highly observable.

---

## Core Concepts

- Core models and terminology
- Operational workflows and control points
- Threat-informed detection and monitoring
- Risk reduction and defensive engineering
- Validation, investigation, and response

---

## Key Technologies

- Security telemetry and event sources
- Detection logic and alerting workflows
- Defensive controls and response playbooks
- Threat-informed operations and risk reduction

---

## Common Attack Techniques

- Credential abuse and identity manipulation
- Abuse of legitimate tooling and valid accounts
- Initial access, persistence, and privilege escalation
- Data staging, exfiltration, and evasion
- Supply-chain, cloud, and application-layer abuse

---

## Defensive Techniques

- Detection engineering and validation
- Telemetry improvement and coverage gaps analysis
- Identity and access hardening
- Segmentation, alerting, and response automation
- Risk prioritization and continuous improvement

---

## Detection Opportunities

- Endpoint telemetry and process lineage
- Authentication and identity events
- Network flow, DNS, proxy, and firewall logs
- Cloud control plane activity
- Application and API access analytics

---

## Investigation Methodology

1. Establish scope and confirm the alert or behavior.
2. Correlate telemetry across identity, endpoint, network, and cloud data.
3. Review actor behavior, privileges, and timelines.
4. Validate whether an adversary or automation is involved.
5. Capture evidence, reduce risk, and document lessons learned.

---

## Tools

- SIEM and analytics platforms
- Threat intel feeds and enrichment
- Endpoint, identity, network, and cloud telemetry
- Automation and case management tools
- Reference frameworks such as MITRE ATT&CK and NIST

---

## Commands / Examples

```bash
# Example: inspect a known IOC or validate a suspicious artifact
whois example.com
nslookup example.com
curl -I https://example.com
```

```bash
# Example: search a repository for related references
grep -R "credential theft" .
```

---

## Practical Scenarios

A defender can use this domain to identify suspicious behavior across environment telemetry, generate hypotheses, validate detection coverage, and close gaps before adversaries achieve impact.

---

## Related MITRE ATT&CK Techniques

- T1059 - Command and Scripting Interpreter
- T1078 - Valid Accounts
- T1566 - Phishing
- T1583 - Acquire Infrastructure
- Tactic mapping varies by implementation and environment

---

## Learning Path

1. Learn the fundamentals and terminology.
2. Map the domain to the wider security stack.
3. Build detection and investigation workflows.
4. Practice with real telemetry and case-based scenarios.
5. Integrate the knowledge into SOC, cloud, or engineering operations.

---

## Related Knowledge Base Topics

- [Windows](../Windows/README.md)
- [Linux](../Linux/README.md)
- [Malware Analysis](../Malware-Analysis/README.md)
- [SIEM](../SIEM/Readme.md)

---

## References

- MITRE ATT&CK
- NIST
- CISA
- Microsoft Learn
- OWASP
- Official vendor documentation

---

## Responsible Use

This content is intended for defensive, educational, and authorized security research use in controlled or authorized environments.
