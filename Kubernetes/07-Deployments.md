# Chapter 7 – Deployments

## Overview

A **Deployment** is one of the most important Kubernetes objects.

While a ReplicaSet ensures that a certain number of Pods are running, a Deployment manages ReplicaSets and provides advanced application lifecycle management such as:

- Rolling Updates
- Rollbacks
- Version History
- Controlled Scaling
- Zero (or near-zero) Downtime Deployments
- Declarative Updates

In production Kubernetes clusters, applications are almost always deployed using **Deployments**, not standalone Pods or ReplicaSets.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Deployment is
- Why Deployments exist
- Deployment Architecture
- Deployment Lifecycle
- ReplicaSet Management
- Rolling Updates
- Rollbacks
- Deployment Strategies
- Scaling Deployments
- Deployment YAML
- Best Practices

---

# Why Deployments?

Suppose you create a ReplicaSet.

```
ReplicaSet

↓

3 Pods
```

It provides:

- Self-healing
- Scaling

However, updating the application version is difficult.

Example:

```
NGINX v1

↓

Need

↓

NGINX v2
```

A Deployment automates this process.

---

# What is a Deployment?

A Deployment is a Kubernetes controller that manages ReplicaSets and Pods.

```
Deployment

↓

ReplicaSet

↓

Pods
```

The Deployment is responsible for application lifecycle management.

---

# Deployment Responsibilities

Deployments provide:

- Create ReplicaSets
- Create Pods
- Rolling Updates
- Rollbacks
- Scaling
- Version History
- Self-Healing (through ReplicaSets)

---

# Deployment Architecture

```
               Deployment

                     │

             ReplicaSet

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

      Pod 1        Pod 2        Pod 3
```

The Deployment never manages Pods directly.

Instead:

```
Deployment

↓

ReplicaSet

↓

Pods
```

---

# Deployment Hierarchy

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

Each layer has a different responsibility.

---

# Deployment YAML

Example:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:
  name: nginx

spec:

  replicas: 3

  selector:

    matchLabels:

      app: nginx

  template:

    metadata:

      labels:

        app: nginx

    spec:

      containers:

      - name: nginx

        image: nginx:1.29
```

---

# YAML Structure

```
Deployment

↓

Metadata

↓

Spec

↓

Replicas

↓

Selector

↓

Pod Template
```

---

# Creating a Deployment

Apply:

```bash
kubectl apply -f deployment.yaml
```

Verify:

```bash
kubectl get deployments
```

View ReplicaSets:

```bash
kubectl get rs
```

View Pods:

```bash
kubectl get pods
```

---

# Deployment Lifecycle

```
Create Deployment

↓

Create ReplicaSet

↓

Create Pods

↓

Running

↓

Scale

↓

Update

↓

Rollback

↓

Delete
```

---

# Deployment Creation Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Deployment Controller

↓

ReplicaSet

↓

Pods

↓

Running
```

---

# Scaling Deployments

Scale:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Workflow:

```
Deployment

↓

ReplicaSet

↓

5 Pods
```

Scale down:

```bash
kubectl scale deployment nginx \
--replicas=2
```

---

# Updating an Application

Suppose current image:

```
nginx:1.29
```

Need:

```
nginx:1.30
```

Update:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Deployment automatically begins a rolling update.

---

# Rolling Update

Instead of deleting all Pods:

```
Old Pods

↓

Delete All

↓

Create New
```

Kubernetes performs:

```
Old Pod

↓

New Pod

↓

Old Pod

↓

New Pod

↓

Complete
```

Applications remain available during the update.

---

# Rolling Update Workflow

```
Deployment

↓

New ReplicaSet

↓

Create New Pod

↓

Ready

↓

Delete Old Pod

↓

Repeat
```

This process continues until all Pods are updated.

---

# ReplicaSets During Updates

Before update:

```
Deployment

↓

ReplicaSet A

↓

3 Pods
```

After update starts:

```
Deployment

↓

ReplicaSet A

↓

ReplicaSet B

↓

Pods Transition
```

Eventually:

```
ReplicaSet B

↓

3 Pods
```

ReplicaSet A is retained for rollback history (subject to revision history limits).

---

# Rollback

Suppose update fails.

Command:

```bash
kubectl rollout undo deployment nginx
```

Workflow:

```
ReplicaSet B

↓

Rollback

↓

ReplicaSet A

↓

Application Restored
```

---

# Deployment Status

Check rollout:

```bash
kubectl rollout status deployment nginx
```

History:

```bash
kubectl rollout history deployment nginx
```

---

# Viewing Deployments

List:

```bash
kubectl get deployments
```

Describe:

```bash
kubectl describe deployment nginx
```

The output includes:

- Replicas
- Strategy
- Conditions
- Events
- ReplicaSets

---

# Deleting Deployments

Delete:

```bash
kubectl delete deployment nginx
```

Workflow:

```
Deployment

↓

ReplicaSets

↓

Pods

↓

Removed
```

---

# Deployment Strategies

Kubernetes supports multiple deployment strategies.

The most common:

```
RollingUpdate
```

Alternative:

```
Recreate
```

RollingUpdate is the default.

---

# RollingUpdate Strategy

```
Old Pod

↓

New Pod

↓

Healthy

↓

Remove Old Pod

↓

Repeat
```

Advantages:

- High availability
- Minimal downtime
- Controlled updates

---

# Recreate Strategy

```
Old Pods

↓

Delete All

↓

Create New Pods
```

Advantages:

- Simpler
- Useful when multiple versions cannot run simultaneously

Disadvantage:

- Downtime during deployment

---

# Deployment vs ReplicaSet

| Deployment | ReplicaSet |
|------------|------------|
| Manages ReplicaSets | Manages Pods |
| Rolling Updates | No Rolling Updates |
| Rollbacks | No Rollbacks |
| Version History | No Version History |
| Production Standard | Internal Building Block |

---

# Deployment vs Pod

| Deployment | Pod |
|------------|-----|
| Multiple replicas | Single workload |
| Automatic updates | No update management |
| Self-healing | None by itself |
| Scalable | Single instance |

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f deployment.yaml
```

View:

```bash
kubectl get deployments
```

Describe:

```bash
kubectl describe deployment nginx
```

Scale:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Update image:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Status:

```bash
kubectl rollout status deployment nginx
```

History:

```bash
kubectl rollout history deployment nginx
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Delete:

```bash
kubectl delete deployment nginx
```

---

# Deployment Architecture Summary

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

---

# Best Practices

### 1. Use Deployments for Stateless Applications

Deployments are the standard controller for web applications, APIs, and microservices.

---

### 2. Use Versioned Images

Avoid:

```yaml
image: nginx:latest
```

Prefer:

```yaml
image: nginx:1.29.1
```

---

### 3. Monitor Rollouts

Always verify:

```bash
kubectl rollout status
```

after deploying a new version.

---

### 4. Keep Revision History

Revision history enables fast rollbacks when problems occur.

---

### 5. Store Deployment Manifests in Git

Use GitOps or Infrastructure as Code practices for reproducible deployments.

---

# How Deployments Work Internally

## Overview

A Deployment is one of the most intelligent controllers in Kubernetes.

Unlike a ReplicaSet, which only ensures a certain number of Pods exist, a Deployment manages the **entire application lifecycle** by creating, updating, and replacing ReplicaSets.

The Deployment Controller continuously compares the desired application state with the current state and performs the necessary actions to keep them synchronized.

---

# Complete Deployment Workflow

Suppose a Deployment is created.

```bash
kubectl apply -f deployment.yaml
```

Complete workflow:

```
Developer

↓

kubectl

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

etcd

↓

Deployment Controller

↓

ReplicaSet

↓

Scheduler

↓

Worker Nodes

↓

Pods

↓

Application Running
```

---

# Step 1 – User Creates Deployment

Example:

```yaml
kind: Deployment
```

Deploy:

```bash
kubectl apply -f deployment.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates user
- Authorizes request
- Validates manifest
- Stores Deployment

Workflow:

```
kubectl

↓

API Server

↓

Deployment Stored
```

---

# Step 3 – Store in etcd

```
API Server

↓

etcd
```

Current state:

```
Deployment Exists

↓

No ReplicaSet Yet
```

---

# Step 4 – Deployment Controller

The Deployment Controller watches Deployment objects.

It detects:

```
Deployment Created
```

and creates:

```
ReplicaSet
```

---

# Step 5 – ReplicaSet Creation

Example:

```
Deployment

↓

ReplicaSet A
```

ReplicaSet receives:

```
replicas = 3
```

---

# Step 6 – ReplicaSet Creates Pods

ReplicaSet detects:

```
Desired = 3

↓

Current = 0

↓

Create 3 Pods
```

Initially:

```
Pending
```

---

# Step 7 – Scheduler

Scheduler assigns Pods.

```
Pod

↓

Best Node

↓

Worker Node
```

---

# Step 8 – kubelet

Worker node:

```
kubelet

↓

Container Runtime

↓

Container Starts
```

---

# Step 9 – Running

Final state:

```
Deployment

↓

ReplicaSet

↓

3 Running Pods
```

Application becomes available.

---

# Continuous Monitoring

Deployment Controller continuously watches:

```
Deployment

↓

ReplicaSets

↓

Pods
```

It reacts whenever changes occur.

---

# Updating a Deployment

Suppose:

```
Image

↓

nginx:1.29
```

Update:

```
nginx:1.30
```

Command:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Deployment detects:

```
Template Changed
```

---

# New ReplicaSet

Old state:

```
Deployment

↓

ReplicaSet A

↓

Pods v1
```

Update:

```
Deployment

↓

ReplicaSet A

↓

ReplicaSet B
```

ReplicaSet B contains:

```
Updated Image
```

---

# Rolling Update Workflow

```
ReplicaSet B

↓

Create 1 Pod

↓

Healthy

↓

Delete 1 Pod

↓

Repeat
```

Until:

```
ReplicaSet B

↓

All Pods Running
```

---

# Old ReplicaSet

Deployment does **not** immediately delete the previous ReplicaSet.

Instead:

```
ReplicaSet A

↓

Scaled Down

↓

Retained
```

This enables rollbacks.

---

# Rollback Workflow

Suppose:

```
ReplicaSet B

↓

Application Errors
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Workflow:

```
Deployment

↓

ReplicaSet A

↓

Scale Up

↓

ReplicaSet B

↓

Scale Down
```

Application returns to the previous version.

---

# Scaling Deployment

Command:

```bash
kubectl scale deployment nginx \
--replicas=6
```

Workflow:

```
Deployment

↓

ReplicaSet

↓

Desired = 6

↓

Current = 3

↓

Create 3 Pods
```

---

# Scaling Down

Command:

```bash
kubectl scale deployment nginx \
--replicas=2
```

Workflow:

```
Desired = 2

↓

Delete Extra Pods

↓

2 Running
```

---

# Deployment Conditions

Deployments report several conditions.

Examples:

- Available
- Progressing

View:

```bash
kubectl describe deployment nginx
```

---

# Deployment Status

Check rollout:

```bash
kubectl rollout status deployment nginx
```

Example:

```
Waiting

↓

Updating

↓

Complete
```

---

# Deployment History

View revisions:

```bash
kubectl rollout history deployment nginx
```

Example:

```
Revision 1

↓

Revision 2

↓

Revision 3
```

---

# Internal Architecture

```
Deployment

↓

Deployment Controller

↓

ReplicaSet

↓

Pods

↓

Containers
```

---

# Rolling Update Internals

Before update:

```
ReplicaSet A

↓

3 Pods
```

After update begins:

```
ReplicaSet A

↓

2 Pods

ReplicaSet B

↓

1 Pod
```

Later:

```
ReplicaSet A

↓

1 Pod

ReplicaSet B

↓

2 Pods
```

Finally:

```
ReplicaSet B

↓

3 Pods
```

This gradual transition minimizes service disruption.

---

# Hands-on Lab 1 – Create Deployment

Deployment YAML:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: nginx

spec:

  replicas: 3

  selector:

    matchLabels:

      app: nginx

  template:

    metadata:

      labels:

        app: nginx

    spec:

      containers:

      - name: nginx

        image: nginx:1.29
```

Deploy:

```bash
kubectl apply -f deployment.yaml
```

---

# Hands-on Lab 2 – Verify

```bash
kubectl get deployments

kubectl get rs

kubectl get pods
```

Observe:

```
Deployment

↓

ReplicaSet

↓

Pods
```

---

# Hands-on Lab 3 – Scale

```bash
kubectl scale deployment nginx \
--replicas=5
```

Verify:

```bash
kubectl get pods
```

Scale down:

```bash
kubectl scale deployment nginx \
--replicas=2
```

---

# Hands-on Lab 4 – Rolling Update

Update image:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Watch:

```bash
kubectl rollout status deployment nginx
```

Observe Pods:

```bash
kubectl get pods -w
```

---

# Hands-on Lab 5 – Rollback

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Verify:

```bash
kubectl rollout history deployment nginx
```

---

# Best Practices

### 1. Always Use Deployments for Stateless Applications

Avoid standalone ReplicaSets unless you have a specific learning or troubleshooting objective.

---

### 2. Monitor Rollouts

Verify every update using:

```bash
kubectl rollout status
```

---

### 3. Keep Image Tags Immutable

Use explicit version tags instead of mutable tags like `latest`.

---

### 4. Review Deployment History

Check revision history before performing rollbacks.

---

### 5. Validate After Every Update

Confirm:

- Pods are Ready
- ReplicaSets are healthy
- Application responds correctly
- Events show no errors

---

# Common Mistakes

Deployments are the **most commonly used workload controller** in Kubernetes. While they simplify application management, many production incidents occur because of incorrect Deployment configurations or misunderstandings of how Deployments interact with ReplicaSets and Pods.

The following are the most common mistakes made when working with Deployments.

---

# 1. Creating Standalone Pods Instead of Deployments

Many beginners deploy applications like this:

```yaml
kind: Pod
```

Although this works, it provides:

- No automatic scaling
- No rolling updates
- No rollback
- No version history

Recommended:

```
Deployment

↓

ReplicaSet

↓

Pods
```

Use Deployments for almost all stateless production applications.

---

# 2. Editing Pods Directly

Incorrect workflow:

```bash
kubectl edit pod nginx
```

Suppose the Pod belongs to a Deployment.

```
Pod Edited

↓

Pod Deleted

↓

Deployment Creates New Pod

↓

Changes Lost
```

Correct workflow:

```
Edit Deployment

↓

New ReplicaSet

↓

Rolling Update
```

Always modify the Deployment rather than individual Pods.

---

# 3. Using `latest` Image Tag

Avoid:

```yaml
image: nginx:latest
```

Problems:

- Unpredictable deployments
- Difficult troubleshooting
- Complicated rollbacks

Preferred:

```yaml
image: nginx:1.29.1
```

Use immutable image versions whenever possible.

---

# 4. Not Monitoring Rollouts

Many users execute:

```bash
kubectl apply -f deployment.yaml
```

and immediately assume success.

Always verify:

```bash
kubectl rollout status deployment nginx
```

and inspect Pods:

```bash
kubectl get pods
```

---

# 5. Ignoring ReplicaSets

Some engineers believe Deployments manage Pods directly.

Actual hierarchy:

```
Deployment

↓

ReplicaSet

↓

Pods
```

Understanding this relationship is essential for troubleshooting updates and rollbacks.

---

# 6. Deleting Pods to Fix Problems

Suppose:

```
Deployment

↓

ReplicaSet

↓

Pods
```

Deleting a Pod:

```bash
kubectl delete pod pod-name
```

results in:

```
ReplicaSet

↓

Creates New Pod
```

Deleting the Pod rarely fixes the underlying issue.

Investigate the root cause instead.

---

# 7. Forgetting Label Selectors

Deployment selector:

```yaml
selector:

  matchLabels:

    app: nginx
```

Pod template:

```yaml
labels:

  app: web
```

Result:

```
Selector Mismatch

↓

Deployment Cannot Manage Intended Pods
```

Selectors and template labels must match.

---

# 8. Scaling Pods Manually

Incorrect:

```
Pod

↓

Duplicate Pod
```

Correct:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Scaling should occur at the Deployment level.

---

# 9. Forgetting Rollback Capability

Before major deployments:

Verify revision history:

```bash
kubectl rollout history deployment nginx
```

Rollback if required:

```bash
kubectl rollout undo deployment nginx
```

Always confirm rollback procedures work before critical production releases.

---

# 10. Ignoring Deployment Events

Many users only inspect application logs.

Also check:

```bash
kubectl describe deployment nginx
```

Review:

- Events
- Conditions
- ReplicaSets
- Progress status

Events often reveal rollout problems.

---

# 11. Misunderstanding Rolling Updates

Incorrect assumption:

```
Old Pods

↓

Deleted

↓

New Pods
```

Actual Rolling Update:

```
Old Pod

↓

New Pod

↓

Ready

↓

Delete Old Pod

↓

Repeat
```

This process minimizes downtime.

---

# 12. Updating Without Health Probes

Without readiness probes:

```
New Pod

↓

Not Ready

↓

Traffic Sent

↓

Users Experience Errors
```

Deployments work best when Pods implement:

- Startup Probes
- Readiness Probes
- Liveness Probes

---

# 13. Ignoring Resource Requests and Limits

Pods without resource requests may be difficult to schedule or may compete unfairly for cluster resources.

Always define:

- CPU requests
- CPU limits
- Memory requests
- Memory limits

for production workloads.

---

# 14. Forgetting Namespace Context

Example:

```bash
kubectl get deployments
```

returns nothing.

Reason:

Deployment exists in:

```
production
```

Specify:

```bash
kubectl get deployments \
-n production
```

or verify the current context and namespace.

---

# 15. Using Deployments for Stateful Applications

Deployments are designed for **stateless** applications.

Examples:

Suitable:

- Web servers
- REST APIs
- Microservices
- Frontend applications

Generally use **StatefulSets** for workloads such as:

- Databases
- Distributed storage systems
- Applications requiring stable identities

---

# Deployment Quick Revision

## Architecture

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

---

## Deployment Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Deployment Controller

↓

ReplicaSet

↓

Scheduler

↓

Worker Nodes

↓

Pods Running
```

---

## Rolling Update

```
ReplicaSet A

↓

ReplicaSet B

↓

Gradual Replacement

↓

Application Updated
```

---

## Rollback

```
Current ReplicaSet

↓

Previous ReplicaSet

↓

Application Restored
```

---

## Scaling

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Desired Replicas
```

---

# Essential kubectl Commands

Create:

```bash
kubectl apply -f deployment.yaml
```

View:

```bash
kubectl get deployments

kubectl get rs

kubectl get pods
```

Describe:

```bash
kubectl describe deployment nginx
```

Scale:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Update Image:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Check Rollout:

```bash
kubectl rollout status deployment nginx
```

View History:

```bash
kubectl rollout history deployment nginx
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Delete:

```bash
kubectl delete deployment nginx
```

---

# Deployment Feature Comparison

| Feature | Deployment |
|----------|:----------:|
| Self-Healing | ✓ |
| Scaling | ✓ |
| Replica Management | ✓ |
| Rolling Updates | ✓ |
| Rollbacks | ✓ |
| Revision History | ✓ |
| Declarative Updates | ✓ |
| High Availability | ✓ |

---

# Deployment Checklist

| Topic | Status |
|--------|:------:|
| Deployment Basics | ✓ |
| Deployment Architecture | ✓ |
| Deployment Lifecycle | ✓ |
| ReplicaSet Relationship | ✓ |
| Rolling Updates | ✓ |
| Rollbacks | ✓ |
| Scaling | ✓ |
| Deployment Strategies | ✓ |
| Hands-on Labs | ✓ |
| Common Mistakes | ✓ |

---

# Interview Questions

### Basic

- What is a Deployment?
- Why are Deployments preferred over ReplicaSets?
- How does a Deployment manage Pods?
- What is the relationship between a Deployment and a ReplicaSet?
- What happens when you delete a Pod managed by a Deployment?

---

### Intermediate

- Explain the Deployment lifecycle.
- How does a Rolling Update work?
- What is the difference between RollingUpdate and Recreate strategies?
- How do you scale a Deployment?
- How do you check rollout progress?

---

### Advanced

- How does Kubernetes perform a rollback?
- What triggers the creation of a new ReplicaSet?
- Why does a Deployment retain old ReplicaSets?
- What happens internally when `kubectl set image` is executed?
- How do readiness probes affect rolling updates?

---

# References

## Official Kubernetes Documentation

- Kubernetes Deployments Documentation
- Deployment Concepts
- Rolling Updates
- ReplicaSets
- Kubernetes API Reference
- kubectl Reference

---

## CNCF Resources

- Cloud Native Computing Foundation (CNCF)
- Kubernetes Best Practices
- Kubernetes Learning Path
- Production Kubernetes Guides

---

## Security & Operations

- CIS Kubernetes Benchmark
- NIST SP 800-190 — Application Container Security Guide
- NSA/CISA Kubernetes Hardening Guidance
- OWASP Kubernetes Top 10

---

## Recommended Books

- *Kubernetes Up & Running* — Kelsey Hightower, Brendan Burns & Joe Beda
- *Kubernetes in Action* — Marko Lukša
- *Production Kubernetes* — Josh Rosso & Rich Lander
- *Managing Kubernetes* — Brendan Burns, Craig Tracey & Joe Beda

---

## Recommended Hands-on Practice

1. Create a Deployment with three replicas.
2. Observe the automatically created ReplicaSet.
3. Scale the Deployment up and down.
4. Perform a rolling update using a new container image.
5. Watch Pods during the rollout using:

```bash
kubectl get pods -w
```

6. Roll back to the previous revision.
7. Inspect Deployment events and ReplicaSet history.
8. Experiment with both `RollingUpdate` and `Recreate` strategies in a non-production environment.

---

# Chapter Summary

```
Deployment Created

↓

Deployment Controller

↓

ReplicaSet Created

↓

Pods Created

↓

Scheduler

↓

Worker Nodes

↓

Application Running

↓

Rolling Updates

↓

Rollback (if required)

↓

Continuous Reconciliation
```

A Deployment is the **standard controller for stateless applications** in Kubernetes. It builds upon ReplicaSets to provide **automated updates, version history, controlled rollouts, self-healing, scaling, and rollback capabilities**, making it the preferred choice for modern cloud-native application deployment.

