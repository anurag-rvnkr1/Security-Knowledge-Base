# Chapter 50 – Admission Controllers

## Overview

Kubernetes processes API requests through several security and policy stages.

A simplified request pipeline is:

```text
Client
  ↓
Authentication
  ↓
Authorization
  ↓
Admission Control
  ↓
Persistence
```

Authentication determines:

```text
Who are you?
```

Authorization determines:

```text
Are you allowed to perform this operation?
```

Admission control determines:

```text
Should this request be accepted, rejected, or modified?
```

Admission Controllers are therefore an important enforcement layer for:

```text
Security
Compliance
Governance
Policy
Resource Management
Configuration
```

They can:

```text
Reject requests
Modify requests
Validate requests
Enforce organizational policies
```

---

# Learning Objectives

After completing this chapter, you will understand:

- What Admission Controllers are
- Why admission control is needed
- Kubernetes API request pipeline
- Authentication vs authorization vs admission
- Mutating admission
- Validating admission
- Built-in admission controllers
- `ValidatingAdmissionPolicy`
- `MutatingAdmissionPolicy`
- Admission webhooks
- Validating webhooks
- Mutating webhooks
- Pod Security Admission
- Security policy enforcement
- Image policy
- Resource policy
- Namespace policy
- Custom admission controllers
- Admission webhook architecture
- Webhook TLS
- Failure policies
- `failurePolicy`
- `matchPolicy`
- `namespaceSelector`
- `objectSelector`
- `sideEffects`
- `timeoutSeconds`
- Admission ordering
- Security risks
- Webhook security
- Availability risks
- Admission controller troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Are Admission Controllers?

Admission Controllers are components of the Kubernetes API Server processing pipeline that intercept API requests after authentication and authorization and before the object is persisted.

Conceptually:

```text
kubectl
   ↓
API Server
   ↓
Authentication
   ↓
Authorization
   ↓
Admission
   ↓
Validation
   ↓
Persist Object
```

Admission control can:

```text
Allow
Reject
Mutate
Validate
```

---

# Why Is Admission Control Needed?

RBAC answers:

```text
Can Alice create a Pod?
```

But it does not necessarily answer:

```text
Is Alice's Pod secure enough?
```

For example, an organization may require:

```text
No privileged containers
Run as non-root
Approved image registries
Resource limits
Required labels
Security policies
```

Admission control can enforce such rules.

---

# Example

Suppose a developer creates:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: insecure-app

spec:

  containers:

  - name: app

    image: nginx:1.30

    securityContext:

      privileged: true
```

RBAC may allow the developer to create the Pod.

However, an admission policy could reject it:

```text
privileged containers are not allowed
```

Therefore:

```text
Authentication
      ↓
Authorization = ALLOWED
      ↓
Admission = DENIED
```

---

# Admission vs Authorization

This distinction is extremely important.

## Authorization

```text
Can this identity perform this API operation?
```

Example:

```text
Developer
 ↓
create Pod?
 ↓
Yes
```

---

## Admission

```text
Should this particular object/request be accepted?
```

Example:

```text
Pod
 ↓
privileged=true
 ↓
Policy violation
 ↓
Reject
```

---

# Complete API Request Flow

A simplified Kubernetes request flow is:

```text
                  Client
                    │
                    ▼
              Kubernetes API
                    │
                    ▼
             Authentication
                    │
                    ▼
                Identity
                    │
                    ▼
              Authorization
                    │
                    ▼
            Admission Control
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Mutating           Validating
          │                   │
          └─────────┬─────────┘
                    ▼
                Validation
                    │
                    ▼
                Persistence
```

The exact internal processing details are more nuanced, but this model is useful for understanding the security pipeline.

---

# Admission Control Types

Admission controls can broadly be divided into:

```text
Mutating
Validating
```

---

# Mutating Admission

A mutating admission mechanism can modify an incoming object before it is persisted.

Example:

```text
Developer creates Pod
        ↓
Mutating Admission
        ↓
Adds required label
        ↓
Object continues
```

---

# Example Mutation

Input:

```yaml
metadata:

  name: backend
```

Admission mechanism may add:

```yaml
metadata:

  labels:

    environment: production
```

The final object becomes:

```yaml
metadata:

  name: backend

  labels:

    environment: production
```

---

# Common Uses of Mutation

Mutating admission can be used for:

```text
Defaulting
Sidecar Injection
Security Configuration
Labels
Annotations
Resource Defaults
Configuration Injection
```

---

# Sidecar Injection

A classic example is service mesh injection.

Developer creates:

```text
Pod
```

Admission webhook modifies it:

```text
Pod
 +
Sidecar Container
 +
Volumes
 +
Configuration
```

Result:

```text
Application Pod
 ├── Application
 └── Sidecar
```

---

# Validating Admission

Validating admission checks whether a request satisfies a policy.

It normally does not modify the object.

Example:

```text
Pod
 ↓
Validation
 ↓
privileged=true
 ↓
Reject
```

---

# Example Validation

Policy:

```text
Images must come from:
registry.example.com
```

Request:

```yaml
image: docker.io/nginx:1.30
```

Admission result:

```text
Rejected
```

---

# Mutating vs Validating

| Type | Purpose |
|---|---|
| Mutating | Modify request |
| Validating | Accept or reject request |

Example:

```text
Mutating:
Add securityContext
```

```text
Validating:
Reject privileged Pod
```

---

# Admission Webhooks

Kubernetes can call external webhook services during admission.

There are two major webhook types:

```text
MutatingAdmissionWebhook
ValidatingAdmissionWebhook
```

Conceptually:

```text
API Server
    │
    ▼
Admission Webhook
    │
    ▼
External Service
    │
    ▼
Response
    │
    ▼
API Server
```

---

# Validating Admission Webhook

A validating webhook receives an admission request and returns a decision.

Conceptually:

```text
API Server
    ↓
Webhook
    ↓
Is request valid?
    ↓
Yes / No
```

---

# Mutating Admission Webhook

A mutating webhook can return changes to the object.

Conceptually:

```text
API Server
    ↓
Webhook
    ↓
Generate Patch
    ↓
API Server applies mutation
```

---

# Webhook Architecture

```text
                    API Server
                        │
                        ▼
                Admission Request
                        │
                        ▼
                  Webhook Service
                        │
                        ▼
                 Webhook Container
                        │
                        ▼
                  Policy Decision
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
          Allowed                Denied
             │
             ▼
        API Processing
```

---

# Admission Webhook Components

A typical webhook deployment contains:

```text
Deployment
Service
Webhook Configuration
TLS Certificate
Webhook Application
```

Example:

```text
Namespace
 ├── webhook Deployment
 ├── webhook Service
 └── webhook Secret / Certificate
```

---

# TLS for Webhooks

Admission webhooks communicate securely with the API Server.

TLS is essential because:

```text
API Server
    ↓
Webhook
```

may involve sensitive API objects and policy decisions.

The API Server must be able to verify the webhook server's certificate.

---

# Webhook Security

A webhook should:

```text
Use TLS
Use trusted certificates
Run with least privilege
Restrict network exposure
Be highly available
Validate requests carefully
Avoid unnecessary data access
```

---

# Webhook Configuration

A validating webhook is configured using:

```text
ValidatingWebhookConfiguration
```

A mutating webhook uses:

```text
MutatingWebhookConfiguration
```

---

# Example Validating Webhook Configuration

Conceptually:

```yaml
apiVersion: admissionregistration.k8s.io/v1

kind: ValidatingWebhookConfiguration

metadata:

  name: security-policy

webhooks:

- name: security.example.com

  admissionReviewVersions:

  - v1

  sideEffects: None

  clientConfig:

    service:

      name: security-webhook

      namespace: security

      path: /validate
```

Additional fields are normally required for a production configuration.

---

# AdmissionReview

The API Server communicates with admission webhooks using:

```text
AdmissionReview
```

The request contains information about the object and operation.

Conceptually:

```text
AdmissionReview
 ├── Request
 │    ├── UID
 │    ├── Operation
 │    ├── UserInfo
 │    ├── Resource
 │    ├── Namespace
 │    └── Object
 │
 └── Response
      ├── Allowed
      └── Patch
```

---

# Admission Operations

Admission requests can involve operations such as:

```text
CREATE
UPDATE
DELETE
CONNECT
```

A webhook can specify which operations it wants to intercept.

---

# `failurePolicy`

One of the most important webhook settings is:

```text
failurePolicy
```

Common values:

```text
Fail
Ignore
```

---

# `failurePolicy: Fail`

If the webhook cannot be reached or returns an appropriate failure:

```text
Request fails
```

Conceptually:

```text
API Server
   ↓
Webhook unavailable
   ↓
Admission failure
   ↓
Request rejected
```

---

# `failurePolicy: Ignore`

If the webhook cannot be reached:

```text
Request may continue
```

Conceptually:

```text
API Server
   ↓
Webhook unavailable
   ↓
Skip webhook decision
   ↓
Continue processing
```

---

# Fail vs Ignore

| Policy | Webhook unavailable |
|---|---|
| `Fail` | Request rejected |
| `Ignore` | Request can continue |

---

# Security Trade-Off

For security-critical policies:

```text
Fail
```

may provide stronger enforcement.

But it also creates an availability dependency.

For example:

```text
Webhook outage
      ↓
All matching Pod creations fail
```

Therefore:

```text
Security
+
Availability
```

must both be considered.

---

# `timeoutSeconds`

Webhooks should respond quickly.

The configuration can specify:

```yaml
timeoutSeconds: 5
```

This limits how long the API Server waits for the webhook.

A very slow webhook can:

```text
Increase API latency
Block deployments
Create cluster-wide operational issues
```

---

# `matchPolicy`

A webhook can specify how API resource matching should behave.

Common values include:

```text
Exact
Equivalent
```

This determines how requests are matched against the webhook's configured resources and API versions.

---

# `namespaceSelector`

A webhook can restrict matching based on namespace labels.

Example concept:

```text
namespaceSelector
```

can target:

```text
environment=production
```

while excluding:

```text
environment=development
```

---

# Why Namespace Selectors Matter

Suppose a security webhook is expensive.

You may want:

```text
Production
 ↓
Webhook

Development
 ↓
No webhook
```

This can reduce unnecessary processing.

---

# `objectSelector`

`objectSelector` can match objects using labels.

Example:

```text
security-scan=true
```

A webhook can target objects matching the selector.

Use selectors carefully because labeling can affect whether a webhook receives an object.

---

# `sideEffects`

Webhook configuration requires declaring whether the webhook has side effects.

A common value for a read-only policy webhook is:

```yaml
sideEffects: None
```

This helps Kubernetes understand webhook behavior.

---

# Admission Webhook Ordering

Multiple admission mechanisms can apply to the same request.

For example:

```text
Mutating Webhook A
Mutating Webhook B
Validating Webhook A
Validating Webhook B
```

Do not build fragile assumptions around webhook ordering.

Policies should be designed to remain correct even when multiple admission controls are involved.

---

# Built-in Admission Controllers

Kubernetes provides built-in admission controllers.

Examples include:

```text
NamespaceLifecycle
ServiceAccount
ResourceQuota
LimitRanger
PodSecurity
DefaultStorageClass
NodeRestriction
```

The exact set enabled by default can vary by Kubernetes version and distribution.

---

# NamespaceLifecycle

This admission control helps enforce namespace lifecycle behavior.

For example:

```text
Terminating Namespace
```

should not accept arbitrary new resources.

---

# ServiceAccount Admission

The ServiceAccount admission controller can help assign a default Service Account to Pods when one is not explicitly specified.

Conceptually:

```text
Pod
 ↓
No serviceAccountName
 ↓
ServiceAccount admission
 ↓
default ServiceAccount
```

---

# ResourceQuota Admission

ResourceQuota helps enforce namespace resource quotas.

Example:

```text
Namespace quota:
10 CPU
20 GiB memory
```

A request that would exceed the quota can be rejected.

---

# LimitRanger

LimitRanger can apply default resource requests/limits and enforce configured limits within a namespace.

Example:

```text
Container without memory limit
       ↓
LimitRange
       ↓
Default memory limit
```

---

# Pod Security Admission

Pod Security Admission enforces the:

```text
Pod Security Standards
```

at the namespace level.

The standards include:

```text
Privileged
Baseline
Restricted
```

---

# Privileged

The:

```text
Privileged
```

profile is intentionally permissive.

It is appropriate only for workloads that genuinely require elevated capabilities.

---

# Baseline

The:

```text
Baseline
```

profile aims to prevent known privilege escalation patterns while remaining practical for many workloads.

---

# Restricted

The:

```text
Restricted
```

profile is the most security-focused standard.

It applies stronger restrictions around:

```text
Privilege
Capabilities
User identity
Security settings
```

---

# Pod Security Labels

Pod Security Admission is commonly configured using namespace labels.

Example:

```yaml
metadata:

  labels:

    pod-security.kubernetes.io/enforce: restricted
```

This tells Kubernetes to enforce the:

```text
restricted
```

Pod Security Standard for that namespace.

---

# Pod Security Modes

Pod Security Admission supports modes such as:

```text
enforce
audit
warn
```

---

# `enforce`

Violating Pods are:

```text
Rejected
```

---

# `audit`

Violations are:

```text
Recorded for auditing
```

without necessarily rejecting the request.

---

# `warn`

Users receive:

```text
Warnings
```

while the request may still be accepted.

---

# Recommended Rollout

For introducing stronger Pod Security:

```text
warn
   ↓
audit
   ↓
enforce
```

This allows teams to discover existing violations before enforcing the policy.

---

# ValidatingAdmissionPolicy

Kubernetes also provides:

```text
ValidatingAdmissionPolicy
```

for declarative admission validation.

It uses:

```text
CEL
```

(Common Expression Language) to express validation logic.

This can avoid creating a separate webhook for some policy requirements.

---

# Why ValidatingAdmissionPolicy?

Traditional model:

```text
API Server
   ↓
External Webhook
   ↓
Custom Application
```

Declarative model:

```text
API Server
   ↓
ValidatingAdmissionPolicy
   ↓
CEL Expression
```

Benefits can include:

```text
Less infrastructure
Simpler deployment
Lower operational overhead
```

---

# Example ValidatingAdmissionPolicy

A simplified example can validate that a Pod contains a required label.

Conceptually:

```yaml
apiVersion: admissionregistration.k8s.io/v1

kind: ValidatingAdmissionPolicy

metadata:

  name: require-team-label

spec:

  matchConstraints:

    resourceRules:

    - apiGroups:

      - ""

      apiVersions:

      - v1

      operations:

      - CREATE

      - UPDATE

      resources:

      - pods

  validations:

  - expression: "has(object.metadata.labels) && has(object.metadata.labels.team)"
```

The exact syntax and API behavior should be validated against the Kubernetes version being used.

---

# ValidatingAdmissionPolicyBinding

A policy must be appropriately bound to determine where and how it is applied.

Conceptually:

```text
ValidatingAdmissionPolicy
          ↓
Policy Binding
          ↓
Matching Resources
```

---

# MutatingAdmissionPolicy

Modern Kubernetes also provides:

```text
MutatingAdmissionPolicy
```

for declarative mutation using supported mechanisms such as CEL expressions and patches.

This can reduce the need for external mutating webhooks for suitable use cases.

---

# Built-in vs Webhook vs Policy

| Mechanism | Typical Use |
|---|---|
| Built-in Admission | Kubernetes platform behavior |
| ValidatingAdmissionPolicy | Declarative validation |
| MutatingAdmissionPolicy | Declarative mutation |
| Validating Webhook | Custom validation |
| Mutating Webhook | Custom mutation |

---

# Admission Controller Example

Imagine an organization requires:

```text
Every Deployment must contain:

team
environment
owner
```

Admission validation can enforce:

```text
No team label
    ↓
Reject
```

while mutation could provide:

```text
Missing environment
    ↓
Add default value
```

---

# Admission Security Policy

A production policy framework may enforce:

```text
Approved image registries
No privileged containers
Required labels
Required resource limits
No hostPath
Non-root containers
Required securityContext
Allowed namespaces
```

---

# Image Security

Admission can enforce approved registries.

Example policy:

```text
Allowed:

registry.company.com/*
```

Reject:

```text
docker.io/*
quay.io/*
```

if those registries are not approved by organizational policy.

---

# Image Tag Policy

An organization may require:

```text
Immutable image references
```

instead of:

```text
latest
```

For example:

```text
nginx:latest
```

may be rejected.

A stronger approach can use:

```text
Image Digest
```

such as:

```text
image@sha256:<digest>
```

---

# Why Image Admission Matters

Without admission enforcement:

```text
Developer
 ↓
Untrusted Image
 ↓
Production
```

With policy:

```text
Developer
 ↓
Image Validation
 ↓
Approved?
 ├── Yes → Continue
 └── No  → Reject
```

---

# Resource Policy

Admission can enforce:

```text
CPU requests
Memory requests
CPU limits
Memory limits
```

Example:

```text
No resource requests
      ↓
Reject
```

This helps prevent workloads from consuming uncontrolled resources.

---

# Namespace Policy

Admission can enforce policies based on:

```text
Namespace
Namespace Labels
Object Labels
```

For example:

```text
production
 ↓
Strict policy

development
 ↓
Relaxed policy
```

---

# Required Labels

Organizations often require:

```text
team
owner
environment
cost-center
application
```

Admission validation can enforce these.

---

# Example

Required:

```yaml
metadata:

  labels:

    app: backend

    team: security

    environment: production
```

Missing:

```text
team
```

can cause:

```text
Admission rejection
```

---

# Custom Admission Controller

A custom admission controller is usually implemented as:

```text
Webhook Service
```

Architecture:

```text
API Server
    │
    ▼
Admission Webhook
    │
    ▼
Custom Policy Engine
    │
    ▼
Allow / Deny / Mutate
```

---

# Admission Webhook Deployment

A production webhook may contain:

```text
Namespace
 ├── Deployment
 │    ├── webhook container
 │    └── webhook container
 │
 ├── Service
 │
 └── TLS configuration
```

Use multiple replicas for availability.

---

# Webhook High Availability

Avoid:

```text
Webhook
  ↓
1 Pod
```

because:

```text
Pod failure
 ↓
Webhook unavailable
 ↓
Admission failure
```

Prefer:

```text
Webhook
 ├── Replica 1
 ├── Replica 2
 └── Replica 3
```

behind a Service.

---

# Webhook Availability

Admission webhooks can become part of the Kubernetes control-plane dependency chain.

Example:

```text
API Server
 ↓
Webhook
 ↓
Webhook unavailable
 ↓
Requests blocked
```

Therefore:

```text
Webhook reliability
=
Cluster operational reliability
```

for policies using:

```text
failurePolicy: Fail
```

---

# Webhook Performance

Admission requests occur on the API Server request path.

A slow webhook can cause:

```text
High API latency
Slow deployments
kubectl delays
Controller delays
Cluster instability
```

Keep admission webhooks:

```text
Fast
Reliable
Stateless where possible
```

---

# Webhook Timeout

Example:

```yaml
timeoutSeconds: 5
```

Avoid unnecessarily large timeouts.

A long timeout means:

```text
Webhook unavailable
 ↓
API request waits longer
```

---

# Webhook Failure Policy

For security-critical validation:

```yaml
failurePolicy: Fail
```

can ensure the policy is not silently bypassed when the webhook is unavailable.

For less critical integrations:

```yaml
failurePolicy: Ignore
```

may be appropriate.

The correct choice depends on:

```text
Security requirement
Availability requirement
Operational risk
```

---

# Admission Security Risks

Admission controllers can create serious security risks if poorly configured.

Potential risks:

```text
Webhook compromise
Certificate compromise
Policy bypass
Excessive privileges
Denial of service
Configuration errors
Infinite mutation loops
Supply-chain compromise
```

---

# Webhook Compromise

If an attacker compromises a mutating webhook:

```text
API Server
   ↓
Compromised Webhook
   ↓
Malicious Mutation
   ↓
Production Objects
```

This can affect many workloads.

Therefore, admission infrastructure must be highly trusted.

---

# Webhook Certificate Security

Protect:

```text
Private Key
CA
Webhook Certificates
```

If an attacker can impersonate the webhook endpoint, they may interfere with admission processing.

---

# Webhook RBAC

The webhook's Service Account should receive only required permissions.

Do not automatically give:

```text
cluster-admin
```

to webhook Pods.

---

# Admission Denial of Service

A badly designed webhook can cause:

```text
Every API request
   ↓
Webhook
   ↓
Slow response
   ↓
API latency
```

This can impact the entire cluster.

---

# Admission Webhook Loop

Mutating webhooks should be designed carefully.

For example:

```text
Webhook A
 ↓
Mutation
 ↓
Webhook B
 ↓
Mutation
 ↓
Webhook A
```

Poorly designed mutation behavior can create repeated processing or unexpected object changes.

---

# Admission Policy Bypass

Potential bypass techniques can involve:

```text
Incorrect selectors
Unmatched resources
Incorrect API groups
Wrong namespaces
Missing subresources
Unexpected object forms
```

Always test policies against realistic workloads.

---

# Security Testing

Admission policies should be tested with:

```text
Valid Object
Invalid Object
Missing Labels
Wrong Image
Privileged Container
HostPath
HostNetwork
Missing Resources
Unexpected Namespace
```

---

# Admission Logging

Monitor:

```text
Admission denials
Webhook errors
Webhook latency
Policy violations
Policy changes
```

This is useful for:

```text
Troubleshooting
Security Monitoring
Compliance
Incident Response
```

---

# Admission and Audit Logs

Audit logs can help answer:

```text
Who submitted the request?
What resource was requested?
Was it allowed?
Which policy rejected it?
When did it happen?
```

Admission logs and Kubernetes audit logs provide complementary visibility.

---

# Admission Troubleshooting

If:

```bash
kubectl apply -f deployment.yaml
```

returns:

```text
denied by admission webhook
```

investigate:

```text
1. Which webhook?
2. Which policy?
3. Which object field violated the policy?
4. Which namespace?
5. Which operation?
6. Is the webhook healthy?
7. Is the policy configuration correct?
```

---

# Check Webhook Configurations

List validating webhooks:

```bash
kubectl get validatingwebhookconfigurations
```

List mutating webhooks:

```bash
kubectl get mutatingwebhookconfigurations
```

---

# Describe Webhook Configuration

```bash
kubectl describe validatingwebhookconfiguration <name>
```

or:

```bash
kubectl describe mutatingwebhookconfiguration <name>
```

---

# Check Webhook Pods

```bash
kubectl get pods -n <webhook-namespace>
```

Check:

```text
Running
Ready
Restarts
```

---

# Check Webhook Logs

```bash
kubectl logs -n <webhook-namespace> \
  deployment/<webhook-deployment>
```

Look for:

```text
Request errors
TLS errors
Timeouts
Policy failures
Application exceptions
```

---

# Check Webhook Service

```bash
kubectl get service -n <webhook-namespace>
```

Verify:

```text
Service exists
Endpoints exist
Ports are correct
```

---

# Check Endpoints

```bash
kubectl get endpoints -n <webhook-namespace>
```

or:

```bash
kubectl get endpointslices -n <webhook-namespace>
```

No endpoints can cause webhook connectivity failures.

---

# TLS Troubleshooting

Potential issues:

```text
Expired certificate
Wrong CA bundle
Hostname mismatch
Incorrect Service name
Certificate rotation failure
```

---

# Admission Failure Troubleshooting Flow

```text
API request denied
      ↓
Is it RBAC?
      ↓
No
      ↓
Admission?
      ↓
Identify webhook/policy
      ↓
Check configuration
      ↓
Check selectors
      ↓
Check webhook health
      ↓
Check TLS
      ↓
Check logs
      ↓
Check failurePolicy
```

---

# Hands-on Lab 1 – Observe Pod Security Admission

Create a test namespace:

```bash
kubectl create namespace admission-lab
```

Apply a Pod Security label:

```bash
kubectl label namespace admission-lab \
  pod-security.kubernetes.io/enforce=restricted
```

Now attempt to deploy a Pod that violates the Restricted profile.

Observe:

```text
Admission rejection
```

---

# Hands-on Lab 2 – Test Pod Security Modes

Experiment with:

```text
warn
audit
enforce
```

For example:

```bash
kubectl label namespace admission-lab \
  pod-security.kubernetes.io/warn=restricted
```

Then test an intentionally non-compliant Pod.

Observe the difference between:

```text
Warning
```

and:

```text
Rejection
```

---

# Hands-on Lab 3 – ValidatingAdmissionPolicy

In a Kubernetes version supporting `ValidatingAdmissionPolicy`, create a test policy that requires a label such as:

```text
team
```

on Pods.

Conceptually:

```text
Pod without team label
       ↓
Policy
       ↓
Rejected
```

Test:

```yaml
metadata:

  name: test-pod
```

and then:

```yaml
metadata:

  name: test-pod

  labels:

    team: security
```

Compare the results.

---

# Hands-on Lab 4 – ResourceQuota

Create:

```bash
kubectl create namespace quota-lab
```

Create a ResourceQuota:

```yaml
apiVersion: v1

kind: ResourceQuota

metadata:

  name: compute-quota

  namespace: quota-lab

spec:

  hard:

    requests.cpu: "1"

    requests.memory: 1Gi

    limits.cpu: "2"

    limits.memory: 2Gi
```

Apply:

```bash
kubectl apply -f quota.yaml
```

Deploy workloads and observe what happens when the quota is exceeded.

---

# Hands-on Lab 5 – LimitRange

Create:

```yaml
apiVersion: v1

kind: LimitRange

metadata:

  name: container-limits

  namespace: quota-lab

spec:

  limits:

  - type: Container

    default:

      cpu: "500m"

      memory: "256Mi"

    defaultRequest:

      cpu: "100m"

      memory: "128Mi"
```

Deploy a container without explicit resource settings.

Observe the resulting Pod specification.

---

# Hands-on Lab 6 – Inspect Webhooks

Run:

```bash
kubectl get validatingwebhookconfigurations
```

Then:

```bash
kubectl get mutatingwebhookconfigurations
```

Identify:

```text
Webhook name
Service
Namespace
Rules
Failure policy
Timeout
Selectors
```

Do not modify production webhook configurations during this exercise.

---

# Hands-on Lab 7 – Admission Failure Simulation

In a disposable cluster, deploy a test webhook.

Configure:

```text
failurePolicy: Fail
```

Then make the webhook unavailable.

Attempt a matching API operation.

Observe:

```text
Webhook unavailable
 ↓
Admission request fails
```

Restore the webhook immediately after the experiment.

---

# Hands-on Lab 8 – Failure Policy Comparison

In a disposable environment, compare:

```text
failurePolicy: Fail
```

and:

```text
failurePolicy: Ignore
```

Observe how webhook availability affects API requests.

---

# Hands-on Lab 9 – Namespace Selector

Create:

```text
production
development
```

Apply different labels.

Configure a test webhook or policy to match only:

```text
environment=production
```

Verify that matching behavior differs between namespaces.

---

# Hands-on Lab 10 – Admission Troubleshooting

Create an intentionally invalid object.

Observe:

```text
kubectl apply
```

failure.

Then identify:

```text
Admission controller
Policy
Reason
Namespace
Object
```

Document the troubleshooting process.

---

# Common Mistakes

## 1. Confusing Authorization and Admission

Remember:

```text
Authorization
=
Can identity perform operation?
```

```text
Admission
=
Should this object/request be accepted?
```

---

## 2. Using `failurePolicy: Ignore` for Critical Security Controls

This can create a policy bypass if the webhook becomes unavailable.

---

## 3. Using `failurePolicy: Fail` Without HA

A single webhook Pod can become a cluster availability dependency.

---

## 4. Slow Webhooks

A slow admission webhook increases API latency.

---

## 5. Incorrect TLS Configuration

Certificate problems can make the API Server unable to communicate with the webhook.

---

## 6. Overly Broad Selectors

A webhook that matches too many resources can unexpectedly affect:

```text
System Components
Controllers
Operators
Infrastructure
```

---

## 7. Incorrect Selectors

A policy can be bypassed if its matching rules are incomplete.

---

## 8. Giving Webhooks Excessive RBAC

A webhook should not automatically receive:

```text
cluster-admin
```

---

## 9. Ignoring Webhook Availability

Admission infrastructure must be monitored like other production control-plane dependencies.

---

## 10. Mutating Objects Unnecessarily

Every mutation adds complexity.

Only mutate when there is a clear reason.

---

## 11. Building Policy That Depends on Webhook Ordering

Admission systems should be designed to avoid fragile dependencies on ordering.

---

## 12. Forgetting Existing Policies

A request may be rejected by:

```text
Pod Security
ValidatingAdmissionPolicy
Webhook
ResourceQuota
LimitRange
```

or another admission mechanism.

---

# Best Practices

### 1. Use Built-In Policies Where Possible

Prefer native Kubernetes mechanisms when they satisfy your requirement.

---

### 2. Use ValidatingAdmissionPolicy for Suitable Declarative Rules

This can reduce external webhook complexity.

---

### 3. Keep Webhooks Fast

Admission is on the API request path.

---

### 4. Make Webhooks Highly Available

Use:

```text
Multiple replicas
Service
Pod anti-affinity where appropriate
PodDisruptionBudget where appropriate
```

---

### 5. Use TLS

Never expose an admission webhook without appropriate secure transport.

---

### 6. Choose `failurePolicy` Carefully

Balance:

```text
Security
+
Availability
```

---

### 7. Restrict Webhook Scope

Use:

```text
namespaceSelector
objectSelector
resourceRules
```

where appropriate.

---

### 8. Minimize Webhook RBAC

Grant only the permissions needed by the webhook.

---

### 9. Monitor Webhook Latency

Track:

```text
Request Count
Latency
Errors
Timeouts
Rejections
```

---

### 10. Test Policy Bypass Scenarios

Test:

```text
Different namespaces
Different API versions
Different resource types
CREATE
UPDATE
DELETE
Subresources
```

---

### 11. Roll Out Policies Gradually

For Pod Security:

```text
warn
 ↓
audit
 ↓
enforce
```

can help teams identify violations before enforcement.

---

### 12. Document Every Security Policy

Record:

```text
Purpose
Scope
Owner
Failure Policy
Expected Impact
Exception Process
```

---

### 13. Protect Admission Infrastructure

Treat admission webhooks as highly trusted security components.

---

# Production Admission Architecture

A mature cluster can look like:

```text
                         API Request
                              │
                              ▼
                        API Server
                              │
                              ▼
                       Authentication
                              │
                              ▼
                        Authorization
                              │
                              ▼
                   ┌──────────┴──────────┐
                   │                     │
                   ▼                     ▼
              Mutating Policies     Validating Policies
                   │                     │
                   ▼                     ▼
             Built-in / Webhook     Built-in / Webhook
                   │                     │
                   └──────────┬──────────┘
                              ▼
                         Final Object
                              │
                              ▼
                          Persistence
```

---

# Defense-in-Depth Architecture

Admission control should not be the only security mechanism.

Use:

```text
Authentication
      ↓
Authorization
      ↓
Admission
      ↓
Pod Security
      ↓
NetworkPolicy
      ↓
Image Security
      ↓
Runtime Security
      ↓
Monitoring
      ↓
Audit
```

---

# Admission Policy Lifecycle

A good policy lifecycle is:

```text
Design
  ↓
Test
  ↓
Warn
  ↓
Audit
  ↓
Enforce
  ↓
Monitor
  ↓
Review
```

---

# Security Policy Example

Requirement:

```text
All production Pods must:

1. Use approved images
2. Run as non-root
3. Have resource requests
4. Have resource limits
5. Include owner label
6. Avoid privileged mode
```

Possible implementation:

```text
Image Policy
     +
Pod Security
     +
LimitRange
     +
ValidatingAdmissionPolicy
     +
Webhook
```

This demonstrates that multiple controls can work together.

---

# Admission and DevSecOps

Admission control moves security enforcement into the cluster.

Traditional:

```text
Developer
 ↓
Deploy
 ↓
Security discovers issue
```

Admission-based:

```text
Developer
 ↓
Deploy
 ↓
Policy
 ↓
Reject insecure object
```

This provides:

```text
Shift-Left Enforcement
```

while still protecting the cluster at runtime.

---

# Admission and CI/CD

CI/CD should ideally validate policies before deployment.

Architecture:

```text
Developer
   ↓
Git
   ↓
CI Security Checks
   ↓
Kubernetes
   ↓
Admission Policies
   ↓
Production
```

This provides multiple enforcement layers.

---

# Admission and GitOps

In GitOps environments:

```text
Git
 ↓
Controller
 ↓
API Server
 ↓
Admission
```

Admission policies still apply.

This means:

```text
GitOps
```

does not automatically bypass:

```text
Admission Control
```

---

# Admission and Multi-Tenancy

Admission controls can enforce tenant boundaries.

Example:

```text
Tenant A
 ↓
Allowed namespaces
 ↓
Allowed images
 ↓
Allowed resources
```

and:

```text
Tenant B
 ↓
Different policies
```

This helps implement organizational governance.

---

# Quick Revision

## Admission Controller

```text
Policy enforcement layer
```

---

## Mutating

```text
Modify request
```

---

## Validating

```text
Accept or reject request
```

---

## Validating Webhook

```text
External validation service
```

---

## Mutating Webhook

```text
External mutation service
```

---

## `failurePolicy`

```text
Fail or Ignore
```

---

## `timeoutSeconds`

```text
Maximum webhook response time
```

---

## `namespaceSelector`

```text
Match namespaces
```

---

## `objectSelector`

```text
Match objects
```

---

## Pod Security Admission

```text
Enforces Pod Security Standards
```

---

## ValidatingAdmissionPolicy

```text
Declarative admission validation
```

---

## MutatingAdmissionPolicy

```text
Declarative admission mutation
```

---

# Essential Commands

List validating webhooks:

```bash
kubectl get validatingwebhookconfigurations
```

List mutating webhooks:

```bash
kubectl get mutatingwebhookconfigurations
```

Describe validating webhook:

```bash
kubectl describe validatingwebhookconfiguration <name>
```

Describe mutating webhook:

```bash
kubectl describe mutatingwebhookconfiguration <name>
```

Check webhook Pods:

```bash
kubectl get pods -n <namespace>
```

Check webhook Service:

```bash
kubectl get svc -n <namespace>
```

Check endpoints:

```bash
kubectl get endpoints -n <namespace>
```

Check EndpointSlices:

```bash
kubectl get endpointslices -n <namespace>
```

View webhook logs:

```bash
kubectl logs -n <namespace> \
  deployment/<deployment>
```

List Pod Security labels:

```bash
kubectl get namespaces --show-labels
```

Check namespace:

```bash
kubectl get namespace <name> -o yaml
```

---

# Interview Questions

## Basic

- What is an Admission Controller?
- What is the purpose of admission control?
- What is the difference between authentication, authorization, and admission?
- What is mutating admission?
- What is validating admission?
- What is an admission webhook?
- What is a validating webhook?
- What is a mutating webhook?
- What is Pod Security Admission?
- What are Pod Security Standards?

---

## Intermediate

- Explain the Kubernetes API request pipeline.
- What is `failurePolicy`?
- What is the difference between `Fail` and `Ignore`?
- What is `namespaceSelector`?
- What is `objectSelector`?
- What is `timeoutSeconds`?
- What is `sideEffects`?
- What is `ValidatingAdmissionPolicy`?
- What is `MutatingAdmissionPolicy`?
- Why is TLS required for admission webhooks?
- Why should admission webhooks be highly available?
- What happens when an admission webhook becomes unavailable?
- What are the `warn`, `audit`, and `enforce` modes of Pod Security Admission?

---

## Advanced

- Explain the complete Kubernetes admission control flow.
- How would you design a highly available admission webhook?
- How would you prevent an admission webhook from becoming a cluster-wide availability risk?
- When would you choose `failurePolicy: Fail`?
- When would you choose `failurePolicy: Ignore`?
- How can admission controllers enforce image security?
- How would you enforce mandatory labels?
- How would you prevent privileged Pods from being deployed?
- How would you enforce resource requests and limits?
- How would you design admission controls for a multi-tenant cluster?
- What security risks are associated with mutating webhooks?
- How can admission webhook selectors accidentally create policy bypasses?
- How would you troubleshoot an admission webhook timeout?
- How would you troubleshoot a TLS failure between the API Server and webhook?
- How can admission policies be integrated into DevSecOps?
- What is the difference between a webhook and `ValidatingAdmissionPolicy`?
- How would you safely roll out a new admission policy in production?

---

# Interview Scenario 1

### Question

> A developer has permission to create Pods but receives an error saying the Pod was rejected by an admission webhook. Is this an RBAC problem?

### Answer

Not necessarily.

RBAC determines:

```text
Can the identity create a Pod?
```

The admission controller determines:

```text
Should this particular Pod be accepted?
```

The flow may be:

```text
Authentication
      ↓
Authorization
      ↓
CREATE Pod = Allowed
      ↓
Admission
      ↓
Security Policy = Violated
      ↓
Rejected
```

Therefore, a user can be authorized to create Pods while still being prevented from creating insecure Pods.

---

# Interview Scenario 2

### Question

> Your validating webhook is down and production deployments are failing. What could cause this?

### Answer

If the webhook uses:

```yaml
failurePolicy: Fail
```

the API Server may reject matching requests when the webhook cannot be reached.

Possible causes include:

```text
Webhook Pod down
Service unavailable
No endpoints
TLS failure
Network connectivity issue
Certificate expiration
Webhook timeout
```

Troubleshooting:

```bash
kubectl get pods -n <namespace>
```

```bash
kubectl get svc -n <namespace>
```

```bash
kubectl get endpoints -n <namespace>
```

```bash
kubectl logs -n <namespace> deployment/<webhook>
```

Then inspect the webhook configuration.

---

# Interview Scenario 3

### Question

> How would you enforce that production Pods cannot use privileged containers?

### Answer

Use:

```text
Pod Security Admission
```

with an appropriate Pod Security Standard, such as:

```text
restricted
```

for namespaces where the workload requirements permit it.

You can also use a validating policy or webhook for additional organization-specific controls.

Architecture:

```text
Pod
 ↓
Admission
 ↓
Pod Security
 ↓
privileged=true
 ↓
Rejected
```

---

# Interview Scenario 4

### Question

> Why can a poorly designed admission webhook become a security and availability problem?

### Answer

Because admission webhooks run on the API request path.

If the webhook is:

```text
Slow
Unavailable
Compromised
Misconfigured
```

it can:

```text
Delay API requests
Reject legitimate workloads
Block deployments
Modify objects maliciously
Create cluster-wide outages
```

Therefore, admission infrastructure must be:

```text
Secure
Fast
Highly Available
Well Tested
Monitored
```

---

# Interview Scenario 5

### Question

> When should you use a mutating admission controller instead of a validating controller?

### Answer

Use mutation when the platform should automatically modify an object.

Example:

```text
Add sidecar
Add default configuration
Inject labels
Add required security settings
```

Use validation when the object should simply be:

```text
Accepted
or
Rejected
```

Example:

```text
Reject privileged containers
Reject unapproved image registries
Reject missing required labels
```

---

# Production Admission Checklist

```text
☑ Understand authentication → authorization → admission
☑ Use Pod Security Admission
☑ Prefer native admission policies where suitable
☑ Keep webhooks highly available
☑ Use TLS
☑ Protect webhook private keys
☑ Use least-privilege RBAC
☑ Configure selectors carefully
☑ Configure timeout appropriately
☑ Choose failurePolicy deliberately
☑ Monitor webhook latency
☑ Monitor webhook errors
☑ Test policy bypasses
☑ Test webhook failure scenarios
☑ Roll out policies gradually
☑ Document exceptions
☑ Audit policy changes
```

---

# Recommended Practice

1. Study the Kubernetes API request pipeline.
2. Understand authentication vs authorization vs admission.
3. Enable Pod Security Admission in a test namespace.
4. Test `warn`.
5. Test `audit`.
6. Test `enforce`.
7. Create an intentionally insecure Pod.
8. Observe admission rejection.
9. Study `ValidatingAdmissionPolicy`.
10. Create a simple label validation policy.
11. Test a valid object.
12. Test an invalid object.
13. Inspect validating webhook configurations.
14. Inspect mutating webhook configurations.
15. Study `failurePolicy`.
16. Study `namespaceSelector`.
17. Study `objectSelector`.
18. Study `timeoutSeconds`.
19. Study webhook TLS.
20. Deploy a test webhook in a disposable cluster.
21. Test webhook failure.
22. Test webhook recovery.
23. Review webhook RBAC.
24. Test admission policy bypass scenarios.
25. Design production admission architecture.
26. Document an admission policy rollout strategy.

---

# References

## Official Kubernetes Documentation

- Admission Control
- Dynamic Admission Control
- Admission Webhooks
- Validating Admission Policy
- Mutating Admission Policy
- Pod Security Admission
- Pod Security Standards
- ResourceQuota
- LimitRange
- Kubernetes API Concepts
- Kubernetes Auditing

---

# Chapter Summary

Admission Controllers provide an important policy enforcement layer in Kubernetes.

The simplified API request pipeline is:

```text
Client
  ↓
Authentication
  ↓
Authorization
  ↓
Admission
  ↓
Persistence
```

Authentication answers:

```text
Who are you?
```

Authorization answers:

```text
Are you allowed to perform this operation?
```

Admission answers:

```text
Should this request/object be accepted?
```

Admission controls can be:

```text
Mutating
```

or:

```text
Validating
```

Mutating admission can modify objects:

```text
Pod
 ↓
Add Sidecar
 ↓
Final Pod
```

Validating admission can reject objects:

```text
Pod
 ↓
privileged=true
 ↓
Reject
```

Kubernetes supports several approaches:

```text
Built-in Admission Controllers
ValidatingAdmissionPolicy
MutatingAdmissionPolicy
Validating Webhooks
Mutating Webhooks
```

Admission webhooks are powerful but introduce operational dependencies.

A production webhook should be:

```text
Secure
Fast
Highly Available
TLS-protected
Least-privileged
Monitored
```

The setting:

```yaml
failurePolicy: Fail
```

provides stronger enforcement when a webhook is unavailable, but can also make the webhook an availability dependency.

The setting:

```yaml
failurePolicy: Ignore
```

improves availability but can allow matching requests to continue without the webhook's decision.

Pod Security Admission provides a native mechanism for enforcing:

```text
Privileged
Baseline
Restricted
```

Pod Security Standards.

The available enforcement modes include:

```text
warn
audit
enforce
```

A gradual rollout can therefore be:

```text
warn
 ↓
audit
 ↓
enforce
```

Admission policies can enforce organizational requirements such as:

```text
Approved Images
Required Labels
Non-Root Containers
No Privileged Containers
Resource Requirements
Security Context
Namespace Policies
```

The key architectural principle is:

> **RBAC controls who can perform an operation; admission control determines whether the requested object or operation satisfies cluster policy.**

A mature Kubernetes security architecture therefore combines:

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
Image Security
       ↓
Runtime Security
       ↓
Monitoring
       ↓
Auditing
```

This creates multiple independent security layers instead of relying on a single control.

---

## Next Chapter

# Chapter 51 – Pod Security Standards

Topics will include:

- What Are Pod Security Standards?
- Why Pod Security Matters
- Pod Security Admission
- Privileged Profile
- Baseline Profile
- Restricted Profile
- Pod Security Levels
- Namespace Labels
- `enforce`
- `audit`
- `warn`
- SecurityContext
- Running as Non-Root
- Linux Capabilities
- Privileged Containers
- Host Networking
- Host PID
- Host IPC
- HostPath
- Seccomp
- AppArmor
- SELinux
- AllowPrivilegeEscalation
- Read-Only Root Filesystem
- Namespace Isolation
- Security Policy Design
- Pod Security Migration
- Production Hardening
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---