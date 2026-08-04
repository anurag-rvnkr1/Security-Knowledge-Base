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

## Next Section

How kubectl Works Internally

Advanced kubectl Features

Common Mistakes

Quick Revision

References

---