# Chapter 45 – Cluster Autoscaler

## Overview

In the previous chapters, we learned:

```text
HPA
 ↓
Changes the number of Pods
```

and:

```text
VPA
 ↓
Changes CPU/Memory resources of Pods
```

But what happens when Kubernetes does not have enough Nodes to run those Pods?

For example:

```text
Traffic increases
      ↓
HPA creates more Pods
      ↓
Available Node capacity is exhausted
      ↓
New Pods remain Pending
      ↓
Cluster Autoscaler detects unschedulable Pods
      ↓
Adds Nodes
      ↓
Pods become schedulable
```

This is the role of the **Cluster Autoscaler (CA)**.

> **Cluster Autoscaler automatically adjusts the number of Nodes in a cluster by adding Nodes when Pods cannot be scheduled and removing underutilized Nodes when they are no longer needed.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Cluster Autoscaler is
- Why Node autoscaling is required
- Cluster Autoscaler architecture
- Scale-up
- Scale-down
- Unschedulable Pods
- Node Groups
- Node Pools
- Cloud provider integration
- Minimum and maximum Node counts
- Expander strategies
- Scale-down candidates
- Node draining
- Pod eviction
- PodDisruptionBudgets
- DaemonSets
- Local storage
- Node affinity
- Taints and tolerations
- HPA and Cluster Autoscaler
- VPA and Cluster Autoscaler
- Cost optimization
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Interview questions

---

# What Is Cluster Autoscaler?

Cluster Autoscaler is a Kubernetes component that adjusts cluster capacity.

It can:

```text
Add Nodes
```

when workloads cannot be scheduled.

It can also:

```text
Remove Nodes
```

when Nodes are no longer required and their workloads can safely be moved elsewhere.

The basic model is:

```text
                    Cluster Autoscaler
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
           Scale Up                  Scale Down
              │                         │
              ▼                         ▼
        Add Nodes                  Remove Nodes
```

---

# Why Is Cluster Autoscaling Needed?

Suppose a cluster has:

```text
3 Nodes
```

Each Node provides:

```text
4 CPU
8Gi Memory
```

Total theoretical capacity:

```text
CPU = 12
Memory = 24Gi
```

Now HPA scales an application from:

```text
6 Pods
```

to:

```text
20 Pods
```

The existing Nodes may not have enough available capacity.

Some Pods become:

```text
Pending
```

Cluster Autoscaler can detect that these Pods cannot currently be scheduled and request additional Nodes.

---

# Basic Architecture

```text
                    User Traffic
                         │
                         ▼
                        HPA
                         │
                         ▼
                    More Pods
                         │
                         ▼
                    Scheduler
                         │
                ┌────────┴────────┐
                │                 │
                ▼                 ▼
             Schedulable       Pending
                │                 │
                │                 ▼
                │       Cluster Autoscaler
                │                 │
                │                 ▼
                │            Add Nodes
                │                 │
                └─────────┬───────┘
                          ▼
                      Scheduler
                          │
                          ▼
                         Pods
```

---

# Cluster Autoscaler vs HPA

This is one of the most important distinctions.

## HPA

HPA changes:

```text
Pod count
```

Example:

```text
3 Pods
 ↓
10 Pods
```

---

## Cluster Autoscaler

Cluster Autoscaler changes:

```text
Node count
```

Example:

```text
3 Nodes
 ↓
5 Nodes
```

---

# HPA + Cluster Autoscaler

They can work together.

Example:

```text
Traffic increases
      ↓
HPA increases Pods
      ↓
Pods require more resources
      ↓
Some Pods cannot fit
      ↓
Pods become Pending
      ↓
Cluster Autoscaler adds Nodes
      ↓
Scheduler places Pods
```

This creates an elastic system.

---

# Cluster Autoscaler vs VPA

VPA:

```text
Changes resources requested by Pods
```

Cluster Autoscaler:

```text
Changes number of Nodes
```

Together:

```text
VPA
 ↓
Larger Pod requests
 ↓
Insufficient capacity
 ↓
Cluster Autoscaler
 ↓
More Nodes
```

---

# Cluster Autoscaler vs Manual Scaling

Without autoscaling:

```text
Administrator

↓

Manually adds Nodes
```

With Cluster Autoscaler:

```text
Cluster state

↓

Autoscaler evaluates demand

↓

Nodes automatically adjusted
```

---

# Node Groups

Cluster Autoscaler typically works with:

```text
Node Groups
```

or:

```text
Node Pools
```

A Node Group is a logical collection of similar Nodes.

Example:

```text
Worker Group

min = 2
max = 10

Node type:
4 CPU
16Gi Memory
```

The autoscaler can increase:

```text
2 → 3 → 4 → ... → 10
```

according to cluster demand and provider capabilities.

---

# Node Pool

Cloud Kubernetes platforms often use the term:

```text
Node Pool
```

A pool contains Nodes with similar:

```text
Instance type
CPU
Memory
OS
Labels
Taints
Configuration
```

The exact terminology varies by cloud provider.

---

# Minimum Nodes

Example:

```text
minNodes = 3
```

The autoscaler should not normally reduce that Node Group below:

```text
3 Nodes
```

---

# Maximum Nodes

Example:

```text
maxNodes = 10
```

The autoscaler should not normally increase that Node Group above:

```text
10 Nodes
```

---

# Node Group Example

Suppose:

```text
Node Group:

Minimum = 2
Maximum = 6
Current = 3
```

During high demand:

```text
3
 ↓
4
 ↓
5
```

During low demand:

```text
5
 ↓
4
 ↓
3
 ↓
2
```

The configured boundaries are respected.

---

# Scale-Up

Cluster Autoscaler performs scale-up when it determines that Pods cannot currently be scheduled because sufficient cluster capacity is unavailable.

Example:

```text
Pod A → Running
Pod B → Running
Pod C → Pending
Pod D → Pending
```

Scheduler cannot place:

```text
Pod C
Pod D
```

because Nodes lack sufficient capacity or suitable scheduling conditions.

Cluster Autoscaler detects the unschedulable Pods.

---

# Scale-Up Flow

```text
Pod Created
    ↓
Scheduler Attempts Placement
    ↓
No Suitable Node
    ↓
Pod Pending
    ↓
Cluster Autoscaler Detects
    ↓
Selects Suitable Node Group
    ↓
Requests Additional Node(s)
    ↓
Cloud Provider Creates Node
    ↓
Node Joins Cluster
    ↓
Scheduler Retries
    ↓
Pod Scheduled
```

---

# Unschedulable Pods

An important concept is:

```text
Unschedulable Pod
```

The Pod may be Pending because:

```text
Insufficient CPU
```

or:

```text
Insufficient Memory
```

or:

```text
Node Affinity
```

or:

```text
Taints
```

or:

```text
Topology Constraints
```

or other scheduling constraints.

Cluster Autoscaler can respond when adding capacity can resolve the scheduling problem.

---

# Check Pending Pods

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

You may see messages such as:

```text
0/3 nodes are available: 3 Insufficient cpu.
```

---

# Important Distinction

Not every Pending Pod causes a useful scale-up.

For example, a Pod may be unschedulable because:

```text
No Node has the required label
```

Adding generic Nodes may not solve the problem.

Similarly:

```text
Incompatible taints
```

or:

```text
Impossible affinity rules
```

may prevent scheduling even after Nodes are added.

---

# Scale-Down

Cluster Autoscaler can also remove Nodes that are no longer required.

Example:

```text
10 Nodes
```

but workloads now require only:

```text
6 Nodes
```

If suitable Nodes are underutilized and their Pods can be safely moved, Cluster Autoscaler may remove some Nodes.

---

# Scale-Down Flow

```text
Cluster Demand Decreases
        ↓
Nodes Become Underutilized
        ↓
Autoscaler Identifies Candidate
        ↓
Checks Whether Pods Can Move
        ↓
Node Drain / Pod Eviction
        ↓
Node Removed
```

---

# Why Scale-Down Is More Complicated

Removing a Node means its Pods must be handled.

Before deleting a Node, Kubernetes must consider:

```text
Can Pods be scheduled elsewhere?
```

It must account for:

```text
PodDisruptionBudgets
DaemonSets
Local Storage
Affinity
Taints
Resource Requests
Scheduling Constraints
```

---

# Node Utilization

Cluster Autoscaler can use resource utilization and scheduling simulation when determining whether Nodes are candidates for removal.

The exact behavior depends on the Cluster Autoscaler version and configuration.

Do not think of scale-down as simply:

```text
CPU < 20%
    ↓
Delete Node
```

There are additional scheduling and safety checks.

---

# Node Drain

Before removing a Node, workloads generally need to be evicted or otherwise handled.

Conceptually:

```text
Node

Pod A
Pod B
Pod C

      ↓

Drain / Eviction

      ↓

Pods rescheduled elsewhere

      ↓

Node removed
```

---

# Pod Eviction

Eviction means Kubernetes asks a Pod to terminate gracefully.

This is different from simply deleting the Node.

The objective is:

```text
Move workloads safely
```

rather than:

```text
Abruptly lose workloads
```

---

# PodDisruptionBudget

A PodDisruptionBudget (PDB) can limit voluntary disruptions.

Example:

```yaml
apiVersion: policy/v1

kind: PodDisruptionBudget

metadata:

  name: web-pdb

spec:

  minAvailable: 2

  selector:

    matchLabels:

      app: web
```

This means the application should maintain at least:

```text
2 available Pods
```

during covered voluntary disruptions.

---

# PDB and Cluster Autoscaler

Suppose:

```text
Application:

3 Pods
```

and:

```text
PDB:

minAvailable = 3
```

If every Pod must remain available, evicting any Pod may be blocked.

That can make Node scale-down impossible.

Therefore:

```text
PDB
+
Autoscaling
```

must be designed together.

---

# DaemonSets

DaemonSets commonly run one Pod on each eligible Node.

Example:

```text
Node 1 → logging agent
Node 2 → logging agent
Node 3 → logging agent
```

When considering Node removal, DaemonSet Pods are treated differently because they are recreated automatically on other eligible Nodes.

DaemonSets can still affect resource calculations and scheduling behavior.

---

# Local Storage

Pods using local storage can complicate Node scale-down.

Example:

```text
Node
 ↓
Pod
 ↓
Local filesystem data
```

If the Pod depends on local data, moving it to another Node may not preserve that data.

Autoscaler therefore has to consider local storage-related constraints and configuration.

---

# Node Affinity

Suppose a Pod requires:

```yaml
nodeSelector:

  disk: nvme
```

and only one Node Group provides:

```text
disk=nvme
```

If the Pod becomes Pending:

```text
Cluster Autoscaler
```

needs a Node Group capable of satisfying that requirement.

Adding a generic Node may not help.

---

# Taints and Tolerations

Suppose a Node has:

```text
taint:

dedicated=gpu:NoSchedule
```

A Pod without the corresponding toleration cannot run there.

If a Pending Pod requires GPU Nodes, the appropriate Node Group must be available.

---

# GPU Node Groups

Specialized workloads may require:

```text
GPU
```

Example:

```yaml
resources:

  limits:

    nvidia.com/gpu: 1
```

Cluster Autoscaler can work with specialized Node Groups when configured correctly.

The autoscaler must understand which Node Group can satisfy the Pod's requirements.

---

# Expander Strategies

When multiple Node Groups could satisfy a scale-up request, Cluster Autoscaler can use an **expander strategy** to choose among them.

Common strategies include concepts such as:

```text
least-waste
```

```text
most-pods
```

```text
price
```

```text
random
```

The exact available strategies and behavior depend on the Cluster Autoscaler version and cloud-provider integration.

---

# Least-Waste

The goal is generally to select the Node Group that leaves the least unused capacity after accommodating pending workloads.

Conceptually:

```text
Pending workload:

2 CPU

Node Group A:
4 CPU

Unused:
2 CPU

Node Group B:
8 CPU

Unused:
6 CPU
```

The smaller Node may be preferred under a least-waste strategy.

---

# Most-Pods

This strategy considers how many pending Pods can potentially be accommodated by a Node Group.

The objective is to maximize scheduling opportunities.

---

# Price-Based Selection

Some cloud integrations can use pricing information.

The autoscaler may prefer a cheaper Node type when it can satisfy workload requirements.

Exact behavior depends on the cloud provider and configuration.

---

# Random

A random strategy can select among eligible Node Groups without applying a resource-efficiency preference.

---

# Cloud Provider Integration

Cluster Autoscaler needs a mechanism to create and remove Nodes.

Therefore, it commonly integrates with cloud provider infrastructure.

Examples include:

```text
Amazon Web Services
Microsoft Azure
Google Cloud
```

The exact implementation depends on the Kubernetes environment.

---

# Managed Kubernetes

Cloud Kubernetes services commonly provide Node Pool or Node Group abstractions.

Examples:

```text
AWS
Azure
Google Cloud
```

Cluster Autoscaler can interact with these pools to change their size.

---

# Important Cloud Concept

Cluster Autoscaler does not magically create a physical machine by itself.

Conceptually:

```text
Cluster Autoscaler
       ↓
Cloud Provider / Node Group
       ↓
New VM / Instance
       ↓
Kubernetes Node
```

---

# Node Lifecycle

When scaling up:

```text
Autoscaler requests Node

        ↓

Cloud provider creates VM

        ↓

Kubernetes components start

        ↓

Node registers

        ↓

Node becomes Ready

        ↓

Scheduler places Pods
```

---

# Check Nodes

```bash
kubectl get nodes
```

Watch:

```bash
kubectl get nodes -w
```

Check details:

```bash
kubectl describe node <node-name>
```

---

# Node Readiness

A newly created Node may initially show:

```text
NotReady
```

before becoming:

```text
Ready
```

The Node needs:

```text
Kubelet
Networking
Container Runtime
CNI
Control Plane Connectivity
```

to become operational.

---

# Cluster Autoscaler and Scheduler

Scheduler:

```text
Where should this Pod run?
```

Cluster Autoscaler:

```text
Do we need more Nodes because the Pod cannot currently run?
```

They are different controllers.

---

# Scheduler + Cluster Autoscaler

```text
               Pod
                │
                ▼
            Scheduler
                │
        ┌───────┴───────┐
        │               │
        ▼               ▼
      Fits           Doesn't Fit
        │               │
        ▼               ▼
    Schedule       Pending
                        │
                        ▼
                Cluster Autoscaler
                        │
                        ▼
                    Add Node
                        │
                        ▼
                    Scheduler
```

---

# Cluster Autoscaler and Requests

Resource requests are extremely important.

Suppose:

```text
Pod request:

CPU = 2
Memory = 4Gi
```

A Node must have sufficient allocatable capacity.

If all Nodes have:

```text
1 CPU available
```

the Pod cannot fit.

Cluster Autoscaler can add capacity if an appropriate Node Group can accommodate it.

---

# Requests Too Low

Suppose:

```text
Actual usage = 2 CPU

Request = 250m
```

The Scheduler and Cluster Autoscaler may see only:

```text
250m
```

as the scheduling requirement.

This can lead to underestimation of capacity requirements.

Therefore:

> **Accurate resource requests are important for both scheduling and autoscaling.**

---

# Requests Too High

Suppose:

```text
Actual usage = 250m

Request = 4 CPU
```

Cluster Autoscaler may add more Nodes than truly necessary because workloads appear to require more capacity.

This increases:

```text
Cost
```

and:

```text
Unused Capacity
```

---

# Cluster Autoscaler and VPA

VPA can change resource requests.

Example:

```text
Current request:
500m CPU
```

VPA:

```text
Recommendation:
2 CPU
```

Now:

```text
Pod requires more capacity
```

If existing Nodes cannot accommodate the Pod:

```text
Pending
 ↓
Cluster Autoscaler
 ↓
Add Node
```

---

# Cluster Autoscaler and HPA

HPA increases replicas:

```text
3
 ↓
8
```

If there is insufficient capacity:

```text
Pending Pods
```

Cluster Autoscaler responds:

```text
Add Nodes
```

This is a common production architecture.

---

# Complete Autoscaling Architecture

```text
                    User Traffic
                         │
                         ▼
                        HPA
                         │
                         ▼
                    More Pods
                         │
                         ▼
                     Scheduler
                         │
                ┌────────┴────────┐
                │                 │
                ▼                 ▼
             Schedule          Pending
                                  │
                                  ▼
                         Cluster Autoscaler
                                  │
                                  ▼
                             Add Nodes
                                  │
                                  ▼
                              Scheduler
                                  │
                                  ▼
                                 Pods
```

VPA can also participate:

```text
VPA
 ↓
Adjust Pod Requests
 ↓
Scheduler
 ↓
Possible Pending
 ↓
Cluster Autoscaler
 ↓
More Nodes
```

---

# Scale-Down Candidate

A Node may become a candidate for removal when:

```text
It is sufficiently underutilized
```

and:

```text
Its Pods can be moved elsewhere
```

and:

```text
Removing it does not violate relevant constraints
```

The exact thresholds and timing depend on configuration.

---

# Unremovable Node

A Node may not be removable because:

```text
Pods cannot be rescheduled
```

or:

```text
PDB blocks eviction
```

or:

```text
Local storage is involved
```

or:

```text
Affinity constraints prevent relocation
```

or:

```text
Other scheduling constraints apply
```

---

# Why Nodes May Not Scale Down

Common reasons:

```text
PodDisruptionBudget
```

```text
Local storage
```

```text
Pod affinity
```

```text
Node affinity
```

```text
Taints and tolerations
```

```text
Insufficient remaining capacity
```

```text
Pods that cannot be safely evicted
```

---

# Scale-Down Timing

Cluster Autoscaler generally does not immediately remove a Node the moment utilization decreases.

It uses:

```text
Evaluation intervals
```

and:

```text
Scale-down delays / stabilization
```

depending on configuration.

This prevents:

```text
Rapid scale-up
 ↓
Rapid scale-down
 ↓
Rapid scale-up
```

---

# Scaling Thrashing

Suppose:

```text
Traffic increases
 ↓
Add Nodes

Traffic decreases
 ↓
Remove Nodes

Traffic increases
 ↓
Add Nodes
```

This can cause:

```text
Node Churn
```

and:

```text
Higher Costs
```

Autoscaling systems therefore use delays and stabilization mechanisms.

---

# Cost Optimization

Cluster Autoscaler can reduce cost by removing unnecessary Nodes.

Example:

```text
Daytime:

10 Nodes
```

Night:

```text
4 Nodes
```

Instead of running:

```text
10 Nodes × 24 hours
```

the cluster can potentially reduce capacity during low-demand periods.

---

# But Cost Is Not the Only Goal

Autoscaling should balance:

```text
Cost
+
Performance
+
Availability
+
Reliability
```

Aggressive scale-down may save money but increase:

```text
Startup delays
Pod churn
Application disruption
```

---

# Capacity Planning

Before configuring Cluster Autoscaler, consider:

```text
Minimum capacity
Maximum capacity
Node type
Pod density
Resource requests
Availability requirements
Failure domains
Cost
```

---

# Multiple Node Groups

A production cluster may have:

```text
General-purpose Node Group

GPU Node Group

Memory-optimized Node Group

Compute-optimized Node Group
```

Example:

```text
General:

min = 3
max = 20
```

```text
GPU:

min = 0
max = 5
```

```text
Memory:

min = 2
max = 10
```

This enables workload-specific scaling.

---

# Labels and Node Groups

Nodes can have labels:

```yaml
labels:

  workload: gpu
```

Pods can request:

```yaml
nodeSelector:

  workload: gpu
```

This helps ensure the workload lands on the correct Node Group.

---

# Taints and Node Groups

A specialized Node Group can be protected with a taint:

```text
workload=gpu:NoSchedule
```

GPU workloads use:

```yaml
tolerations:

- key: workload

  operator: Equal

  value: gpu

  effect: NoSchedule
```

This prevents unrelated workloads from consuming specialized capacity.

---

# Cluster Autoscaler and Spot Nodes

Cloud providers may offer lower-cost interruptible/spot capacity.

Cluster Autoscaler can work with such Node Groups depending on provider integration.

However, workloads must tolerate:

```text
Node interruption
```

and:

```text
Pod rescheduling
```

Use appropriate:

```text
PDB
Replica counts
Topology distribution
Application recovery
```

---

# High Availability

Do not design autoscaling around a single Node Group if availability requirements are high.

Consider:

```text
Multiple Availability Zones
```

and:

```text
Multiple Node Groups
```

where appropriate.

---

# Failure Scenario

Suppose:

```text
3 Nodes
```

across:

```text
3 Availability Zones
```

If one zone fails:

```text
1/3 capacity lost
```

Cluster Autoscaler may add capacity elsewhere if the infrastructure and Node Groups permit it.

---

# Pod Topology

Topology constraints can influence where Pods can run.

Examples:

```text
Zone
Region
Hostname
```

If Pods require distribution across zones, the autoscaler must work with the scheduler's constraints.

---

# Hands-on Lab 1 – Observe Pending Pods

Create a Pod with a large request:

```yaml
resources:

  requests:

    cpu: "10"

    memory: "32Gi"
```

On a small cluster, the Pod may remain:

```text
Pending
```

Inspect:

```bash
kubectl describe pod <pod-name>
```

Study the scheduling events.

---

# Hands-on Lab 2 – Observe Node Capacity

Run:

```bash
kubectl get nodes
```

Then:

```bash
kubectl describe node <node-name>
```

Look for:

```text
Capacity
Allocatable
Allocated resources
```

---

# Hands-on Lab 3 – HPA + Cluster Autoscaler

In a cloud or suitable autoscaling cluster:

```text
1. Deploy application
2. Configure HPA
3. Generate load
4. Observe Pod count increase
5. Exhaust available Node capacity
6. Observe Pending Pods
7. Observe Node scale-up
8. Observe Pods becoming Running
```

Useful commands:

```bash
kubectl get hpa -w
```

```bash
kubectl get pods -w
```

```bash
kubectl get nodes -w
```

---

# Hands-on Lab 4 – Scale Down

Reduce application demand.

Observe:

```text
Pods decrease

↓

Nodes become underutilized

↓

Autoscaler identifies removable Nodes

↓

Pods are moved

↓

Node removed
```

Monitor:

```bash
kubectl get nodes -w
```

---

# Hands-on Lab 5 – PodDisruptionBudget

Create:

```yaml
apiVersion: policy/v1

kind: PodDisruptionBudget

metadata:

  name: web-pdb

spec:

  minAvailable: 2

  selector:

    matchLabels:

      app: web
```

Observe how disruption constraints affect Node maintenance and scale-down behavior.

---

# Hands-on Lab 6 – Node Affinity

Create a Node label:

```bash
kubectl label node <node-name> workload=special
```

Then configure:

```yaml
nodeSelector:

  workload: special
```

Observe scheduling behavior.

In an autoscaling environment, consider which Node Group could satisfy the requirement if that Node becomes unavailable.

---

# Hands-on Lab 7 – Taints and Tolerations

Add a taint:

```bash
kubectl taint nodes <node-name> dedicated=special:NoSchedule
```

Create a Pod without a matching toleration.

Observe:

```text
Pending
```

Then add:

```yaml
tolerations:

- key: dedicated

  operator: Equal

  value: special

  effect: NoSchedule
```

Observe scheduling behavior.

Remove the test taint afterward:

```bash
kubectl taint nodes <node-name> dedicated=special:NoSchedule-
```

---

# Troubleshooting

## Cluster Autoscaler Is Not Scaling Up

Check:

```bash
kubectl get pods
```

Find:

```text
Pending
```

Then:

```bash
kubectl describe pod <pod-name>
```

Check:

```text
Events
```

---

# Check Autoscaler Logs

Depending on installation:

```bash
kubectl logs -n kube-system deployment/cluster-autoscaler
```

The exact resource name and namespace may differ.

---

# Look for Scale-Up Messages

Autoscaler logs may contain information about:

```text
Unschedulable Pods
Node Group Selection
Scale-Up Decision
Cloud Provider Errors
```

---

# Cluster Autoscaler Does Not Scale Up

Possible causes:

```text
No eligible Node Group
```

```text
Maximum Node count reached
```

```text
Pod cannot be satisfied by any available Node Group
```

```text
Cloud provider failure
```

```text
Incorrect autoscaler configuration
```

```text
Scheduling constraints prevent scale-up
```

---

# Maximum Capacity Reached

Example:

```text
Current Nodes = 10
Maximum = 10
```

If Pods remain Pending:

```text
Cluster Autoscaler cannot exceed configured maximum
```

You may need to increase capacity limits after validating cost and infrastructure constraints.

---

# Scale-Up but Pods Still Pending

Possible reasons:

```text
New Nodes are not Ready
```

```text
Node does not satisfy Pod constraints
```

```text
Insufficient resource type
```

```text
Taints without tolerations
```

```text
Affinity mismatch
```

```text
Network/CNI issue
```

---

# Cluster Autoscaler Is Not Scaling Down

Possible causes:

```text
Minimum Node count reached
```

```text
Pods cannot be moved
```

```text
PDB prevents eviction
```

```text
Local storage prevents removal
```

```text
Affinity rules prevent relocation
```

```text
Node is not considered sufficiently underutilized
```

---

# Check PDBs

```bash
kubectl get pdb
```

Describe:

```bash
kubectl describe pdb <pdb-name>
```

---

# Check Node Utilization

```bash
kubectl top nodes
```

and:

```bash
kubectl describe node <node-name>
```

---

# Check Scheduling Constraints

Inspect:

```bash
kubectl get pod <pod-name> -o yaml
```

Look for:

```text
nodeSelector
affinity
tolerations
topologySpreadConstraints
resources
```

---

# Common Mistakes

## 1. Confusing HPA and Cluster Autoscaler

Remember:

```text
HPA
 ↓
Pods
```

```text
Cluster Autoscaler
 ↓
Nodes
```

---

## 2. Assuming Every Pending Pod Causes Scale-Up

A Pod may be unschedulable for reasons that additional generic Nodes cannot solve.

---

## 3. Setting maxNodes Too Low

Example:

```text
max = 3
```

while workload requires:

```text
10 Nodes
```

The cluster cannot scale beyond 3.

---

## 4. Ignoring Resource Requests

Cluster Autoscaler relies heavily on scheduling information.

Bad requests produce bad capacity decisions.

---

## 5. Ignoring PDB

An overly restrictive PDB can prevent safe Node removal.

---

## 6. Ignoring Affinity

A Node may look removable, but its Pods may have nowhere else to go.

---

## 7. Ignoring Taints

Specialized Node Groups may require tolerations.

---

## 8. Ignoring Local Storage

Pods using local storage can prevent Node removal or complicate safe rescheduling.

---

## 9. Using Huge Pod Requests

Huge requests can cause:

```text
Poor bin packing
```

and:

```text
Unnecessary Node scaling
```

---

## 10. Setting Maximum Capacity Too Low

This can cause:

```text
Pending Pods
```

during legitimate traffic spikes.

---

## 11. Scaling Without Considering Cost

Unlimited scale-out is not a production strategy.

Always define:

```text
Maximum capacity
Budget
SLO
```

---

## 12. Treating Autoscaling as Instantaneous

Node creation takes time.

The flow is:

```text
Decision
 ↓
Cloud VM Creation
 ↓
Node Initialization
 ↓
Node Registration
 ↓
Ready
 ↓
Pod Scheduling
```

This can take longer than Pod-level scaling.

---

# Cluster Autoscaler and Startup Time

Suppose:

```text
Node startup = 2 minutes
```

and:

```text
Traffic spike = 30 seconds
```

Cluster Autoscaler may not react quickly enough to fully address that short spike.

Therefore HPA configuration should account for:

```text
Existing spare capacity
Pod startup time
Node startup time
Traffic patterns
```

---

# Overprovisioning

Some production environments intentionally maintain spare capacity.

Example:

```text
Normal usage = 70%

Reserved spare capacity = 20%
```

This can reduce:

```text
Node scale-up latency
```

at the cost of:

```text
Additional infrastructure cost
```

---

# Buffer Capacity

A capacity buffer can help absorb sudden workload spikes.

Conceptually:

```text
Current workload
      ↓
80% capacity

Remaining
      ↓
20% buffer
```

When traffic increases:

```text
Use buffer first
      ↓
Autoscaler adds Nodes
```

---

# Cost Optimization Strategy

A mature autoscaling strategy can combine:

```text
Accurate requests
+
HPA
+
Cluster Autoscaler
+
Right-sized Nodes
+
Multiple Node Groups
+
Cost-aware capacity
```

---

# Production Architecture

A robust architecture may look like:

```text
                       Internet
                          │
                          ▼
                    Load Balancer
                          │
                          ▼
                       Service
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            Pod         Pod         Pod
              │           │           │
              └───────────┼───────────┘
                          │
                          ▼
                         HPA
                          │
                          ▼
                   Desired Pod Count
                          │
                          ▼
                      Scheduler
                          │
                  ┌───────┴───────┐
                  │               │
                  ▼               ▼
                Fits            Pending
                  │               │
                  │               ▼
                  │      Cluster Autoscaler
                  │               │
                  │               ▼
                  │          Node Groups
                  │               │
                  │               ▼
                  │          New Nodes
                  │               │
                  └───────┬───────┘
                          ▼
                       Scheduler
                          │
                          ▼
                         Pods
```

---

# Multi-Node-Group Architecture

Example:

```text
                Cluster Autoscaler
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   General Pool     GPU Pool      Memory Pool
        │              │              │
      Nodes          Nodes          Nodes
        │              │              │
     Web Apps      ML Workloads   Databases
```

Each pool can have:

```text
Minimum size
Maximum size
Instance type
Labels
Taints
```

---

# Availability Zones

A production cluster can distribute Nodes across multiple zones:

```text
Zone A
 ├── Node
 └── Node

Zone B
 ├── Node
 └── Node

Zone C
 ├── Node
 └── Node
```

Autoscaling should preserve sufficient capacity across failure domains where possible.

---

# Cluster Autoscaler and Disaster Recovery

Autoscaling is not disaster recovery.

Cluster Autoscaler provides:

```text
Capacity elasticity
```

It does not provide:

```text
Database backups
Application backups
Persistent data recovery
```

These are handled by separate disaster-recovery mechanisms.

---

# Cluster Autoscaler and Security

Adding Nodes dynamically requires secure:

```text
Node Bootstrap
Credentials
IAM Permissions
Networking
Container Runtime
Kubelet Configuration
```

Cloud IAM permissions should follow least privilege.

---

# Monitoring Cluster Autoscaler

Monitor:

```text
Current Node count
Desired Node count
Pending Pods
Scale-up events
Scale-down events
Node provisioning time
Node utilization
```

Also monitor:

```text
HPA
VPA
Scheduler
Cloud provider
```

because autoscaling is a multi-controller system.

---

# Important Metrics

Useful operational metrics include:

```text
Pending Pods
```

```text
Node CPU utilization
```

```text
Node memory utilization
```

```text
Pod scheduling latency
```

```text
Node startup time
```

```text
Scale-up frequency
```

```text
Scale-down frequency
```

---

# Autoscaling Feedback Loop

A complete system can be visualized as:

```text
              Workload Demand
                     │
                     ▼
                    HPA
                     │
                     ▼
                Pod Count
                     │
                     ▼
                 Scheduler
                     │
                     ▼
              Cluster Capacity
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
           Enough         Not Enough
           Capacity        Capacity
              │             │
              │             ▼
              │       Cluster Autoscaler
              │             │
              │             ▼
              │          More Nodes
              │             │
              └──────┬──────┘
                     ▼
                 Scheduler
                     │
                     ▼
                    Pods
```

---

# Best Practices

### 1. Set Realistic Min/Max Node Counts

Do not make maximum capacity arbitrarily small or large.

---

### 2. Use Accurate Resource Requests

Requests influence scheduling and capacity planning.

---

### 3. Combine HPA and Cluster Autoscaler Carefully

Use:

```text
HPA → Pod scaling
CA → Node scaling
```

---

### 4. Test Scale-Up

Verify that:

```text
Pending Pods
```

actually result in:

```text
New Nodes
```

when appropriate.

---

### 5. Test Scale-Down

Verify that workloads can safely move between Nodes.

---

### 6. Use PDBs Carefully

Protect availability without completely blocking Node maintenance.

---

### 7. Design Node Groups Around Workloads

Use specialized pools when necessary:

```text
GPU
Memory
Compute
General
```

---

### 8. Use Labels and Taints Intentionally

Ensure specialized workloads reach appropriate Nodes.

---

### 9. Monitor Node Provisioning Time

Autoscaling is only as effective as the time required to bring capacity online.

---

### 10. Keep Spare Capacity for Critical Workloads

For latency-sensitive applications, some spare capacity may be preferable to waiting for new Nodes.

---

### 11. Consider Multiple Availability Zones

Avoid creating a single-zone capacity dependency for critical workloads.

---

### 12. Set a Maximum Capacity

Protect against:

```text
Unexpected Cost
Runaway Scaling
Application Bugs
Traffic Attacks
```

---

# Quick Revision

## Cluster Autoscaler

```text
Automatically changes Node count
```

---

## Scale Up

```text
Pending Pods
    ↓
More Nodes
```

---

## Scale Down

```text
Unused/Underutilized Capacity
    ↓
Remove Nodes
```

---

## HPA

```text
Pod count
```

---

## VPA

```text
Pod resources
```

---

## Cluster Autoscaler

```text
Node count
```

---

## Node Group

```text
Collection of similar Nodes
```

---

## min

```text
Minimum Node capacity
```

---

## max

```text
Maximum Node capacity
```

---

## PDB

```text
Controls voluntary disruption
```

---

## Requests

```text
Important for scheduling and capacity planning
```

---

# Essential kubectl Commands

List Nodes:

```bash
kubectl get nodes
```

Watch Nodes:

```bash
kubectl get nodes -w
```

Describe Node:

```bash
kubectl describe node <node-name>
```

View Pod status:

```bash
kubectl get pods
```

Describe Pending Pod:

```bash
kubectl describe pod <pod-name>
```

View Node resource usage:

```bash
kubectl top nodes
```

View Pod resource usage:

```bash
kubectl top pods
```

List PDBs:

```bash
kubectl get pdb
```

Describe PDB:

```bash
kubectl describe pdb <pdb-name>
```

View scheduling constraints:

```bash
kubectl get pod <pod-name> -o yaml
```

Check events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Check autoscaler logs:

```bash
kubectl logs -n kube-system deployment/cluster-autoscaler
```

The exact autoscaler resource name and namespace may differ by installation.

---

# Interview Questions

## Basic

- What is Cluster Autoscaler?
- Why do we need Cluster Autoscaler?
- What is the difference between HPA and Cluster Autoscaler?
- What is a Node Group?
- What are minimum and maximum Node counts?
- What causes Cluster Autoscaler to scale up?
- What causes Cluster Autoscaler to scale down?

---

## Intermediate

- How does Cluster Autoscaler detect that more Nodes are needed?
- What is an unschedulable Pod?
- What happens when HPA creates more Pods than the cluster can accommodate?
- How does Cluster Autoscaler interact with the Scheduler?
- What is Node draining?
- What is Pod eviction?
- How does a PodDisruptionBudget affect scale-down?
- Why might a Node not be removable?
- What are Node affinity and taints relevant to autoscaling?

---

## Advanced

- Explain the complete Cluster Autoscaler scale-up flow.
- Explain the complete scale-down flow.
- How does Cluster Autoscaler decide which Node Group to scale?
- What are expander strategies?
- Explain `least-waste`.
- Why can a Pending Pod fail to trigger useful scale-up?
- How does Cluster Autoscaler interact with HPA?
- How does Cluster Autoscaler interact with VPA?
- How can inaccurate resource requests cause unnecessary Node scaling?
- How would you troubleshoot Pods remaining Pending after scale-up?
- Why might Cluster Autoscaler refuse to remove an underutilized Node?
- How do PDBs affect Node scale-down?
- How do DaemonSets affect scale-down?
- How does local storage affect Node removal?
- How would you design Cluster Autoscaler for a multi-zone production cluster?
- How would you control runaway infrastructure costs?
- How would you design multiple Node Groups for different workloads?
- What happens when Cluster Autoscaler reaches `maxNodes`?
- How does Node startup time affect autoscaling?
- How would you combine HPA, VPA, and Cluster Autoscaler?

---

# Production Scenario

Suppose a production API normally runs:

```text
5 Pods
```

on:

```text
3 Nodes
```

Traffic suddenly increases.

HPA observes:

```text
CPU = 90%
Target = 65%
```

HPA increases:

```text
5 Pods
 ↓
10 Pods
```

The Scheduler attempts placement.

Suppose:

```text
7 Pods → Running
3 Pods → Pending
```

The Pending Pods require:

```text
CPU = 2 each
```

but existing Nodes cannot accommodate them.

Cluster Autoscaler detects:

```text
Unschedulable Pods
```

and determines that an eligible Node Group can satisfy the requirements.

It scales:

```text
3 Nodes
 ↓
5 Nodes
```

New Nodes become Ready.

The Scheduler then places the Pending Pods:

```text
Pending
 ↓
Running
```

The final architecture becomes:

```text
Traffic
   ↓
HPA
   ↓
10 Pods
   ↓
Scheduler
   ↓
5 Nodes
```

---

# Scale-Down Scenario

Later:

```text
Traffic decreases
```

HPA reduces:

```text
10 Pods
 ↓
4 Pods
```

Now the cluster has:

```text
5 Nodes
```

but only:

```text
4 Pods
```

are required.

Cluster Autoscaler evaluates Node utilization and scheduling constraints.

Suppose:

```text
Node 5
```

is removable.

It verifies:

```text
Pods can move
PDB allows eviction
Affinity allows relocation
Capacity exists elsewhere
No blocking constraints
```

Then:

```text
Node 5
 ↓
Pods Evicted
 ↓
Pods Rescheduled
 ↓
Node Removed
```

Cluster becomes:

```text
4 Nodes
```

---

# Production Autoscaling Model

A mature Kubernetes environment can use:

```text
                    Application Demand
                           │
                           ▼
                          HPA
                           │
                           ▼
                    Pod Replica Count
                           │
                           ▼
                       Scheduler
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
          Existing Capacity      Insufficient
                │                 Capacity
                │                     │
                │                     ▼
                │            Cluster Autoscaler
                │                     │
                │                     ▼
                │                 Node Group
                │                     │
                │                     ▼
                │                 New Nodes
                │                     │
                └──────────┬──────────┘
                           ▼
                       Scheduler
                           │
                           ▼
                          Pods
```

VPA can be added:

```text
VPA
 ↓
Right-size Pod Requests
 ↓
Scheduler
 ↓
Potential Capacity Increase
 ↓
Cluster Autoscaler
```

---

# Recommended Practice

1. Understand the difference between HPA, VPA, and Cluster Autoscaler.
2. Inspect Node capacity and allocatable resources.
3. Create intentionally Pending Pods in a disposable cluster.
4. Study the Scheduler events.
5. Install Cluster Autoscaler in a supported test environment.
6. Configure minimum Node capacity.
7. Configure maximum Node capacity.
8. Test scale-up.
9. Observe Node provisioning.
10. Observe Pods becoming schedulable.
11. Reduce workload demand.
12. Test scale-down.
13. Configure a PodDisruptionBudget.
14. Observe how PDB affects Node eviction.
15. Test Node affinity.
16. Test taints and tolerations.
17. Test multiple Node Groups.
18. Study specialized GPU or memory-optimized Node Groups.
19. Combine HPA with Cluster Autoscaler.
20. Study VPA + Cluster Autoscaler interaction.
21. Monitor autoscaler logs.
22. Analyze Node provisioning time.
23. Calculate the cost impact of scaling.
24. Design a multi-zone production autoscaling architecture.

---

# References

## Official Kubernetes Documentation

- Cluster Autoscaling
- Node Autoscaling
- Kubernetes Scheduler
- Resource Management for Pods and Containers
- Horizontal Pod Autoscaling
- Vertical Pod Autoscaling
- Pod Disruption Budgets
- Assign Pods to Nodes
- Taints and Tolerations
- Node Affinity
- Node Labels
- Topology Spread Constraints

---

## Kubernetes Ecosystem

- Cluster Autoscaler
- Kubernetes SIG Autoscaling
- Kubernetes SIG Scheduling
- Kubernetes SIG Node

---

## Cloud Platforms

Cluster Autoscaler implementations are commonly integrated with managed Kubernetes platforms and their Node Group/Node Pool systems.

Examples include:

```text
Amazon EKS
Microsoft AKS
Google Kubernetes Engine
```

Always consult the documentation for the specific Kubernetes distribution and cloud provider because installation, configuration, supported strategies, and Node Group behavior vary.

---

# Chapter Summary

Cluster Autoscaler provides **Node-level elasticity** for Kubernetes.

The fundamental relationship is:

```text
HPA
 ↓
Pod Count
```

```text
VPA
 ↓
Pod Resources
```

```text
Cluster Autoscaler
 ↓
Node Count
```

The scale-up flow is:

```text
Pod Demand
    ↓
Scheduler
    ↓
Pod Cannot Be Scheduled
    ↓
Pending Pod
    ↓
Cluster Autoscaler
    ↓
Node Group Expansion
    ↓
New Node
    ↓
Node Ready
    ↓
Scheduler
    ↓
Pod Running
```

The scale-down flow is:

```text
Lower Demand
    ↓
Underutilized Node
    ↓
Check Scheduling Constraints
    ↓
Check Pod Disruption
    ↓
Evict / Reschedule Pods
    ↓
Remove Node
```

Cluster Autoscaler must consider much more than CPU utilization.

Important factors include:

```text
Resource Requests
Node Affinity
Pod Affinity
Taints
Tolerations
PodDisruptionBudgets
DaemonSets
Local Storage
Topology Constraints
Node Group Capacity
Minimum Nodes
Maximum Nodes
```

A Pod remaining Pending does not automatically mean:

```text
Add any Node
```

The new Node must be capable of satisfying the Pod's requirements.

For example:

```text
Pod requires GPU
```

requires:

```text
GPU-capable Node
```

not merely:

```text
Another generic Node
```

Similarly:

```text
Pod requires:

nodeSelector:
  workload: gpu
```

requires a Node with the appropriate label.

The most important production relationship is:

```text
                    HPA
                     │
                     ▼
                More Pods
                     │
                     ▼
                 Scheduler
                     │
             ┌───────┴───────┐
             │               │
             ▼               ▼
          Enough          Not Enough
          Capacity         Capacity
             │               │
             │               ▼
             │        Cluster Autoscaler
             │               │
             │               ▼
             │           More Nodes
             │               │
             └───────┬───────┘
                     ▼
                 Scheduler
```

The overall goal is:

```text
Enough Capacity
+
Good Performance
+
High Availability
+
Controlled Cost
```

rather than simply maximizing the number of Nodes.

A production-ready autoscaling strategy should therefore combine:

```text
Accurate Resource Requests
        +
HPA
        +
VPA where appropriate
        +
Cluster Autoscaler
        +
Multiple Node Groups
        +
PodDisruptionBudgets
        +
Topology Awareness
        +
Monitoring
```

The key principle is:

> **HPA scales workloads, VPA right-sizes workloads, and Cluster Autoscaler provides the infrastructure capacity required to run them.**

This completes **Module 6 — Kubernetes Scheduling**.

---

# Module 6 Complete

```text
Chapter 36 – Scheduler
Chapter 37 – Node Selectors
Chapter 38 – Node Affinity
Chapter 39 – Pod Affinity & Anti-Affinity
Chapter 40 – Taints & Tolerations
Chapter 41 – Priority Classes
Chapter 42 – Resource Requests & Limits
Chapter 43 – Horizontal Pod Autoscaler (HPA)
Chapter 44 – Vertical Pod Autoscaler (VPA)
Chapter 45 – Cluster Autoscaler
```

---

## Next Module

# Module 7 — Kubernetes Security

### Chapter 46 – Kubernetes Security Fundamentals

Topics will include:

- Kubernetes Security Model
- Defense in Depth
- Control Plane Security
- Node Security
- Pod Security
- Container Security
- API Server Security
- Authentication
- Authorization
- RBAC
- Service Accounts
- Secrets
- Network Policies
- Pod Security Standards
- Admission Control
- Image Security
- Runtime Security
- Supply Chain Security
- Encryption
- Audit Logging
- Security Contexts
- Linux Capabilities
- Privileged Containers
- Security Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---