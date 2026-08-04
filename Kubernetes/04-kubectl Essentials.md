# Chapter 4 – kubectl Essentials

## Overview

**kubectl** is the official command-line interface (CLI) for Kubernetes. It allows users to interact with a Kubernetes cluster by communicating with the Kubernetes API Server.

Almost every Kubernetes task—including deploying applications, viewing cluster resources, troubleshooting issues, scaling workloads, and debugging Pods—is performed using `kubectl`.

Whether you are a Developer, DevOps Engineer, Platform Engineer, SRE, or Security Engineer, `kubectl` is the primary tool used for daily Kubernetes operations.

---

# Learning Objectives

After completing this chapter, you will understand:

- What kubectl is
- How kubectl works
- kubectl architecture
- kubectl syntax
- Resource management
- kubeconfig
- Contexts
- Namespaces
- Output formats
- Essential kubectl commands

---

# What is kubectl?

kubectl is the Kubernetes command-line client.

It allows you to:

- Deploy applications
- Manage resources
- View cluster information
- Debug workloads
- Monitor cluster state
- Update applications
- Delete resources

Everything ultimately communicates through the Kubernetes API Server.

---

# kubectl Architecture

```
User

↓

kubectl

↓

API Server

↓

Kubernetes Cluster
```

kubectl never communicates directly with Worker Nodes.

Every request goes through the API Server.

---

# kubectl Request Flow

Example:

```bash
kubectl get pods
```

Workflow:

```
kubectl

↓

API Server

↓

Authentication

↓

Authorization

↓

Retrieve Data

↓

Return Results
```

---

# kubectl Syntax

General syntax:

```bash
kubectl <command> <resource> [name] [flags]
```

Examples:

```bash
kubectl get pods

kubectl describe pod nginx

kubectl delete deployment app
```

---

# Common kubectl Commands

| Command | Purpose |
|----------|----------|
| get | Display resources |
| describe | Show detailed information |
| create | Create resources |
| apply | Apply declarative configuration |
| delete | Remove resources |
| edit | Edit resources |
| logs | View logs |
| exec | Execute commands in containers |
| scale | Scale workloads |
| rollout | Manage deployments |
| explain | Display API documentation |

---

# Understanding Resources

Everything in Kubernetes is represented as an API object.

Examples:

```
Pods

Deployments

ReplicaSets

Services

Namespaces

Nodes

Secrets

ConfigMaps

PersistentVolumes
```

kubectl manages these resources.

---

# The get Command

Display Pods:

```bash
kubectl get pods
```

Display Deployments:

```bash
kubectl get deployments
```

Display Nodes:

```bash
kubectl get nodes
```

Display Services:

```bash
kubectl get services
```

Display everything in a namespace:

```bash
kubectl get all
```

---

# Viewing All Namespaces

```bash
kubectl get pods -A
```

or

```bash
kubectl get pods --all-namespaces
```

Useful for administrators managing the entire cluster.

---

# Describe Command

Provides detailed information.

Example:

```bash
kubectl describe pod nginx
```

Information includes:

- Status
- Events
- Node
- Labels
- Containers
- Conditions
- Volumes

---

# Create Resources

Imperative creation:

```bash
kubectl create deployment nginx \
--image=nginx
```

Service:

```bash
kubectl expose deployment nginx \
--port=80
```

---

# Declarative Management

Preferred approach:

```bash
kubectl apply -f deployment.yaml
```

Workflow:

```
YAML

↓

kubectl apply

↓

API Server

↓

Deployment
```

Declarative management supports version control and automation.

---

# Delete Resources

Delete Pod:

```bash
kubectl delete pod nginx
```

Delete Deployment:

```bash
kubectl delete deployment nginx
```

Delete manifest:

```bash
kubectl delete -f deployment.yaml
```

---

# Viewing Logs

View logs:

```bash
kubectl logs pod-name
```

Stream logs:

```bash
kubectl logs -f pod-name
```

Specify container:

```bash
kubectl logs pod-name \
-c container-name
```

---

# Executing Commands Inside Pods

Open a shell:

```bash
kubectl exec -it pod-name \
-- /bin/bash
```

If Bash is unavailable:

```bash
kubectl exec -it pod-name \
-- /bin/sh
```

Execute a single command:

```bash
kubectl exec pod-name \
-- ls /
```

---

# Port Forwarding

Forward local port:

```bash
kubectl port-forward pod-name \
8080:80
```

Workflow:

```
Laptop

↓

kubectl

↓

Pod
```

Useful for debugging applications without exposing them externally.

---

# Copy Files

Copy from Pod:

```bash
kubectl cp pod-name:/tmp/file .
```

Copy to Pod:

```bash
kubectl cp local.txt pod-name:/tmp/
```

---

# Scaling Applications

Scale Deployment:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Workflow:

```
Deployment

↓

5 Replicas

↓

Scheduler

↓

5 Pods
```

---

# Rolling Updates

View rollout status:

```bash
kubectl rollout status deployment nginx
```

History:

```bash
kubectl rollout history deployment nginx
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

---

# Viewing Events

Display cluster events:

```bash
kubectl get events
```

All namespaces:

```bash
kubectl get events -A
```

Events are invaluable for troubleshooting.

---

# kubectl explain

Display API documentation.

Example:

```bash
kubectl explain deployment
```

Nested fields:

```bash
kubectl explain deployment.spec
```

This command is useful when writing YAML manifests.

---

# kubeconfig

kubectl stores cluster connection details in:

```
kubeconfig
```

View:

```bash
kubectl config view
```

Current context:

```bash
kubectl config current-context
```

Contexts:

```bash
kubectl config get-contexts
```

Switch context:

```bash
kubectl config use-context <context-name>
```

---

# Namespaces

View:

```bash
kubectl get namespaces
```

Use namespace:

```bash
kubectl get pods \
-n production
```

Default namespace:

```
default
```

Namespaces provide logical isolation within a cluster.

---

# Output Formats

Default:

```bash
kubectl get pods
```

Wide output:

```bash
kubectl get pods -o wide
```

YAML:

```bash
kubectl get pod nginx \
-o yaml
```

JSON:

```bash
kubectl get pod nginx \
-o json
```

Name only:

```bash
kubectl get pods \
-o name
```

---

# Label Selectors

Pods with label:

```bash
kubectl get pods \
-l app=frontend
```

Multiple labels:

```bash
kubectl get pods \
-l app=frontend,tier=web
```

---

# Watching Resources

Continuously monitor:

```bash
kubectl get pods -w
```

Useful for observing deployments and Pod state transitions.

---

# kubectl Workflow

```
Developer

↓

kubectl

↓

API Server

↓

Cluster

↓

Response
```

---

# Most Frequently Used Commands

```bash
kubectl get pods

kubectl get nodes

kubectl get deployments

kubectl describe pod

kubectl logs

kubectl exec

kubectl apply

kubectl delete

kubectl scale

kubectl rollout

kubectl get events

kubectl config view
```

---

# Best Practices

### 1. Prefer Declarative Management

Use:

```bash
kubectl apply -f
```

instead of repeatedly creating resources imperatively.

---

### 2. Store YAML in Git

Treat Kubernetes manifests as Infrastructure as Code.

---

### 3. Learn get, describe, logs, and events First

These four commands solve a large percentage of day-to-day troubleshooting tasks.

---

### 4. Use Contexts Carefully

Always verify the current context before applying changes to avoid modifying the wrong cluster.

---

### 5. Use Namespaces

Separate:

- Development
- Testing
- Staging
- Production

to improve organization and reduce operational risk.

---

## How kubectl Works Internally

Although `kubectl` appears to be a simple command-line tool, every command triggers a series of interactions with the Kubernetes Control Plane.

Understanding this workflow helps explain:

- Why certain commands fail
- How authentication works
- How authorization is enforced
- How Kubernetes processes requests
- How resources are created and updated

---

# High-Level kubectl Workflow

Suppose a user executes:

```bash
kubectl get pods
```

The complete workflow is:

```
User

↓

kubectl

↓

Read kubeconfig

↓

API Server

↓

Authentication

↓

Authorization

↓

Retrieve Resource

↓

Return Response

↓

Display Output
```

Everything flows through the Kubernetes API Server.

---

# Step 1 – Read kubeconfig

Before contacting the cluster, `kubectl` reads the **kubeconfig** file.

The kubeconfig contains:

- Cluster information
- User credentials
- Contexts
- API Server address

Workflow:

```
kubectl

↓

kubeconfig

↓

Cluster Information
```

View configuration:

```bash
kubectl config view
```

---

# Step 2 – Select Context

A kubeconfig may contain multiple clusters.

Example:

```
Development

Testing

Production
```

Current context:

```bash
kubectl config current-context
```

Switch context:

```bash
kubectl config use-context production
```

The selected context determines which cluster receives the request.

---

# Step 3 – Connect to API Server

```
kubectl

↓

HTTPS Request

↓

API Server
```

All communication uses the Kubernetes REST API.

No request goes directly to Worker Nodes.

---

# Step 4 – Authentication

The API Server verifies the client's identity.

Possible authentication methods include:

```
Client Certificate

Bearer Token

OIDC

Service Account

External Identity Provider
```

If authentication fails:

```
401 Unauthorized
```

---

# Step 5 – Authorization

Once authenticated:

```
Can this identity perform this action?
```

Most production clusters use **Role-Based Access Control (RBAC)**.

Example:

```
Developer

↓

View Pods

✓ Allowed

↓

Delete Nodes

✗ Denied
```

If authorization fails:

```
403 Forbidden
```

---

# Step 6 – Admission Controllers

Admission Controllers perform additional checks.

Example:

```
Deployment

↓

Policy Validation

↓

Approved
```

Possible actions:

- Validate requests
- Mutate objects
- Reject requests
- Apply defaults

---

# Step 7 – API Processing

The API Server processes the request.

Examples:

```
GET

↓

Retrieve Object
```

```
CREATE

↓

Store Object
```

```
DELETE

↓

Remove Object
```

---

# Step 8 – etcd

If the request changes cluster state:

```
API Server

↓

etcd
```

Examples:

- New Deployment
- New Service
- Updated ConfigMap
- Deleted Pod

Read-only requests retrieve information from the current cluster state without modifying it.

---

# Step 9 – Controllers React

Suppose:

```bash
kubectl apply -f deployment.yaml
```

Controller detects:

```
Deployment

↓

ReplicaSet

↓

Pods Needed
```

The Controller Manager begins reconciliation.

---

# Step 10 – Scheduler

Pods initially remain:

```
Pending
```

Scheduler workflow:

```
Pending Pod

↓

Available Nodes

↓

Scheduling Decision

↓

Node Assigned
```

---

# Step 11 – kubelet

Worker Node:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Start Pod
```

The kubelet ensures the assigned Pod is created and maintained.

---

# Step 12 – Status Returned

The kubelet reports:

```
Pod Running

↓

API Server

↓

kubectl Displays Result
```

Example:

```bash
kubectl get pods
```

Output:

```
Running
```

---

# Internal Request Flow

```
User

↓

kubectl

↓

kubeconfig

↓

API Server

↓

Authentication

↓

Authorization

↓

Admission Controllers

↓

etcd

↓

Controllers

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Container Runtime

↓

Pod

↓

Status Back to API Server

↓

kubectl
```

This is the complete lifecycle for many Kubernetes operations.

---

# Imperative vs Declarative Commands

## Imperative

Example:

```bash
kubectl create deployment nginx \
--image=nginx
```

Workflow:

```
Command

↓

API Server

↓

Deployment Created
```

---

## Declarative

Example:

```bash
kubectl apply -f deployment.yaml
```

Workflow:

```
YAML

↓

Desired State

↓

API Server

↓

Reconciliation

↓

Deployment
```

Declarative workflows are preferred for production because they support:

- Version control
- Auditing
- CI/CD
- Repeatability

---

# Resource Discovery

View available resource types:

```bash
kubectl api-resources
```

View supported API versions:

```bash
kubectl api-versions
```

These commands help explore cluster capabilities.

---

# Advanced Output Options

Wide output:

```bash
kubectl get pods -o wide
```

YAML:

```bash
kubectl get deployment nginx -o yaml
```

JSON:

```bash
kubectl get deployment nginx -o json
```

Custom columns:

```bash
kubectl get pods \
-o custom-columns=NAME:.metadata.name,STATUS:.status.phase
```

JSONPath:

```bash
kubectl get pods \
-o jsonpath='{.items[*].metadata.name}'
```

These formats are useful for scripting and automation.

---

# Dry Run

Preview resource creation:

```bash
kubectl create deployment nginx \
--image=nginx \
--dry-run=client -o yaml
```

Benefits:

- Validate commands
- Generate manifests
- Avoid unintended changes

---

# Explain API Objects

Example:

```bash
kubectl explain pod
```

Nested fields:

```bash
kubectl explain deployment.spec.template
```

Useful when writing YAML without referencing documentation.

---

# Useful Debugging Commands

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

Logs:

```bash
kubectl logs <pod-name>
```

Events:

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

Watch resources:

```bash
kubectl get pods -w
```

These commands are often the first tools used during troubleshooting.

---

# Hands-on Exercise

## Create a Deployment

```bash
kubectl create deployment nginx \
--image=nginx
```

---

## Verify

```bash
kubectl get deployments

kubectl get pods
```

---

## Inspect

```bash
kubectl describe deployment nginx
```

---

## View YAML

```bash
kubectl get deployment nginx \
-o yaml
```

---

## Delete

```bash
kubectl delete deployment nginx
```

---

# Best Practices

### 1. Use Declarative Workflows

Store manifests in Git and use:

```bash
kubectl apply -f
```

for deployments.

---

### 2. Learn Resource Discovery Commands

`kubectl api-resources` and `kubectl explain` are invaluable when learning Kubernetes APIs.

---

### 3. Always Check Context

Before running commands:

```bash
kubectl config current-context
```

to avoid modifying the wrong cluster.

---

### 4. Use Output Formats for Automation

Prefer JSON or YAML when integrating with scripts or CI/CD pipelines.

---

### 5. Investigate Before Changing

When troubleshooting:

1. `kubectl get`
2. `kubectl describe`
3. `kubectl logs`
4. `kubectl get events`

Collect evidence before making changes.

---

