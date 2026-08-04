# Chapter 17 – CronJobs

## Overview

A **CronJob** is a Kubernetes workload controller that creates **Jobs on a scheduled basis**.

Think of a CronJob as a scheduler.

```
CronJob

↓

Creates Job

↓

Job Creates Pod

↓

Pod Executes Task

↓

Task Completes
```

A CronJob is equivalent to the Linux **cron** utility but runs inside a Kubernetes cluster.

It is commonly used for:

- Database backups
- Log cleanup
- Report generation
- Data synchronization
- Email notifications
- Cache cleanup
- Certificate renewal
- Scheduled batch processing

---

# Learning Objectives

After completing this chapter, you will understand:

- What a CronJob is
- Why CronJobs are needed
- CronJob Architecture
- Cron Schedule Format
- CronJob Lifecycle
- Concurrency Policies
- Missed Schedules
- Suspend & Resume
- Cleanup Policies
- Best Practices

---

# Why CronJobs?

Imagine a database backup.

Without CronJob:

```
Administrator

↓

Run Backup

↓

Every Night
```

This requires manual intervention.

Or use:

```
Linux Cron

↓

Runs on One Server
```

Problem:

- Not Kubernetes-native
- Difficult to manage
- Not portable

---

# Solution

Use a Kubernetes CronJob.

```
Every Midnight

↓

CronJob

↓

Backup Job

↓

Backup Completed
```

---

# What is a CronJob?

A CronJob is a controller that **creates Jobs according to a schedule**.

```
CronJob

↓

Schedule

↓

Job

↓

Pod

↓

Task

↓

Complete
```

---

# CronJob Architecture

```
               CronJob

                   │

              Schedule

                   │

                   ▼

                 Job

                   │

                   ▼

                  Pod

                   │

                   ▼

             Execute Task
```

---

# CronJob vs Job

| Job | CronJob |
|------|----------|
| Runs once | Runs repeatedly |
| Manual execution | Automatic schedule |
| One-time task | Recurring task |
| No schedule | Cron schedule |

---

# CronJob Workflow

```
Time Reached

↓

CronJob

↓

Create Job

↓

Create Pod

↓

Execute Task

↓

Complete
```

---

# Cron Schedule Format

General format:

```
* * * * *
│ │ │ │ │
│ │ │ │ └── Day of Week
│ │ │ └──── Month
│ │ └────── Day of Month
│ └──────── Hour
└────────── Minute
```

---

# Common Cron Expressions

| Schedule | Meaning |
|-----------|---------|
| `* * * * *` | Every minute |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour |
| `0 0 * * *` | Every day at midnight |
| `0 2 * * *` | Every day at 2:00 AM |
| `0 0 * * 0` | Every Sunday |
| `0 9 * * 1-5` | Weekdays at 9:00 AM |
| `30 23 1 * *` | 11:30 PM on the first day of every month |

---

# CronJob YAML

```yaml
apiVersion: batch/v1

kind: CronJob

metadata:

  name: backup-job

spec:

  schedule: "0 2 * * *"

  jobTemplate:

    spec:

      template:

        spec:

          restartPolicy: Never

          containers:

          - name: backup

            image: busybox

            command:

            - echo

            - "Running Backup"
```

---

# YAML Structure

```
CronJob

↓

Schedule

↓

Job Template

↓

Pod Template

↓

Container
```

---

# Execution Timeline

```
02:00

↓

CronJob

↓

Job Created

↓

Pod Created

↓

Backup

↓

Complete
```

---

# Job Creation

Important:

A CronJob does **not** execute Pods directly.

It creates:

```
CronJob

↓

Job

↓

Pod
```

Exactly like manually creating a Job.

---

# Suspend CronJob

Pause scheduling.

Example:

```yaml
suspend: true
```

Result:

```
CronJob Exists

↓

No New Jobs
```

Resume:

```yaml
suspend: false
```

---

# Concurrency Policy

Controls what happens when the next schedule occurs before the previous Job has finished.

Three options:

```
Allow

Forbid

Replace
```

---

# Allow

Default behavior.

```
Job 1

Running

↓

Job 2 Starts

↓

Both Run
```

---

# Forbid

```
Job 1

Running

↓

Next Schedule

↓

Skipped
```

No overlapping Jobs.

---

# Replace

```
Job 1

Running

↓

Terminate

↓

Job 2 Starts
```

Useful when only the latest execution matters.

---

# startingDeadlineSeconds

Defines how long Kubernetes should wait to start a missed Job.

Example:

```yaml
startingDeadlineSeconds: 300
```

Workflow:

```
Schedule Missed

↓

Within 5 Minutes

↓

Run Job
```

If the deadline passes:

```
Skip Job
```

---

# Successful Job History

Keep successful Jobs.

Example:

```yaml
successfulJobsHistoryLimit: 3
```

Result:

```
Latest

3

Successful Jobs
```

Older successful Jobs are removed.

---

# Failed Job History

Example:

```yaml
failedJobsHistoryLimit: 1
```

Keep only the most recent failed Job.

---

# Time Zone Support

Modern Kubernetes versions support:

```yaml
timeZone: "Asia/Kolkata"
```

Without specifying a time zone, scheduling uses the time zone configured for the Kubernetes control plane.

---

# CronJob Lifecycle

```
Create

↓

Wait for Schedule

↓

Create Job

↓

Create Pod

↓

Execute

↓

Complete

↓

Cleanup

↓

Wait for Next Schedule
```

---

# Viewing CronJobs

List:

```bash
kubectl get cronjobs
```

or

```bash
kubectl get cj
```

Describe:

```bash
kubectl describe cronjob backup-job
```

---

# Viewing Jobs

```bash
kubectl get jobs
```

---

# Viewing Pods

```bash
kubectl get pods
```

---

# Logs

Latest Job:

```bash
kubectl logs job/<job-name>
```

---

# Deleting CronJob

```bash
kubectl delete cronjob backup-job
```

Deleting the CronJob prevents future Jobs from being scheduled. Existing Jobs are not automatically removed.

---

# Common Use Cases

## Database Backup

```
02:00 AM

↓

CronJob

↓

Backup
```

---

## Log Cleanup

```
Every Night

↓

Delete Logs
```

---

## Cache Cleanup

```
Every Hour

↓

Clear Cache
```

---

## Email Reports

```
08:00 AM

↓

Generate Report

↓

Send Email
```

---

## ETL Jobs

```
Every Midnight

↓

Import Data
```

---

## Certificate Renewal

```
Monthly

↓

Renew Certificates
```

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f cronjob.yaml
```

View:

```bash
kubectl get cronjobs
```

Describe:

```bash
kubectl describe cronjob backup-job
```

Suspend:

```bash
kubectl patch cronjob backup-job \
-p '{"spec":{"suspend":true}}'
```

Resume:

```bash
kubectl patch cronjob backup-job \
-p '{"spec":{"suspend":false}}'
```

Delete:

```bash
kubectl delete cronjob backup-job
```

---

# CronJob Architecture Summary

```
CronJob

↓

Schedule

↓

Job

↓

Pod

↓

Task

↓

Completion
```

---

# Best Practices

### 1. Use CronJobs Only for Scheduled Tasks

Examples:

- Backups
- Reports
- Cleanup
- Maintenance

---

### 2. Configure Concurrency Policy

Choose:

- Allow
- Forbid
- Replace

based on workload requirements.

---

### 3. Limit Job History

Prevent excessive accumulation of completed Jobs by configuring history limits.

---

### 4. Set startingDeadlineSeconds

Handle missed schedules gracefully, especially after controller downtime.

---

### 5. Monitor Job Failures

Regularly inspect failed Jobs and their logs to identify recurring issues.

---

## Next Section

How CronJobs Work Internally

Cron Schedule Deep Dive

Concurrency Policies

Hands-on Labs

Common Mistakes

Quick Revision

References

---