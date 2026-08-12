# Chapter 42 – Resource Requests & Limits

## Overview

Kubernetes runs multiple workloads across shared cluster infrastructure.

Each Node has finite resources such as:

```text
CPU
Memory
```

If Kubernetes does not know how much resource a Pod requires, the Scheduler cannot make reliable placement decisions.

Kubernetes therefore provides:

```text
Resource Requests
```

and:

```text
Resource Limits
```

These mechanisms control how much CPU and memory containers request and are allowed to consume.

The basic relationship is:

```text
Resource Request
        ↓
Used primarily for scheduling

Resource Limit
        ↓
Used primarily for runtime enforcement
```

For example:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "512Mi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

This means:

```text
CPU request  = 0.5 CPU
CPU limit    = 1 CPU

Memory request = 512 MiB
Memory limit   = 1 GiB
```

> **Requests influence where a Pod can be scheduled; limits define runtime resource ceilings.**

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes resource management
- CPU resources
- Memory resources
- Resource requests
- Resource limits
- How the Scheduler uses requests
- CPU units
- Memory units
- Requests vs limits
- CPU throttling
- Memory OOM behavior
- Quality of Service classes
- Guaranteed QoS
- Burstable QoS
- BestEffort QoS
- LimitRange
- ResourceQuota
- Namespace resource management
- Container-level resource configuration
- Pod-level resource configuration
- Resource overcommitment
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices

---

# Why Are Resource Requests Needed?

Suppose a Node has:

```text
CPU = 8
Memory = 16Gi
```

Three Pods are already running:

```text
Pod A
CPU request = 2
Memory request = 4Gi
```

```text
Pod B
CPU request = 2
Memory request = 2Gi
```

```text
Pod C
CPU request = 1
Memory request = 2Gi
```

Total requested CPU:

```text
2 + 2 + 1 = 5 CPU
```

Total requested memory:

```text
4 + 2 + 2 = 8Gi
```

A new Pod requests:

```text
CPU = 2
Memory = 4Gi
```

The Scheduler can determine whether sufficient allocatable capacity remains.

---

# Why Are Resource Limits Needed?

A container might consume significantly more CPU or memory than expected.

For example:

```text
Application normally uses:

CPU = 0.5

Memory = 512Mi
```

But due to a bug:

```text
Memory = 8Gi
```

If the container has no appropriate limit, it can consume excessive resources and affect other workloads.

Limits provide runtime boundaries.

---

# Resource Types

Kubernetes primarily manages:

```text
CPU
Memory
```

Other resources can also exist, including:

```text
Ephemeral Storage
```

and extended resources such as:

```text
nvidia.com/gpu
```

The core concepts in this chapter focus on CPU and memory.

---

# CPU Resources

CPU is represented using CPU units.

Examples:

```text
1
```

means:

```text
1 CPU
```

```text
500m
```

means:

```text
0.5 CPU
```

```text
250m
```

means:

```text
0.25 CPU
```

---

# CPU Units

Common examples:

| Value | Meaning |
|---|---:|
| `1` | 1 CPU |
| `500m` | 0.5 CPU |
| `250m` | 0.25 CPU |
| `100m` | 0.1 CPU |
| `50m` | 0.05 CPU |

The `m` stands for:

```text
milliCPU
```

---

# CPU Example

```yaml
resources:

  requests:

    cpu: "500m"

  limits:

    cpu: "1"
```

Meaning:

```text
Request:

0.5 CPU
```

```text
Limit:

1 CPU
```

---

# Memory Resources

Memory is commonly expressed using binary units such as:

```text
Ki
Mi
Gi
Ti
```

Examples:

```text
128Mi
512Mi
1Gi
2Gi
```

---

# Memory Units

Common examples:

| Value | Approximate Binary Size |
|---|---:|
| `128Mi` | 128 MiB |
| `256Mi` | 256 MiB |
| `512Mi` | 512 MiB |
| `1Gi` | 1 GiB |
| `2Gi` | 2 GiB |

Kubernetes also accepts decimal SI units such as:

```text
M
G
```

but it is important to understand the distinction between decimal and binary units.

---

# CPU vs Memory

CPU is generally a compressible resource.

If CPU demand increases:

```text
CPU contention
```

can lead to throttling or reduced CPU availability.

Memory is not compressible in the same way.

If memory demand exceeds available memory:

```text
OOM
```

can occur.

This distinction is extremely important.

---

# Resource Requests

A request represents the amount of a resource that the container expects to require for scheduling purposes.

Example:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "512Mi"
```

The Scheduler uses requests when determining whether a Pod can fit on a Node.

---

# Resource Limits

A limit defines the maximum resource amount the container can consume according to the resource's runtime enforcement semantics.

Example:

```yaml
resources:

  limits:

    cpu: "1"

    memory: "1Gi"
```

---

# Complete Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: resource-demo

spec:

  containers:

  - name: nginx

    image: nginx

    resources:

      requests:

        cpu: "500m"

        memory: "256Mi"

      limits:

        cpu: "1"

        memory: "512Mi"
```

---

# Request vs Limit

| Resource | Request | Limit |
|---|---|---|
| CPU | Scheduling baseline | Runtime ceiling |
| Memory | Scheduling baseline | Runtime ceiling |
| Used by Scheduler | Yes | Not as the primary scheduling value |
| Can exceed request? | Runtime may use more if allowed | Cannot exceed configured limit under normal enforcement |
| Purpose | Placement | Resource control |

---

# Important Rule

A common relationship is:

```text
request <= limit
```

For example:

```yaml
requests:

  cpu: "500m"

limits:

  cpu: "1"
```

is valid.

---

# Can Request Equal Limit?

Yes.

Example:

```yaml
resources:

  requests:

    cpu: "1"

    memory: "1Gi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

This configuration is important for the **Guaranteed QoS** classification when applied consistently across all containers in the Pod for CPU and memory.

---

# Can Request Be Lower Than Limit?

Yes.

Example:

```yaml
requests:

  cpu: "250m"

limits:

  cpu: "1"
```

This allows the container to request:

```text
0.25 CPU
```

for scheduling while potentially using up to:

```text
1 CPU
```

at runtime.

---

# What Happens If Request Is Missing?

If a request is not explicitly specified, Kubernetes may derive a request from a configured limit in certain situations, particularly when a `LimitRange` applies.

Without such configuration, the request may remain unset.

Therefore, cluster policy matters.

---

# What Happens If Limit Is Missing?

A container can have a request without a limit.

Example:

```yaml
requests:

  cpu: "500m"
```

Whether an effective limit exists can depend on:

- Explicit configuration
- Namespace `LimitRange`
- Cluster defaults

Always inspect the resulting Pod specification when troubleshooting.

---

# Scheduler and Requests

Suppose a Node has:

```text
Allocatable CPU = 8
```

Existing Pods request:

```text
Pod A = 2
Pod B = 2
Pod C = 1
```

Total:

```text
5 CPU
```

New Pod requests:

```text
3 CPU
```

Then:

```text
5 + 3 = 8
```

The Node can satisfy the CPU requests assuming other scheduling requirements also pass.

---

# Actual Usage vs Requests

Suppose:

```text
Node:

8 CPU
```

Pods:

```text
Request = 1 CPU
Actual = 0.2 CPU
```

The Scheduler does not simply assume:

```text
Only 0.2 CPU is reserved
```

It uses the declared request for scheduling capacity.

Therefore:

```text
Request

↓

Scheduling reservation/accounting
```

while:

```text
Actual usage

↓

Runtime behavior
```

---

# Why Accurate Requests Matter

If requests are too low:

```text
Cluster appears to have more capacity than it really should allocate
```

This can lead to:

- CPU contention
- Memory pressure
- Poor performance
- Unexpected evictions
- Overcommitment

If requests are too high:

```text
Pods require more declared capacity
```

which can cause:

- Poor bin packing
- More Nodes required
- Higher infrastructure cost
- Pods remaining Pending unnecessarily

---

# CPU Limits

CPU limits are generally enforced through CPU scheduling controls.

If a container attempts to use more CPU than its limit:

```text
CPU demand

↓

Limit enforcement

↓

CPU throttling
```

The container normally remains running but receives limited CPU time.

---

# CPU Throttling

Example:

```yaml
limits:

  cpu: "500m"
```

If the workload wants:

```text
1 CPU
```

the runtime may throttle it to approximately the configured limit over time.

This can affect:

- Latency
- Throughput
- Response time
- Performance-sensitive applications

---

# CPU Requests and Bursting

Suppose:

```yaml
requests:

  cpu: "250m"

limits:

  cpu: "1"
```

The container requests:

```text
0.25 CPU
```

but may use up to:

```text
1 CPU
```

when capacity is available.

This creates:

```text
Bursting
```

---

# Memory Limits

Memory is different.

Suppose:

```yaml
limits:

  memory: "512Mi"
```

and the container attempts to use more than its memory limit.

The container can be terminated due to:

```text
OOMKilled
```

depending on the circumstances and system behavior.

---

# OOMKilled

OOM means:

```text
Out Of Memory
```

Example:

```text
Memory Limit = 512Mi

Application usage > 512Mi
```

The container may be terminated.

Check:

```bash
kubectl describe pod <pod-name>
```

Look for:

```text
Reason: OOMKilled
```

---

# Memory Is Not Compressible

CPU:

```text
Can be throttled
```

Memory:

```text
Cannot simply be throttled indefinitely
```

When memory becomes unavailable, Linux/Kubernetes memory pressure mechanisms may result in:

```text
OOM termination
```

or:

```text
Pod eviction
```

depending on the situation.

---

# Resource Requests and QoS

Kubernetes assigns Pods a QoS class based on their resource requests and limits.

The major classes are:

```text
Guaranteed
```

```text
Burstable
```

```text
BestEffort
```

---

# Guaranteed QoS

A Pod generally receives `Guaranteed` QoS when:

- Every container has CPU and memory limits.
- For every container, CPU request equals CPU limit.
- For every container, memory request equals memory limit.

Example:

```yaml
resources:

  requests:

    cpu: "1"

    memory: "1Gi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

For a multi-container Pod, the condition applies to every relevant container.

---

# Guaranteed Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: guaranteed-demo

spec:

  containers:

  - name: app

    image: nginx

    resources:

      requests:

        cpu: "500m"

        memory: "512Mi"

      limits:

        cpu: "500m"

        memory: "512Mi"
```

This is a Guaranteed QoS configuration.

---

# Burstable QoS

A Pod generally receives `Burstable` QoS when it has resource requests or limits but does not meet all the conditions required for Guaranteed.

Example:

```yaml
resources:

  requests:

    cpu: "250m"

    memory: "256Mi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

Here:

```text
Request < Limit
```

so the Pod is not Guaranteed.

---

# BestEffort QoS

A Pod generally receives `BestEffort` QoS when none of its containers specify CPU or memory requests or limits.

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: besteffort-demo

spec:

  containers:

  - name: nginx

    image: nginx
```

No CPU or memory resources are specified.

---

# QoS Comparison

| QoS | Requests/Limits | Typical Characteristics |
|---|---|---|
| Guaranteed | Requests = Limits for CPU and memory on all containers | Strongest resource guarantees |
| Burstable | Some resource configuration, but not Guaranteed | Flexible |
| BestEffort | No CPU/memory requests or limits | Lowest resource guarantees |

---

# QoS and Eviction

During Node memory pressure, Kubernetes uses QoS and other factors when determining which Pods are more vulnerable to eviction.

Generally:

```text
BestEffort
```

is more vulnerable than:

```text
Burstable
```

and:

```text
Guaranteed
```

However, actual eviction behavior also considers:

- Pod priority
- Resource usage relative to requests
- Node conditions
- Eviction thresholds
- Other Kubernetes policies

Do not treat QoS as the only eviction factor.

---

# Priority vs QoS

This distinction is important.

Priority:

```text
How important is this Pod?
```

QoS:

```text
How are this Pod's CPU/memory resources configured?
```

A Pod can be:

```text
Guaranteed + Low Priority
```

or:

```text
Burstable + High Priority
```

These are independent concepts.

---

# ResourceQuota

A namespace can have a total resource quota.

Example:

```yaml
apiVersion: v1

kind: ResourceQuota

metadata:

  name: compute-quota

spec:

  hard:

    requests.cpu: "10"

    requests.memory: 20Gi

    limits.cpu: "20"

    limits.memory: 40Gi
```

This limits the aggregate resources requested/limited by workloads in the namespace according to the quota configuration.

---

# Why ResourceQuota Matters

Without quotas:

```text
One namespace

↓

Can potentially consume excessive cluster resources
```

With quotas:

```text
Namespace

↓

Controlled resource consumption
```

---

# Checking ResourceQuota

```bash
kubectl get resourcequota
```

Describe:

```bash
kubectl describe resourcequota compute-quota
```

---

# LimitRange

A `LimitRange` can define default or minimum/maximum resource constraints for containers in a namespace.

Example:

```yaml
apiVersion: v1

kind: LimitRange

metadata:

  name: resource-limits

spec:

  limits:

  - type: Container

    default:

      cpu: "1"

      memory: "512Mi"

    defaultRequest:

      cpu: "250m"

      memory: "256Mi"

    max:

      cpu: "2"

      memory: "2Gi"

    min:

      cpu: "100m"

      memory: "128Mi"
```

---

# LimitRange Purpose

A LimitRange can enforce:

```text
Minimum resource values
Maximum resource values
Default requests
Default limits
```

This is useful for namespace-level governance.

---

# ResourceQuota vs LimitRange

| ResourceQuota | LimitRange |
|---|---|
| Controls aggregate namespace usage | Controls individual resource settings |
| Namespace level | Namespace level |
| Limits total requests/limits | Sets defaults and min/max constraints |
| Prevents namespace overconsumption | Enforces resource policy |

---

# Container-Level Resources

Resources are commonly configured at the container level.

Example:

```yaml
containers:

- name: app

  image: nginx

  resources:

    requests:

      cpu: "500m"

      memory: "512Mi"

    limits:

      cpu: "1"

      memory: "1Gi"
```

---

# Multi-Container Pod

Suppose a Pod has:

```text
Container A
CPU request = 500m

Container B
CPU request = 250m
```

Total Pod CPU request is approximately:

```text
500m + 250m = 750m
```

The Scheduler considers the aggregate resource requirements of the Pod.

---

# Example

```yaml
containers:

- name: app

  image: nginx

  resources:

    requests:

      cpu: "500m"

      memory: "512Mi"

- name: sidecar

  image: busybox

  resources:

    requests:

      cpu: "100m"

      memory: "128Mi"
```

Total requests:

```text
CPU = 600m

Memory = 640Mi
```

---

# Pod-Level Resource Configuration

Modern Kubernetes versions can support Pod-level resource declarations depending on the enabled feature set and API behavior.

The traditional and most widely encountered pattern remains:

```text
Container resources

↓

Pod aggregate
```

When using Pod-level resource features, always verify the Kubernetes version and feature availability in your cluster.

---

# Ephemeral Storage

Kubernetes can also manage:

```text
ephemeral-storage
```

Example:

```yaml
resources:

  requests:

    ephemeral-storage: "1Gi"

  limits:

    ephemeral-storage: "2Gi"
```

This controls local ephemeral storage requests and limits for containers.

---

# Extended Resources

Specialized hardware can be exposed as extended resources.

Example:

```yaml
resources:

  limits:

    nvidia.com/gpu: 1
```

This is different from CPU and memory and typically depends on a device plugin.

---

# Resource Overcommitment

Suppose a Node has:

```text
CPU = 8
```

Pods collectively request:

```text
CPU = 8
```

but limits collectively equal:

```text
CPU = 16
```

This represents CPU overcommitment at the limit level.

The cluster assumes not all workloads will necessarily consume their maximum CPU simultaneously.

---

# Overcommitment Example

```text
Node CPU = 8

Pod A
Request = 2
Limit = 4

Pod B
Request = 2
Limit = 4

Pod C
Request = 2
Limit = 4

Pod D
Request = 2
Limit = 4
```

Total:

```text
Requests = 8 CPU

Limits = 16 CPU
```

This can be valid depending on cluster policy.

---

# Memory Overcommitment

Memory overcommitment is more dangerous.

Example:

```text
Node memory = 16Gi
```

Pods:

```text
Requests = 16Gi
Limits = 32Gi
```

If many containers simultaneously approach their limits:

```text
Memory pressure
```

can occur.

This can lead to:

```text
OOM
```

or:

```text
Evictions
```

---

# Resource Sizing Strategy

A practical approach is:

```text
Measure actual usage

↓

Estimate normal usage

↓

Set realistic request

↓

Set appropriate limit

↓

Monitor

↓

Tune
```

---

# Right-Sizing

Suppose monitoring shows:

```text
Typical CPU:
200m

Peak CPU:
700m
```

A possible configuration could be:

```yaml
requests:

  cpu: "250m"

limits:

  cpu: "1"
```

The exact values should be based on real workload behavior.

---

# Memory Right-Sizing

Suppose:

```text
Normal memory:
400Mi

Peak:
800Mi
```

Potential configuration:

```yaml
requests:

  memory: "512Mi"

limits:

  memory: "1Gi"
```

Again, production values should be based on measured behavior and safety margin.

---

# Requests Too High

Example:

```text
Application normally uses:

100m CPU
```

but request is:

```text
2 CPU
```

Result:

```text
Scheduler sees:

2 CPU reserved
```

This can waste cluster capacity.

---

# Requests Too Low

Example:

```text
Application normally uses:

1 CPU
```

but request is:

```text
100m
```

Result:

```text
Scheduler assumes:

0.1 CPU
```

The Node can become heavily overcommitted.

---

# Limits Too Low

If a workload requires:

```text
1 CPU
```

but limit is:

```text
100m
```

it may experience:

```text
CPU throttling
```

and poor performance.

---

# Memory Limit Too Low

If the application requires:

```text
1Gi
```

but the limit is:

```text
256Mi
```

the container may repeatedly hit:

```text
OOMKilled
```

---

# Troubleshooting Resource Problems

Check:

```bash
kubectl describe pod <pod-name>
```

Check:

```bash
kubectl get pod <pod-name> -o yaml
```

Look at:

```text
resources.requests
resources.limits
```

---

# Check Pod Status

```bash
kubectl get pods
```

Look for:

```text
OOMKilled
```

or:

```text
CrashLoopBackOff
```

---

# Check Previous Container State

```bash
kubectl describe pod <pod-name>
```

and:

```bash
kubectl get pod <pod-name> \
-o jsonpath='{.status.containerStatuses[*].lastState}'
```

---

# Metrics

If Metrics Server is installed:

```bash
kubectl top pods
```

and:

```bash
kubectl top nodes
```

can help compare actual usage with requests and limits.

Remember:

```text
kubectl top

↓

Current observed usage

```

while:

```text
resources.requests

↓

Declared scheduling requirement
```

---

# Hands-on Lab 1 – Resource Requests

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: requests-demo

spec:

  containers:

  - name: nginx

    image: nginx

    resources:

      requests:

        cpu: "500m"

        memory: "256Mi"
```

Apply:

```bash
kubectl apply -f requests-demo.yaml
```

Inspect:

```bash
kubectl describe pod requests-demo
```

---

# Hands-on Lab 2 – Requests and Limits

Create:

```yaml
resources:

  requests:

    cpu: "250m"

    memory: "256Mi"

  limits:

    cpu: "1"

    memory: "512Mi"
```

Inspect:

```bash
kubectl get pod <pod-name> -o yaml
```

---

# Hands-on Lab 3 – Guaranteed QoS

Create:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "512Mi"

  limits:

    cpu: "500m"

    memory: "512Mi"
```

Check:

```bash
kubectl get pod <pod-name> \
-o jsonpath='{.status.qosClass}'
```

Expected:

```text
Guaranteed
```

---

# Hands-on Lab 4 – Burstable QoS

Use:

```yaml
resources:

  requests:

    cpu: "250m"

    memory: "256Mi"

  limits:

    cpu: "1"

    memory: "512Mi"
```

Check:

```bash
kubectl get pod <pod-name> \
-o jsonpath='{.status.qosClass}'
```

Expected:

```text
Burstable
```

---

# Hands-on Lab 5 – BestEffort QoS

Create a Pod without:

```text
requests
```

or:

```text
limits
```

Then:

```bash
kubectl get pod <pod-name> \
-o jsonpath='{.status.qosClass}'
```

Expected:

```text
BestEffort
```

---

# Hands-on Lab 6 – LimitRange

Create:

```yaml
apiVersion: v1

kind: LimitRange

metadata:

  name: lab-limits

spec:

  limits:

  - type: Container

    default:

      cpu: "1"

      memory: "512Mi"

    defaultRequest:

      cpu: "250m"

      memory: "256Mi"
```

Apply:

```bash
kubectl apply -f limitrange.yaml
```

Create a Pod without resource settings.

Inspect its resulting configuration.

---

# Hands-on Lab 7 – ResourceQuota

Create:

```yaml
apiVersion: v1

kind: ResourceQuota

metadata:

  name: lab-quota

spec:

  hard:

    requests.cpu: "2"

    requests.memory: 2Gi

    limits.cpu: "4"

    limits.memory: 4Gi
```

Apply:

```bash
kubectl apply -f quota.yaml
```

Inspect:

```bash
kubectl describe resourcequota lab-quota
```

---

# Hands-on Lab 8 – CPU Stress Test

In a disposable lab environment, deploy a CPU-intensive container with a CPU limit.

Observe:

```text
CPU usage

↓

Limit

↓

Potential throttling
```

Use:

```bash
kubectl top pod
```

if Metrics Server is available.

---

# Hands-on Lab 9 – Memory Limit Test

In a disposable environment, run a workload that intentionally consumes more memory than its configured limit.

Observe:

```text
OOMKilled
```

Check:

```bash
kubectl describe pod <pod-name>
```

Do not perform destructive resource tests on production workloads.

---

# Common Mistakes

## 1. Confusing Requests and Limits

Remember:

```text
Request
    ↓
Scheduling

Limit
    ↓
Runtime ceiling
```

---

## 2. Setting Requests Too Low

This can cause:

```text
Overcommitment
```

and poor scheduling decisions.

---

## 3. Setting Requests Too High

This can result in:

```text
Poor bin packing
```

and unnecessary Node scaling.

---

## 4. Setting Memory Limits Too Low

This can cause:

```text
OOMKilled
```

---

## 5. Setting CPU Limits Too Low

This can cause:

```text
CPU throttling
```

and latency problems.

---

## 6. Assuming CPU and Memory Behave the Same Way

They do not.

```text
CPU
    ↓
Can be throttled
```

```text
Memory
    ↓
Can trigger OOM/eviction
```

---

## 7. Ignoring Multi-Container Pods

The Scheduler considers the aggregate resource requirements of the Pod.

---

## 8. Forgetting LimitRange

Namespace policies can automatically provide defaults or reject invalid resource configurations.

Always inspect:

```bash
kubectl get limitrange
```

---

## 9. Ignoring ResourceQuota

A Pod may be correctly configured but still fail admission because the namespace has insufficient quota.

---

## 10. Confusing Priority with Resource Capacity

High priority does not create additional CPU or memory.

---

# Requests and Limits vs Priority

```text
Requests

↓

How much resource does the Pod need?
```

```text
Priority

↓

How important is the Pod?
```

For example:

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

Pod B is more important but does not require more CPU.

---

# Resource Management Architecture

```text
                    Pod

                     │
                     ▼

             Resource Requests
                     │
                     ▼
                 Scheduler
                     │
                     ▼
                    Node
                     │
                     ▼
              Resource Allocation
                     │
                     ▼
             Container Runtime
                     │
                     ▼
            Runtime Enforcement
                     │
              ┌──────┴──────┐
              ▼             ▼
             CPU          Memory
              │             │
          Throttling       OOM
```

---

# Production Resource Strategy

A production workload should generally have carefully considered:

```text
CPU Request
Memory Request
CPU Limit
Memory Limit
```

Example:

```yaml
resources:

  requests:

    cpu: "250m"

    memory: "512Mi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

The correct values depend on:

- Application behavior
- Traffic
- Latency requirements
- Peak usage
- JVM/runtime behavior
- Garbage collection
- Batch vs interactive workload
- Node capacity

---

# Resource Requests and Autoscaling

Resource requests are important for autoscaling.

For example, HPA can use CPU utilization relative to requested CPU.

If:

```text
CPU request = 500m
```

and observed usage is:

```text
250m
```

then utilization is approximately:

```text
50%
```

This becomes important in the next autoscaling chapter.

---

# Resource Requests and Cluster Autoscaler

Cluster Autoscaler can use unschedulable Pods and their resource requests when determining whether additional Nodes are needed.

Therefore:

```text
Pod Requests

↓

Scheduling

↓

Cluster Autoscaler
```

Resource requests are an important input to cluster capacity planning.

---

# Quick Revision

## Request

```text
Used primarily for scheduling
```

---

## Limit

```text
Runtime resource ceiling
```

---

## CPU

```text
Can be throttled
```

---

## Memory

```text
Can trigger OOM
```

---

## QoS

```text
Guaranteed
Burstable
BestEffort
```

---

## LimitRange

```text
Namespace-level resource defaults and constraints
```

---

## ResourceQuota

```text
Namespace-level aggregate resource limits
```

---

# Essential kubectl Commands

View Pod resources:

```bash
kubectl get pod <pod> -o yaml
```

Describe Pod:

```bash
kubectl describe pod <pod>
```

View Node resources:

```bash
kubectl describe node <node>
```

View current usage:

```bash
kubectl top pods
```

View Node usage:

```bash
kubectl top nodes
```

View QoS:

```bash
kubectl get pod <pod> \
-o jsonpath='{.status.qosClass}'
```

View LimitRanges:

```bash
kubectl get limitrange
```

View ResourceQuotas:

```bash
kubectl get resourcequota
```

Describe ResourceQuota:

```bash
kubectl describe resourcequota <name>
```

---

# Interview Questions

## Basic

- What are resource requests?
- What are resource limits?
- Why are requests important for Kubernetes scheduling?
- What is the difference between CPU and memory resources?
- What does `500m` CPU mean?
- What does `512Mi` memory mean?

---

## Intermediate

- What is the difference between requests and limits?
- How does the Scheduler use resource requests?
- What happens when a container exceeds its CPU limit?
- What happens when a container exceeds its memory limit?
- What is OOMKilled?
- What are Kubernetes QoS classes?
- What is the difference between Guaranteed, Burstable, and BestEffort?
- What is a LimitRange?
- What is a ResourceQuota?

---

## Advanced

- Explain how Kubernetes schedules Pods using resource requests.
- Why can incorrect requests lead to inefficient cluster utilization?
- Explain CPU throttling.
- Explain how memory pressure differs from CPU pressure.
- How do resource requests affect HPA?
- How do resource requests affect Cluster Autoscaler?
- How would you right-size resource requests and limits?
- What happens when a namespace ResourceQuota is exhausted?
- How do LimitRange and ResourceQuota work together?
- Explain how QoS and Pod Priority interact during resource pressure.
- Why should production workloads avoid blindly setting extremely high limits?
- How would you troubleshoot repeated `OOMKilled` containers?
- How would you troubleshoot CPU throttling and latency?

---

# Production Design Example

Consider:

```text
Application
    ↓
Production API
```

Observed usage:

```text
Normal CPU:
200m

Peak CPU:
700m

Normal Memory:
450Mi

Peak Memory:
850Mi
```

Potential initial configuration:

```yaml
resources:

  requests:

    cpu: "250m"

    memory: "512Mi"

  limits:

    cpu: "1"

    memory: "1Gi"
```

Then:

```text
Deploy

↓

Monitor

↓

Compare actual usage

↓

Tune requests/limits

↓

Repeat
```

This is preferable to guessing permanently.

---

# Best Practices

### 1. Always Define Requests for Production Workloads

Accurate requests improve scheduling and capacity planning.

---

### 2. Size Requests Based on Measurements

Use real usage data whenever possible.

---

### 3. Avoid Extremely Low Requests

They can cause excessive overcommitment.

---

### 4. Avoid Extremely High Requests

They waste schedulable capacity.

---

### 5. Be Careful with CPU Limits

Very restrictive CPU limits can cause throttling and application latency.

---

### 6. Set Appropriate Memory Limits

Memory limits should provide enough headroom for normal and expected peak usage.

---

### 7. Monitor OOMKilled Events

Repeated OOM kills usually require investigation rather than simply increasing limits blindly.

---

### 8. Use LimitRange for Namespace Governance

Provide sensible defaults and enforce minimum/maximum values where appropriate.

---

### 9. Use ResourceQuota for Multi-Tenant Clusters

Prevent one namespace from consuming unlimited resources.

---

### 10. Review Resource Settings Regularly

Workloads change over time.

Resource configurations should be periodically re-evaluated.

---

# References

## Official Kubernetes Documentation

- Resource Management for Pods and Containers
- Assign Memory Resources to Containers and Pods
- Assign CPU Resources to Containers and Pods
- Configure Default Memory Requests and Limits for a Namespace
- Configure Default CPU Requests and Limits for a Namespace
- Limit Ranges
- Resource Quotas
- Pod Quality of Service Classes
- Node-pressure Eviction

---

## CNCF Resources

- Kubernetes Resource Management
- Kubernetes Scheduling
- Kubernetes SIG Node
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. Create a Pod with CPU and memory requests.
2. Add CPU and memory limits.
3. Inspect the resulting Pod specification.
4. Calculate total resource requests for multi-container Pods.
5. Compare requests with actual usage.
6. Create Guaranteed, Burstable, and BestEffort Pods.
7. Configure a LimitRange.
8. Configure a ResourceQuota.
9. Test CPU throttling in a disposable environment.
10. Test memory limits and observe OOM behavior.
11. Practice troubleshooting resource-related Pending Pods.
12. Experiment with different request/limit combinations.
13. Study how resource requests affect HPA and Cluster Autoscaler.

---

# Chapter Summary

```text
                    Resource Management

                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
         Requests                      Limits
             │                           │
             ▼                           ▼
        Scheduling                 Runtime Control
             │                           │
             ▼                           ▼
          Scheduler                 Container Runtime
```

Kubernetes resource management is based primarily on:

```text
CPU
Memory
```

The most important distinction is:

```text
Request
    ↓
Used primarily for scheduling

Limit
    ↓
Runtime ceiling
```

CPU and memory behave differently:

```text
CPU
    ↓
Can be throttled
```

```text
Memory
    ↓
Can result in OOM termination
```

Kubernetes also classifies Pods into:

```text
Guaranteed
    ↓
Strongest resource configuration

Burstable
    ↓
Partial resource configuration

BestEffort
    ↓
No CPU/memory requests or limits
```

Namespace-level controls provide additional governance:

```text
LimitRange
    ↓
Defaults + min/max constraints

ResourceQuota
    ↓
Aggregate namespace limits
```

The most important production principle is:

```text
Measure

↓

Set realistic requests

↓

Set appropriate limits

↓

Monitor

↓

Tune
```

Incorrect resource configuration can cause both:

```text
Under-utilization

or

Resource contention
```

Therefore, resource requests and limits should be treated as an important part of Kubernetes capacity planning, scheduling, autoscaling, and production reliability.

---

## Next Chapter

# Chapter 43 – Horizontal Pod Autoscaler (HPA)

Topics will include:

- What is HPA?
- Why autoscaling is needed
- HPA architecture
- Scaling Replicas
- CPU-based Autoscaling
- Memory-based Autoscaling
- Resource Requests and HPA
- `autoscaling/v2`
- `minReplicas`
- `maxReplicas`
- Target Utilization
- Scaling Behavior
- Scale Up
- Scale Down
- Stabilization Windows
- Multiple Metrics
- Custom Metrics
- External Metrics
- Metrics Server
- HPA Troubleshooting
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---