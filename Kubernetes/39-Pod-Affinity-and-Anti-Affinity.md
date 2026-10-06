# Chapter 39 – Pod Affinity & Anti-Affinity

## Overview

In the previous chapters, we learned how Kubernetes can schedule Pods based on **Node characteristics**.

```text
nodeSelector
    ↓
Node labels

Node Affinity
    ↓
Advanced Node label rules
```

But sometimes the location of a Pod should depend on the location of **other Pods**.

For example:

- Keep an API Pod close to its cache Pod.
- Run frontend and backend Pods in the same zone.
- Prevent multiple replicas of an application from running on the same Node.
- Spread database replicas across availability zones.
- Keep redundant application instances separated for high availability.

Kubernetes provides:

```text
Pod Affinity
```

and:

```text
Pod Anti-Affinity
```

for these scenarios.

> **Pod Affinity attracts Pods toward Nodes where matching Pods are already running. Pod Anti-Affinity repels Pods from Nodes where matching Pods are already running.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Pod Affinity is
- What Pod Anti-Affinity is
- Why Pod-to-Pod scheduling matters
- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`
- `topologyKey`
- Label selectors
- Same-Node placement
- Same-Zone placement
- Cross-zone distribution
- High-availability patterns
- Affinity vs Anti-Affinity
- Pod Affinity vs Node Affinity
- Scheduling failures
- Hands-on Labs
- Common Mistakes
- Best Practices

---

# Why Do We Need Pod Affinity?

Suppose a cluster contains:

```text
Node 1
Frontend Pod

Node 2
Backend Pod

Node 3
Cache Pod
```

The application may perform better if:

```text
Frontend

↓

Backend

↓

Cache
```

are placed close together.

Pod Affinity can express:

> Schedule this Pod near Nodes that already contain Pods matching a particular label.

---

# Why Do We Need Pod Anti-Affinity?

Consider a Deployment with three replicas:

```text
app-1
app-2
app-3
```

If all three run on the same Node:

```text
Node 1

├── app-1
├── app-2
└── app-3
```

and that Node fails:

```text
Node 1
    ↓
Failure
```

all replicas could become unavailable simultaneously.

Pod Anti-Affinity can distribute them:

```text
Node 1 → app-1

Node 2 → app-2

Node 3 → app-3
```

This improves resilience.

---

# Core Concept

## Pod Affinity

```text
Pod A

↓

Find Nodes containing Pod B

↓

Schedule Pod A nearby
```

---

## Pod Anti-Affinity

```text
Pod A

↓

Find Nodes containing Pod B

↓

Avoid those Nodes
```

---

# High-Level Architecture

```text
                  Kubernetes Scheduler

                          │

            ┌─────────────┴─────────────┐

            ▼                           ▼

      Pod Affinity                Pod Anti-Affinity

            │                           │

            ▼                           ▼

      Attract toward              Avoid matching
      matching Pods               Pod locations
```

---

# Example Cluster

```text
Node 1
zone=a

├── frontend-1
└── backend-1
```

```text
Node 2
zone=b

└── backend-2
```

```text
Node 3
zone=c

└── backend-3
```

A new Pod can use affinity to prefer Nodes containing:

```text
app=backend
```

---

# Pod Affinity Structure

A typical configuration:

```yaml
affinity:

  podAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

    - labelSelector:

        matchLabels:

          app: backend

      topologyKey: kubernetes.io/hostname
```

This means:

> Schedule this Pod only where a matching `backend` Pod exists within the specified topology domain.

---

# Pod Anti-Affinity Structure

```yaml
affinity:

  podAntiAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

    - labelSelector:

        matchLabels:

          app: web

      topologyKey: kubernetes.io/hostname
```

This means:

> Do not schedule this Pod in a topology domain containing another matching `web` Pod.

---

# Required vs Preferred

Like Node Affinity, Pod Affinity and Anti-Affinity support:

```text
requiredDuringSchedulingIgnoredDuringExecution
```

and:

```text
preferredDuringSchedulingIgnoredDuringExecution
```

---

# Required

Required means:

```text
Must satisfy the rule
```

If no suitable location exists:

```text
Pod

↓

Pending
```

---

# Preferred

Preferred means:

```text
Try to satisfy the rule
```

If the preference cannot be satisfied:

```text
Scheduler

↓

Can still select another feasible Node
```

---

# topologyKey

`topologyKey` is one of the most important concepts in Pod Affinity and Anti-Affinity.

It tells Kubernetes:

> **At what topology level should the relationship be evaluated?**

Examples:

```text
kubernetes.io/hostname
```

```text
topology.kubernetes.io/zone
```

```text
topology.kubernetes.io/region
```

---

# topologyKey: hostname

Example:

```yaml
topologyKey: kubernetes.io/hostname
```

This evaluates relationships at the **Node level**.

Conceptually:

```text
Node 1
    ↓
Hostname domain

Node 2
    ↓
Hostname domain
```

---

# topologyKey: zone

Example:

```yaml
topologyKey: topology.kubernetes.io/zone
```

This evaluates relationships at the **availability-zone level**.

Example:

```text
Zone A
├── Node 1
└── Node 2

Zone B
├── Node 3
└── Node 4
```

---

# topologyKey: region

Example:

```yaml
topologyKey: topology.kubernetes.io/region
```

This evaluates the relationship at the regional level.

---

# Why topologyKey Matters

Consider:

```text
Pod A
Node 1
Zone A
```

If we use:

```text
topologyKey=hostname
```

another Pod can be constrained relative to:

```text
Node 1
```

If we use:

```text
topologyKey=zone
```

the relationship applies to:

```text
Zone A
```

The scope is therefore different.

---

# Pod Affinity Example

Suppose a backend Pod exists:

```yaml
labels:

  app: backend
```

A frontend Pod can request:

```yaml
affinity:

  podAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

    - labelSelector:

        matchLabels:

          app: backend

      topologyKey: kubernetes.io/hostname
```

The frontend Pod must be scheduled in a Node topology domain where a matching backend Pod exists.

---

# Same-Node Affinity

Using:

```yaml
topologyKey: kubernetes.io/hostname
```

allows affinity to be evaluated at the Node level.

Conceptually:

```text
Node 1

├── backend
└── frontend
```

---

# Same-Zone Affinity

Using:

```yaml
topologyKey: topology.kubernetes.io/zone
```

allows:

```text
Zone A

├── Node 1
│   └── backend
│
├── Node 2
│   └── frontend
```

The Pods do not necessarily need to be on the same Node.

They need to satisfy the relationship within the same topology domain.

---

# Pod Anti-Affinity

Pod Anti-Affinity does the opposite.

Example:

```yaml
affinity:

  podAntiAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

    - labelSelector:

        matchLabels:

          app: web

      topologyKey: kubernetes.io/hostname
```

Meaning:

```text
Do not place this Pod

↓

on a Node

↓

that already contains a matching web Pod
```

---

# Example

Existing:

```text
Node 1

web-1
```

New:

```text
web-2
```

With required anti-affinity:

```text
Node 1

↓

Rejected
```

Scheduler may choose:

```text
Node 2
```

---

# High Availability Pattern

Deployment:

```text
replicas: 3
```

Anti-affinity:

```text
app=web
```

topology:

```text
kubernetes.io/hostname
```

Result:

```text
Node 1
web-1

Node 2
web-2

Node 3
web-3
```

If Node 1 fails:

```text
web-2
web-3
```

remain available.

---

# Zone-Level Anti-Affinity

For stronger resilience:

```yaml
topologyKey: topology.kubernetes.io/zone
```

The goal can be to distribute matching replicas across zones.

Conceptually:

```text
Zone A
web-1

Zone B
web-2

Zone C
web-3
```

This protects against an entire zone failure.

---

# Important Distinction

Node-level anti-affinity:

```text
kubernetes.io/hostname
```

Protects against:

```text
Node failure
```

Zone-level distribution:

```text
topology.kubernetes.io/zone
```

Can protect against:

```text
Zone failure
```

---

# Pod Affinity vs Node Affinity

These are different.

## Node Affinity

Uses:

```text
Node Labels
```

Example:

```text
disk=ssd
```

---

## Pod Affinity

Uses:

```text
Labels of Other Pods
```

Example:

```text
app=backend
```

---

# Comparison

| Feature | Node Affinity | Pod Affinity |
|---|---|---|
| Based on | Node labels | Pod labels |
| Relationship | Pod → Node | Pod → Pod |
| Example | disk=ssd | app=backend |
| Topology | Optional | Important |
| Main purpose | Hardware/location selection | Pod co-location |

---

# Pod Affinity vs Anti-Affinity

| Feature | Pod Affinity | Pod Anti-Affinity |
|---|---|---|
| Behavior | Attract | Repel |
| Goal | Co-location | Separation |
| Example | Frontend near cache | Replicas on different Nodes |
| Useful for | Locality | High availability |

---

# Label Selector

Pod Affinity depends on identifying the Pods involved.

Example:

```yaml
labelSelector:

  matchLabels:

    app: backend
```

The Scheduler looks for Pods matching:

```text
app=backend
```

---

# matchExpressions

Pod Affinity also supports label selector expressions.

Example:

```yaml
labelSelector:

  matchExpressions:

  - key: app

    operator: In

    values:

    - backend

    - cache
```

This matches:

```text
app=backend

OR

app=cache
```

---

# Namespace Considerations

Pod Affinity and Anti-Affinity can specify the namespaces in which matching Pods should be considered.

Example:

```yaml
namespaces:

- production
```

This can prevent relationships from accidentally considering Pods in unrelated namespaces.

---

# namespaceSelector

More flexible configurations can use:

```yaml
namespaceSelector:
```

to select namespaces based on labels.

This is useful in multi-tenant environments.

---

# Namespace Scope

If you do not intentionally configure namespace selection, carefully understand which Pods are considered by the affinity rule.

For production systems, explicitly defining the intended scope can make scheduling behavior easier to reason about.

---

# Required Pod Affinity Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: frontend

  labels:

    app: frontend

spec:

  affinity:

    podAffinity:

      requiredDuringSchedulingIgnoredDuringExecution:

      - labelSelector:

          matchLabels:

            app: backend

        topologyKey: kubernetes.io/hostname

  containers:

  - name: nginx

    image: nginx
```

---

# Required Pod Anti-Affinity Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: web

  labels:

    app: web

spec:

  affinity:

    podAntiAffinity:

      requiredDuringSchedulingIgnoredDuringExecution:

      - labelSelector:

          matchLabels:

            app: web

        topologyKey: kubernetes.io/hostname

  containers:

  - name: nginx

    image: nginx
```

---

# Preferred Pod Anti-Affinity

```yaml
affinity:

  podAntiAffinity:

    preferredDuringSchedulingIgnoredDuringExecution:

    - weight: 100

      podAffinityTerm:

        labelSelector:

          matchLabels:

            app: web

        topologyKey: kubernetes.io/hostname
```

This tells the Scheduler:

```text
Prefer not to colocate web Pods
```

but does not make separation mandatory.

---

# Weight

Preferred affinity and anti-affinity rules use:

```yaml
weight: 100
```

The valid range is:

```text
1–100
```

Higher weight indicates a stronger preference.

---

# Combining Affinity and Anti-Affinity

A workload can use both.

Example:

```text
Prefer:

same zone as cache
```

and:

```text
Avoid:

same Node as another replica
```

Conceptually:

```text
Pod

├── Pod Affinity
│      ↓
│   Same Zone
│
└── Pod Anti-Affinity
       ↓
    Different Node
```

---

# Real-World Example – Frontend and Backend

Suppose:

```text
backend
app=backend
```

Frontend:

```text
app=frontend
```

Frontend uses:

```text
Pod Affinity

↓

app=backend

↓

same zone
```

Architecture:

```text
Zone A

Node 1
backend

Node 2
frontend
```

The Pods are in the same zone, potentially reducing network latency compared with placing them in different zones.

---

# Real-World Example – Database Replicas

Database replicas:

```text
db-1
db-2
db-3
```

Use anti-affinity:

```text
app=database
```

with:

```text
topologyKey=hostname
```

This discourages or prevents multiple replicas from sharing a Node, depending on whether the rule is preferred or required.

---

# Real-World Example – Multi-Zone Application

Application replicas:

```text
replica-1 → Zone A
replica-2 → Zone B
replica-3 → Zone C
```

This reduces the blast radius of a zone-level failure.

For precise replica distribution, Kubernetes **topology spread constraints** may sometimes be a better fit than anti-affinity.

---

# Pod Affinity and Scheduler

The Scheduler evaluates Pod Affinity and Anti-Affinity during scheduling.

Conceptually:

```text
Pod

↓

Affinity Rules

↓

Inspect Matching Pods

↓

Evaluate Topology

↓

Filter / Score Nodes

↓

Select Node
```

---

# Scheduling Failure

Suppose:

```text
Pod A

requires:

app=backend
```

and:

```text
topologyKey=hostname
```

But no Node contains:

```text
app=backend
```

If the rule is required:

```text
Pod

↓

Pending
```

---

# Anti-Affinity Failure

Suppose:

```text
Node 1
web-1

Node 2
web-2
```

and the cluster has only two Nodes.

A third Pod requires:

```text
required Pod Anti-Affinity
```

with:

```text
app=web
```

There is no eligible Node.

Result:

```text
web-3

↓

Pending
```

---

# Troubleshooting

Check:

```bash
kubectl get pods -o wide
```

Then:

```bash
kubectl describe pod <pod-name>
```

Inspect:

```text
Events
```

Look for:

```text
FailedScheduling
```

---

# Check Pod Labels

```bash
kubectl get pods --show-labels
```

This helps confirm that the Pods actually match the affinity selector.

---

# Check Node Topology Labels

```bash
kubectl get nodes \
-L kubernetes.io/hostname \
-L topology.kubernetes.io/zone \
-L topology.kubernetes.io/region
```

---

# Check Pod Placement

```bash
kubectl get pods -o wide
```

This displays the Node on which each Pod is running.

---

# Hands-on Lab 1 – Create Backend Pod

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: backend

  labels:

    app: backend

spec:

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f backend.yaml
```

---

# Hands-on Lab 2 – Create Frontend with Pod Affinity

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: frontend

  labels:

    app: frontend

spec:

  affinity:

    podAffinity:

      requiredDuringSchedulingIgnoredDuringExecution:

      - labelSelector:

          matchLabels:

            app: backend

        topologyKey: kubernetes.io/hostname

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f frontend.yaml
```

Check:

```bash
kubectl get pods -o wide
```

---

# Hands-on Lab 3 – Test Required Anti-Affinity

Create multiple replicas with:

```text
app=web
```

and:

```yaml
podAntiAffinity:

  requiredDuringSchedulingIgnoredDuringExecution:
```

using:

```text
kubernetes.io/hostname
```

Observe how Pods are distributed across Nodes.

---

# Hands-on Lab 4 – Force an Anti-Affinity Failure

Use more replicas than available Nodes.

Example:

```text
2 Nodes

3 replicas

Required anti-affinity
```

Eventually:

```text
One Pod

↓

Pending
```

Inspect:

```bash
kubectl describe pod <pod-name>
```

---

# Hands-on Lab 5 – Preferred Anti-Affinity

Change:

```text
required
```

to:

```text
preferred
```

Create more replicas than available Nodes.

Observe that Kubernetes can colocate Pods when necessary.

---

# Hands-on Lab 6 – Zone-Based Affinity

If your cluster has multiple zones:

```bash
kubectl get nodes \
-L topology.kubernetes.io/zone
```

Create Pods using:

```yaml
topologyKey: topology.kubernetes.io/zone
```

Observe placement.

---

# Hands-on Lab 7 – Inspect Labels

Run:

```bash
kubectl get pods --show-labels
```

Then:

```bash
kubectl get nodes --show-labels
```

Identify:

```text
Pod labels
```

and:

```text
Node topology labels
```

---

# Common Mistakes

## 1. Confusing Pod Affinity with Node Affinity

Pod Affinity:

```text
Pod → Other Pods
```

Node Affinity:

```text
Pod → Node Labels
```

---

## 2. Forgetting topologyKey

Pod Affinity and Anti-Affinity require a topology domain.

Without a meaningful topology key, the intended placement relationship cannot be expressed correctly.

---

## 3. Using Required Anti-Affinity Too Aggressively

Example:

```text
3 replicas

2 Nodes

Required anti-affinity
```

At least one replica may remain Pending.

---

## 4. Using hostname When You Really Need Zone Separation

```text
hostname
```

provides Node-level separation.

For zone-level separation:

```text
topology.kubernetes.io/zone
```

may be more appropriate.

---

## 5. Assuming Anti-Affinity Automatically Guarantees Perfect Distribution

Anti-affinity can prevent co-location based on the specified topology, but it is not the same as a precise balancing mechanism.

For exact distribution goals, consider:

```text
Pod Topology Spread Constraints
```

---

## 6. Forgetting Pod Labels

Affinity depends on matching Pod labels.

Check:

```bash
kubectl get pods --show-labels
```

---

## 7. Ignoring Namespace Scope

Matching Pods may come from namespaces depending on the affinity configuration.

Explicitly define the intended scope when necessary.

---

## 8. Making Every Rule Required

Hard constraints can make workloads unschedulable.

Use preferred rules where flexibility is acceptable.

---

# Pod Affinity vs Pod Anti-Affinity

```text
Pod Affinity

Pod A

↓

Find Pod B

↓

Move toward Pod B
```

```text
Pod Anti-Affinity

Pod A

↓

Find Pod B

↓

Move away from Pod B
```

---

# topologyKey Quick Reference

| topologyKey | Typical Meaning |
|---|---|
| `kubernetes.io/hostname` | Node |
| `topology.kubernetes.io/zone` | Availability Zone |
| `topology.kubernetes.io/region` | Region |

The exact labels available depend on the cluster and infrastructure.

---

# Required vs Preferred Quick Reference

```text
Required

↓

Hard Constraint

↓

No Match = Pending
```

```text
Preferred

↓

Soft Constraint

↓

No Match = Try Another Feasible Option
```

---

# Quick Revision

## Pod Affinity

```text
Attract

↓

Co-locate
```

---

## Pod Anti-Affinity

```text
Repel

↓

Separate
```

---

## Required

```text
Must satisfy
```

---

## Preferred

```text
Try to satisfy
```

---

## topologyKey

```text
Defines topology domain
```

---

# Essential kubectl Commands

View Pods:

```bash
kubectl get pods -o wide
```

View Pod Labels:

```bash
kubectl get pods --show-labels
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

View Node Labels:

```bash
kubectl get nodes --show-labels
```

View Zones:

```bash
kubectl get nodes -L topology.kubernetes.io/zone
```

View Hostnames:

```bash
kubectl get nodes -L kubernetes.io/hostname
```

---

# Interview Questions

## Basic

- What is Pod Affinity?
- What is Pod Anti-Affinity?
- Why do we need Pod Anti-Affinity?
- What is `topologyKey`?
- What is the difference between affinity and anti-affinity?

---

## Intermediate

- Explain required vs preferred Pod Affinity.
- How does Pod Affinity identify other Pods?
- What is the purpose of `labelSelector`?
- What does `kubernetes.io/hostname` mean?
- What does `topology.kubernetes.io/zone` represent?
- How can anti-affinity improve high availability?

---

## Advanced

- Explain the complete Pod Affinity scheduling process.
- Compare Pod Affinity with Node Affinity.
- Explain the difference between Node-level and Zone-level anti-affinity.
- Why can required anti-affinity make Pods remain Pending?
- How would you design a multi-zone application using anti-affinity?
- When should you use Pod Topology Spread Constraints instead of anti-affinity?
- How would you troubleshoot a Pod stuck in Pending because of Pod Anti-Affinity?
- How do namespace selectors affect Pod Affinity?
- How can affinity and anti-affinity be combined in a production workload?

---

# Production Design Example

A highly available application might use:

```text
Deployment

replicas: 3
```

with:

```text
Pod Anti-Affinity

↓

app=web
```

and:

```text
topologyKey:

kubernetes.io/hostname
```

Conceptually:

```text
              Web Application

                    │

          ┌─────────┼─────────┐

          ▼         ▼         ▼

       Node 1    Node 2    Node 3

       web-1     web-2     web-3
```

For stronger multi-zone resilience:

```text
Zone A
web-1

Zone B
web-2

Zone C
web-3
```

However, when the primary objective is controlled and balanced distribution across topology domains, **Pod Topology Spread Constraints** should also be considered.

---

# Best Practices

### 1. Use Anti-Affinity for High Availability

Separate critical replicas across Nodes or zones.

---

### 2. Prefer Soft Rules When Appropriate

Use:

```text
preferredDuringSchedulingIgnoredDuringExecution
```

when temporary co-location is acceptable.

---

### 3. Use Required Rules for Genuine Requirements

Do not unnecessarily make workloads unschedulable.

---

### 4. Choose topologyKey Carefully

Use:

```text
hostname
```

for Node-level separation.

Use:

```text
zone
```

for zone-level separation.

---

### 5. Use Topology Spread for Precise Distribution

For workloads that need balanced replica distribution, evaluate:

```text
topologySpreadConstraints
```

rather than relying solely on anti-affinity.

---

### 6. Keep Label Selectors Precise

A broad selector can unintentionally affect many workloads.

---

### 7. Test Failure Scenarios

Simulate:

```text
Node failure
```

and:

```text
Zone failure
```

to verify that your placement strategy actually improves availability.

---

# References

## Official Kubernetes Documentation

- Assigning Pods to Nodes
- Inter-Pod Affinity and Anti-Affinity
- Pod Topology Spread Constraints
- Labels and Selectors
- Kubernetes Scheduler
- Node Affinity

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Scheduling Framework
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. Create Pods with meaningful labels.
2. Experiment with required Pod Affinity.
3. Experiment with preferred Pod Affinity.
4. Test required Pod Anti-Affinity.
5. Test preferred Pod Anti-Affinity.
6. Compare `hostname` and `zone` topology.
7. Intentionally create an unschedulable anti-affinity workload.
8. Diagnose the `FailedScheduling` event.
9. Build a multi-Node high-availability Deployment.
10. Test what happens when a Node becomes unavailable.
11. Compare Pod Anti-Affinity with topology spread constraints.
12. Practice combining Node Affinity with Pod Anti-Affinity.

---

# Chapter Summary

```text
                  Pod Scheduling

                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     Pod Affinity            Pod Anti-Affinity
          │                         │
          ▼                         ▼
      Attract                    Repel
          │                         │
          ▼                         ▼
     Co-location               Separation
```

Pod Affinity and Anti-Affinity allow Kubernetes scheduling decisions to consider **relationships between Pods**, rather than only the characteristics of Nodes.

The key concepts are:

```text
Pod Affinity
    ↓
Place near matching Pods

Pod Anti-Affinity
    ↓
Place away from matching Pods

Required
    ↓
Hard constraint

Preferred
    ↓
Soft preference

topologyKey
    ↓
Defines where the relationship applies
```

The most important topology distinction is:

```text
kubernetes.io/hostname
    ↓
Node-level relationship

topology.kubernetes.io/zone
    ↓
Zone-level relationship

topology.kubernetes.io/region
    ↓
Region-level relationship
```

These mechanisms are especially valuable for:

```text
High Availability
      ↓
Replica Separation

Performance
      ↓
Pod Co-location

Fault Isolation
      ↓
Node / Zone Separation
```

However, for precise replica distribution across topology domains, Kubernetes **Topology Spread Constraints** can provide more explicit control than anti-affinity alone.

---

## Next Chapter

# Chapter 40 – Taints & Tolerations

Topics will include:

- What are Taints?
- What are Tolerations?
- Why Taints and Tolerations are needed
- Taint Effects
- `NoSchedule`
- `PreferNoSchedule`
- `NoExecute`
- Adding Taints
- Removing Taints
- Toleration Operators
- `Equal`
- `Exists`
- Toleration Seconds
- Dedicated Nodes
- GPU Nodes
- Control-Plane Nodes
- Workload Isolation
- Taints vs Node Affinity
- Hands-on Labs
- Common Mistakes
- Troubleshooting
- Quick Revision
- Interview Questions
- References

----
```