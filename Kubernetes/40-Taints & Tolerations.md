# Chapter 40 – Taints & Tolerations

## Overview

In the previous chapters, we learned how Kubernetes can influence **where Pods are scheduled**.

```text
Node Selector
    ↓
Simple Node selection

Node Affinity
    ↓
Advanced Node selection

Pod Affinity
    ↓
Place Pods near other Pods

Pod Anti-Affinity
    ↓
Separate Pods from other Pods
```

These mechanisms primarily answer:

> **Where should a Pod run?**

But Kubernetes also needs a mechanism to answer:

> **Which Pods should be allowed to run on this Node?**

This is where **Taints and Tolerations** are used.

A **Taint** is applied to a Node and tells Kubernetes:

```text
"Do not schedule certain Pods here unless they tolerate this taint."
```

A **Toleration** is applied to a Pod and tells Kubernetes:

```text
"This Pod is allowed to run on Nodes with this taint."
```

The basic relationship is:

```text
Node

↓

Taint

↓

Repels Pods
```

and:

```text
Pod

↓

Toleration

↓

Allows the Pod to tolerate the taint
```

> **Taints are applied to Nodes; tolerations are applied to Pods.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Taints are
- What Tolerations are
- Why Taints and Tolerations are needed
- Taint structure
- Taint effects
- `NoSchedule`
- `PreferNoSchedule`
- `NoExecute`
- Toleration operators
- `Equal`
- `Exists`
- `tolerationSeconds`
- Adding Taints
- Removing Taints
- Dedicated Nodes
- GPU Nodes
- Control-Plane Nodes
- Workload isolation
- Taints vs Node Affinity
- Taints and Scheduler behavior
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices

---

# Why Do We Need Taints?

Suppose a Kubernetes cluster contains:

```text
Node 1
General workloads

Node 2
GPU hardware

Node 3
Database hardware
```

We do not want every ordinary Pod to accidentally run on:

```text
GPU Node
```

because GPU Nodes may be expensive.

Similarly, we may want a dedicated database Node to run only database workloads.

Taints solve this problem.

---

# Basic Concept

Apply a taint:

```text
Node

↓

dedicated=database:NoSchedule
```

Now a Pod without the appropriate toleration cannot normally be scheduled there.

A database Pod can have:

```yaml
tolerations:

- key: dedicated

  operator: Equal

  value: database

  effect: NoSchedule
```

Now it can tolerate the taint.

---

# High-Level Architecture

```text
                  Kubernetes Scheduler

                          │

              ┌───────────┴───────────┐

              ▼                       ▼

            Node                    Pod

              │                       │

            Taint                 Toleration

              │                       │

              └───────────┬───────────┘

                          ▼

                   Scheduling Decision
```

---

# Taint Structure

A taint consists of:

```text
key
value
effect
```

Example:

```text
dedicated=database:NoSchedule
```

Breakdown:

```text
key
 ↓
dedicated
```

```text
value
 ↓
database
```

```text
effect
 ↓
NoSchedule
```

---

# Adding a Taint

Use:

```bash
kubectl taint nodes <node-name> dedicated=database:NoSchedule
```

Example:

```bash
kubectl taint nodes worker-01 dedicated=database:NoSchedule
```

---

# Viewing Node Taints

Run:

```bash
kubectl describe node <node-name>
```

Look for:

```text
Taints:
```

You can also inspect the Node directly:

```bash
kubectl get node <node-name> -o yaml
```

Look under:

```text
spec.taints
```

---

# Three Taint Effects

Kubernetes supports three main taint effects:

```text
NoSchedule
```

```text
PreferNoSchedule
```

```text
NoExecute
```

These effects behave differently.

---

# NoSchedule

```text
NoSchedule
```

means:

> New Pods that do not tolerate the taint should not be scheduled onto the Node.

Example:

```text
Node:

dedicated=database:NoSchedule
```

Pod:

```text
No matching toleration
```

Result:

```text
Pod

↓

Cannot be scheduled there
```

---

# Important NoSchedule Behavior

Existing Pods are not automatically removed merely because the taint is added.

The primary effect is on **new scheduling decisions**.

---

# PreferNoSchedule

```text
PreferNoSchedule
```

is a softer rule.

It means:

> Kubernetes should try to avoid scheduling Pods that do not tolerate the taint, but the constraint is not absolute.

Conceptually:

```text
NoSchedule

↓

Hard avoidance
```

```text
PreferNoSchedule

↓

Soft avoidance
```

---

# NoExecute

`NoExecute` affects both:

```text
New Pods
```

and:

```text
Existing Pods
```

A Pod without a matching toleration can be evicted from the Node.

Example:

```text
Node

↓

maintenance=true:NoExecute
```

Existing non-tolerating Pods may be removed from the Node.

---

# Comparing Taint Effects

| Effect | New Pods | Existing Pods |
|---|---|---|
| `NoSchedule` | Prevents scheduling | Existing Pods remain |
| `PreferNoSchedule` | Tries to avoid | Existing Pods remain |
| `NoExecute` | Prevents scheduling | Can evict non-tolerating Pods |

---

# Tolerations

A toleration allows a Pod to tolerate a matching Node taint.

Example:

```yaml
tolerations:

- key: dedicated

  operator: Equal

  value: database

  effect: NoSchedule
```

Node:

```text
dedicated=database:NoSchedule
```

Pod:

```text
Matching toleration
```

Result:

```text
Pod can be considered for that Node
```

---

# Important Concept

A toleration does **not** mean:

```text
"Schedule this Pod onto that Node."
```

It means:

```text
"This Pod is not rejected merely because of this matching taint."
```

The Scheduler may still choose another Node.

---

# Taint + Toleration

The complete relationship is:

```text
Node

dedicated=database:NoSchedule

        │
        ▼
     Taint

        │
        ▼

Pod without toleration
        │
        ▼
     Rejected

Pod with matching toleration
        │
        ▼
     Allowed to be considered
```

---

# Toleration Operator

Tolerations support:

```text
Equal
```

and:

```text
Exists
```

---

# Equal Operator

Example:

```yaml
tolerations:

- key: dedicated

  operator: Equal

  value: database

  effect: NoSchedule
```

This matches:

```text
dedicated=database:NoSchedule
```

---

# Exists Operator

Example:

```yaml
tolerations:

- key: dedicated

  operator: Exists

  effect: NoSchedule
```

This tolerates the taint based on the key regardless of the taint value.

For example:

```text
dedicated=database:NoSchedule
```

and:

```text
dedicated=gpu:NoSchedule
```

can both match the same key-based toleration, assuming the effect also matches.

---

# Empty Key with Exists

A toleration using:

```yaml
operator: Exists
```

with an empty key and an appropriate effect can be used to tolerate all taints of that effect.

Example:

```yaml
tolerations:

- operator: Exists

  effect: NoSchedule
```

This is powerful and should be used carefully.

---

# Empty Effect

If the toleration does not specify an effect, it can match taints with the same key across taint effects, subject to the toleration matching rules.

For production workloads, explicitly specifying the intended effect usually makes the configuration easier to understand.

---

# TolerationSeconds

`NoExecute` tolerations can specify:

```yaml
tolerationSeconds:
```

This controls how long a Pod can remain on a Node after a matching `NoExecute` taint is applied.

Example:

```yaml
tolerations:

- key: maintenance

  operator: Equal

  value: planned

  effect: NoExecute

  tolerationSeconds: 300
```

Meaning:

```text
Taint applied

↓

Pod tolerates it for up to 300 seconds

↓

After that

↓

Pod may be evicted
```

---

# Why TolerationSeconds Is Useful

It can provide temporary tolerance during:

- Node maintenance
- Network disruptions
- Temporary infrastructure conditions
- Graceful failover

---

# Example

Node:

```text
maintenance=true:NoExecute
```

Pod:

```yaml
tolerationSeconds: 600
```

Result:

```text
0 seconds
    ↓
Pod remains

600 seconds
    ↓
Pod may be evicted
```

---

# Node Taint Example

Apply:

```bash
kubectl taint nodes worker-01 dedicated=database:NoSchedule
```

Now:

```text
worker-01

↓

dedicated=database:NoSchedule
```

---

# Pod Without Toleration

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: normal-pod

spec:

  containers:

  - name: nginx

    image: nginx
```

This Pod does not tolerate:

```text
dedicated=database
```

Therefore it cannot normally be scheduled onto that Node.

---

# Pod With Toleration

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: database-pod

spec:

  tolerations:

  - key: dedicated

    operator: Equal

    value: database

    effect: NoSchedule

  containers:

  - name: postgres

    image: postgres
```

Now the Pod can be considered for the tainted Node.

---

# Important: Toleration Does Not Guarantee Placement

Suppose:

```text
Node 1
dedicated=database:NoSchedule
```

and:

```text
Node 2
No taint
```

Pod tolerates:

```text
dedicated=database
```

The Scheduler may still select:

```text
Node 2
```

because the Pod is allowed on both.

If you want the Pod to actually target the dedicated Nodes, combine:

```text
Toleration

+

Node Selector / Node Affinity
```

---

# Dedicated Node Pattern

A common production design is:

```text
Node:

dedicated=database:NoSchedule
```

and:

```text
Pod:

tolerates database taint
```

plus:

```text
nodeSelector:

dedicated=database
```

Architecture:

```text
Database Pod

├── Toleration
│
│   Can enter database Node
│
└── Node Selector
    │
    └── Select database Node
```

This provides:

```text
Permission

+

Selection
```

---

# Taints vs Node Affinity

These mechanisms solve different problems.

## Taints

Applied to:

```text
Node
```

Purpose:

```text
Repel unwanted Pods
```

---

## Node Affinity

Applied to:

```text
Pod
```

Purpose:

```text
Select preferred/required Nodes
```

---

# Comparison

| Feature | Taints | Node Affinity |
|---|---|---|
| Applied to | Node | Pod |
| Primary behavior | Repel | Attract/select |
| Requires Pod configuration | Only for tolerating | Yes |
| Main use | Node isolation | Placement |
| Can prevent unwanted workloads | Yes | Not by itself |
| Can select Nodes | No | Yes |

---

# Taints + Node Affinity

For dedicated workloads, use both.

Example:

```text
Node:

dedicated=database:NoSchedule
```

Pod:

```text
Toleration

+

Node Affinity
```

Result:

```text
Only database Pods

↓

Can tolerate database Node

↓

Select database Node
```

This is a powerful production pattern.

---

# Control-Plane Nodes

Kubernetes control-plane Nodes are commonly protected with taints so ordinary application Pods are not scheduled there.

Inspect:

```bash
kubectl describe node <control-plane-node>
```

Look for:

```text
Taints:
```

Typical environments use a control-plane-related taint.

The exact taint key and configuration can vary by Kubernetes distribution and cluster setup.

---

# GPU Nodes

GPU Nodes are expensive and specialized.

A cluster might use:

```text
accelerator=nvidia:NoSchedule
```

Then only GPU workloads with the appropriate toleration can be considered.

In addition, GPU workloads normally request the actual GPU resource exposed by the relevant device plugin.

Conceptually:

```text
GPU Node

├── Taint
│
├── GPU Resource
│
└── Specialized Hardware
```

GPU Pod:

```text
Toleration

+

GPU Resource Request
```

---

# Maintenance Scenario

Suppose a Node needs maintenance.

You may first use:

```bash
kubectl cordon <node-name>
```

This prevents new Pods from being scheduled there.

Then:

```bash
kubectl drain <node-name>
```

to safely evict workloads according to Kubernetes disruption rules.

Taints can also be used as part of operational workflows, but **cordon/drain** are separate mechanisms and should not be confused with taint behavior.

---

# Taint vs Cordon

These are different.

## Cordon

```text
Node

↓

Unschedulable
```

It prevents new Pods from being scheduled onto the Node.

---

## Taint

```text
Node

↓

Repels Pods without matching tolerations
```

A taint can selectively repel Pods.

---

# NoExecute and Node Conditions

Kubernetes can use taints to react to Node conditions.

For example:

```text
node.kubernetes.io/not-ready
```

or:

```text
node.kubernetes.io/unreachable
```

These are associated with Node health and can trigger eviction behavior.

Pods may have tolerations for such taints.

---

# Example

```yaml
tolerations:

- key: node.kubernetes.io/not-ready

  operator: Exists

  effect: NoExecute

  tolerationSeconds: 300
```

This allows a Pod to tolerate a NotReady condition for a limited time.

---

# Scheduler Workflow with Taints

```text
Pod Created

↓

Scheduler

↓

Inspect Node Taints

↓

Check Pod Tolerations

↓

Taint Tolerated?

├── No → Node rejected
│
└── Yes → Node remains eligible

↓

Continue Scheduling
```

---

# Multiple Taints

A Node can have multiple taints.

Example:

```text
dedicated=database:NoSchedule
```

and:

```text
maintenance=false:NoExecute
```

A Pod must satisfy the relevant taint requirements to avoid being rejected or evicted.

---

# Example

Node:

```text
dedicated=database:NoSchedule
maintenance=true:NoExecute
```

Pod needs:

```text
Toleration 1
```

for:

```text
dedicated=database
```

and:

```text
Toleration 2
```

for:

```text
maintenance=true
```

---

# Removing a Taint

Use:

```bash
kubectl taint nodes <node-name> dedicated=database:NoSchedule-
```

The trailing:

```text
-
```

removes the taint.

Verify:

```bash
kubectl describe node <node-name>
```

---

# View Taints

```bash
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
```

---

# Hands-on Lab 1 – Add a Taint

Choose a worker Node:

```bash
kubectl taint nodes <node-name> dedicated=database:NoSchedule
```

Verify:

```bash
kubectl describe node <node-name>
```

---

# Hands-on Lab 2 – Deploy a Pod Without Toleration

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: taint-test

spec:

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f taint-test.yaml
```

Observe:

```bash
kubectl get pod taint-test
```

If the cluster has no other suitable Nodes, the Pod may remain:

```text
Pending
```

Inspect:

```bash
kubectl describe pod taint-test
```

---

# Hands-on Lab 3 – Add a Toleration

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: toleration-test

spec:

  tolerations:

  - key: dedicated

    operator: Equal

    value: database

    effect: NoSchedule

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f toleration-test.yaml
```

Observe:

```bash
kubectl get pod toleration-test -o wide
```

---

# Hands-on Lab 4 – Toleration Does Not Select

Create:

```text
Node 1
dedicated=database:NoSchedule
```

and:

```text
Node 2
No taint
```

Deploy a Pod with the database toleration.

Observe that Kubernetes may choose Node 2.

This demonstrates:

```text
Toleration

≠

Node Selection
```

---

# Hands-on Lab 5 – Toleration + Node Selector

Use:

```yaml
tolerations:

- key: dedicated

  operator: Equal

  value: database

  effect: NoSchedule

nodeSelector:

  dedicated: database
```

Now the Pod:

```text
Tolerates database Node

+

Selects database Node
```

---

# Hands-on Lab 6 – Test NoExecute

Apply:

```bash
kubectl taint nodes <node-name> maintenance=true:NoExecute
```

Observe the behavior of existing Pods.

Then remove the taint:

```bash
kubectl taint nodes <node-name> maintenance=true:NoExecute-
```

Only perform this test on a disposable lab cluster.

---

# Hands-on Lab 7 – Test TolerationSeconds

Create a Pod with:

```yaml
tolerations:

- key: maintenance

  operator: Equal

  value: true

  effect: NoExecute

  tolerationSeconds: 60
```

Apply a matching `NoExecute` taint.

Observe that the Pod can tolerate the taint temporarily.

---

# Hands-on Lab 8 – Multiple Taints

Add:

```text
dedicated=database:NoSchedule
```

and:

```text
environment=production:NoSchedule
```

Create a Pod that tolerates only one of them.

Observe the scheduling behavior.

Then add the second toleration.

---

# Troubleshooting

## Check Node Taints

```bash
kubectl describe node <node-name>
```

Look for:

```text
Taints:
```

---

## Check Pod Tolerations

```bash
kubectl get pod <pod-name> -o yaml
```

Look under:

```text
spec.tolerations
```

---

## Check Scheduling Events

```bash
kubectl describe pod <pod-name>
```

Look for:

```text
FailedScheduling
```

---

# Example Scheduling Error

You may encounter messages indicating:

```text
node(s) had untolerated taint
```

This means:

```text
Node

↓

Has Taint

↓

Pod

↓

Does not have matching Toleration
```

---

# Common Mistakes

## 1. Thinking a Toleration Forces Scheduling

Incorrect:

```text
Toleration

↓

Pod must run on tainted Node
```

Correct:

```text
Toleration

↓

Pod is allowed to tolerate the taint
```

The Scheduler can still select another suitable Node.

---

## 2. Forgetting the Taint Effect

These are different:

```text
NoSchedule
```

```text
NoExecute
```

```text
PreferNoSchedule
```

The toleration must match the intended effect where applicable.

---

## 3. Using NoExecute Without Understanding Eviction

`NoExecute` can affect existing Pods.

Use it carefully in production.

---

## 4. Forgetting TolerationSeconds

For temporary tolerance:

```yaml
tolerationSeconds: 300
```

can be useful.

Without a time limit, the toleration can remain effective indefinitely, subject to the rest of the configuration.

---

## 5. Assuming Taints Replace Node Affinity

Taints repel unwanted workloads.

Node Affinity selects desired Nodes.

They often work together.

---

## 6. Forgetting Other Taints

A Node may have multiple taints.

Tolerating one does not necessarily tolerate all others.

---

## 7. Accidentally Tainting Production Nodes

Always verify the target Node before running:

```bash
kubectl taint nodes ...
```

---

# Taints vs Tolerations vs Affinity

| Mechanism | Applied To | Purpose |
|---|---|---|
| Taint | Node | Repel Pods |
| Toleration | Pod | Allow Pod to tolerate taint |
| Node Selector | Pod | Select Nodes |
| Node Affinity | Pod | Advanced Node selection |
| Pod Affinity | Pod | Co-locate with Pods |
| Pod Anti-Affinity | Pod | Separate from Pods |

---

# Quick Revision

## Taint

```text
Node

↓

Repels Pods
```

---

## Toleration

```text
Pod

↓

Allows it to tolerate matching taint
```

---

## Effects

```text
NoSchedule
    ↓
Do not schedule non-tolerating Pods
```

```text
PreferNoSchedule
    ↓
Try to avoid
```

```text
NoExecute
    ↓
Do not schedule + can evict
```

---

# Essential Commands

Add taint:

```bash
kubectl taint nodes <node> key=value:NoSchedule
```

Remove taint:

```bash
kubectl taint nodes <node> key=value:NoSchedule-
```

View Node:

```bash
kubectl describe node <node>
```

View all taints:

```bash
kubectl get nodes \
-o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
```

View Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

View scheduling events:

```bash
kubectl describe pod <pod>
```

---

# Interview Questions

## Basic

- What is a taint?
- What is a toleration?
- Why are taints and tolerations used?
- Where is a taint configured?
- Where is a toleration configured?
- What are the three taint effects?

---

## Intermediate

- Explain `NoSchedule`.
- Explain `PreferNoSchedule`.
- Explain `NoExecute`.
- What is the difference between `Equal` and `Exists`?
- What is `tolerationSeconds`?
- Does a toleration force a Pod onto a Node?

---

## Advanced

- Explain the complete taint and toleration scheduling workflow.
- Compare taints with Node Affinity.
- Why would you use taints and Node Affinity together?
- How would you create dedicated database Nodes?
- How would you isolate GPU Nodes?
- Explain how `NoExecute` affects existing Pods.
- How would you troubleshoot `node(s) had untolerated taint`?
- How do multiple taints affect scheduling?
- How would you design maintenance behavior using taints and tolerations?
- Explain the difference between cordoning a Node and tainting a Node.

---

# Production Design Example

Consider a production cluster:

```text
                    Kubernetes Cluster

                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼

   General Nodes      Database Nodes     GPU Nodes

                       │                 │
                       ▼                 ▼

              dedicated=database    accelerator=gpu

              :NoSchedule           :NoSchedule
```

Database Pod:

```text
Toleration

+

Node Affinity
```

GPU Pod:

```text
Toleration

+

GPU Resource Request

+

Optional Node Affinity
```

General workloads:

```text
No toleration

↓

Cannot use dedicated Nodes
```

This creates workload isolation.

---

# Best Practices

### 1. Use Taints for Dedicated Nodes

Good candidates:

```text
Database Nodes
GPU Nodes
Security workloads
Infrastructure workloads
Specialized hardware
```

---

### 2. Combine Taints with Node Affinity

Use:

```text
Toleration

+

Node Affinity
```

when a workload should both:

```text
Be allowed onto

+

Prefer/require
```

a specialized Node.

---

### 3. Use NoExecute Carefully

It can evict existing workloads.

Always understand the impact before applying it.

---

### 4. Prefer Explicit Tolerations

Avoid broad tolerations such as:

```yaml
operator: Exists
```

unless the workload genuinely needs to tolerate a broad class of taints.

---

### 5. Use TolerationSeconds for Temporary Conditions

Useful for controlled grace periods.

---

### 6. Document Dedicated Node Policies

For example:

```text
dedicated=database
dedicated=gpu
dedicated=security
```

Keep naming consistent across the cluster.

---

### 7. Test Before Production

Test:

```text
NoSchedule
PreferNoSchedule
NoExecute
```

in a lab environment before using them in critical clusters.

---

# References

## Official Kubernetes Documentation

- Taints and Tolerations
- Assigning Pods to Nodes
- Node Affinity
- Node Management
- Pod Lifecycle
- Node Pressure Eviction

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Scheduling Framework
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. Create a dedicated lab Node.
2. Apply a `NoSchedule` taint.
3. Deploy a Pod without a toleration.
4. Inspect the `FailedScheduling` event.
5. Add a matching toleration.
6. Verify that the Pod can now be considered for the Node.
7. Demonstrate that toleration alone does not force placement.
8. Combine toleration with Node Affinity.
9. Test `PreferNoSchedule`.
10. Test `NoExecute` on a disposable cluster.
11. Experiment with `tolerationSeconds`.
12. Create a realistic database or GPU Node isolation policy.
13. Practice removing taints safely.

---

# Chapter Summary

```text
                     Node

                       │
                       ▼
                     Taint

                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
       No Toleration       Matching
              │            Toleration
              ▼                 │
           Rejected             ▼
                            Allowed
```

Taints and tolerations provide a powerful mechanism for **Node-level workload isolation**.

The most important relationship is:

```text
Taint
    ↓
Applied to Node

Toleration
    ↓
Applied to Pod
```

The three major effects are:

```text
NoSchedule
    ↓
Reject new non-tolerating Pods

PreferNoSchedule
    ↓
Prefer not to schedule them

NoExecute
    ↓
Reject new Pods
+
Can evict existing non-tolerating Pods
```

Remember:

```text
Toleration ≠ Node Selection
```

A toleration only makes a Pod **eligible to tolerate** a matching taint. It does not force the Pod onto that Node.

For dedicated workloads, the recommended pattern is often:

```text
                Dedicated Node

                     │
                     ▼
                   Taint
                     │
          dedicated=database
                     │
                     ▼
                NoSchedule

                     ▲
                     │
              Toleration
                     │
                 Database
                   Pod

                     +

               Node Affinity
                     │
                     ▼
             Select Database
                 Nodes
```

This combination provides both:

```text
Isolation

+

Placement Control
```

which is particularly useful for production databases, GPU workloads, security workloads, and other specialized infrastructure.

---

## Next Chapter

# Chapter 41 – Priority Classes

Topics will include:

- What is Pod Priority?
- Why Priority Classes are needed
- `PriorityClass`
- Priority values
- Default PriorityClass
- `globalDefault`
- `preemptionPolicy`
- Pod preemption
- Scheduler behavior
- High-priority workloads
- Low-priority workloads
- Non-preempting PriorityClasses
- Resource pressure
- Priority vs QoS
- Priority vs Requests and Limits
- Real-World Use Cases
- Hands-on Labs
- Common Mistakes
- Troubleshooting
- Quick Revision
- Interview Questions
- References

---