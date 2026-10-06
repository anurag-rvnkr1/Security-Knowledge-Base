# Chapter 85 – Kubernetes Cheat Sheet

## Overview

This chapter is a compact, practical Kubernetes reference designed for:

- Interviews
- Daily Kubernetes administration
- DevOps work
- Cloud engineering
- SRE operations
- Platform engineering
- Kubernetes security
- Troubleshooting
- Production operations
- Quick revision

The cheat sheet is organized around the Kubernetes workflow:

```text
Cluster
  ↓
Nodes
  ↓
Namespaces
  ↓
Workloads
  ↓
Services
  ↓
Networking
  ↓
Storage
  ↓
Scheduling
  ↓
Security
  ↓
Observability
  ↓
Operations
```

---

# 1. Kubernetes Architecture

```text
                         Kubernetes Cluster
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
        Control Plane                         Worker Nodes
              │                                   │
      ┌───────┼────────┐                ┌─────────┼─────────┐
      ▼       ▼        ▼                ▼         ▼         ▼
   API      etcd   Scheduler         Kubelet   Runtime   Networking
  Server
              │
              ▼
        Controllers
```

---

# 2. Core Components

| Component | Purpose |
|---|---|
| API Server | Kubernetes API entry point |
| etcd | Stores cluster state |
| Scheduler | Assigns Pods to nodes |
| Controller Manager | Runs reconciliation controllers |
| Kubelet | Node agent |
| Container Runtime | Runs containers |
| kube-proxy | Traditionally implements Service networking |

---

# 3. Essential kubectl Syntax

```bash
kubectl <command> <resource> <name> [options]
```

Examples:

```bash
kubectl get pods
kubectl describe pod my-pod
kubectl delete pod my-pod
kubectl logs my-pod
kubectl apply -f app.yaml
```

---

# 4. Cluster Information

Check cluster information:

```bash
kubectl cluster-info
```

Check client and server versions:

```bash
kubectl version
```

Check API resources:

```bash
kubectl api-resources
```

Check API versions:

```bash
kubectl api-versions
```

Get Kubernetes configuration:

```bash
kubectl config view
```

---

# 5. Context Management

List contexts:

```bash
kubectl config get-contexts
```

Show current context:

```bash
kubectl config current-context
```

Switch context:

```bash
kubectl config use-context <context>
```

Set namespace for the current context:

```bash
kubectl config set-context --current --namespace=<namespace>
```

---

# 6. Namespace Commands

List namespaces:

```bash
kubectl get namespaces
```

Create namespace:

```bash
kubectl create namespace production
```

Delete namespace:

```bash
kubectl delete namespace production
```

Get resources in a namespace:

```bash
kubectl get all -n production
```

---

# 7. YAML Management

Apply configuration:

```bash
kubectl apply -f app.yaml
```

Apply an entire directory:

```bash
kubectl apply -f ./manifests/
```

Delete using YAML:

```bash
kubectl delete -f app.yaml
```

View the configured object:

```bash
kubectl get deployment app -o yaml
```

---

# 8. Pod Commands

List Pods:

```bash
kubectl get pods
```

List Pods across namespaces:

```bash
kubectl get pods -A
```

Detailed Pod information:

```bash
kubectl describe pod <pod>
```

Get Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

Get Pod IP:

```bash
kubectl get pod <pod> -o wide
```

---

# 9. Pod Logs

View logs:

```bash
kubectl logs <pod>
```

Follow logs:

```bash
kubectl logs -f <pod>
```

Specific container:

```bash
kubectl logs <pod> -c <container>
```

Previous container instance:

```bash
kubectl logs <pod> --previous
```

Follow previous logs:

```bash
kubectl logs -f <pod> --previous
```

Logs since a duration:

```bash
kubectl logs <pod> --since=1h
```

---

# 10. Execute Commands Inside Pods

Open a shell:

```bash
kubectl exec -it <pod> -- /bin/sh
```

If Bash exists:

```bash
kubectl exec -it <pod> -- /bin/bash
```

Run a command:

```bash
kubectl exec <pod> -- env
```

Specific container:

```bash
kubectl exec -it <pod> -c <container> -- /bin/sh
```

---

# 11. Pod Debugging

Inspect:

```bash
kubectl describe pod <pod>
```

Check events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Check Pod status:

```bash
kubectl get pod <pod> -o wide
```

Check previous logs:

```bash
kubectl logs <pod> --previous
```

---

# 12. Pod Status Cheat Sheet

| Status | Meaning |
|---|---|
| Pending | Not yet running |
| Running | Pod is running |
| Succeeded | Completed successfully |
| Failed | Completed with failure |
| Unknown | State could not be obtained |

Common additional conditions:

```text
CrashLoopBackOff
ImagePullBackOff
ErrImagePull
OOMKilled
ContainerCreating
Terminating
```

---

# 13. Deployment Commands

List Deployments:

```bash
kubectl get deployments
```

Create Deployment:

```bash
kubectl create deployment nginx --image=nginx
```

Scale Deployment:

```bash
kubectl scale deployment nginx --replicas=5
```

Describe:

```bash
kubectl describe deployment nginx
```

---

# 14. Deployment Rollouts

Check rollout:

```bash
kubectl rollout status deployment/nginx
```

View history:

```bash
kubectl rollout history deployment/nginx
```

Rollback:

```bash
kubectl rollout undo deployment/nginx
```

Rollback to revision:

```bash
kubectl rollout undo deployment/nginx --to-revision=2
```

Pause rollout:

```bash
kubectl rollout pause deployment/nginx
```

Resume rollout:

```bash
kubectl rollout resume deployment/nginx
```

Restart Deployment:

```bash
kubectl rollout restart deployment/nginx
```

---

# 15. Update Deployment Image

```bash
kubectl set image deployment/nginx nginx=nginx:<version>
```

Example:

```bash
kubectl set image deployment/web web=nginx:1.29
```

---

# 16. ReplicaSet Commands

List:

```bash
kubectl get replicasets
```

Describe:

```bash
kubectl describe replicaset <name>
```

---

# 17. StatefulSet Commands

List:

```bash
kubectl get statefulsets
```

Describe:

```bash
kubectl describe statefulset <name>
```

Restart:

```bash
kubectl rollout restart statefulset/<name>
```

---

# 18. DaemonSet Commands

List:

```bash
kubectl get daemonsets
```

Describe:

```bash
kubectl describe daemonset <name>
```

---

# 19. Job Commands

List Jobs:

```bash
kubectl get jobs
```

Describe:

```bash
kubectl describe job <name>
```

Delete Job:

```bash
kubectl delete job <name>
```

---

# 20. CronJob Commands

List:

```bash
kubectl get cronjobs
```

Describe:

```bash
kubectl describe cronjob <name>
```

Suspend a CronJob:

```bash
kubectl patch cronjob <name> -p '{"spec":{"suspend":true}}'
```

---

# 21. Service Commands

List Services:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc <service>
```

Get Service YAML:

```bash
kubectl get svc <service> -o yaml
```

---

# 22. Service Types

```text
ClusterIP
NodePort
LoadBalancer
ExternalName
```

---

# 23. Expose a Deployment

Create ClusterIP Service:

```bash
kubectl expose deployment nginx \
  --port=80 \
  --target-port=80
```

Create NodePort:

```bash
kubectl expose deployment nginx \
  --type=NodePort \
  --port=80
```

---

# 24. Endpoints

Check Endpoints:

```bash
kubectl get endpoints
```

Check EndpointSlices:

```bash
kubectl get endpointslices
```

This is one of the first places to check when a Service cannot reach Pods.

---

# 25. Ingress Commands

List Ingress:

```bash
kubectl get ingress
```

Describe:

```bash
kubectl describe ingress <name>
```

Get YAML:

```bash
kubectl get ingress <name> -o yaml
```

Remember:

```text
Ingress Resource
        ↓
Ingress Controller
        ↓
Service
        ↓
Pod
```

---

# 26. Gateway API Commands

List GatewayClasses:

```bash
kubectl get gatewayclass
```

List Gateways:

```bash
kubectl get gateway
```

List HTTPRoutes:

```bash
kubectl get httproute
```

Describe:

```bash
kubectl describe gateway <name>
kubectl describe httproute <name>
```

---

# 27. ConfigMap Commands

List:

```bash
kubectl get configmaps
```

Create:

```bash
kubectl create configmap app-config \
  --from-literal=ENV=production
```

Describe:

```bash
kubectl describe configmap app-config
```

Get YAML:

```bash
kubectl get configmap app-config -o yaml
```

---

# 28. Secret Commands

List:

```bash
kubectl get secrets
```

Describe:

```bash
kubectl describe secret <name>
```

Create:

```bash
kubectl create secret generic app-secret \
  --from-literal=password='example'
```

Get YAML:

```bash
kubectl get secret <name> -o yaml
```

Decode a specific field:

```bash
kubectl get secret <name> \
  -o jsonpath='{.data.password}' | base64 --decode
```

Do not expose secret values in shell history, logs, tickets, or chat.

---

# 29. Labels

Show labels:

```bash
kubectl get pods --show-labels
```

Add label:

```bash
kubectl label pod <pod> environment=production
```

Remove label:

```bash
kubectl label pod <pod> environment-
```

---

# 30. Selectors

List Pods by label:

```bash
kubectl get pods -l app=frontend
```

Multiple labels:

```bash
kubectl get pods -l 'app=frontend,environment=production'
```

---

# 31. Annotations

Add annotation:

```bash
kubectl annotate pod <pod> description="frontend"
```

Remove annotation:

```bash
kubectl annotate pod <pod> description-
```

---

# 32. Node Commands

List nodes:

```bash
kubectl get nodes
```

Detailed information:

```bash
kubectl describe node <node>
```

Wide output:

```bash
kubectl get nodes -o wide
```

Node labels:

```bash
kubectl get nodes --show-labels
```

---

# 33. Node Labels

Add label:

```bash
kubectl label node <node> disktype=ssd
```

Remove:

```bash
kubectl label node <node> disktype-
```

---

# 34. Node Scheduling Control

Cordon:

```bash
kubectl cordon <node>
```

Cordon prevents new normal scheduling while leaving existing workloads in place.

Drain:

```bash
kubectl drain <node> --ignore-daemonsets
```

Uncordon:

```bash
kubectl uncordon <node>
```

---

# 35. Node Taints

Add taint:

```bash
kubectl taint nodes <node> dedicated=security:NoSchedule
```

Remove:

```bash
kubectl taint nodes <node> dedicated=security:NoSchedule-
```

Common effects:

```text
NoSchedule
PreferNoSchedule
NoExecute
```

---

# 36. Scheduling Cheat Sheet

```text
nodeSelector
→ Simple node selection

NodeAffinity
→ Advanced node selection

PodAffinity
→ Place Pods near other Pods

PodAntiAffinity
→ Separate Pods

Taint
→ Restrict node scheduling

Toleration
→ Allow Pod to tolerate taint
```

---

# 37. Resource Requests

Example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
```

Remember:

```text
Requests influence scheduling.
```

---

# 38. Resource Limits

Example:

```yaml
resources:
  limits:
    cpu: "1"
    memory: "1Gi"
```

Remember:

```text
Limits define resource boundaries.
```

---

# 39. Resource Monitoring

If Metrics Server is installed:

```bash
kubectl top nodes
```

Pods:

```bash
kubectl top pods
```

All namespaces:

```bash
kubectl top pods -A
```

---

# 40. HPA Commands

List:

```bash
kubectl get hpa
```

Describe:

```bash
kubectl describe hpa <name>
```

Autoscaling:

```bash
kubectl autoscale deployment nginx \
  --min=2 \
  --max=10 \
  --cpu-percent=70
```

---

# 41. VPA

VPA availability and update behavior depend on the VPA implementation installed in the cluster.

Typical objects can be inspected with:

```bash
kubectl get vpa
```

---

# 42. Cluster Autoscaler

Cluster Autoscaler is usually deployed as a cluster component rather than controlled through a simple universal `kubectl autoscale` command.

Typical workflow:

```text
Pending Pods
    ↓
Insufficient Capacity
    ↓
Cluster Autoscaler
    ↓
Node Added
    ↓
Pod Scheduled
```

---

# 43. Storage Commands

List PVs:

```bash
kubectl get pv
```

List PVCs:

```bash
kubectl get pvc
```

All namespaces:

```bash
kubectl get pvc -A
```

StorageClasses:

```bash
kubectl get storageclass
```

---

# 44. PersistentVolume

Describe:

```bash
kubectl describe pv <pv>
```

Get YAML:

```bash
kubectl get pv <pv> -o yaml
```

---

# 45. PersistentVolumeClaim

Describe:

```bash
kubectl describe pvc <pvc>
```

Check status:

```bash
kubectl get pvc
```

Typical states:

```text
Pending
Bound
Lost
```

---

# 46. StorageClass

List:

```bash
kubectl get storageclass
```

Describe:

```bash
kubectl describe storageclass <name>
```

Show default StorageClass:

```bash
kubectl get storageclass
```

Look for:

```text
(default)
```

---

# 47. CSI Troubleshooting

Check CSI-related Pods:

```bash
kubectl get pods -A | grep -i csi
```

Check CSI resources:

```bash
kubectl get csidrivers
```

Describe:

```bash
kubectl describe csidriver <name>
```

---

# 48. Network Commands

List Services:

```bash
kubectl get svc -A
```

List Pods with IPs:

```bash
kubectl get pods -A -o wide
```

List EndpointSlices:

```bash
kubectl get endpointslices -A
```

---

# 49. DNS

Typical Service DNS:

```text
service.namespace.svc.cluster.local
```

Example:

```text
backend.production.svc.cluster.local
```

---

# 50. DNS Troubleshooting

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check CoreDNS Service:

```bash
kubectl get svc -n kube-system
```

Check logs:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Test DNS from a debugging Pod:

```bash
nslookup kubernetes.default.svc.cluster.local
```

---

# 51. CNI

Common CNI implementations include:

```text
Calico
Cilium
Flannel
Antrea
```

Check cluster Pods:

```bash
kubectl get pods -A
```

Look for networking components in the relevant namespace.

---

# 52. NetworkPolicy

List:

```bash
kubectl get networkpolicy
```

All namespaces:

```bash
kubectl get networkpolicy -A
```

Describe:

```bash
kubectl describe networkpolicy <name>
```

---

# 53. NetworkPolicy Mental Model

```text
Source
  ↓
Selector
  ↓
Port / Protocol
  ↓
Allowed or Denied
  ↓
Destination
```

Remember:

```text
Ingress
→ Traffic coming into Pod

Egress
→ Traffic leaving Pod
```

---

# 54. RBAC Commands

List Roles:

```bash
kubectl get roles -A
```

List ClusterRoles:

```bash
kubectl get clusterroles
```

List RoleBindings:

```bash
kubectl get rolebindings -A
```

List ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

---

# 55. Check Permissions

Test:

```bash
kubectl auth can-i get pods
```

As another identity:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:my-sa
```

Namespace:

```bash
kubectl auth can-i get pods -n production
```

---

# 56. RBAC Mental Model

```text
Subject
   ↓
Binding
   ↓
Role / ClusterRole
   ↓
Verb
   ↓
Resource
```

Common verbs:

```text
get
list
watch
create
update
patch
delete
```

---

# 57. ServiceAccount Commands

List:

```bash
kubectl get serviceaccounts
```

Describe:

```bash
kubectl describe serviceaccount <name>
```

Create:

```bash
kubectl create serviceaccount app-sa
```

---

# 58. Security Context

Inspect Pod:

```bash
kubectl get pod <pod> -o yaml
```

Look for:

```yaml
securityContext:
```

Important controls include:

```text
runAsNonRoot
readOnlyRootFilesystem
allowPrivilegeEscalation
capabilities
seccompProfile
```

---

# 59. Pod Security

Namespaces can be labeled for Pod Security admission enforcement.

Example:

```bash
kubectl label namespace production \
  pod-security.kubernetes.io/enforce=restricted
```

Before applying cluster-wide policies, test workloads carefully because restrictive settings can break workloads that rely on privileged behavior.

---

# 60. Admission Control

Admission happens after authentication/authorization and before the object is persisted.

Conceptually:

```text
Request
  ↓
Authentication
  ↓
Authorization
  ↓
Admission
  ↓
Persistence
```

---

# 61. Audit Logs

Kubernetes audit logs record API activity according to the configured audit policy.

Useful for:

```text
Security Investigations
Compliance
Change Tracking
Incident Response
```

---

# 62. Image Security

Best practices:

```text
Trusted Registry
Image Scanning
Minimal Images
SBOM
Image Signing
Digest Pinning
Regular Updates
```

Prefer:

```text
image@sha256:<digest>
```

over mutable tags for highly controlled production deployments.

---

# 63. Runtime Security

Monitor:

```text
Process Execution
File Activity
Network Connections
Privilege Escalation
Container Behavior
System Calls
```

Runtime security tools can complement Kubernetes-native controls.

---

# 64. Logging

Application logs:

```bash
kubectl logs <pod>
```

Previous instance:

```bash
kubectl logs <pod> --previous
```

Node-level logs may require access to the node operating system and depend on the distribution.

---

# 65. Events

List events:

```bash
kubectl get events
```

Sort by timestamp:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Namespace:

```bash
kubectl get events -n production
```

Events are often the fastest way to identify:

```text
Scheduling Failures
Image Pull Failures
Mount Failures
Probe Failures
Admission Errors
```

---

# 66. Debugging Pods

Run a temporary debugging Pod:

```bash
kubectl run debug \
  --image=busybox:1.36 \
  -it --rm --restart=Never \
  -- sh
```

Inside:

```bash
nslookup kubernetes.default
```

or:

```bash
wget -qO- http://service-name
```

Use a purpose-built debugging image if the application container does not contain diagnostic tools.

---

# 67. Port Forwarding

Forward local port:

```bash
kubectl port-forward pod/<pod> 8080:80
```

Service:

```bash
kubectl port-forward svc/<service> 8080:80
```

Useful for:

```text
Local Testing
Debugging
Internal Dashboards
```

---

# 68. Copy Files

Copy from Pod:

```bash
kubectl cp <pod>:/path/file ./file
```

Copy to Pod:

```bash
kubectl cp ./file <pod>:/path/file
```

For multi-container Pods:

```bash
kubectl cp <pod>:/path/file ./file -c <container>
```

---

# 69. Labels and Filtering

```bash
kubectl get pods -l app=api
```

Negation:

```bash
kubectl get pods -l 'environment!=production'
```

---

# 70. JSONPath

Get Pod IP:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.status.podIP}'
```

Get Pod node:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.nodeName}'
```

Get container images:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.containers[*].image}'
```

---

# 71. Custom Columns

```bash
kubectl get pods \
  -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName
```

---

# 72. Wide Output

```bash
kubectl get pods -o wide
```

Useful information includes:

```text
Pod IP
Node
Readiness
Status
```

---

# 73. Sorting

Sort Pods:

```bash
kubectl get pods \
  --sort-by=.metadata.creationTimestamp
```

Sort nodes by CPU capacity:

```bash
kubectl get nodes \
  --sort-by=.status.capacity.cpu
```

---

# 74. Resource Shortcuts

Common resource abbreviations:

```text
po   → pods
deploy → deployments
rs   → replicasets
sts  → statefulsets
ds   → daemonsets
svc  → services
cm   → configmaps
ns   → namespaces
no   → nodes
pv   → persistentvolumes
pvc  → persistentvolumeclaims
sa   → serviceaccounts
```

Example:

```bash
kubectl get po
kubectl get svc
kubectl get deploy
```

---

# 75. Get All Resources

```bash
kubectl get all
```

All namespaces:

```bash
kubectl get all -A
```

Remember that `get all` does not literally include every Kubernetes resource type.

---

# 76. Delete Resources

Delete Pod:

```bash
kubectl delete pod <pod>
```

Delete Deployment:

```bash
kubectl delete deployment <deployment>
```

Delete Service:

```bash
kubectl delete svc <service>
```

Delete namespace:

```bash
kubectl delete namespace <namespace>
```

Use namespace deletion carefully because it can remove many namespaced resources.

---

# 77. Force Deletion

Avoid force deletion unless you understand the consequences.

Example:

```bash
kubectl delete pod <pod> --grace-period=0 --force
```

Potentially dangerous in stateful or storage-sensitive workloads.

---

# 78. Resource Quotas

List:

```bash
kubectl get resourcequota -A
```

Describe:

```bash
kubectl describe resourcequota <name>
```

---

# 79. LimitRanges

List:

```bash
kubectl get limitrange -A
```

Describe:

```bash
kubectl describe limitrange <name>
```

---

# 80. PriorityClasses

List:

```bash
kubectl get priorityclass
```

Describe:

```bash
kubectl describe priorityclass <name>
```

---

# 81. Scheduling Inspection

Check Pod scheduling events:

```bash
kubectl describe pod <pod>
```

Look for:

```text
FailedScheduling
Insufficient cpu
Insufficient memory
Untolerated taint
NodeAffinity
Volume constraints
```

---

# 82. Drain a Node Safely

Typical workflow:

```bash
kubectl cordon <node>
```

Then:

```bash
kubectl drain <node> --ignore-daemonsets
```

After maintenance:

```bash
kubectl uncordon <node>
```

Before draining, understand:

```text
PodDisruptionBudgets
Stateful workloads
Local storage
DaemonSets
Critical workloads
```

---

# 83. PodDisruptionBudget

List:

```bash
kubectl get pdb -A
```

Describe:

```bash
kubectl describe pdb <name>
```

PDBs help limit voluntary disruptions.

---

# 84. Probes

## Readiness

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

Purpose:

```text
Should this Pod receive traffic?
```

---

## Liveness

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
```

Purpose:

```text
Should this container be restarted?
```

---

## Startup

```yaml
startupProbe:
  httpGet:
    path: /startup
    port: 8080
```

Purpose:

```text
Has the application finished starting?
```

---

# 85. Probe Cheat Sheet

```text
Startup
→ Application initialization

Readiness
→ Traffic eligibility

Liveness
→ Restart decision
```

---

# 86. Rolling Update Parameters

Typical Deployment settings:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 25%
    maxSurge: 25%
```

---

# 87. Deployment Strategy

```text
RollingUpdate
→ Gradual replacement

Recreate
→ Replace old Pods before starting new ones
```

---

# 88. YAML Skeleton – Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example
spec:
  containers:
    - name: app
      image: nginx:stable
```

---

# 89. YAML Skeleton – Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:stable
          ports:
            - containerPort: 80
```

---

# 90. YAML Skeleton – Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
```

---

# 91. YAML Skeleton – ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
```

---

# 92. YAML Skeleton – Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  username: example
  password: change-me
```

Do not commit real credentials into Git.

---

# 93. YAML Skeleton – PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

---

# 94. YAML Skeleton – NetworkPolicy

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

---

# 95. YAML Skeleton – ServiceAccount

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
```

---

# 96. YAML Skeleton – Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
  - apiGroups: [""]
    resources:
      - pods
    verbs:
      - get
      - list
      - watch
```

---

# 97. YAML Skeleton – RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
subjects:
  - kind: ServiceAccount
    name: app-sa
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

---

# 98. YAML Skeleton – HPA

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web
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

---

# 99. Helm Commands

Check Helm:

```bash
helm version
```

Add repository:

```bash
helm repo add <name> <url>
```

Update repositories:

```bash
helm repo update
```

Search:

```bash
helm search repo <keyword>
```

Install:

```bash
helm install <release> <chart>
```

Install into namespace:

```bash
helm install <release> <chart> -n <namespace> --create-namespace
```

List releases:

```bash
helm list -A
```

Upgrade:

```bash
helm upgrade <release> <chart>
```

Rollback:

```bash
helm rollback <release> <revision>
```

Uninstall:

```bash
helm uninstall <release>
```

---

# 100. Helm Inspection

Show values:

```bash
helm get values <release>
```

Show all values:

```bash
helm get values <release> -a
```

Show manifest:

```bash
helm get manifest <release>
```

Render locally:

```bash
helm template <release> <chart>
```

Lint:

```bash
helm lint <chart>
```

---

# 101. Kustomize Commands

Build manifests:

```bash
kubectl kustomize .
```

Apply:

```bash
kubectl apply -k .
```

Delete:

```bash
kubectl delete -k .
```

---

# 102. GitOps Cheat Sheet

Typical flow:

```text
Git
 ↓
GitOps Controller
 ↓
Kubernetes API
 ↓
Desired State
 ↓
Cluster
```

Common GitOps platforms include:

```text
Argo CD
Flux
```

---

# 103. Operators

Operator pattern:

```text
Custom Resource
      ↓
Controller
      ↓
Application
      ↓
Reconciliation
```

Inspect CRDs:

```bash
kubectl get crds
```

List custom resources:

```bash
kubectl api-resources
```

---

# 104. Service Mesh

Common technologies:

```text
Istio
Linkerd
```

Core concepts:

```text
mTLS
Traffic Management
Service Identity
Authorization
Observability
Retries
Timeouts
Circuit Breaking
```

---

# 105. Istio Commands

Check Istio workloads:

```bash
kubectl get pods -n istio-system
```

Check proxies:

```bash
istioctl proxy-status
```

Analyze configuration:

```bash
istioctl analyze -A
```

Inspect routes:

```bash
istioctl proxy-config routes <pod> -n <namespace>
```

Inspect clusters:

```bash
istioctl proxy-config clusters <pod> -n <namespace>
```

Inspect listeners:

```bash
istioctl proxy-config listeners <pod> -n <namespace>
```

---

# 106. Linkerd Commands

Check Linkerd:

```bash
linkerd check
```

Inspect workloads:

```bash
linkerd viz stat deploy -n <namespace>
```

Traffic:

```bash
linkerd viz top deploy/<deployment> -n <namespace>
```

---

# 107. Prometheus Quick Reference

Common metric concepts:

```text
Counter
Gauge
Histogram
Summary
```

---

# 108. PromQL Examples

CPU usage:

```promql
rate(container_cpu_usage_seconds_total[5m])
```

Memory:

```promql
container_memory_working_set_bytes
```

Request rate:

```promql
rate(http_requests_total[5m])
```

Error rate:

```promql
rate(http_requests_total{status=~"5.."}[5m])
```

Always verify metric names because they depend on the exporters and monitoring stack installed.

---

# 109. Grafana

Typical workflow:

```text
Prometheus
    ↓
Grafana
    ↓
Dashboard
```

Useful dashboards include:

```text
Cluster Health
Node Health
Pod Resources
API Server
Network
Storage
Application Metrics
```

---

# 110. Alertmanager

Alert flow:

```text
Prometheus
   ↓
Alert Rule
   ↓
Alertmanager
   ↓
Routing
   ↓
Notification
```

Possible destinations include:

```text
Email
PagerDuty
Slack
Webhook
```

depending on configuration.

---

# 111. OpenTelemetry

Telemetry:

```text
Metrics
Logs
Traces
```

Typical architecture:

```text
Application
    ↓
OpenTelemetry SDK / Collector
    ↓
Backend
```

---

# 112. Distributed Tracing

Example:

```text
Frontend
   ↓
API
   ↓
Orders
   ↓
Payments
```

A trace connects these operations into one request journey.

---

# 113. Production Monitoring Checklist

Monitor:

```text
☑ CPU
☑ Memory
☑ Disk
☑ Network
☑ Pod Restarts
☑ Pod Readiness
☑ Node Health
☑ API Server
☑ etcd
☑ Scheduler
☑ Controllers
☑ DNS
☑ Storage
☑ Application Latency
☑ Error Rate
☑ Request Rate
```

---

# 114. Backup Cheat Sheet

Back up:

```text
etcd
Application Data
Persistent Volumes
Configuration
Custom Resources
Secrets
```

Do not assume that backing up Kubernetes object definitions alone protects application data.

---

# 115. Disaster Recovery

Basic DR workflow:

```text
Detect
 ↓
Assess
 ↓
Contain
 ↓
Restore Infrastructure
 ↓
Restore Kubernetes State
 ↓
Restore Storage
 ↓
Restore Applications
 ↓
Validate
 ↓
Monitor
```

---

# 116. Upgrade Checklist

```text
☑ Read release notes
☑ Check version skew
☑ Check API deprecations
☑ Backup
☑ Test
☑ Validate add-ons
☑ Upgrade control plane
☑ Upgrade nodes
☑ Validate workloads
☑ Monitor
```

---

# 117. High Availability

Production HA usually involves:

```text
Multiple Control-Plane Nodes
Multiple etcd Members
Load-Balanced API Server
Multiple Worker Nodes
Multiple Failure Domains
Replicated Applications
Redundant Storage
```

---

# 118. Production Best Practices

```text
☑ Use declarative configuration
☑ Store manifests in Git
☑ Use namespaces
☑ Use RBAC
☑ Apply least privilege
☑ Use NetworkPolicy
☑ Scan images
☑ Pin important images
☑ Use resource requests
☑ Use sensible limits
☑ Configure probes
☑ Use PodDisruptionBudgets
☑ Monitor everything important
☑ Back up critical data
☑ Test restoration
☑ Use HA
☑ Automate deployments
☑ Test upgrades
☑ Document recovery procedures
```

---

# 119. Kubernetes Troubleshooting Flow

```text
Problem
   │
   ▼
kubectl get
   │
   ▼
kubectl describe
   │
   ▼
kubectl logs
   │
   ▼
kubectl logs --previous
   │
   ▼
kubectl get events
   │
   ▼
Check Dependencies
   │
   ├── DNS
   ├── Service
   ├── NetworkPolicy
   ├── Storage
   ├── RBAC
   └── Node
   │
   ▼
Root Cause
   │
   ▼
Fix
   │
   ▼
Validate
```

---

# 120. Pending Pod Flow

```text
Pod Pending
    ↓
kubectl describe pod
    ↓
Check Events
    ↓
Resource Capacity?
    │
    ├── No → Add/Free Capacity
    │
    └── Yes
         ↓
Taints?
         ↓
Affinity?
         ↓
NodeSelector?
         ↓
PVC?
         ↓
Quota?
```

---

# 121. CrashLoopBackOff Flow

```text
CrashLoopBackOff
      ↓
kubectl logs --previous
      ↓
kubectl describe pod
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
Secret?
           ↓
Dependency?
           ↓
OOMKilled?
```

---

# 122. ImagePullBackOff Flow

```text
ImagePullBackOff
      ↓
Check Image Name
      ↓
Check Tag
      ↓
Check Registry
      ↓
Private Registry?
      │
      ├── Yes → Check ImagePullSecret
      │
      └── No
           ↓
Check Network
           ↓
Check Image Availability
```

---

# 123. Service Failure Flow

```text
Client
  ↓
Service
  ↓
Endpoints?
  │
  ├── No → Selector / Labels / Readiness
  │
  └── Yes
       ↓
Port Correct?
       ↓
TargetPort Correct?
       ↓
Application Listening?
       ↓
NetworkPolicy?
       ↓
DNS?
```

---

# 124. DNS Failure Flow

```text
DNS Failure
    ↓
CoreDNS Running?
    ↓
CoreDNS Service?
    ↓
Pod DNS Configuration?
    ↓
NetworkPolicy?
    ↓
CNI?
    ↓
Upstream DNS?
```

---

# 125. PVC Failure Flow

```text
PVC Pending
    ↓
StorageClass
    ↓
CSI Driver
    ↓
Provisioner
    ↓
Capacity
    ↓
Access Mode
    ↓
Topology
    ↓
PV
```

---

# 126. RBAC Failure Flow

```text
403 Forbidden
     ↓
Who?
     ↓
ServiceAccount / User
     ↓
RoleBinding?
     ↓
Role?
     ↓
Verb?
     ↓
Resource?
     ↓
Namespace?
```

Use:

```bash
kubectl auth can-i
```

---

# 127. Node Failure Flow

```text
Node NotReady
     ↓
kubectl describe node
     ↓
Kubelet
     ↓
Runtime
     ↓
Disk
     ↓
Memory
     ↓
Network
     ↓
Certificates
```

---

# 128. Security Incident Flow

```text
Detection
    ↓
Validation
    ↓
Containment
    ↓
Evidence Preservation
    ↓
Investigation
    ↓
Credential Rotation
    ↓
Eradication
    ↓
Recovery
    ↓
Monitoring
    ↓
Root Cause Analysis
```

---

# 129. Kubernetes Security Quick Reference

```text
Authentication
→ Who are you?

Authorization
→ What can you do?

Admission
→ Should this request be accepted or modified?

RBAC
→ Permission model

ServiceAccount
→ Workload identity

NetworkPolicy
→ Network access control

Pod Security
→ Pod-level security standards

Secret
→ Sensitive configuration object

Audit
→ API activity record

Runtime Security
→ Detect/Prevent malicious workload behavior
```

---

# 130. Kubernetes Networking Quick Reference

```text
Pod
 ↓
Pod IP
 ↓
Service
 ↓
Ingress / Gateway
 ↓
External Client
```

Supporting components:

```text
CNI
CoreDNS
kube-proxy / equivalent networking
NetworkPolicy
Load Balancer
Ingress Controller
Gateway Controller
```

---

# 131. Kubernetes Storage Quick Reference

```text
Application
    ↓
Pod
    ↓
PVC
    ↓
PV
    ↓
CSI
    ↓
Storage Backend
```

---

# 132. Kubernetes Scheduling Quick Reference

```text
Pod
 ↓
Requests
 ↓
Scheduler
 ↓
NodeSelector
 ↓
Affinity
 ↓
Taints / Tolerations
 ↓
Topology Constraints
 ↓
Node
```

---

# 133. Autoscaling Quick Reference

```text
HPA
→ Pod count

VPA
→ Pod resource allocation

Cluster Autoscaler
→ Node count
```

---

# 134. Workload Quick Reference

```text
Pod
→ Smallest deployable unit

Deployment
→ Stateless applications

StatefulSet
→ Stable identity/state

DaemonSet
→ Node-level agent

Job
→ One-time task

CronJob
→ Scheduled task
```

---

# 135. Service Quick Reference

```text
ClusterIP
→ Internal access

NodePort
→ Node-level external port

LoadBalancer
→ External load balancer

ExternalName
→ DNS alias
```

---

# 136. Storage Access Modes

Common access modes:

```text
ReadWriteOnce
ReadOnlyMany
ReadWriteMany
ReadWriteOncePod
```

Actual support depends on the storage driver and backend.

---

# 137. PersistentVolume Reclaim Policies

Common policies:

```text
Retain
Delete
```

`Recycle` is deprecated/removed in modern Kubernetes usage and should not be treated as a production option.

---

# 138. Service Discovery

Inside a namespace:

```text
service-name
```

Across namespaces:

```text
service-name.namespace
```

Full DNS:

```text
service-name.namespace.svc.cluster.local
```

---

# 139. Kubernetes API Object Structure

Typical object:

```yaml
apiVersion: ...
kind: ...
metadata:
  name: ...
spec:
  ...
status:
  ...
```

Remember:

```text
spec
→ Desired state

status
→ Observed state
```

---

# 140. Declarative vs Imperative

Imperative:

```bash
kubectl create deployment nginx --image=nginx
```

Declarative:

```bash
kubectl apply -f deployment.yaml
```

Production workflows generally favor declarative configuration and version control.

---

# 141. Desired State vs Actual State

Kubernetes continuously reconciles:

```text
Desired State
      │
      ▼
Controllers
      │
      ▼
Actual State
```

If they differ:

```text
Actual State
      ↓
Reconciliation
      ↓
Desired State
```

This is one of the most important Kubernetes concepts.

---

# 142. Labels vs Annotations

```text
Labels
→ Identify and select objects

Annotations
→ Store additional metadata
```

---

# 143. Requests vs Limits

```text
Request
→ Scheduling reservation/expectation

Limit
→ Maximum resource boundary
```

---

# 144. Readiness vs Liveness

```text
Readiness
→ Receive traffic?

Liveness
→ Restart?

Startup
→ Finished starting?
```

---

# 145. Authentication vs Authorization

```text
Authentication
→ Who are you?

Authorization
→ What can you do?
```

---

# 146. Ingress vs Gateway API

```text
Ingress
→ Established HTTP/HTTPS routing API

Gateway API
→ More expressive, role-oriented networking APIs
```

---

# 147. Service vs EndpointSlice

```text
Service
→ Stable access abstraction

EndpointSlice
→ Backend endpoint information
```

---

# 148. PV vs PVC

```text
PV
→ Storage resource

PVC
→ Storage request
```

---

# 149. Static vs Dynamic Provisioning

```text
Static
→ Administrator creates PV

Dynamic
→ PVC triggers storage provisioning
```

---

# 150. Service Mesh Quick Reference

```text
Application
    ↓
Proxy / Mesh
    ↓
Network
    ↓
Proxy / Mesh
    ↓
Application
```

Capabilities:

```text
mTLS
Traffic Management
Identity
Authorization
Retries
Timeouts
Observability
```

---

# 151. Kubernetes Production Checklist

## Cluster

```text
☐ HA control plane
☐ etcd backup
☐ Multiple failure domains
☐ Capacity planning
☐ Upgrade strategy
```

## Workloads

```text
☐ Resource requests
☐ Resource limits
☐ Readiness probes
☐ Liveness probes
☐ Startup probes where needed
☐ PodDisruptionBudgets
```

## Networking

```text
☐ CNI
☐ DNS
☐ Services
☐ NetworkPolicy
☐ Ingress/Gateway
☐ Egress controls
```

## Security

```text
☐ RBAC
☐ Least privilege
☐ ServiceAccounts
☐ Pod Security
☐ Secret management
☐ Image scanning
☐ Image signing
☐ Audit logging
☐ Runtime security
```

## Storage

```text
☐ CSI
☐ StorageClasses
☐ Backup
☐ Restore testing
☐ Capacity monitoring
```

## Observability

```text
☐ Metrics
☐ Logs
☐ Traces
☐ Alerts
☐ Dashboards
```

---

# 152. Emergency Command Reference

Check cluster:

```bash
kubectl get nodes
```

Check all Pods:

```bash
kubectl get pods -A
```

Check recent events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Check failing Pod:

```bash
kubectl describe pod <pod> -n <namespace>
```

Check logs:

```bash
kubectl logs <pod> -n <namespace>
```

Check previous logs:

```bash
kubectl logs <pod> -n <namespace> --previous
```

Check nodes:

```bash
kubectl describe node <node>
```

Check resources:

```bash
kubectl top nodes
kubectl top pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Check EndpointSlices:

```bash
kubectl get endpointslices -A
```

Check PVCs:

```bash
kubectl get pvc -A
```

Check RBAC:

```bash
kubectl auth can-i get pods
```

---

# 153. Commands to Avoid Using Blindly

Be careful with:

```bash
kubectl delete namespace
```

```bash
kubectl delete pod --force --grace-period=0
```

```bash
kubectl delete pvc
```

```bash
kubectl delete pv
```

```bash
kubectl drain
```

```bash
kubectl taint nodes
```

These can have significant production impact.

Always understand:

```text
Scope
Dependencies
Data
Recovery
```

before executing destructive commands.

---

# 154. Interview One-Liners

### Kubernetes

```text
Container orchestration platform.
```

### Pod

```text
Smallest deployable Kubernetes unit.
```

### Deployment

```text
Manages stateless application replicas and rollouts.
```

### StatefulSet

```text
Manages workloads requiring stable identity and storage.
```

### DaemonSet

```text
Runs a Pod on each eligible node.
```

### Service

```text
Provides stable networking for selected Pods.
```

### Ingress

```text
Routes HTTP/HTTPS traffic to Services.
```

### Gateway API

```text
Role-oriented Kubernetes networking API family.
```

### ConfigMap

```text
Non-sensitive configuration.
```

### Secret

```text
Object designed for sensitive configuration data.
```

### CNI

```text
Container networking interface.
```

### CoreDNS

```text
Cluster DNS.
```

### NetworkPolicy

```text
Controls network traffic to and from Pods.
```

### PV

```text
Persistent storage resource.
```

### PVC

```text
Request for persistent storage.
```

### StorageClass

```text
Defines storage provisioning behavior.
```

### CSI

```text
Standard interface for storage integrations.
```

### Scheduler

```text
Assigns unscheduled Pods to nodes.
```

### RBAC

```text
Role-based authorization model.
```

### ServiceAccount

```text
Identity used by workloads.
```

### HPA

```text
Scales Pod replicas.
```

### VPA

```text
Adjusts or recommends Pod resource allocation.
```

### Cluster Autoscaler

```text
Adjusts cluster node count.
```

### Prometheus

```text
Metrics monitoring and alerting system.
```

### Grafana

```text
Observability visualization platform.
```

### OpenTelemetry

```text
Vendor-neutral telemetry framework.
```

### Service Mesh

```text
Infrastructure layer for service-to-service communication.
```

---

# 155. Top 20 Commands to Memorize

```bash
kubectl get pods
```

```bash
kubectl get pods -A
```

```bash
kubectl describe pod <pod>
```

```bash
kubectl logs <pod>
```

```bash
kubectl logs <pod> --previous
```

```bash
kubectl exec -it <pod> -- /bin/sh
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl get nodes
```

```bash
kubectl describe node <node>
```

```bash
kubectl get events --sort-by=.lastTimestamp
```

```bash
kubectl apply -f <file>
```

```bash
kubectl delete -f <file>
```

```bash
kubectl rollout status deployment/<name>
```

```bash
kubectl rollout undo deployment/<name>
```

```bash
kubectl get pvc
```

```bash
kubectl get pv
```

```bash
kubectl get networkpolicy
```

```bash
kubectl auth can-i get pods
```

```bash
kubectl top pods
```

---

# 156. Top 10 Troubleshooting Commands

```bash
kubectl get pods -A
```

```bash
kubectl describe pod <pod>
```

```bash
kubectl logs <pod>
```

```bash
kubectl logs <pod> --previous
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

```bash
kubectl get nodes
```

```bash
kubectl describe node <node>
```

```bash
kubectl top pods -A
```

---

# 157. 10-Step Production Troubleshooting Method

```text
1. Identify the symptom
2. Determine affected scope
3. Check recent changes
4. Inspect resource status
5. Inspect events
6. Inspect logs
7. Check dependencies
8. Isolate root cause
9. Apply minimal safe remediation
10. Validate and monitor
```

---

# 158. Final Kubernetes Mental Model

```text
                     KUBERNETES
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     Control           Workloads       Networking
      Plane               │                │
        │                 │                │
   ┌────┼────┐       ┌────┼────┐      ┌────┼────┐
   ▼    ▼    ▼       ▼    ▼    ▼      ▼    ▼    ▼
  API  etcd Sched   Pod Deploy STS   Svc Ingress DNS
                    │
                    ▼
                 Storage
                    │
               ┌────┼────┐
               ▼    ▼    ▼
              PV   PVC  CSI
                    │
                    ▼
                Scheduling
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
          Affinity Taint Resources
                    │
                    ▼
                 Security
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
            RBAC   PSS   Network
                    │
                    ▼
               Observability
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
           Logs  Metrics  Traces
                    │
                    ▼
                Operations
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        Backup     HA        DR
```

---

# 159. Final Revision

## Kubernetes

```text
Container Orchestration
```

## Control Plane

```text
API Server
etcd
Scheduler
Controllers
```

## Worker Node

```text
Kubelet
Container Runtime
Networking
```

## Workloads

```text
Pod
Deployment
StatefulSet
DaemonSet
Job
CronJob
```

## Networking

```text
Service
Ingress
Gateway API
CNI
CoreDNS
NetworkPolicy
```

## Storage

```text
Volume
PV
PVC
StorageClass
CSI
```

## Scheduling

```text
Scheduler
NodeSelector
Affinity
Anti-Affinity
Taints
Tolerations
Requests
Limits
```

## Autoscaling

```text
HPA
VPA
Cluster Autoscaler
```

## Security

```text
Authentication
RBAC
ServiceAccounts
Admission
Pod Security
Secrets
Image Security
Runtime Security
Audit
```

## Observability

```text
Logs
Metrics
Traces
Prometheus
Grafana
Alertmanager
OpenTelemetry
```

## Operations

```text
Backup
Restore
Upgrade
HA
DR
Maintenance
Optimization
```

## Advanced

```text
GitOps
CI/CD
Helm
Kustomize
Operators
Service Mesh
```

---

# 160. Final Takeaway

The most important Kubernetes commands are not the ones you memorize.

The most important skill is knowing **which command to use for a particular problem**.

A production Kubernetes engineer should think:

```text
Observe
   ↓
Understand
   ↓
Investigate
   ↓
Secure
   ↓
Fix
   ↓
Validate
   ↓
Automate
```

The fundamental Kubernetes mental model is:

```text
Desired State
      ↓
Kubernetes API
      ↓
Controllers
      ↓
Scheduling
      ↓
Workloads
      ↓
Networking + Storage
      ↓
Observed State
      ↓
Reconciliation
      ↺
```

And the production mindset is:

```text
Availability
+
Security
+
Observability
+
Scalability
+
Reliability
+
Automation
+
Recoverability
```

> **Kubernetes expertise is not simply knowing `kubectl`. It is understanding the control loop, distributed architecture, networking, storage, security, scheduling, observability, and operational behavior well enough to diagnose and safely operate real workloads.**

---

# Course Completion

With this chapter, the Kubernetes interview and cheat-sheet section is complete.

The remaining practical-learning chapters are:

```text
Chapter 86 – Hands-on Labs
Chapter 87 – Real-World Case Studies
Chapter 88 – Troubleshooting Playbook
Chapter 89 – Production Operations Checklist
```

These chapters move from **knowledge → practical implementation → real-world troubleshooting → production operations**.