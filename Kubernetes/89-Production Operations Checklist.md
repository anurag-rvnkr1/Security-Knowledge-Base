# Chapter 89 – Production Operations Checklist

## Overview

This chapter provides a comprehensive checklist for operating Kubernetes clusters in production.

A production Kubernetes environment should not be considered ready simply because applications are running.

Production readiness requires:

```text
Security
+
Reliability
+
Observability
+
Scalability
+
Backup
+
Disaster Recovery
+
Operations
+
Governance
```

This checklist can be used for:

- Production readiness reviews
- Kubernetes cluster audits
- Go-live assessments
- Security reviews
- DevOps operations
- SRE operations
- Platform engineering
- Incident preparedness
- Disaster recovery testing
- Kubernetes interview preparation

---

# 1. Production Readiness Model

Use the following model:

```text
                    Production
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
     Security       Reliability     Observability
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                    Operations
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
      Backup            DR             Scaling
```

---

# 2. Pre-Production Checklist

Before deploying an application to production:

```text
☐ Architecture reviewed
☐ Resource requirements defined
☐ Security requirements defined
☐ Networking requirements defined
☐ Storage requirements defined
☐ Availability requirements defined
☐ Backup requirements defined
☐ Monitoring configured
☐ Logging configured
☐ Alerting configured
☐ Rollback strategy documented
☐ Disaster recovery requirements documented
☐ Runbook created
```

---

# 3. Cluster Architecture Checklist

Verify:

```text
☐ Production cluster architecture documented
☐ Control plane architecture documented
☐ Worker node architecture documented
☐ Failure domains identified
☐ Availability zones considered
☐ Node pools documented
☐ Network architecture documented
☐ Storage architecture documented
☐ CNI documented
☐ CSI documented
☐ DNS architecture documented
```

---

# 4. Control Plane Checklist

Verify:

```text
☐ API Server available
☐ Scheduler available
☐ Controller Manager available
☐ etcd healthy
☐ Control plane capacity sufficient
☐ Control plane monitoring enabled
☐ Control plane logs collected
☐ Certificate expiration monitored
☐ Control plane backups configured
```

For HA environments:

```text
☐ Multiple control-plane nodes
☐ etcd quorum maintained
☐ API server load balancing
☐ Failure-domain distribution
```

---

# 5. Node Checklist

For every production node:

```text
☐ Node Ready
☐ Correct Kubernetes version
☐ Correct OS version
☐ Container runtime healthy
☐ Kubelet healthy
☐ Sufficient CPU
☐ Sufficient memory
☐ Sufficient disk
☐ Network connectivity verified
☐ Time synchronization working
☐ Monitoring installed
```

---

# 6. Node Capacity

Review:

```text
CPU
Memory
Ephemeral Storage
Persistent Storage
Network
PID Capacity
```

Avoid running production nodes close to permanent capacity.

Maintain sufficient headroom for:

```text
Traffic Spikes
Pod Failures
Rolling Deployments
Node Maintenance
Autoscaling
```

---

# 7. Node Pool Strategy

Consider separate node pools for:

```text
General Workloads
Memory-Optimized Workloads
CPU-Optimized Workloads
GPU Workloads
System Components
Security Workloads
Stateful Workloads
```

Use labels and taints carefully.

---

# 8. Kubernetes Version Management

Document:

```text
Current Kubernetes Version
Supported Version Range
Upgrade Target
Upgrade Schedule
End-of-Support Date
```

Before upgrading:

```text
☐ Review release notes
☐ Review deprecated APIs
☐ Test workloads
☐ Test CRDs
☐ Test CNI
☐ Test CSI
☐ Test Ingress/Gateway
☐ Test monitoring
☐ Test service mesh
☐ Verify backup
```

---

# 9. Namespace Checklist

Use namespaces to provide logical organization and isolation.

Recommended:

```text
platform-system
monitoring
security
development
staging
production
```

For multi-tenant environments:

```text
tenant-a
tenant-b
tenant-c
```

Verify:

```text
☐ Namespace ownership defined
☐ RBAC configured
☐ ResourceQuota configured
☐ LimitRange configured
☐ NetworkPolicy configured
☐ Pod Security configured
```

---

# 10. Workload Checklist

Every production Deployment should be reviewed for:

```text
☐ Replicas configured
☐ RollingUpdate strategy
☐ Resource requests
☐ Resource limits
☐ Readiness probe
☐ Liveness probe
☐ Startup probe where required
☐ SecurityContext
☐ ServiceAccount
☐ ConfigMap
☐ Secret
☐ PodDisruptionBudget where appropriate
☐ Affinity / topology requirements
```

---

# 11. Replica Checklist

Avoid:

```yaml
replicas: 1
```

for critical stateless production services unless there is a deliberate reason.

Prefer multiple replicas where appropriate:

```text
Replica 1 → Node A
Replica 2 → Node B
Replica 3 → Node C
```

Use topology constraints to reduce correlated failures.

---

# 12. Rolling Update Checklist

Verify:

```text
☐ RollingUpdate configured
☐ maxUnavailable reviewed
☐ maxSurge reviewed
☐ Readiness configured
☐ Rollback tested
☐ Application backward compatibility considered
```

---

# 13. Zero-Downtime Deployment Checklist

Verify:

```text
☐ Multiple replicas
☐ Readiness probe
☐ Graceful shutdown
☐ terminationGracePeriodSeconds reviewed
☐ Rolling update
☐ PDB where appropriate
☐ Load balancer behavior tested
☐ Connection draining considered
```

---

# 14. Container Image Checklist

Verify:

```text
☐ Trusted registry
☐ Image scanning
☐ Critical vulnerabilities reviewed
☐ Image provenance understood
☐ Image digest available
☐ Minimal base image
☐ Unnecessary packages removed
☐ Image signing where applicable
```

Prefer controlled immutable references for production deployments.

---

# 15. Image Tagging

Avoid relying solely on:

```text
latest
```

Prefer controlled versions:

```text
app:1.4.2
```

For stronger immutability:

```text
app@sha256:<digest>
```

---

# 16. Container Security Checklist

Verify:

```text
☐ Non-root execution where possible
☐ Privilege escalation disabled
☐ Unnecessary Linux capabilities dropped
☐ Seccomp configured
☐ Read-only root filesystem where possible
☐ Host namespaces avoided
☐ Privileged containers avoided
☐ HostPath minimized
```

---

# 17. ServiceAccount Checklist

Every application should use an appropriate ServiceAccount.

Verify:

```text
☐ Dedicated ServiceAccount where needed
☐ Permissions reviewed
☐ Default ServiceAccount not unnecessarily used
☐ Token exposure minimized
☐ RBAC permissions documented
```

---

# 18. RBAC Checklist

Review:

```text
☐ Least privilege
☐ Namespace-scoped permissions where possible
☐ ClusterRole usage justified
☐ ClusterRoleBindings reviewed
☐ ServiceAccount permissions reviewed
☐ Human access reviewed
☐ Break-glass access controlled
☐ Unused permissions removed
```

---

# 19. RBAC Audit

Regularly check:

```bash
kubectl get roles -A
kubectl get rolebindings -A
kubectl get clusterroles
kubectl get clusterrolebindings
```

Investigate:

```text
Wildcard permissions
Cluster-wide Secret access
Unnecessary create/update/delete permissions
Unused ServiceAccounts
```

---

# 20. Authentication Checklist

Verify:

```text
☐ Authentication mechanism documented
☐ Identity provider configured
☐ MFA used where applicable
☐ Human identities managed centrally
☐ Service identities separated
☐ Expired credentials removed
☐ Emergency access documented
```

---

# 21. Pod Security Checklist

For production namespaces:

```text
☐ Pod Security Standard selected
☐ Restricted policy evaluated
☐ Privileged workloads documented
☐ Host networking reviewed
☐ Host PID/IPC reviewed
☐ HostPath reviewed
☐ Root execution reviewed
```

---

# 22. Admission Control Checklist

Review:

```text
☐ Admission policies documented
☐ Security policies enforced
☐ Image policies configured
☐ Resource policies configured
☐ Namespace policies configured
☐ Webhook availability monitored
```

Never deploy a critical admission dependency without considering its failure behavior.

---

# 23. Secret Management Checklist

Verify:

```text
☐ Secrets not committed to Git
☐ Secret rotation process exists
☐ Secret access is restricted
☐ Encryption at rest configured
☐ External secret management evaluated
☐ Expiration monitored
☐ Compromise response documented
```

---

# 24. Secret Rotation

Define:

```text
Rotation Frequency
Rotation Owner
Rotation Mechanism
Emergency Rotation Process
Application Reload Behavior
```

Test whether applications can safely consume rotated credentials.

---

# 25. Network Security Checklist

Verify:

```text
☐ NetworkPolicy implemented
☐ Default-deny strategy evaluated
☐ Ingress restricted
☐ Egress restricted where appropriate
☐ Database access restricted
☐ Management access restricted
☐ Namespace isolation configured
```

---

# 26. NetworkPolicy Model

A common architecture:

```text
Internet
   │
   ▼
Ingress
   │
   ▼
Frontend
   │
   ▼
Backend
   │
   ▼
Database
```

Allow:

```text
Ingress → Frontend
Frontend → Backend
Backend → Database
```

Deny:

```text
Frontend → Database
Internet → Database
Untrusted → Internal Services
```

---

# 27. CNI Checklist

Verify:

```text
☐ CNI healthy
☐ Pod networking working
☐ Cross-node connectivity working
☐ NetworkPolicy enforcement working
☐ CNI version documented
☐ CNI monitoring configured
☐ CNI upgrade procedure documented
```

---

# 28. DNS Checklist

Verify:

```text
☐ CoreDNS healthy
☐ DNS Service available
☐ Internal DNS resolution works
☐ Service discovery works
☐ External DNS resolution works where required
☐ DNS monitoring configured
```

Test:

```bash
nslookup kubernetes.default
```

and:

```bash
nslookup <service>.<namespace>.svc.cluster.local
```

---

# 29. Ingress / Gateway Checklist

Verify:

```text
☐ Controller / Gateway implementation healthy
☐ TLS configured
☐ Certificates valid
☐ Routes correct
☐ Backend Services available
☐ EndpointSlices populated
☐ Access logs enabled
☐ Rate limiting evaluated
```

---

# 30. TLS Checklist

Verify:

```text
☐ TLS enabled
☐ Certificates valid
☐ Certificate expiration monitored
☐ Strong protocol configuration
☐ Private keys protected
☐ Renewal tested
```

---

# 31. Storage Checklist

For stateful applications:

```text
☐ StorageClass selected
☐ CSI driver healthy
☐ PVC created
☐ PV provisioned
☐ Access mode appropriate
☐ Capacity sufficient
☐ Performance requirements defined
☐ Backup configured
☐ Restore tested
```

---

# 32. CSI Checklist

Verify:

```text
☐ CSI Controller healthy
☐ CSI Node components healthy
☐ Storage provisioning works
☐ Attach/detach works
☐ Mount/unmount works
☐ Volume expansion tested
☐ Snapshot functionality evaluated
```

---

# 33. Persistent Data Checklist

For databases:

```text
☐ Persistent storage
☐ Backup
☐ Restore
☐ Replication
☐ Failover
☐ Data integrity checks
☐ Storage monitoring
```

---

# 34. Storage Performance

Monitor:

```text
Latency
IOPS
Throughput
Capacity
Queue Depth
Errors
```

Ensure storage performance matches application requirements.

---

# 35. Scheduling Checklist

Review:

```text
☐ NodeSelector
☐ Node Affinity
☐ Pod Affinity
☐ Pod Anti-Affinity
☐ Taints
☐ Tolerations
☐ PriorityClass
☐ Topology Spread
```

Avoid unnecessarily strict scheduling rules that prevent recovery.

---

# 36. High Availability Checklist

For critical applications:

```text
☐ Multiple replicas
☐ Multiple nodes
☐ Multiple failure domains
☐ PodDisruptionBudget
☐ Topology spread
☐ Load balancing
☐ Health probes
☐ Automated recovery
```

---

# 37. PodDisruptionBudget Checklist

For critical services:

```text
☐ PDB configured
☐ minAvailable / maxUnavailable reviewed
☐ Compatible with replica count
☐ Tested during maintenance
```

Do not configure PDBs so strictly that they prevent necessary maintenance indefinitely.

---

# 38. Resource Requests Checklist

Every production workload should have realistic requests.

Example:

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
```

Requests affect:

```text
Scheduling
Capacity Planning
Autoscaling
```

---

# 39. Resource Limits Checklist

Evaluate:

```text
☐ CPU limits
☐ Memory limits
☐ Application behavior under limits
☐ OOM behavior
☐ CPU throttling
```

Do not blindly apply identical limits to every workload.

---

# 40. ResourceQuota Checklist

For namespaces:

```text
☐ CPU quota
☐ Memory quota
☐ Pod quota
☐ Storage quota where appropriate
☐ Object count limits where appropriate
```

---

# 41. LimitRange Checklist

Define reasonable defaults where appropriate:

```text
☐ Default CPU
☐ Default Memory
☐ Default Requests
☐ Maximum CPU
☐ Maximum Memory
```

---

# 42. Autoscaling Checklist

Evaluate:

```text
☐ HPA
☐ VPA
☐ Cluster Autoscaler
```

Understand their interactions before enabling all three for the same workload.

---

# 43. HPA Checklist

Verify:

```text
☐ Metrics available
☐ Resource requests configured
☐ Minimum replicas
☐ Maximum replicas
☐ Target utilization
☐ Scale-up behavior
☐ Scale-down behavior
☐ Stabilization behavior
```

---

# 44. Cluster Autoscaler Checklist

Verify:

```text
☐ Node groups configured
☐ Minimum nodes
☐ Maximum nodes
☐ Cloud provider integration
☐ Pending Pods trigger evaluation
☐ Scale-down behavior understood
☐ Scheduling constraints compatible
```

---

# 45. Observability Checklist

A production platform should provide:

```text
Metrics
Logs
Traces
Events
Alerts
Dashboards
```

---

# 46. Logging Checklist

Verify:

```text
☐ Application logs collected
☐ Kubernetes logs collected
☐ Structured logging used where possible
☐ Log retention defined
☐ Log storage capacity monitored
☐ Sensitive data filtered
☐ Search available
```

---

# 47. Logging Security

Never intentionally log:

```text
Passwords
API Keys
Tokens
Private Keys
Session Credentials
Sensitive Personal Data
```

Review application logs for accidental secret exposure.

---

# 48. Metrics Checklist

Monitor:

```text
CPU
Memory
Network
Disk
Pod Restarts
Pod Availability
Node Health
API Server
DNS
Storage
```

---

# 49. Application Metrics

At minimum consider:

```text
Request Rate
Error Rate
Latency
Saturation
```

Also monitor important business metrics where appropriate.

---

# 50. Prometheus Checklist

Verify:

```text
☐ Prometheus healthy
☐ Targets discovered
☐ Scraping succeeds
☐ Retention configured
☐ Storage monitored
☐ Rules loaded
☐ Alerts evaluated
```

---

# 51. Grafana Checklist

Verify:

```text
☐ Data sources configured
☐ Dashboards available
☐ Production dashboards standardized
☐ Access controlled
☐ Dashboard ownership documented
```

---

# 52. Alerting Checklist

Every critical alert should have:

```text
☐ Clear description
☐ Severity
☐ Owner
☐ Runbook
☐ Action
☐ Escalation path
```

Avoid alerts that provide no actionable response.

---

# 53. Alert Categories

Useful categories:

```text
Availability
Performance
Capacity
Security
Storage
Networking
Control Plane
Certificate
Backup
Disaster Recovery
```

---

# 54. Distributed Tracing Checklist

Verify where appropriate:

```text
☐ Application instrumentation
☐ Trace propagation
☐ Collector
☐ Storage backend
☐ Sampling strategy
☐ Sensitive data handling
```

---

# 55. SLO Checklist

Define service objectives.

Example:

```text
Availability: 99.9%
Latency: 95% < 300ms
```

Track:

```text
SLO
SLI
Error Budget
```

---

# 56. Backup Checklist

Backup:

```text
☐ Kubernetes configuration
☐ Important manifests
☐ Secrets
☐ Persistent data
☐ Application configuration
☐ Critical custom resources
```

Use appropriate backup mechanisms for your environment.

---

# 57. Backup Validation

A backup is not considered reliable until restoration is tested.

Verify:

```text
☐ Backup succeeds
☐ Backup integrity checked
☐ Restore succeeds
☐ Data integrity verified
☐ Restore time measured
☐ Recovery documentation updated
```

---

# 58. Backup Security

Protect backups using:

```text
Encryption
Access Control
Separate Credentials
Separate Failure Domain
Retention Policy
Immutable / Protected Storage where appropriate
```

---

# 59. Disaster Recovery Checklist

Define:

```text
☐ RTO
☐ RPO
☐ Recovery Architecture
☐ Backup Location
☐ Recovery Procedure
☐ DNS / Traffic Switching
☐ Data Restoration
☐ Application Restoration
☐ Validation
```

---

# 60. DR Testing

Perform periodic recovery exercises.

Example:

```text
Primary Cluster
      ↓
Simulated Failure
      ↓
DR Environment
      ↓
Restore
      ↓
Validate
      ↓
Measure RTO/RPO
```

---

# 61. Upgrade Checklist

Before upgrade:

```text
☐ Backup
☐ Test
☐ Review compatibility
☐ Review deprecated APIs
☐ Check add-ons
☐ Check CNI
☐ Check CSI
☐ Check Ingress/Gateway
☐ Check CRDs
☐ Define rollback/recovery
```

---

# 62. Upgrade Execution

During upgrade:

```text
☐ Monitor nodes
☐ Monitor Pods
☐ Monitor API server
☐ Monitor workloads
☐ Monitor errors
☐ Monitor latency
☐ Monitor storage
```

---

# 63. Post-Upgrade Validation

Verify:

```text
☐ Nodes Ready
☐ Pods healthy
☐ Services healthy
☐ DNS healthy
☐ Storage healthy
☐ Monitoring healthy
☐ Logging healthy
☐ Alerts healthy
☐ Ingress healthy
```

---

# 64. Maintenance Checklist

Before maintenance:

```text
☐ Change approved
☐ Impact assessed
☐ Backup verified
☐ Maintenance window defined
☐ Stakeholders informed
☐ Rollback plan available
```

---

# 65. Node Maintenance

Typical workflow:

```bash
kubectl cordon <node>
```

Then drain when appropriate:

```bash
kubectl drain <node> --ignore-daemonsets
```

After maintenance:

```bash
kubectl uncordon <node>
```

Validate:

```bash
kubectl get nodes
kubectl get pods -A
```

---

# 66. Production Change Checklist

Before change:

```text
☐ Why is the change required?
☐ What will change?
☐ What can break?
☐ How will we detect failure?
☐ How will we roll back?
☐ Who owns the change?
```

---

# 67. GitOps Checklist

For GitOps-managed environments:

```text
☐ Git is source of truth
☐ Pull requests reviewed
☐ CI validation
☐ Security scanning
☐ Policy validation
☐ Deployment reconciliation
☐ Drift detection
☐ Rollback strategy
```

---

# 68. CI/CD Checklist

Pipeline:

```text
Source
 ↓
Build
 ↓
Test
 ↓
Security Scan
 ↓
Image Build
 ↓
Image Scan
 ↓
SBOM
 ↓
Sign
 ↓
Registry
 ↓
Deploy
 ↓
Validate
```

---

# 69. CI/CD Security Gates

Evaluate:

```text
☐ SAST
☐ Dependency Scanning
☐ Secret Scanning
☐ Container Scanning
☐ IaC Scanning
☐ SBOM
☐ Image Signature
☐ Policy Validation
```

---

# 70. Helm Checklist

Verify:

```text
☐ Chart versioning
☐ values documented
☐ Secrets handled securely
☐ Templates validated
☐ helm lint
☐ helm template
☐ Upgrade tested
☐ Rollback tested
```

Run:

```bash
helm lint <chart>
```

---

# 71. Kustomize Checklist

Verify:

```text
☐ Base configuration
☐ Environment overlays
☐ Production differences documented
☐ Secrets handled securely
☐ Generated manifests reviewed
```

Test:

```bash
kubectl kustomize overlays/production
```

---

# 72. Operator Checklist

For Operators:

```text
☐ CRDs documented
☐ Operator version documented
☐ Reconciliation behavior understood
☐ Upgrade procedure documented
☐ Backup strategy defined
☐ Failure behavior tested
```

---

# 73. Service Mesh Checklist

If using a service mesh:

```text
☐ Control plane healthy
☐ Data plane healthy
☐ mTLS configuration
☐ Traffic policies
☐ Retry policies
☐ Timeout policies
☐ Circuit breaking
☐ Metrics
☐ Tracing
☐ Certificate rotation
```

Avoid enabling complex traffic policies without understanding their failure behavior.

---

# 74. Security Operations Checklist

Daily review:

```text
☐ Security alerts
☐ Suspicious workloads
☐ Image vulnerabilities
☐ RBAC changes
☐ Secret changes
☐ Admission violations
☐ Network anomalies
```

---

# 75. Vulnerability Management

Track:

```text
Vulnerability
Severity
Affected Image
Affected Workload
Version
Remediation
Owner
Deadline
```

Prioritize:

```text
Critical
High
Exploitable
Internet-facing
Privileged
Sensitive Workloads
```

---

# 76. Image Vulnerability Management

Regularly scan:

```text
Base Images
Application Images
Third-Party Images
Sidecars
Operators
System Components
```

Rebuild images when vulnerabilities require remediation.

---

# 77. Runtime Security Checklist

Monitor for:

```text
Unexpected Processes
Privilege Escalation
Suspicious File Access
Unexpected Network Connections
Container Escape Attempts
Credential Access
```

---

# 78. Kubernetes Audit Checklist

Where supported and configured, review:

```text
Authentication
Authorization
Resource Changes
Secret Access
RBAC Changes
Privileged Workloads
Administrative Actions
```

Protect audit logs from unauthorized modification.

---

# 79. Compliance Checklist

Map Kubernetes controls to applicable requirements.

Review:

```text
Identity
Access Control
Encryption
Logging
Monitoring
Vulnerability Management
Change Management
Backup
Incident Response
Data Protection
```

---

# 80. Security Incident Response Checklist

```text
☐ Detect
☐ Validate
☐ Scope
☐ Contain
☐ Preserve Evidence
☐ Revoke Credentials
☐ Investigate
☐ Eradicate
☐ Recover
☐ Monitor
☐ Document
☐ Postmortem
```

---

# 81. Incident Response Questions

Ask:

```text
What happened?
When did it start?
What changed?
Which workloads are affected?
Which identities are involved?
What data may be affected?
How did the attacker enter?
How did they move?
What permissions were available?
What controls failed?
```

---

# 82. Production Go-Live Checklist

Before go-live:

```text
☐ Application tested
☐ Load tested
☐ Security tested
☐ Failure tested
☐ Rollback tested
☐ Monitoring tested
☐ Alerts tested
☐ Backup tested
☐ Restore tested
☐ DR documented
☐ Runbooks completed
☐ On-call ownership assigned
```

---

# 83. Load Testing Checklist

Test:

```text
Normal Load
Peak Load
Burst Load
Sustained Load
Failure Load
Recovery
```

Measure:

```text
Latency
Throughput
Errors
CPU
Memory
Scaling
```

---

# 84. Failure Testing Checklist

Intentionally test:

```text
☐ Pod Failure
☐ Node Failure
☐ Network Failure
☐ DNS Failure
☐ Storage Failure
☐ Dependency Failure
☐ Application Failure
☐ Image Failure
```

The goal is to validate recovery, not merely to cause outages.

---

# 85. Chaos Engineering

Start with controlled experiments.

Example:

```text
Experiment:
Delete one non-critical Pod.

Expected:
Controller recreates Pod.

Observed:
Record recovery time.
```

Gradually increase complexity.

---

# 86. Production Readiness Scorecard

| Area | Status |
|---|---|
| Architecture | ☐ |
| Security | ☐ |
| Networking | ☐ |
| Storage | ☐ |
| Scheduling | ☐ |
| Resources | ☐ |
| Scaling | ☐ |
| Monitoring | ☐ |
| Logging | ☐ |
| Alerting | ☐ |
| Backup | ☐ |
| Disaster Recovery | ☐ |
| CI/CD | ☐ |
| GitOps | ☐ |
| Incident Response | ☐ |
| Documentation | ☐ |

---

# 87. Daily Operations Checklist

Every day:

```text
☐ Check cluster health
☐ Check node health
☐ Check critical Pods
☐ Check failed workloads
☐ Review alerts
☐ Review security alerts
☐ Review capacity
☐ Review backup status
☐ Review major deployment changes
```

---

# 88. Weekly Operations Checklist

Every week:

```text
☐ Review resource utilization
☐ Review failed Pods
☐ Review restart trends
☐ Review vulnerabilities
☐ Review RBAC changes
☐ Review NetworkPolicy changes
☐ Review certificate status
☐ Review backup success
☐ Review alert quality
☐ Review incidents
```

---

# 89. Monthly Operations Checklist

Every month:

```text
☐ Capacity planning
☐ Vulnerability review
☐ Access review
☐ Secret rotation review
☐ Backup restoration test
☐ DR readiness review
☐ Kubernetes version review
☐ Add-on version review
☐ Cost optimization
☐ SLO review
```

---

# 90. Quarterly Operations Checklist

Every quarter:

```text
☐ Full DR exercise
☐ Security assessment
☐ RBAC audit
☐ Network security review
☐ Image security review
☐ Disaster recovery validation
☐ Architecture review
☐ Capacity forecast
☐ Incident trend analysis
☐ Production readiness reassessment
```

---

# 91. Cluster Cost Optimization

Review:

```text
Node Utilization
Pod Requests
Pod Limits
Idle Workloads
Overprovisioned Nodes
Storage
Load Balancers
Persistent Volumes
Logging Costs
Monitoring Costs
```

---

# 92. Resource Optimization

Compare:

```text
Requested
vs
Actual
```

Example:

```text
CPU Request = 2 cores
Actual = 250m
```

Potential optimization:

```text
Reduce Request
```

But validate:

```text
Peak Usage
Startup Usage
Scaling Behavior
Performance
```

---

# 93. Idle Resource Cleanup

Identify:

```text
Unused Namespaces
Unused Services
Unused PVCs
Unused Load Balancers
Old ReplicaSets
Unused Helm Releases
Unused Images
```

Never delete resources solely because they appear unused without confirming ownership and dependencies.

---

# 94. Production Documentation Checklist

Maintain:

```text
☐ Architecture Diagram
☐ Network Diagram
☐ Data Flow
☐ Security Model
☐ RBAC Model
☐ Storage Model
☐ Backup Plan
☐ DR Plan
☐ Deployment Procedure
☐ Rollback Procedure
☐ Incident Runbooks
☐ Upgrade Procedure
☐ Contact / Ownership Information
```

---

# 95. Runbook Checklist

Every critical service should have:

```text
☐ Health Check
☐ Common Failures
☐ Troubleshooting Commands
☐ Rollback
☐ Restart Procedure
☐ Scaling Procedure
☐ Dependency List
☐ Escalation Path
```

---

# 96. Ownership Checklist

For every production workload define:

```text
Application Owner
Platform Owner
Security Owner
On-Call Team
Business Owner
```

Avoid services with no clearly defined owner.

---

# 97. Dependency Inventory

Document:

```text
Application
 ↓
Service
 ↓
Database
 ↓
Cache
 ↓
External APIs
 ↓
DNS
 ↓
Identity Provider
```

Know which dependencies are critical.

---

# 98. External Dependency Checklist

For external services:

```text
☐ Endpoint documented
☐ Authentication documented
☐ Timeout configured
☐ Retry behavior reviewed
☐ Circuit breaker considered
☐ Failure behavior tested
☐ Monitoring configured
```

---

# 99. Graceful Shutdown Checklist

Applications should handle termination appropriately.

Verify:

```text
☐ SIGTERM handling
☐ Connection draining
☐ In-flight request handling
☐ Shutdown timeout
☐ Readiness behavior
```

Typical flow:

```text
Pod Termination
      ↓
Readiness Removed
      ↓
Traffic Draining
      ↓
SIGTERM
      ↓
Graceful Shutdown
      ↓
Process Exit
```

---

# 100. Production Networking Checklist

Verify:

```text
☐ Pod-to-Pod
☐ Pod-to-Service
☐ Service-to-Service
☐ Pod-to-External
☐ Ingress-to-Service
☐ DNS
☐ TLS
☐ NetworkPolicy
☐ CNI
```

---

# 101. Production Storage Checklist

Verify:

```text
☐ StorageClass
☐ CSI
☐ PV
☐ PVC
☐ Mount
☐ Performance
☐ Capacity
☐ Backup
☐ Restore
☐ Failure Recovery
```

---

# 102. Production Security Checklist

```text
☐ Authentication
☐ Authorization
☐ RBAC
☐ ServiceAccounts
☐ Secrets
☐ Pod Security
☐ Admission
☐ NetworkPolicy
☐ Image Scanning
☐ Image Signing
☐ Runtime Security
☐ Audit Logs
☐ Vulnerability Management
```

---

# 103. Production Observability Checklist

```text
☐ Metrics
☐ Logs
☐ Traces
☐ Events
☐ Dashboards
☐ Alerts
☐ SLOs
☐ Error Budgets
```

---

# 104. Production Reliability Checklist

```text
☐ Multiple replicas
☐ Health probes
☐ PDB
☐ Topology distribution
☐ Autoscaling
☐ Backup
☐ DR
☐ Failure testing
```

---

# 105. Production Deployment Checklist

Before deployment:

```text
☐ Version identified
☐ Image scanned
☐ Tests passed
☐ Security checks passed
☐ Configuration reviewed
☐ Resource requirements reviewed
☐ Rollout strategy reviewed
☐ Rollback confirmed
```

During deployment:

```text
☐ Monitor rollout
☐ Monitor errors
☐ Monitor latency
☐ Monitor resource usage
☐ Monitor Pod health
```

After deployment:

```text
☐ All replicas Ready
☐ Traffic healthy
☐ Error rate normal
☐ Latency normal
☐ Logs normal
☐ Alerts normal
```

---

# 106. Production Rollback Checklist

Before rollback:

```text
☐ Confirm failure
☐ Identify last known-good version
☐ Check database compatibility
☐ Assess rollback impact
```

Execute:

```bash
kubectl rollout undo deployment/<name>
```

Then validate:

```text
☐ Pods healthy
☐ Traffic healthy
☐ Error rate normal
☐ Data integrity maintained
```

---

# 107. Incident Postmortem Checklist

After a significant incident:

```text
☐ Timeline documented
☐ Impact documented
☐ Root cause documented
☐ Contributing factors documented
☐ Detection reviewed
☐ Response reviewed
☐ Recovery reviewed
☐ Preventive actions created
☐ Owners assigned
☐ Deadlines assigned
```

---

# 108. Blameless Postmortem

Focus on:

```text
Systems
Processes
Architecture
Controls
Automation
Detection
```

Avoid reducing the analysis to individual blame.

---

# 109. Production Security Review Questions

Ask:

```text
Can a compromised Pod access Kubernetes API resources?

Can one namespace access another?

Can a workload read Secrets it does not need?

Can a container run as root?

Can a container become privileged?

Can a workload access the host filesystem?

Can an untrusted image reach production?

Can an attacker move laterally?

Can we detect suspicious behavior?
```

---

# 110. Production Reliability Review Questions

Ask:

```text
What happens if a Pod fails?

What happens if a node fails?

What happens if a zone fails?

What happens if the database fails?

What happens if DNS fails?

What happens if the control plane becomes unavailable?

What happens if storage fails?

What happens if a deployment is broken?

What happens if the entire cluster is lost?
```

---

# 111. Production Observability Questions

Ask:

```text
Can we detect failure?

Can we determine impact?

Can we identify the failing component?

Can we determine when the failure began?

Can we identify what changed?

Can we measure recovery?

Can we identify recurring patterns?
```

---

# 112. Production Security Operations Questions

Ask:

```text
Do we know which images are running?

Do we know which workloads are privileged?

Do we know which identities have elevated permissions?

Do we monitor RBAC changes?

Do we monitor Secret access?

Do we have runtime detection?

Do we have incident response procedures?

Can we preserve forensic evidence?
```

---

# 113. Go-Live Approval

A production workload should not be approved until:

```text
Security
       ✓
Reliability
       ✓
Observability
       ✓
Backup
       ✓
Recovery
       ✓
Operations
       ✓
Ownership
       ✓
```

---

# 114. Production Readiness Gate

Use:

```text
GREEN
→ Ready

YELLOW
→ Ready with documented risk

RED
→ Not ready
```

Example:

```text
Security = GREEN
Monitoring = GREEN
Backup = YELLOW
DR = RED

Overall = RED
```

---

# 115. Emergency Change Checklist

Emergency changes should still have:

```text
☐ Reason
☐ Owner
☐ Scope
☐ Risk
☐ Mitigation
☐ Rollback
☐ Validation
```

After the emergency:

```text
☐ Document
☐ Review
☐ Convert to permanent fix
```

---

# 116. Decommissioning Checklist

When retiring an application:

```text
☐ Confirm owner approval
☐ Stop traffic
☐ Backup required data
☐ Export required configuration
☐ Remove workloads
☐ Remove Services
☐ Remove Ingress
☐ Remove PVCs only after data approval
☐ Remove Secrets
☐ Remove RBAC
☐ Remove monitoring
☐ Remove alerts
☐ Remove DNS
☐ Remove cloud resources
```

Be especially careful with persistent data.

---

# 117. Cluster Decommissioning

Before destroying a cluster:

```text
☐ Business approval
☐ Application migration complete
☐ Backup complete
☐ Restore verified
☐ DNS migrated
☐ Traffic migrated
☐ Monitoring migrated
☐ Secrets migrated
☐ Persistent data migrated
☐ Access revoked
☐ Cloud resources inventoried
```

---

# 118. Final Production Checklist

## Cluster

```text
☐ HA
☐ Nodes healthy
☐ Control plane healthy
☐ etcd healthy
☐ CNI healthy
☐ CSI healthy
☐ DNS healthy
```

## Workloads

```text
☐ Replicas
☐ Probes
☐ Resources
☐ SecurityContext
☐ ServiceAccounts
☐ PDB
☐ Scheduling
```

## Networking

```text
☐ Services
☐ EndpointSlices
☐ Ingress / Gateway
☐ TLS
☐ DNS
☐ NetworkPolicy
```

## Storage

```text
☐ PV
☐ PVC
☐ StorageClass
☐ CSI
☐ Backup
☐ Restore
```

## Security

```text
☐ RBAC
☐ Authentication
☐ Secrets
☐ Pod Security
☐ Admission
☐ Image Security
☐ Runtime Security
☐ Audit
```

## Observability

```text
☐ Metrics
☐ Logs
☐ Traces
☐ Dashboards
☐ Alerts
☐ SLOs
```

## Operations

```text
☐ GitOps
☐ CI/CD
☐ Helm
☐ Kustomize
☐ Runbooks
☐ On-call
☐ Incident Response
```

## Recovery

```text
☐ Backup
☐ Restore
☐ RTO
☐ RPO
☐ DR
☐ Failure Testing
```

---

# 119. Kubernetes Production Readiness Score

A practical internal scoring model can use:

```text
Security              20%
Reliability           20%
Observability         15%
Networking             10%
Storage                10%
Operations             10%
Backup / DR            10%
Documentation           5%
```

Example:

```text
Security       18/20
Reliability    17/20
Observability  14/15
Networking      9/10
Storage         8/10
Operations      8/10
Backup/DR       7/10
Documentation   4/5
--------------------
Total          85/100
```

Use the score as an internal assessment tool, not as a universal Kubernetes standard.

---

# 120. Final Operations Philosophy

Production Kubernetes is not simply:

```text
kubectl apply
```

It is a continuous lifecycle:

```text
Plan
 ↓
Build
 ↓
Secure
 ↓
Deploy
 ↓
Observe
 ↓
Operate
 ↓
Scale
 ↓
Troubleshoot
 ↓
Recover
 ↓
Improve
```

---

# 121. The Kubernetes Production Lifecycle

```text
                    DESIGN
                      │
                      ▼
                  DEVELOP
                      │
                      ▼
                    TEST
                      │
                      ▼
                   SECURE
                      │
                      ▼
                  DEPLOY
                      │
                      ▼
                 OBSERVE
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
       HEALTHY                  FAILURE
          │                       │
          ▼                       ▼
      OPERATE                 TROUBLESHOOT
          │                       │
          ▼                       ▼
       OPTIMIZE                  FIX
          │                       │
          └───────────┬───────────┘
                      ▼
                  IMPROVE
```

---

# 122. Final Kubernetes Operations Principles

## Principle 1 – Automate

Automate repetitive operational work.

```text
Deployment
Testing
Scaling
Backup
Monitoring
Security
```

---

## Principle 2 – Observe

Everything important should be observable.

```text
Metrics
Logs
Traces
Events
```

---

## Principle 3 – Secure by Default

Prefer:

```text
Least Privilege
Non-Root
Restricted Networking
Trusted Images
Strong Identity
```

---

## Principle 4 – Design for Failure

Assume:

```text
Pods fail
Nodes fail
Networks fail
Storage fails
Applications fail
Dependencies fail
```

---

## Principle 5 – Test Recovery

A documented recovery procedure is not enough.

Actually test it.

```text
Backup
 ↓
Restore
 ↓
Validate
```

---

## Principle 6 – Make Changes Reversible

Every significant production change should have a rollback or recovery strategy.

---

## Principle 7 – Minimize Blast Radius

Prefer:

```text
Small Deployments
Namespaces
Network Segmentation
Least Privilege
Canary Releases
Failure Domains
```

---

## Principle 8 – Treat Kubernetes as a Platform

Kubernetes is not only a container scheduler.

A production platform includes:

```text
Compute
Networking
Storage
Security
Identity
Observability
Automation
Governance
Recovery
```

---

# 123. Final Production Command Set

Frequently useful commands:

```bash
kubectl get nodes
kubectl get pods -A
kubectl get svc -A
kubectl get endpointslices -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl get pvc -A
kubectl get pv
kubectl get storageclass
kubectl get ingress -A
kubectl get networkpolicy -A
kubectl get sa -A
kubectl get roles -A
kubectl get rolebindings -A
kubectl top nodes
kubectl top pods -A
```

Troubleshooting:

```bash
kubectl describe pod <pod>
kubectl describe node <node>
kubectl describe deployment <deployment>
kubectl describe svc <service>
kubectl describe pvc <pvc>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl exec -it <pod> -- /bin/sh
kubectl auth can-i <verb> <resource>
```

Rollouts:

```bash
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>
kubectl rollout undo deployment/<name>
```

Maintenance:

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets
kubectl uncordon <node>
```

---

# 124. Final Troubleshooting Formula

```text
Symptoms
   +
Events
   +
Logs
   +
Metrics
   +
Configuration
   +
Dependencies
   =
Root Cause
```

Then:

```text
Root Cause
   ↓
Minimal Safe Fix
   ↓
Validation
   ↓
Automation / Prevention
```

---

# 125. Final Security Formula

```text
Strong Identity
      +
Least Privilege
      +
Network Segmentation
      +
Secure Images
      +
Admission Controls
      +
Runtime Protection
      +
Monitoring
      =
Defense in Depth
```

---

# 126. Final Reliability Formula

```text
Multiple Replicas
      +
Health Probes
      +
Resource Management
      +
Autoscaling
      +
Failure-Domain Awareness
      +
Backup
      +
Disaster Recovery
      =
Resilient Platform
```

---

# 127. Final Observability Formula

```text
Metrics
   +
Logs
   +
Traces
   +
Events
   +
Alerts
   +
SLOs
   =
Operational Visibility
```

---

# 128. Final Operations Formula

```text
Automation
    +
Documentation
    +
Monitoring
    +
Security
    +
Testing
    +
Incident Response
    +
Continuous Improvement
    =
Production Operations
```

---

# 129. Complete Kubernetes Learning Journey

You have now covered the Kubernetes learning path from fundamentals through production operations:

```text
Kubernetes Fundamentals
        ↓
Architecture
        ↓
kubectl
        ↓
Pods
        ↓
Deployments
        ↓
Services
        ↓
Networking
        ↓
DNS
        ↓
CNI
        ↓
Volumes
        ↓
PV
        ↓
PVC
        ↓
StorageClass
        ↓
Dynamic Provisioning
        ↓
CSI
        ↓
Scheduling
        ↓
Security
        ↓
Observability
        ↓
Operations
        ↓
Security Operations
        ↓
Best Practices
        ↓
GitOps / CI/CD
        ↓
Helm / Kustomize
        ↓
Service Mesh
        ↓
Interview Preparation
        ↓
Hands-on Labs
        ↓
Real-World Case Studies
        ↓
Troubleshooting
        ↓
Production Operations
```

---

# 130. Final Production Readiness Checklist

Before declaring a Kubernetes environment production-ready:

```text
☐ Architecture reviewed
☐ HA reviewed
☐ Security reviewed
☐ RBAC reviewed
☐ NetworkPolicies reviewed
☐ Secrets protected
☐ Images scanned
☐ Runtime security reviewed
☐ CNI validated
☐ DNS validated
☐ Storage validated
☐ CSI validated
☐ Resource requests defined
☐ Resource limits reviewed
☐ HPA reviewed
☐ PDB reviewed
☐ Health probes configured
☐ Monitoring configured
☐ Logging configured
☐ Alerting configured
☐ Tracing configured where required
☐ SLOs defined
☐ Backup configured
☐ Restore tested
☐ DR tested
☐ Upgrade tested
☐ Rollback tested
☐ Incident response documented
☐ Runbooks documented
☐ Ownership defined
☐ On-call defined
☐ Security incident procedures defined
☐ Vulnerability management defined
☐ Capacity planning defined
☐ Cost optimization reviewed
```

---

# Final Takeaways

A production Kubernetes environment should satisfy five fundamental questions:

### 1. Can we deploy safely?

```text
CI/CD
GitOps
Testing
Rollback
```

### 2. Can we keep it secure?

```text
Identity
RBAC
NetworkPolicy
Pod Security
Image Security
Runtime Security
```

### 3. Can we observe it?

```text
Metrics
Logs
Traces
Alerts
SLOs
```

### 4. Can we recover it?

```text
Backup
Restore
HA
DR
Failure Testing
```

### 5. Can we operate it?

```text
Runbooks
Automation
On-Call
Incident Response
Maintenance
Continuous Improvement
```

If any of these areas is missing, production readiness is incomplete.

---

# Final Kubernetes Operations Mindset

```text
                    BUILD
                      │
                      ▼
                   SECURE
                      │
                      ▼
                   DEPLOY
                      │
                      ▼
                  OBSERVE
                      │
                      ▼
                   OPERATE
                      │
                      ▼
                  TROUBLESHOOT
                      │
                      ▼
                   RECOVER
                      │
                      ▼
                  OPTIMIZE
                      │
                      ▼
                  AUTOMATE
                      │
                      ▼
                 CONTINUOUSLY
                  IMPROVE
```

> **Production Kubernetes is not a one-time deployment. It is a continuously operated system that must remain secure, observable, resilient, scalable, and recoverable throughout its entire lifecycle.**

---

# Course Completion

With this chapter, the practical Kubernetes curriculum is complete.

The complete journey now covers:

```text
Chapter 1  → Kubernetes Fundamentals
Chapter 2  → Architecture
Chapter 3  → kubectl
...
Chapter 30 → Volumes
Chapter 31 → Persistent Volumes
Chapter 32 → Persistent Volume Claims
Chapter 33 → Storage Classes
Chapter 34 → Dynamic Provisioning
Chapter 35 → CSI Drivers
...
Chapter 36 → Scheduler
...
Chapter 45 → Cluster Autoscaler
...
Chapter 46 → Kubernetes Security Fundamentals
...
Chapter 56 → Supply Chain Security
...
Chapter 57 → Logging
...
Chapter 64 → Distributed Tracing
...
Chapter 65 → Cluster Administration
...
Chapter 71 → Resource Optimization
...
Chapter 72 → Vulnerability Management
...
Chapter 76 → Compliance & Auditing
...
Chapter 77 → Production Best Practices
...
Chapter 83 → Service Mesh
...
Chapter 84 → Kubernetes Interview Questions
Chapter 85 → Kubernetes Cheat Sheet
Chapter 86 → Hands-on Labs
Chapter 87 → Real-World Case Studies
Chapter 88 → Troubleshooting Playbook
Chapter 89 → Production Operations Checklist
```

---

# Final Goal

The end goal is not simply to memorize Kubernetes commands.

The goal is to be able to:

```text
Design
   ↓
Deploy
   ↓
Secure
   ↓
Observe
   ↓
Scale
   ↓
Troubleshoot
   ↓
Recover
   ↓
Optimize
   ↓
Operate
```

a Kubernetes platform confidently in real-world environments.

> **Learn Kubernetes by building it. Master Kubernetes by breaking it. Become production-ready by learning how to recover it.**