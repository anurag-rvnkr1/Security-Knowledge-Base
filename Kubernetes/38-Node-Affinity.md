# Chapter 38 – Node Affinity

## Overview

In the previous chapter, we learned about **Node Selectors**.

A `nodeSelector` is useful when a Pod needs a simple label match:

```yaml
nodeSelector:
  disk: ssd
```

However, real production environments often require more complex scheduling rules.

For example:

- Run on SSD **or** NVMe Nodes.
- Prefer high-memory Nodes.
- Avoid a particular hardware type.
- Run only on Nodes in specific zones.
- Prefer Nodes in the same region.
- Require one label but only prefer another.
- Use multiple logical conditions.

For these scenarios, Kubernetes provides **Node Affinity**.

> **Node Affinity allows Pods to express more sophisticated rules about which Nodes they can or should run on.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Node Affinity is
- Why Node Affinity is needed
- Node Affinity architecture
- Required vs preferred affinity
- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`
- Affinity operators
- `In`
- `NotIn`
- `Exists`
- `DoesNotExist`
- `Gt`
- `Lt`
- Multiple affinity rules
- OR and AND behavior
- Node Selector vs Node Affinity
- Real-world use cases
- Troubleshooting
- Hands-on Labs
- Best practices

---

# Why Do We Need Node Affinity?

Suppose a cluster contains:

```text
Node 1
disk=ssd

Node 2
disk=nvme

Node 3
disk=hdd
```

With `nodeSelector`:

```yaml
nodeSelector:

  disk: ssd
```

the Pod can only run on:

```text
Node 1
```

But suppose we want:

```text
SSD OR NVMe
```

A simple `nodeSelector` cannot express that OR requirement.

Node Affinity can:

```text
disk In [ssd, nvme]
```

Now:

```text
Node 1 → Match
Node 2 → Match
Node 3 → Reject
```

---

# What is Node Affinity?

Node Affinity is a Kubernetes scheduling mechanism that allows Pods to specify rules based on Node labels.

It provides:

- Required scheduling rules
- Preferred scheduling rules
- Multiple operators
- Logical expressions
- More flexible scheduling than `nodeSelector`

---

# High-Level Architecture

```text
                    Pod

                     │

                     ▼

                Node Affinity

                     │

                     ▼

                  Scheduler

                     │

          ┌──────────┼──────────┐

          ▼          ▼          ▼

       Node 1      Node 2      Node 3

       disk=ssd    disk=nvme   disk=hdd

          │           │           X

          └───── Candidates ──────┘

                     │

                     ▼

               Selected Node
```

---

# Node Affinity Structure

A typical Node Affinity configuration looks like:

```yaml
affinity:

  nodeAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

      nodeSelectorTerms:

      - matchExpressions:

        - key: disk

          operator: In

          values:

          - ssd

          - nvme
```

---

# Two Main Types

Node Affinity provides two primary scheduling behaviors:

```text
requiredDuringSchedulingIgnoredDuringExecution
```

and:

```text
preferredDuringSchedulingIgnoredDuringExecution
```

---

# Required Node Affinity

```yaml
requiredDuringSchedulingIgnoredDuringExecution:
```

means:

> The Pod **must** be scheduled on a Node satisfying the affinity rule.

If no Node matches:

```text
Pod

↓

Pending
```

---

# Preferred Node Affinity

```yaml
preferredDuringSchedulingIgnoredDuringExecution:
```

means:

> The Scheduler should prefer matching Nodes, but can use another suitable Node if necessary.

Example:

```text
Prefer SSD

↓

If unavailable

↓

Use another suitable Node
```

---

# Required vs Preferred

| Feature | Required | Preferred |
|---|---|---|
| Must match? | Yes | No |
| Scheduling failure if no match? | Yes | No |
| Acts as hard constraint | Yes | No |
| Acts as preference | No | Yes |
| Useful for | Mandatory requirements | Optimization |

---

# Meaning of IgnoredDuringExecution

The name is important.

Consider:

```text
requiredDuringSchedulingIgnoredDuringExecution
```

It means:

```text
During Scheduling

↓

Rule is enforced
```

But:

```text
After Pod is Running

↓

Changes to Node labels are not automatically used to evict the Pod
```

Therefore, the rule controls **scheduling**, not automatic eviction based solely on later label changes.

---

# Affinity Operators

Node Affinity supports several operators:

```text
In
```

```text
NotIn
```

```text
Exists
```

```text
DoesNotExist
```

```text
Gt
```

```text
Lt
```

---

# Operator: In

Matches when the label value is one of the specified values.

Example:

```yaml
operator: In

values:

- ssd
- nvme
```

Means:

```text
disk=ssd

OR

disk=nvme
```

---

# Example

Node:

```text
disk=ssd
```

Result:

```text
Match
```

Node:

```text
disk=nvme
```

Result:

```text
Match
```

Node:

```text
disk=hdd
```

Result:

```text
No Match
```

---

# Operator: NotIn

Matches when the label value is not one of the specified values.

Example:

```yaml
operator: NotIn

values:

- hdd
```

Means:

```text
disk != hdd
```

---

# Example

```text
disk=ssd

↓

Match
```

```text
disk=nvme

↓

Match
```

```text
disk=hdd

↓

Reject
```

---

# Operator: Exists

Checks whether a label key exists.

Example:

```yaml
key: gpu

operator: Exists
```

This means:

```text
gpu label exists
```

The actual value does not matter.

---

# Example

Node:

```text
gpu=nvidia
```

Matches.

Node:

```text
gpu=amd
```

Also matches.

Node:

```text
No gpu label
```

Does not match.

---

# Operator: DoesNotExist

Checks that a label key is absent.

Example:

```yaml
key: experimental

operator: DoesNotExist
```

Nodes with:

```text
experimental=true
```

do not match.

Nodes without the label can match.

---

# Operator: Gt

`Gt` means greater than.

Example:

```yaml
key: cpu-count

operator: Gt

values:

- "8"
```

Conceptually:

```text
cpu-count > 8
```

This operator is useful for supported numeric-style label comparisons.

---

# Operator: Lt

`Lt` means less than.

Example:

```yaml
key: cpu-count

operator: Lt

values:

- "16"
```

Conceptually:

```text
cpu-count < 16
```

---

# Basic Required Affinity Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: required-affinity

spec:

  affinity:

    nodeAffinity:

      requiredDuringSchedulingIgnoredDuringExecution:

        nodeSelectorTerms:

        - matchExpressions:

          - key: disk

            operator: In

            values:

            - ssd

  containers:

  - name: nginx

    image: nginx
```

This Pod requires:

```text
disk=ssd
```

---

# Multiple Values

Example:

```yaml
- key: disk

  operator: In

  values:

  - ssd

  - nvme
```

Meaning:

```text
disk=ssd

OR

disk=nvme
```

---

# Multiple matchExpressions

Example:

```yaml
nodeSelectorTerms:

- matchExpressions:

  - key: disk

    operator: In

    values:

    - ssd

  - key: environment

    operator: In

    values:

    - production
```

This means:

```text
disk=ssd

AND

environment=production
```

---

# AND Logic

Within the same `matchExpressions` list:

```text
Condition A

AND

Condition B
```

Example:

```text
disk=ssd

AND

environment=production
```

Both must be satisfied.

---

# OR Logic with nodeSelectorTerms

Multiple `nodeSelectorTerms` represent OR logic.

Example:

```yaml
nodeSelectorTerms:

- matchExpressions:

  - key: disk

    operator: In

    values:

    - ssd

- matchExpressions:

  - key: disk

    operator: In

    values:

    - nvme
```

Meaning:

```text
disk=ssd

OR

disk=nvme
```

---

# AND + OR Together

Consider:

```yaml
nodeSelectorTerms:

- matchExpressions:

  - key: disk

    operator: In

    values:

    - ssd

  - key: environment

    operator: In

    values:

    - production

- matchExpressions:

  - key: disk

    operator: In

    values:

    - nvme

  - key: environment

    operator: In

    values:

    - production
```

Meaning:

```text
(disk=ssd AND environment=production)

OR

(disk=nvme AND environment=production)
```

This is one of the major advantages over `nodeSelector`.

---

# Preferred Node Affinity

Example:

```yaml
affinity:

  nodeAffinity:

    preferredDuringSchedulingIgnoredDuringExecution:

    - weight: 80

      preference:

        matchExpressions:

        - key: disk

          operator: In

          values:

          - ssd
```

This means:

```text
Prefer SSD Nodes
```

but does not make SSD mandatory.

---

# Weight

Preferred rules support:

```yaml
weight: 80
```

The weight ranges from:

```text
1

to

100
```

Higher weight means a stronger preference.

---

# Multiple Preferred Rules

Example:

```yaml
preferredDuringSchedulingIgnoredDuringExecution:

- weight: 80

  preference:

    matchExpressions:

    - key: disk

      operator: In

      values:

      - ssd

- weight: 40

  preference:

    matchExpressions:

    - key: environment

      operator: In

      values:

      - production
```

A Node satisfying both preferences can receive a higher overall score than a Node satisfying only one.

---

# Required + Preferred

You can combine both.

Example:

```yaml
affinity:

  nodeAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

      nodeSelectorTerms:

      - matchExpressions:

        - key: environment

          operator: In

          values:

          - production

    preferredDuringSchedulingIgnoredDuringExecution:

    - weight: 80

      preference:

        matchExpressions:

        - key: disk

          operator: In

          values:

          - ssd
```

Meaning:

```text
Must:

environment=production

Prefer:

disk=ssd
```

---

# Real-World Example

Suppose a production cluster contains:

```text
Node 1
environment=production
disk=ssd

Node 2
environment=production
disk=hdd

Node 3
environment=development
disk=ssd
```

Pod requirements:

```text
Required:

environment=production
```

Preference:

```text
disk=ssd
```

Result:

```text
Node 1

↓

Preferred
```

```text
Node 2

↓

Acceptable
```

```text
Node 3

↓

Rejected
```

---

# Node Affinity vs nodeSelector

| Feature | nodeSelector | Node Affinity |
|---|---|---|
| Simple label matching | Yes | Yes |
| Multiple values with OR | Limited | Yes |
| `In` | No explicit operator | Yes |
| `NotIn` | No | Yes |
| `Exists` | No | Yes |
| `DoesNotExist` | No | Yes |
| Required rules | Yes | Yes |
| Preferred rules | No | Yes |
| Weight | No | Yes |
| Complex expressions | No | Yes |

---

# Node Affinity vs nodeName

### nodeName

```text
Specific Node
```

Example:

```yaml
nodeName: worker-01
```

---

### Node Affinity

```text
Set of Nodes

↓

Matching Requirements
```

Example:

```yaml
operator: In

values:

- ssd
- nvme
```

Node Affinity gives the Scheduler flexibility.

---

# Node Affinity and Taints

These mechanisms can complement each other.

Node Affinity:

```text
Which Nodes should this Pod run on?
```

Taints:

```text
Which Pods should be prevented from running here?
```

Tolerations:

```text
Which Pods are allowed onto the tainted Node?
```

Example:

```text
Database Nodes

↓

Tainted:

dedicated=database:NoSchedule
```

Database Pod:

```text
Node Affinity

+

Toleration
```

This creates both:

```text
Selection

+

Isolation
```

---

# Node Affinity and Pod Affinity

Do not confuse:

```text
Node Affinity
```

with:

```text
Pod Affinity
```

Node Affinity:

```text
Pod

↓

Node Labels
```

Pod Affinity:

```text
Pod

↓

Other Pods
```

Pod Affinity and Anti-Affinity are covered in the next chapter.

---

# Node Affinity and Topology

Node labels often represent topology.

Examples:

```text
topology.kubernetes.io/zone
```

```text
topology.kubernetes.io/region
```

A workload can use Node Affinity to constrain placement to particular topology domains.

Example:

```yaml
key: topology.kubernetes.io/zone

operator: In

values:

- zone-a
- zone-b
```

---

# Scheduling Workflow

```text
Pod Created

↓

Scheduler

↓

Read Node Affinity

↓

Filter

↓

Required Rules

↓

Feasible Nodes

↓

Score

↓

Preferred Rules

↓

Select Node

↓

Bind
```

---

# Required Affinity Failure

Suppose all Nodes have:

```text
disk=hdd
```

Pod requires:

```text
disk In [ssd]
```

Result:

```text
No feasible Node
```

Pod:

```text
Pending
```

---

# Preferred Affinity Behavior

Suppose:

```text
Node 1
disk=ssd

Node 2
disk=hdd
```

Pod prefers:

```text
disk=ssd
```

Both Nodes may remain feasible.

Scheduler can select:

```text
Node 1
```

because it satisfies the preference.

But if Node 1 becomes unavailable:

```text
Node 2
```

may still be selected.

---

# Important Difference

Required:

```text
Preference cannot be satisfied

↓

Scheduling fails
```

Preferred:

```text
Preference cannot be satisfied

↓

Scheduling can continue
```

---

# Hands-on Lab 1 – Create Node Labels

Label Nodes:

```bash
kubectl label node <node1> disk=ssd
```

```bash
kubectl label node <node2> disk=hdd
```

Verify:

```bash
kubectl get nodes -L disk
```

---

# Hands-on Lab 2 – Required Node Affinity

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: required-affinity-demo

spec:

  affinity:

    nodeAffinity:

      requiredDuringSchedulingIgnoredDuringExecution:

        nodeSelectorTerms:

        - matchExpressions:

          - key: disk

            operator: In

            values:

            - ssd

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f required-affinity.yaml
```

Check:

```bash
kubectl get pod -o wide
```

---

# Hands-on Lab 3 – Preferred Node Affinity

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: preferred-affinity-demo

spec:

  affinity:

    nodeAffinity:

      preferredDuringSchedulingIgnoredDuringExecution:

      - weight: 100

        preference:

          matchExpressions:

          - key: disk

            operator: In

            values:

            - ssd

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f preferred-affinity.yaml
```

Observe the selected Node.

---

# Hands-on Lab 4 – Multiple Values

Use:

```yaml
operator: In

values:

- ssd

- nvme
```

Verify that both Node types are eligible.

---

# Hands-on Lab 5 – NotIn

Create:

```yaml
operator: NotIn

values:

- hdd
```

Observe that HDD Nodes are excluded.

---

# Hands-on Lab 6 – Exists

Create:

```yaml
key: gpu

operator: Exists
```

Only Nodes with a `gpu` label are eligible.

---

# Hands-on Lab 7 – Required + Preferred

Create a Pod with:

```text
Required:

environment=production
```

and:

```text
Preferred:

disk=ssd
```

Observe how the Scheduler handles the two constraints differently.

---

# Hands-on Lab 8 – Force Scheduling Failure

Create:

```yaml
key: hardware

operator: In

values:

- quantum
```

If no Node has:

```text
hardware=quantum
```

check:

```bash
kubectl describe pod <pod-name>
```

Observe the `FailedScheduling` event.

---

# Troubleshooting Node Affinity

Check Pod:

```bash
kubectl get pod
```

Describe:

```bash
kubectl describe pod <pod-name>
```

Inspect:

```text
Events
```

Then inspect Node labels:

```bash
kubectl get nodes --show-labels
```

---

# Common Scheduling Errors

You may see messages related to:

```text
node(s) didn't match Pod's node affinity/selector
```

This usually means:

```text
Required Affinity

↓

No matching Node
```

---

# Common Mistakes

## 1. Confusing Required and Preferred

Required:

```text
Hard Requirement
```

Preferred:

```text
Soft Preference
```

---

## 2. Misunderstanding AND and OR

Within one `matchExpressions` list:

```text
AND
```

Across multiple `nodeSelectorTerms`:

```text
OR
```

This distinction is extremely important.

---

## 3. Using `In` Without Values

For:

```text
In
```

you normally need:

```yaml
values:
```

---

## 4. Assuming Preferred Affinity Guarantees Placement

It doesn't.

Preferred rules influence scoring but do not make a Node mandatory.

---

## 5. Using Too Many Complex Rules

Overly complicated affinity rules can make scheduling difficult to understand and troubleshoot.

---

## 6. Forgetting Node Labels

Affinity depends on actual Node labels.

Verify:

```bash
kubectl get nodes --show-labels
```

---

## 7. Using Mutable Labels Carelessly

Changing Node labels can affect where new Pods are eligible to run.

Maintain controlled label management.

---

## 8. Confusing Node Affinity with Pod Affinity

Node Affinity:

```text
Node Labels
```

Pod Affinity:

```text
Other Pods
```

---

# Quick Revision

## Required

```text
requiredDuringSchedulingIgnoredDuringExecution

↓

Must Match
```

---

## Preferred

```text
preferredDuringSchedulingIgnoredDuringExecution

↓

Try to Match
```

---

## Operators

```text
In

NotIn

Exists

DoesNotExist

Gt

Lt
```

---

## Logic

```text
matchExpressions

↓

AND
```

```text
nodeSelectorTerms

↓

OR
```

---

# Essential kubectl Commands

View Nodes:

```bash
kubectl get nodes
```

View Labels:

```bash
kubectl get nodes --show-labels
```

Add Label:

```bash
kubectl label node <node> key=value
```

Describe Node:

```bash
kubectl describe node <node>
```

View Pods:

```bash
kubectl get pods -o wide
```

Describe Pod:

```bash
kubectl describe pod <pod>
```

---

# Interview Questions

## Basic

- What is Node Affinity?
- Why is Node Affinity better than `nodeSelector` for complex requirements?
- What is the difference between required and preferred affinity?
- What is `requiredDuringSchedulingIgnoredDuringExecution`?
- What is `preferredDuringSchedulingIgnoredDuringExecution`?

---

## Intermediate

- Explain the `In` operator.
- What does `NotIn` do?
- What is the difference between `Exists` and `DoesNotExist`?
- What is the purpose of the `weight` field?
- What happens if required Node Affinity cannot be satisfied?
- Explain AND and OR behavior in Node Affinity.

---

## Advanced

- Explain the complete Node Affinity scheduling workflow.
- How does Node Affinity interact with Scheduler filtering and scoring?
- Compare Node Selector and Node Affinity.
- How can Node Affinity be combined with Taints and Tolerations?
- How can topology labels be used with Node Affinity?
- Explain `requiredDuringSchedulingIgnoredDuringExecution` in detail.
- Explain why preferred affinity does not guarantee placement.
- How would you troubleshoot a Pod stuck in Pending because of Node Affinity?
- Design an affinity policy for production database workloads.
- How would you use Node Affinity to prefer SSD Nodes while allowing fallback to HDD Nodes?

---

# Production Design Example

Suppose a production cluster has:

```text
Node 1
environment=production
disk=ssd
workload=database

Node 2
environment=production
disk=hdd
workload=database

Node 3
environment=production
disk=ssd
workload=api
```

Database workload:

```text
Required:

environment=production
```

```text
Preferred:

workload=database
```

```text
Preferred:

disk=ssd
```

Conceptually:

```text
                    Database Pod

                         │
                         ▼
              Required Affinity
                         │
                  environment=
                    production
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           Node 1                 Node 2
           database              database
           SSD                   HDD
              │
              ▼
        Higher Preference
```

The Pod can run on production Nodes but will prefer Nodes that better satisfy the preferred rules.

---

# Best Practices

### 1. Use Required Rules Only for Genuine Requirements

If a requirement is not mandatory, use preferred affinity.

---

### 2. Use Preferred Affinity for Optimization

Examples:

```text
Prefer SSD
```

```text
Prefer high-memory
```

```text
Prefer a particular zone
```

---

### 3. Keep Rules Understandable

Avoid unnecessary scheduling complexity.

---

### 4. Use Stable Node Labels

Labels should represent stable infrastructure characteristics.

---

### 5. Combine with Taints for Dedicated Nodes

Use:

```text
Affinity

+

Taints/Tolerations
```

when you need strong workload isolation.

---

### 6. Test Scheduling Failures

Intentionally create unsatisfiable rules in a lab and learn how to diagnose:

```text
FailedScheduling
```

---

### 7. Consider Topology

For highly available workloads, affinity should be designed together with:

- Zones
- Regions
- Pod anti-affinity
- Topology spread constraints

---

# References

## Official Kubernetes Documentation

- Assigning Pods to Nodes
- Node Affinity
- Labels and Selectors
- Taints and Tolerations
- Pod Topology Spread Constraints
- Kubernetes Scheduler

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Scheduling Framework
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. Create Nodes with different labels.
2. Deploy a Pod using required Node Affinity.
3. Deploy another Pod using preferred Node Affinity.
4. Experiment with `In`.
5. Experiment with `NotIn`.
6. Test `Exists` and `DoesNotExist`.
7. Experiment with multiple `matchExpressions`.
8. Experiment with multiple `nodeSelectorTerms`.
9. Combine required and preferred affinity.
10. Intentionally create an impossible affinity rule and troubleshoot it.
11. Combine Node Affinity with Taints and Tolerations.
12. Practice topology-based scheduling.

---

# Chapter Summary

```text
                     Pod

                      │
                      ▼
                Node Affinity
                      │
          ┌───────────┴───────────┐
          │                       │
       Required                Preferred
          │                       │
          ▼                       ▼
       Filter                    Score
          │                       │
          └───────────┬───────────┘
                      ▼
                 Scheduler
                      │
                      ▼
                 Selected Node
```

**Node Affinity** extends the capabilities of `nodeSelector` by allowing Pods to express sophisticated scheduling requirements and preferences.

The most important concepts are:

```text
Required
    ↓
Must match

Preferred
    ↓
Should match if possible
```

And the logical behavior:

```text
matchExpressions
    ↓
AND

nodeSelectorTerms
    ↓
OR
```

The key comparison is:

```text
nodeName
    ↓
Exact Node

nodeSelector
    ↓
Simple label matching

Node Affinity
    ↓
Advanced label-based scheduling
```

Node Affinity becomes especially powerful when combined with:

```text
Taints & Tolerations
        ↓
Workload Isolation

Pod Affinity / Anti-Affinity
        ↓
Pod Placement Relationships

Topology Spread
        ↓
High Availability
```

These mechanisms together form the foundation of production-grade Kubernetes scheduling.

---

## Next Chapter

# Chapter 39 – Pod Affinity & Anti-Affinity

Topics will include:

- What is Pod Affinity?
- What is Pod Anti-Affinity?
- Why Pod-to-Pod placement matters
- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`
- `topologyKey`
- Pod labels and selectors
- Same-Node placement
- Same-Zone placement
- Cross-zone distribution
- High Availability
- Database and application patterns
- Affinity vs Anti-Affinity
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---