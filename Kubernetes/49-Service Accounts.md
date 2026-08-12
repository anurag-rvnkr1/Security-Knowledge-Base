# Chapter 49 – Service Accounts

## Overview

A Kubernetes **Service Account** provides an identity for workloads running inside a cluster.

Human users typically authenticate through mechanisms such as:

```text
OIDC
Client Certificates
External Identity Providers
```

Workloads, however, commonly use:

```text
Service Accounts
```

A simplified architecture is:

```text
                  Kubernetes Cluster
                         │
                         ▼
                  Service Account
                         │
                         ▼
                       Pod
                         │
                         ▼
                Kubernetes API Server
                         │
                         ▼
                       RBAC
                         │
                         ▼
                    Permissions
```

A Service Account answers:

> **Which Kubernetes identity should this workload use?**

It does **not** automatically determine what the workload is allowed to do.

Authorization is controlled separately through:

```text
RBAC
```

---

# Learning Objectives

After completing this chapter, you will understand:

- What Service Accounts are
- Human users vs Service Accounts
- Service Account architecture
- Default Service Account
- Creating Service Accounts
- Assigning Service Accounts to Pods
- Service Account identity
- Service Account tokens
- Bound Service Account tokens
- Projected tokens
- TokenRequest API
- Token expiration
- Token rotation
- Token audience
- `automountServiceAccountToken`
- Service Account RBAC
- Dedicated Service Accounts
- Service Accounts for applications
- Service Accounts for controllers
- Service Accounts for operators
- Service Accounts for CI/CD
- Service Account security
- Service Account token theft
- Workload identity
- Cloud workload identity
- Service Account troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is a Service Account?

A Service Account is a Kubernetes API identity intended primarily for workloads and automation.

For example:

```text
api-sa
```

can represent:

```text
Backend Application
```

The Pod can then authenticate to the Kubernetes API using that identity when required.

---

# Human User vs Service Account

| Identity | Typical Purpose |
|---|---|
| Human User | Developer / Administrator |
| Group | Collection of users |
| Service Account | Application / Workload |
| External Identity | Enterprise authentication |

Example:

```text
Developer
   ↓
OIDC
   ↓
Kubernetes User
```

while:

```text
Application Pod
   ↓
Service Account
   ↓
Kubernetes API
```

---

# Why Service Accounts Exist

Applications sometimes need to interact with Kubernetes.

Examples:

```text
Controllers
Operators
Monitoring Agents
Custom Automation
Deployment Controllers
Kubernetes-aware Applications
```

Instead of giving an application a human administrator's credentials:

```text
Application
     ↓
Human Credentials
```

use:

```text
Application
     ↓
Dedicated Service Account
```

This provides a clearer security boundary.

---

# Service Account Architecture

```text
                    Pod
                     │
                     ▼
              Service Account
                     │
                     ▼
               Authentication
                     │
                     ▼
                API Server
                     │
                     ▼
                   RBAC
                     │
                     ▼
                API Resource
```

The responsibilities are separated:

```text
Service Account
=
Identity
```

```text
RBAC
=
Authorization
```

---

# Service Account Identity

A Service Account identity commonly has the format:

```text
system:serviceaccount:<namespace>:<name>
```

Example:

```text
system:serviceaccount:production:backend-sa
```

Breakdown:

```text
system:serviceaccount
        │
        ├── namespace = production
        │
        └── name = backend-sa
```

---

# Creating a Service Account

Using `kubectl`:

```bash
kubectl create serviceaccount backend-sa
```

Check it:

```bash
kubectl get serviceaccount backend-sa
```

---

# YAML Definition

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: backend-sa

  namespace: default
```

Apply:

```bash
kubectl apply -f serviceaccount.yaml
```

---

# List Service Accounts

```bash
kubectl get serviceaccounts
```

or:

```bash
kubectl get sa
```

Across all namespaces:

```bash
kubectl get serviceaccounts -A
```

---

# Describe Service Account

```bash
kubectl describe serviceaccount backend-sa
```

This can show information associated with the Service Account.

---

# Default Service Account

Every namespace has a:

```text
default
```

Service Account.

Check:

```bash
kubectl get serviceaccount
```

Example:

```text
NAME      SECRETS   AGE
default   0         10d
```

Modern Kubernetes versions do not generally create long-lived Secret-based Service Account tokens automatically merely because a Service Account exists.

---

# Default Service Account Usage

If a Pod does not specify:

```yaml
serviceAccountName:
```

it generally uses:

```text
default
```

in its namespace.

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: demo

spec:

  containers:

  - name: app

    image: nginx:1.30
```

This Pod uses:

```text
default ServiceAccount
```

unless another identity is configured.

---

# Why Avoid Default Service Account for Applications?

Using the default identity for unrelated applications makes identity management less precise.

Better:

```text
Frontend
 ↓
frontend-sa

Backend
 ↓
backend-sa

Controller
 ↓
controller-sa
```

This allows each workload to receive different permissions.

---

# Assign Service Account to a Pod

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: backend

spec:

  serviceAccountName: backend-sa

  containers:

  - name: app

    image: nginx:1.30
```

Apply:

```bash
kubectl apply -f backend.yaml
```

---

# Verify Service Account

Run:

```bash
kubectl get pod backend -o yaml
```

Look for:

```yaml
serviceAccountName: backend-sa
```

---

# Service Account and Deployment

For a Deployment:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: backend

spec:

  replicas: 2

  selector:

    matchLabels:

      app: backend

  template:

    metadata:

      labels:

        app: backend

    spec:

      serviceAccountName: backend-sa

      containers:

      - name: backend

        image: example/backend:1.0
```

All Pods created by this Deployment use:

```text
backend-sa
```

---

# Service Account Tokens

A workload may need a credential to authenticate to the Kubernetes API.

Modern Kubernetes uses mechanisms based on:

```text
TokenRequest API
+
Projected Volumes
```

for short-lived Service Account tokens.

Conceptually:

```text
ServiceAccount
      │
      ▼
TokenRequest
      │
      ▼
Short-Lived Token
      │
      ▼
Projected Volume
      │
      ▼
Container
```

---

# Bound Service Account Tokens

Modern Service Account tokens can be:

```text
Short-lived
Audience-bound
Bound to workload-related objects
```

This reduces the risk associated with indefinitely valid credentials.

---

# TokenRequest API

Kubernetes provides:

```text
TokenRequest API
```

for obtaining Service Account tokens.

A token can contain information such as:

```text
Audience
Expiration
Binding information
```

---

# Token Audience

The audience identifies the intended recipient of a token.

Conceptually:

```text
Token
   │
   └── Audience = Kubernetes API
```

A token intended for one service should not automatically be trusted by an unrelated service.

---

# Token Expiration

Modern Service Account tokens are designed to be short-lived.

Conceptually:

```text
Token Issued
     ↓
Valid
     ↓
Expiration
     ↓
No Longer Valid
```

Short-lived credentials reduce the window in which a stolen credential can be abused.

---

# Token Rotation

Projected Service Account tokens can be refreshed as they approach expiration.

Conceptually:

```text
Token A
   ↓
Near Expiration
   ↓
Refresh
   ↓
Token B
```

Applications should avoid assuming that a token remains valid forever.

---

# Projected Service Account Token

A Pod can receive a Service Account token through a projected volume.

Conceptually:

```text
Pod
 │
 └── projected volume
          │
          └── token
```

The application reads the token from the filesystem.

---

# Example Projected Token Configuration

A simplified example:

```yaml
volumes:

- name: token

  projected:

    sources:

    - serviceAccountToken:

        path: token

        expirationSeconds: 3600

        audience: https://kubernetes.default.svc
```

The token can then be mounted into the container.

---

# Token Security

Treat Service Account tokens as:

```text
Sensitive Credentials
```

Do not:

```text
Commit them to Git
Print them in logs
Embed them into images
Share them publicly
Store them in ConfigMaps
```

---

# `automountServiceAccountToken`

By default, Kubernetes may make Service Account credentials available to Pods depending on configuration.

If an application does not need Kubernetes API access, disable automatic mounting:

```yaml
automountServiceAccountToken: false
```

---

# Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: frontend

spec:

  automountServiceAccountToken: false

  containers:

  - name: frontend

    image: nginx:1.30
```

This is a useful security hardening measure for workloads that do not need Kubernetes API credentials.

---

# Pod-Level vs ServiceAccount-Level Configuration

You can specify:

```yaml
automountServiceAccountToken: false
```

on the Pod.

You can also configure it on the Service Account:

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: frontend-sa

automountServiceAccountToken: false
```

A Pod-level setting can explicitly control the behavior for that workload.

---

# When Should You Use a Service Account Token?

A workload may need Kubernetes API credentials if it must:

```text
Read Pods
Watch Deployments
Create resources
Update resources
Read cluster state
Manage custom resources
```

Examples:

```text
Operator
Controller
Kubernetes Agent
Custom Scheduler
Automation Controller
```

---

# When Should You Not Use a Service Account Token?

A normal application such as:

```text
Frontend Web Server
```

often does not need to access:

```text
Kubernetes API
```

In such cases:

```yaml
automountServiceAccountToken: false
```

can reduce credential exposure.

---

# Service Account + RBAC

A Service Account only establishes identity.

RBAC grants permissions.

Example:

```text
backend-sa
     ↓
RoleBinding
     ↓
backend-reader Role
     ↓
get ConfigMaps
```

Without the RoleBinding:

```text
Identity exists
```

but:

```text
No additional permissions
```

---

# Example RBAC

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: config-reader

  namespace: production

rules:

- apiGroups:

  - ""

  resources:

  - configmaps

  verbs:

  - get
```

Bind it:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: RoleBinding

metadata:

  name: backend-config-reader

  namespace: production

subjects:

- kind: ServiceAccount

  name: backend-sa

  namespace: production

roleRef:

  kind: Role

  name: config-reader

  apiGroup: rbac.authorization.k8s.io
```

---

# Effective Architecture

```text
Backend Pod
    │
    ▼
backend-sa
    │
    ▼
RoleBinding
    │
    ▼
config-reader Role
    │
    ▼
get ConfigMaps
    │
    ▼
production namespace
```

---

# Least Privilege

The Service Account should receive:

```text
Only required permissions
```

Bad:

```text
backend-sa
     ↓
cluster-admin
```

Better:

```text
backend-sa
     ↓
Role
     ↓
get ConfigMaps
```

---

# Dedicated Service Accounts

A dedicated Service Account gives workloads distinct identities.

Example:

```text
frontend-sa
backend-sa
worker-sa
monitoring-sa
```

Benefits:

```text
Better auditing
Better RBAC
Smaller blast radius
Clear ownership
Easier credential isolation
```

---

# Service Accounts for Applications

Example:

```text
Application
    ↓
backend-sa
    ↓
get ConfigMaps
```

Only grant the permissions required by the application.

---

# Service Accounts for Controllers

Controllers often need to:

```text
Watch resources
Create resources
Update resources
Delete resources
```

They should use:

```text
Dedicated ServiceAccount
+
Dedicated RBAC
```

---

# Service Accounts for Operators

Operators can require significant privileges because they manage Kubernetes resources.

Architecture:

```text
Operator
   ↓
operator-sa
   ↓
ClusterRole
   ↓
ClusterRoleBinding
```

Review these permissions carefully.

---

# Service Accounts for CI/CD

A CI/CD pipeline can use a dedicated identity:

```text
CI/CD
  ↓
ci-deployer-sa
  ↓
Role
  ↓
production
```

Avoid:

```text
CI/CD
  ↓
cluster-admin
```

unless an exceptional and well-justified requirement exists.

---

# Service Accounts for Monitoring

A monitoring agent may need:

```text
get Pods
get Nodes
watch resources
```

Use a dedicated identity:

```text
monitoring-sa
```

rather than a general administrative identity.

---

# Service Account for Security Tools

Security agents may need additional permissions for:

```text
Pod discovery
Node metadata
Events
Security configuration
```

These should still be reviewed using least privilege.

---

# Workload Identity

Workload identity is a broader concept:

```text
Workload
   ↓
Identity
   ↓
Access to external resources
```

A Kubernetes Service Account can sometimes be mapped to a cloud identity.

Conceptually:

```text
Kubernetes ServiceAccount
           ↓
Cloud Workload Identity
           ↓
Cloud IAM Identity
           ↓
Cloud Resource
```

---

# Why Workload Identity Matters

Without workload identity, applications may use static cloud credentials:

```text
Access Key
Secret Key
```

stored in:

```text
Secret
```

A stronger architecture can provide temporary identity-based access.

```text
Pod
 ↓
Kubernetes ServiceAccount
 ↓
Cloud Identity
 ↓
Temporary Credentials
 ↓
Cloud Resource
```

Exact implementation varies by cloud provider.

---

# Kubernetes Service Account vs Cloud Identity

These are related but not identical.

```text
Kubernetes Service Account
=
Kubernetes workload identity
```

```text
Cloud Workload Identity
=
Mapping workload identity to cloud IAM
```

The exact integration depends on the cloud platform.

---

# Service Account Token Theft

If an attacker compromises a Pod and obtains its Service Account credential:

```text
Compromised Pod
      ↓
Token Theft
      ↓
Kubernetes API
      ↓
RBAC Permissions
```

The attacker's access is limited by:

```text
RBAC
```

Therefore:

```text
Least-Privilege RBAC
```

is an important defense against token theft.

---

# Reducing Token Theft Impact

Use:

```text
Dedicated Service Accounts
```

```text
Least-Privilege RBAC
```

```text
Short-Lived Tokens
```

```text
automountServiceAccountToken: false
```

when API access is unnecessary.

Also use:

```text
NetworkPolicy
Pod Security
Runtime Security
Audit Logging
```

---

# Service Account Token Attack Path

```text
Application Vulnerability
       ↓
Container Compromise
       ↓
Service Account Credential
       ↓
Kubernetes API
       ↓
RBAC Evaluation
       ↓
Limited / Broad Access
```

The strongest control at the authorization stage is:

```text
Least Privilege
```

---

# Service Account Security Architecture

```text
                    Workload
                       │
                       ▼
                Service Account
                       │
                       ▼
                Short-Lived Token
                       │
                       ▼
                  Kubernetes API
                       │
                       ▼
                      RBAC
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Allowed             Denied
              │
              ▼
          API Resource
```

---

# Service Account Namespace Scope

Service Accounts are namespace-scoped.

Example:

```text
production/backend-sa
```

is different from:

```text
development/backend-sa
```

Even if the names are identical.

---

# Same Name, Different Namespace

```text
production
 └── backend-sa

development
 └── backend-sa
```

These are separate Service Accounts.

---

# Service Account and Pod Namespace

A Pod generally uses a Service Account from its own namespace.

For example:

```text
Pod:
production/backend

ServiceAccount:
production/backend-sa
```

---

# Service Account and Deployment

The Service Account is configured in:

```text
spec.template.spec
```

Example:

```yaml
spec:

  template:

    spec:

      serviceAccountName: backend-sa
```

This is important because changing:

```text
Pod template
```

can result in new Pods being created with the updated identity.

---

# Service Account and Jobs

A Job can also specify:

```yaml
spec:

  template:

    spec:

      serviceAccountName: job-sa
```

This is useful for automation workloads.

---

# Service Account and CronJobs

CronJobs can specify the Service Account in their Pod template:

```yaml
spec:

  jobTemplate:

    spec:

      template:

        spec:

          serviceAccountName: backup-sa
```

Use a dedicated identity for scheduled automation.

---

# Service Account and Init Containers

Init Containers share the Pod's identity configuration.

If the Pod uses:

```yaml
serviceAccountName: app-sa
```

the containers in that Pod operate under the Pod's configured Service Account identity.

---

# Service Account and Sidecars

Sidecars also run within the same Pod.

Therefore, identity configuration should be considered at the Pod level.

Avoid unnecessarily giving a sidecar access to Kubernetes API credentials.

---

# Service Account and Multi-Container Pods

All containers in a Pod share the Pod's Service Account identity.

This is an important security consideration.

Example:

```text
Pod
 ├── app
 ├── sidecar
 └── logging
       │
       ▼
   Same ServiceAccount
```

If one container can access the credential, it may potentially act using the Pod's identity.

---

# Important Security Principle

Do not assume:

```text
Container A
```

and:

```text
Container B
```

inside the same Pod have separate Kubernetes identities.

They share the Pod's identity configuration.

---

# Service Account Token File

Applications using projected Service Account credentials can typically access the token from the mounted filesystem location configured by Kubernetes.

A common path in Kubernetes Pods is:

```text
/var/run/secrets/kubernetes.io/serviceaccount/
```

However, applications should rely on the configured credential mechanism rather than hard-coding assumptions where possible.

---

# Inspect Service Account Files

Inside a test Pod:

```bash
kubectl exec -it <pod> -- ls \
  /var/run/secrets/kubernetes.io/serviceaccount/
```

You may see files such as:

```text
token
ca.crt
namespace
```

depending on the Pod configuration.

---

# Important Warning

Do not print Service Account tokens during normal testing.

Avoid:

```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

in shared environments because this exposes a credential.

If you must inspect token behavior in a controlled lab, protect the output and immediately clean up.

---

# Service Account CA Certificate

The projected Service Account volume may also contain:

```text
ca.crt
```

which can help clients verify the Kubernetes API server certificate.

---

# Service Account Namespace File

The projected volume can also expose:

```text
namespace
```

which identifies the Pod's namespace.

---

# Service Account Token Security Layers

Protect Service Account credentials through:

```text
1. Short Lifetime
2. Audience Restrictions
3. RBAC
4. Pod Security
5. NetworkPolicy
6. Runtime Monitoring
7. Audit Logging
```

---

# Service Account Troubleshooting

## Check Service Account

```bash
kubectl get serviceaccount
```

---

# Check Pod Service Account

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.serviceAccountName}'
```

---

# Describe Pod

```bash
kubectl describe pod <pod>
```

Look for:

```text
Service Account
```

---

# Check RBAC

```bash
kubectl auth can-i --list \
  --as=system:serviceaccount:default:app-sa
```

---

# Check Specific Permission

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:app-sa
```

---

# Check Secret Access

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:default:app-sa
```

Expected for a least-privilege application:

```text
no
```

unless Secret access is genuinely required.

---

# Check API Connectivity

From a test Pod that is intentionally configured to access the API:

```bash
kubectl exec -it <pod> -- sh
```

Then inspect the application's configured Kubernetes API endpoint and authentication mechanism.

Do not expose the token.

---

# Service Account Authentication Failure

Possible causes:

```text
Wrong Service Account
Missing token
Token expired
Incorrect audience
RBAC denial
API endpoint issue
NetworkPolicy
TLS configuration
```

---

# RBAC vs Service Account Problem

Suppose:

```text
Pod cannot get ConfigMaps
```

Check:

```text
1. Which Service Account?
2. Is a token available?
3. Is the token valid?
4. Is RBAC configured?
5. Does RoleBinding reference the correct Service Account?
6. Is the namespace correct?
7. Does the Role contain get permission?
```

---

# Hands-on Lab 1 – Create Service Account

Create:

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: app-sa

  namespace: default
```

Apply:

```bash
kubectl apply -f app-sa.yaml
```

Verify:

```bash
kubectl get serviceaccount app-sa
```

---

# Hands-on Lab 2 – Assign Service Account to Pod

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: sa-demo

spec:

  serviceAccountName: app-sa

  containers:

  - name: app

    image: nginx:1.30
```

Apply:

```bash
kubectl apply -f sa-demo.yaml
```

Verify:

```bash
kubectl get pod sa-demo -o yaml
```

---

# Hands-on Lab 3 – Inspect Identity

Run:

```bash
kubectl get pod sa-demo \
  -o jsonpath='{.spec.serviceAccountName}'
```

Expected:

```text
app-sa
```

---

# Hands-on Lab 4 – Create Role

Create:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: pod-reader

  namespace: default

rules:

- apiGroups:

  - ""

  resources:

  - pods

  verbs:

  - get

  - list

  - watch
```

---

# Hands-on Lab 5 – Bind Service Account

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: RoleBinding

metadata:

  name: app-sa-reader

  namespace: default

subjects:

- kind: ServiceAccount

  name: app-sa

  namespace: default

roleRef:

  kind: Role

  name: pod-reader

  apiGroup: rbac.authorization.k8s.io
```

Apply:

```bash
kubectl apply -f rolebinding.yaml
```

---

# Hands-on Lab 6 – Test Permissions

Run:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:app-sa
```

Expected:

```text
yes
```

Test:

```bash
kubectl auth can-i delete pods \
  --as=system:serviceaccount:default:app-sa
```

Expected:

```text
no
```

---

# Hands-on Lab 7 – Disable Token Mounting

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: no-token-demo

spec:

  serviceAccountName: app-sa

  automountServiceAccountToken: false

  containers:

  - name: app

    image: nginx:1.30
```

Apply:

```bash
kubectl apply -f no-token-demo.yaml
```

Inspect:

```bash
kubectl get pod no-token-demo -o yaml
```

Observe:

```text
automountServiceAccountToken: false
```

---

# Hands-on Lab 8 – Compare Pods

Compare:

```text
sa-demo
```

with:

```text
no-token-demo
```

Inspect:

```bash
kubectl exec -it sa-demo -- ls \
  /var/run/secrets/kubernetes.io/serviceaccount/
```

Then:

```bash
kubectl exec -it no-token-demo -- ls \
  /var/run/secrets/kubernetes.io/serviceaccount/
```

The credential projection behavior should differ based on the configuration.

---

# Hands-on Lab 9 – Test Service Account Scope

Create:

```text
namespace-a
namespace-b
```

Create:

```text
app-sa
```

in:

```text
namespace-a
```

Then verify that the same Service Account identity does not exist in:

```text
namespace-b
```

Service Accounts are namespace-scoped.

---

# Hands-on Lab 10 – Test RBAC Blast Radius

Give:

```text
app-sa
```

only:

```text
get ConfigMaps
```

Then test:

```bash
kubectl auth can-i get configmaps \
  --as=system:serviceaccount:default:app-sa
```

and:

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:default:app-sa
```

The expected result should demonstrate least privilege.

---

# Hands-on Lab 11 – Service Account for a Deployment

Create:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: backend

spec:

  replicas: 2

  selector:

    matchLabels:

      app: backend

  template:

    metadata:

      labels:

        app: backend

    spec:

      serviceAccountName: app-sa

      containers:

      - name: backend

        image: nginx:1.30
```

Verify:

```bash
kubectl get pods
```

Then inspect one Pod:

```bash
kubectl get pod <pod-name> \
  -o jsonpath='{.spec.serviceAccountName}'
```

---

# Hands-on Lab 12 – Service Account for a Job

Create:

```yaml
apiVersion: batch/v1

kind: Job

metadata:

  name: api-job

spec:

  template:

    spec:

      serviceAccountName: app-sa

      restartPolicy: Never

      containers:

      - name: job

        image: busybox:1.36

        command:

        - sh

        - -c

        - echo "Service Account lab"
```

Observe the Job's Pod configuration.

---

# Hands-on Lab 13 – Service Account Security Review

For each Service Account, answer:

```text
1. Who uses it?
2. Which namespace?
3. Which Pods use it?
4. What RBAC permissions does it have?
5. Does it access Secrets?
6. Does it access the Kubernetes API?
7. Does it need a token?
8. Does it have cluster-wide permissions?
```

This is a useful production security review exercise.

---

# Common Mistakes

## 1. Using the Default Service Account Everywhere

Avoid using:

```text
default
```

for unrelated workloads when dedicated identities are more appropriate.

---

## 2. Giving `cluster-admin`

Avoid:

```text
ServiceAccount
 ↓
cluster-admin
```

unless there is a strong, documented requirement.

---

## 3. Mounting Tokens Unnecessarily

If the application does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

---

## 4. Sharing Service Accounts

Avoid:

```text
Frontend
Backend
Worker
   ↓
same highly privileged ServiceAccount
```

Prefer separate identities where different permissions are required.

---

## 5. Exposing Tokens

Never log:

```text
Service Account token
```

---

## 6. Putting Tokens in Git

Never commit:

```text
Token
Private Key
Credential
```

---

## 7. Ignoring RBAC

Creating a Service Account does not automatically grant application-specific permissions.

---

## 8. Forgetting Namespace Scope

These are different:

```text
production/app-sa
```

and:

```text
development/app-sa
```

---

## 9. Giving Sidecars Unnecessary Access

All containers in a Pod share the Pod's Service Account identity.

---

## 10. Assuming Tokens Are Permanent

Modern Service Account credentials are designed around short-lived, renewable tokens.

---

# Best Practices

### 1. Use Dedicated Service Accounts

Create workload-specific identities.

---

### 2. Follow Least Privilege

Grant only the permissions required.

---

### 3. Disable Token Mounting When Unnecessary

```yaml
automountServiceAccountToken: false
```

---

### 4. Use Short-Lived Tokens

Prefer modern bound Service Account token mechanisms.

---

### 5. Restrict Token Audience

Use appropriate audience values for tokens where supported.

---

### 6. Avoid Long-Lived Static Credentials

Do not create unnecessary permanent credentials.

---

### 7. Audit Service Account Permissions

Regularly inspect:

```text
RoleBindings
ClusterRoleBindings
```

---

### 8. Protect Service Account Tokens

Treat them as credentials.

---

### 9. Separate Workloads

Use separate identities when workloads have different privilege requirements.

---

### 10. Combine Service Account Security with Pod Security

Use:

```text
Non-root
Seccomp
Capability dropping
NetworkPolicy
RBAC
Runtime monitoring
```

---

### 11. Use Workload Identity for Cloud Access

Where supported, prefer temporary identity-based cloud access over static cloud credentials.

---

### 12. Monitor API Usage

Track:

```text
Service Account
API operation
Resource
Time
Result
```

through appropriate auditing and monitoring.

---

# Service Account Security Checklist

```text
☑ Dedicated Service Account
☑ Least-privilege RBAC
☑ No unnecessary cluster-wide access
☑ No unnecessary Secret access
☑ Disable token mounting where unnecessary
☑ Short-lived tokens
☑ Appropriate token audience
☑ Protect credentials
☑ Audit API activity
☑ Monitor unusual activity
☑ Review permissions regularly
☑ Avoid sharing privileged identities
```

---

# Service Account Architecture

A secure application architecture:

```text
                    Application
                         │
                         ▼
                  Dedicated SA
                         │
                         ▼
                Short-Lived Token
                         │
                         ▼
                   Kubernetes API
                         │
                         ▼
                    Least RBAC
                         │
                         ▼
                 Required Resource
```

For an application that does not need API access:

```text
                    Application
                         │
                         ▼
                  Dedicated SA
                         │
                         ▼
              Token Mount Disabled
                         │
                         ▼
                No Kubernetes API
```

---

# Service Account Threat Model

Potential threats include:

```text
Token Theft
Excessive RBAC
Credential Leakage
Compromised Pod
Compromised Sidecar
Malicious Image
API Abuse
Cloud Credential Abuse
```

Defenses:

```text
Least Privilege
Short-Lived Tokens
Token Audience
RBAC
Pod Security
NetworkPolicy
Runtime Security
Audit Logs
Workload Identity
```

---

# Attack Scenario

Suppose:

```text
backend Pod
```

is compromised.

The attacker discovers:

```text
Service Account token
```

The attacker tries:

```text
GET /api/v1/secrets
```

RBAC checks:

```text
Does backend-sa have get secrets?
```

If:

```text
No
```

the request is denied.

Architecture:

```text
Compromised Pod
      ↓
Token
      ↓
API Server
      ↓
Authentication
      ↓
backend-sa
      ↓
RBAC
      ↓
No Secret Permission
      ↓
DENIED
```

This demonstrates why:

> **Service Account security and RBAC must be designed together.**

---

# Advanced Security Consideration

A compromised Service Account with:

```text
pods/exec
```

or powerful workload-management permissions may be significantly more dangerous than one with simple read-only permissions.

Therefore, permissions should be evaluated not only by:

```text
Number of permissions
```

but also by:

```text
Privilege escalation potential
```

---

# Service Account and Pod Security

Service Account security is only one layer.

A secure workload should combine:

```text
Service Account
+
RBAC
+
Pod Security
+
NetworkPolicy
+
Image Security
+
Runtime Security
```

---

# Service Account and NetworkPolicy

RBAC controls:

```text
Kubernetes API access
```

NetworkPolicy controls:

```text
Network communication
```

They solve different problems.

Example:

```text
RBAC
 ↓
Can access Kubernetes API?

NetworkPolicy
 ↓
Can communicate with destination?
```

Use both where appropriate.

---

# Service Account and Runtime Security

Runtime security can detect suspicious behavior such as:

```text
Unexpected API calls
Shell execution
Credential access
Privilege escalation
Suspicious processes
```

This adds another defense layer.

---

# Service Account and Audit Logging

Audit logs can help identify:

```text
Which Service Account
performed which API action
at what time
against which resource
```

This is valuable during incident response.

---

# Quick Revision

## Service Account

```text
Workload identity
```

---

## Default Service Account

```text
Namespace default identity
```

---

## Service Account Identity

```text
system:serviceaccount:<namespace>:<name>
```

---

## Service Account Token

```text
Credential used for Kubernetes API authentication
```

---

## TokenRequest

```text
Mechanism for obtaining Service Account tokens
```

---

## Projected Token

```text
Credential provided through a projected volume
```

---

## Token Audience

```text
Intended recipient of a token
```

---

## Token Expiration

```text
Limits credential lifetime
```

---

## `automountServiceAccountToken`

```text
Controls automatic token projection
```

---

## RBAC

```text
Controls Service Account permissions
```

---

## Workload Identity

```text
Maps workload identity to external resource permissions
```

---

# Essential Commands

Create Service Account:

```bash
kubectl create serviceaccount app-sa
```

List Service Accounts:

```bash
kubectl get serviceaccounts
```

List across namespaces:

```bash
kubectl get serviceaccounts -A
```

Describe:

```bash
kubectl describe serviceaccount app-sa
```

Find Pod Service Account:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.serviceAccountName}'
```

Check permissions:

```bash
kubectl auth can-i --list \
  --as=system:serviceaccount:default:app-sa
```

Check specific permission:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:app-sa
```

Check Secret access:

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:default:app-sa
```

List RoleBindings:

```bash
kubectl get rolebindings -A
```

List ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

Inspect Pod:

```bash
kubectl get pod <pod> -o yaml
```

---

# Interview Questions

## Basic

- What is a Service Account?
- Why are Service Accounts used?
- How are Service Accounts different from users?
- What is the default Service Account?
- How do you create a Service Account?
- How do you assign a Service Account to a Pod?
- What is a Service Account token?
- What is `automountServiceAccountToken`?

---

## Intermediate

- How does a Service Account authenticate to the Kubernetes API?
- What is the TokenRequest API?
- What are projected Service Account tokens?
- What is a bound Service Account token?
- Why should tokens be short-lived?
- What is token audience?
- How does RBAC work with Service Accounts?
- Why should applications use dedicated Service Accounts?
- How can you disable automatic Service Account token mounting?
- What is the difference between a Service Account and a cloud workload identity?

---

## Advanced

- Explain the complete Service Account authentication flow.
- How would you secure Service Accounts in production?
- How would you reduce the impact of a stolen Service Account token?
- How would you design Service Accounts for a multi-tenant cluster?
- How would you secure Service Accounts used by CI/CD?
- How would you secure an Operator's Service Account?
- Why is `pods/exec` dangerous for a Service Account?
- How would you identify Service Accounts with excessive privileges?
- How would you investigate suspicious Service Account API activity?
- How do projected tokens improve Service Account security?
- How does token audience reduce credential misuse?
- How would you combine Service Account security with NetworkPolicy?
- How does cloud workload identity improve security?
- How would you respond if a Service Account token was suspected to be compromised?

---

# Interview Scenario 1

### Question

> A frontend application does not communicate with the Kubernetes API. Should it have a Service Account token mounted?

### Answer

There is generally no need for the frontend to receive Kubernetes API credentials.

Use:

```yaml
automountServiceAccountToken: false
```

This reduces credential exposure.

The architecture becomes:

```text
Frontend
   ↓
No Kubernetes API Credential
   ↓
Reduced Attack Surface
```

---

# Interview Scenario 2

### Question

> A backend application needs to read one ConfigMap. How would you configure access?

### Answer

Create:

```text
Dedicated ServiceAccount
```

Then create:

```text
Role
```

with:

```text
get ConfigMap
```

and bind it using:

```text
RoleBinding
```

Architecture:

```text
backend
 ↓
backend-sa
 ↓
Role
 ↓
get ConfigMap
 ↓
RoleBinding
 ↓
production
```

Do not grant:

```text
cluster-admin
```

or:

```text
get secrets
```

unless required.

---

# Interview Scenario 3

### Question

> A Pod is compromised and the attacker obtains its Service Account token. What determines how much access the attacker has?

### Answer

The attacker's effective access is determined primarily by the permissions granted to that Service Account through:

```text
RBAC
```

Other controls can further limit impact:

```text
NetworkPolicy
Pod Security
Runtime Security
Token lifetime
Token audience
Audit Monitoring
```

Therefore:

```text
Token Theft
      ↓
Service Account Identity
      ↓
RBAC
      ↓
Limited Permissions
```

---

# Interview Scenario 4

### Question

> Why should different applications use different Service Accounts?

### Answer

Because separate identities provide:

```text
Least Privilege
Isolation
Better Auditing
Smaller Blast Radius
Clear Ownership
```

For example:

```text
Frontend → frontend-sa
Backend  → backend-sa
Worker   → worker-sa
```

If the backend is compromised, the attacker does not automatically inherit permissions intended for the worker.

---

# Interview Scenario 5

### Question

> How would you secure a Service Account used by a CI/CD pipeline?

### Answer

Use:

```text
Dedicated identity
+
Short-lived credentials
+
Least-privilege RBAC
+
Namespace-scoped permissions
+
No unnecessary Secret access
+
No cluster-admin
+
Audit logging
```

Where the platform supports it, use workload or cloud identity mechanisms instead of long-lived static credentials.

---

# Production Service Account Checklist

```text
☑ Dedicated Service Account
☑ No unnecessary default identity
☑ Least-privilege RBAC
☑ Namespace-scoped permissions where possible
☑ Short-lived tokens
☑ Appropriate token audience
☑ Disable token mounting when unnecessary
☑ No unnecessary Secret access
☑ No unnecessary pods/exec
☑ No cluster-admin
☑ Audit API activity
☑ Monitor suspicious behavior
☑ Protect credentials
☑ Use workload identity where appropriate
☑ Periodically review permissions
```

---

# Recommended Practice

1. Create a dedicated Service Account.
2. Assign it to a Pod.
3. Inspect the Pod configuration.
4. Identify the Service Account identity.
5. Create a least-privilege Role.
6. Bind the Role to the Service Account.
7. Test permissions using `kubectl auth can-i`.
8. Test an allowed operation.
9. Test a denied operation.
10. Disable automatic token mounting for a workload that does not need API access.
11. Compare token projection behavior.
12. Study TokenRequest.
13. Study token expiration.
14. Study token audience.
15. Study projected Service Account tokens.
16. Create Service Accounts for Jobs and Deployments.
17. Design separate identities for frontend and backend.
18. Audit Service Account permissions.
19. Identify Service Accounts with cluster-wide access.
20. Study workload identity for cloud resources.
21. Practice a stolen-token threat scenario.
22. Design a defense-in-depth strategy for Service Account compromise.

---

# References

## Official Kubernetes Documentation

- Service Accounts
- Configure Service Accounts for Pods
- Authentication
- TokenRequest API
- Projected Volumes
- Bound Service Account Tokens
- RBAC Authorization
- Kubernetes API Authentication
- Workload Identity Concepts

---

# Chapter Summary

A Service Account is a Kubernetes identity intended primarily for:

```text
Workloads
Automation
Controllers
Operators
Agents
```

The key distinction is:

```text
Service Account
=
Identity
```

while:

```text
RBAC
=
Authorization
```

The architecture is:

```text
Pod
 ↓
Service Account
 ↓
Authentication
 ↓
API Server
 ↓
RBAC
 ↓
Permissions
```

Every namespace has a:

```text
default
```

Service Account.

However, production workloads should generally use:

```text
Dedicated Service Accounts
```

when different applications require different permissions.

Modern Kubernetes uses short-lived Service Account tokens through mechanisms such as:

```text
TokenRequest API
Projected Volumes
```

These tokens can be:

```text
Short-lived
Audience-bound
Workload-bound
```

which reduces the risks associated with long-lived credentials.

If a workload does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

can reduce unnecessary credential exposure.

A compromised Pod may attempt to steal its Service Account credential:

```text
Pod Compromise
      ↓
Token Theft
      ↓
API Request
      ↓
Service Account Identity
      ↓
RBAC
```

Therefore, the impact depends heavily on:

```text
RBAC Permissions
```

The most important security principle is:

> **A Service Account should have only the permissions required for the workload it represents.**

For stronger security, combine:

```text
Dedicated Service Accounts
+
Least-Privilege RBAC
+
Short-Lived Tokens
+
Token Audience
+
Pod Security
+
NetworkPolicy
+
Runtime Security
+
Audit Logging
```

For cloud environments, workload identity can extend this model:

```text
Kubernetes ServiceAccount
        ↓
Workload Identity
        ↓
Cloud IAM
        ↓
Cloud Resource
```

This can eliminate unnecessary long-lived cloud credentials stored inside workloads.

The final security model is:

```text
                    Workload
                       │
                       ▼
               Dedicated Identity
                       │
                       ▼
                Short-Lived Token
                       │
                       ▼
                 Kubernetes API
                       │
                       ▼
                      RBAC
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              Allowed      Denied
                 │
                 ▼
             Resource
```

The central principle to remember is:

> **Service Accounts identify workloads; RBAC determines what those workloads can do.**

---

## Next Chapter

# Chapter 50 – Admission Controllers

Topics will include:

- What Are Admission Controllers?
- Why Admission Control Is Needed
- Kubernetes API Request Pipeline
- Authentication vs Authorization vs Admission
- Mutating Admission
- Validating Admission
- Built-in Admission Controllers
- ValidatingAdmissionPolicy
- MutatingAdmissionPolicy
- Admission Webhooks
- Validating Webhooks
- Mutating Webhooks
- Pod Security Admission
- Security Policy Enforcement
- Image Policy
- Resource Policy
- Namespace Policy
- Custom Admission Controllers
- Admission Webhook Architecture
- Webhook TLS
- Failure Policies
- `failurePolicy`
- `matchPolicy`
- `namespaceSelector`
- `objectSelector`
- `sideEffects`
- `timeoutSeconds`
- Admission Ordering
- Security Risks
- Webhook Security
- Availability Risks
- Admission Controller Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---