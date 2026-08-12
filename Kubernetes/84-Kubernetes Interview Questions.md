# Chapter 84 – Kubernetes Interview Questions

## Overview

Kubernetes interviews typically test three levels of knowledge:

```text
Fundamentals
     ↓
Practical Administration
     ↓
Production + Troubleshooting + Security
```

For DevOps, Cloud, SRE, Platform Engineering, and Kubernetes Security roles, interviewers commonly evaluate whether you understand:

```text
Architecture
Networking
Storage
Scheduling
Security
Observability
Operations
Troubleshooting
Production Design
```

This chapter provides a structured Kubernetes interview preparation guide containing:

- Basic questions
- Intermediate questions
- Advanced questions
- Scenario-based questions
- Troubleshooting questions
- Security questions
- Networking questions
- Storage questions
- Production questions
- Hands-on interview tasks
- Short oral interview questions
- Frequently confused concepts
- Quick revision
- Interview cheat sheet

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain Kubernetes architecture
- Explain control-plane components
- Explain worker-node components
- Explain Pods and controllers
- Explain Deployments and StatefulSets
- Explain Services and Ingress
- Explain Kubernetes networking
- Explain CNI plugins
- Explain CoreDNS
- Explain NetworkPolicies
- Explain Kubernetes storage
- Explain PV, PVC, and StorageClass
- Explain CSI
- Explain scheduling
- Explain affinity and anti-affinity
- Explain taints and tolerations
- Explain resource requests and limits
- Explain HPA, VPA, and Cluster Autoscaler
- Explain Kubernetes security
- Explain RBAC
- Explain ServiceAccounts
- Explain Secrets
- Explain Pod Security Standards
- Explain admission controllers
- Explain observability
- Explain Prometheus and Grafana
- Explain OpenTelemetry
- Explain cluster operations
- Troubleshoot failed Pods
- Troubleshoot networking
- Troubleshoot DNS
- Troubleshoot storage
- Troubleshoot scheduling
- Troubleshoot RBAC
- Design production Kubernetes clusters
- Answer scenario-based interview questions

---

# Section 1 – Kubernetes Fundamentals

## 1. What is Kubernetes?

Kubernetes is an open-source container orchestration platform used to automate:

```text
Deployment
Scaling
Networking
Service Discovery
Scheduling
Self-Healing
Configuration
Storage
```

for containerized workloads.

---

## 2. Why is Kubernetes used?

Kubernetes helps manage containerized applications across multiple machines.

Major capabilities include:

```text
Self-Healing
Rolling Updates
Scaling
Service Discovery
Load Balancing
Scheduling
Configuration Management
Secret Management
Storage Orchestration
```

---

## 3. What is a Kubernetes cluster?

A Kubernetes cluster consists of:

```text
Control Plane
+
Worker Nodes
```

Conceptually:

```text
              Kubernetes Cluster
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     Control Plane          Worker Nodes
                               │
                    ┌──────────┼──────────┐
                    ▼          ▼          ▼
                  Node 1     Node 2     Node 3
```

---

## 4. What is the Control Plane?

The Control Plane manages the overall Kubernetes cluster.

Major components include:

```text
API Server
etcd
Scheduler
Controller Manager
```

---

## 5. What is the Kubernetes API Server?

The API Server is the primary entry point to the Kubernetes control plane.

Requests from:

```text
kubectl
Controllers
Scheduler
Kubelet
External Clients
```

communicate with the Kubernetes API.

---

## 6. What is etcd?

etcd is a distributed key-value store used by Kubernetes to store cluster state.

It stores information such as:

```text
Pods
Deployments
Services
Secrets
ConfigMaps
Cluster Configuration
```

---

## 7. What is the Scheduler?

The Scheduler selects an appropriate node for newly created Pods that do not yet have a node assignment.

Conceptually:

```text
Pod
 ↓
Scheduler
 ↓
Evaluate Nodes
 ↓
Select Node
 ↓
Bind Pod
```

---

## 8. What is the Controller Manager?

The Controller Manager runs Kubernetes controllers that continuously reconcile desired state with actual state.

Examples include controllers responsible for:

```text
Nodes
Deployments
ReplicaSets
Jobs
Namespaces
Endpoints
```

---

# Section 2 – Worker Nodes

## 9. What is a Worker Node?

A Worker Node runs application workloads.

Common components include:

```text
Kubelet
Container Runtime
Kube-Proxy
```

---

## 10. What is Kubelet?

Kubelet is the primary node agent.

It:

```text
Receives Pod specifications
Starts containers
Monitors containers
Reports Pod status
```

---

## 11. What is Kube-Proxy?

Kube-Proxy helps implement Kubernetes Service networking.

Depending on the networking implementation, it can configure packet forwarding/load-balancing rules using mechanisms such as:

```text
iptables
IPVS
```

Modern Kubernetes environments may also use alternatives such as eBPF-based networking that reduce or replace kube-proxy functionality.

---

## 12. What is a Container Runtime?

The Container Runtime runs containers.

Examples include:

```text
containerd
CRI-O
```

---

# Section 3 – Pods

## 13. What is a Pod?

A Pod is the smallest deployable unit in Kubernetes.

A Pod may contain:

```text
One Container
```

or:

```text
Multiple Containers
```

Containers in the same Pod share:

```text
Network Namespace
Pod IP
Volumes
```

---

## 14. Why are Pods ephemeral?

Pods are designed to be replaceable.

If a Pod fails:

```text
Pod Failure
    ↓
Controller
    ↓
New Pod
```

Applications should therefore not depend on a Pod's permanent identity unless using an appropriate workload such as StatefulSet.

---

## 15. What is a multi-container Pod?

A Pod can contain multiple closely related containers.

Example:

```text
Pod
├── Application
└── Sidecar
```

Common examples include:

```text
Logging Sidecar
Proxy Sidecar
Security Agent
```

---

## 16. Do containers inside a Pod have different IP addresses?

Normally, containers in the same Pod share the Pod's network namespace and therefore use the same Pod IP.

They can communicate through:

```text
localhost
```

using different ports.

---

# Section 4 – Deployments and Controllers

## 17. What is a ReplicaSet?

A ReplicaSet ensures that a specified number of Pod replicas exist.

Example:

```yaml
spec:
  replicas: 3
```

The ReplicaSet attempts to maintain:

```text
3 Running Pods
```

---

## 18. What is a Deployment?

A Deployment manages stateless application workloads and typically manages ReplicaSets.

It supports:

```text
Rolling Updates
Rollback
Scaling
Replica Management
```

---

## 19. Deployment vs ReplicaSet?

| Deployment | ReplicaSet |
|---|---|
| Higher-level controller | Lower-level controller |
| Manages ReplicaSets | Manages Pods |
| Supports rollout history | Maintains replica count |
| Supports rolling updates | Does not manage application rollout strategy |

---

## 20. What happens during a Deployment update?

Conceptually:

```text
Deployment
    ↓
New ReplicaSet
    ↓
New Pods
    ↓
Old ReplicaSet Scaled Down
```

---

## 21. What is a rolling update?

A rolling update gradually replaces old Pods with new Pods.

Example:

```text
v1 → v1 → v1

      ↓

v2 → v1 → v1

      ↓

v2 → v2 → v1

      ↓

v2 → v2 → v2
```

---

## 22. How do you rollback a Deployment?

```bash
kubectl rollout undo deployment/<deployment-name>
```

Check rollout history:

```bash
kubectl rollout history deployment/<deployment-name>
```

---

# Section 5 – StatefulSets

## 23. What is a StatefulSet?

StatefulSet manages workloads that require stable identity or persistent storage.

It provides characteristics such as:

```text
Stable Pod Names
Stable Network Identity
Ordered Operations
Persistent Storage Association
```

---

## 24. Deployment vs StatefulSet?

| Deployment | StatefulSet |
|---|---|
| Stateless workloads | Stateful workloads |
| Pods are interchangeable | Pods have stable identity |
| Random Pod names | Ordered names |
| Common web applications | Databases / clustered systems |

---

## 25. Example StatefulSet Pod names

```text
database-0
database-1
database-2
```

---

# Section 6 – DaemonSets

## 26. What is a DaemonSet?

A DaemonSet ensures that a Pod runs on eligible nodes.

Typical use cases:

```text
Log Collection
Monitoring Agents
Security Agents
Node Networking
```

---

## 27. DaemonSet vs Deployment?

```text
Deployment
→ Desired number of replicas

DaemonSet
→ Pod on each eligible node
```

---

# Section 7 – Jobs and CronJobs

## 28. What is a Job?

A Job runs a task until successful completion.

Example:

```text
Database Migration
Batch Processing
Data Processing
```

---

## 29. What is a CronJob?

A CronJob creates Jobs according to a schedule.

Example:

```text
Every Day at 02:00
```

---

# Section 8 – Services

## 30. What is a Kubernetes Service?

A Service provides a stable network endpoint for a group of Pods.

```text
Client
  ↓
Service
  ↓
Pods
```

---

## 31. Why do we need Services?

Pod IPs can change.

A Service provides:

```text
Stable DNS
Stable Virtual IP
Load Distribution
Service Discovery
```

---

## 32. What are common Service types?

```text
ClusterIP
NodePort
LoadBalancer
ExternalName
```

---

## 33. What is ClusterIP?

ClusterIP exposes a Service internally within the cluster.

```text
Pod
 ↓
ClusterIP Service
 ↓
Backend Pods
```

It is the default Service type.

---

## 34. What is NodePort?

NodePort exposes a Service through a port on each eligible node.

Conceptually:

```text
Client
 ↓
NodeIP:NodePort
 ↓
Service
 ↓
Pods
```

---

## 35. What is LoadBalancer?

LoadBalancer exposes a Service through an external load-balancing mechanism, typically provided by the cloud/platform environment.

---

## 36. What is ExternalName?

ExternalName maps a Service name to an external DNS name.

Example:

```yaml
spec:
  type: ExternalName
  externalName: example.com
```

---

# Section 9 – Ingress

## 37. What is Ingress?

Ingress provides HTTP/HTTPS routing into Kubernetes Services.

Example:

```text
Internet
   ↓
Ingress
   ├── /api → API Service
   └── /web → Web Service
```

---

## 38. What is an Ingress Controller?

An Ingress resource is only configuration.

An Ingress Controller implements the actual routing behavior.

Examples include controllers based on:

```text
NGINX
HAProxy
Traefik
Cloud Load Balancers
```

---

# Section 10 – Gateway API

## 39. What is Gateway API?

Gateway API is a Kubernetes networking API family designed to provide expressive and role-oriented traffic management.

Important resources include:

```text
GatewayClass
Gateway
HTTPRoute
GRPCRoute
TCPRoute
TLSRoute
```

---

## 40. Ingress vs Gateway API?

Ingress:

```text
Simpler
Older
HTTP/HTTPS Focused
```

Gateway API:

```text
More Expressive
Role-Oriented
Extensible
Supports Multiple Route Types
```

---

# Section 11 – ConfigMaps and Secrets

## 41. What is a ConfigMap?

ConfigMap stores non-sensitive configuration.

Examples:

```text
Environment Variables
Application Configuration
Command-Line Arguments
Configuration Files
```

---

## 42. What is a Secret?

Secret is designed to store sensitive configuration such as:

```text
Passwords
Tokens
API Keys
Certificates
```

However, Kubernetes Secrets are not automatically equivalent to a complete secrets-management system. Encryption at rest and access controls should be configured appropriately.

---

## 43. ConfigMap vs Secret?

| ConfigMap | Secret |
|---|---|
| Non-sensitive configuration | Sensitive data |
| Application settings | Credentials |
| Feature flags | Tokens |
| URLs | Certificates |

---

# Section 12 – Namespaces

## 44. What is a Namespace?

A Namespace provides a logical boundary for namespaced Kubernetes resources.

Example:

```text
production
staging
development
```

Namespaces can support:

```text
Resource Organization
RBAC
Resource Quotas
Network Policies
```

---

# Section 13 – Labels and Selectors

## 45. What are Labels?

Labels are key-value metadata used to identify and organize resources.

Example:

```yaml
labels:
  app: frontend
  environment: production
```

---

## 46. What are Selectors?

Selectors identify resources based on labels.

Example:

```yaml
selector:
  matchLabels:
    app: frontend
```

---

# Section 14 – Annotations

## 47. What are Annotations?

Annotations store non-identifying metadata associated with resources.

They are commonly used by:

```text
Ingress Controllers
Operators
Cloud Controllers
Monitoring Tools
```

---

# Section 15 – Kubernetes Networking

## 48. What are the fundamental Kubernetes networking requirements?

A typical Kubernetes networking model expects:

```text
Pod-to-Pod Communication
Node-to-Pod Communication
Pod-to-Service Communication
Service Discovery
```

---

## 49. What is a CNI plugin?

CNI stands for Container Network Interface.

CNI plugins provide container networking functionality.

Examples include:

```text
Calico
Cilium
Flannel
Antrea
```

---

## 50. What is CoreDNS?

CoreDNS provides cluster DNS.

It resolves Kubernetes service names such as:

```text
service.namespace.svc.cluster.local
```

---

# Section 16 – NetworkPolicy

## 51. What is NetworkPolicy?

NetworkPolicy controls network traffic to and/or from Pods.

Example:

```text
Frontend
   ↓ Allowed
Backend

Database
   ↓ Allowed only from Backend
```

---

## 52. What happens if no NetworkPolicy exists?

In many Kubernetes networking implementations, Pods are not isolated by NetworkPolicy by default.

Actual behavior depends on the CNI implementation and applied policies.

---

## 53. NetworkPolicy vs Service Mesh?

NetworkPolicy primarily provides network-level enforcement.

Service Mesh can provide:

```text
mTLS
Service Identity
L7 Routing
Application-Level Authorization
Traffic Management
```

They can complement each other.

---

# Section 17 – Volumes and Storage

## 54. What is a Volume?

A Volume provides storage accessible to containers in a Pod.

---

## 55. What is a PersistentVolume?

A PersistentVolume, or PV, is a cluster storage resource.

```text
Storage
   ↓
PersistentVolume
```

---

## 56. What is a PersistentVolumeClaim?

PVC is a request for storage.

```text
Pod
 ↓
PVC
 ↓
PV
 ↓
Storage
```

---

## 57. What is a StorageClass?

StorageClass defines how storage should be provisioned.

It commonly enables dynamic provisioning.

---

## 58. What is CSI?

CSI stands for Container Storage Interface.

CSI allows storage vendors to integrate storage systems with Kubernetes.

---

# Section 18 – Scheduling

## 59. What is Kubernetes Scheduling?

Scheduling determines which node should run a Pod.

The scheduler considers factors such as:

```text
Resource Requests
Node Constraints
Affinity
Anti-Affinity
Taints
Tolerations
Topology
```

---

## 60. What is nodeSelector?

nodeSelector schedules Pods onto nodes having specific labels.

Example:

```yaml
nodeSelector:
  disktype: ssd
```

---

## 61. What is Node Affinity?

Node Affinity provides more expressive node selection.

It supports:

```text
Required Rules
Preferred Rules
```

---

## 62. What is Pod Affinity?

Pod Affinity can place Pods near other Pods.

Example:

```text
Application
+
Cache
```

on the same topology domain.

---

## 63. What is Pod Anti-Affinity?

Pod Anti-Affinity helps spread Pods apart.

Example:

```text
Replica 1 → Node A
Replica 2 → Node B
Replica 3 → Node C
```

---

# Section 19 – Taints and Tolerations

## 64. What is a Taint?

A taint marks a node so that Pods without a matching toleration are prevented from scheduling there, depending on the effect.

---

## 65. What is a Toleration?

A toleration allows a Pod to tolerate a matching node taint.

---

## 66. Taint vs Toleration?

```text
Taint
→ Applied to Node

Toleration
→ Applied to Pod
```

---

# Section 20 – Resources

## 67. What are resource requests?

Requests specify the resources a Pod needs for scheduling.

Example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
```

---

## 68. What are resource limits?

Limits specify the maximum resource usage allowed for a container.

Example:

```yaml
resources:
  limits:
    cpu: "1"
    memory: "1Gi"
```

---

## 69. Requests vs Limits?

```text
Request
→ Scheduling expectation

Limit
→ Maximum resource boundary
```

---

# Section 21 – Autoscaling

## 70. What is HPA?

Horizontal Pod Autoscaler changes the number of Pod replicas based on metrics.

```text
Load ↑
 ↓
HPA
 ↓
Replicas ↑
```

---

## 71. What is VPA?

Vertical Pod Autoscaler adjusts resource requests and limits based on observed usage, depending on configuration and update mode.

```text
CPU Need ↑
 ↓
VPA
 ↓
Resource Recommendation / Update
```

---

## 72. What is Cluster Autoscaler?

Cluster Autoscaler changes the number of nodes in the cluster based on scheduling and capacity requirements.

```text
Pending Pods
 ↓
Insufficient Capacity
 ↓
Cluster Autoscaler
 ↓
Add Nodes
```

---

# Section 22 – Kubernetes Security

## 73. What is RBAC?

RBAC stands for Role-Based Access Control.

It controls:

```text
Who
Can Perform What
On Which Resources
```

---

## 74. Role vs ClusterRole?

```text
Role
→ Namespace-scoped permissions

ClusterRole
→ Cluster-scoped permissions
```

A ClusterRole can also be bound within a namespace using a RoleBinding.

---

## 75. RoleBinding vs ClusterRoleBinding?

```text
RoleBinding
→ Grants permissions within a namespace

ClusterRoleBinding
→ Grants ClusterRole permissions cluster-wide
```

---

## 76. What is a ServiceAccount?

A ServiceAccount provides an identity for workloads running inside Kubernetes.

---

## 77. What is an Admission Controller?

Admission controllers intercept API requests after authentication/authorization and before persistence, allowing requests to be validated or mutated.

---

## 78. What are Pod Security Standards?

Pod Security Standards define security profiles for Pods.

Common profiles include:

```text
Privileged
Baseline
Restricted
```

---

# Section 23 – Secret Management

## 79. Are Kubernetes Secrets encrypted?

Kubernetes Secret objects are encoded rather than inherently encrypted merely because they are represented as base64.

Encryption at rest can be configured for Kubernetes data in etcd.

---

## 80. How should secrets be secured?

Use:

```text
Encryption at Rest
RBAC
External Secret Managers
Secret Rotation
Least Privilege
Audit Logging
```

---

# Section 24 – Image Security

## 81. How do you secure container images?

Use:

```text
Trusted Registries
Minimal Images
Image Scanning
SBOM
Image Signing
Digest Pinning
Regular Updates
```

---

## 82. What is an image digest?

An image digest uniquely identifies a specific image content.

Example:

```text
image@sha256:<digest>
```

Digest pinning improves deployment reproducibility.

---

# Section 25 – Observability

## 83. What are the three major observability signals?

Commonly:

```text
Metrics
Logs
Traces
```

---

## 84. What is Prometheus?

Prometheus is a monitoring and metrics system widely used with Kubernetes.

---

## 85. What is Grafana?

Grafana is a visualization and dashboarding platform that can display metrics and other observability data.

---

## 86. What is Alertmanager?

Alertmanager handles Prometheus alerts and supports functions such as:

```text
Grouping
Routing
Silencing
Inhibition
Notifications
```

---

## 87. What is OpenTelemetry?

OpenTelemetry is a vendor-neutral observability framework for collecting and exporting telemetry such as:

```text
Traces
Metrics
Logs
```

---

# Section 26 – Logging

## 88. How do you view Pod logs?

```bash
kubectl logs <pod>
```

For a specific container:

```bash
kubectl logs <pod> -c <container>
```

For previous container instance:

```bash
kubectl logs <pod> --previous
```

---

# Section 27 – Troubleshooting

## 89. A Pod is stuck in Pending. What do you check?

Check:

```bash
kubectl describe pod <pod>
```

Then investigate:

```text
Insufficient CPU
Insufficient Memory
Node Selector
Node Affinity
Taints
Tolerations
PVC
Scheduling Constraints
Resource Quotas
```

---

## 90. A Pod is CrashLoopBackOff. What do you check?

Check:

```bash
kubectl logs <pod>
```

Then:

```bash
kubectl logs <pod> --previous
```

Also:

```bash
kubectl describe pod <pod>
```

Investigate:

```text
Application Crash
Configuration
Secret
ConfigMap
Probe Failure
Permissions
Resource Limits
Dependency Failure
```

---

## 91. What does ImagePullBackOff mean?

It means Kubernetes is repeatedly failing to pull the container image.

Possible causes:

```text
Wrong Image Name
Wrong Tag
Private Registry
Missing ImagePullSecret
Registry Authentication Failure
Network Problem
Image Does Not Exist
```

---

## 92. A Service cannot reach a Pod. What do you check?

Check:

```bash
kubectl get svc
kubectl get endpoints
kubectl get endpointslices
```

Then verify:

```text
Service Selector
Pod Labels
Pod Readiness
Port
TargetPort
NetworkPolicy
DNS
```

---

## 93. DNS is failing. What do you check?

Check:

```bash
kubectl get pods -n kube-system
```

Identify CoreDNS Pods.

Then:

```bash
kubectl logs -n kube-system <coredns-pod>
```

Also test DNS from a debugging Pod.

---

# Section 28 – Production Questions

## 94. How would you design a production Kubernetes cluster?

Consider:

```text
High Availability
Multiple Control-Plane Nodes
Worker Node Distribution
Networking
Storage
Security
Observability
Backup
Disaster Recovery
Autoscaling
Resource Management
Upgrade Strategy
```

---

## 95. How many control-plane nodes should a production cluster have?

A common HA design uses an odd number such as:

```text
3
5
```

for quorum-based control-plane components such as etcd.

The correct number depends on availability requirements and failure-domain design.

---

## 96. Why use multiple availability zones?

To reduce the impact of a failure affecting a single zone.

Example:

```text
Zone A
Zone B
Zone C
```

Workloads can be distributed across zones.

---

# Section 29 – High Availability

## 97. How do you make Kubernetes highly available?

Use:

```text
Multiple Control-Plane Nodes
etcd Quorum
Load-Balanced API Server
Multiple Worker Nodes
Multiple Availability Zones
Replicated Applications
Redundant Networking
```

---

# Section 30 – Backup and Restore

## 98. What should be backed up?

Important components include:

```text
etcd
Application Data
Persistent Volumes
Cluster Configuration
Secrets
Custom Resources
```

The exact backup strategy depends on the cluster architecture.

---

## 99. Why is etcd backup important?

etcd contains critical Kubernetes cluster state.

Loss of etcd data can result in loss of cluster configuration and object state.

---

# Section 31 – Upgrades

## 100. How do you upgrade Kubernetes safely?

Typical process:

```text
Review Compatibility
 ↓
Backup
 ↓
Test
 ↓
Upgrade Control Plane
 ↓
Upgrade Nodes
 ↓
Validate Workloads
 ↓
Monitor
```

---

# Section 32 – Security Interview Questions

## 101. How would you secure a Kubernetes cluster?

Use:

```text
RBAC
NetworkPolicy
Pod Security Standards
Secret Management
Image Security
Admission Controls
Audit Logging
Runtime Security
Least Privilege
Node Hardening
```

---

## 102. What is the principle of least privilege?

Grant only the permissions required to perform the intended operation.

---

## 103. How do you secure the Kubernetes API Server?

Controls can include:

```text
Strong Authentication
RBAC
Network Restrictions
TLS
Audit Logging
Admission Controls
```

---

## 104. How do you secure workloads?

Use:

```text
Non-Root Containers
Read-Only Filesystems Where Possible
Dropped Linux Capabilities
No Privilege Escalation
Resource Limits
NetworkPolicy
Image Scanning
Pod Security Standards
```

---

# Section 33 – Scenario-Based Questions

## Scenario 1 – Pod Pending

### Question

> A Pod remains in Pending state. What will you do?

### Answer

Start with:

```bash
kubectl describe pod <pod>
```

Check scheduler events.

Then investigate:

```text
CPU
Memory
Taints
Tolerations
Affinity
NodeSelector
PVC
Topology Constraints
ResourceQuota
```

---

# Scenario 2 – Pod CrashLoopBackOff

### Question

> A production Pod is repeatedly restarting.

### Answer

Check:

```bash
kubectl logs <pod> --previous
kubectl describe pod <pod>
```

Investigate:

```text
Application Error
Configuration
Secrets
Probes
Dependencies
OOMKilled
Permissions
```

---

# Scenario 3 – Service Returns Connection Refused

### Question

> The Service exists, but clients cannot connect.

### Answer

Check:

```text
Service Selector
Endpoints
Pod Readiness
Service Port
TargetPort
Container Port
NetworkPolicy
Application Listener
```

Commands:

```bash
kubectl get svc
kubectl get endpoints
kubectl get endpointslices
```

---

# Scenario 4 – Service Has No Endpoints

### Question

> Why does a Service have no endpoints?

Possible causes:

```text
Selector Does Not Match Pod Labels
Pods Not Ready
Pods Do Not Exist
Readiness Conditions
Incorrect Namespace
```

---

# Scenario 5 – Deployment Rollout Stuck

### Question

> A Deployment update never completes.

Check:

```bash
kubectl rollout status deployment/<name>
kubectl describe deployment/<name>
```

Then inspect:

```text
New Pods
Image Pulling
Readiness Probes
Resource Constraints
Scheduling
Application Startup
```

---

# Scenario 6 – Node NotReady

### Question

> A node becomes NotReady.

Check:

```bash
kubectl describe node <node>
```

Investigate:

```text
Kubelet
Container Runtime
Disk Pressure
Memory Pressure
Network
Certificates
Node Conditions
```

---

# Scenario 7 – DNS Failure

### Question

> Pods cannot resolve Kubernetes Services.

Check:

```text
CoreDNS Pods
CoreDNS Logs
DNS Service
NetworkPolicy
Pod DNS Configuration
CNI
```

---

# Scenario 8 – High Memory Usage

### Question

> A workload keeps consuming memory.

Check:

```bash
kubectl top pod
kubectl describe pod <pod>
```

Investigate:

```text
Memory Requests
Memory Limits
Application Leak
Traffic Increase
Workload Pattern
OOMKilled Events
```

---

# Scenario 9 – HPA Not Scaling

### Question

> HPA exists but replicas do not increase.

Check:

```bash
kubectl get hpa
kubectl describe hpa <name>
```

Investigate:

```text
Metrics Server
CPU Requests
Target Metrics
Current Metrics
Resource Availability
```

---

# Scenario 10 – PVC Pending

### Question

> A PVC is stuck in Pending.

Check:

```bash
kubectl describe pvc <name>
```

Investigate:

```text
StorageClass
CSI Driver
Available PV
Capacity
Access Modes
Topology
Provisioner
```

---

# Scenario 11 – ImagePullBackOff

### Question

> A Pod cannot start because the image cannot be pulled.

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
Authentication
Registry
Image Name
Tag
ImagePullSecrets
Network
```

---

# Scenario 12 – Unauthorized API Request

### Question

> A Pod receives HTTP 403 when accessing the Kubernetes API.

Check:

```text
ServiceAccount
Role / ClusterRole
RoleBinding / ClusterRoleBinding
Namespace
Requested Resource
Requested Verb
```

---

# Scenario 13 – NetworkPolicy Blocks Traffic

### Question

> Two Pods cannot communicate after a NetworkPolicy was applied.

Check:

```text
Ingress Rules
Egress Rules
Pod Selectors
Namespace Selectors
Ports
Protocol
```

---

# Scenario 14 – Node Has No Available Capacity

### Question

> New Pods cannot be scheduled because all nodes lack capacity.

Possible solutions:

```text
Add Nodes
Cluster Autoscaler
Optimize Requests
Move Workloads
Increase Node Size
```

---

# Scenario 15 – Database Pod Restarted

### Question

> A database Pod restarted unexpectedly.

Do not immediately delete resources.

Investigate:

```text
Events
Logs
Previous Logs
OOMKilled
Node Failure
Storage
Probes
Application Errors
```

For stateful systems, protect persistent data and verify recovery behavior.

---

# Section 34 – Security Scenarios

## Scenario 16 – Compromised Pod

### Question

> You suspect a Pod has been compromised.

Possible response:

```text
Identify Workload
 ↓
Contain Network Access
 ↓
Preserve Evidence
 ↓
Inspect Logs
 ↓
Review Process Activity
 ↓
Review Kubernetes Audit Logs
 ↓
Rotate Credentials
 ↓
Replace Workload
 ↓
Investigate Root Cause
```

Do not destroy evidence before deciding what forensic information needs to be preserved.

---

# Scenario 17 – Suspicious Service Account

### Question

> A ServiceAccount appears to have excessive permissions.

Check:

```bash
kubectl get rolebinding -A
kubectl get clusterrolebinding
```

Determine:

```text
Who uses the ServiceAccount?
What permissions exist?
Are they required?
```

Then reduce permissions according to least privilege.

---

# Scenario 18 – Exposed Kubernetes API

### Question

> The Kubernetes API Server is unnecessarily exposed to the public internet.

Treat this as a high-priority security issue.

Review:

```text
Network Exposure
Authentication
Authorization
Firewall Rules
API Server Configuration
Audit Logs
Access History
Credentials
```

---

# Section 35 – Kubernetes Networking Interview

## 105. Explain Pod-to-Pod communication.

A typical Kubernetes networking model gives each Pod an IP address and allows Pods to communicate without requiring NAT between Pods.

The exact implementation is provided by the cluster's networking solution.

---

## 106. Explain Service-to-Pod communication.

```text
Client
 ↓
Service Virtual IP
 ↓
Service Routing
 ↓
Selected Pod
```

---

## 107. What is kube-proxy?

kube-proxy helps implement Service networking on nodes in traditional Kubernetes networking architectures.

---

## 108. What is CNI?

CNI provides a standard interface for configuring container networking.

---

# Section 36 – Storage Interview

## 109. PV vs PVC?

```text
PV
→ Storage Resource

PVC
→ Storage Request
```

---

## 110. What is dynamic provisioning?

Dynamic provisioning automatically creates storage when a PVC requests it.

```text
PVC
 ↓
StorageClass
 ↓
CSI Provisioner
 ↓
PV
 ↓
Storage
```

---

# Section 37 – Scheduling Interview

## 111. NodeSelector vs NodeAffinity?

```text
nodeSelector
→ Simple node label matching

NodeAffinity
→ More expressive rules
```

---

## 112. Taint vs Toleration?

```text
Taint
→ Node restriction

Toleration
→ Pod permission to tolerate matching taint
```

---

# Section 38 – Autoscaling Interview

## 113. HPA vs VPA vs Cluster Autoscaler?

| Autoscaler | Changes |
|---|---|
| HPA | Number of Pod replicas |
| VPA | Pod resource requests/limits recommendations or updates |
| Cluster Autoscaler | Number of nodes |

---

# Section 39 – Kubernetes Objects Interview

## 114. What is the difference between a Deployment and StatefulSet?

Deployment:

```text
Stateless
Interchangeable Pods
```

StatefulSet:

```text
Stable Identity
Stable Storage
Ordered Operations
```

---

## 115. Deployment vs DaemonSet?

```text
Deployment
→ Desired number of replicas

DaemonSet
→ One Pod on each eligible node
```

---

## 116. Job vs CronJob?

```text
Job
→ One-off task

CronJob
→ Scheduled Jobs
```

---

# Section 40 – Production Design

## 117. Design a production Kubernetes platform.

A production platform could look like:

```text
                         Users
                           │
                           ▼
                    External Gateway
                           │
                           ▼
                    Kubernetes Cluster
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     Zone A             Zone B             Zone C
        │                  │                  │
     Workers            Workers            Workers
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    Application Layer
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Services      Storage      Messaging
              │
              ▼
        Observability
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
    Metrics  Logs  Traces
```

Security:

```text
RBAC
NetworkPolicy
Pod Security
Image Security
Secret Management
Runtime Security
Audit Logging
```

Operations:

```text
Backup
Upgrade
DR
Monitoring
Autoscaling
Capacity Planning
```

---

# Section 41 – Hands-on Interview Tasks

## Task 1 – Create a Deployment

Create an NGINX Deployment with:

```text
3 replicas
```

Verify:

```bash
kubectl get deployment
kubectl get pods
```

---

## Task 2 – Expose the Deployment

Create a ClusterIP Service.

Verify:

```bash
kubectl get svc
```

---

## Task 3 – Scale the Deployment

```bash
kubectl scale deployment <name> --replicas=5
```

---

## Task 4 – Perform a Rolling Update

Update the image:

```bash
kubectl set image deployment/<name> nginx=nginx:<version>
```

Check:

```bash
kubectl rollout status deployment/<name>
```

---

## Task 5 – Rollback

```bash
kubectl rollout undo deployment/<name>
```

---

## Task 6 – Create a ConfigMap

```bash
kubectl create configmap app-config \
  --from-literal=ENV=production
```

---

## Task 7 – Create a Secret

```bash
kubectl create secret generic app-secret \
  --from-literal=password='example'
```

Use secure handling practices in real environments.

---

## Task 8 – Debug a Pod

Given:

```text
CrashLoopBackOff
```

identify the cause using:

```bash
kubectl logs
kubectl logs --previous
kubectl describe pod
```

---

## Task 9 – Debug a Service

Given:

```text
Service has no endpoints
```

identify the mismatch between:

```text
Service Selector
Pod Labels
```

---

## Task 10 – Configure NetworkPolicy

Allow:

```text
frontend → backend
```

and deny unrelated traffic.

---

# Section 42 – Frequently Confused Concepts

## Pod vs Container

```text
Container
→ Application execution environment

Pod
→ Kubernetes deployment unit containing one or more containers
```

---

## Deployment vs StatefulSet

```text
Deployment
→ Stateless

StatefulSet
→ Stable Identity / Stateful
```

---

## Service vs Ingress

```text
Service
→ Exposes application inside or outside cluster depending on type

Ingress
→ HTTP/HTTPS routing into Services
```

---

## ConfigMap vs Secret

```text
ConfigMap
→ Non-sensitive configuration

Secret
→ Sensitive data
```

---

## PV vs PVC

```text
PV
→ Storage resource

PVC
→ Storage request
```

---

## Role vs ClusterRole

```text
Role
→ Namespace-scoped

ClusterRole
→ Cluster-scoped permissions definition
```

---

## RoleBinding vs ClusterRoleBinding

```text
RoleBinding
→ Namespace-scoped binding

ClusterRoleBinding
→ Cluster-wide binding
```

---

## HPA vs VPA

```text
HPA
→ More/Fewer Pods

VPA
→ More/Less Resources per Pod
```

---

## NodeSelector vs Affinity

```text
NodeSelector
→ Simple matching

Affinity
→ Advanced matching
```

---

## Taint vs Toleration

```text
Taint
→ Node

Toleration
→ Pod
```

---

## NetworkPolicy vs Service Mesh

```text
NetworkPolicy
→ Network-Level Controls

Service Mesh
→ Service-Level Networking
```

---

# Section 43 – 1-Line Oral Interview Questions

These are particularly useful for rapid technical interviews.

### What is Kubernetes?

Container orchestration platform for managing containerized workloads.

### What is a Pod?

Smallest deployable unit in Kubernetes.

### What is a Deployment?

Controller for managing stateless application replicas and rollout history.

### What is a ReplicaSet?

Ensures a desired number of Pod replicas exist.

### What is StatefulSet?

Controller for workloads requiring stable identity and/or persistent storage.

### What is DaemonSet?

Ensures a Pod runs on each eligible node.

### What is a Service?

Stable network endpoint for accessing a group of Pods.

### What is ClusterIP?

Internal Service IP.

### What is NodePort?

Exposes a Service through a port on nodes.

### What is Ingress?

HTTP/HTTPS routing into Kubernetes Services.

### What is Gateway API?

Kubernetes API family for expressive traffic management.

### What is ConfigMap?

Stores non-sensitive configuration.

### What is Secret?

Stores sensitive configuration data.

### What is Namespace?

Logical boundary for namespaced resources.

### What is CNI?

Container Network Interface.

### What is CoreDNS?

Cluster DNS service.

### What is NetworkPolicy?

Controls allowed network traffic to/from Pods.

### What is PV?

Persistent storage resource.

### What is PVC?

Request for persistent storage.

### What is StorageClass?

Defines storage provisioning behavior.

### What is CSI?

Container Storage Interface.

### What is Scheduler?

Assigns unscheduled Pods to nodes.

### What is nodeSelector?

Simple node label-based scheduling constraint.

### What is Node Affinity?

Advanced node selection rules.

### What is Taint?

Node-level scheduling restriction.

### What is Toleration?

Pod configuration allowing it to tolerate a matching taint.

### What is HPA?

Scales Pod replicas.

### What is VPA?

Adjusts/recommends Pod resource allocation.

### What is Cluster Autoscaler?

Adjusts cluster node count.

### What is RBAC?

Role-Based Access Control.

### What is ServiceAccount?

Identity used by workloads.

### What is an Admission Controller?

Component that validates or mutates API requests during admission.

### What is etcd?

Distributed key-value store containing Kubernetes state.

### What is Kubelet?

Node agent responsible for running and monitoring Pods.

### What is kube-proxy?

Component traditionally responsible for implementing Kubernetes Service networking.

### What is a Container Runtime?

Software that runs containers.

### What is Prometheus?

Metrics monitoring and alerting system.

### What is Grafana?

Observability visualization platform.

### What is OpenTelemetry?

Open observability framework for telemetry collection and export.

### What is an Operator?

Application-specific Kubernetes controller that automates operational tasks.

### What is a Service Mesh?

Infrastructure layer for service-to-service communication.

---

# Section 44 – Advanced Rapid-Fire Questions

## 1. Why are Pods ephemeral?

Because Kubernetes controllers replace failed or outdated Pods rather than treating individual Pods as permanent infrastructure.

---

## 2. Why should applications not depend on Pod IPs?

Pod IPs can change when Pods are recreated.

Use Services for stable connectivity.

---

## 3. Why are readiness probes important?

They determine whether a Pod should receive traffic.

---

## 4. Why are liveness probes important?

They can detect containers that need to be restarted.

---

## 5. Why are startup probes useful?

They allow slow-starting applications time to initialize before liveness/readiness behavior takes effect.

---

## 6. Why use resource requests?

They help the scheduler determine whether a node has sufficient capacity.

---

## 7. Why use resource limits?

They place boundaries on container resource consumption.

---

## 8. Why use namespaces?

They provide organization and a scope for many policies and resources.

---

## 9. Why use NetworkPolicy?

To reduce unauthorized network communication.

---

## 10. Why use RBAC?

To enforce least-privilege access to the Kubernetes API.

---

# Section 45 – Senior-Level Scenario Questions

## Scenario 19 – Cluster Outage

### Question

> Your entire production cluster becomes unavailable. What do you do?

### Answer

Follow the incident response process:

```text
Detect
 ↓
Assess Impact
 ↓
Declare Incident
 ↓
Check Control Plane
 ↓
Check Networking
 ↓
Check Nodes
 ↓
Check Storage
 ↓
Check External Dependencies
 ↓
Restore Service
 ↓
Validate
 ↓
Monitor
 ↓
Root Cause Analysis
```

If recovery is impossible:

```text
Disaster Recovery
 ↓
Restore Cluster State
 ↓
Restore Applications
 ↓
Restore Data
```

---

# Scenario 20 – etcd Failure

### Question

> What happens if etcd becomes unavailable?

The Kubernetes API Server may lose access to cluster state.

Potential effects include:

```text
API Operations Failing
Control Plane Degradation
Scheduling Problems
Controller Problems
```

Existing workloads may continue running for some time depending on what components remain healthy, but cluster management can be severely affected.

---

# Scenario 21 – Node Failure

### Question

> What happens when a worker node fails?

Kubernetes detects the node condition and, depending on workload configuration and controller behavior:

```text
Node Failure
 ↓
Pod Loss
 ↓
Controller Detects Missing Replicas
 ↓
New Pods Scheduled
 ↓
Healthy Nodes
```

Persistent workloads require appropriate storage and recovery design.

---

# Scenario 22 – API Server High Latency

### Question

> The Kubernetes API Server is responding slowly.

Investigate:

```text
API Server CPU
API Server Memory
etcd Latency
API Request Rate
Admission Webhooks
Network
Large API Objects
Controllers
```

Admission webhooks are particularly important because poorly performing webhooks can increase API request latency.

---

# Scenario 23 – etcd High Latency

Check:

```text
Disk I/O
CPU
Memory
Network
Database Size
Defragmentation
Request Rate
Member Health
```

etcd is sensitive to storage and network performance.

---

# Scenario 24 – Kubernetes Security Incident

### Question

> You detect suspicious activity in a Kubernetes cluster. What evidence do you investigate?

Potential evidence sources include:

```text
Kubernetes Audit Logs
API Server Logs
Container Logs
Node Logs
Runtime Events
Network Telemetry
Service Mesh Telemetry
Cloud Audit Logs
Process Activity
Identity Information
```

Preserve relevant evidence before destructive remediation where possible.

---

# Section 46 – Kubernetes Security Interview Checklist

```text
☑ Authentication
☑ Authorization
☑ RBAC
☑ ServiceAccounts
☑ Admission Controllers
☑ Pod Security Standards
☑ NetworkPolicy
☑ Secrets
☑ Encryption at Rest
☑ TLS
☑ mTLS
☑ Image Scanning
☑ Image Signing
☑ SBOM
☑ Runtime Security
☑ Audit Logging
☑ Node Security
☑ Supply Chain Security
☑ Least Privilege
```

---

# Section 47 – Kubernetes Troubleshooting Framework

When troubleshooting Kubernetes, follow:

```text
1. Identify
2. Observe
3. Isolate
4. Test
5. Remediate
6. Validate
7. Monitor
8. Document
```

---

# Layered Troubleshooting Model

```text
Application
    ↓
Container
    ↓
Pod
    ↓
Service
    ↓
DNS
    ↓
Network
    ↓
Node
    ↓
Control Plane
    ↓
External Dependencies
```

This prevents random troubleshooting.

---

# Essential Troubleshooting Commands

## Cluster

```bash
kubectl cluster-info
kubectl get nodes
kubectl get componentstatuses
```

Note: `kubectl get componentstatuses` is deprecated in modern Kubernetes and may not provide useful information. Prefer checking the health of the actual control-plane components and APIs.

---

## Pods

```bash
kubectl get pods -A
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

---

## Deployments

```bash
kubectl get deployments -A
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>
```

---

## Services

```bash
kubectl get svc -A
kubectl get endpoints -A
kubectl get endpointslices -A
```

---

## Nodes

```bash
kubectl get nodes
kubectl describe node <node>
```

---

## Events

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

---

## Resources

```bash
kubectl top nodes
kubectl top pods -A
```

---

## Storage

```bash
kubectl get pv
kubectl get pvc -A
kubectl get storageclass
```

---

## RBAC

```bash
kubectl get roles -A
kubectl get rolebindings -A
kubectl get clusterroles
kubectl get clusterrolebindings
```

---

# Section 48 – Interview Answer Framework

For scenario questions, use:

```text
Problem
 ↓
Observation
 ↓
Commands
 ↓
Possible Causes
 ↓
Isolation
 ↓
Fix
 ↓
Validation
 ↓
Prevention
```

Example:

```text
"Pod is failing"

1. Check status
2. Describe Pod
3. Check current logs
4. Check previous logs
5. Check events
6. Identify root cause
7. Apply minimal fix
8. Verify recovery
9. Add preventive monitoring
```

This approach demonstrates practical troubleshooting rather than memorized commands.

---

# Section 49 – How to Answer Kubernetes Interview Questions

## Basic Question

Give:

```text
Definition
+
One Example
```

---

## Intermediate Question

Give:

```text
Definition
+
How It Works
+
Example
```

---

## Scenario Question

Give:

```text
Problem
+
Investigation
+
Commands
+
Root Cause
+
Fix
+
Validation
```

---

## Architecture Question

Give:

```text
Components
+
Data Flow
+
Failure Handling
+
Security
+
Observability
```

---

# Section 50 – Common Interview Mistakes

## Mistake 1

Saying:

> "A Pod is a container."

Correct:

> A Pod is the smallest Kubernetes deployable unit and can contain one or more containers.

---

## Mistake 2

Saying:

> "Secrets are encrypted because they are base64."

Incorrect.

Base64 is encoding, not encryption.

---

## Mistake 3

Saying:

> "HPA increases CPU."

Incorrect.

HPA changes the number of Pod replicas.

---

## Mistake 4

Saying:

> "VPA adds Pods."

Incorrect.

VPA adjusts or recommends resource allocation for Pods.

---

## Mistake 5

Saying:

> "Toleration attracts Pods to a node."

Incorrect.

A toleration allows a Pod to be scheduled onto a node with a matching taint; it does not by itself force scheduling there.

---

## Mistake 6

Saying:

> "NetworkPolicy encrypts traffic."

Incorrect.

NetworkPolicy controls network connectivity. It does not provide encryption.

---

## Mistake 7

Saying:

> "Service IP belongs to the Pod."

Incorrect.

A Service provides a stable virtual networking abstraction in front of selected Pods.

---

# Section 51 – Kubernetes Architecture Cheat Sheet

```text
                         Kubernetes
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
          Control Plane                Worker Nodes
                │                           │
        ┌───────┼────────┐          ┌───────┼────────┐
        ▼       ▼        ▼          ▼       ▼        ▼
      API     etcd   Scheduler    Kubelet Runtime kube-proxy
     Server
                │
                ▼
          Controllers
```

---

# Kubernetes Workload Cheat Sheet

```text
Deployment
→ Stateless Applications

StatefulSet
→ Stateful Applications

DaemonSet
→ One Pod per Eligible Node

Job
→ One-Time Task

CronJob
→ Scheduled Task
```

---

# Kubernetes Networking Cheat Sheet

```text
Pod
 ↓
Service
 ↓
Ingress / Gateway
 ↓
External Traffic
```

Core components:

```text
CNI
CoreDNS
Service
Ingress
Gateway API
NetworkPolicy
```

---

# Kubernetes Storage Cheat Sheet

```text
Pod
 ↓
PVC
 ↓
PV
 ↓
StorageClass / CSI
 ↓
Storage Backend
```

---

# Kubernetes Security Cheat Sheet

```text
Authentication
      ↓
Authorization
      ↓
Admission
      ↓
Pod Security
      ↓
Network Security
      ↓
Runtime Security
      ↓
Audit
```

---

# Kubernetes Scheduling Cheat Sheet

```text
Pod
 ↓
Scheduler
 ↓
Requests
 ↓
NodeSelector / Affinity
 ↓
Taints / Tolerations
 ↓
Topology
 ↓
Node
```

---

# Kubernetes Autoscaling Cheat Sheet

```text
HPA
→ Pod Count

VPA
→ Pod Resources

Cluster Autoscaler
→ Node Count
```

---

# Kubernetes Observability Cheat Sheet

```text
Logs
 ↓
Metrics
 ↓
Traces
 ↓
Alerts
 ↓
Incident Response
```

Common stack:

```text
Prometheus
Grafana
Alertmanager
OpenTelemetry
```

---

# Kubernetes Security Operations Cheat Sheet

```text
Vulnerability
 ↓
Detection
 ↓
Investigation
 ↓
Containment
 ↓
Eradication
 ↓
Recovery
 ↓
Lessons Learned
```

---

# Top 25 Kubernetes Questions to Memorize

1. What is Kubernetes?
2. What is a Pod?
3. What is a Deployment?
4. Deployment vs StatefulSet?
5. Deployment vs DaemonSet?
6. What is a Service?
7. ClusterIP vs NodePort vs LoadBalancer?
8. What is Ingress?
9. What is Gateway API?
10. What is a ConfigMap?
11. What is a Secret?
12. What is a Namespace?
13. What is a CNI?
14. What is CoreDNS?
15. What is NetworkPolicy?
16. What is PV?
17. What is PVC?
18. What is StorageClass?
19. What is CSI?
20. What is RBAC?
21. What is a ServiceAccount?
22. What are requests and limits?
23. HPA vs VPA vs Cluster Autoscaler?
24. What are taints and tolerations?
25. How do you troubleshoot a failing Pod?

---

# Top 25 Kubernetes Security Questions

1. How do you secure Kubernetes?
2. What is RBAC?
3. Role vs ClusterRole?
4. RoleBinding vs ClusterRoleBinding?
5. What is a ServiceAccount?
6. What is Pod Security Standards?
7. What are admission controllers?
8. How do you secure Secrets?
9. Are Kubernetes Secrets encrypted by default?
10. How do you secure container images?
11. What is image signing?
12. What is an SBOM?
13. What is NetworkPolicy?
14. NetworkPolicy vs Service Mesh?
15. How do you implement least privilege?
16. How do you secure the API Server?
17. How do you secure kubelet?
18. What is Kubernetes audit logging?
19. How do you detect compromised Pods?
20. How do you rotate credentials?
21. How do you prevent privilege escalation?
22. Why avoid privileged containers?
23. What is runtime security?
24. What is supply-chain security?
25. How would you investigate a Kubernetes security incident?

---

# Top 25 Troubleshooting Questions

1. Pod stuck in Pending?
2. Pod in CrashLoopBackOff?
3. ImagePullBackOff?
4. Pod keeps restarting?
5. Service has no endpoints?
6. DNS is failing?
7. Node is NotReady?
8. Deployment rollout stuck?
9. HPA not scaling?
10. PVC stuck in Pending?
11. Container OOMKilled?
12. Readiness probe failing?
13. Liveness probe failing?
14. Service returns connection refused?
15. NetworkPolicy blocks traffic?
16. Ingress returns 404?
17. Ingress returns 502?
18. API Server is slow?
19. etcd is slow?
20. Node disk pressure?
21. Node memory pressure?
22. Pods cannot schedule?
23. CSI volume mount failing?
24. RBAC returns 403?
25. Service Mesh mTLS failure?

---

# Interview Preparation Strategy

## Level 1 – Fundamentals

Master:

```text
Pod
Deployment
Service
Namespace
ConfigMap
Secret
```

---

## Level 2 – Networking

Master:

```text
Service
Ingress
Gateway API
CNI
CoreDNS
NetworkPolicy
```

---

## Level 3 – Storage

Master:

```text
Volume
PV
PVC
StorageClass
CSI
```

---

## Level 4 – Scheduling

Master:

```text
Scheduler
Requests
Limits
Affinity
Anti-Affinity
Taints
Tolerations
```

---

## Level 5 – Security

Master:

```text
RBAC
ServiceAccounts
Secrets
Pod Security
NetworkPolicy
Admission
Image Security
Runtime Security
```

---

## Level 6 – Operations

Master:

```text
Monitoring
Logging
Backup
Restore
Upgrade
HA
DR
Troubleshooting
```

---

## Level 7 – Advanced

Master:

```text
GitOps
Helm
Kustomize
Operators
Service Mesh
CI/CD
Production Architecture
```

---

# 30-Minute Kubernetes Revision Plan

## 0–5 Minutes

Architecture:

```text
API Server
etcd
Scheduler
Controller Manager
Kubelet
Runtime
kube-proxy
```

---

## 5–10 Minutes

Workloads:

```text
Pod
Deployment
StatefulSet
DaemonSet
Job
CronJob
```

---

## 10–15 Minutes

Networking:

```text
Service
Ingress
Gateway API
CNI
CoreDNS
NetworkPolicy
```

---

## 15–20 Minutes

Storage + Scheduling:

```text
PV
PVC
StorageClass
CSI
Affinity
Taints
Tolerations
Requests
Limits
```

---

## 20–25 Minutes

Security:

```text
RBAC
ServiceAccount
Secrets
Admission
Pod Security
Image Security
NetworkPolicy
```

---

## 25–30 Minutes

Troubleshooting:

```text
Pending
CrashLoopBackOff
ImagePullBackOff
NotReady
DNS Failure
Service Failure
PVC Pending
RBAC Failure
```

---

# Final Interview Cheat Sheet

```text
Kubernetes
│
├── Architecture
│   ├── API Server
│   ├── etcd
│   ├── Scheduler
│   └── Controllers
│
├── Nodes
│   ├── Kubelet
│   ├── Runtime
│   └── kube-proxy
│
├── Workloads
│   ├── Pod
│   ├── Deployment
│   ├── StatefulSet
│   ├── DaemonSet
│   ├── Job
│   └── CronJob
│
├── Networking
│   ├── Service
│   ├── Ingress
│   ├── Gateway API
│   ├── CNI
│   ├── CoreDNS
│   └── NetworkPolicy
│
├── Storage
│   ├── Volume
│   ├── PV
│   ├── PVC
│   ├── StorageClass
│   └── CSI
│
├── Scheduling
│   ├── Scheduler
│   ├── NodeSelector
│   ├── Affinity
│   ├── Anti-Affinity
│   ├── Taints
│   ├── Tolerations
│   └── Resources
│
├── Autoscaling
│   ├── HPA
│   ├── VPA
│   └── Cluster Autoscaler
│
├── Security
│   ├── Authentication
│   ├── RBAC
│   ├── ServiceAccounts
│   ├── Admission
│   ├── Pod Security
│   ├── Secrets
│   ├── Image Security
│   └── Runtime Security
│
├── Observability
│   ├── Logs
│   ├── Metrics
│   ├── Prometheus
│   ├── Grafana
│   ├── Alertmanager
│   └── OpenTelemetry
│
├── Operations
│   ├── Backup
│   ├── Restore
│   ├── Upgrades
│   ├── HA
│   └── Disaster Recovery
│
└── Advanced
    ├── GitOps
    ├── CI/CD
    ├── Helm
    ├── Kustomize
    ├── Operators
    └── Service Mesh
```

---

# Final Takeaways

For Kubernetes interviews, memorizing commands alone is not enough.

You should be able to explain:

```text
What
Why
How
Failure
Security
Troubleshooting
```

for every major Kubernetes component.

A strong answer generally follows:

```text
Definition
   ↓
Architecture
   ↓
How It Works
   ↓
Example
   ↓
Failure Scenario
   ↓
Security Consideration
```

The most important practical skill is troubleshooting.

When an interviewer gives you:

```text
"Pod is not working."
```

do not immediately guess the answer.

Follow a structured process:

```text
kubectl get
      ↓
kubectl describe
      ↓
kubectl logs
      ↓
kubectl logs --previous
      ↓
kubectl get events
      ↓
Check Dependencies
      ↓
Identify Root Cause
      ↓
Fix
      ↓
Validate
```

> **The goal of a Kubernetes interview is not just to prove that you know Kubernetes objects. It is to demonstrate that you understand how Kubernetes works as a distributed system and can securely operate, troubleshoot, and scale it in real production environments.**

---

## Next Chapter

# Chapter 85 – Kubernetes Cheat Sheet

The next chapter will provide a compact command and concept reference covering:

- Cluster Commands
- Node Commands
- Pod Commands
- Deployment Commands
- StatefulSet Commands
- DaemonSet Commands
- Job Commands
- CronJob Commands
- Service Commands
- Ingress Commands
- Gateway API Commands
- ConfigMap Commands
- Secret Commands
- Namespace Commands
- Label Commands
- Annotation Commands
- Resource Commands
- Scheduling Commands
- Storage Commands
- PV Commands
- PVC Commands
- StorageClass Commands
- CSI Commands
- Network Commands
- DNS Commands
- NetworkPolicy Commands
- RBAC Commands
- ServiceAccount Commands
- Security Commands
- Logs
- Events
- Debugging
- Resource Monitoring
- HPA
- VPA
- Autoscaling
- Rollouts
- Rollbacks
- Helm Commands
- Kustomize Commands
- GitOps Commands
- Operator Commands
- Service Mesh Commands
- Prometheus Queries
- Troubleshooting Flowcharts
- Production Commands
- Emergency Commands
- One-Line Definitions
- Kubernetes YAML Templates
- Interview Quick Reference
- Security Quick Reference
- Troubleshooting Quick Reference
- Production Operations Quick Reference