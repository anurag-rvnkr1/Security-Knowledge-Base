# Chapter 41 – Priority Classes

## Overview

Kubernetes clusters often run many different workloads at the same time.

For example:

```text
Critical Infrastructure
    ↓
Monitoring
    ↓
Production Applications
    ↓
Batch Processing
    ↓
Development Workloads
```

Not every Pod has the same importance.

Suppose a cluster has insufficient resources and a critical production Pod needs to be scheduled.

Kubernetes needs a mechanism to determine:

> **Which Pods should receive scheduling preference when resources are scarce?**

Kubernetes provides **Priority Classes** for this purpose.

A PriorityClass assigns a priority value to Pods.

Conceptually:

```text
PriorityClass

      ↓

Priority Value

      ↓

Pod

      ↓

Scheduler
```

Higher-priority Pods receive preferential scheduling treatment.

Priority can also participate in **Pod preemption**, where lower-priority Pods may be removed to make room for a higher-priority Pod when appropriate.

> **Priority Classes determine the relative importance of Pods during scheduling and can influence preemption.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Pod priority is
- What a PriorityClass is
- Why Priority Classes are needed
- Priority values
- Default PriorityClass
- `globalDefault`
- `preemptionPolicy`
- Pod preemption
- Scheduler behavior
- High-priority workloads
- Low-priority workloads
- Non-preempting PriorityClasses
- Priority vs QoS
- Priority vs resource requests and limits
- Resource pressure
- Real-world use cases
- Hands-on Labs
- Common mistakes
- Troubleshooting
- Best practices

---

# Why Do We Need Priority?

Imagine a Node with:

```text
Available CPU:
1 CPU
```

Two Pods are waiting:

```text
Pod A
Priority: 1000

Pod B
Priority: 100
```

Both require:

```text
1 CPU
```

The Scheduler needs to determine which Pod should receive the available capacity.

Priority allows Kubernetes to treat:

```text
Pod A
```

as more important than:

```text
Pod B
```

---

# Basic Concept

```text
Pod A
Priority = 1000

Pod B
Priority = 100

Pod C
Priority = 10
```

Higher value:

```text
1000 > 100 > 10
```

Therefore:

```text
Pod A

↓

Highest scheduling priority
```

---

# What is a PriorityClass?

A `PriorityClass` is a cluster-scoped Kubernetes object that defines a priority value.

Example:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: critical-workload

value: 100000

globalDefault: false

description: "Priority for critical workloads"
```

---

# PriorityClass Structure

Important fields include:

```text
value
```

```text
globalDefault
```

```text
description
```

and:

```text
preemptionPolicy
```

---

# Priority Value

The `value` determines the relative priority.

Example:

```yaml
value: 1000
```

Another:

```yaml
value: 100
```

Higher values indicate higher priority.

---

# Example

```text
critical-workload
value=100000

production-workload
value=10000

batch-workload
value=100

development-workload
value=10
```

Conceptually:

```text
100000
   ↑
Critical

10000
   ↑
Production

100
   ↑
Batch

10
   ↑
Development
```

---

# PriorityClass is Cluster-Scoped

Unlike Pods and Deployments, PriorityClass is not namespaced.

You can create:

```bash
kubectl get priorityclass
```

from any namespace.

---

# Creating a PriorityClass

Example:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: production-high

value: 10000

globalDefault: false

description: "High priority for production workloads"
```

Apply:

```bash
kubectl apply -f priorityclass.yaml
```

---

# Viewing Priority Classes

```bash
kubectl get priorityclass
```

Example:

```text
NAME                VALUE

production-high     10000

batch-low           100
```

---

# Describe a PriorityClass

```bash
kubectl describe priorityclass production-high
```

---

# Assigning Priority to a Pod

A Pod uses:

```yaml
priorityClassName: production-high
```

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: high-priority-pod

spec:

  priorityClassName: production-high

  containers:

  - name: nginx

    image: nginx
```

The Pod inherits the priority value from:

```text
production-high
```

---

# Priority Assignment

The relationship is:

```text
PriorityClass

      ↓

value = 10000

      ↓

Pod

      ↓

priorityClassName:
production-high
```

---

# Pod Priority

Once the Pod references a PriorityClass, Kubernetes associates the corresponding priority value with the Pod.

You can inspect it with:

```bash
kubectl get pod <pod-name> -o yaml
```

Look for:

```yaml
priorityClassName:
```

and:

```yaml
priority:
```

---

# Scheduling Queue

Priority affects how Pods are considered by the Scheduler.

Conceptually:

```text
             Pending Pods

                  │

                  ▼

          Scheduling Queue

                  │

       ┌──────────┼──────────┐
       ▼          ▼          ▼

    Priority    Priority   Priority
     10000        100          10

       │
       ▼

   Higher priority
   considered first
```

The actual Scheduler queue behavior is more sophisticated, but the important idea is:

> Higher-priority Pods receive preferential scheduling treatment.

---

# Priority and Resource Availability

Priority becomes especially important when:

```text
Cluster resources are limited
```

Suppose:

```text
Node:

CPU = 4
```

Existing workloads consume:

```text
CPU = 4
```

A new Pod requests:

```text
CPU = 2
```

The Pod cannot fit.

If the Pod has sufficiently high priority and preemption is allowed, Kubernetes may consider preempting lower-priority Pods.

---

# Pod Preemption

Preemption means:

> A higher-priority Pod may cause lower-priority Pods to be evicted so that the higher-priority Pod can be scheduled.

Conceptually:

```text
High Priority Pod

        ↓

Insufficient Resources

        ↓

Find Lower Priority Pods

        ↓

Preempt

        ↓

Resources Become Available

        ↓

Schedule High Priority Pod
```

---

# Example

Node capacity:

```text
CPU = 4
```

Existing Pods:

```text
Pod A
Priority = 100
CPU = 2

Pod B
Priority = 100
CPU = 1
```

Available:

```text
CPU = 1
```

New Pod:

```text
Pod C
Priority = 1000
CPU = 2
```

Pod C cannot fit.

If preemption is allowed, the Scheduler may consider removing a lower-priority Pod.

For example:

```text
Pod B
Priority = 100
```

may be preempted.

Then:

```text
CPU available

↓

Pod C can be scheduled
```

---

# Important: Preemption Is Not Always Guaranteed

Higher priority does not mean:

```text
Always evict something
```

The Scheduler considers whether preemption can actually make the Pod schedulable.

If no useful preemption solution exists, the Pod can remain:

```text
Pending
```

---

# preemptionPolicy

PriorityClass supports:

```yaml
preemptionPolicy:
```

Two important values are:

```text
PreemptLowerPriority
```

and:

```text
Never
```

---

# PreemptLowerPriority

This is the default behavior when applicable.

Example:

```yaml
preemptionPolicy: PreemptLowerPriority
```

A high-priority Pod can potentially preempt lower-priority Pods if necessary and if the scheduling constraints permit it.

---

# Never

Example:

```yaml
preemptionPolicy: Never
```

The Pod receives scheduling priority but does not preempt lower-priority Pods.

This is known as a **non-preempting PriorityClass**.

---

# Non-Preempting PriorityClass

Example:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: high-nonpreempting

value: 50000

globalDefault: false

preemptionPolicy: Never

description: "High scheduling priority without preemption"
```

This means:

```text
High scheduling priority

+

No preemption
```

---

# Why Use Non-Preempting Priority?

Suppose a workload should be considered before normal workloads but should not disrupt running applications.

Example:

```text
Important batch job
```

You may want:

```text
Higher queue priority
```

without:

```text
Evicting existing workloads
```

A non-preempting PriorityClass can be useful for this pattern.

---

# Priority vs Preemption

These are related but different.

Priority:

```text
How important is this Pod?
```

Preemption:

```text
Can lower-priority Pods be removed to make room?
```

Therefore:

```text
High Priority

≠

Automatically Preemptive
```

if:

```text
preemptionPolicy: Never
```

is configured.

---

# globalDefault

A PriorityClass can have:

```yaml
globalDefault: true
```

This makes it the default PriorityClass for Pods that do not explicitly specify one, subject to Kubernetes behavior and cluster configuration.

Only one PriorityClass should normally be designated as the global default.

Example:

```yaml
globalDefault: true
```

---

# Example Default PriorityClass

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: default-priority

value: 100

globalDefault: true

description: "Default priority for ordinary workloads"
```

---

# Why Use globalDefault?

It can establish a baseline priority for workloads that do not explicitly select a PriorityClass.

However, production clusters should define priority policies carefully.

---

# Built-in Priority Classes

Kubernetes installations commonly include system-related PriorityClasses such as:

```text
system-node-critical
```

and:

```text
system-cluster-critical
```

These are used for critical system workloads.

Inspect:

```bash
kubectl get priorityclass
```

---

# System Critical Workloads

Critical Kubernetes components may need to remain schedulable even when resources are constrained.

Very high priority classes help protect important system workloads.

Conceptually:

```text
System Critical
      ↑
Production Critical
      ↑
Production
      ↑
Batch
      ↑
Development
```

---

# Priority and QoS Are Different

Do not confuse:

```text
Priority
```

with:

```text
Quality of Service (QoS)
```

Priority answers:

```text
Which Pod is more important for scheduling?
```

QoS answers:

```text
How are the Pod's resource requests and limits configured?
```

---

# QoS Classes

Kubernetes commonly classifies Pods as:

```text
Guaranteed
```

```text
Burstable
```

```text
BestEffort
```

These are different from PriorityClasses.

---

# Priority vs QoS

| Priority | QoS |
|---|---|
| Scheduling importance | Resource configuration classification |
| Defined by PriorityClass | Derived from requests/limits |
| Influences scheduling order | Influences resource management |
| Can affect preemption | Can affect eviction behavior |

---

# Priority vs Resource Requests

These also serve different purposes.

Resource requests:

```text
How much resource does the Pod ask Scheduler to reserve?
```

Priority:

```text
How important is the Pod compared with other Pods?
```

Example:

```text
Pod A
CPU request = 2
Priority = 100
```

```text
Pod B
CPU request = 1
Priority = 10000
```

Pod B has higher priority but needs fewer resources.

---

# Priority Does Not Create Resources

If a cluster has:

```text
0 CPU available
```

and a high-priority Pod requests:

```text
100 CPU
```

priority does not magically create:

```text
100 CPU
```

The Pod can remain:

```text
Pending
```

if no feasible scheduling solution exists.

---

# Priority and Limits

Resource limits do not determine Pod priority.

For example:

```yaml
resources:

  limits:

    cpu: "2"
```

does not mean:

```text
High priority
```

Priority is separately configured using:

```yaml
priorityClassName:
```

---

# Priority and Taints

Priority does not override taints.

Suppose:

```text
Node:

dedicated=database:NoSchedule
```

A high-priority Pod without a matching toleration still cannot normally be scheduled onto that Node.

Therefore:

```text
High Priority

≠

Ignore Taints
```

---

# Priority and Node Affinity

Priority also does not override required Node Affinity.

If a Pod requires:

```text
environment=production
```

and no Node matches:

```text
environment=production
```

the Pod cannot simply ignore the requirement because it has high priority.

---

# Priority and Pod Anti-Affinity

Similarly, required Pod Anti-Affinity can prevent a high-priority Pod from being placed in certain locations.

Scheduling constraints still matter.

---

# Preemption and Scheduling Constraints

When preemption is considered, Kubernetes must find a solution that satisfies the higher-priority Pod's scheduling requirements.

For example:

```text
High Priority Pod

requires:

disk=ssd
```

If preempting Pods on an HDD-only Node does not make an SSD Node available, preemption there does not solve the problem.

---

# Preemption Workflow

Conceptually:

```text
High Priority Pod

        ↓

Cannot Schedule

        ↓

Consider Preemption

        ↓

Find Candidate Nodes

        ↓

Identify Lower Priority Victims

        ↓

Check Scheduling Constraints

        ↓

Select Victims

        ↓

Evict Victims

        ↓

Schedule High Priority Pod
```

---

# Preemption Victims

A **victim** is a lower-priority Pod selected for preemption.

Example:

```text
High Priority Pod
Priority = 10000
```

may preempt:

```text
Pod A
Priority = 100
```

but generally should not preempt:

```text
Pod B
Priority = 20000
```

because Pod B has higher priority.

---

# Preemption and Graceful Termination

Preempted Pods are not necessarily removed instantaneously.

They can go through termination behavior according to Pod lifecycle and configured termination grace periods.

Therefore:

```text
Preemption initiated

↓

Victim termination

↓

Resources become available

↓

Higher-priority Pod scheduled
```

---

# Priority Ordering Example

Suppose:

```text
PriorityClass          Value

critical               100000
production             10000
batch                   1000
development              100
```

Pods:

```text
critical-api
production-api
batch-job
dev-test
```

Conceptually:

```text
critical-api
     ↓
production-api
     ↓
batch-job
     ↓
dev-test
```

Higher values represent higher priority.

---

# Creating Multiple Priority Classes

Create:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: production

value: 10000

globalDefault: false

preemptionPolicy: PreemptLowerPriority

description: "Production workloads"
```

Another:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: batch

value: 100

globalDefault: false

preemptionPolicy: Never

description: "Batch workloads"
```

---

# Assigning Priority Classes

Production Pod:

```yaml
spec:

  priorityClassName: production
```

Batch Pod:

```yaml
spec:

  priorityClassName: batch
```

---

# Viewing Pod Priority

Run:

```bash
kubectl get pod <pod-name> -o yaml
```

Look for:

```text
priorityClassName
```

and:

```text
priority
```

---

# Viewing Priority Classes

```bash
kubectl get priorityclass
```

Example:

```text
NAME                     VALUE

system-node-critical     2000001000

system-cluster-critical  2000000000

production               10000

batch                    100
```

Actual values and available classes depend on the cluster.

---

# Hands-on Lab 1 – Create PriorityClass

Create:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: high-priority

value: 10000

globalDefault: false

description: "High priority application workloads"
```

Apply:

```bash
kubectl apply -f high-priority.yaml
```

Verify:

```bash
kubectl get priorityclass
```

---

# Hands-on Lab 2 – Create High-Priority Pod

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: high-priority-pod

spec:

  priorityClassName: high-priority

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f high-priority-pod.yaml
```

Inspect:

```bash
kubectl get pod high-priority-pod -o yaml
```

---

# Hands-on Lab 3 – Create Low-Priority Pod

Create another PriorityClass:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: low-priority

value: 100

globalDefault: false

description: "Low priority workloads"
```

Then assign it to another Pod.

Compare:

```text
priority
```

values.

---

# Hands-on Lab 4 – Test Scheduling Order

Create several Pods with different priority values.

For example:

```text
10000
5000
100
```

Create them while resources are constrained.

Observe scheduling behavior.

Use:

```bash
kubectl get pods -o wide
```

and:

```bash
kubectl describe pod <pod-name>
```

---

# Hands-on Lab 5 – Non-Preempting Priority

Create:

```yaml
apiVersion: scheduling.k8s.io/v1

kind: PriorityClass

metadata:

  name: high-nonpreempting

value: 20000

globalDefault: false

preemptionPolicy: Never

description: "High priority without preemption"
```

Deploy a Pod using it.

Verify:

```bash
kubectl get priorityclass high-nonpreempting -o yaml
```

---

# Hands-on Lab 6 – Resource-Constrained Preemption

On a disposable lab cluster:

1. Create a low-priority Pod with a substantial CPU request.
2. Create a high-priority Pod that cannot fit.
3. Allow preemption.
4. Observe the scheduling events.

Inspect:

```bash
kubectl describe pod <high-priority-pod>
```

Look for scheduling and preemption-related events.

---

# Important Lab Warning

Do not experiment with aggressive preemption policies on a production cluster.

Preemption can intentionally disrupt workloads.

Use:

```text
kind
minikube
k3d
```

or another disposable Kubernetes environment for experiments.

---

# Hands-on Lab 7 – Inspect System Priority Classes

Run:

```bash
kubectl get priorityclass
```

Identify:

```text
system-node-critical
```

and:

```text
system-cluster-critical
```

where present.

---

# Troubleshooting

## Check PriorityClass

```bash
kubectl get priorityclass
```

---

## Describe PriorityClass

```bash
kubectl describe priorityclass <name>
```

---

## Check Pod Priority

```bash
kubectl get pod <pod> -o yaml
```

---

## Check Scheduling Events

```bash
kubectl describe pod <pod>
```

---

# Example Problem

Pod:

```text
priority=10000
```

but remains:

```text
Pending
```

Possible reasons include:

```text
Insufficient resources
```

```text
Node affinity mismatch
```

```text
Untolerated taint
```

```text
Pod anti-affinity
```

```text
No feasible Node
```

High priority does not bypass normal scheduling constraints.

---

# Common Mistakes

## 1. Thinking Priority Guarantees Scheduling

Incorrect:

```text
High Priority

↓

Must Run
```

Correct:

```text
High Priority

↓

Gets preferential treatment
```

The Pod still requires a feasible scheduling solution.

---

## 2. Confusing Priority with QoS

They are different mechanisms.

```text
Priority

↓

Scheduling importance
```

```text
QoS

↓

Resource configuration class
```

---

## 3. Thinking Priority Ignores Taints

It does not.

A high-priority Pod still needs to satisfy required scheduling constraints.

---

## 4. Using Extremely High Priorities Without Policy

Poorly designed priority hierarchies can lead to unnecessary preemption.

Define a clear organization-wide priority policy.

---

## 5. Using Preemption Everywhere

Preemption can disrupt lower-priority workloads.

Use it only when the workload genuinely requires it.

---

## 6. Forgetting preemptionPolicy

A high-priority workload can use:

```yaml
preemptionPolicy: Never
```

if it should not evict lower-priority workloads.

---

## 7. Assuming Priority Creates Resources

It does not.

If the cluster has no feasible capacity:

```text
Pod

↓

Pending
```

can still occur.

---

# Priority vs Resource Requests vs Limits

| Concept | Purpose |
|---|---|
| PriorityClass | Scheduling importance |
| Resource Request | Scheduling resource requirement |
| Resource Limit | Runtime resource ceiling |
| QoS Class | Resource configuration classification |

---

# Priority vs Taints

```text
Priority

↓

Which Pod is more important?
```

```text
Taint

↓

Which Pods should be repelled from this Node?
```

---

# Priority vs Affinity

```text
Priority

↓

Importance
```

```text
Affinity

↓

Placement constraints/preferences
```

---

# Quick Revision

## PriorityClass

```text
Defines Pod priority
```

---

## Higher Value

```text
Higher value

↓

Higher priority
```

---

## Preemption

```text
High priority Pod

↓

May remove lower-priority Pods

↓

Creates capacity
```

---

## Non-Preempting

```text
High priority

+

preemptionPolicy: Never

↓

No preemption
```

---

# Essential kubectl Commands

List PriorityClasses:

```bash
kubectl get priorityclass
```

Describe PriorityClass:

```bash
kubectl describe priorityclass <name>
```

Create PriorityClass:

```bash
kubectl apply -f priorityclass.yaml
```

View Pod priority:

```bash
kubectl get pod <pod> -o yaml
```

View Pod scheduling events:

```bash
kubectl describe pod <pod>
```

List Pods:

```bash
kubectl get pods -o wide
```

---

# Interview Questions

## Basic

- What is a PriorityClass?
- Why are PriorityClasses used?
- How do you assign a PriorityClass to a Pod?
- What does the `value` field represent?
- What is Pod priority?

---

## Intermediate

- What is Pod preemption?
- What is `preemptionPolicy`?
- What is the difference between `PreemptLowerPriority` and `Never`?
- What is a non-preempting PriorityClass?
- What does `globalDefault` do?
- Can a high-priority Pod always be scheduled?

---

## Advanced

- Explain the Kubernetes preemption workflow.
- How does priority influence the Scheduler?
- How are lower-priority Pods selected as preemption victims?
- Why might a high-priority Pod remain Pending?
- Explain PriorityClass vs QoS.
- Explain PriorityClass vs resource requests.
- Explain how Priority interacts with Taints and Node Affinity.
- How would you design priority levels for a production cluster?
- When should you use a non-preempting PriorityClass?
- What risks are associated with excessive Pod preemption?
- How would you troubleshoot an unexpected preemption event?

---

# Production Priority Hierarchy

A production cluster might define:

```text
System Critical
        ↓
Critical Production
        ↓
Production
        ↓
Important Batch
        ↓
Batch
        ↓
Development
```

Example:

```text
system-critical
value = very high

critical-production
value = 100000

production
value = 10000

batch
value = 1000

development
value = 100
```

The exact numerical values should be designed according to organizational requirements.

---

# Example Production Policy

```text
Priority Level       Preemption

System Critical      Yes

Critical Production  Yes

Production           Controlled

Batch                No

Development          No
```

This can prevent development or batch workloads from competing equally with critical applications.

---

# Best Practices

### 1. Define a Clear Priority Hierarchy

Document what each priority level means.

---

### 2. Keep the Number of Priority Classes Manageable

Too many classes create unnecessary complexity.

---

### 3. Use Preemption Carefully

Preemption can intentionally disrupt lower-priority workloads.

---

### 4. Use Non-Preempting Classes When Appropriate

If a workload should receive queue priority but should not evict others:

```yaml
preemptionPolicy: Never
```

---

### 5. Do Not Use Priority as a Replacement for Capacity Planning

Priority cannot compensate for an undersized cluster.

---

### 6. Combine Priority with Resource Requests

Accurate resource requests allow the Scheduler to make meaningful decisions.

---

### 7. Protect System Workloads

System-critical workloads should have appropriate priority policies.

---

### 8. Test Preemption

Use a disposable cluster to understand the actual behavior before enabling aggressive production policies.

---

# References

## Official Kubernetes Documentation

- Pod Priority and Preemption
- PriorityClass
- Kubernetes Scheduler
- Resource Management for Pods and Containers
- Quality of Service Classes
- Assigning Pods to Nodes

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Scheduling Framework
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. Create a low-priority PriorityClass.
2. Create a high-priority PriorityClass.
3. Assign them to different Pods.
4. Inspect Pod priority values.
5. Constrain cluster resources.
6. Observe scheduling behavior.
7. Create a non-preempting PriorityClass.
8. Compare preempting and non-preempting workloads.
9. Inspect preemption-related events.
10. Study the relationship between priority and resource requests.
11. Test priority with taints and affinity.
12. Design a realistic production priority hierarchy.

---

# Chapter Summary

```text
                    PriorityClass

                          │
                          ▼
                    Priority Value

                          │
                          ▼
                         Pod

                          │
                          ▼
                     Scheduler

                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Scheduling Order       Preemption
                                  │
                                  ▼
                         Lower Priority Pods
```

A **PriorityClass** allows Kubernetes to express the relative importance of workloads.

The fundamental relationship is:

```text
PriorityClass
      ↓
Priority Value
      ↓
Pod
      ↓
Scheduler
```

Higher-priority Pods receive preferential scheduling treatment when resources are constrained.

If preemption is allowed:

```text
High Priority Pod
       ↓
Insufficient Resources
       ↓
Find Lower Priority Victims
       ↓
Preempt
       ↓
Schedule High Priority Pod
```

However:

```text
High Priority

≠

Guaranteed Scheduling
```

and:

```text
High Priority

≠

Ignore Scheduling Constraints
```

A Pod must still satisfy requirements involving:

```text
Resources
Taints
Node Affinity
Pod Affinity
Pod Anti-Affinity
Topology
Storage
```

The most important distinction is:

```text
Priority
    ↓
How important is the Pod?

Preemption
    ↓
Can lower-priority Pods be removed?

Resource Request
    ↓
How much resource does the Pod require?

Resource Limit
    ↓
What is the runtime resource ceiling?

QoS
    ↓
How is the Pod's resource configuration classified?
```

A well-designed production cluster should use PriorityClasses deliberately, with clear policies for:

```text
System Workloads
Critical Applications
Production Applications
Batch Processing
Development
```

This ensures that scarce cluster resources are allocated according to business and operational importance rather than treating every workload equally.

---

## Next Chapter

# Chapter 42 – Resource Requests & Limits

Topics will include:

- Kubernetes Resources
- CPU
- Memory
- Resource Requests
- Resource Limits
- How the Scheduler Uses Requests
- CPU Units
- Memory Units
- Requests vs Limits
- CPU Throttling
- Memory OOM Behavior
- Quality of Service Classes
- Guaranteed
- Burstable
- BestEffort
- LimitRange
- ResourceQuota
- Namespace Resource Management
- Pod-Level Resource Configuration
- Container-Level Resources
- Resource Overcommitment
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---
```