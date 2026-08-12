# Chapter 80 – Helm

## Overview

Helm is a package manager and application management tool for Kubernetes.

It allows Kubernetes applications to be packaged, configured, installed, upgraded, and rolled back using reusable **Charts**.

Without Helm, a complex application may require many Kubernetes manifests:

```text
Deployment
Service
ConfigMap
Secret
Ingress
ServiceAccount
ConfigMap
HorizontalPodAutoscaler
NetworkPolicy
```

Managing all these manifests independently can become difficult.

Helm provides a structured packaging and templating system:

```text
Helm Chart
    ↓
Templates + Values
    ↓
Rendered Kubernetes Manifests
    ↓
Kubernetes
```

A simplified Helm workflow is:

```text
Create Chart
    ↓
Define Templates
    ↓
Define Values
    ↓
Render
    ↓
Validate
    ↓
Install
    ↓
Upgrade
    ↓
Monitor
    ↓
Rollback if Required
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Helm fundamentals
- What Helm is
- Why Helm is used
- Helm architecture
- Helm CLI
- Helm charts
- Chart structure
- `Chart.yaml`
- `values.yaml`
- `templates/`
- `templates/_helpers.tpl`
- `charts/`
- `crds/`
- README
- LICENSE
- Helm releases
- Helm repositories
- Helm registries
- Helm installation
- Helm upgrade
- Helm rollback
- Helm uninstall
- Helm history
- Helm status
- Helm list
- Helm values
- Default values
- Custom values
- Value precedence
- Helm templates
- Go templates
- Template functions
- Pipelines
- Conditionals
- Loops
- Variables
- Named templates
- Helpers
- `include`
- `required`
- `default`
- `lookup`
- `tpl`
- `toYaml`
- `nindent`
- `with`
- `range`
- `if`
- Chart dependencies
- Subcharts
- Library charts
- Helm hooks
- Helm tests
- Helm upgrade strategies
- Helm rollbacks
- Helm secrets
- Helm security
- OCI registries
- Chart signing
- Provenance
- Helm lint
- Helm template
- Helm diff
- Helm with Kubernetes
- Helm with GitOps
- Helm with Argo CD
- Helm with Flux
- Helm with CI/CD
- Environment management
- Production Helm
- Helm best practices
- Common mistakes
- Hands-on labs
- Quick revision
- Interview questions

---

# What Is Helm?

Helm is a tool for managing Kubernetes applications.

It packages Kubernetes resources into reusable units called:

```text
Charts
```

A Chart contains:

```text
Templates
+
Default Configuration
+
Metadata
+
Dependencies
```

---

# Why Helm?

Without Helm:

```text
deployment.yaml
service.yaml
configmap.yaml
ingress.yaml
serviceaccount.yaml
hpa.yaml
networkpolicy.yaml
```

With Helm:

```text
my-application/
└── Chart
```

Helm can generate the required Kubernetes resources from templates.

---

# Helm Architecture

Conceptually:

```text
                 Helm CLI
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Chart      Values    Release
          │         │
          └────┬────┘
               ▼
          Template Engine
               │
               ▼
      Kubernetes Manifests
               │
               ▼
          Kubernetes API
```

---

# Helm Components

Important Helm concepts include:

```text
Helm CLI
Chart
Repository
Registry
Release
Values
Templates
Dependencies
Hooks
```

---

# Helm Chart

A Chart is a package containing Kubernetes application definitions.

Example:

```text
api-chart/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── _helpers.tpl
└── charts/
```

---

# Chart Structure

A typical Chart:

```text
mychart/
├── Chart.yaml
├── values.yaml
├── charts/
├── crds/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   ├── ingress.yaml
│   ├── serviceaccount.yaml
│   ├── _helpers.tpl
│   └── NOTES.txt
├── README.md
└── LICENSE
```

---

# Chart.yaml

`Chart.yaml` contains Chart metadata.

Example:

```yaml
apiVersion: v2
name: api
description: A Helm chart for a Kubernetes API
type: application
version: 1.0.0
appVersion: "2.4.0"
```

---

# Chart Version

The:

```yaml
version: 1.0.0
```

represents the version of the Helm Chart itself.

---

# App Version

The:

```yaml
appVersion: "2.4.0"
```

usually represents the version of the application packaged by the Chart.

These are different concepts.

---

# `values.yaml`

`values.yaml` contains default configuration values.

Example:

```yaml
replicaCount: 2

image:
  repository: nginx
  tag: "1.27"

service:
  type: ClusterIP
  port: 80
```

---

# Templates

Templates contain Kubernetes manifests with dynamic values.

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "api.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
```

---

# Helm Template Engine

Helm uses Go template syntax.

Example:

```yaml
replicas: {{ .Values.replicaCount }}
```

If:

```yaml
replicaCount: 3
```

the rendered manifest becomes:

```yaml
replicas: 3
```

---

# Helm Rendering

The process is:

```text
values.yaml
     +
Template
     ↓
Helm
     ↓
Rendered YAML
     ↓
Kubernetes
```

---

# Helm Release

A release is an installed instance of a Helm Chart.

Example:

```text
Chart:
api

Release:
production-api
```

The same Chart can have multiple releases:

```text
dev-api
staging-api
production-api
```

---

# Multiple Releases

```text
                Helm Chart
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Dev API     Staging API   Prod API
```

Each release can use different values.

---

# Helm Repository

A Helm repository stores Charts.

Conceptually:

```text
Chart
 ↓
Package
 ↓
Repository
 ↓
helm install
```

---

# Helm Registry

Modern Helm workflows can also use OCI-compatible registries.

Conceptually:

```text
Helm Chart
    ↓
OCI Registry
    ↓
Helm
```

---

# Installing Helm

After installing Helm, verify:

```bash
helm version
```

---

# Helm Help

```bash
helm help
```

---

# Helm Commands

Important commands:

```text
helm create
helm lint
helm template
helm install
helm upgrade
helm rollback
helm uninstall
helm list
helm status
helm history
helm repo
helm dependency
helm package
helm pull
helm test
```

---

# Create a Chart

Create a new Chart:

```bash
helm create mychart
```

This generates a starter structure.

---

# List Chart Files

```bash
tree mychart
```

or inspect the directory manually.

---

# Helm Lint

Validate Chart structure:

```bash
helm lint ./mychart
```

---

# Why Use `helm lint`?

It can identify common Chart problems before installation.

Examples:

```text
Invalid Templates
Incorrect Metadata
Potential Configuration Errors
```

---

# Helm Template

Render the Chart locally:

```bash
helm template myrelease ./mychart
```

This displays the generated Kubernetes manifests without installing them.

---

# Debug Rendering

Use:

```bash
helm template myrelease ./mychart --debug
```

Useful for troubleshooting template rendering.

---

# Helm Install

Install a Chart:

```bash
helm install myrelease ./mychart
```

---

# Specify Namespace

```bash
helm install myrelease ./mychart \
  --namespace production \
  --create-namespace
```

---

# Set Values During Installation

Example:

```bash
helm install myrelease ./mychart \
  --set replicaCount=3
```

---

# Values File

Create:

```text
production-values.yaml
```

Then:

```bash
helm install myrelease ./mychart \
  -f production-values.yaml
```

---

# Multiple Values Files

Helm allows multiple values files.

Example:

```bash
helm install myrelease ./mychart \
  -f values.yaml \
  -f production-values.yaml
```

Later values generally override earlier values where keys overlap.

---

# Value Precedence

A simplified model is:

```text
Chart Defaults
      ↓
Values Files
      ↓
Later Values Files
      ↓
--set
```

More specific overrides generally take precedence over less specific defaults.

Always verify the final rendered configuration rather than relying on memory of precedence rules.

---

# Helm Upgrade

Upgrade an existing release:

```bash
helm upgrade myrelease ./mychart
```

---

# Install or Upgrade

Use:

```bash
helm upgrade --install myrelease ./mychart
```

This is useful in automation because it handles both cases.

---

# Helm Status

```bash
helm status myrelease
```

Provides release information and status.

---

# Helm List

List releases:

```bash
helm list
```

All namespaces:

```bash
helm list -A
```

---

# Helm History

View release revisions:

```bash
helm history myrelease
```

Example conceptual history:

```text
REVISION   STATUS
1          deployed
2          superseded
3          deployed
```

---

# Helm Rollback

Rollback to a previous revision:

```bash
helm rollback myrelease 1
```

---

# Helm Uninstall

Remove a release:

```bash
helm uninstall myrelease
```

Be careful when uninstalling production workloads.

---

# Helm Get

Inspect release information:

```bash
helm get all myrelease
```

Other useful commands:

```bash
helm get values myrelease
helm get manifest myrelease
helm get hooks myrelease
```

---

# Helm Values

Retrieve configured values:

```bash
helm get values myrelease
```

Retrieve all values including defaults:

```bash
helm get values myrelease --all
```

---

# Basic Template Variables

Example:

```yaml
{{ .Values.replicaCount }}
```

This accesses:

```text
values.yaml
```

---

# The Dot (`.`)

In Helm templates, `.` represents the current template context.

Example:

```yaml
{{ .Values.image.repository }}
```

---

# Built-In Objects

Common Helm objects include:

```text
.Values
.Release
.Chart
.Capabilities
.Files
.Template
```

---

# `.Values`

Access Chart values.

Example:

```yaml
{{ .Values.service.port }}
```

---

# `.Release`

Provides information about the current release.

Example:

```yaml
{{ .Release.Name }}
```

---

# `.Chart`

Provides Chart metadata.

Example:

```yaml
{{ .Chart.Name }}
```

---

# `.Capabilities`

Provides information about Kubernetes capabilities available during rendering.

Example:

```yaml
{{ .Capabilities.KubeVersion.Version }}
```

---

# `.Files`

Provides access to files packaged within the Chart, subject to Helm's Chart file rules.

---

# `.Template`

Provides information about the current template.

---

# Template Functions

Helm provides many template functions.

Examples:

```text
default
required
quote
upper
lower
toYaml
nindent
include
tpl
lookup
```

---

# `default`

Provides a fallback value.

Example:

```yaml
replicas: {{ default 1 .Values.replicaCount }}
```

If `replicaCount` is empty or unset, the default may be used according to Helm template semantics.

---

# `required`

Require a value.

Example:

```yaml
host: {{ required "host is required" .Values.ingress.host }}
```

If the value is missing, template rendering fails.

---

# `quote`

Example:

```yaml
value: {{ .Values.environment | quote }}
```

---

# Pipelines

Functions can be chained using pipelines.

Example:

```yaml
{{ .Values.environment | quote }}
```

Conceptually:

```text
Value
 ↓
Function
 ↓
Output
```

---

# `toYaml`

Convert structured values into YAML.

Example:

```yaml
resources:
{{ toYaml .Values.resources | nindent 2 }}
```

---

# `nindent`

Adds indentation and a newline.

Example:

```yaml
{{ toYaml .Values.resources | nindent 12 }}
```

---

# `include`

Render a named template.

Example:

```yaml
name: {{ include "api.fullname" . }}
```

---

# Named Templates

Named templates are often stored in:

```text
templates/_helpers.tpl
```

Example:

```gotemplate
{{- define "api.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
```

---

# `_helpers.tpl`

Helpers reduce repeated template logic.

Typical helpers include:

```text
Name
Full Name
Labels
Selector Labels
Service Account Name
```

---

# Standard Labels

A helper can generate:

```yaml
labels:
  app.kubernetes.io/name: ...
  app.kubernetes.io/instance: ...
  app.kubernetes.io/version: ...
```

Consistent labels improve:

```text
Operations
Monitoring
Selection
Troubleshooting
```

---

# `if`

Conditionals:

```gotemplate
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
...
{{- end }}
```

---

# `else`

Example:

```gotemplate
{{- if .Values.enabled }}
enabled
{{- else }}
disabled
{{- end }}
```

---

# `with`

`with` changes the current context.

Example:

```gotemplate
{{- with .Values.ingress }}
host: {{ .host }}
{{- end }}
```

---

# `range`

Used for iteration.

Example:

```gotemplate
{{- range .Values.hosts }}
- {{ . }}
{{- end }}
```

---

# Variables

Template variables can be created using:

```gotemplate
{{- $name := .Release.Name }}
```

Then:

```gotemplate
{{ $name }}
```

---

# `tpl`

`tpl` evaluates a string as a Helm template.

Example:

```gotemplate
{{ tpl .Values.templateString . }}
```

Use carefully because it allows values to contain template expressions.

---

# `lookup`

`lookup` can query existing Kubernetes resources during template rendering.

Conceptually:

```text
Helm
 ↓
Kubernetes API
 ↓
Existing Resource
```

Use carefully because this can make rendering dependent on cluster state.

---

# Conditional Resources

Example:

```yaml
ingress:
  enabled: false
```

Template:

```gotemplate
{{- if .Values.ingress.enabled }}
...
{{- end }}
```

---

# Environment-Specific Values

Development:

```yaml
replicaCount: 1

resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

Production:

```yaml
replicaCount: 5

resources:
  requests:
    cpu: 500m
    memory: 512Mi
```

---

# Values File Structure

Example:

```yaml
replicaCount: 3

image:
  repository: example/api
  tag: "2.4.0"

service:
  type: ClusterIP
  port: 8080

ingress:
  enabled: true
  host: api.example.com
```

---

# Schema Validation

Charts can define:

```text
values.schema.json
```

This can validate user-provided values.

Example concepts:

```text
Required Fields
Types
Allowed Values
Structure
```

---

# Chart Dependencies

A Chart can depend on other Charts.

Example:

```text
Application Chart
      │
      ├── Redis
      └── PostgreSQL
```

Dependencies can be declared in `Chart.yaml`.

---

# Example Dependency

```yaml
dependencies:
  - name: redis
    version: 20.x.x
    repository: https://charts.example.com
```

Use controlled versions and trusted sources.

---

# Helm Dependency Update

```bash
helm dependency update ./mychart
```

---

# Helm Dependency Build

```bash
helm dependency build ./mychart
```

---

# Subcharts

A dependency can function as a subchart of the parent Chart.

Parent configuration may pass values to the subchart.

---

# Global Values

Helm supports global values:

```yaml
global:
  environment: production
```

Subcharts can access appropriately scoped global values.

Use global configuration carefully to avoid hidden coupling.

---

# Library Charts

Library Charts provide reusable template helpers instead of directly deploying an application.

Useful for:

```text
Shared Labels
Naming
Security Defaults
Common Templates
```

---

# Helm Hooks

Hooks allow certain resources or Jobs to execute at lifecycle points.

Examples include:

```text
pre-install
post-install
pre-upgrade
post-upgrade
pre-rollback
post-rollback
```

---

# Hook Example

Conceptually:

```yaml
metadata:
  annotations:
    "helm.sh/hook": pre-install
```

---

# Hook Use Cases

Possible use cases:

```text
Database Migration
Initialization
Validation
Cleanup
```

Use hooks carefully because they can complicate deployment behavior.

---

# Helm Tests

Helm supports test hooks.

Example:

```yaml
metadata:
  annotations:
    "helm.sh/hook": test
```

Run:

```bash
helm test myrelease
```

---

# Helm Tests

Tests can validate:

```text
Service Reachability
Application Health
Basic Functionality
```

---

# Helm Package

Package a Chart:

```bash
helm package ./mychart
```

This creates an archive:

```text
mychart-1.0.0.tgz
```

---

# Helm Repository Index

Traditional Chart repositories use an index describing available Charts.

Conceptually:

```text
Chart Package
 ↓
Repository
 ↓
index.yaml
```

---

# Helm Repo Add

Example:

```bash
helm repo add example https://charts.example.com
```

---

# Helm Repo Update

```bash
helm repo update
```

---

# Helm Search

Search repositories:

```bash
helm search repo nginx
```

---

# Helm Pull

Download a Chart:

```bash
helm pull example/api
```

---

# OCI Registries

Helm supports OCI-based Chart storage.

Conceptually:

```text
Helm Chart
 ↓
OCI Registry
```

---

# OCI Authentication

Authentication depends on the registry.

Example:

```bash
helm registry login registry.example.com
```

---

# OCI Chart Push

A packaged Chart can be pushed to an OCI registry.

Example:

```bash
helm push mychart-1.0.0.tgz oci://registry.example.com/charts
```

---

# OCI Chart Pull

```bash
helm pull oci://registry.example.com/charts/mychart \
  --version 1.0.0
```

---

# Chart Signing

Chart signing can provide integrity and provenance information.

Historically Helm supported provenance files and signing workflows.

Modern supply-chain systems may additionally use:

```text
OCI
+
Sigstore
+
Cosign
```

depending on the organization's security architecture.

---

# Helm Security

Helm should be treated as part of the production software supply chain.

Security considerations:

```text
Chart Source
+
Dependencies
+
Values
+
Templates
+
Registry
+
Credentials
+
Kubernetes Permissions
```

---

# Trusted Chart Sources

Use Charts from:

```text
Trusted Organizations
Verified Sources
Internal Repositories
Approved Registries
```

Review third-party Charts before production use.

---

# Chart Security Review

Inspect:

```text
RBAC
SecurityContext
HostPath
HostNetwork
Privileged Containers
Capabilities
Secrets
Images
Network Policies
Resource Limits
```

---

# Dangerous Chart Configuration

Be careful with:

```yaml
privileged: true
```

or:

```yaml
hostNetwork: true
```

or:

```yaml
hostPath:
```

These may be legitimate in some infrastructure workloads but should require deliberate review.

---

# Helm and RBAC

A Helm Chart may create:

```text
ServiceAccounts
Roles
RoleBindings
ClusterRoles
ClusterRoleBindings
```

Review these carefully.

---

# Helm and Secrets

Avoid placing production secrets directly into:

```text
values.yaml
```

in plaintext.

Instead use appropriate secret-management systems.

---

# Helm With External Secrets

A Chart can deploy an ExternalSecret resource.

Conceptually:

```text
Helm
 ↓
ExternalSecret
 ↓
Secret Manager
 ↓
Kubernetes Secret
```

---

# Helm and GitOps

Helm integrates naturally with GitOps.

Architecture:

```text
Git
 ↓
Helm Chart
+
Values
 ↓
Argo CD / Flux
 ↓
Kubernetes
```

---

# Argo CD and Helm

Argo CD can use Helm Charts as an application source.

Conceptually:

```text
Repository
 ↓
Chart
 ↓
Values
 ↓
Argo CD
 ↓
Kubernetes
```

---

# Flux and Helm

Flux can manage Helm releases declaratively.

Conceptually:

```text
Git
 ↓
HelmRelease
 ↓
Flux
 ↓
Helm
 ↓
Kubernetes
```

---

# Helm With CI/CD

A pipeline may run:

```bash
helm lint ./chart
```

Then:

```bash
helm template api ./chart
```

Then:

```bash
kubectl apply --dry-run=server ...
```

Then update the GitOps repository.

---

# Production Helm Pipeline

```text
Pull Request
    ↓
helm lint
    ↓
Template
    ↓
Security Scan
    ↓
Policy Validation
    ↓
Review
    ↓
Merge
    ↓
GitOps
    ↓
Kubernetes
```

---

# Helm Upgrade Strategy

Before production upgrades:

```text
Review
 ↓
Render
 ↓
Validate
 ↓
Test
 ↓
Deploy
 ↓
Monitor
```

---

# Atomic Upgrade

Helm supports:

```bash
helm upgrade myrelease ./mychart \
  --atomic
```

This can roll back the release if the upgrade fails according to Helm's upgrade behavior.

Use it deliberately and understand the consequences for hooks and application-level migrations.

---

# Wait

Helm can wait for resources:

```bash
helm upgrade myrelease ./mychart \
  --wait
```

This makes Helm wait for supported resources to reach the expected state.

---

# Timeout

Example:

```bash
helm upgrade myrelease ./mychart \
  --wait \
  --timeout 10m
```

Choose timeout values based on actual application startup behavior.

---

# Dry Run

Preview an installation:

```bash
helm install myrelease ./mychart \
  --dry-run
```

For additional rendered output:

```bash
helm install myrelease ./mychart \
  --dry-run \
  --debug
```

---

# Helm Diff

The `helm-diff` plugin can help compare current and proposed release manifests.

Conceptually:

```text
Current
   vs
Proposed
```

Always review changes before sensitive production upgrades.

---

# Helm Rollback Strategy

Example:

```bash
helm history myrelease
```

Identify a known-good revision.

Then:

```bash
helm rollback myrelease <revision>
```

---

# Helm Rollback Limitations

A Helm rollback restores a previous Chart release state.

It does not automatically solve every application-level issue.

For example:

```text
Database Migration
```

may not be safely reversible.

Always design application migrations with rollback and compatibility in mind.

---

# Database Migrations

A common safe deployment pattern is:

```text
Backward-Compatible Schema
        ↓
Application Deployment
        ↓
Migration Completion
        ↓
New Application Behavior
```

Avoid assuming Helm rollback automatically reverses database schema changes.

---

# Helm Release History

Helm maintains release revisions.

Example:

```text
Revision 1 → v1
Revision 2 → v2
Revision 3 → v3
```

Rollback can return to:

```text
Revision 2
```

---

# Helm and Namespaces

Always know where the release is installed.

```bash
helm list -A
```

A release is namespace-scoped.

---

# Helm Release Naming

Use clear names:

```text
production-api
staging-api
dev-api
```

Avoid confusing or ambiguous release names.

---

# Production Chart Structure

Recommended structure:

```text
api/
├── Chart.yaml
├── values.yaml
├── values.schema.json
├── README.md
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── serviceaccount.yaml
│   ├── configmap.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   ├── networkpolicy.yaml
│   └── _helpers.tpl
└── tests/
```

---

# Production Values

A production values file may contain:

```yaml
replicaCount: 5

image:
  repository: registry.example.com/api
  tag: "2.4.0"

resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: "1"
    memory: 1Gi

podSecurityContext:
  runAsNonRoot: true
```

---

# Avoid Huge Templates

Do not place hundreds of lines of complicated logic into a single template.

Prefer:

```text
Small Templates
+
Reusable Helpers
+
Clear Values
```

---

# Avoid Excessive Templating

Helm should simplify Kubernetes configuration.

Overly complex templates can become difficult to:

```text
Read
Debug
Test
Maintain
```

---

# Use Schema Validation

For reusable production Charts:

```text
values.schema.json
```

can catch invalid configuration early.

---

# Document Values

Document important values.

Example:

```yaml
# Number of application replicas.
replicaCount: 3
```

---

# Chart README

The README should explain:

```text
Installation
Configuration
Values
Dependencies
Examples
Upgrades
Rollback
Troubleshooting
```

---

# Chart Testing

Test:

```text
Template Rendering
Installation
Upgrade
Rollback
Health
Security
```

---

# Helm Test Workflow

```text
helm lint
    ↓
helm template
    ↓
Install
    ↓
helm test
    ↓
Upgrade
    ↓
helm test
    ↓
Rollback
    ↓
Validate
```

---

# Helm Troubleshooting

When a Helm deployment fails:

```text
1. Check Helm status
2. Check Helm history
3. Inspect rendered manifests
4. Check Kubernetes events
5. Check Pods
6. Check Logs
7. Check Values
8. Check Dependencies
9. Check Admission Policies
10. Check RBAC
```

---

# Check Release Status

```bash
helm status myrelease
```

---

# Check History

```bash
helm history myrelease
```

---

# Inspect Values

```bash
helm get values myrelease --all
```

---

# Inspect Manifest

```bash
helm get manifest myrelease
```

---

# Kubernetes Investigation

```bash
kubectl get pods -n production
```

Then:

```bash
kubectl describe pod <pod> -n production
```

And:

```bash
kubectl logs <pod> -n production
```

---

# Check Events

```bash
kubectl get events \
  -n production \
  --sort-by=.lastTimestamp
```

---

# Helm Rendering Problems

Common causes:

```text
Wrong Values
Missing Required Value
Template Syntax Error
Incorrect Indentation
Wrong Data Type
Missing Dependency
```

---

# Kubernetes Problems

Helm may render successfully while Kubernetes rejects or fails the workload.

Possible causes:

```text
RBAC
Admission Policy
Image Pull Failure
Insufficient Resources
Invalid Configuration
Probe Failure
```

---

# Helm and ImagePullBackOff

If the Chart deploys:

```text
ImagePullBackOff
```

check:

```text
Image Repository
Image Tag
Registry Credentials
Network Access
Image Existence
```

---

# Helm and CrashLoopBackOff

Check:

```text
Application Logs
Configuration
Secrets
Environment Variables
Probes
Dependencies
```

---

# Helm and Pending Pods

Check:

```text
Resource Requests
Node Capacity
Affinity
Taints
Tolerations
PVCs
Scheduling Constraints
```

---

# Helm and GitOps

Avoid manually changing a GitOps-managed Helm release.

Preferred:

```text
Change Values in Git
       ↓
Review
       ↓
Merge
       ↓
GitOps Reconciliation
```

---

# Helm Best Practices

### 1. Keep Charts Reusable

Avoid hardcoding environment-specific configuration.

---

### 2. Use Values for Configuration

Example:

```yaml
replicaCount: 3
```

instead of hardcoding:

```yaml
replicas: 3
```

everywhere.

---

### 3. Validate Charts

Use:

```bash
helm lint
helm template
```

---

### 4. Use Schema Validation

Add:

```text
values.schema.json
```

for reusable Charts.

---

### 5. Pin Dependencies

Use controlled Chart dependency versions.

---

### 6. Review Third-Party Charts

Never blindly deploy an external Chart.

---

### 7. Secure Images

Use:

```text
Trusted Registry
Pinned Versions
Image Scanning
Digests
```

where appropriate.

---

### 8. Avoid Plaintext Secrets

Use external secret-management mechanisms.

---

### 9. Use Resource Controls

Charts should expose:

```text
Requests
Limits
```

---

### 10. Configure Security Contexts

Where appropriate:

```yaml
securityContext:
  runAsNonRoot: true
```

---

### 11. Use Health Probes

Production applications should expose:

```text
Startup
Readiness
Liveness
```

where appropriate.

---

### 12. Test Rollbacks

A rollback strategy should be tested before production incidents occur.

---

### 13. Avoid Excessive Hooks

Hooks can introduce lifecycle complexity.

Use them only when necessary.

---

### 14. Keep Templates Simple

Complex logic belongs in application or tooling code when possible.

---

### 15. Document Values

Make Chart configuration understandable to operators.

---

# Common Mistakes

## 1. Hardcoding Configuration

This makes Charts difficult to reuse.

---

## 2. Storing Secrets in `values.yaml`

Plaintext secrets can leak into Git.

---

## 3. Using `latest`

This creates unpredictable deployments.

---

## 4. Not Testing Templates

A Chart can look correct while rendering invalid YAML.

---

## 5. Not Checking Rendered Output

Always inspect:

```bash
helm template
```

for important changes.

---

## 6. Excessive Template Logic

Overly complex templates become difficult to maintain.

---

## 7. Unpinned Dependencies

Dependency updates can unexpectedly change behavior.

---

## 8. Blindly Trusting Third-Party Charts

Charts can create powerful resources.

Always review them.

---

## 9. Overusing `lookup`

Cluster-dependent rendering can reduce reproducibility.

---

## 10. Ignoring RBAC

A Chart may create broad cluster-level permissions.

---

## 11. Ignoring Hooks

Hooks can modify deployment behavior in unexpected ways.

---

## 12. Assuming Rollback Reverses Everything

Application data and database schema changes may not be reversible automatically.

---

## 13. No Resource Requests

Workloads may become difficult to schedule and manage.

---

## 14. No SecurityContext

Containers may run with unnecessarily broad privileges.

---

## 15. Manual Changes to GitOps Releases

This creates drift.

---

# Hands-on Lab 1 – Create a Helm Chart

Create:

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

# Hands-on Lab 2 – Customize Values

Change:

```yaml
replicaCount: 3
```

Render:

```bash
helm template myapp ./myapp
```

Verify the Deployment.

---

# Hands-on Lab 3 – Install a Chart

Install:

```bash
helm install myapp ./myapp
```

Verify:

```bash
helm status myapp
```

---

# Hands-on Lab 4 – Upgrade a Release

Change:

```yaml
replicaCount: 5
```

Then:

```bash
helm upgrade myapp ./myapp
```

Verify:

```bash
kubectl get pods
```

---

# Hands-on Lab 5 – Rollback

View:

```bash
helm history myapp
```

Rollback:

```bash
helm rollback myapp 1
```

Verify the workload.

---

# Hands-on Lab 6 – Environment Values

Create:

```text
values-dev.yaml
values-staging.yaml
values-production.yaml
```

Deploy:

```bash
helm upgrade --install myapp ./myapp \
  -f values-production.yaml
```

---

# Hands-on Lab 7 – Template Conditions

Add:

```yaml
ingress:
  enabled: false
```

Use an `if` condition.

Verify that the Ingress appears only when enabled.

---

# Hands-on Lab 8 – Named Templates

Create helpers in:

```text
templates/_helpers.tpl
```

Generate:

```text
Name
Full Name
Labels
Selector Labels
```

---

# Hands-on Lab 9 – Resource Configuration

Expose:

```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

Render and verify.

---

# Hands-on Lab 10 – SecurityContext

Add:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
```

Deploy and validate.

---

# Hands-on Lab 11 – Helm Tests

Create a test Job.

Run:

```bash
helm test myapp
```

Verify the result.

---

# Hands-on Lab 12 – Chart Dependency

Add a controlled dependency to a test Chart.

Run:

```bash
helm dependency update ./myapp
```

Inspect:

```text
charts/
```

---

# Hands-on Lab 13 – Helm With GitOps

Store:

```text
Chart
+
Values
```

in Git.

Deploy through:

```text
Argo CD
```

or:

```text
Flux
```

---

# Hands-on Lab 14 – Production Validation

Before deployment run:

```bash
helm lint ./myapp
```

Then:

```bash
helm template myapp ./myapp
```

Then validate the resulting manifests.

---

# Hands-on Lab 15 – Helm Security Review

Inspect a third-party Chart.

Look for:

```text
Privileged Containers
RBAC
HostPath
HostNetwork
Secrets
Images
Capabilities
SecurityContext
```

Document all security concerns.

---

# Hands-on Lab 16 – Helm CI Pipeline

Create a CI pipeline:

```text
Pull Request
 ↓
helm lint
 ↓
helm template
 ↓
Security Scan
 ↓
Policy Validation
 ↓
Review
```

---

# Hands-on Lab 17 – OCI Registry

Package a Chart:

```bash
helm package ./myapp
```

Push it to a test OCI registry.

Pull it back.

Verify the Chart version.

---

# Hands-on Lab 18 – Production Upgrade

Deploy:

```text
v1
```

Then upgrade to:

```text
v2
```

Use:

```bash
helm upgrade
```

with an appropriate timeout and deployment strategy.

Monitor:

```text
Pods
Events
Logs
Health
```

---

# Hands-on Lab 19 – Failed Upgrade

Introduce an intentionally broken configuration.

Attempt:

```bash
helm upgrade
```

Observe the failure.

Use:

```bash
helm history
helm status
```

Then perform a controlled rollback.

---

# Hands-on Lab 20 – Complete Production Helm Project

Build a production-style Chart containing:

```text
Deployment
Service
ConfigMap
Secret Integration
Ingress / Gateway
HPA
PDB
NetworkPolicy
ServiceAccount
SecurityContext
Resource Requests
Resource Limits
Health Probes
```

Support:

```text
Development
Staging
Production
```

Then integrate it with:

```text
CI/CD
+
GitOps
+
Image Scanning
+
Policy Validation
+
Monitoring
```

---

# Quick Revision

## Helm

```text
Kubernetes Package Manager
```

---

## Chart

```text
Reusable Kubernetes Application Package
```

---

## Release

```text
Installed Instance of a Chart
```

---

## `Chart.yaml`

```text
Chart Metadata
```

---

## `values.yaml`

```text
Default Configuration
```

---

## `templates/`

```text
Kubernetes Resource Templates
```

---

## `_helpers.tpl`

```text
Reusable Named Templates
```

---

## `helm install`

```text
Install a Chart
```

---

## `helm upgrade`

```text
Update an Existing Release
```

---

## `helm rollback`

```text
Return a Release to a Previous Revision
```

---

## `helm lint`

```text
Validate Chart Structure
```

---

## `helm template`

```text
Render Kubernetes Manifests Locally
```

---

## `helm test`

```text
Execute Chart Tests
```

---

## OCI

```text
Registry-Based Storage for Helm Artifacts
```

---

# Essential Commands

Check Helm:

```bash
helm version
```

Create Chart:

```bash
helm create mychart
```

Lint:

```bash
helm lint ./mychart
```

Render:

```bash
helm template myrelease ./mychart
```

Debug render:

```bash
helm template myrelease ./mychart --debug
```

Install:

```bash
helm install myrelease ./mychart
```

Install into namespace:

```bash
helm install myrelease ./mychart \
  -n production \
  --create-namespace
```

Install with values:

```bash
helm install myrelease ./mychart \
  -f production-values.yaml
```

Install with `--set`:

```bash
helm install myrelease ./mychart \
  --set replicaCount=3
```

Install or upgrade:

```bash
helm upgrade --install myrelease ./mychart
```

List releases:

```bash
helm list -A
```

Release status:

```bash
helm status myrelease
```

Release history:

```bash
helm history myrelease
```

Release values:

```bash
helm get values myrelease
```

All values:

```bash
helm get values myrelease --all
```

Release manifest:

```bash
helm get manifest myrelease
```

Upgrade:

```bash
helm upgrade myrelease ./mychart
```

Upgrade with wait:

```bash
helm upgrade myrelease ./mychart \
  --wait
```

Upgrade atomically:

```bash
helm upgrade myrelease ./mychart \
  --atomic \
  --wait
```

Rollback:

```bash
helm rollback myrelease 1
```

Uninstall:

```bash
helm uninstall myrelease
```

Package:

```bash
helm package ./mychart
```

Add repository:

```bash
helm repo add example https://charts.example.com
```

Update repositories:

```bash
helm repo update
```

Search:

```bash
helm search repo nginx
```

Pull Chart:

```bash
helm pull example/mychart
```

Dependency update:

```bash
helm dependency update ./mychart
```

Dependency build:

```bash
helm dependency build ./mychart
```

OCI login:

```bash
helm registry login registry.example.com
```

OCI pull:

```bash
helm pull oci://registry.example.com/charts/mychart \
  --version 1.0.0
```

---

# Interview Questions

## Basic

- What is Helm?
- Why is Helm used in Kubernetes?
- What is a Helm Chart?
- What is a Helm Release?
- What is `Chart.yaml`?
- What is `values.yaml`?
- What is the `templates` directory?
- What is `_helpers.tpl`?
- What is the difference between Chart version and application version?
- What is `helm install`?
- What is `helm upgrade`?
- What is `helm rollback`?
- What is `helm lint`?
- What is `helm template`?
- What is a Helm repository?
- What is an OCI registry?

---

## Intermediate

- How does Helm templating work?
- What are Helm values?
- How does value precedence work?
- What are named templates?
- What is the purpose of `_helpers.tpl`?
- What does `include` do?
- What does `required` do?
- What does `default` do?
- What does `toYaml` do?
- What does `nindent` do?
- What are Helm dependencies?
- What are subcharts?
- What are library Charts?
- What are Helm hooks?
- What are Helm tests?
- How do you manage multiple environments using Helm?
- How do you use Helm with GitOps?
- How do you secure Helm Charts?

---

## Advanced

- Explain Helm architecture.
- How does Helm render templates?
- How would you design a production Helm Chart?
- How would you manage secrets with Helm?
- How would you secure third-party Helm Charts?
- How do Helm dependencies work?
- How would you design reusable Helm Charts?
- What are the risks of excessive Helm templating?
- How does Helm interact with Kubernetes?
- How does Helm work with Argo CD?
- How does Helm work with Flux?
- How would you implement Helm in a CI/CD pipeline?
- How would you implement Helm rollback in production?
- What are the limitations of Helm rollback?
- How would you handle database migrations with Helm?
- How would you store Helm Charts in OCI registries?
- How would you secure the Helm software supply chain?

---

# Interview Scenario 1

### Question

> What is the difference between a Helm Chart and a Helm Release?

### Answer

A **Chart** is the reusable package.

A **Release** is an installed instance of that Chart.

Example:

```text
Chart:
api

Releases:
dev-api
staging-api
production-api
```

---

# Interview Scenario 2

### Question

> What happens when you run `helm install`?

### Answer

Conceptually:

```text
Chart
 ↓
Values
 ↓
Template Rendering
 ↓
Kubernetes Manifests
 ↓
Kubernetes API
 ↓
Resources Created
 ↓
Release Recorded
```

---

# Interview Scenario 3

### Question

> What is the difference between `helm upgrade` and `kubectl apply`?

### Answer

`kubectl apply` directly applies Kubernetes manifests.

Helm manages a packaged application as a release and provides:

```text
Values
+
Templates
+
Release History
+
Upgrade
+
Rollback
+
Dependencies
```

---

# Interview Scenario 4

### Question

> How do you manage different configurations for dev and production?

### Answer

Use environment-specific values files:

```text
values-dev.yaml
values-staging.yaml
values-production.yaml
```

For example:

```bash
helm upgrade --install api ./chart \
  -f values-production.yaml
```

The Chart remains reusable while environment-specific configuration changes.

---

# Interview Scenario 5

### Question

> How do you secure a Helm Chart?

### Answer

I would review:

```text
RBAC
+
SecurityContext
+
Images
+
Capabilities
+
HostPath
+
HostNetwork
+
Secrets
+
NetworkPolicy
+
Resource Limits
```

I would also scan the Chart and dependencies and use trusted sources.

---

# Interview Scenario 6

### Question

> Does Helm rollback reverse a database migration?

### Answer

No.

Helm rollback restores a previous release configuration, but database schema changes may not be automatically reversible.

Database migrations should therefore be designed for compatibility and controlled rollback.

---

# Interview Scenario 7

### Question

> How would you use Helm with GitOps?

### Answer

Store:

```text
Chart
+
Values
```

in Git.

Then:

```text
Git
 ↓
Argo CD / Flux
 ↓
Helm
 ↓
Kubernetes
```

Changes are reviewed and reconciled through GitOps.

---

# Interview Scenario 8

### Question

> How would you troubleshoot a failed Helm deployment?

### Answer

I would start with:

```bash
helm status <release>
helm history <release>
helm get values <release> --all
helm get manifest <release>
```

Then inspect Kubernetes:

```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get events --sort-by=.lastTimestamp
```

I would then determine whether the problem is:

```text
Template
+
Configuration
+
RBAC
+
Image
+
Resources
+
Scheduling
+
Application
```

---

# Interview Scenario 9

### Question

> Why should you run `helm template` before production deployment?

### Answer

It lets you inspect the exact Kubernetes manifests generated from:

```text
Chart
+
Values
```

before they are applied.

This helps catch:

```text
Incorrect Values
Bad YAML
Unexpected Resources
Security Problems
Configuration Errors
```

---

# Interview Scenario 10

### Question

> Design a production Helm architecture.

### Answer

```text
                    Git
                     │
                     ▼
                 Helm Chart
                     │
             ┌───────┴───────┐
             ▼               ▼
        values-dev       values-prod
             │               │
             └───────┬───────┘
                     ▼
                    CI
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Lint         Render       Scan
        │            │            │
        └────────────┼────────────┘
                     ▼
               Policy Validation
                     │
                     ▼
                 GitOps Repo
                     │
                     ▼
                Argo CD / Flux
                     │
                     ▼
                 Kubernetes
                     │
             ┌───────┼───────┐
             ▼       ▼       ▼
          Monitor   Logs    Alerts
```

The Chart should provide:

```text
Resource Management
+
SecurityContext
+
Health Probes
+
PDB
+
HPA
+
NetworkPolicy
+
ServiceAccount
```

and should avoid embedding environment-specific secrets directly into the Chart.

---

# Production Helm Checklist

```text
☑ Chart metadata defined
☑ Chart version controlled
☑ Application version documented
☑ values.yaml documented
☑ values.schema.json added where appropriate
☑ Templates validated
☑ helm lint passing
☑ helm template reviewed
☑ Dependencies pinned
☑ Third-party Charts reviewed
☑ Images controlled
☑ Images scanned
☑ Immutable image references considered
☑ SecurityContext configured
☑ RBAC reviewed
☑ NetworkPolicy reviewed
☑ Resource requests defined
☑ Resource limits defined
☑ Health probes configured
☑ PDB configured where appropriate
☑ Secrets not stored in plaintext
☑ Environment values separated
☑ Hooks minimized
☑ Helm tests implemented where useful
☑ Rollback tested
☑ Upgrade strategy documented
☑ Database migrations handled separately
☑ GitOps integration configured
☑ CI validation configured
☑ Production changes reviewed
☑ OCI/registry access secured
☑ Chart provenance/signing considered
☑ Documentation maintained
```

---

# Chapter Summary

Helm provides a reusable packaging and configuration layer for Kubernetes.

The core model is:

```text
Chart
 +
Values
 ↓
Templates
 ↓
Rendered Manifests
 ↓
Helm Release
 ↓
Kubernetes
```

Important Helm concepts are:

```text
Chart
Release
Values
Templates
Dependencies
Hooks
Repositories
OCI Registries
```

The most important commands are:

```bash
helm lint
helm template
helm install
helm upgrade
helm history
helm rollback
helm status
helm uninstall
```

For production environments, Helm should be combined with:

```text
CI/CD
+
GitOps
+
Image Security
+
Secret Management
+
Policy as Code
+
RBAC
+
Monitoring
```

Helm is powerful, but it does not replace Kubernetes security, GitOps governance, or application-level reliability practices.

The most important principle is:

> **Use Helm to package and template Kubernetes applications consistently, keep configuration explicit and validated, secure Charts and dependencies, test upgrades and rollbacks, and integrate Helm with GitOps and CI/CD for controlled production delivery.**

---

## Next Chapter

# Chapter 81 – Kustomize

Topics will include:

- Kustomize Fundamentals
- What Is Kustomize?
- Why Kustomize?
- Kustomize vs Helm
- Kustomize Architecture
- Declarative Configuration
- Base and Overlays
- `kustomization.yaml`
- Resources
- Namespaces
- Common Labels
- Common Annotations
- Name Prefix
- Name Suffix
- Images
- Replicas
- ConfigMap Generators
- Secret Generators
- Generators
- Patches
- Strategic Merge Patches
- JSON Patches
- JSON6902
- Replacement
- Transformers
- Built-In Transformers
- Components
- Variables
- Replacements
- Environment Management
- Development
- Staging
- Production
- Multi-Cluster Configuration
- Kustomize Directory Structure
- Kustomize Build
- Kustomize Edit
- Kustomize Validation
- Kustomize with `kubectl`
- Kustomize with GitOps
- Kustomize with Argo CD
- Kustomize with Flux
- Kustomize with CI/CD
- Secrets
- Secret Security
- Configuration Management
- Image Updates
- Immutable Images
- Patches
- Patch Ordering
- Overlay Design
- Base Design
- Reusability
- Production Best Practices
- Kustomize vs Helm
- Common Mistakes
- Troubleshooting
- Hands-on Labs
- Quick Revision
- Interview Questions
- References

---