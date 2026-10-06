# Lab: Hypothesis-Driven Authentication Hunt

> Category: Threat Hunting  
> Difficulty: Beginner  
> Estimated Time: 30 minutes  
> Environment: Synthetic event table in this document

## Objective

Practice forming and testing an identity-focused hunt hypothesis using a small synthetic dataset.

## Synthetic Data

| Time (UTC) | User | Source | Result | Application | Note |
|---|---|---|---|---|---|
| 08:00 | alex | 192.0.2.10 | Success | Portal | Usual lab location |
| 08:03 | alex | 192.0.2.10 | Failure | Portal | Single failed attempt |
| 08:05 | alex | 198.51.100.25 | Success | Portal | Unfamiliar synthetic source |
| 08:09 | sam | 198.51.100.25 | Success | Portal | Shared training gateway possible |

Addresses are reserved for documentation and examples; rows are fabricated.

## Procedure

1. Hypothesis: a successful authentication from an unfamiliar source after a failure may warrant validation.
2. Identify the required baseline: user, source, application, device, MFA result, geography quality, and known VPN/proxy ranges.
3. Describe what the table supports and what it cannot establish.
4. Write a query for your available sample data, bounded to a time range; do not ingest real personal data for this exercise.
5. List benign explanations and a next evidence source before calling an event suspicious.

## Expected Results

The sequence for `alex` merits a contextual pivot, not a conclusion of compromise. Shared infrastructure could explain multiple users appearing from the same source.

## Lessons Learned

Hunting conclusions should distinguish anomalies from evidence of malicious activity. See [Threat Hunting](../../Threat-Hunting/) and [IAM](../../Identity-and-Access-Management/).
