# Lab: Build a Linux Host Baseline

> Category: Linux Security  
> Difficulty: Beginner  
> Estimated Time: 25 minutes  
> Environment: Linux host or disposable VM

## Objective

Collect a small read-only baseline of identity, processes, listeners, storage, and recent service logs; identify unknowns that need validation.

## Procedure

Run the following commands and save only output that is approved for your environment:

```bash
date -Is
hostnamectl
id
ps -eo user,pid,ppid,comm --sort=pid | head -n 25
ss -lntup
df -h
```

If systemd is available, inspect recent system messages with `journalctl --since '1 hour ago' --no-pager | tail -n 100`. Do not assume a message is malicious solely because it is unfamiliar.

## Analysis

For each listener or process of interest, identify its owner, purpose, expected network exposure, and authoritative source for expected behavior. Record the host's timezone and any visibility limitations.

## Expected Results

The commands return a snapshot of the current host. Output varies by distribution, permissions, running services, and init system.

## Safety and Cleanup

These commands are intended to be read-only. Protect exported output because it can contain usernames, process names, and internal addresses. Remove any temporary notes according to local policy.

## Further Practice

Repeat on a disposable VM before and after installing a known service, then compare the listener and process deltas. See [Linux](../../Linux/) and [Endpoint Security](../../Endpoint-Security/).
