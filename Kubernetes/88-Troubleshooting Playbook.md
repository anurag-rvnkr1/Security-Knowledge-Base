# Chapter 88 – Troubleshooting Playbook

## Overview

This chapter provides a systematic Kubernetes troubleshooting methodology for diagnosing and resolving common cluster, workload, networking, storage, security, and production incidents.

The objective is to move from:

```text
Symptom
   ↓
Evidence
   ↓
Hypothesis
   ↓
Test
   ↓
Root Cause
   ↓
Remediation
   ↓
Validation
   ↓
Prevention
```

This playbook is designed for:

- Kubernetes administrators
- DevOps engineers
- SREs
- Cloud engineers
- Platform engineers
- SOC analysts
- Kubernetes security engineers
- Production support teams
- Interview preparation

---

# 1. Golden Troubleshooting Rule

Do not immediately restart or delete the failing resource.

First:

```text
Observe
 ↓
Collect Evidence
 ↓
Understand
 ↓
Change
 ↓
Validate
```

A restart may temporarily hide the root cause.

---

# 2. First Five Commands

When a Kubernetes problem occurs, start with:

```bash
kubectl get pods -A
```

```bash
kubectl get nodes
```

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

```bash
kubectl get svc -A
```

```bash
kubectl get endpointslices -A
```

Then narrow the investigation.

---

# 3. Universal Troubleshooting Workflow

```text
1. What is broken?
2. Who is affected?
3. When did it start?
4. What changed?
5. Which Kubernetes object is involved?
6. What do Events say?
7. What do Logs say?
8. What do Metrics say?
9. Which dependencies are involved?
10. What is the smallest safe fix?
11. Did the fix work?
12. How do we prevent recurrence?
```

---

# 4. Determine Scope

First determine whether the issue is:

```text
Single Pod
Single Deployment
Single Namespace
Single Node
Multiple Nodes
Entire Cluster
Multiple Clusters
External Dependency
```

Example:

```bash
kubectl get pods -A
```

If only one Pod is failing:

```text
Workload-level issue
```

If hundreds of Pods fail:

```text
Cluster / dependency / networking / infrastructure issue
```

---

# 5. Check Recent Changes

Always ask:

```text
What changed immediately before the incident?
```

Possible changes:

```text
Deployment
ConfigMap
Secret
NetworkPolicy
RBAC
Ingress
StorageClass
Node
CNI
CSI
Admission Policy
Helm Release
GitOps Commit
Cluster Upgrade
```

---

# 6. Check Events

Events are one of the fastest sources of Kubernetes diagnostic information.

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Namespace:

```bash
kubectl get events -n production \
  --sort-by=.lastTimestamp
```

Look for:

```text
FailedScheduling
FailedMount
FailedAttachVolume
FailedCreate
BackOff
Unhealthy
Killing
Pulling
Pulled
AdmissionDenied
```

---

# 7. Pod Troubleshooting

## Basic Inspection

```bash
kubectl get pod <pod>
```

Wide output:

```bash
kubectl get pod <pod> -o wide
```

Detailed:

```bash
kubectl describe pod <pod>
```

YAML:

```bash
kubectl get pod <pod> -o yaml
```

---

# 8. Pod State – Pending

If:

```text
STATUS = Pending
```

investigate:

```bash
kubectl describe pod <pod>
```

Look at:

```text
Events
Node
Scheduling Constraints
Volumes
Resource Requests
```

---

# 9. Pending Pod Decision Tree

```text
Pod Pending
     ↓
Events
     ↓
FailedScheduling?
     │
     ├── Yes
     │    ↓
     │  Resources?
     │    ↓
     │  Taints?
     │    ↓
     │  Affinity?
     │    ↓
     │  NodeSelector?
     │    ↓
     │  Topology?
     │
     └── No
          ↓
       Volume?
          ↓
       Admission?
          ↓
       Image?
```

---

# 10. Insufficient CPU

Typical event:

```text
Insufficient cpu
```

Check:

```bash
kubectl describe pod <pod>
kubectl get nodes
kubectl describe node <node>
```

Check usage:

```bash
kubectl top nodes
```

Possible solutions:

```text
Reduce requests
Add nodes
Scale cluster
Move workloads
Optimize resource allocation
```

Do not blindly reduce requests for critical workloads.

---

# 11. Insufficient Memory

Typical event:

```text
Insufficient memory
```

Check:

```bash
kubectl top nodes
```

Then:

```bash
kubectl describe node <node>
```

Look for:

```text
MemoryPressure
Allocatable Memory
Requested Memory
```

---

# 12. NodeSelector Failure

If a Pod has:

```yaml
nodeSelector:
  disktype: ssd
```

but no node has that label:

```text
Pod → Pending
```

Check:

```bash
kubectl get nodes --show-labels
```

Fix the label or scheduling requirement.

---

# 13. Node Affinity Failure

Inspect:

```bash
kubectl get pod <pod> -o yaml
```

Look for:

```yaml
affinity:
  nodeAffinity:
```

Check node labels:

```bash
kubectl get nodes --show-labels
```

Verify that the required expression can actually match a node.

---

# 14. Taint and Toleration Failure

Check node taints:

```bash
kubectl describe node <node>
```

Look for:

```text
Taints:
```

Example:

```text
dedicated=security:NoSchedule
```

Check Pod tolerations:

```bash
kubectl get pod <pod> -o yaml
```

If there is no matching toleration:

```text
Pod cannot schedule there.
```

---

# 15. ImagePullBackOff

Check:

```bash
kubectl describe pod <pod>
```

Look under:

```text
Events
```

Common causes:

```text
Wrong Registry
Wrong Repository
Wrong Tag
Private Registry
Missing imagePullSecret
Registry Unavailable
Network Failure
```

---

# 16. Image Pull Checklist

```text
☐ Image name correct
☐ Tag exists
☐ Registry reachable
☐ Authentication valid
☐ imagePullSecrets configured
☐ Node can reach registry
☐ Image architecture compatible
```

---

# 17. ErrImagePull

`ErrImagePull` usually means Kubernetes attempted to pull the image and failed.

Inspect:

```bash
kubectl describe pod <pod>
```

Do not immediately restart the Pod.

First identify the exact image pull error.

---

# 18. CrashLoopBackOff

Check:

```bash
kubectl logs <pod>
```

Then:

```bash
kubectl logs <pod> --previous
```

And:

```bash
kubectl describe pod <pod>
```

Investigate:

```text
Application Error
Configuration
Secret
ConfigMap
Database
Permissions
Probe
Resources
Command
Arguments
```

---

# 19. CrashLoopBackOff Decision Tree

```text
CrashLoopBackOff
      ↓
Previous Logs
      ↓
Application Error?
      │
      ├── Yes → Fix Application
      │
      └── No
           ↓
       Probe Failure?
           ↓
       Configuration?
           ↓
       Dependency?
           ↓
       OOMKilled?
           ↓
       Permission?
```

---

# 20. OOMKilled

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
Reason: OOMKilled
```

Then inspect:

```bash
kubectl top pod <pod>
```

Investigate:

```text
Memory Leak
High Workload
Incorrect Limit
Insufficient Request
Application Configuration
```

---

# 21. Container Restarting

Check restart count:

```bash
kubectl get pods
```

Example:

```text
NAME    READY   STATUS    RESTARTS
api     1/1     Running   15
```

Then:

```bash
kubectl describe pod api
```

and:

```bash
kubectl logs api --previous
```

---

# 22. Pod Running but Not Ready

Important distinction:

```text
Running ≠ Ready
```

Check:

```bash
kubectl get pod <pod>
```

Example:

```text
1/1 Running
```

or:

```text
0/1 Running
```

If not Ready:

```bash
kubectl describe pod <pod>
```

Investigate:

```text
Readiness Probe
Application Startup
Dependencies
Configuration
Network
```

---

# 23. Readiness Probe Failure

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
Readiness probe failed
```

Verify:

```text
Path
Port
Protocol
Initial Delay
Timeout
Period
Failure Threshold
```

Test manually from inside or from an appropriate debugging Pod.

---

# 24. Liveness Probe Failure

Symptoms:

```text
Pod restarts repeatedly
```

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
Liveness probe failed
```

Potential causes:

```text
Bad Endpoint
Incorrect Port
Application Hung
Probe Too Aggressive
Slow Startup
```

---

# 25. Startup Probe Failure

If an application takes several minutes to start, a liveness probe may restart it prematurely.

Use:

```yaml
startupProbe:
```

Investigate:

```text
Application Startup Time
Probe Configuration
Failure Threshold
```

---

# 26. Init Container Failure

Check:

```bash
kubectl describe pod <pod>
```

Then:

```bash
kubectl logs <pod> -c <init-container>
```

Common causes:

```text
Dependency unavailable
Permission failure
Configuration failure
Network failure
```

---

# 27. Multi-Container Pod

List containers:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.containers[*].name}'
```

Check specific container logs:

```bash
kubectl logs <pod> -c <container>
```

---

# 28. Deployment Troubleshooting

Check:

```bash
kubectl get deployment
```

Then:

```bash
kubectl describe deployment <deployment>
```

Check ReplicaSets:

```bash
kubectl get rs
```

Check Pods:

```bash
kubectl get pods
```

---

# 29. Deployment Replicas Not Available

Check:

```bash
kubectl get deployment <deployment>
```

Look at:

```text
DESIRED
CURRENT
UP-TO-DATE
AVAILABLE
```

If:

```text
DESIRED = 3
AVAILABLE = 1
```

investigate the missing replicas.

---

# 30. ReplicaSet Troubleshooting

```bash
kubectl get rs
```

Then:

```bash
kubectl describe rs <replicaset>
```

Look for:

```text
FailedCreate
SelectorMismatch
AdmissionFailure
PodCreationFailure
```

---

# 31. Deployment Rollout Stuck

Check:

```bash
kubectl rollout status deployment/<name>
```

Then:

```bash
kubectl describe deployment <name>
```

Check:

```text
New Pods
Old Pods
Readiness
Image
Resources
PDB
Scheduling
```

---

# 32. Rollout History

```bash
kubectl rollout history deployment/<name>
```

If the new version is broken:

```bash
kubectl rollout undo deployment/<name>
```

Verify:

```bash
kubectl rollout status deployment/<name>
```

---

# 33. Service Troubleshooting

Check:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc <service>
```

Check EndpointSlices:

```bash
kubectl get endpointslices
```

---

# 34. Service Has No Endpoints

This is one of the most common Kubernetes networking problems.

Check:

```bash
kubectl get svc <service> -o yaml
```

Find:

```yaml
selector:
```

Then:

```bash
kubectl get pods --show-labels
```

Compare:

```text
Service Selector
        ↓
Pod Labels
```

They must match appropriately.

---

# 35. Service Selector Troubleshooting

Example:

Service:

```yaml
selector:
  app: backend
```

Pod:

```yaml
labels:
  app: api
```

Result:

```text
No matching endpoint
```

Fix the selector or labels.

---

# 36. Service Port Troubleshooting

Check:

```yaml
ports:
  - port: 80
    targetPort: 8080
```

Verify application actually listens on:

```text
8080
```

A Service can exist correctly while traffic still fails because `targetPort` does not match the application's listening port.

---

# 37. Service Connectivity Test

Create a debugging Pod:

```bash
kubectl run curl-test \
  --image=curlimages/curl:latest \
  -it --rm \
  --restart=Never -- sh
```

Test:

```bash
curl http://service-name
```

Test port:

```bash
curl http://service-name:8080
```

---

# 38. DNS Troubleshooting

Test:

```bash
nslookup kubernetes.default
```

Test Service DNS:

```bash
nslookup web.default.svc.cluster.local
```

Test from an application/debug Pod.

---

# 39. CoreDNS Troubleshooting

Check:

```bash
kubectl get pods -n kube-system
```

Find CoreDNS.

Then:

```bash
kubectl logs -n kube-system \
  -l k8s-app=kube-dns
```

Check Service:

```bash
kubectl get svc -n kube-system
```

---

# 40. DNS Decision Tree

```text
DNS Failure
    ↓
Can Pod reach DNS?
    ↓
CoreDNS Running?
    ↓
CoreDNS Service?
    ↓
NetworkPolicy?
    ↓
CNI?
    ↓
CoreDNS Configuration?
    ↓
Upstream DNS?
```

---

# 41. Ingress Troubleshooting

Check:

```bash
kubectl get ingress
```

Describe:

```bash
kubectl describe ingress <name>
```

Check controller:

```bash
kubectl get pods -A
```

Then verify:

```text
Ingress
 ↓
Ingress Controller
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
```

---

# 42. Ingress 404

Possible causes:

```text
Wrong Host
Wrong Path
Wrong Ingress Rule
Wrong Controller
Wrong Service
```

Check:

```bash
kubectl describe ingress <name>
```

---

# 43. Ingress 502 / 503

Typical chain:

```text
Ingress
 ↓
Service
 ↓
Endpoint
 ↓
Pod
```

Check:

```bash
kubectl get svc
kubectl get endpointslices
kubectl get pods
```

If the Service has no endpoints:

```text
Investigate Pod selectors/readiness.
```

---

# 44. Gateway API Troubleshooting

Check:

```bash
kubectl get gatewayclass
kubectl get gateway
kubectl get httproute
```

Describe:

```bash
kubectl describe gateway <name>
kubectl describe httproute <name>
```

Check:

```text
Accepted
Programmed
ResolvedRefs
```

---

# 45. NetworkPolicy Troubleshooting

List:

```bash
kubectl get networkpolicy -A
```

Describe:

```bash
kubectl describe networkpolicy <name>
```

Check labels:

```bash
kubectl get pods --show-labels
```

---

# 46. NetworkPolicy Mental Model

Always identify:

```text
Source
Destination
Direction
Protocol
Port
Namespace
Pod Labels
```

Then determine whether the traffic is:

```text
Ingress
Egress
Both
```

---

# 47. NetworkPolicy Default Deny

If a default deny policy exists:

```yaml
podSelector: {}
```

then explicit allow policies may be required.

Check:

```bash
kubectl get networkpolicy -o yaml
```

---

# 48. NetworkPolicy DNS Problem

If egress is restricted, DNS traffic may also be blocked.

Typical requirement:

```text
Application
   ↓
UDP/TCP 53
   ↓
CoreDNS
```

Check whether DNS traffic is explicitly allowed.

---

# 49. CNI Troubleshooting

If Pod-to-Pod networking fails, investigate the CNI.

Check:

```bash
kubectl get pods -A
```

Identify CNI components.

Check:

```text
CNI Pods
CNI Logs
Node Network
Routes
Interfaces
NetworkPolicy Implementation
```

---

# 50. Cross-Node Pod Connectivity

If:

```text
Pod A → Pod B
```

fails only when Pods are on different nodes, investigate:

```text
CNI
Node Routing
Firewall
Cloud Security Groups
Overlay Network
MTU
```

---

# 51. MTU Problems

Symptoms may include:

```text
Large requests fail
Small requests work
TLS connections fail
Intermittent network failures
```

Investigate:

```text
Node MTU
CNI MTU
Overlay MTU
Cloud Network MTU
```

---

# 52. Service Connectivity vs Pod Connectivity

Test both.

Direct Pod:

```text
Pod A → Pod B IP
```

Service:

```text
Pod A → Service DNS
```

If direct Pod connectivity works but Service connectivity fails:

```text
Service / kube-proxy / EndpointSlice / routing
```

may be involved.

---

# 53. Storage Troubleshooting

Check:

```bash
kubectl get pv
kubectl get pvc
kubectl get storageclass
```

For CSI:

```bash
kubectl get csidrivers
```

---

# 54. PVC Pending

Run:

```bash
kubectl describe pvc <pvc>
```

Check events.

Possible causes:

```text
No StorageClass
Wrong StorageClass
CSI Failure
No Capacity
Unsupported Access Mode
Topology Constraint
```

---

# 55. PVC Bound but Pod Cannot Mount

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
FailedMount
FailedAttachVolume
```

Then:

```bash
kubectl describe pvc <pvc>
kubectl describe pv <pv>
```

Investigate the CSI driver and node.

---

# 56. CSI Troubleshooting

Check:

```bash
kubectl get csidrivers
```

Check CSI Pods:

```bash
kubectl get pods -A | grep -i csi
```

Check logs for the relevant CSI controller/node components.

---

# 57. Volume Attachment Failure

Potential causes:

```text
Node Problem
CSI Controller
CSI Node Plugin
Cloud API
Volume Already Attached
Access Mode
```

---

# 58. StatefulSet Troubleshooting

Check:

```bash
kubectl get statefulset
```

Then:

```bash
kubectl describe statefulset <name>
```

Check:

```bash
kubectl get pods
kubectl get pvc
```

Remember:

```text
StatefulSet
 ↓
Stable Identity
 ↓
Stable Storage
```

---

# 59. StatefulSet Pod Stuck

Investigate:

```text
PVC
Volume Mount
Readiness
Ordering
Application State
```

Do not casually delete StatefulSet Pods when they contain stateful workloads.

---

# 60. DaemonSet Troubleshooting

Check:

```bash
kubectl get daemonset
```

If a node does not have the DaemonSet Pod, investigate:

```text
Node Taints
Node Selectors
Affinity
DaemonSet Selector
Node Eligibility
```

---

# 61. Job Troubleshooting

Check:

```bash
kubectl get jobs
```

Then:

```bash
kubectl describe job <job>
```

Inspect Job Pods:

```bash
kubectl get pods
```

Check logs:

```bash
kubectl logs <pod>
```

---

# 62. CronJob Troubleshooting

Check:

```bash
kubectl get cronjobs
```

Then:

```bash
kubectl describe cronjob <name>
```

Check generated Jobs:

```bash
kubectl get jobs
```

Potential issues:

```text
Schedule
Suspension
Concurrency Policy
Job Failure
Resource Constraints
```

---

# 63. RBAC Troubleshooting

If you receive:

```text
Forbidden
```

check:

```bash
kubectl auth can-i <verb> <resource>
```

Example:

```bash
kubectl auth can-i get pods
```

---

# 64. Identify ServiceAccount

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.serviceAccountName}'
```

Then test:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:<namespace>:<serviceaccount>
```

---

# 65. RBAC Decision Tree

```text
403 Forbidden
     ↓
Identify Subject
     ↓
RoleBinding?
     ↓
Role?
     ↓
Correct Namespace?
     ↓
Correct Resource?
     ↓
Correct API Group?
     ↓
Correct Verb?
```

---

# 66. Common RBAC Mistake

Incorrect:

```yaml
apiGroups:
  - ""
resources:
  - deployments
```

Deployments belong to:

```text
apps
```

Correct:

```yaml
apiGroups:
  - apps
resources:
  - deployments
```

---

# 67. Secret Access Troubleshooting

Check:

```bash
kubectl get secret
```

Then determine:

```text
Who needs access?
Why?
Which namespace?
Which key?
```

Avoid granting:

```text
Cluster-wide Secret Read
```

unless explicitly required.

---

# 68. Pod Security Troubleshooting

If admission rejects a Pod:

```text
Admission denied
```

Inspect:

```text
Privileged
Root User
Capabilities
HostPath
HostNetwork
HostPID
HostIPC
```

Use a secure `securityContext`.

---

# 69. Admission Webhook Troubleshooting

If an admission webhook is causing failures:

Check:

```bash
kubectl get validatingwebhookconfigurations
```

and:

```bash
kubectl get mutatingwebhookconfigurations
```

Investigate:

```text
Webhook Availability
TLS
Service
Endpoints
Policy
Timeouts
```

Do not disable security webhooks blindly during an incident.

---

# 70. Node Troubleshooting

Check:

```bash
kubectl get nodes
```

If:

```text
NotReady
```

run:

```bash
kubectl describe node <node>
```

---

# 71. Node Conditions

Look for:

```text
Ready
MemoryPressure
DiskPressure
PIDPressure
NetworkUnavailable
```

---

# 72. Node NotReady

Potential causes:

```text
Kubelet
Container Runtime
Network
Disk
Memory
Certificates
Cloud Provider
```

---

# 73. Kubelet Troubleshooting

On the node, where authorized:

```text
Check kubelet status
Check kubelet logs
Check certificates
Check configuration
Check API connectivity
```

The exact commands depend on the operating system and distribution.

---

# 74. Container Runtime Troubleshooting

Investigate:

```text
containerd
CRI-O
```

Check:

```text
Runtime Health
Images
Container Creation
Disk
Runtime Logs
```

---

# 75. DiskPressure

Check:

```bash
kubectl describe node <node>
```

Look for:

```text
DiskPressure=True
```

Potential causes:

```text
Container Logs
Unused Images
Ephemeral Storage
Runtime Data
```

---

# 76. MemoryPressure

Check:

```bash
kubectl describe node <node>
```

Then:

```bash
kubectl top node <node>
```

Potential causes:

```text
High Workload
Overcommitment
Memory Leak
Insufficient Capacity
```

---

# 77. PIDPressure

PID pressure means the node is approaching process ID limits.

Investigate:

```text
Process Count
Container Behavior
Fork Bomb / Runaway Process
Node PID Limits
```

---

# 78. Resource Troubleshooting

Check:

```bash
kubectl top nodes
kubectl top pods -A
```

Compare:

```text
Requests
Limits
Actual Usage
```

---

# 79. CPU Throttling

Symptoms:

```text
High Latency
Slow Requests
CPU Limit Saturation
```

Investigate:

```text
CPU Requests
CPU Limits
Application CPU Usage
Node Capacity
```

Avoid assuming every CPU issue is solved by increasing limits.

---

# 80. Memory Leak

Symptoms:

```text
Memory Increasing
OOMKilled
Restarts
Performance Degradation
```

Investigate:

```text
Application Heap
Runtime Metrics
Container Memory
Request Patterns
```

---

# 81. HPA Troubleshooting

Check:

```bash
kubectl get hpa
```

Describe:

```bash
kubectl describe hpa <name>
```

Check metrics:

```bash
kubectl top pods
```

---

# 82. HPA Not Scaling

Possible causes:

```text
Metrics Server unavailable
No resource requests
Incorrect target
Wrong metric
Target workload incorrect
Insufficient cluster capacity
```

---

# 83. HPA Scaling but Pods Pending

Architecture:

```text
HPA
 ↓
More Pods
 ↓
Insufficient Node Capacity
 ↓
Pending Pods
```

Investigate:

```text
Cluster Autoscaler
Node Capacity
Scheduling Constraints
```

---

# 84. VPA Troubleshooting

Check VPA resources if installed:

```bash
kubectl get vpa
```

Investigate:

```text
Recommendations
Update Mode
Resource Usage
Pod Restart Behavior
```

---

# 85. Cluster Autoscaler Troubleshooting

Symptoms:

```text
Pods Pending
Nodes not added
```

Investigate:

```text
Cloud Provider
Node Group Configuration
Autoscaler Logs
Scheduling Constraints
Resource Availability
```

---

# 86. Priority and Preemption Troubleshooting

If a high-priority Pod cannot schedule:

Check:

```bash
kubectl describe pod <pod>
```

Investigate:

```text
PriorityClass
Resources
Taints
Affinity
PodDisruptionBudget
Preemption
```

---

# 87. Pod Affinity Troubleshooting

A Pod may remain Pending because its affinity rule cannot be satisfied.

Check:

```bash
kubectl get pod <pod> -o yaml
```

Review:

```text
topologyKey
labelSelector
requiredDuringScheduling...
```

---

# 88. Pod Anti-Affinity Troubleshooting

If replicas cannot be distributed:

```text
Anti-Affinity
+
Insufficient Nodes
=
Pending Pods
```

Relax constraints only when appropriate.

---

# 89. Topology Spread Troubleshooting

Check:

```text
topologySpreadConstraints
```

Investigate:

```text
Topology Domains
Node Labels
MaxSkew
WhenUnsatisfiable
```

---

# 90. ConfigMap Troubleshooting

Check:

```bash
kubectl get configmap
kubectl describe configmap <name>
```

If the application cannot find configuration:

```text
ConfigMap Name
Namespace
Key
Environment Variable
Volume Mount
```

---

# 91. Secret Troubleshooting

Check:

```bash
kubectl get secret
```

Inspect metadata:

```bash
kubectl describe secret <name>
```

Verify:

```text
Secret Name
Namespace
Key
Mount
Environment Variable
RBAC
```

---

# 92. Environment Variable Troubleshooting

Inside the container:

```bash
kubectl exec <pod> -- env
```

Check whether expected variables exist.

Do not expose sensitive values in logs or incident tickets.

---

# 93. Volume Mount Troubleshooting

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
MountVolume
FailedMount
Permission
Path
```

Verify:

```text
Volume Name
Volume Source
Mount Path
ReadOnly
```

---

# 94. In-Container Debugging

Enter:

```bash
kubectl exec -it <pod> -- /bin/sh
```

Test:

```bash
env
```

Network:

```bash
wget
curl
nslookup
```

Filesystem:

```bash
df -h
mount
ls
```

Use a debugging Pod when application images lack diagnostic tools.

---

# 95. Ephemeral Debug Containers

Where supported and appropriate:

```bash
kubectl debug <pod> \
  -it \
  --image=busybox:1.36
```

Useful for troubleshooting minimal production images without modifying the application image.

---

# 96. Node Debugging

Where appropriate:

```bash
kubectl debug node/<node> -it \
  --image=ubuntu
```

Use carefully and according to your cluster's security policy.

---

# 97. API Server Troubleshooting

Symptoms:

```text
kubectl slow
API timeouts
Controller failures
Admission delays
```

Investigate:

```text
API Server Metrics
API Server Logs
etcd
Authentication
Admission
Network
Resource Saturation
```

---

# 98. Scheduler Troubleshooting

Symptoms:

```text
Pods remain Pending
```

Check scheduler-related events:

```bash
kubectl get events -A \
  --sort-by=.lastTimestamp
```

Investigate:

```text
Resources
Taints
Affinity
Topology
Volumes
Priority
```

---

# 99. Controller Manager Troubleshooting

Symptoms:

```text
Deployments not creating Pods
Replica count not reconciled
Jobs not progressing
```

Investigate:

```text
Controller Manager Health
API Server
etcd
Resource Definitions
Events
```

---

# 100. etcd Troubleshooting

If control-plane behavior is abnormal, investigate etcd health.

Look for:

```text
High Latency
Member Failure
Disk Problems
Leader Changes
Quorum Problems
```

Never experiment with etcd membership changes on production clusters without understanding quorum and recovery procedures.

---

# 101. etcd Backup Validation

A backup is useful only if it can be restored.

Test:

```text
Backup
 ↓
Restore
 ↓
Validation
```

Document:

```text
RPO
RTO
Restore Procedure
Dependencies
```

---

# 102. Certificate Troubleshooting

Symptoms:

```text
x509 errors
TLS handshake failures
Authentication failures
```

Investigate:

```text
Certificate Expiration
Certificate Authority
Kubeconfig
Server Name
Trust Chain
```

---

# 103. Time Synchronization Problems

Certificate validation and distributed systems can be affected by incorrect system time.

If TLS behavior is strange, investigate:

```text
Node Time
NTP
Clock Drift
```

---

# 104. Logging Troubleshooting

If application logs are missing:

Check:

```bash
kubectl logs <pod>
```

Then determine whether the problem is:

```text
Application
Container Runtime
Log Collector
Storage
Pipeline
Backend
```

---

# 105. Centralized Logging Failure

Architecture:

```text
Pod
 ↓
Collector
 ↓
Transport
 ↓
Storage
 ↓
Dashboard
```

Identify where data stops.

---

# 106. Prometheus Troubleshooting

Check:

```text
Prometheus Pod
Targets
Service Discovery
RBAC
NetworkPolicy
ServiceMonitor / PodMonitor
```

If a target is missing:

```text
Check discovery configuration.
```

---

# 107. Grafana Troubleshooting

If dashboards show no data:

Check:

```text
Data Source
Prometheus
Network
Credentials
Query
Time Range
```

---

# 108. Alertmanager Troubleshooting

If alerts are generated but notifications are not delivered:

Check:

```text
Alertmanager
Routing
Receivers
Silences
Inhibition
Network
Credentials
```

---

# 109. OpenTelemetry Troubleshooting

Trace missing?

Check:

```text
Instrumentation
Collector
Export
Network
Backend
Sampling
```

Pipeline:

```text
Application
 ↓
OTel SDK
 ↓
Collector
 ↓
Backend
```

---

# 110. Performance Troubleshooting

Start with:

```text
Latency
Traffic
Errors
Saturation
```

Then investigate:

```text
CPU
Memory
Network
Storage
Dependencies
Database
```

---

# 111. High API Latency

Check:

```text
Application CPU
Memory
Database
External APIs
Network
Pod Scheduling
Node Saturation
```

Distributed tracing can identify the slow dependency.

---

# 112. High Error Rate

Determine:

```text
Which endpoint?
Which version?
Which Pod?
Which node?
Which region?
```

Compare:

```text
Before Deployment
After Deployment
```

If errors began immediately after a release:

```text
Rollback may be the safest mitigation.
```

---

# 113. Network Latency

Investigate:

```text
Pod → Pod
Pod → Service
Pod → External
```

Determine where latency appears.

---

# 114. Storage Latency

Investigate:

```text
Application
PVC
CSI
Storage Backend
Node
Cloud Provider
```

Check:

```text
IOPS
Throughput
Latency
Queue Depth
```

---

# 115. Production Incident Response

When a serious incident occurs:

```text
Detect
 ↓
Declare
 ↓
Assign Roles
 ↓
Assess Impact
 ↓
Mitigate
 ↓
Investigate
 ↓
Recover
 ↓
Validate
 ↓
Communicate
 ↓
Postmortem
```

---

# 116. Incident Roles

Typical roles:

```text
Incident Commander
Technical Lead
Communications Lead
Subject Matter Experts
Scribe
```

The exact structure depends on the organization.

---

# 117. Incident Communication

Good incident updates should answer:

```text
What happened?
Who is affected?
What are we doing?
What is the current status?
What is the next action?
```

Avoid speculation presented as fact.

---

# 118. Evidence Preservation

During security incidents preserve:

```text
Logs
Events
Pod Definitions
Images
ServiceAccounts
RBAC
NetworkPolicies
Audit Logs
Relevant Node Evidence
```

Avoid destroying evidence through unnecessary deletion or restart.

---

# 119. Security Incident Containment

Possible containment actions:

```text
Isolate Namespace
Block Network Traffic
Scale Down Compromised Workload
Revoke Credentials
Rotate Secrets
Restrict ServiceAccount
Quarantine Image
```

Choose the least destructive action that effectively reduces risk.

---

# 120. Kubernetes Forensics Checklist

```text
☐ Identify compromised workload
☐ Record Pod metadata
☐ Record image digest
☐ Identify ServiceAccount
☐ Review RBAC
☐ Review NetworkPolicy
☐ Collect logs
☐ Collect events
☐ Review audit logs
☐ Identify network connections
☐ Preserve relevant node evidence
☐ Build timeline
☐ Determine scope
```

---

# 121. Root Cause Analysis

A strong RCA should answer:

```text
What happened?
Why did it happen?
Why wasn't it detected earlier?
Why did existing controls fail?
What will prevent recurrence?
```

---

# 122. Five Whys

Example:

```text
Why did API requests fail?
→ Database was unreachable.

Why?
→ NetworkPolicy blocked traffic.

Why?
→ Policy selector changed.

Why?
→ Manual change bypassed review.

Why?
→ Production changes were not GitOps-controlled.
```

Root cause:

```text
Process + Technical Control Gap
```

---

# 123. Change Failure Rate

Track:

```text
Deployments
Failures
Rollbacks
Incidents
```

High change failure rate suggests problems in:

```text
Testing
Deployment Strategy
Observability
Rollback
Change Management
```

---

# 124. Safe Remediation Principles

Prefer:

```text
Small Change
Reversible Change
Observable Change
Documented Change
```

Avoid:

```text
Large Unplanned Changes
Multiple Simultaneous Changes
Force Deletion
Blind Restarts
```

---

# 125. Troubleshooting Command Matrix

| Problem | First Commands |
|---|---|
| Pod Pending | `get pod`, `describe pod`, `get events` |
| CrashLoopBackOff | `logs`, `logs --previous`, `describe pod` |
| ImagePullBackOff | `describe pod` |
| Service Failure | `get svc`, `get endpointslices`, `describe svc` |
| DNS Failure | `nslookup`, CoreDNS logs |
| PVC Pending | `describe pvc`, `get storageclass` |
| Node NotReady | `get nodes`, `describe node` |
| RBAC Failure | `kubectl auth can-i` |
| HPA Failure | `get hpa`, `describe hpa`, `top pods` |
| NetworkPolicy | `get networkpolicy`, labels, connectivity test |
| Ingress | `get ingress`, `describe ingress`, controller logs |
| Deployment Failure | `rollout status`, `describe deployment`, `get rs` |

---

# 126. Quick Decision Tree

```text
Is the Pod Running?
        │
   ┌────┴────┐
   No        Yes
   │          │
Pending?     Ready?
   │          │
   ▼       ┌──┴──┐
Schedule   No    Yes
           │      │
         Probe   Service
                  │
                  ▼
              Endpoints?
                  │
              ┌───┴───┐
             No      Yes
             │         │
          Selector   Network
          /Ready     /DNS
```

---

# 127. Production Troubleshooting Sequence

```text
1. Cluster
2. Node
3. Pod
4. Container
5. Application
6. Service
7. EndpointSlice
8. DNS
9. NetworkPolicy
10. Storage
11. Identity
12. External Dependency
```

Do not always follow this order rigidly. Start with the evidence and symptom that best narrows the problem.

---

# 128. Troubleshooting by Symptom

## "Pod is Pending"

Check:

```text
Scheduling
Resources
Taints
Affinity
Storage
```

---

## "Pod keeps restarting"

Check:

```text
Logs
Previous Logs
Probes
OOMKilled
Application
```

---

## "Service returns 503"

Check:

```text
Endpoints
Readiness
Service Selector
TargetPort
Ingress
```

---

## "DNS does not work"

Check:

```text
CoreDNS
CNI
NetworkPolicy
Pod DNS
```

---

## "PVC is Pending"

Check:

```text
StorageClass
CSI
Capacity
Access Mode
Topology
```

---

## "403 Forbidden"

Check:

```text
Authentication
ServiceAccount
Role
RoleBinding
Verb
Resource
Namespace
```

---

## "Node is NotReady"

Check:

```text
Kubelet
Runtime
Network
Disk
Memory
Certificates
```

---

# 129. What Not to Do

Avoid:

```text
❌ Delete the entire namespace immediately
❌ Force-delete Pods without understanding impact
❌ Restart every component
❌ Disable NetworkPolicies blindly
❌ Remove RBAC protections
❌ Disable admission security
❌ Delete PVCs during storage incidents
❌ Change multiple variables simultaneously
❌ Rotate credentials without understanding dependencies
❌ Modify etcd blindly
```

---

# 130. Troubleshooting Best Practices

```text
☑ Start with read-only commands
☑ Preserve evidence
☑ Check events
☑ Compare desired vs actual state
☑ Check dependencies
☑ Use controlled tests
☑ Make one meaningful change at a time
☑ Validate after every change
☑ Document findings
☑ Automate recurring checks
```

---

# 131. Desired vs Actual State

Always compare:

```text
Desired State
      │
      ▼
Kubernetes Object
      │
      ▼
Observed State
```

Example:

```text
Desired replicas = 5
Actual replicas = 2
```

Ask:

```text
Why can't Kubernetes reach desired state?
```

---

# 132. Dependency Mapping

For complex applications:

```text
Frontend
   ↓
API
   ↓
Authentication
   ↓
Database
   ↓
External Payment API
```

Troubleshoot from the failing component outward.

---

# 133. Recent Change Analysis

If an incident begins at:

```text
10:15 AM
```

and a deployment occurred at:

```text
10:12 AM
```

the deployment becomes an important hypothesis.

Check:

```bash
kubectl rollout history deployment/<name>
```

---

# 134. Rollback Decision

Rollback when:

```text
New Version Clearly Causes Impact
Previous Version Known Good
Rollback Is Safe
Database Compatibility Is Confirmed
```

Do not roll back blindly if schema changes are incompatible.

---

# 135. Database Migration Warning

Application deployment:

```text
v1
 ↓
Database Schema
 ↓
v2
```

A rollback may fail if:

```text
v2 changed database schema
```

Use backward-compatible migration strategies where possible.

---

# 136. Troubleshooting Production Databases

Check:

```text
Pod
StatefulSet
PVC
Storage
Readiness
Replication
Connections
CPU
Memory
Disk
```

Do not delete stateful resources simply because they appear unhealthy.

---

# 137. Kubernetes Security Troubleshooting

When investigating security issues, review:

```text
Identity
RBAC
Admission
Pod Security
NetworkPolicy
Secrets
Images
Runtime
Audit Logs
```

---

# 138. Security Baseline

A production workload should ideally have:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  seccompProfile:
    type: RuntimeDefault
```

Container-level controls may additionally include:

```yaml
securityContext:
  capabilities:
    drop:
      - ALL
```

Use only controls compatible with the application.

---

# 139. Incident Prevention

Every significant incident should produce at least one improvement:

```text
Monitoring
Alert
Test
Automation
Documentation
Policy
Architecture
```

Example:

```text
DNS outage
 ↓
Add DNS health alert
 ↓
Add DNS synthetic test
 ↓
Document recovery
```

---

# 140. Troubleshooting Runbook Template

Use this template for production runbooks:

```text
# Incident Name

## Symptoms

## Impact

## Detection

## Initial Checks

## Investigation

## Root Cause

## Immediate Mitigation

## Permanent Fix

## Validation

## Rollback

## Prevention

## Escalation

## Related Dashboards

## Related Logs

## Related Alerts
```

---

# 141. Example Runbook – CrashLoopBackOff

```text
# CrashLoopBackOff

## Symptoms

Pod repeatedly restarts.

## Commands

kubectl get pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl describe pod <pod>

## Check

Application
Configuration
Secret
ConfigMap
Probe
Memory
Dependencies

## Remediation

Fix root cause.

## Validation

Pod Ready
No unexpected restarts
Application healthy
```

---

# 142. Example Runbook – Service Failure

```text
# Service Failure

## Symptoms

Application cannot reach Service.

## Commands

kubectl get svc
kubectl describe svc <service>
kubectl get endpointslices

## Check

Selector
Labels
Port
TargetPort
Readiness
NetworkPolicy
DNS

## Validation

curl http://service-name
```

---

# 143. Example Runbook – Node Failure

```text
# Node Failure

## Symptoms

Node NotReady.

## Commands

kubectl get nodes
kubectl describe node <node>

## Check

Kubelet
Runtime
Disk
Memory
Network

## Mitigation

Cordon / Drain if appropriate.

## Recovery

Restore node or replace node.

## Validation

Pods healthy
Cluster capacity healthy
```

---

# 144. Example Runbook – PVC Failure

```text
# PVC Failure

## Symptoms

PVC Pending or mount failure.

## Commands

kubectl get pvc
kubectl describe pvc <pvc>
kubectl get pv
kubectl get storageclass
kubectl get csidrivers

## Check

StorageClass
CSI
Capacity
Access Mode
Topology
Attachment

## Validation

PVC Bound
Pod Running
Data Accessible
```

---

# 145. Example Runbook – RBAC Failure

```text
# RBAC Failure

## Symptoms

403 Forbidden.

## Commands

kubectl auth can-i
kubectl get roles
kubectl get rolebindings
kubectl get clusterroles
kubectl get clusterrolebindings

## Check

Identity
Verb
Resource
API Group
Namespace

## Validation

Authorized operation succeeds.
Unauthorized operations remain blocked.
```

---

# 146. Production Troubleshooting Checklist

## Cluster

```text
☐ Nodes Ready
☐ Control Plane Healthy
☐ API Server Healthy
☐ etcd Healthy
☐ Scheduler Healthy
☐ Controllers Healthy
```

## Workloads

```text
☐ Pods Running
☐ Pods Ready
☐ No CrashLoops
☐ No ImagePull failures
☐ Replica counts correct
```

## Networking

```text
☐ Services
☐ EndpointSlices
☐ DNS
☐ CNI
☐ NetworkPolicies
☐ Ingress/Gateway
```

## Storage

```text
☐ PVC Bound
☐ PV Healthy
☐ CSI Healthy
☐ Storage Capacity
```

## Security

```text
☐ RBAC
☐ ServiceAccounts
☐ Pod Security
☐ Admission
☐ Secrets
☐ Image Security
```

## Resources

```text
☐ CPU
☐ Memory
☐ Disk
☐ Network
☐ PID
```

## Observability

```text
☐ Logs
☐ Metrics
☐ Traces
☐ Alerts
☐ Dashboards
```

---

# 147. The 10-Minute Incident Drill

When receiving a Kubernetes alert, perform:

```text
Minute 1
→ Determine impact

Minute 2
→ Check Pods

Minute 3
→ Check Events

Minute 4
→ Check Logs

Minute 5
→ Check Services

Minute 6
→ Check Nodes

Minute 7
→ Check Dependencies

Minute 8
→ Identify recent changes

Minute 9
→ Apply safe mitigation

Minute 10
→ Validate recovery
```

This is a training framework, not a rigid production SLA.

---

# 148. The 30-Minute Deep Investigation

If the root cause is unclear:

```text
0–5 min
→ Scope and impact

5–10 min
→ Workload investigation

10–15 min
→ Networking/storage/dependencies

15–20 min
→ Recent changes

20–25 min
→ Test hypotheses

25–30 min
→ Mitigation and validation
```

---

# 149. Root Cause Categories

Most Kubernetes incidents fall into:

```text
Application
Configuration
Networking
Storage
Scheduling
Resources
Security
Infrastructure
Control Plane
External Dependency
Human Error
Automation
```

---

# 150. Final Troubleshooting Mental Model

```text
                    INCIDENT
                       │
                       ▼
                    SYMPTOM
                       │
                       ▼
                    SCOPE
                       │
                       ▼
                    EVIDENCE
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      Logs           Events         Metrics
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                   HYPOTHESIS
                       │
                       ▼
                      TEST
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              Wrong        Correct
                 │           │
                 ▼           ▼
             New Test      ROOT CAUSE
                              │
                              ▼
                          MITIGATION
                              │
                              ▼
                           RECOVERY
                              │
                              ▼
                           VALIDATE
                              │
                              ▼
                          PREVENTION
```

---

# 151. Final Takeaways

Kubernetes troubleshooting is fundamentally about understanding relationships.

A Pod problem may actually be caused by:

```text
Scheduler
Node
CNI
DNS
Storage
RBAC
Admission
Application
```

A Service problem may actually be caused by:

```text
Selector
Labels
Readiness
EndpointSlice
Port
NetworkPolicy
DNS
CNI
```

A storage problem may actually be caused by:

```text
PVC
PV
StorageClass
CSI
Node
Cloud Provider
```

A security problem may actually be caused by:

```text
ServiceAccount
RBAC
Admission
Pod Security
NetworkPolicy
Image
Runtime
```

Therefore:

> **Never troubleshoot Kubernetes objects in isolation. Follow the dependency chain.**

---

# Troubleshooting Golden Rules

```text
1. Check before changing.
2. Preserve evidence.
3. Start with scope.
4. Check events early.
5. Compare desired vs actual state.
6. Follow dependencies.
7. Test hypotheses.
8. Make minimal changes.
9. Validate recovery.
10. Prevent recurrence.
```

The ultimate goal is not:

```text
"Make the Pod Running."
```

The goal is:

```text
"Restore the service safely,
understand why it failed,
and prevent the same failure from recurring."
```

---

# Next Chapter

## Chapter 89 – Production Operations Checklist

The final chapter will provide a complete operational checklist covering:

```text
Cluster Readiness
Production Deployment
Security
Networking
Storage
Scheduling
Resource Management
Observability
Backup
Disaster Recovery
Upgrades
Maintenance
Incident Response
Vulnerability Management
Compliance
GitOps
CI/CD
Helm
Kustomize
Service Mesh
Daily Operations
Weekly Operations
Monthly Operations
Quarterly Reviews
Production Go-Live
Post-Incident Review
Kubernetes Retirement / Decommissioning
```