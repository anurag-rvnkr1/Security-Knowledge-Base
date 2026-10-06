# Lab: Validate a Detection with Synthetic Events

> Category: Detection Engineering  
> Difficulty: Beginner  
> Estimated Time: 30 minutes  
> Environment: Text editor or local notebook; synthetic data only

## Objective

Define a detection hypothesis and test whether its proposed logic distinguishes synthetic positive and benign events.

## Synthetic Events

| Time (UTC) | Host | Process | Parent | User | Context |
|---|---|---|---|---|---|
| 10:00 | LAB-01 | `inventory.exe` | `services.exe` | SYSTEM | Approved inventory agent |
| 10:05 | LAB-01 | `cmd.exe` | `inventory.exe` | SYSTEM | Synthetic unexpected child process |
| 10:08 | LAB-02 | `cmd.exe` | `explorer.exe` | analyst | Analyst opened a local shell |

These rows are invented training data, not real indicators or event records.

## Procedure

1. State a hypothesis specific enough to be testable. For example: an approved service agent unexpectedly launches an interactive command interpreter.
2. Define required fields and note that a process tree, signer, command line, and change ticket would be needed for operational confidence.
3. Mark which rows satisfy the initial condition and which benign alternatives exist.
4. Draft a detection in a query or rule format supported by your lab. Do not deploy it based only on these three rows.
5. Record expected positives, false positives, missing context, and a test plan using a larger representative dataset.

## Expected Results

The second row matches the illustrative parent-child behavior; the first is a baseline, and the third shows why a child process alone is too broad. Context and data quality determine whether an alert is actionable.

## Lessons Learned

Document objective, telemetry, logic, limitations, and tuning plan. See [Detection Engineering](../../Detection-Engineering/) and [MITRE ATT&CK](../../MITRE-ATTACK/).
