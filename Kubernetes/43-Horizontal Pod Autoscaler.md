# Chapter 43 – Horizontal Pod Autoscaler (HPA)

## Overview

In the previous chapter, we learned how Kubernetes manages CPU and memory using:

```text
Resource Requests
Resource Limits
```

But workloads do not always have constant traffic.

For example:

```text
Normal traffic
    ↓
2 Pods

High traffic
    ↓
8 Pods

Low traffic
    ↓
2 Pods
```

Running a fixed number of replicas all the time can be inefficient.

Kubernetes provides the **Horizontal Pod Autoscaler (HPA)** to automatically adjust the number of Pod replicas based on observed resource utilization or other supported metrics.

The basic concept is:

```text
Workload Metrics

      ↓

Horizontal Pod Autoscaler

      ↓

Desired Replica Count

      ↓

Deployment / ReplicaSet

      ↓

More or Fewer Pods
```

> **HPA horizontally scales a workload by changing the number of Pod replicas.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What HPA is
- Why horizontal scaling is needed
- HPA architecture
- How HPA changes replica counts
- CPU-based autoscaling
- Memory-based autoscaling
- `autoscaling/v2`
- `minReplicas`
- `maxReplicas`
- Target utilization
- Resource requests and HPA
- Scale-up behavior
- Scale-down behavior
- Stabilization windows
- Multiple metrics
- Custom metrics
- External metrics
- Metrics Server
- HPA troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Interview questions

---

# What Is Horizontal Scaling?

Horizontal scaling means:

```text
Add more Pods
```

or:

```text
Remove Pods
```

Example:

```text
Before:

Pod 1
Pod 2
```

During high traffic:

```text
Pod 1
Pod 2
Pod 3
Pod 4
Pod 5
```

This is called:

```text
Scale Out
```

When traffic decreases:

```text
Pod 1
Pod 2
```

This is:

```text
Scale In
```

---

# Horizontal vs Vertical Scaling

## Horizontal Scaling

```text
More Pods
```

Example:

```text
2 Pods
 ↓
6 Pods
```

---

## Vertical Scaling

```text
More CPU / Memory per Pod
```

Example:

```text
500m CPU
 ↓
1 CPU
```

Horizontal scaling:

```text
HPA
```

Vertical scaling:

```text
VPA
```

---

# HPA Architecture

A simplified architecture:

```text
                 Application Pods
                       │
                       ▼
                 Resource Usage
                       │
                       ▼
                Metrics Pipeline
                       │
                       ▼
                 Metrics API
                       │
                       ▼
                      HPA
                       │
                       ▼
              Desired Replicas
                       │
                       ▼
                  Deployment
                       │
                       ▼
                   ReplicaSet
                       │
                       ▼
                     Pods
```

---

# HPA and Deployment

HPA normally targets a scalable workload such as:

```text
Deployment
```

or another supported scalable resource.

Example:

```text
Deployment
replicas: 3
```

HPA can change:

```text
3
```

to:

```text
5
```

or:

```text
2
```

based on the configured metrics and policies.

---

# Basic HPA Example

```yaml
apiVersion: autoscaling/v2

kind: HorizontalPodAutoscaler

metadata:

  name: web-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: web

  minReplicas: 2

  maxReplicas: 10

  metrics:

  - type: Resource

    resource:

      name: cpu

      target:

        type: Utilization

        averageUtilization: 70
```

This means:

```text
Minimum Pods = 2

Maximum Pods = 10

Target CPU utilization = 70%
```

---

# HPA Fields

Important fields include:

```text
scaleTargetRef
```

```text
minReplicas
```

```text
maxReplicas
```

```text
metrics
```

and:

```text
behavior
```

---

# scaleTargetRef

Example:

```yaml
scaleTargetRef:

  apiVersion: apps/v1

  kind: Deployment

  name: web
```

This tells HPA:

```text
Which workload should be scaled?
```

---

# minReplicas

Example:

```yaml
minReplicas: 2
```

The HPA should not normally scale the target below:

```text
2 replicas
```

---

# maxReplicas

Example:

```yaml
maxReplicas: 10
```

The HPA should not normally scale the target above:

```text
10 replicas
```

---

# Target Utilization

Example:

```yaml
averageUtilization: 70
```

means the desired average CPU utilization is approximately:

```text
70%
```

The percentage is generally calculated relative to the Pods' CPU **requests**.

This is why CPU requests are important for HPA.

---

# Why CPU Requests Matter

Suppose:

```text
CPU request = 500m
```

and:

```text
Actual usage = 250m
```

Then:

```text
Utilization = 250 / 500 × 100
            = 50%
```

If the HPA target is:

```text
70%
```

the workload is below the target.

---

# Another Example

Request:

```text
500m
```

Usage:

```text
400m
```

Utilization:

```text
400 / 500 × 100
= 80%
```

If target is:

```text
70%
```

the HPA may scale out.

---

# HPA Scaling Formula

Conceptually, for utilization-based scaling:

```text
desiredReplicas
≈
ceil(
currentReplicas × currentMetric / targetMetric
)
```

Example:

```text
Current replicas = 4

Current CPU = 90%

Target CPU = 60%
```

Then:

```text
4 × 90 / 60
= 6
```

So approximately:

```text
Desired replicas = 6
```

Actual HPA behavior also incorporates tolerance, missing metrics, stabilization, and other considerations.

---

# CPU-Based HPA

Example:

```yaml
metrics:

- type: Resource

  resource:

    name: cpu

    target:

      type: Utilization

      averageUtilization: 70
```

The HPA monitors CPU utilization.

Conceptually:

```text
CPU increases

↓

HPA detects target exceeded

↓

Desired replicas increase

↓

Deployment creates Pods
```

---

# Memory-Based HPA

HPA can also use memory utilization.

Example:

```yaml
metrics:

- type: Resource

  resource:

    name: memory

    target:

      type: Utilization

      averageUtilization: 70
```

The HPA then uses memory utilization relative to memory requests.

---

# CPU + Memory

HPA can use multiple metrics.

Example:

```yaml
metrics:

- type: Resource

  resource:

    name: cpu

    target:

      type: Utilization

      averageUtilization: 70

- type: Resource

  resource:

    name: memory

    target:

      type: Utilization

      averageUtilization: 75
```

When multiple metrics are configured, HPA calculates a desired replica count for each metric and uses the **largest desired count**.

Conceptually:

```text
CPU metric
    ↓
Desired = 5

Memory metric
    ↓
Desired = 7

                ↓

HPA chooses:

7 replicas
```

---

# HPA Requires Metrics

HPA needs current metrics.

For CPU and memory resource metrics, a common component is:

```text
Metrics Server
```

Architecture:

```text
Kubelets

   ↓

Metrics Server

   ↓

Metrics API

   ↓

HPA
```

---

# Check Metrics Server

Run:

```bash
kubectl get deployment metrics-server -n kube-system
```

Then:

```bash
kubectl top pods
```

and:

```bash
kubectl top nodes
```

If `kubectl top` does not work, resource-based HPA may also fail to obtain the required metrics.

---

# Check HPA

```bash
kubectl get hpa
```

Example:

```text
NAME      REFERENCE          TARGETS   MINPODS   MAXPODS   REPLICAS
web-hpa   Deployment/web     45%/70%   2         10        3
```

---

# Describe HPA

```bash
kubectl describe hpa web-hpa
```

Important sections include:

```text
Metrics
Conditions
Events
Current Replicas
Desired Replicas
```

---

# HPA Conditions

HPA status can indicate conditions such as:

```text
AbleToScale
ScalingActive
ScalingLimited
```

These help diagnose problems.

---

# ScalingActive

A healthy HPA commonly reports that scaling is active.

If scaling is inactive, investigate:

```text
Metric availability
Target configuration
Workload configuration
```

---

# ScalingLimited

This condition can indicate that HPA wants a replica count outside the configured boundaries.

Example:

```text
Desired = 15

maxReplicas = 10
```

The HPA is limited to:

```text
10
```

---

# HPA and Deployments

Suppose:

```yaml
replicas: 3
```

is configured on a Deployment.

Then HPA manages the workload's replica count.

You should avoid treating the Deployment's static replica count as an independent scaling policy.

Conceptually:

```text
Deployment

replicas = HPA-controlled value
```

---

# Important Operational Rule

Do not continuously modify:

```bash
kubectl scale deployment web --replicas=3
```

while HPA is actively managing the same Deployment.

HPA may overwrite that manual replica setting according to its desired state.

---

# Scale Up

Suppose:

```text
Current replicas = 2
CPU target = 70%
Current CPU = 95%
```

HPA may determine:

```text
More replicas required
```

Result:

```text
2
 ↓
4
 ↓
6
```

depending on the workload, metrics, and configured behavior.

---

# Scale Down

Suppose:

```text
Current replicas = 8

CPU target = 70%

Current CPU = 25%
```

HPA may determine:

```text
Fewer replicas required
```

Result:

```text
8
 ↓
6
 ↓
4
```

Again, actual timing and rate are controlled by HPA behavior.

---

# Why Scale Down Is Usually More Conservative

Rapid scale-up can be useful during traffic spikes.

Rapid scale-down can cause:

```text
Thrashing
```

or:

```text
Repeated scale-out / scale-in cycles
```

Therefore Kubernetes supports scaling behavior controls.

---

# HPA Behavior

The `behavior` field can configure:

```text
scaleUp
```

and:

```text
scaleDown
```

Example:

```yaml
behavior:

  scaleUp:

    policies:

    - type: Percent

      value: 100

      periodSeconds: 60

  scaleDown:

    stabilizationWindowSeconds: 300
```

---

# Stabilization Window

A stabilization window prevents rapid oscillation.

Example:

```yaml
scaleDown:

  stabilizationWindowSeconds: 300
```

This means HPA uses a five-minute stabilization period for scale-down decisions.

Conceptually:

```text
Traffic drops

↓

HPA observes lower demand

↓

Wait / stabilize

↓

Scale down
```

---

# Why Stabilization Matters

Without stabilization:

```text
Traffic spike
 ↓
Scale up

Traffic drops
 ↓
Scale down

Traffic spike
 ↓
Scale up

Traffic drops
 ↓
Scale down
```

This creates:

```text
Scaling Thrashing
```

---

# Scale-Up Policies

HPA can control how quickly it scales up.

Example:

```yaml
scaleUp:

  policies:

  - type: Percent

    value: 100

    periodSeconds: 60
```

This allows scaling by a percentage within the configured period.

---

# Scale-Up Pods Policy

You can also use:

```yaml
- type: Pods

  value: 4

  periodSeconds: 60
```

This controls the number of Pods that can be added according to the policy.

---

# Multiple Scaling Policies

Example:

```yaml
scaleUp:

  policies:

  - type: Percent

    value: 100

    periodSeconds: 60

  - type: Pods

    value: 4

    periodSeconds: 60

  selectPolicy: Max
```

The policy selection determines how multiple policies are combined.

---

# Custom Metrics

HPA is not limited to CPU and memory.

It can use:

```text
Custom Metrics
```

Examples:

```text
Requests per second
Queue length
Active connections
Application-specific latency
```

Architecture:

```text
Application

↓

Metrics Adapter

↓

Custom Metrics API

↓

HPA
```

---

# External Metrics

HPA can also use:

```text
External Metrics
```

These are metrics that are not necessarily associated directly with a Kubernetes object.

Examples:

```text
Cloud queue length
Message backlog
External service demand
```

---

# HPA Metric Types

Common HPA metric types include:

```text
Resource
```

```text
Pods
```

```text
Object
```

```text
External
```

Custom metrics can be exposed through Kubernetes metrics APIs.

---

# Resource Metric

Example:

```yaml
type: Resource
```

Used for:

```text
CPU
Memory
```

---

# Pods Metric

The `Pods` metric can scale based on an application-specific metric associated with Pods.

Conceptually:

```text
Requests per Pod

↓

HPA

↓

Replica Count
```

---

# Object Metric

An Object metric can use a metric associated with another Kubernetes object.

Conceptually:

```text
Service / Ingress / Other Object

↓

Metric

↓

HPA
```

---

# External Metric

Example concept:

```text
Cloud Queue

↓

Messages = 10,000

↓

HPA

↓

Increase replicas
```

---

# HPA and Application Load

CPU is not always the best scaling metric.

For example:

```text
Web API
```

may be better scaled based on:

```text
Requests per second
```

A queue worker may be better scaled based on:

```text
Queue length
```

Therefore:

```text
Choose a metric that correlates with actual workload demand.
```

---

# HPA and Resource Requests

Suppose:

```text
CPU request = 100m
```

and:

```text
CPU usage = 80m
```

Utilization:

```text
80 / 100 = 80%
```

If target:

```text
60%
```

HPA may scale out.

Now change request to:

```text
500m
```

with the same usage:

```text
80m
```

Utilization becomes:

```text
80 / 500 = 16%
```

This demonstrates why unrealistic requests can distort utilization-based HPA behavior.

---

# HPA and Limits

HPA primarily uses metrics and targets, not CPU limits, to determine utilization.

For utilization-based CPU or memory scaling:

```text
Actual usage

relative to

Resource Request
```

is especially important.

---

# HPA and ReplicaSets

The hierarchy is:

```text
HPA

↓

Deployment

↓

ReplicaSet

↓

Pods
```

HPA changes the Deployment's desired replica count.

The Deployment then manages the ReplicaSet.

---

# HPA and Services

A Service does not perform autoscaling.

The relationship is:

```text
Service
    ↓
Routes traffic

Deployment
    ↓
Manages Pods

HPA
    ↓
Changes replica count
```

---

# HPA and Load Balancing

Suppose:

```text
2 Pods
```

receive traffic through a Service.

HPA scales:

```text
2 → 5 Pods
```

The Service automatically discovers the additional Pods through EndpointSlice-based service discovery.

Conceptually:

```text
             Service

       ┌───────┼───────┐
       ▼       ▼       ▼
     Pod 1   Pod 2   Pod 3
                       +
                     Pod 4
                     Pod 5
```

---

# HPA and Cluster Autoscaler

HPA:

```text
Changes number of Pods
```

Cluster Autoscaler:

```text
Changes number of Nodes
```

They can work together.

Example:

```text
Traffic increases

↓

HPA increases Pods

↓

Cluster lacks capacity

↓

Some Pods remain Pending

↓

Cluster Autoscaler adds Nodes

↓

Pending Pods become schedulable
```

---

# HPA + Cluster Autoscaler

```text
                Traffic

                   ↓

                  HPA

                   ↓

             More Pods

                   ↓

          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   Capacity Available   Capacity Missing
          │                 │
          ▼                 ▼
       Schedule       Cluster Autoscaler
                            │
                            ▼
                       More Nodes
```

---

# HPA and VPA

HPA:

```text
Horizontal

More/Fewer Pods
```

VPA:

```text
Vertical

More/Fewer Resources per Pod
```

Using both together requires careful design because both can respond to resource usage.

---

# HPA and StatefulSets

HPA can also target supported scalable workloads such as StatefulSets.

However, stateful workloads require more careful consideration because scaling them may involve:

```text
Storage
Replication
Ordering
Application-level clustering
```

---

# HPA Example – Production API

Suppose:

```text
Minimum replicas = 3
Maximum replicas = 20
CPU target = 65%
```

Configuration:

```yaml
apiVersion: autoscaling/v2

kind: HorizontalPodAutoscaler

metadata:

  name: api-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: api

  minReplicas: 3

  maxReplicas: 20

  metrics:

  - type: Resource

    resource:

      name: cpu

      target:

        type: Utilization

        averageUtilization: 65
```

---

# Hands-on Lab 1 – Create Deployment

Create:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: web

spec:

  replicas: 2

  selector:

    matchLabels:

      app: web

  template:

    metadata:

      labels:

        app: web

    spec:

      containers:

      - name: nginx

        image: nginx

        resources:

          requests:

            cpu: "100m"

            memory: "128Mi"

          limits:

            cpu: "500m"

            memory: "256Mi"

        ports:

        - containerPort: 80
```

Apply:

```bash
kubectl apply -f web.yaml
```

---

# Hands-on Lab 2 – Verify Metrics

Run:

```bash
kubectl top pods
```

If metrics are unavailable:

```bash
kubectl get apiservice
```

and:

```bash
kubectl get pods -n kube-system
```

Check the Metrics Server installation.

---

# Hands-on Lab 3 – Create HPA

Create:

```yaml
apiVersion: autoscaling/v2

kind: HorizontalPodAutoscaler

metadata:

  name: web-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: web

  minReplicas: 2

  maxReplicas: 10

  metrics:

  - type: Resource

    resource:

      name: cpu

      target:

        type: Utilization

        averageUtilization: 50
```

Apply:

```bash
kubectl apply -f hpa.yaml
```

Check:

```bash
kubectl get hpa
```

---

# Hands-on Lab 4 – Describe HPA

Run:

```bash
kubectl describe hpa web-hpa
```

Study:

```text
Current Metrics
Desired Replicas
Conditions
Events
```

---

# Hands-on Lab 5 – Generate CPU Load

In a disposable environment, generate CPU load against the application.

Then monitor:

```bash
kubectl get hpa -w
```

and:

```bash
kubectl get deployment web -w
```

Observe:

```text
CPU increases

↓

HPA calculates desired replicas

↓

Deployment scales
```

---

# Hands-on Lab 6 – Observe Scale Down

Stop the artificial workload.

Monitor:

```bash
kubectl get hpa -w
```

Observe that the workload may take time to scale down because HPA uses stabilization and scaling behavior controls.

---

# Hands-on Lab 7 – Configure Scale Behavior

Example:

```yaml
behavior:

  scaleUp:

    stabilizationWindowSeconds: 0

    policies:

    - type: Percent

      value: 100

      periodSeconds: 60

  scaleDown:

    stabilizationWindowSeconds: 300

    policies:

    - type: Percent

      value: 50

      periodSeconds: 60
```

Observe the difference in scaling behavior.

---

# Hands-on Lab 8 – Multiple Metrics

Configure:

```yaml
metrics:

- type: Resource

  resource:

    name: cpu

    target:

      type: Utilization

      averageUtilization: 60

- type: Resource

  resource:

    name: memory

    target:

      type: Utilization

      averageUtilization: 70
```

Observe:

```text
CPU desired replicas
```

and:

```text
Memory desired replicas
```

The HPA uses the highest desired replica count produced by the metrics.

---

# Hands-on Lab 9 – Test HPA Limits

Set:

```yaml
minReplicas: 2

maxReplicas: 5
```

Generate sustained load.

Observe that the Deployment does not scale beyond:

```text
5 replicas
```

---

# Troubleshooting

## HPA Shows Unknown Metrics

Run:

```bash
kubectl get hpa
```

If you see:

```text
<unknown>
```

check:

```bash
kubectl top pods
```

If that also fails, investigate Metrics Server.

---

# Check Metrics API

Run:

```bash
kubectl get apiservice | grep metrics
```

Look for:

```text
v1beta1.metrics.k8s.io
```

The exact API registration depends on the cluster setup.

---

# Check Metrics Server

```bash
kubectl get pods -n kube-system
```

Then:

```bash
kubectl logs -n kube-system deployment/metrics-server
```

---

# Check HPA Events

```bash
kubectl describe hpa <hpa-name>
```

Look at:

```text
Events
```

---

# HPA Does Not Scale

Possible causes:

```text
Metrics unavailable
```

```text
CPU/memory requests missing
```

```text
Target metric misconfigured
```

```text
Already at maxReplicas
```

```text
Already at minReplicas
```

```text
Scaling behavior delaying action
```

---

# HPA Scales Too Aggressively

Possible causes:

```text
Target too low
```

```text
Requests incorrectly sized
```

```text
Unstable workload
```

```text
Scaling policies too aggressive
```

```text
Insufficient stabilization
```

---

# HPA Scales Too Slowly

Possible causes:

```text
Target too high
```

```text
Metrics collection delay
```

```text
Scale-up policies too restrictive
```

```text
Application startup is slow
```

```text
Cluster capacity is insufficient
```

---

# HPA Stuck at maxReplicas

Example:

```text
Current replicas = 10
maxReplicas = 10
```

Check:

```bash
kubectl describe hpa <hpa-name>
```

The application may simply require more capacity than the configured maximum.

Increase `maxReplicas` only after confirming:

```text
Application capacity
Database capacity
Cluster capacity
Downstream dependencies
```

---

# HPA Stuck at minReplicas

Example:

```text
Current replicas = 2
minReplicas = 2
```

This can simply mean:

```text
Current demand is low
```

If load is high but HPA stays at minimum, inspect metrics and configuration.

---

# Common Mistakes

## 1. Forgetting Resource Requests

For CPU/memory utilization targets, missing resource requests can prevent meaningful utilization calculations.

---

## 2. Installing HPA Without Metrics

HPA requires a metrics source.

For resource metrics, Metrics Server is commonly used.

---

## 3. Setting maxReplicas Too Low

Example:

```text
maxReplicas = 3
```

for a workload that needs:

```text
10 Pods
```

The HPA cannot scale beyond 3.

---

## 4. Setting minReplicas Too Low

For production applications, too few replicas can create:

```text
Availability risk
```

during scaling transitions.

---

## 5. Using Unrealistic Requests

HPA utilization is commonly calculated relative to resource requests.

Bad requests can therefore produce misleading scaling behavior.

---

## 6. Scaling Based on the Wrong Metric

CPU may not correlate with application demand.

For a queue worker:

```text
Queue depth
```

may be a better signal.

For an API:

```text
Requests per second
```

may be more meaningful.

---

## 7. Expecting Immediate Scale Down

HPA behavior includes stabilization and scaling policies.

Scale-down is often intentionally conservative.

---

## 8. Fighting HPA with Manual Scaling

Do not repeatedly run:

```bash
kubectl scale deployment ...
```

against a Deployment managed by HPA.

The HPA controller may change the replica count again.

---

## 9. Ignoring Cluster Capacity

HPA can create more Pods than the cluster can currently host.

Those Pods may remain:

```text
Pending
```

Cluster Autoscaler may be required to add capacity.

---

## 10. Ignoring Downstream Bottlenecks

Scaling application Pods does not automatically scale:

```text
Database
Cache
External APIs
Message brokers
```

The application can become faster at generating load against an already overloaded dependency.

---

# HPA vs VPA vs Cluster Autoscaler

| Mechanism | Scales | Direction |
|---|---|---|
| HPA | Pods | Horizontal |
| VPA | Pod resources | Vertical |
| Cluster Autoscaler | Nodes | Cluster capacity |

---

# HPA vs ReplicaSet

ReplicaSet:

```text
Maintains desired number of Pods
```

HPA:

```text
Changes desired number of Pods
```

Relationship:

```text
HPA

↓

Deployment

↓

ReplicaSet

↓

Pods
```

---

# HPA vs Deployment

Deployment manages:

```text
Application rollout
```

HPA manages:

```text
Replica count
```

They work together.

---

# HPA and Rolling Updates

During a Deployment rollout:

```text
Old ReplicaSet
        ↓
New ReplicaSet
```

HPA can continue adjusting the desired replica count.

Therefore production deployment strategies should consider:

```text
HPA
+
Rolling Update
+
PodDisruptionBudget
```

together.

---

# HPA and PodDisruptionBudget

A PodDisruptionBudget can protect application availability during voluntary disruptions.

HPA and PDB solve different problems:

```text
HPA
    ↓
How many replicas should exist?
```

```text
PDB
    ↓
How many Pods should remain available during voluntary disruption?
```

---

# HPA and Readiness

A newly created Pod should not receive production traffic until it is ready.

Therefore:

```text
HPA scales

↓

New Pods start

↓

Readiness Probe

↓

Pod becomes Ready

↓

Service sends traffic
```

Good readiness configuration is important for effective autoscaling.

---

# HPA and Startup Time

If an application takes:

```text
90 seconds
```

to start, rapidly scaling based on short-term load can create problems.

Consider:

```text
Startup probes
Readiness probes
Stabilization windows
Scaling policies
```

---

# HPA and Databases

Be careful when scaling workloads that depend heavily on a database.

Example:

```text
Traffic increases

↓

HPA creates 20 API Pods

↓

All 20 Pods query database

↓

Database becomes overloaded
```

Autoscaling the application can therefore amplify a database bottleneck.

---

# Production Design Example

Suppose:

```text
Application:

3–20 replicas

CPU target:
65%

Memory target:
75%
```

Configuration:

```yaml
apiVersion: autoscaling/v2

kind: HorizontalPodAutoscaler

metadata:

  name: api-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: api

  minReplicas: 3

  maxReplicas: 20

  metrics:

  - type: Resource

    resource:

      name: cpu

      target:

        type: Utilization

        averageUtilization: 65

  - type: Resource

    resource:

      name: memory

      target:

        type: Utilization

        averageUtilization: 75

  behavior:

    scaleUp:

      stabilizationWindowSeconds: 0

    scaleDown:

      stabilizationWindowSeconds: 300
```

This provides:

```text
Minimum availability
        ↓
3 Pods

Elastic capacity
        ↓
Up to 20 Pods

CPU signal
        ↓
65%

Memory signal
        ↓
75%

Conservative scale-down
        ↓
300 seconds
```

---

# Best Practices

### 1. Use `autoscaling/v2`

For modern Kubernetes environments, `autoscaling/v2` provides richer metric and behavior support.

---

### 2. Define Resource Requests

CPU/memory utilization-based HPA depends on meaningful requests.

---

### 3. Set Sensible minReplicas

Ensure enough replicas for:

```text
Availability
Rolling Updates
Failure Tolerance
```

---

### 4. Set maxReplicas Based on Capacity

Consider:

```text
Cluster capacity
Database capacity
Downstream services
Cost
```

---

### 5. Choose Metrics Carefully

Use metrics that correlate with actual workload demand.

---

### 6. Configure Scale Behavior

Use:

```text
scaleUp
scaleDown
stabilizationWindowSeconds
```

to prevent unstable scaling.

---

### 7. Monitor HPA

Use:

```bash
kubectl get hpa
```

and:

```bash
kubectl describe hpa <name>
```

Also monitor the underlying workload.

---

### 8. Combine HPA with Cluster Autoscaler

When HPA can create more Pods than current Nodes can accommodate, Cluster Autoscaler can provide additional capacity.

---

### 9. Test Under Realistic Load

Do not validate autoscaling only with idle workloads.

Test:

```text
Normal traffic
Peak traffic
Traffic spikes
Traffic drops
Dependency failures
```

---

### 10. Avoid Blind Autoscaling

More Pods do not always solve the problem.

Investigate:

```text
CPU
Memory
Database
Network
External APIs
Locks
Queues
```

---

# Quick Revision

## HPA

```text
Automatically changes Pod replica count
```

---

## Horizontal Scaling

```text
More/Fewer Pods
```

---

## Vertical Scaling

```text
More/Fewer Resources per Pod
```

---

## minReplicas

```text
Lower replica boundary
```

---

## maxReplicas

```text
Upper replica boundary
```

---

## Resource Utilization

```text
Actual usage
     ÷
Resource request
     ×
100
```

---

## Multiple Metrics

```text
CPU desired = 5

Memory desired = 7

↓

HPA chooses 7
```

---

## Metrics Server

```text
Collects resource metrics

↓

Metrics API

↓

HPA
```

---

# Essential kubectl Commands

View HPA:

```bash
kubectl get hpa
```

Watch HPA:

```bash
kubectl get hpa -w
```

Describe HPA:

```bash
kubectl describe hpa <name>
```

View Pods:

```bash
kubectl get pods -o wide
```

Watch Deployment:

```bash
kubectl get deployment <name> -w
```

View resource usage:

```bash
kubectl top pods
```

View Node usage:

```bash
kubectl top nodes
```

Check Metrics Server:

```bash
kubectl get pods -n kube-system
```

Check Metrics API:

```bash
kubectl get apiservice
```

---

# Interview Questions

## Basic

- What is HPA?
- Why is HPA used?
- What is horizontal scaling?
- What is the difference between horizontal and vertical scaling?
- What are `minReplicas` and `maxReplicas`?
- What is `scaleTargetRef`?

---

## Intermediate

- How does HPA calculate CPU utilization?
- Why are resource requests important for HPA?
- What is Metrics Server?
- Can HPA scale based on memory?
- Can HPA use multiple metrics?
- What is `autoscaling/v2`?
- What is HPA stabilization?
- What is the difference between scale-up and scale-down behavior?

---

## Advanced

- Explain the complete HPA control loop.
- Explain how HPA calculates desired replicas.
- How does HPA behave when multiple metrics are configured?
- Why might an HPA show `<unknown>`?
- How would you troubleshoot an HPA that does not scale?
- How does HPA interact with Cluster Autoscaler?
- How does HPA interact with VPA?
- Why can incorrect CPU requests cause unexpected HPA behavior?
- When would CPU be a poor autoscaling metric?
- How would you scale a queue-processing application?
- How can aggressive HPA configuration cause scaling thrashing?
- How would you design HPA for a high-traffic production API?
- What happens if HPA wants 20 replicas but the cluster has capacity for only 10?
- How do readiness probes affect autoscaling workloads?

---

# Production Architecture

A typical production autoscaling architecture can look like:

```text
                  User Traffic

                       │
                       ▼
                  Load Balancer

                       │
                       ▼
                    Service

                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Pod 1        Pod 2        Pod 3
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  Application

                       │
                       ▼
                Resource Metrics

                       │
                       ▼
                Metrics Server

                       │
                       ▼
                      HPA

                       │
                       ▼
             Desired Replica Count

                       │
                       ▼
                  Deployment

                       │
                       ▼
                  ReplicaSet

                       │
                       ▼
                 More / Fewer Pods
```

When cluster capacity becomes insufficient:

```text
HPA

↓

More Pods

↓

Pods Pending

↓

Cluster Autoscaler

↓

More Nodes

↓

Pods Scheduled
```

---

# Real-World Scaling Example

Suppose an API normally runs:

```text
3 replicas
```

During a traffic spike:

```text
CPU = 85%
Target = 60%
```

HPA calculates that more replicas are required.

It may scale:

```text
3
 ↓
5
```

Traffic continues increasing:

```text
5
 ↓
8
```

Eventually:

```text
maxReplicas = 10
```

so:

```text
10
```

becomes the upper boundary.

When traffic decreases:

```text
85%
 ↓
50%
 ↓
30%
```

HPA gradually scales down according to the configured behavior.

---

# Recommended Practice

1. Deploy a sample application.
2. Define CPU and memory requests.
3. Install or verify Metrics Server.
4. Create an HPA using `autoscaling/v2`.
5. Configure `minReplicas`.
6. Configure `maxReplicas`.
7. Set a CPU target.
8. Generate CPU load.
9. Watch HPA scale out.
10. Stop the load.
11. Observe scale-down behavior.
12. Configure stabilization windows.
13. Test multiple metrics.
14. Experiment with scale-up policies.
15. Test HPA with Cluster Autoscaler if available.
16. Troubleshoot an intentionally broken metrics configuration.
17. Test an application whose startup time is slow.
18. Analyze whether CPU is actually the right scaling signal.

---

# References

## Official Kubernetes Documentation

- Horizontal Pod Autoscaling
- HorizontalPodAutoscaler API
- Autoscaling Concepts
- Metrics APIs
- Resource Metrics Pipeline
- Resource Management for Pods and Containers
- Deployments
- Pod Lifecycle

---

## CNCF Resources

- Kubernetes SIG Autoscaling
- Kubernetes SIG Instrumentation
- Kubernetes Scheduling
- Cloud Native Computing Foundation (CNCF)

---

# Chapter Summary

HPA allows Kubernetes to automatically adjust the number of Pod replicas based on workload demand.

The basic control loop is:

```text
Application Load

      ↓

Resource / Custom Metrics

      ↓

HPA

      ↓

Desired Replica Count

      ↓

Deployment

      ↓

ReplicaSet

      ↓

Pods
```

The most important HPA configuration is:

```yaml
scaleTargetRef:
```

which identifies the workload being scaled.

```yaml
minReplicas:
```

defines the lower boundary.

```yaml
maxReplicas:
```

defines the upper boundary.

And:

```yaml
metrics:
```

defines what HPA uses to determine scaling demand.

For CPU utilization:

```text
Utilization
    =
Actual CPU Usage
----------------
CPU Request
    × 100
```

This is why resource requests must be realistic.

HPA can use:

```text
CPU
Memory
Pod Metrics
Object Metrics
External Metrics
Custom Metrics
```

For multiple metrics:

```text
CPU → Desired replicas = 5

Memory → Desired replicas = 7

             ↓

HPA → 7 replicas
```

HPA controls:

```text
Pod count
```

while:

```text
VPA
```

controls:

```text
Pod resource sizing
```

and:

```text
Cluster Autoscaler
```

controls:

```text
Node count
```

A production autoscaling architecture therefore often looks like:

```text
              HPA
               │
               ▼
          More Pods
               │
               ▼
      Cluster Capacity
               │
       ┌───────┴───────┐
       ▼               ▼
   Capacity        No Capacity
   Available            │
       │                ▼
       ▼        Cluster Autoscaler
   Schedule             │
                        ▼
                   More Nodes
```

The most important production principle is:

> **Autoscale based on a metric that actually represents workload demand, not simply because a metric is available.**

For a CPU-intensive application, CPU may be appropriate.

For a queue worker:

```text
Queue depth
```

may be better.

For an API:

```text
Requests per second
```

may be more meaningful.

For a latency-sensitive service:

```text
Request latency
```

may be useful when exposed through an appropriate metrics system.

HPA is therefore not simply:

```text
High CPU → More Pods
```

It is a control loop that continuously evaluates:

```text
Demand
  ↓
Metrics
  ↓
Desired Capacity
  ↓
Replica Count
  ↓
Observed Performance
  ↓
Repeat
```

A well-designed HPA configuration should also consider:

```text
Resource Requests
Min Replicas
Max Replicas
Scaling Policies
Stabilization
Readiness
Startup Time
Cluster Capacity
Database Capacity
Downstream Dependencies
```

This makes HPA an important foundation for building elastic Kubernetes applications.

---

## Next Chapter

# Chapter 44 – Vertical Pod Autoscaler (VPA)

Topics will include:

- What is VPA?
- Why VPA is needed
- Horizontal vs Vertical Autoscaling
- VPA Architecture
- VPA Components
- Recommender
- Updater
- Admission Controller
- VPA Modes
- `Off`
- `Initial`
- `Recreate`
- `Auto`
- Resource Recommendations
- CPU Recommendations
- Memory Recommendations
- VPA and Resource Requests
- VPA and Limits
- VPA with HPA
- VPA with Cluster Autoscaler
- VPA Limitations
- Production Considerations
- Hands-on Labs
- Common Mistakes
- Troubleshooting
- Quick Revision
- Interview Questions
- References

---