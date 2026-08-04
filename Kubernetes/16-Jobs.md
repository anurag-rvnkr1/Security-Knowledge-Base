# Chapter 16 – Jobs

## Overview

A **Job** is a Kubernetes workload controller that creates one or more Pods and ensures they **successfully complete a specific task**.

Unlike Deployments or StatefulSets, Jobs are **not designed to run forever**.

A Job finishes when its task completes successfully.

Jobs are ideal for:

- Database migrations
- Backup operations
- Batch processing
- Data imports
- Machine Learning training
- Report generation
- ETL pipelines
- One-time administrative tasks

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Job is
- Why Jobs are needed
- Job Architecture
- Job Lifecycle
- Parallel Jobs
- Sequential Jobs
- Job Retry Mechanism
- Job Completion Modes
- Cleanup Policies
- Best Practices

---

# Why Jobs?

Most Kubernetes workloads are long-running.

Example:

```
Deployment

↓

Web Server

↓

Runs Forever
```

But sometimes we need:

```
Backup Database

↓

Complete Once

↓

Exit
```

or

```
Import CSV

↓

Finish

↓

Exit
```

Deployments are not designed for these workloads.

---

# Solution

Use a Job.

```
Job

↓

Create Pod

↓

Run Task

↓

Complete

↓

Success
```

---

# What is a Job?

A Job is a controller that ensures a task is completed successfully.

```
Job

↓

Pod

↓

Execute Task

↓

Exit (Code 0)

↓

Completed
```

---

# Job Architecture

```
                 Job

                  │

                  ▼

                Pod

                  │

                  ▼

           Execute Task

                  │

                  ▼

            Successful Exit
```

---

# Deployment vs Job

| Deployment | Job |
|------------|-----|
| Runs continuously | Runs until task completes |
| Restarts failed Pods indefinitely | Retries until completion or failure limit |
| Web applications | Batch processing |
| Long-running services | One-time tasks |

---

# Job Workflow

```
Create Job

↓

Create Pod

↓

Execute Task

↓

Successful?

↓

Yes

↓

Job Complete
```

---

# Job YAML

```yaml
apiVersion: batch/v1

kind: Job

metadata:

  name: hello-job

spec:

  template:

    spec:

      containers:

      - name: hello

        image: busybox

        command:

        - echo

        - "Hello Kubernetes"

      restartPolicy: Never
```

---

# YAML Structure

```
Job

↓

Pod Template

↓

Container

↓

Command
```

Unlike Deployments:

```
No Service

No ReplicaSet

No Continuous Running
```

---

# restartPolicy

Jobs support:

```
Never
```

or

```
OnFailure
```

Example:

```yaml
restartPolicy: Never
```

---

# Successful Job

```
Job

↓

Pod

↓

Task Finished

↓

Exit Code 0

↓

Complete
```

---

# Failed Job

```
Job

↓

Pod

↓

Crash

↓

Retry
```

Kubernetes retries according to Job configuration.

---

# Retry Mechanism

Example:

```yaml
backoffLimit: 4
```

Workflow:

```
Attempt 1

↓

Fail

↓

Attempt 2

↓

Fail

↓

Attempt 3

↓

Fail

↓

Attempt 4

↓

Fail

↓

Job Failed
```

Default value:

```
backoffLimit: 6
```

---

# Parallel Jobs

Some tasks can run simultaneously.

Example:

```yaml
parallelism: 3
```

Workflow:

```
Job

↓

Pod 1

Pod 2

Pod 3
```

Three Pods execute concurrently.

---

# Completions

Example:

```yaml
completions: 5
```

Meaning:

```
Need

↓

5 Successful Pods
```

The Job completes after five successful executions.

---

# Parallelism vs Completions

Example:

```yaml
parallelism: 2

completions: 6
```

Workflow:

```
Two Pods

↓

Run

↓

Finish

↓

Next Two

↓

Finish

↓

Until

↓

6 Completed
```

---

# Indexed Jobs

Modern Kubernetes supports indexed Jobs.

Each Pod receives an index:

```
worker-0

worker-1

worker-2
```

Useful for distributed batch processing.

---

# Suspend Jobs

Example:

```yaml
suspend: true
```

Result:

```
Job Created

↓

Paused
```

Resume:

```yaml
suspend: false
```

---

# Active Deadline

Limit execution time.

Example:

```yaml
activeDeadlineSeconds: 300
```

Workflow:

```
5 Minutes

↓

Still Running

↓

Terminate Job
```

---

# Cleanup Finished Jobs

Automatically remove completed Jobs.

Example:

```yaml
ttlSecondsAfterFinished: 600
```

Meaning:

```
Complete

↓

Wait

10 Minutes

↓

Delete Job
```

---

# Job Lifecycle

```
Create

↓

Schedule Pod

↓

Execute

↓

Complete

↓

Cleanup
```

---

# Viewing Jobs

List:

```bash
kubectl get jobs
```

Describe:

```bash
kubectl describe job hello-job
```

---

# Viewing Job Pods

```bash
kubectl get pods
```

Logs:

```bash
kubectl logs job/hello-job
```

or

```bash
kubectl logs <pod-name>
```

---

# Deleting Jobs

```bash
kubectl delete job hello-job
```

---

# Common Job Use Cases

## Database Backup

```
Job

↓

mysqldump

↓

Backup
```

---

## Database Migration

```
Job

↓

Liquibase

↓

Migration
```

---

## ETL Pipeline

```
CSV

↓

Job

↓

Database
```

---

## ML Training

```
Training Data

↓

Job

↓

Model
```

---

## Report Generation

```
Sales Data

↓

Job

↓

PDF Report
```

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f job.yaml
```

View:

```bash
kubectl get jobs
```

Describe:

```bash
kubectl describe job hello-job
```

Logs:

```bash
kubectl logs job/hello-job
```

Delete:

```bash
kubectl delete job hello-job
```

---

# Job Architecture Summary

```
Job

↓

Pod

↓

Task

↓

Completion

↓

Success
```

---

# Best Practices

### 1. Use Jobs for Finite Tasks

Jobs should perform work that eventually finishes.

---

### 2. Configure Retry Limits

Set an appropriate:

```yaml
backoffLimit
```

to avoid endless retries.

---

### 3. Set Execution Timeouts

Use:

```yaml
activeDeadlineSeconds
```

to prevent runaway Jobs.

---

### 4. Clean Up Completed Jobs

Use:

```yaml
ttlSecondsAfterFinished
```

to automatically remove completed Jobs when appropriate.

---

### 5. Monitor Job Logs

Always inspect Job logs to verify successful execution and diagnose failures.

---

## Next Section

How Jobs Work Internally

Parallel Jobs

Indexed Jobs

Hands-on Labs

Common Mistakes

Quick Revision

References

---

# How Jobs Work Internally

## Overview

The **Job Controller** continuously watches Kubernetes and ensures the requested number of successful task executions are completed.

Unlike Deployments that reconcile **running Pods**, Jobs reconcile **completed Pods**.

---

# Internal Architecture

```
Developer

↓

kubectl apply

↓

API Server

↓

Job Controller

↓

Create Pod

↓

Scheduler

↓

Worker Node

↓

Task Executes

↓

Exit Code

↓

Job Status Updated
```

---

# Complete Workflow

```
Job Created

↓

API Server

↓

Store in etcd

↓

Job Controller

↓

Need Pod?

↓

Yes

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

Task

↓

Exit Code

↓

Complete
```

---

# Exit Codes

```
0

↓

Success
```

```
Non-Zero

↓

Failure
```

The Job Controller uses the container's exit code to determine success or failure.

---

# Retry Logic

Suppose:

```
Attempt 1

↓

Exit Code 1
```

Controller:

```
Create New Pod

↓

Retry
```

Continues until:

```
Success

or

backoffLimit Reached
```

---

# Parallel Execution

Example:

```yaml
parallelism: 3

completions: 6
```

Execution:

```
Pods 1-3

↓

Complete

↓

Pods 4-6

↓

Complete

↓

Job Finished
```

---

# Indexed Job Workflow

```
Job

↓

Index 0

↓

Index 1

↓

Index 2
```

Each Pod knows its index through environment variables and annotations, allowing distributed workloads to divide tasks deterministically.

---

# Hands-on Lab 1 – Simple Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: hello
        image: busybox
        command: ["echo","Hello Kubernetes"]
```

Deploy:

```bash
kubectl apply -f job.yaml
```

---

# Hands-on Lab 2 – Watch Status

```bash
kubectl get jobs

kubectl get pods

kubectl logs job/hello-job
```

---

# Hands-on Lab 3 – Failed Job

Create a Job that exits with:

```bash
exit 1
```

Observe:

```bash
kubectl describe job
```

Notice retry attempts.

---

# Hands-on Lab 4 – Parallel Job

```yaml
parallelism: 2

completions: 4
```

Observe multiple Pods running simultaneously.

---

# Hands-on Lab 5 – TTL Cleanup

```yaml
ttlSecondsAfterFinished: 120
```

Watch the Job automatically disappear after completion.

---

# Common Mistakes

## 1. Using a Deployment for Batch Tasks

Incorrect:

```
Deployment

↓

Backup Script
```

Correct:

```
Job
```

---

## 2. Forgetting restartPolicy

Jobs require:

```yaml
restartPolicy:

Never

or

OnFailure
```

---

## 3. Unlimited Retries

Set an appropriate:

```yaml
backoffLimit
```

---

## 4. Missing Cleanup

Thousands of completed Jobs can clutter the cluster.

Use:

```yaml
ttlSecondsAfterFinished
```

---

## 5. Ignoring Logs

Always inspect:

```bash
kubectl logs job/<job-name>
```

---

# Quick Revision

```
Job

↓

Finite Task

↓

Pod

↓

Exit Code

↓

Complete
```

---

# Interview Questions

### Basic

- What is a Kubernetes Job?
- When should you use a Job instead of a Deployment?
- What is `restartPolicy` for Jobs?

### Intermediate

- Explain `parallelism` and `completions`.
- What is `backoffLimit`?
- What is `activeDeadlineSeconds`?

### Advanced

- How does the Job Controller work?
- What is an Indexed Job?
- How are failed Jobs retried?
- What is `ttlSecondsAfterFinished`?
- How does Kubernetes determine that a Job has completed?

---

# References

- Kubernetes Jobs
- Batch API
- Indexed Jobs
- Job Controller
- Kubernetes Best Practices

---

**End of Chapter 16 – Jobs**

**Next Chapter:** **Chapter 17 – CronJobs**

---