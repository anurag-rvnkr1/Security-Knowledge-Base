# Security Research Methodology

Use a documented, reproducible process for vulnerability, threat, malware, detection, and security-engineering research.

```text
Research Question → Scope → Threat Model → Environment → Data Collection
→ Analysis → Validation → Documentation → Findings → Mitigation → Responsible Disclosure
```

1. **Question:** State what is unknown and what evidence would answer it.
2. **Scope:** Identify systems, datasets, users, and actions explicitly authorized.
3. **Threat model:** Define assets, trust boundaries, adversary assumptions, and impact.
4. **Environment:** Prefer isolated systems, synthetic data, and recorded versions.
5. **Collection:** Use the least intrusive method; record provenance and timestamps.
6. **Analysis:** Separate observations from assumptions and hypotheses.
7. **Validation:** Reproduce findings safely and consider alternative explanations.
8. **Documentation:** Preserve relevant evidence, methodology, limitations, and tool versions.
9. **Mitigation:** Explain practical risk reduction and residual risk.
10. **Disclosure:** Report affected parties privately and follow coordinated disclosure expectations.

Never publish credentials, personal information, or unapproved exploit details.
