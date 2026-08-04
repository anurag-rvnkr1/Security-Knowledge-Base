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

# How CronJobs Work Internally

## Overview

A CronJob is one of the most automated workload controllers in Kubernetes.

Unlike a Job, which starts immediately after creation, a CronJob continuously watches the current time and creates new Jobs whenever the configured schedule matches.

Internally, the following Kubernetes components work together:

- CronJob Controller
- API Server
- etcd
- Job Controller
- Scheduler
- kubelet
- Worker Nodes

A CronJob itself **never executes application code**.

Instead, it creates a **Job**, and that Job creates one or more **Pods**.

---

# High-Level Architecture

```
                  CronJob

                     │

             Cron Schedule

                     │

                     ▼

           CronJob Controller

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

# Complete Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Store CronJob

↓

CronJob Controller

↓

Check Time

↓

Schedule Matches?

↓

Yes

↓

Create Job

↓

Job Controller

↓

Create Pod

↓

Scheduler

↓

Node

↓

kubelet

↓

Container

↓

Task Complete
```

---

# Step 1 – Create CronJob

Example:

```yaml
kind: CronJob
```

Deploy:

```bash
kubectl apply -f cronjob.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates request
- Authorizes request
- Validates YAML
- Stores CronJob

Workflow:

```
kubectl

↓

API Server

↓

CronJob Stored
```

---

# Step 3 – Store in etcd

```
API Server

↓

etcd

↓

CronJob Object
```

The schedule is now persisted.

---

# Step 4 – CronJob Controller

The CronJob Controller continuously watches:

```
Current Time

↓

Cron Schedule

↓

CronJobs
```

Every reconciliation cycle it determines whether a Job should be created.

---

# Step 5 – Schedule Evaluation

Suppose:

```yaml
schedule: "0 2 * * *"
```

Current time:

```
01:59
```

Result:

```
Wait
```

Current time:

```
02:00
```

Result:

```
Create Job
```

---

# Cron Expression Parsing

Expression:

```
30 23 * * 1-5
```

Meaning:

```
11:30 PM

↓

Monday-Friday
```

Controller checks every field.

```
Minute

↓

Hour

↓

Day

↓

Month

↓

Weekday
```

All fields must match.

---

# Step 6 – Job Creation

CronJob creates:

```
Job
```

Example:

```
backup-job

↓

backup-job-28931721
```

Every scheduled execution creates a **new Job**.

---

# Step 7 – Job Controller

After the Job exists:

```
Job Controller

↓

Pod Created
```

The CronJob's work is complete for that execution.

---

# Step 8 – Scheduler

```
Pod

↓

Scheduler

↓

Choose Node
```

---

# Step 9 – kubelet

Worker Node:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Run Container
```

---

# Step 10 – Task Execution

Example:

```
Backup Script

↓

Database Dump

↓

Success

↓

Exit Code 0
```

Job status:

```
Complete
```

---

# Waiting for Next Schedule

After completion:

```
CronJob

↓

Sleep

↓

Next Schedule

↓

Create New Job
```

Unlike a Job:

```
Never Ends
```

It continues scheduling until deleted or suspended.

---

# Concurrency Policy

Suppose:

```
Every Minute
```

Job execution:

```
2 Minutes
```

New schedule occurs before the previous Job finishes.

Behavior depends on:

```
concurrencyPolicy
```

---

# Allow

```
Job 1

Running

↓

Job 2 Starts

↓

Both Execute
```

This is the default behavior.

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

Create Job 2
```

Only the latest execution continues.

---

# Missed Schedule

Suppose:

```
Controller Down
```

Schedule:

```
02:00
```

Controller returns:

```
02:03
```

If:

```yaml
startingDeadlineSeconds: 300
```

Result:

```
Run Missed Job
```

If the deadline has passed:

```
Skip Execution
```

---

# Suspend Workflow

Configuration:

```yaml
suspend: true
```

Workflow:

```
Schedule Reached

↓

No Job Created
```

Resume:

```
suspend: false

↓

Normal Scheduling
```

---

# Successful Job Cleanup

Configuration:

```yaml
successfulJobsHistoryLimit: 3
```

Suppose:

```
Job 1

Job 2

Job 3

Job 4
```

Controller keeps:

```
Job 2

Job 3

Job 4
```

Old successful Jobs are removed.

---

# Failed Job Cleanup

Configuration:

```yaml
failedJobsHistoryLimit: 1
```

Only the latest failed Job is retained.

---

# Time Zone Handling

Example:

```yaml
timeZone: "Asia/Kolkata"
```

Workflow:

```
Current Time

↓

Convert

↓

Schedule

↓

Execute
```

This ensures predictable execution regardless of the control plane's local time zone.

---

# Internal Architecture

```
API Server

↓

CronJob Controller

↓

Job

↓

Job Controller

↓

Pod

↓

Scheduler

↓

kubelet

↓

Container
```

---

# Database Backup Example

```
02:00

↓

CronJob

↓

Backup Job

↓

mysqldump

↓

S3 Storage

↓

Complete
```

---

# Log Cleanup Example

```
Every Night

↓

CronJob

↓

Cleanup Job

↓

Delete Logs

↓

Complete
```

---

# Email Report Example

```
08:00

↓

CronJob

↓

Generate Report

↓

Email

↓

Complete
```

---

# Hands-on Lab 1 – Create CronJob

Example:

```yaml
apiVersion: batch/v1

kind: CronJob

metadata:

  name: hello-cron

spec:

  schedule: "*/2 * * * *"

  jobTemplate:

    spec:

      template:

        spec:

          restartPolicy: Never

          containers:

          - name: hello

            image: busybox

            command:

            - echo

            - "Hello CronJob"
```

Deploy:

```bash
kubectl apply -f cronjob.yaml
```

---

# Hands-on Lab 2 – Watch Jobs

```bash
kubectl get jobs -w
```

Observe:

```
New Job

↓

Every 2 Minutes
```

---

# Hands-on Lab 3 – View Pods

```bash
kubectl get pods
```

Observe a new Pod for each scheduled Job.

---

# Hands-on Lab 4 – Suspend CronJob

```bash
kubectl patch cronjob hello-cron \
-p '{"spec":{"suspend":true}}'
```

Observe:

```
No New Jobs
```

Resume:

```bash
kubectl patch cronjob hello-cron \
-p '{"spec":{"suspend":false}}'
```

---

# Hands-on Lab 5 – Concurrency Policy

Set:

```yaml
concurrencyPolicy: Forbid
```

Create a Job that intentionally runs longer than its schedule interval.

Observe that overlapping executions are skipped.

---

# Common Mistakes

## 1. Using CronJobs for Long-Running Applications

Incorrect:

```
CronJob

↓

Web Server
```

Correct:

```
Deployment
```

CronJobs are intended for finite tasks.

---

## 2. Choosing the Wrong Concurrency Policy

For database backups:

Prefer:

```
Forbid
```

to prevent multiple backups from running simultaneously.

---

## 3. Unlimited Job History

Without cleanup:

```
Thousands of Jobs

↓

Cluster Clutter
```

Configure history limits.

---

## 4. Forgetting startingDeadlineSeconds

A controller outage may cause scheduled executions to be skipped unexpectedly.

Configure a reasonable deadline for critical workloads.

---

## 5. Ignoring Failed Jobs

Always review:

```bash
kubectl describe job

kubectl logs job/<job-name>
```

to diagnose failures.

---

# CronJobs Quick Revision

## Architecture

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

## Lifecycle

```
Wait

↓

Schedule

↓

Create Job

↓

Run

↓

Complete

↓

Wait Again
```

---

## Concurrency Policies

```
Allow

↓

Parallel Jobs
```

```
Forbid

↓

Skip Overlap
```

```
Replace

↓

Stop Old

↓

Run New
```

---

# Essential kubectl Commands

View CronJobs:

```bash
kubectl get cronjobs
```

Describe:

```bash
kubectl describe cronjob hello-cron
```

View Jobs:

```bash
kubectl get jobs
```

View Pods:

```bash
kubectl get pods
```

View Logs:

```bash
kubectl logs job/<job-name>
```

Suspend:

```bash
kubectl patch cronjob hello-cron \
-p '{"spec":{"suspend":true}}'
```

Resume:

```bash
kubectl patch cronjob hello-cron \
-p '{"spec":{"suspend":false}}'
```

Delete:

```bash
kubectl delete cronjob hello-cron
```

---

# Interview Questions

### Basic

- What is a CronJob?
- How is a CronJob different from a Job?
- What is a cron expression?

---

### Intermediate

- Explain `concurrencyPolicy`.
- What is `startingDeadlineSeconds`?
- What is `successfulJobsHistoryLimit`?

---

### Advanced

- How does the CronJob Controller work internally?
- How are missed schedules handled?
- Why does a CronJob create Jobs instead of Pods directly?
- What happens when a CronJob is suspended?
- How does Kubernetes prevent overlapping scheduled tasks?

---

# References

## Official Kubernetes Documentation

- CronJobs
- Jobs
- Batch API
- CronJob Controller
- Time Zone Support

---

## CNCF Resources

- Kubernetes Best Practices
- Batch Workloads
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Kubernetes Production Best Practices
- CIS Kubernetes Benchmark
- NIST SP 800-190
- Kubernetes Workload Management

---

## Recommended Practice

1. Create a CronJob that runs every two minutes.
2. Observe automatic Job creation using `kubectl get jobs -w`.
3. Experiment with all three concurrency policies.
4. Suspend and resume a CronJob.
5. Configure automatic cleanup using job history limits.
6. Simulate missed schedules with `startingDeadlineSeconds`.
7. Compare Job and CronJob behavior in a lab cluster.

---

# Chapter Summary

```
Developer

↓

CronJob

↓

Cron Schedule

↓

CronJob Controller

↓

Job

↓

Job Controller

↓

Pod

↓

Scheduler

↓

kubelet

↓

Task Complete

↓

Wait For Next Schedule
```

CronJobs extend Kubernetes Jobs by adding **time-based scheduling**. They are the preferred solution for recurring automation such as backups, maintenance tasks, report generation, and periodic data processing. By combining scheduling, Job execution, retry logic, and cleanup policies, CronJobs provide a robust and Kubernetes-native approach to recurring batch workloads.

---

