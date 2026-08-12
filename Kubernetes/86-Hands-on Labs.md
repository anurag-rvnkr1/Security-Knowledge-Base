# Chapter 86 – Hands-on Labs

## Overview

This chapter provides a progressive set of practical Kubernetes labs designed to convert theoretical knowledge into real operational skills.

The labs progress from:

```text
Beginner
   ↓
Intermediate
   ↓
Advanced
   ↓
Security
   ↓
Networking
   ↓
Storage
   ↓
Scheduling
   ↓
Observability
   ↓
Production
```

These labs are suitable for:

- Kubernetes beginners
- DevOps learners
- Cloud engineers
- SRE learners
- Platform engineers
- Cybersecurity engineers
- Kubernetes security practitioners
- Interview preparation
- Production readiness training

---

# Learning Objectives

By completing these labs, you should be able to:

- Deploy applications on Kubernetes
- Create and manage Pods
- Create Deployments
- Perform rolling updates
- Roll back deployments
- Configure Services
- Configure Ingress
- Work with ConfigMaps
- Work with Secrets
- Configure persistent storage
- Use PVs and PVCs
- Work with StorageClasses
- Understand CSI-based storage
- Configure scheduling rules
- Use node affinity
- Use taints and tolerations
- Configure resource requests and limits
- Configure HPA
- Implement NetworkPolicies
- Configure RBAC
- Debug failed workloads
- Monitor Kubernetes resources
- Work with Helm
- Understand GitOps workflows
- Perform production-style troubleshooting
- Practice Kubernetes security operations

---

# Lab Environment

You can perform these labs using one of the following environments:

```text
Minikube
Kind
K3d
Docker Desktop Kubernetes
Managed Kubernetes
```

For advanced labs, a real multi-node cluster is preferable.

---

# Recommended Local Tools

Install:

```text
kubectl
Docker
Minikube / Kind / K3d
Helm
Git
curl
jq
```

Optional:

```text
Prometheus
Grafana
Argo CD
Istio
Cilium
Trivy
OpenTelemetry
```

---

# Lab Rules

Follow these principles:

```text
1. Read the objective.
2. Understand the expected behavior.
3. Create the resources.
4. Verify the result.
5. Intentionally break something.
6. Troubleshoot it.
7. Restore the system.
8. Document the lesson.
```

The most valuable part of a lab is often the troubleshooting exercise.

---

# Lab 1 – Create Your First Kubernetes Cluster

## Objective

Create a local Kubernetes cluster.

Using Minikube:

```bash
minikube start
```

Verify:

```bash
kubectl cluster-info
```

Check nodes:

```bash
kubectl get nodes
```

Expected:

```text
STATUS
Ready
```

---

## Verification

```bash
kubectl get nodes -o wide
```

---

## Challenge

Answer:

1. How many nodes exist?
2. What Kubernetes version is running?
3. Which container runtime is being used?
4. What is the node's internal IP?

---

# Lab 2 – Create a Pod

## Objective

Create a simple NGINX Pod.

```bash
kubectl run nginx \
  --image=nginx:stable
```

Check:

```bash
kubectl get pods
```

---

## Inspect

```bash
kubectl describe pod nginx
```

Get YAML:

```bash
kubectl get pod nginx -o yaml
```

---

## Test

```bash
kubectl port-forward pod/nginx 8080:80
```

Open:

```text
http://localhost:8080
```

---

## Cleanup

```bash
kubectl delete pod nginx
```

---

# Lab 3 – Create a Deployment

## Objective

Create a Deployment with three replicas.

```bash
kubectl create deployment web \
  --image=nginx:stable
```

Scale:

```bash
kubectl scale deployment web --replicas=3
```

Verify:

```bash
kubectl get deployment
kubectl get pods -o wide
```

---

# Lab 4 – Create a Deployment Using YAML

Create:

```text
deployment.yaml
```

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

Apply:

```bash
kubectl apply -f deployment.yaml
```

Verify:

```bash
kubectl get deployment
kubectl get pods
```

---

# Lab 5 – Scale a Deployment

Scale from:

```text
3 → 5
```

Command:

```bash
kubectl scale deployment web --replicas=5
```

Verify:

```bash
kubectl get pods
```

Then scale down:

```bash
kubectl scale deployment web --replicas=2
```

---

# Lab 6 – Rolling Update

## Objective

Update the NGINX version.

Check:

```bash
kubectl get deployment
```

Update:

```bash
kubectl set image deployment/web \
  web=nginx:1.29
```

Monitor:

```bash
kubectl rollout status deployment/web
```

---

# Lab 7 – Rollback

Check history:

```bash
kubectl rollout history deployment/web
```

Rollback:

```bash
kubectl rollout undo deployment/web
```

Verify:

```bash
kubectl rollout status deployment/web
```

---

# Lab 8 – Create a ClusterIP Service

Expose the Deployment:

```bash
kubectl expose deployment web \
  --port=80 \
  --target-port=80
```

Check:

```bash
kubectl get svc
```

---

# Lab 9 – Test Service Connectivity

Run a temporary Pod:

```bash
kubectl run curl \
  --image=curlimages/curl:latest \
  -it --rm \
  --restart=Never -- sh
```

Inside:

```bash
curl http://web
```

Expected:

```text
NGINX response
```

---

# Lab 10 – Investigate Service Endpoints

Check:

```bash
kubectl get endpoints web
```

Also:

```bash
kubectl get endpointslices
```

Questions:

1. Which Pods are selected?
2. What IP addresses are present?
3. Which ports are exposed?

---

# Lab 11 – Break the Service

Change the Pod label so it no longer matches the Service selector.

Inspect:

```bash
kubectl get svc web -o yaml
kubectl get pods --show-labels
```

Check:

```bash
kubectl get endpoints web
```

Expected:

```text
No matching endpoints
```

Fix the labels and verify recovery.

---

# Lab 12 – NodePort Service

Create:

```bash
kubectl expose deployment web \
  --type=NodePort \
  --port=80
```

Check:

```bash
kubectl get svc web
```

Find the assigned NodePort.

For Minikube:

```bash
minikube service web
```

---

# Lab 13 – ConfigMap

Create:

```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=development \
  --from-literal=LOG_LEVEL=info
```

Check:

```bash
kubectl get configmap
```

Inspect:

```bash
kubectl describe configmap app-config
```

---

# Lab 14 – Inject ConfigMap as Environment Variables

Create a Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-test
spec:
  containers:
    - name: app
      image: busybox:1.36
      command:
        - sh
        - -c
        - |
          env
          sleep 3600
      envFrom:
        - configMapRef:
            name: app-config
```

Apply:

```bash
kubectl apply -f config-test.yaml
```

Check:

```bash
kubectl exec config-test -- env
```

---

# Lab 15 – Secret

Create:

```bash
kubectl create secret generic app-secret \
  --from-literal=username=admin \
  --from-literal=password='change-me'
```

Check:

```bash
kubectl get secret app-secret
```

Inspect metadata:

```bash
kubectl describe secret app-secret
```

Do not expose secret values unnecessarily.

---

# Lab 16 – Mount a Secret

Example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-test
spec:
  containers:
    - name: app
      image: busybox:1.36
      command:
        - sh
        - -c
        - sleep 3600
      volumeMounts:
        - name: secret-volume
          mountPath: /etc/app-secret
          readOnly: true
  volumes:
    - name: secret-volume
      secret:
        secretName: app-secret
```

Check:

```bash
kubectl exec secret-test -- ls /etc/app-secret
```

---

# Lab 17 – PersistentVolumeClaim

Create:

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
      storage: 1Gi
```

Apply:

```bash
kubectl apply -f pvc.yaml
```

Check:

```bash
kubectl get pvc
kubectl get pv
```

---

# Lab 18 – Dynamic Provisioning

Check StorageClasses:

```bash
kubectl get storageclass
```

Create a PVC.

Then:

```bash
kubectl get pv
```

Observe:

```text
PVC
 ↓
StorageClass
 ↓
Dynamic Provisioning
 ↓
PV
```

---

# Lab 19 – Persistent Data

Create a Pod using the PVC.

Write data:

```bash
echo "persistent-data" > /data/message.txt
```

Delete the Pod.

Create another Pod using the same PVC.

Verify:

```bash
cat /data/message.txt
```

Expected:

```text
persistent-data
```

---

# Lab 20 – Storage Failure Simulation

Break the PVC configuration.

Examples:

```text
Wrong StorageClass
Unsupported Access Mode
Insufficient Capacity
Missing CSI Driver
```

Run:

```bash
kubectl describe pvc <name>
```

Use events to identify the cause.

---

# Lab 21 – Node Labels

Label a node:

```bash
kubectl label node <node> disktype=ssd
```

Verify:

```bash
kubectl get nodes --show-labels
```

---

# Lab 22 – NodeSelector

Create:

```yaml
spec:
  nodeSelector:
    disktype: ssd
```

Deploy the Pod.

Verify:

```bash
kubectl get pod -o wide
```

Confirm the Pod runs on the labeled node.

---

# Lab 23 – Node Affinity

Example:

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: disktype
              operator: In
              values:
                - ssd
```

Verify:

```bash
kubectl describe pod <pod>
```

---

# Lab 24 – Taints and Tolerations

Taint a node:

```bash
kubectl taint nodes <node> dedicated=security:NoSchedule
```

Deploy a normal Pod.

Observe:

```text
Pod → Pending
```

Check:

```bash
kubectl describe pod <pod>
```

Then add:

```yaml
tolerations:
  - key: dedicated
    operator: Equal
    value: security
    effect: NoSchedule
```

The Pod should now be eligible for that tainted node, subject to other scheduling constraints.

---

# Lab 25 – Pod Anti-Affinity

Deploy multiple replicas with anti-affinity.

Goal:

```text
Replica 1 → Node A
Replica 2 → Node B
Replica 3 → Node C
```

Use:

```yaml
podAntiAffinity:
```

Verify:

```bash
kubectl get pods -o wide
```

---

# Lab 26 – Resource Requests

Create:

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
```

Deploy.

Inspect:

```bash
kubectl describe pod <pod>
```

---

# Lab 27 – Resource Limits

Add:

```yaml
resources:
  limits:
    cpu: "500m"
    memory: "256Mi"
```

Observe resource behavior.

---

# Lab 28 – Simulate OOMKilled

Create a container with a small memory limit and intentionally allocate more memory than permitted.

Observe:

```bash
kubectl get pod
kubectl describe pod <pod>
```

Look for:

```text
OOMKilled
```

Learn why resource limits must be chosen carefully.

---

# Lab 29 – HPA

Create a Deployment with CPU requests.

Example:

```yaml
resources:
  requests:
    cpu: "100m"
```

Create HPA:

```bash
kubectl autoscale deployment web \
  --cpu-percent=50 \
  --min=2 \
  --max=10
```

Check:

```bash
kubectl get hpa
```

---

# Lab 30 – Generate Load

Inside the cluster, generate HTTP traffic against the Service.

Observe:

```bash
kubectl get hpa -w
```

Then:

```bash
kubectl get pods
```

Observe replica changes.

---

# Lab 31 – NetworkPolicy

## Objective

Create:

```text
frontend
backend
```

Allow:

```text
frontend → backend
```

Deny unrelated Pods.

---

## Step 1

Create backend:

```yaml
labels:
  app: backend
```

---

## Step 2

Create frontend:

```yaml
labels:
  app: frontend
```

---

## Step 3

Apply NetworkPolicy.

Test connectivity before and after the policy.

---

# Lab 32 – Default Deny

Create namespace-wide default deny:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

Observe how traffic changes.

Then create explicit allow rules.

---

# Lab 33 – DNS Testing

Create a debug Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  -it --rm \
  --restart=Never -- sh
```

Inside:

```bash
nslookup kubernetes.default
```

Test:

```bash
nslookup web.default.svc.cluster.local
```

---

# Lab 34 – Break DNS

Apply a restrictive NetworkPolicy that prevents DNS traffic.

Test:

```bash
nslookup web
```

Observe failure.

Troubleshoot:

```text
Pod
 ↓
DNS
 ↓
NetworkPolicy
 ↓
CoreDNS
```

Restore DNS connectivity.

---

# Lab 35 – RBAC

Create ServiceAccount:

```bash
kubectl create serviceaccount app-sa
```

Create a Role allowing:

```text
get pods
list pods
watch pods
```

Bind it using RoleBinding.

---

# Lab 36 – Test RBAC

Check:

```bash
kubectl auth can-i \
  get pods \
  --as=system:serviceaccount:default:app-sa
```

Expected:

```text
yes
```

Check unauthorized operation:

```bash
kubectl auth can-i \
  delete deployments \
  --as=system:serviceaccount:default:app-sa
```

Expected:

```text
no
```

---

# Lab 37 – Least Privilege

Start with an overly broad Role.

For example:

```text
*
```

Then reduce permissions to only:

```text
get
list
watch
```

and only:

```text
pods
```

Compare the security posture.

---

# Lab 38 – ServiceAccount Security

Create a workload with a dedicated ServiceAccount.

Avoid using unnecessarily powerful identities.

Check:

```bash
kubectl get pod <pod> -o yaml
```

Inspect:

```text
serviceAccountName
```

---

# Lab 39 – Pod Security

Create a namespace:

```bash
kubectl create namespace secure-lab
```

Apply restricted Pod Security enforcement:

```bash
kubectl label namespace secure-lab \
  pod-security.kubernetes.io/enforce=restricted
```

Attempt to deploy a privileged workload.

Observe the admission rejection.

---

# Lab 40 – Security Context

Create a Pod using:

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
```

For the container:

```yaml
securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true
```

Test whether the application works under these restrictions.

---

# Lab 41 – Image Security Scanning

Install a scanner such as Trivy.

Scan an image:

```bash
trivy image nginx:stable
```

Review:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Investigate critical vulnerabilities.

---

# Lab 42 – Image Digest Pinning

Inspect image information and identify the digest.

Use:

```text
image@sha256:<digest>
```

instead of relying exclusively on mutable tags.

Discuss:

```text
Reproducibility
Integrity
Supply Chain Security
```

---

# Lab 43 – Deployment Probes

Create:

```text
Readiness Probe
Liveness Probe
Startup Probe
```

Observe:

```text
Ready
NotReady
Restart
Startup behavior
```

---

# Lab 44 – Break Readiness

Configure an incorrect readiness endpoint.

Observe:

```bash
kubectl get pods
kubectl get endpoints
```

The Pod may remain running but should not receive Service traffic when readiness is false.

---

# Lab 45 – Break Liveness

Configure an intentionally failing liveness probe.

Observe:

```bash
kubectl get pod
```

Then:

```bash
kubectl describe pod <pod>
```

Look for restart activity.

---

# Lab 46 – CrashLoopBackOff Investigation

Create a Pod that exits repeatedly.

Example:

```yaml
command:
  - sh
  - -c
  - exit 1
```

Observe:

```bash
kubectl get pod
```

Then investigate:

```bash
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl describe pod <pod>
```

---

# Lab 47 – ImagePullBackOff Investigation

Deploy an invalid image:

```yaml
image: nginx:does-not-exist
```

Observe:

```bash
kubectl get pods
```

Then:

```bash
kubectl describe pod <pod>
```

Identify the exact image pull error.

---

# Lab 48 – Pending Pod Investigation

Create a Pod with impossible resource requests.

Example:

```yaml
resources:
  requests:
    cpu: "100"
    memory: "1Ti"
```

Observe:

```bash
kubectl get pod
```

Then:

```bash
kubectl describe pod <pod>
```

Identify:

```text
FailedScheduling
```

---

# Lab 49 – Node Maintenance

Choose a worker node.

Cordon:

```bash
kubectl cordon <node>
```

Verify:

```bash
kubectl get nodes
```

Drain:

```bash
kubectl drain <node> --ignore-daemonsets
```

Perform simulated maintenance.

Uncordon:

```bash
kubectl uncordon <node>
```

Verify new scheduling.

---

# Lab 50 – PodDisruptionBudget

Deploy multiple replicas.

Create a PDB.

Example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: web
```

Observe how voluntary disruptions are constrained.

---

# Lab 51 – Monitoring with Metrics Server

Check:

```bash
kubectl top nodes
```

and:

```bash
kubectl top pods -A
```

If unavailable, install Metrics Server according to your local cluster distribution's documented procedure.

---

# Lab 52 – Prometheus Installation

Install Prometheus using Helm or a Kubernetes monitoring stack.

Typical flow:

```bash
helm repo add prometheus-community <repository>
helm repo update
```

Install the selected chart according to its documentation.

Verify:

```bash
kubectl get pods -A
```

---

# Lab 53 – Grafana

Deploy Grafana.

Expose it locally:

```bash
kubectl port-forward svc/<grafana-service> 3000:80
```

Open:

```text
http://localhost:3000
```

Configure Prometheus as a data source.

---

# Lab 54 – Create a Kubernetes Dashboard

Create dashboards for:

```text
Node CPU
Node Memory
Pod CPU
Pod Memory
Pod Restarts
Network Traffic
Application Requests
```

---

# Lab 55 – Alerting

Create an alert for:

```text
High CPU
```

or:

```text
Pod Restart Rate
```

Test the alert.

Observe:

```text
Prometheus
 ↓
Alert Rule
 ↓
Alertmanager
 ↓
Notification
```

---

# Lab 56 – Logging

Deploy an application that produces logs.

Use:

```bash
kubectl logs
```

Then design a centralized logging architecture:

```text
Pods
 ↓
Log Collector
 ↓
Log Storage
 ↓
Search / Dashboard
```

---

# Lab 57 – Helm

Create a Helm chart:

```bash
helm create myapp
```

Inspect:

```text
Chart.yaml
values.yaml
templates/
```

---

# Lab 58 – Helm Template

Render without installing:

```bash
helm template myapp ./myapp
```

Inspect generated Kubernetes manifests.

---

# Lab 59 – Helm Install

Install:

```bash
helm install myapp ./myapp
```

Check:

```bash
helm list
kubectl get all
```

---

# Lab 60 – Helm Upgrade and Rollback

Change:

```text
replicaCount
```

Upgrade:

```bash
helm upgrade myapp ./myapp
```

Check:

```bash
helm history myapp
```

Rollback:

```bash
helm rollback myapp <revision>
```

---

# Lab 61 – Kustomize

Create:

```text
base/
overlays/
```

Structure:

```text
base
├── deployment.yaml
├── service.yaml
└── kustomization.yaml

overlays
├── dev
└── production
```

Build:

```bash
kubectl kustomize overlays/dev
```

Apply:

```bash
kubectl apply -k overlays/dev
```

---

# Lab 62 – GitOps

Set up a Git repository containing:

```text
deployment.yaml
service.yaml
configmap.yaml
```

Configure a GitOps controller.

Workflow:

```text
Git Commit
    ↓
GitOps Controller
    ↓
Kubernetes
    ↓
Deployment
```

Change the replica count in Git and observe reconciliation.

---

# Lab 63 – GitOps Drift

Manually change the Deployment:

```bash
kubectl scale deployment web --replicas=1
```

Then restore the desired state in Git.

Observe the GitOps controller reconcile the cluster.

---

# Lab 64 – Operator Exploration

Find installed CRDs:

```bash
kubectl get crds
```

Choose an Operator-managed application.

Inspect:

```bash
kubectl get <custom-resource>
```

Understand:

```text
Custom Resource
 ↓
Controller
 ↓
Reconciliation
```

---

# Lab 65 – Service Mesh

Install a service mesh in a dedicated lab cluster.

Deploy:

```text
Frontend
Backend
```

Enable sidecar injection or the relevant data-plane mechanism.

Observe:

```text
Service Identity
mTLS
Traffic
Metrics
Tracing
```

---

# Lab 66 – mTLS

Verify that service-to-service communication uses mutual TLS according to the selected service mesh configuration.

Investigate:

```text
Identity
Certificates
Trust
Policy
```

---

# Lab 67 – Distributed Tracing

Deploy an application with OpenTelemetry instrumentation.

Trace:

```text
Frontend
 ↓
API
 ↓
Database
```

Identify:

```text
Latency
Errors
Slow Dependencies
```

---

# Lab 68 – Kubernetes API Security

Use:

```bash
kubectl auth can-i
```

to test multiple identities.

Questions:

1. Who can create Pods?
2. Who can read Secrets?
3. Who can delete Deployments?
4. Which namespace are permissions scoped to?

---

# Lab 69 – Secret Access Audit

Identify which ServiceAccounts can read Secrets.

Review:

```bash
kubectl get roles -A
kubectl get clusterroles
kubectl get rolebindings -A
kubectl get clusterrolebindings
```

Look for overly broad permissions.

---

# Lab 70 – Network Segmentation

Create namespaces:

```text
frontend
backend
database
```

Design:

```text
frontend → backend
backend → database
frontend ✕ database
```

Implement with NetworkPolicies.

---

# Lab 71 – Secure Database

Deploy a database workload with:

```text
Dedicated Namespace
Dedicated ServiceAccount
NetworkPolicy
Secret
PersistentVolumeClaim
Resource Requests
Resource Limits
Probes
```

Document the security model.

---

# Lab 72 – Multi-Tenant Namespace

Create:

```text
team-a
team-b
```

Implement:

```text
Separate namespaces
RBAC
ResourceQuota
LimitRange
NetworkPolicy
```

Test that:

```text
Team A cannot access Team B resources
```

---

# Lab 73 – ResourceQuota

Create:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-quota
spec:
  hard:
    requests.cpu: "2"
    requests.memory: 4Gi
    limits.cpu: "4"
    limits.memory: 8Gi
    pods: "10"
```

Apply:

```bash
kubectl apply -f quota.yaml
```

Attempt to exceed the quota.

---

# Lab 74 – LimitRange

Create namespace defaults:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: defaults
spec:
  limits:
    - type: Container
      default:
        cpu: "500m"
        memory: "512Mi"
      defaultRequest:
        cpu: "100m"
        memory: "128Mi"
```

Observe how containers without explicit resources receive defaults.

---

# Lab 75 – PriorityClass

Create:

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: critical-app
value: 100000
globalDefault: false
description: "Priority for critical application workloads"
```

Assign it to a Pod.

Study:

```text
Scheduling Priority
Preemption
```

---

# Lab 76 – Preemption

Create:

```text
Low Priority Pods
High Priority Pod
```

Constrain cluster capacity.

Observe whether the higher-priority Pod can trigger preemption.

Understand:

```text
Priority
+
Preemption
+
PodDisruptionBudget
```

---

# Lab 77 – Topology Spread Constraints

Deploy multiple replicas across nodes or zones.

Use:

```yaml
topologySpreadConstraints:
```

Goal:

```text
Replica Distribution
```

Observe:

```bash
kubectl get pods -o wide
```

---

# Lab 78 – StatefulSet

Deploy a StatefulSet with three replicas.

Expected names:

```text
app-0
app-1
app-2
```

Observe creation order and stable identities.

---

# Lab 79 – StatefulSet Storage

Attach a PVC template:

```yaml
volumeClaimTemplates:
```

Verify:

```bash
kubectl get pvc
```

Observe one storage claim per StatefulSet Pod.

---

# Lab 80 – DaemonSet

Deploy a node-level agent.

Example use case:

```text
Logging Agent
```

Verify:

```bash
kubectl get daemonset
kubectl get pods -o wide
```

Observe one Pod per eligible node.

---

# Lab 81 – Job

Create a Job:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-job
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: job
          image: busybox:1.36
          command:
            - sh
            - -c
            - echo "Job completed"
```

Check:

```bash
kubectl get jobs
```

---

# Lab 82 – CronJob

Create a CronJob that runs every minute.

Verify:

```bash
kubectl get cronjobs
kubectl get jobs
```

Inspect generated Pods.

---

# Lab 83 – Troubleshooting Challenge

Create a Deployment containing several intentional problems:

```text
Wrong Image
Wrong Service Selector
Missing ConfigMap
Failed Readiness Probe
Insufficient Resources
```

Your task:

```text
Identify all failures
Fix them
Verify application availability
Document root causes
```

---

# Lab 84 – Networking Troubleshooting Challenge

Build:

```text
Frontend
Backend
Database
```

Introduce:

```text
Wrong Service Port
Wrong Selector
NetworkPolicy
DNS Failure
```

Troubleshoot without recreating the entire cluster.

---

# Lab 85 – Storage Troubleshooting Challenge

Create a PVC with an incorrect StorageClass.

Observe:

```text
PVC Pending
```

Investigate:

```bash
kubectl describe pvc <name>
kubectl get storageclass
kubectl get events
```

Fix the configuration.

---

# Lab 86 – Scheduling Troubleshooting Challenge

Create a Pod with:

```text
Impossible nodeSelector
```

Observe:

```text
Pending
```

Use:

```bash
kubectl describe pod
```

Identify the scheduling constraint.

---

# Lab 87 – Security Troubleshooting Challenge

Create a Pod that requires:

```text
root
privileged mode
hostPath
```

Apply restricted Pod Security enforcement.

Observe admission failures.

Modify the workload to operate securely without unnecessary privileges.

---

# Lab 88 – RBAC Troubleshooting Challenge

Create a ServiceAccount with:

```text
get pods
```

Then attempt:

```text
delete pods
```

Expected:

```text
Forbidden
```

Use:

```bash
kubectl auth can-i
```

to prove why the request fails.

---

# Lab 89 – Production Simulation

Build a mini production application:

```text
                    Internet
                       │
                       ▼
                    Ingress
                       │
                ┌──────┴──────┐
                ▼             ▼
             Frontend       Backend
                              │
                              ▼
                           Database
```

Required:

```text
Deployment
Service
Ingress
ConfigMap
Secret
PVC
NetworkPolicy
RBAC
Resource Requests
Resource Limits
Probes
HPA
Monitoring
```

---

# Lab 90 – Production Failure Simulation

Intentionally introduce:

```text
Pod Crash
Image Pull Failure
DNS Failure
Service Selector Error
NetworkPolicy Error
PVC Failure
RBAC Failure
Node Failure
```

For each failure:

```text
Detect
Investigate
Fix
Validate
Document
```

---

# Lab 91 – Blue/Green Deployment

Deploy:

```text
v1
v2
```

Route traffic to:

```text
v1
```

Validate v2.

Then switch traffic:

```text
v1 → v2
```

Rollback:

```text
v2 → v1
```

Understand:

```text
Fast Rollback
Traffic Switching
Release Validation
```

---

# Lab 92 – Canary Deployment

Deploy:

```text
v1 → 90%
v2 → 10%
```

Observe:

```text
Traffic
Errors
Latency
```

Increase:

```text
10%
→ 25%
→ 50%
→ 100%
```

Stop rollout if metrics degrade.

---

# Lab 93 – Zero-Downtime Deployment

Configure:

```text
Multiple Replicas
Readiness Probe
RollingUpdate
PodDisruptionBudget
Resource Requests
```

Perform a Deployment update.

Verify that application availability is maintained during the rollout.

---

# Lab 94 – Backup and Restore Exercise

Create critical resources:

```text
Deployment
Service
ConfigMap
Secret
PVC
```

Back them up using an appropriate backup mechanism.

Delete the test namespace.

Restore it.

Validate:

```text
Application
Configuration
Storage
Networking
```

---

# Lab 95 – Disaster Recovery Exercise

Simulate:

```text
Cluster Loss
```

Recovery workflow:

```text
Provision Cluster
 ↓
Restore Configuration
 ↓
Restore Secrets
 ↓
Restore Applications
 ↓
Restore Persistent Data
 ↓
Validate
```

Measure:

```text
RTO
RPO
```

---

# Lab 96 – RTO and RPO

## RTO

Recovery Time Objective:

```text
How quickly must service be restored?
```

## RPO

Recovery Point Objective:

```text
How much data loss is acceptable?
```

Example:

```text
RTO = 1 hour
RPO = 15 minutes
```

---

# Lab 97 – Cluster Upgrade Simulation

Using a disposable test cluster:

```text
Current Version
      ↓
Backup
      ↓
Compatibility Check
      ↓
Upgrade
      ↓
Validation
```

Verify:

```text
Nodes
Pods
Services
Storage
Networking
Applications
```

---

# Lab 98 – Security Assessment Lab

Perform an authorized Kubernetes security assessment.

Review:

```text
RBAC
ServiceAccounts
Secrets
NetworkPolicies
Pod Security
Container Privileges
Host Mounts
Image Vulnerabilities
Admission Controls
Audit Configuration
```

Document:

```text
Finding
Severity
Evidence
Impact
Recommendation
```

---

# Lab 99 – Kubernetes Forensics Lab

Simulate a compromised Pod.

Collect:

```text
Pod metadata
Container logs
Events
ServiceAccount information
RBAC bindings
Network information
Kubernetes audit logs
Node-level evidence where authorized
```

Create a timeline:

```text
Initial Activity
      ↓
Privilege Attempt
      ↓
Network Activity
      ↓
Detection
      ↓
Containment
```

---

# Lab 100 – Final Kubernetes Capstone

## Objective

Build and operate a production-style Kubernetes application from beginning to end.

---

## Architecture

```text
                         Users
                           │
                           ▼
                    Ingress / Gateway
                           │
                           ▼
                     Frontend Service
                           │
                           ▼
                    Frontend Deployment
                           │
                           ▼
                      Backend Service
                           │
                           ▼
                    Backend Deployment
                           │
                           ▼
                    Database Service
                           │
                           ▼
                    Stateful Database
                           │
                           ▼
                       Persistent
                         Storage
```

---

## Required Features

### Workloads

```text
Deployment
StatefulSet
```

### Networking

```text
Service
Ingress / Gateway
NetworkPolicy
CoreDNS
```

### Configuration

```text
ConfigMap
Secret
```

### Storage

```text
PVC
StorageClass
CSI
```

### Scheduling

```text
Affinity
Anti-Affinity
Taints
Tolerations
Topology
```

### Security

```text
RBAC
ServiceAccounts
Pod Security
NetworkPolicy
Image Security
```

### Resources

```text
Requests
Limits
ResourceQuota
LimitRange
```

### Reliability

```text
Readiness
Liveness
Startup
PodDisruptionBudget
HPA
```

### Observability

```text
Metrics
Logs
Traces
Alerts
Dashboards
```

---

# Capstone Phase 1 – Application Deployment

Deploy:

```text
Frontend
Backend
Database
```

Verify:

```bash
kubectl get pods -A
```

---

# Capstone Phase 2 – Networking

Configure:

```text
Frontend Service
Backend Service
Database Service
Ingress
```

Test:

```text
Internet → Frontend
Frontend → Backend
Backend → Database
```

---

# Capstone Phase 3 – Security

Implement:

```text
RBAC
Dedicated ServiceAccounts
NetworkPolicy
Restricted Pod Security
Non-root Containers
Dropped Capabilities
```

---

# Capstone Phase 4 – Storage

Configure:

```text
StorageClass
PVC
Database Storage
```

Verify:

```bash
kubectl get pv
kubectl get pvc
```

---

# Capstone Phase 5 – Scheduling

Implement:

```text
Node Affinity
Pod Anti-Affinity
Topology Spread
Taints
Tolerations
```

Verify:

```bash
kubectl get pods -o wide
```

---

# Capstone Phase 6 – Scaling

Configure:

```text
Resource Requests
HPA
```

Generate traffic.

Observe:

```bash
kubectl get hpa
kubectl get pods
```

---

# Capstone Phase 7 – Observability

Deploy:

```text
Prometheus
Grafana
Alertmanager
OpenTelemetry
```

Monitor:

```text
CPU
Memory
Requests
Latency
Errors
Restarts
```

---

# Capstone Phase 8 – Failure Testing

Introduce:

```text
Pod Failure
Node Failure
Image Failure
Network Failure
Storage Failure
RBAC Failure
DNS Failure
```

Measure:

```text
Detection Time
Recovery Time
User Impact
```

---

# Capstone Phase 9 – Disaster Recovery

Delete the application namespace.

Restore:

```text
Configuration
Applications
Secrets
Storage
Networking
```

Measure:

```text
RTO
RPO
```

---

# Capstone Phase 10 – Documentation

Document:

```text
Architecture
Deployment
Security
Networking
Storage
Monitoring
Backup
Recovery
Troubleshooting
Known Risks
```

---

# Lab Completion Checklist

## Fundamentals

```text
☐ Cluster
☐ Pod
☐ Deployment
☐ ReplicaSet
☐ StatefulSet
☐ DaemonSet
☐ Job
☐ CronJob
```

## Networking

```text
☐ Service
☐ NodePort
☐ LoadBalancer
☐ Ingress
☐ Gateway API
☐ DNS
☐ CNI
☐ NetworkPolicy
```

## Storage

```text
☐ Volume
☐ PV
☐ PVC
☐ StorageClass
☐ Dynamic Provisioning
☐ CSI
```

## Scheduling

```text
☐ Scheduler
☐ NodeSelector
☐ Node Affinity
☐ Pod Affinity
☐ Pod Anti-Affinity
☐ Taints
☐ Tolerations
☐ PriorityClass
☐ Topology Spread
```

## Security

```text
☐ Authentication
☐ RBAC
☐ ServiceAccounts
☐ Admission
☐ Pod Security
☐ NetworkPolicy
☐ Secrets
☐ Image Security
☐ Runtime Security
```

## Observability

```text
☐ Logging
☐ Metrics
☐ Metrics Server
☐ Prometheus
☐ Grafana
☐ Alertmanager
☐ OpenTelemetry
☐ Distributed Tracing
```

## Operations

```text
☐ Backup
☐ Restore
☐ Upgrade
☐ HA
☐ DR
☐ Maintenance
☐ Optimization
```

## Advanced

```text
☐ Helm
☐ Kustomize
☐ GitOps
☐ Operators
☐ Service Mesh
☐ CI/CD
```

---

# Practical Skill Levels

## Level 1 – Beginner

You can:

```text
Create Pods
Create Deployments
Create Services
Read Logs
Scale Workloads
```

---

## Level 2 – Intermediate

You can:

```text
Configure Networking
Configure Storage
Configure Scheduling
Use ConfigMaps
Use Secrets
Configure HPA
Implement RBAC
```

---

## Level 3 – Advanced

You can:

```text
Design HA Clusters
Implement Network Security
Troubleshoot Complex Failures
Implement Observability
Perform Upgrades
Design DR
```

---

## Level 4 – Production

You can:

```text
Operate Kubernetes Reliably
Secure Workloads
Automate Deployments
Manage Incidents
Perform Root Cause Analysis
Optimize Resources
Recover From Failures
```

---

# Final Practical Challenge

Without referring to documentation, build the following:

```text
3-node Kubernetes cluster

        │
        ▼
     Ingress
        │
        ▼
   Frontend × 3
        │
        ▼
   Backend × 3
        │
        ▼
   Database × 3
        │
        ▼
 Persistent Storage
```

Implement:

```text
RBAC
NetworkPolicy
Secrets
ConfigMaps
Probes
Requests
Limits
HPA
PDB
Affinity
Anti-Affinity
Topology Spread
Monitoring
Logging
Alerting
Backup
Recovery
```

Then intentionally break:

```text
DNS
Service
Pod
Node
Storage
RBAC
NetworkPolicy
Image
```

and recover each component without rebuilding the entire cluster.

---

# Final Takeaways

The fastest way to learn Kubernetes is:

```text
Learn
 ↓
Build
 ↓
Break
 ↓
Troubleshoot
 ↓
Secure
 ↓
Automate
 ↓
Repeat
```

Do not limit practice to successful deployments.

Production engineers must be comfortable with failure:

```text
Pod Failure
Node Failure
Network Failure
DNS Failure
Storage Failure
Authentication Failure
Authorization Failure
Configuration Failure
Application Failure
Control Plane Failure
```

A strong Kubernetes engineer should be able to move from:

```text
"What is Kubernetes?"
```

to:

```text
"Why is this workload failing,
what component is responsible,
how do I prove the root cause,
how do I fix it safely,
and how do I prevent it from happening again?"
```

That transition from **theoretical knowledge to systematic troubleshooting** is the primary goal of these hands-on labs.

---

# Next Chapter

## Chapter 87 – Real-World Case Studies

The next chapter will cover practical Kubernetes scenarios based on production-style environments, including:

- E-commerce Platform
- Banking Platform
- SaaS Application
- Microservices Platform
- Multi-Tenant Kubernetes
- High-Traffic Web Application
- Kubernetes Security Incident
- Container Escape Scenario
- Supply Chain Attack Scenario
- Database Failure
- Node Failure
- DNS Outage
- NetworkPolicy Incident
- Storage Failure
- API Server Failure
- etcd Failure
- Cluster Upgrade Failure
- Disaster Recovery
- Zero-Downtime Deployment
- Blue/Green Deployment
- Canary Deployment
- GitOps Incident
- Service Mesh Incident
- Observability Incident
- Complete Production Architecture Case Study