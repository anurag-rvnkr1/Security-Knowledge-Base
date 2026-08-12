# Chapter 36 – Scheduler

## Overview

Kubernetes can run thousands of Pods across hundreds of Worker Nodes.

When a Pod is created, Kubernetes must answer an important question:

> **Which Worker Node should run this Pod?**

The component responsible for making this decision is the **Kubernetes Scheduler**.

The Scheduler watches for newly created Pods that do not yet have a Node assigned and selects the most suitable Node based on:

- Resource availability
- Node constraints
- Affinity rules
- Anti-affinity rules
- Taints and tolerations
- Pod priority
- Topology constraints
- Node conditions
- Scheduling policies

The Scheduler does **not** start containers.

Instead:

```text
Scheduler

↓

Selects Node

↓

kubelet on Selected Node

↓

Container Runtime

↓

Containers Start
```

> **The Scheduler decides where a Pod should run; the kubelet is responsible for running it on that Node.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What the Kubernetes Scheduler is
- Why scheduling is required
- Scheduler architecture
- Pod scheduling lifecycle
- Scheduling Queue
- Filtering
- Scoring
- Binding
- Resource-aware scheduling
- Node selection
- Scheduling constraints
- Scheduling failures
- Scheduler logs
- Manual scheduling
- Multiple schedulers
- Best practices
- Troubleshooting techniques

---

# Why Do We Need a Scheduler?

Suppose a cluster contains:

```text
Node 1
4 CPU
8 GiB RAM
```

```text
Node 2
8 CPU
16 GiB RAM
```

```text
Node 3
16 CPU
32 GiB RAM
```

A new Pod requests:

```text
CPU: 4
Memory: 8Gi
```

Kubernetes needs to determine:

```text
Which Node?
```

The Scheduler evaluates the available Nodes and selects the most suitable one.

---

# Without a Scheduler

The Pod would remain:

```text
Pending
```

because no Node would be assigned.

---

# With Scheduler

```text
Pod

↓

Scheduler

↓

Node 3

↓

kubelet

↓

Container
```

---

# High-Level Architecture

```text
                    API Server

                        │

                        ▼

                Scheduling Queue

                        │

                        ▼

                 Kubernetes
                  Scheduler

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

       Node 1         Node 2        Node 3

          │             │             │

          └─────────────┼─────────────┘

                        │

                        ▼

                  Selected Node

                        │

                        ▼

                     kubelet

                        │

                        ▼

                Container Runtime

                        │

                        ▼

                       Pod
```

---

# Scheduler Responsibilities

The Scheduler primarily determines:

```text
Where should this Pod run?
```

It evaluates:

- Node resources
- Pod requirements
- Scheduling constraints
- Node labels
- Affinity
- Taints
- Topology
- Pod priority

---

# Scheduler Does NOT

The Scheduler does not:

- Start containers
- Create Pods
- Pull images
- Configure networking
- Mount storage
- Monitor application health

These responsibilities belong to other Kubernetes components.

---

# Scheduler vs kubelet

| Scheduler | kubelet |
|---|---|
| Selects Node | Runs Pod |
| Cluster-level decision | Node-level execution |
| Evaluates constraints | Creates containers |
| Assigns Pod to Node | Monitors containers |
| Uses API Server | Uses container runtime |

---

# Scheduler Architecture

The Scheduler is a control-plane component.

Typical architecture:

```text
kube-scheduler

↓

API Server

↓

Nodes

↓

Pods
```

In a standard Kubernetes control plane:

```text
kube-apiserver
kube-scheduler
kube-controller-manager
```

run as control-plane components.

---

# Scheduler Workflow

The simplified scheduling workflow is:

```text
Pod Created

↓

Scheduling Queue

↓

Find Candidate Nodes

↓

Filter Nodes

↓

Score Nodes

↓

Select Best Node

↓

Bind Pod

↓

kubelet Starts Pod
```

---

# Step 1 – Pod Creation

Example:

```bash
kubectl apply -f pod.yaml
```

The API Server stores the Pod.

Initially:

```text
Node:

Not Assigned
```

The Pod is:

```text
Pending
```

---

# Step 2 – Scheduler Detects Pod

The Scheduler watches the API Server for Pods that need scheduling.

Conceptually:

```text
Pod

spec.nodeName = empty

↓

Scheduler Notices
```

---

# Step 3 – Scheduling Queue

The Scheduler places unscheduled Pods into an internal scheduling queue.

Conceptually:

```text
New Pod

↓

Scheduling Queue

↓

Scheduler
```

Pods can have different priorities.

Higher-priority Pods can receive preferential scheduling treatment.

---

# Scheduling Queue

The Scheduler maintains queues for Pods waiting to be scheduled.

Conceptually:

```text
Pending Pods

        │

        ▼

 ┌─────────────────┐
 │ Scheduling Queue│
 └─────────────────┘

        │
        ▼

 Scheduler
```

The exact internal queue behavior is more sophisticated and includes concepts such as:

- ActiveQ
- BackoffQ
- Unschedulable Pods

---

# Step 4 – Filtering

The Scheduler first determines which Nodes are **feasible**.

Suppose:

```text
Node 1
CPU: 2

Node 2
CPU: 8

Node 3
CPU: 16
```

Pod requests:

```text
CPU: 8
```

Filtering:

```text
Node 1

↓

Rejected
```

```text
Node 2

↓

Candidate
```

```text
Node 3

↓

Candidate
```

Filtering answers:

> **Can this Pod run on this Node?**

---

# Filtering

The Scheduler evaluates constraints such as:

- Available resources
- Node selectors
- Node affinity
- Taints
- Pod affinity
- Pod anti-affinity
- Volume topology
- Node conditions

Nodes that fail mandatory requirements are removed from consideration.

---

# Example – Resource Filtering

Pod:

```yaml
resources:

  requests:

    cpu: "4"

    memory: "8Gi"
```

Node:

```text
Available CPU: 2
```

Result:

```text
Node

↓

Filtered Out
```

---

# Example – Node Selector

Pod:

```yaml
nodeSelector:

  disk: ssd
```

Node:

```text
disk=ssd
```

Result:

```text
Candidate
```

Node:

```text
disk=hdd
```

Result:

```text
Rejected
```

---

# Example – Taints

Node:

```text
dedicated=database:NoSchedule
```

Pod without matching toleration:

```text
Rejected
```

Pod with matching toleration:

```text
Candidate
```

---

# Step 5 – Scoring

After filtering, several Nodes may remain.

Example:

```text
Node 2

Node 3

Node 4
```

The Scheduler scores these Nodes.

Scoring answers:

> **Which feasible Node is the best choice?**

---

# Filtering vs Scoring

```text
Filtering

↓

Can the Pod run here?
```

```text
Scoring

↓

Which suitable Node is preferable?
```

---

# Example

Suppose:

```text
Node 1
Rejected

Node 2
Score: 40

Node 3
Score: 75

Node 4
Score: 60
```

Scheduler chooses:

```text
Node 3
```

---

# Scheduling Plugins

Modern Kubernetes Scheduler uses a plugin-based architecture.

Plugins participate in different scheduling phases.

Examples of scheduling extensions include:

- NodeResourcesFit
- NodeAffinity
- TaintToleration
- PodTopologySpread
- InterPodAffinity
- VolumeBinding

---

# NodeResourcesFit

Evaluates whether the Node has enough resources for the Pod.

Example:

```text
Pod:

CPU = 2
Memory = 4Gi
```

Node must have enough allocatable capacity to satisfy the request.

---

# NodeAffinity

Evaluates:

```text
nodeAffinity
```

rules defined by the Pod.

Example:

```text
disk=ssd
```

---

# TaintToleration

Evaluates whether a Pod tolerates Node taints.

Example:

```text
Node:

gpu=true:NoSchedule
```

Only Pods with the appropriate toleration can be scheduled there.

---

# InterPodAffinity

Considers relationships between Pods.

Example:

```text
Frontend

↓

Prefer same Node as

↓

Backend
```

---

# PodTopologySpread

Attempts to distribute Pods across topology domains.

Example:

```text
Zone A
3 Pods

Zone B
3 Pods

Zone C
3 Pods
```

This improves availability.

---

# VolumeBinding

Storage requirements can influence scheduling.

For example:

```text
Pod

↓

PVC

↓

Topology-aware storage
```

The Scheduler considers whether the storage can be used from a candidate Node.

---

# Step 6 – Select Node

After filtering and scoring:

```text
Best Node

↓

Selected
```

Example:

```text
Pod

↓

Node 3
```

---

# Step 7 – Binding

The Scheduler updates the Pod's assignment.

Conceptually:

```text
Pod

↓

spec.nodeName

↓

node-3
```

The binding operation is sent through the API Server.

---

# Step 8 – kubelet

The kubelet on the selected Node notices the Pod assignment.

```text
Scheduler

↓

Node 3

↓

kubelet

↓

Container Runtime
```

---

# Step 9 – Container Creation

The kubelet:

- Creates the Pod sandbox
- Invokes the CNI
- Pulls images if required
- Mounts volumes
- Starts containers

---

# Complete Scheduling Flow

```text
kubectl apply

↓

API Server

↓

Pod Created

↓

Scheduling Queue

↓

Filter Nodes

↓

Score Nodes

↓

Select Node

↓

Bind Pod

↓

kubelet

↓

CNI

↓

Storage

↓

Container Runtime

↓

Application
```

---

# Resource Requests and Scheduling

Resource requests are extremely important for scheduling.

Example:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "512Mi"
```

The Scheduler uses these requests when determining whether a Node has sufficient capacity.

---

# Requests vs Actual Usage

Suppose:

```text
Pod Request:

CPU = 2
```

But actual usage is:

```text
CPU = 0.5
```

The Scheduler primarily considers the declared **request**, not instantaneous CPU usage.

Therefore:

```text
Requests

↓

Scheduling Capacity
```

while actual usage is relevant to runtime monitoring and resource management.

---

# Allocatable Resources

Nodes expose:

```text
Capacity
```

and:

```text
Allocatable
```

The Scheduler considers the resources available for Pods based on the Node's allocatable capacity and existing Pod requests.

---

# Example

Node:

```text
Capacity:

CPU = 8
Memory = 16Gi
```

System components consume resources.

Allocatable:

```text
CPU = 7
Memory = 14Gi
```

Pod requests:

```text
CPU = 2
Memory = 4Gi
```

Scheduler evaluates whether:

```text
2 CPU

+

4Gi Memory
```

can fit within the remaining allocatable resources.

---

# Node Conditions

A Node may become:

```text
Ready
```

or:

```text
NotReady
```

The Scheduler avoids unsuitable Nodes.

Examples:

```text
MemoryPressure
DiskPressure
PIDPressure
NetworkUnavailable
```

Node conditions can affect scheduling decisions.

---

# Scheduling Failure

Suppose no Node satisfies the Pod requirements.

The Pod remains:

```text
Pending
```

Example:

```text
0/3 nodes are available
```

Possible reasons:

```text
Insufficient CPU
```

```text
Insufficient memory
```

```text
Node selector mismatch
```

```text
Untolerated taint
```

```text
Affinity rules not satisfied
```

---

# Troubleshooting Pending Pods

Run:

```bash
kubectl get pods
```

Then:

```bash
kubectl describe pod <pod-name>
```

Look at:

```text
Events
```

Example:

```text
FailedScheduling
```

This is usually the first place to investigate.

---

# Example Scheduling Error

```text
0/3 nodes are available:

2 Insufficient cpu

1 node(s) had untolerated taint
```

Interpretation:

```text
Node 1
↓

CPU insufficient
```

```text
Node 2
↓

CPU insufficient
```

```text
Node 3
↓

Taint not tolerated
```

Result:

```text
Pod Pending
```

---

# Manual Scheduling

Kubernetes allows explicitly assigning a Pod to a Node using:

```yaml
nodeName: worker-01
```

Example:

```yaml
spec:

  nodeName: worker-01
```

This bypasses normal Scheduler selection.

---

# nodeName vs nodeSelector

### nodeName

```text
Pod

↓

Specific Node
```

Direct assignment.

---

### nodeSelector

```text
Pod

↓

Node Label

↓

Matching Node
```

Allows the Scheduler to select from matching Nodes.

---

# Why nodeName Should Be Used Carefully

Hard-coding:

```text
worker-01
```

creates tight coupling.

If:

```text
worker-01

↓

Unavailable
```

the Pod cannot automatically move to another suitable Node.

Prefer scheduling constraints such as:

- Node labels
- Node affinity
- Topology spread

for production workloads.

---

# Multiple Schedulers

Kubernetes supports multiple scheduler profiles and can support multiple scheduler instances/configurations.

A Pod can specify a scheduler name when using a distinct scheduler configuration:

```yaml
spec:

  schedulerName: custom-scheduler
```

The default is normally:

```text
default-scheduler
```

---

# Scheduler Profiles

Modern Kubernetes supports scheduler profiles.

Different profiles can have different plugin configurations.

Conceptually:

```text
Profile A

↓

General workloads
```

```text
Profile B

↓

Specialized workloads
```

This allows customized scheduling behavior without replacing the entire Kubernetes scheduling framework.

---

# Scheduler Extensibility

The Scheduler is highly extensible through plugins.

Scheduling extensions can influence stages such as:

```text
Queueing

↓

PreFilter

↓

Filter

↓

PostFilter

↓

PreScore

↓

Score

↓

Reserve

↓

Permit

↓

PreBind

↓

Bind

↓

PostBind
```

Not every plugin participates in every phase.

---

# Scheduling Framework

The scheduling framework provides extension points for customizing Scheduler behavior.

Important phases include:

### PreFilter

Prepares information before filtering.

---

### Filter

Determines whether a Node is feasible.

---

### PostFilter

Runs when no feasible Node is found.

Often useful for advanced scheduling behavior.

---

### PreScore

Prepares information before scoring.

---

### Score

Assigns scores to feasible Nodes.

---

### Reserve

Reserves resources or state before binding.

---

### Permit

Can delay or reject scheduling.

---

### PreBind

Performs operations before binding.

---

### Bind

Assigns the Pod to a Node.

---

### PostBind

Runs after binding.

---

# Scheduler Architecture Summary

```text
Pod

↓

Queue

↓

PreFilter

↓

Filter

↓

PreScore

↓

Score

↓

Reserve

↓

Permit

↓

PreBind

↓

Bind

↓

PostBind
```

This is a conceptual representation; actual plugin participation depends on configuration.

---

# Scheduling and High Availability

Suppose:

```text
Control Plane

↓

kube-scheduler
```

The scheduler itself is typically run in a highly available control plane configuration.

Multiple scheduler instances may exist, but only one active scheduler instance performs scheduling work for a given scheduler identity at a time, with leader election coordinating active/standby behavior.

---

# Scheduler and Storage

Storage can influence scheduling.

Example:

```text
Pod

↓

PVC

↓

PV

↓

Topology
```

If a volume is restricted to:

```text
Zone A
```

the Scheduler must ensure that the Pod can run on a compatible Node.

---

# Scheduler and Networking

The Scheduler generally does not configure Pod networking.

Instead:

```text
Scheduler

↓

Select Node
```

Then:

```text
kubelet

↓

Container Runtime

↓

CNI

↓

Pod Network
```

---

# Scheduler and CNI

The relationship is:

```text
Scheduler

↓

Node Selection
```

```text
CNI

↓

Network Configuration
```

They solve different problems.

---

# Hands-on Lab 1 – Observe Scheduling

Create a simple Pod:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: scheduler-demo

spec:

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f scheduler-demo.yaml
```

Check:

```bash
kubectl get pod -o wide
```

Observe the selected Node.

---

# Hands-on Lab 2 – Inspect Scheduling Events

```bash
kubectl describe pod scheduler-demo
```

Look for:

```text
Scheduled
```

This event indicates that the Pod was assigned to a Node.

---

# Hands-on Lab 3 – Resource-Based Scheduling

Create a Pod with:

```yaml
resources:

  requests:

    cpu: "1"

    memory: "1Gi"
```

Observe where it is scheduled.

Increase the resource request and observe how available Nodes change.

---

# Hands-on Lab 4 – Node Selector

Label a Node:

```bash
kubectl label node <node-name> disk=ssd
```

Create a Pod:

```yaml
spec:

  nodeSelector:

    disk: ssd
```

Verify:

```bash
kubectl get pod -o wide
```

---

# Hands-on Lab 5 – Force a Scheduling Failure

Create a Pod requesting an impossible resource amount:

```yaml
resources:

  requests:

    cpu: "100"
```

Check:

```bash
kubectl get pod
```

The Pod should remain:

```text
Pending
```

Inspect:

```bash
kubectl describe pod <pod-name>
```

Read the `FailedScheduling` event.

---

# Hands-on Lab 6 – Inspect Node Resources

Run:

```bash
kubectl describe node <node-name>
```

Look for:

```text
Capacity
```

and:

```text
Allocatable
```

Also inspect:

```text
Non-terminated Pods
```

to understand how existing Pod requests consume Node capacity.

---

# Hands-on Lab 7 – Manual Scheduling

Create a Pod with:

```yaml
spec:

  nodeName: <node-name>
```

Verify that the Pod is placed directly on the specified Node.

Compare this behavior with `nodeSelector`.

---

# Common Mistakes

## 1. Thinking the Scheduler Starts Containers

Incorrect:

```text
Scheduler

↓

Starts Container
```

Correct:

```text
Scheduler

↓

Selects Node

↓

kubelet

↓

Starts Container
```

---

## 2. Ignoring Resource Requests

If Pods do not specify requests:

```text
Scheduling decisions

↓

Less predictable
```

Proper requests improve scheduling accuracy.

---

## 3. Confusing Requests with Limits

Requests:

```text
Used by Scheduler
```

Limits:

```text
Runtime resource ceiling
```

They serve different purposes.

---

## 4. Using nodeName Everywhere

Hard-coding Nodes reduces flexibility.

Prefer:

```text
nodeSelector
```

or:

```text
nodeAffinity
```

when possible.

---

## 5. Ignoring Taints

A Node may reject Pods because of:

```text
NoSchedule
```

or other taint effects.

Check:

```bash
kubectl describe node <node-name>
```

---

## 6. Ignoring Pod Affinity Rules

Strict affinity or anti-affinity can make Pods unschedulable.

---

## 7. Ignoring Storage Topology

A Pod using topology-constrained storage may not be schedulable on every Node.

---

## 8. Assuming the Most Powerful Node Is Always Selected

The Scheduler does not simply choose:

```text
Largest Node
```

It evaluates configured filtering and scoring plugins.

---

# Quick Revision

## Scheduler Purpose

```text
Unscheduled Pod

↓

Scheduler

↓

Best Feasible Node
```

---

## Main Workflow

```text
Queue

↓

Filter

↓

Score

↓

Select

↓

Bind
```

---

## Execution

```text
Scheduler

↓

Node Selected

↓

kubelet

↓

Container Runtime

↓

Pod
```

---

# Essential kubectl Commands

View Pods:

```bash
kubectl get pods -o wide
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

View Nodes:

```bash
kubectl get nodes
```

Describe Node:

```bash
kubectl describe node <node-name>
```

View Scheduler:

```bash
kubectl get pods -n kube-system
```

Look for:

```text
kube-scheduler
```

View scheduler logs:

```bash
kubectl logs -n kube-system <kube-scheduler-pod>
```

---

# Interview Questions

## Basic

- What is the Kubernetes Scheduler?
- Why is the Scheduler required?
- What is the difference between Scheduler and kubelet?
- What happens when a Pod is created without a Node assignment?

---

## Intermediate

- Explain the Kubernetes scheduling workflow.
- What is the difference between filtering and scoring?
- What are resource requests?
- What is a nodeSelector?
- What causes a Pod to remain Pending?

---

## Advanced

- Explain the complete Kubernetes scheduling lifecycle.
- How does the Scheduler determine whether a Node is feasible?
- What are Scheduler plugins?
- Explain the Scheduling Framework and its extension points.
- How do resource requests influence scheduling?
- How do taints and tolerations affect scheduling?
- How does topology-aware storage influence scheduling?
- Explain the difference between `nodeName`, `nodeSelector`, and node affinity.
- How does Kubernetes maintain scheduler high availability?
- How would you troubleshoot a Pod stuck in `Pending`?
- How can custom scheduler profiles change scheduling behavior?

---

# References

## Official Kubernetes Documentation

- Kubernetes Scheduler
- Scheduling Framework
- Assigning Pods to Nodes
- Resource Management for Pods and Containers
- Node Selection
- Pod Topology Spread Constraints
- Taints and Tolerations

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Architecture
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Kubernetes Production Scheduling
- CIS Kubernetes Benchmark
- Kubernetes Resource Management Best Practices

---

# Recommended Practice

1. Deploy Pods and observe their assigned Nodes.
2. Inspect `Scheduled` events.
3. Compare Node `Capacity` and `Allocatable`.
4. Create Pods with different resource requests.
5. Experiment with `nodeSelector`.
6. Create scheduling failures intentionally and diagnose `FailedScheduling`.
7. Experiment with taints and tolerations.
8. Test Pod affinity and anti-affinity.
9. Observe how PVC topology can affect scheduling.
10. Study Scheduler plugins before moving to advanced scheduling topics.

---

# Chapter Summary

```text
                    Pod Created
                         │
                         ▼
                 Scheduling Queue
                         │
                         ▼
                      Filter
                         │
                  Feasible Nodes
                         │
                         ▼
                       Score
                         │
                         ▼
                   Best Node
                         │
                         ▼
                       Bind
                         │
                         ▼
                     kubelet
                         │
                         ▼
                Container Runtime
                         │
                         ▼
                        Pod
```

The **Kubernetes Scheduler** is responsible for deciding where unscheduled Pods should run. It evaluates available Nodes against resource requirements, labels, affinity rules, taints, topology constraints, storage requirements, and other scheduling policies.

The core scheduling process is:

```text
Queue
  ↓
Filter
  ↓
Score
  ↓
Select
  ↓
Bind
```

After the Scheduler assigns the Pod to a Node, the **kubelet** takes over and is responsible for actually running the Pod.

The most important distinction to remember is:

```text
Scheduler
    ↓
WHERE should the Pod run?

kubelet
    ↓
RUN the Pod on that Node
```

---

## Next Chapter

# Chapter 37 – Node Selectors

Topics will include:

- Node Labels
- `nodeSelector`
- Node Selection
- Scheduling Workflow
- Multiple Node Labels
- Real-World Use Cases
- `nodeSelector` vs Node Affinity
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---