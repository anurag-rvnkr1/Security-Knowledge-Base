# Chapter 44 – Vertical Pod Autoscaler (VPA)

## Overview

In the previous chapter, we learned about the **Horizontal Pod Autoscaler (HPA)**.

HPA changes:

```text
Number of Pods
```

For example:

```text
2 Pods
   ↓
5 Pods
   ↓
10 Pods
```

But sometimes adding more Pods is not the right solution.

A workload may instead need:

```text
More CPU per Pod
More Memory per Pod
```

This is where **Vertical Pod Autoscaler (VPA)** is useful.

VPA automatically analyzes resource usage and can recommend or update the CPU and memory requests/limits of Pods.

The basic concept is:

```text
Pod Resource Usage

        ↓

VPA Recommender

        ↓

Resource Recommendation

        ↓

VPA

        ↓

Updated Pod Resources
```

> **HPA scales the number of Pods horizontally, while VPA adjusts the resource allocation of individual Pods vertically.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What VPA is
- Why VPA is needed
- Horizontal vs Vertical autoscaling
- VPA architecture
- VPA components
- Recommender
- Updater
- Admission Controller
- VPA modes
- `Off`
- `Initial`
- `Recreate`
- `Auto`
- Resource recommendations
- CPU recommendations
- Memory recommendations
- VPA and resource requests
- VPA and limits
- VPA with HPA
- VPA with Cluster Autoscaler
- VPA limitations
- Production considerations
- Hands-on Labs
- Common mistakes
- Troubleshooting
- Best practices
- Interview questions

---

# What Is Vertical Scaling?

Vertical scaling means:

```text
Increase resources assigned to a Pod
```

Example:

```text
Before:

CPU = 250m
Memory = 256Mi
```

After:

```text
CPU = 500m
Memory = 512Mi
```

The number of Pods does not necessarily change.

---

# Horizontal vs Vertical Scaling

## Horizontal Scaling

```text
More Pods
```

Example:

```text
3 Pods
 ↓
6 Pods
```

Managed by:

```text
HPA
```

---

## Vertical Scaling

```text
More Resources per Pod
```

Example:

```text
500m CPU
 ↓
1 CPU
```

Managed by:

```text
VPA
```

---

# Comparison

| Feature | HPA | VPA |
|---|---|---|
| Scaling direction | Horizontal | Vertical |
| Changes | Pod count | Pod resources |
| Main target | Replica count | Requests/limits |
| Useful for | Elastic traffic | Right-sizing workloads |
| May recreate Pods | Normally no | Some modes can |
| Common metric | CPU, memory, custom metrics | Historical resource usage |

---

# Why Do We Need VPA?

Suppose an application has:

```text
1 Pod
```

and consistently requires:

```text
CPU = 2 CPU
Memory = 4Gi
```

But its configuration is:

```yaml
requests:

  cpu: "250m"

  memory: "512Mi"
```

The workload may be under-requested.

HPA might respond by creating:

```text
8 Pods
```

even though the actual requirement is simply:

```text
1–2 appropriately sized Pods
```

VPA can help identify better resource values.

---

# VPA Architecture

A simplified architecture:

```text
                    Kubernetes Cluster

                           │
                           ▼
                    Running Workloads
                           │
                           ▼
                    Resource Metrics
                           │
                           ▼
                       Recommender
                           │
                           ▼
                  Resource Recommendation
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                 Updater       Admission
                    │          Controller
                    │             │
                    ▼             ▼
                 Pod Restart   New Pod
                    │             │
                    └──────┬──────┘
                           ▼
                    Updated Resources
```

---

# VPA Components

VPA generally consists of three major components:

```text
Recommender
```

```text
Updater
```

```text
Admission Controller
```

---

# VPA Recommender

The **Recommender** analyzes resource usage and determines recommended CPU and memory values.

Conceptually:

```text
Historical Usage

      ↓

Recommender

      ↓

CPU Recommendation
Memory Recommendation
```

It considers workload usage patterns and produces recommendations.

---

# VPA Updater

The **Updater** determines whether running Pods need to be recreated based on the VPA recommendation and policy.

Conceptually:

```text
Running Pod

    ↓

Current Resources

    ↓

VPA Recommendation

    ↓

Significant Difference?

    ↓

Updater

    ↓

Pod Replacement
```

---

# VPA Admission Controller

When a new Pod is created, the Admission Controller can modify the Pod's resource requests and limits according to VPA recommendations.

Conceptually:

```text
Pod Creation

     ↓

Admission Controller

     ↓

VPA Recommendation

     ↓

Mutate Pod Resources

     ↓

Pod Starts
```

---

# VPA Resource Recommendation

VPA can recommend:

```text
CPU Request
Memory Request
```

and corresponding resource limits depending on configuration and VPA policy.

A recommendation may look conceptually like:

```text
CPU:

Target = 500m
Lower Bound = 250m
Upper Bound = 1

Memory:

Target = 512Mi
Lower Bound = 256Mi
Upper Bound = 1Gi
```

---

# Recommendation Components

VPA recommendations can contain:

```text
Lower Bound
Target
Upper Bound
Uncapped Target
```

---

# Lower Bound

The lower bound represents a lower resource estimate below which the workload may be considered under-provisioned.

Conceptually:

```text
CPU:

Lower Bound = 250m
```

---

# Target

The target is the primary recommended resource value.

Example:

```text
CPU Target = 500m
```

This is commonly the value used when updating resources.

---

# Upper Bound

The upper bound represents an upper resource estimate.

Example:

```text
CPU Upper Bound = 1
```

The workload may require more than the target under certain conditions.

---

# Uncapped Target

The uncapped target represents a recommendation before constraints such as container policies or other limits are applied.

It can help understand the recommendation process.

---

# VPA Modes

VPA supports different operating modes.

Important modes include:

```text
Off
```

```text
Initial
```

```text
Recreate
```

```text
Auto
```

---

# Off Mode

Example:

```yaml
updatePolicy:

  updateMode: "Off"
```

VPA:

```text
Analyzes usage

↓

Provides recommendations

↓

Does not automatically update running Pods
```

This is useful for:

```text
Observation
Testing
Right-sizing analysis
```

---

# Initial Mode

Example:

```yaml
updatePolicy:

  updateMode: "Initial"
```

VPA applies recommendations when Pods are initially created.

Existing Pods are not automatically recreated simply because recommendations change.

Conceptually:

```text
New Pod

↓

VPA Admission

↓

Recommended Resources

↓

Pod starts
```

---

# Recreate Mode

Example:

```yaml
updatePolicy:

  updateMode: "Recreate"
```

VPA can recreate Pods when their resource recommendations need significant changes.

Conceptually:

```text
Running Pod

↓

Recommendation changes

↓

Updater identifies Pod

↓

Pod recreated

↓

New resources applied
```

This can cause disruption unless the application is designed for Pod replacement.

---

# Auto Mode

Historically, VPA has supported:

```text
Auto
```

for automatic updates.

The exact behavior and support can vary by VPA version.

When using modern VPA installations, verify the installed VPA version and its documented supported update modes.

---

# VPA Example

A basic VPA object:

```yaml
apiVersion: autoscaling.k8s.io/v1

kind: VerticalPodAutoscaler

metadata:

  name: web-vpa

spec:

  targetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: web

  updatePolicy:

    updateMode: "Off"
```

This tells VPA:

```text
Monitor Deployment/web

↓

Generate recommendations

↓

Do not automatically change Pods
```

---

# VPA Target Reference

Example:

```yaml
targetRef:

  apiVersion: apps/v1

  kind: Deployment

  name: web
```

This identifies the workload whose Pods VPA should analyze.

---

# VPA Update Policy

Example:

```yaml
updatePolicy:

  updateMode: "Off"
```

or:

```yaml
updateMode: "Initial"
```

or:

```yaml
updateMode: "Recreate"
```

The supported modes depend on the VPA version installed in the cluster.

---

# Resource Policy

VPA can also define resource policies.

Example:

```yaml
resourcePolicy:

  containerPolicies:

  - containerName: "*"

    minAllowed:

      cpu: "100m"

      memory: "128Mi"

    maxAllowed:

      cpu: "2"

      memory: "2Gi"
```

This constrains VPA recommendations.

---

# minAllowed

Example:

```yaml
minAllowed:

  cpu: "100m"

  memory: "128Mi"
```

This prevents VPA from recommending values below the specified minimum.

---

# maxAllowed

Example:

```yaml
maxAllowed:

  cpu: "2"

  memory: "2Gi"
```

This prevents VPA from recommending values above the specified maximum.

---

# Container Policy

Example:

```yaml
containerPolicies:

- containerName: app

  minAllowed:

    cpu: "100m"

    memory: "128Mi"

  maxAllowed:

    cpu: "2"

    memory: "2Gi"
```

This policy applies specifically to:

```text
app
```

container.

---

# Wildcard Container Policy

You may encounter:

```yaml
containerName: "*"
```

This means the policy applies broadly to containers in the targeted Pods.

Use carefully in multi-container workloads.

---

# VPA and CPU

Suppose the workload uses:

```text
CPU request = 250m
```

but actual usage consistently reaches:

```text
700m
```

VPA may recommend increasing CPU resources.

Example:

```text
Current:
250m

Recommended:
600m
```

---

# VPA and Memory

Suppose:

```text
Memory request = 256Mi
```

but workload usage regularly reaches:

```text
700Mi
```

VPA may recommend:

```text
Memory request ≈ 768Mi
```

The exact recommendation is determined by VPA's analysis and configured constraints.

---

# VPA and Resource Requests

VPA primarily helps determine better resource requests.

Conceptually:

```text
Actual Usage

↓

Historical Analysis

↓

Recommended Request
```

This can improve:

```text
Scheduling
Capacity Planning
Cost Efficiency
```

---

# VPA and Resource Limits

VPA can also influence resource limits depending on the configured policy and VPA behavior.

Do not assume:

```text
VPA always changes both requests and limits identically.
```

Inspect the resulting Pod specification and the VPA configuration.

---

# VPA and HPA

This is an important production topic.

HPA:

```text
Changes Pod count
```

VPA:

```text
Changes Pod resource allocation
```

Using both on the same CPU/memory signal can create competing feedback loops.

Example:

```text
CPU usage high

↓

HPA adds Pods

↓

CPU per Pod decreases

↓

VPA may recommend less CPU

↓

Resources change

↓

HPA behavior changes again
```

Therefore, careful design is required.

---

# HPA + VPA Best Practice

A common approach is:

```text
HPA

↓

Custom / workload demand metric

```

while:

```text
VPA

↓

CPU / memory resource recommendations
```

This reduces the chance that both controllers react to the exact same signal.

---

# VPA and Cluster Autoscaler

VPA can change resource requests.

Suppose:

```text
Current request:
500m CPU
```

VPA recommends:

```text
1 CPU
```

The Pod may no longer fit on its current Node.

Then:

```text
Pod becomes Pending

↓

Cluster Autoscaler

↓

Adds capacity

↓

Pod scheduled
```

Therefore VPA and Cluster Autoscaler can work together.

---

# VPA + Cluster Autoscaler

```text
VPA

↓

Larger Pod Request

↓

Insufficient Node Capacity

↓

Pod Pending

↓

Cluster Autoscaler

↓

New Node

↓

Pod Scheduled
```

---

# VPA and Pod Disruption

VPA may need to recreate Pods when resource changes are required.

This can cause:

```text
Pod Restart
```

and potentially:

```text
Temporary Capacity Reduction
```

Therefore production workloads should use:

```text
Multiple replicas
Readiness Probes
PodDisruptionBudgets
Rolling Strategies
```

where appropriate.

---

# Stateful Workloads

VPA can be more complicated for:

```text
Databases
StatefulSets
Distributed systems
```

because replacing Pods can affect:

```text
Availability
Leader election
Storage
Replication
Connections
```

Always test carefully.

---

# VPA and DaemonSets

DaemonSets run Pods on Nodes according to Node scheduling rules.

VPA can be applied to supported workloads, but changing resources for DaemonSet Pods can have significant cluster-wide implications because a resource change may affect one Pod per Node.

Use caution.

---

# VPA and Jobs

Batch workloads can also benefit from resource recommendations.

However, for short-lived Jobs, VPA may have less historical data available.

For recurring batch workloads, historical analysis can become more useful.

---

# VPA Installation

VPA is not normally enabled simply by creating a VPA object.

The VPA components must be installed in the cluster.

A typical installation contains components similar to:

```text
vpa-recommender
vpa-updater
vpa-admission-controller
```

Check:

```bash
kubectl get pods -n kube-system
```

or the namespace where your VPA installation is deployed.

---

# Verify VPA CRD

Run:

```bash
kubectl get crd verticalpodautoscalers.autoscaling.k8s.io
```

If VPA is installed, the CRD should be available.

---

# Check VPA Objects

```bash
kubectl get vpa
```

or:

```bash
kubectl get verticalpodautoscalers
```

---

# Describe VPA

```bash
kubectl describe vpa <vpa-name>
```

Look for:

```text
Recommendation
```

---

# VPA Status

Example:

```text
Recommendation:

Container Recommendations:
  Target:
    Cpu: 500m
    Memory: 512Mi

  Lower Bound:
    Cpu: 250m
    Memory: 256Mi

  Upper Bound:
    Cpu: 1
    Memory: 1Gi
```

Exact output varies by VPA version and workload.

---

# Hands-on Lab 1 – Verify VPA Installation

Run:

```bash
kubectl get crd | grep verticalpodautoscaler
```

Then:

```bash
kubectl get pods -A | grep vpa
```

Identify:

```text
Recommender
Updater
Admission Controller
```

---

# Hands-on Lab 2 – Deploy Sample Application

Create:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: vpa-demo

spec:

  replicas: 2

  selector:

    matchLabels:

      app: vpa-demo

  template:

    metadata:

      labels:

        app: vpa-demo

    spec:

      containers:

      - name: app

        image: nginx

        resources:

          requests:

            cpu: "100m"

            memory: "128Mi"

          limits:

            cpu: "500m"

            memory: "512Mi"
```

Apply:

```bash
kubectl apply -f vpa-demo.yaml
```

---

# Hands-on Lab 3 – Create VPA in Off Mode

Create:

```yaml
apiVersion: autoscaling.k8s.io/v1

kind: VerticalPodAutoscaler

metadata:

  name: vpa-demo

spec:

  targetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: vpa-demo

  updatePolicy:

    updateMode: "Off"
```

Apply:

```bash
kubectl apply -f vpa.yaml
```

---

# Hands-on Lab 4 – View Recommendations

Run:

```bash
kubectl get vpa vpa-demo -o yaml
```

Look under:

```text
status.recommendation
```

You may see:

```text
target
lowerBound
upperBound
```

---

# Hands-on Lab 5 – Generate Workload

Generate application activity in a disposable environment.

Then allow VPA to collect historical usage.

Inspect:

```bash
kubectl describe vpa vpa-demo
```

Observe how recommendations evolve over time.

---

# Hands-on Lab 6 – Initial Mode

Change:

```yaml
updateMode: "Initial"
```

Create new Pods.

Observe that new Pods can receive VPA recommendations during creation.

---

# Hands-on Lab 7 – Resource Policies

Create:

```yaml
resourcePolicy:

  containerPolicies:

  - containerName: "*"

    minAllowed:

      cpu: "100m"

      memory: "128Mi"

    maxAllowed:

      cpu: "1"

      memory: "1Gi"
```

Observe how recommendations are bounded.

---

# Hands-on Lab 8 – Recreate Mode

Only in a disposable environment:

```yaml
updatePolicy:

  updateMode: "Recreate"
```

Allow resource recommendations to change significantly.

Observe Pod replacement.

Use:

```bash
kubectl get pods -w
```

and:

```bash
kubectl describe vpa <vpa-name>
```

---

# Important Lab Warning

Do not experiment with VPA `Recreate` mode on critical production workloads without understanding the disruption implications.

VPA may restart Pods to apply new resource settings.

---

# Troubleshooting

## VPA Has No Recommendation

Possible reasons:

```text
VPA is not installed correctly
```

```text
Metrics are unavailable
```

```text
Workload has insufficient historical usage
```

```text
VPA is not targeting the intended workload
```

---

# Check VPA Components

```bash
kubectl get pods -A | grep vpa
```

---

# Check VPA Logs

For example:

```bash
kubectl logs -n kube-system deployment/vpa-recommender
```

The exact deployment name and namespace may vary.

---

# Check VPA Object

```bash
kubectl describe vpa <vpa-name>
```

Look at:

```text
Events
Recommendation
Conditions
```

---

# Check Metrics

If your environment uses Metrics Server:

```bash
kubectl top pods
```

and:

```bash
kubectl top nodes
```

---

# VPA Does Not Update Pods

Check:

```text
updateMode
```

If:

```text
Off
```

then VPA only provides recommendations.

If:

```text
Initial
```

it primarily affects Pod creation.

If:

```text
Recreate
```

or another supported automatic mode is configured, Pod replacement may occur according to VPA behavior.

---

# VPA Recommendation Too High

Possible reasons:

```text
Temporary traffic spike
```

```text
Memory leak
```

```text
Batch workload
```

```text
Insufficient recommendation constraints
```

Inspect:

```text
Historical usage
Target
Upper Bound
```

---

# VPA Recommendation Too Low

Possible causes:

```text
Insufficient workload history
```

```text
Workload has not experienced peak traffic
```

```text
Resource usage is bursty
```

```text
Recommendation window does not capture relevant workload behavior
```

---

# Common Mistakes

## 1. Thinking VPA Adds More Pods

Incorrect:

```text
VPA
 ↓
More Pods
```

Correct:

```text
VPA
 ↓
Resource Adjustment
```

---

## 2. Confusing VPA with HPA

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

---

## 3. Using HPA and VPA Carelessly Together

If both use CPU utilization as their primary feedback signal, they can influence each other.

Design their metrics carefully.

---

## 4. Using Recreate Mode Without Understanding Disruption

VPA may need to recreate Pods.

This can cause:

```text
Temporary availability impact
```

---

## 5. Expecting Immediate Recommendations

VPA relies on usage history.

Recommendations may require time to become meaningful.

---

## 6. Ignoring Resource Policies

Without suitable bounds, VPA recommendations may not align with workload or cluster requirements.

---

## 7. Assuming VPA Fixes Application Memory Leaks

If an application continuously consumes more memory:

```text
Memory usage ↑
```

VPA may increase the recommendation.

But that does not fix:

```text
Memory leak
```

It may simply provide more memory before the problem becomes visible.

---

## 8. Ignoring Node Capacity

Increasing Pod resource requests can make Pods difficult to schedule.

---

## 9. Ignoring Stateful Workloads

Restarting a stateful application can have significant consequences.

---

# VPA vs HPA

```text
HPA

Traffic increases

↓

More Pods
```

```text
VPA

Resource usage increases

↓

More CPU/Memory per Pod
```

---

# VPA vs Cluster Autoscaler

```text
VPA

↓

Changes Pod resource requests
```

```text
Cluster Autoscaler

↓

Changes Node count
```

They can work together.

---

# VPA vs Resource Requests

VPA can help determine:

```text
What should the request be?
```

instead of manually guessing:

```text
cpu: 500m
memory: 512Mi
```

---

# VPA and QoS

VPA can change requests and limits.

This can potentially change a Pod's QoS classification.

For example:

```text
Burstable
```

could become:

```text
Guaranteed
```

if the resulting resource configuration satisfies the requirements for Guaranteed QoS.

Therefore, monitor QoS behavior when VPA changes resource settings.

---

# VPA and Scheduling

Suppose:

```text
Current request:

CPU = 500m
```

VPA recommends:

```text
CPU = 2
```

The Pod now requires significantly more capacity.

If no Node can accommodate:

```text
2 CPU
```

the Pod can remain:

```text
Pending
```

This is why:

```text
VPA
+
Cluster Capacity
```

must be considered together.

---

# VPA and Cost Optimization

VPA can help identify:

```text
Over-provisioned workloads
```

Example:

```text
Request:
4 CPU

Actual:
300m
```

VPA may recommend a much smaller value.

This can improve:

```text
Bin Packing
Node Utilization
Infrastructure Cost
```

---

# VPA Right-Sizing Workflow

```text
Deploy Workload

      ↓

Collect Usage

      ↓

VPA Recommender

      ↓

Analyze Recommendation

      ↓

Validate with Application Team

      ↓

Apply Appropriate Resources

      ↓

Monitor

      ↓

Repeat
```

---

# Production Strategy

A cautious production rollout can be:

```text
Phase 1

VPA = Off

↓

Observe recommendations
```

Then:

```text
Phase 2

Validate recommendations

↓

Set min/max bounds
```

Then:

```text
Phase 3

Use Initial mode for new Pods
```

Then, where appropriate:

```text
Phase 4

Evaluate automatic update mode
```

This reduces operational risk.

---

# VPA and SLOs

Do not optimize resources only for:

```text
CPU utilization
```

Also consider:

```text
Latency
Error Rate
Throughput
Availability
Startup Time
```

A lower CPU allocation might reduce cost but increase latency.

---

# Production Example

Suppose:

```text
Current CPU request:
2 CPU

Actual average:
500m

Peak:
1 CPU
```

VPA might recommend approximately:

```text
Target:
700m

Upper:
1.5 CPU
```

Instead of blindly accepting the recommendation, verify:

```text
Application performance
Peak traffic
Startup behavior
Downstream dependencies
SLOs
```

---

# Best Practices

### 1. Start with Off Mode

Use:

```yaml
updateMode: "Off"
```

to understand recommendations before automatic changes.

---

### 2. Set minAllowed and maxAllowed

Prevent unreasonable resource recommendations.

---

### 3. Monitor Historical Recommendations

Do not make decisions based on one short observation period.

---

### 4. Be Careful with Memory

Memory spikes and leaks require special attention.

---

### 5. Avoid Blind HPA + VPA CPU Scaling

Use different signals where possible.

---

### 6. Account for Pod Restarts

Automatic VPA updates can recreate Pods.

Use:

```text
Multiple replicas
Readiness probes
PodDisruptionBudgets
```

where appropriate.

---

### 7. Monitor Cluster Capacity

Large VPA recommendations can make Pods unschedulable.

---

### 8. Validate Recommendations

Treat VPA as an engineering aid, not an automatic substitute for capacity planning.

---

### 9. Use Workload-Specific Policies

A latency-sensitive API and a batch worker may need very different resource strategies.

---

### 10. Review Recommendations Periodically

Application behavior changes over time.

---

# Quick Revision

## VPA

```text
Vertical Pod Autoscaler
```

---

## VPA Purpose

```text
Adjust CPU / Memory resources
```

---

## Recommender

```text
Analyzes usage
```

---

## Updater

```text
Determines whether Pods need updating
```

---

## Admission Controller

```text
Applies recommendations to newly created Pods
```

---

## Off

```text
Recommendations only
```

---

## Initial

```text
Apply recommendations to new Pods
```

---

## Recreate

```text
Can recreate Pods to apply changes
```

---

## HPA

```text
More/Fewer Pods
```

---

## VPA

```text
More/Fewer Resources per Pod
```

---

# Essential kubectl Commands

Check VPA:

```bash
kubectl get vpa
```

Describe VPA:

```bash
kubectl describe vpa <name>
```

View VPA YAML:

```bash
kubectl get vpa <name> -o yaml
```

Check VPA CRD:

```bash
kubectl get crd verticalpodautoscalers.autoscaling.k8s.io
```

Check VPA components:

```bash
kubectl get pods -A | grep vpa
```

View Pod resources:

```bash
kubectl get pod <pod> -o yaml
```

View resource usage:

```bash
kubectl top pods
```

View Node usage:

```bash
kubectl top nodes
```

---

# Interview Questions

## Basic

- What is VPA?
- What is vertical scaling?
- What is the difference between HPA and VPA?
- What does VPA modify?
- What is the VPA Recommender?
- What is the VPA Updater?
- What is the Admission Controller?

---

## Intermediate

- Explain VPA update modes.
- What does `Off` mode do?
- What does `Initial` mode do?
- What does `Recreate` mode do?
- What is `minAllowed`?
- What is `maxAllowed`?
- What is a VPA recommendation?
- Why does VPA need historical usage?

---

## Advanced

- Explain the complete VPA architecture.
- How does VPA calculate resource recommendations?
- How does VPA interact with the Kubernetes Scheduler?
- How can VPA cause a Pod to become Pending?
- Explain VPA and Cluster Autoscaler interaction.
- Why can HPA and VPA conflict?
- How would you use HPA and VPA together safely?
- What are the risks of VPA `Recreate` mode?
- How would you deploy VPA in production safely?
- How can VPA improve cluster cost efficiency?
- How can VPA recommendations affect QoS?
- How would you troubleshoot a VPA with no recommendations?
- Why might VPA recommend excessive memory?
- Why should VPA not be treated as a replacement for application performance analysis?

---

# Production Architecture

A typical architecture:

```text
                    Application

                         │
                         ▼
                  Resource Usage

                         │
                         ▼
                   Metrics System

                         │
                         ▼
                  VPA Recommender
                         │
                         ▼
                  Recommendations
                         │
               ┌─────────┴─────────┐
               │                   │
               ▼                   ▼
          VPA Updater       Admission Controller
               │                   │
               ▼                   ▼
        Existing Pods        New Pods
               │                   │
               └─────────┬─────────┘
                         ▼
                  Updated Resources
                         │
                         ▼
                     Scheduler
                         │
                         ▼
                        Node
```

---

# HPA + VPA + Cluster Autoscaler

A production environment may use all three:

```text
                    Application Demand
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
               HPA                   VPA
                │                     │
                ▼                     ▼
          Pod Count             Pod Resources
                │                     │
                └──────────┬──────────┘
                           ▼
                       Scheduler
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                 Fits          Does Not Fit
                    │             │
                    ▼             ▼
                Existing      Cluster Autoscaler
                 Nodes              │
                                    ▼
                               New Nodes
```

This architecture can provide:

```text
Horizontal elasticity
+
Vertical right-sizing
+
Cluster capacity elasticity
```

but it requires careful configuration to avoid conflicting control loops.

---

# Recommended Practice

1. Install VPA in a disposable Kubernetes cluster.
2. Verify the VPA CRDs.
3. Verify Recommender, Updater, and Admission Controller.
4. Deploy a sample application.
5. Create a VPA in `Off` mode.
6. Generate realistic workload.
7. Inspect recommendations.
8. Add `minAllowed` and `maxAllowed`.
9. Test `Initial` mode.
10. Test `Recreate` mode in a disposable environment.
11. Observe Pod replacement.
12. Compare VPA recommendations with actual usage.
13. Study how VPA changes scheduling requirements.
14. Test VPA with Cluster Autoscaler.
15. Study HPA + VPA interaction.
16. Measure application latency before and after right-sizing.
17. Design a production VPA rollout strategy.

---

# References

## Official Kubernetes Documentation

- Vertical Pod Autoscaling
- Resource Management for Pods and Containers
- Kubernetes Autoscaling
- Pod Quality of Service Classes
- Node Autoscaling
- Scheduling
- Pod Lifecycle

---

## CNCF Resources

- Kubernetes SIG Autoscaling
- Kubernetes SIG Scheduling
- Kubernetes SIG Node
- Cloud Native Computing Foundation (CNCF)

---

# Chapter Summary

VPA provides Kubernetes with a mechanism for automatically analyzing and adjusting the CPU and memory resources assigned to Pods.

The fundamental difference is:

```text
HPA
    ↓
Changes Pod count

VPA
    ↓
Changes Pod resources

Cluster Autoscaler
    ↓
Changes Node count
```

VPA consists of three major components:

```text
Recommender
    ↓
Analyzes resource usage

Updater
    ↓
Determines which running Pods need updates

Admission Controller
    ↓
Applies recommendations when Pods are created
```

The main VPA modes are:

```text
Off
    ↓
Recommendations only

Initial
    ↓
Apply recommendations to new Pods

Recreate
    ↓
Recreate Pods to apply resource changes

Auto
    ↓
Automatic behavior depending on VPA version/configuration
```

VPA recommendations generally include:

```text
Lower Bound
Target
Upper Bound
Uncapped Target
```

A production VPA configuration can use:

```yaml
resourcePolicy:

  containerPolicies:

  - containerName: "*"

    minAllowed:

      cpu: "100m"

      memory: "128Mi"

    maxAllowed:

      cpu: "2"

      memory: "2Gi"
```

This prevents the autoscaler from making completely unrestricted recommendations.

The most important operational concern is Pod replacement.

When VPA needs to change resources for an existing Pod, some update modes can cause:

```text
Pod termination

↓

New Pod creation

↓

New resource configuration
```

Therefore:

```text
VPA
+
Readiness Probes
+
Multiple Replicas
+
PodDisruptionBudget
```

can be important for production availability.

The relationship between HPA and VPA should also be carefully designed:

```text
HPA
    ↓
Scale number of Pods

VPA
    ↓
Right-size individual Pods
```

Using both against the same resource signal can create feedback loops.

A safer design can use:

```text
HPA
    ↓
Application demand metric

VPA
    ↓
CPU / Memory right-sizing
```

Finally:

> **VPA should be treated as a resource right-sizing and optimization mechanism, not as a replacement for capacity planning, application profiling, or performance engineering.**

A mature production workflow is:

```text
Measure

↓

Recommend

↓

Validate

↓

Bound

↓

Apply

↓

Monitor

↓

Tune
```

This makes VPA a powerful tool for improving:

```text
Resource Efficiency
Cost Optimization
Scheduling
Capacity Planning
Application Reliability
```

when used carefully.

---

## Next Chapter

# Chapter 45 – Cluster Autoscaler

Topics will include:

- What is Cluster Autoscaler?
- Why Node Autoscaling is needed
- HPA vs Cluster Autoscaler
- Cluster Autoscaler Architecture
- Scale Up
- Scale Down
- Unschedulable Pods
- Node Groups
- Node Pools
- Cloud Provider Integration
- AWS
- Azure
- Google Cloud
- Min/Max Node Counts
- Expander Strategies
- Scale-Down Candidates
- Node Drain and Pod Eviction
- PodDisruptionBudgets
- Unremovable Nodes
- DaemonSets
- Local Storage
- Node Affinity
- Taints and Tolerations
- Cluster Autoscaler and HPA
- Cluster Autoscaler and VPA
- Cost Optimization
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---
```