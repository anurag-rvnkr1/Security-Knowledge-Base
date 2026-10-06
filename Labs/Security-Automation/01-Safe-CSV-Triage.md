# Lab: Safe CSV Alert Triage

> Category: Security Automation  
> Difficulty: Beginner  
> Estimated Time: 25 minutes  
> Environment: Python 3 and a local synthetic CSV

## Objective

Read a small local CSV and summarize alert counts without network access or automated response actions.

## Setup

Create `alerts.csv` with this synthetic content:

```csv
id,severity,status
LAB-001,medium,open
LAB-002,high,open
LAB-003,low,closed
```

## Procedure

Run the following Python snippet from the directory containing the file:

```python
import csv
from collections import Counter

with open("alerts.csv", newline="", encoding="utf-8") as source:
    rows = list(csv.DictReader(source))

if not rows or any(not row.get("severity") or not row.get("status") for row in rows):
    raise ValueError("CSV is empty or missing required fields")

print("By severity:", dict(Counter(row["severity"] for row in rows)))
print("By status:", dict(Counter(row["status"] for row in rows)))
```

## Expected Results

The summary reports one row at each severity and two open, one closed. Ordering of dictionary output may vary by Python version.

## Safety Considerations

The script only reads the local training CSV and prints counts. It makes no network calls and takes no response actions. Do not extend an automation exercise to disable accounts or isolate hosts without authorization, safeguards, and human approval.

## Cleanup

Remove the specific synthetic CSV when finished.
