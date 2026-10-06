# Lab: Analyze Synthetic Authentication Events

> Category: SIEM  
> Difficulty: Beginner  
> Estimated Time: 25 minutes  
> Environment: Spreadsheet or SIEM training workspace

## Objective

Explore a small synthetic event set and design a bounded query for unusual authentication patterns.

## Synthetic Dataset

| Time (UTC) | User | Host | Result | Source |
|---|---|---|---|---|
| 11:00 | trainee-a | LAB-01 | Success | 192.0.2.21 |
| 11:02 | trainee-a | LAB-01 | Failure | 192.0.2.21 |
| 11:04 | trainee-a | LAB-01 | Failure | 192.0.2.21 |
| 11:10 | trainee-b | LAB-02 | Success | 192.0.2.22 |

All rows are fabricated and use documentation-only IP ranges.

## Procedure

1. Load the table into a spreadsheet or training workspace with an explicit schema.
2. Count successes and failures by user and source.
3. Choose a time window and define a threshold only as a test hypothesis.
4. Identify benign explanations and fields missing for production triage, such as authentication method, device, MFA outcome, and account type.
5. Save the query and record its assumed table and column names.

## Expected Results

The first synthetic user has two failures followed by one success. This sequence can be highlighted for review but is not proof of password guessing or compromise.

## Cleanup

Delete the synthetic workspace or dataset using its documented controls. No real logs should be uploaded.

## Further Practice

Compare a short and long time window and describe how thresholds affect detection and false positives. See [SIEM](../../SIEM/).
