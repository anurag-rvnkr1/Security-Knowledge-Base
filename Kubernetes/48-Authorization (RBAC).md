# Chapter 48 – Authorization (RBAC)

## Overview

Authentication answers:

```text
Who are you?
```

Authorization answers:

```text
What are you allowed to do?
```

In Kubernetes, authorization determines whether an authenticated identity can perform an operation against a Kubernetes API resource.

One of the most widely used authorization mechanisms is:

```text
RBAC
```

RBAC stands for:

> **Role-Based Access Control**

The basic model is:

```text
Identity
   ↓
Role / ClusterRole
   ↓
RoleBinding / ClusterRoleBinding
   ↓
Permissions
```

For example:

```text
Developer
   ↓
Role
   ↓
get/list/watch Pods
   ↓
RoleBinding
   ↓
Namespace: development
```

The developer can work with Pods in that namespace without automatically receiving cluster-wide administrative privileges.

---

# Learning Objectives

After completing this chapter, you will understand:

- What authorization means
- Authentication vs authorization
- RBAC fundamentals
- RBAC objects
- Role
- ClusterRole
- RoleBinding
- ClusterRoleBinding
- Subjects
- Users
- Groups
- Service Accounts
- Resources
- Verbs
- API Groups
- Resource Names
- Namespace-scoped permissions
- Cluster-scoped permissions
- Role aggregation
- Default Roles
- `cluster-admin`
- Least privilege
- RBAC design patterns
- RBAC for applications
- RBAC for developers
- RBAC for CI/CD
- RBAC for security teams
- RBAC auditing
- `kubectl auth can-i`
- RBAC troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is Authorization?

Authorization is the process of determining whether an authenticated identity is permitted to perform an action.

Example:

```text
Authentication
      ↓
Identity = Alice
      ↓
Authorization
      ↓
Can Alice delete Pods?
      ↓
No
```

The API Server rejects the request.

---

# Authentication vs Authorization

| Concept | Question | Example |
|---|---|---|
| Authentication | Who are you? | Alice |
| Authorization | What can you do? | Alice can read Pods |

A complete request requires both.

```text
Client
  ↓
Authentication
  ↓
Identity
  ↓
Authorization
  ↓
Allowed / Denied
```

---

# Kubernetes Authorization

Kubernetes supports multiple authorization mechanisms.

Common approaches include:

```text
RBAC
Node authorization
Webhook authorization
ABAC in some configurations/legacy environments
```

RBAC is the standard authorization mechanism used in most modern Kubernetes environments.

---

# What Is RBAC?

RBAC allows permissions to be assigned based on roles.

Instead of saying:

```text
Alice can get Pods
Bob can get Pods
Charlie can get Pods
```

define:

```text
Developer Role
```

with:

```text
get Pods
list Pods
watch Pods
```

Then bind users or groups to that role.

```text
Developer Group
      ↓
Developer Role
      ↓
Pod Read Permissions
```

---

# RBAC Architecture

```text
                    Subject
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
         User        Group    ServiceAccount
          │            │            │
          └────────────┼────────────┘
                       ▼
                   Binding
                       │
              ┌────────┴────────┐
              ▼                 ▼
            Role           ClusterRole
              │                 │
              └────────┬────────┘
                       ▼
                  Permissions
```

---

# Four Main RBAC Objects

The four core RBAC resources are:

```text
Role
ClusterRole
RoleBinding
ClusterRoleBinding
```

Remember:

```text
Role
=
Permissions

ClusterRole
=
Permissions

RoleBinding
=
Connects Subject → Role

ClusterRoleBinding
=
Connects Subject → ClusterRole
```

---

# Role

A `Role` defines permissions within a namespace.

Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: pod-reader

  namespace: development

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

This Role allows:

```text
get Pods
list Pods
watch Pods
```

inside:

```text
development
```

---

# Role Is Namespace-Scoped

A Role belongs to a namespace.

Example:

```text
Role:
pod-reader

Namespace:
development
```

The Role does not automatically provide permissions in:

```text
production
```

or:

```text
staging
```

---

# ClusterRole

A `ClusterRole` is a cluster-level RBAC object.

It can define permissions for:

```text
Cluster-scoped resources
```

and can also be used with namespaced resources.

Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRole

metadata:

  name: pod-reader

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

# Role vs ClusterRole

| Feature | Role | ClusterRole |
|---|---|---|
| Namespace-scoped object | Yes | No |
| Cluster-scoped resources | No | Yes |
| Can define Pod permissions | Yes | Yes |
| Can be used by RoleBinding | Yes | Yes |
| Can be used by ClusterRoleBinding | No | Yes |

---

# RoleBinding

A `RoleBinding` grants permissions defined by a Role or ClusterRole to subjects.

Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: RoleBinding

metadata:

  name: pod-reader-binding

  namespace: development

subjects:

- kind: User

  name: alice

  apiGroup: rbac.authorization.k8s.io

roleRef:

  kind: Role

  name: pod-reader

  apiGroup: rbac.authorization.k8s.io
```

This means:

```text
Alice
 ↓
RoleBinding
 ↓
pod-reader Role
 ↓
Pod read permissions
 ↓
development namespace
```

---

# RoleBinding with ClusterRole

A RoleBinding can reference a ClusterRole.

Example:

```yaml
roleRef:

  kind: ClusterRole

  name: pod-reader

  apiGroup: rbac.authorization.k8s.io
```

Even though the referenced role is a ClusterRole, the RoleBinding limits the granted permissions to the RoleBinding's namespace.

This is a very useful RBAC pattern.

---

# ClusterRoleBinding

A `ClusterRoleBinding` grants a ClusterRole across the cluster.

Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRoleBinding

metadata:

  name: cluster-pod-reader

subjects:

- kind: User

  name: alice

  apiGroup: rbac.authorization.k8s.io

roleRef:

  kind: ClusterRole

  name: pod-reader

  apiGroup: rbac.authorization.k8s.io
```

Now Alice receives the ClusterRole's permissions cluster-wide, subject to the resources and verbs defined in that ClusterRole.

---

# RoleBinding vs ClusterRoleBinding

This distinction is extremely important.

```text
RoleBinding
=
Namespace-scoped grant
```

```text
ClusterRoleBinding
=
Cluster-wide grant
```

Example:

```text
RoleBinding
Alice → Pod Reader → development
```

versus:

```text
ClusterRoleBinding
Alice → Pod Reader → all applicable namespaces
```

---

# Subjects

A RoleBinding or ClusterRoleBinding can grant permissions to subjects.

Subjects can be:

```text
User
Group
ServiceAccount
```

---

# User

Example:

```yaml
subjects:

- kind: User

  name: alice

  apiGroup: rbac.authorization.k8s.io
```

The username must match the identity presented during authentication.

---

# Group

Example:

```yaml
subjects:

- kind: Group

  name: developers

  apiGroup: rbac.authorization.k8s.io
```

All authenticated identities belonging to the group can receive the permissions.

This is particularly useful with:

```text
OIDC
```

---

# ServiceAccount

Example:

```yaml
subjects:

- kind: ServiceAccount

  name: api-sa

  namespace: production
```

This grants permissions to the workload identity.

---

# Service Account Identity

A Service Account commonly has the identity:

```text
system:serviceaccount:production:api-sa
```

RBAC can bind permissions to this identity.

---

# RBAC Rules

An RBAC rule typically contains:

```text
apiGroups
resources
verbs
```

Optionally:

```text
resourceNames
nonResourceURLs
```

---

# API Groups

Kubernetes APIs are organized into API groups.

Core API resources use:

```text
""
```

Example:

```yaml
apiGroups:
- ""
```

Core resources include:

```text
pods
services
configmaps
secrets
nodes
```

---

# Apps API Group

Deployments are in:

```text
apps
```

Example:

```yaml
apiGroups:

- apps

resources:

- deployments
```

---

# RBAC API Group

RBAC resources belong to:

```text
rbac.authorization.k8s.io
```

---

# Networking API Group

NetworkPolicy belongs to:

```text
networking.k8s.io
```

---

# Batch API Group

Jobs and CronJobs use:

```text
batch
```

---

# Resource

The `resources` field identifies what the identity can access.

Example:

```yaml
resources:

- pods
```

Other examples:

```text
deployments
services
configmaps
secrets
jobs
cronjobs
nodes
namespaces
```

---

# Resource Names

RBAC can restrict permissions to specific resource names.

Example:

```yaml
resourceNames:

- application-config
```

This can restrict a rule to a particular named resource.

---

# Example

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: specific-secret-reader

rules:

- apiGroups:

  - ""

  resources:

  - secrets

  resourceNames:

  - app-secret

  verbs:

  - get
```

This grants `get` permission specifically for:

```text
app-secret
```

rather than all Secrets in the namespace.

---

# Important Limitation

When using `resourceNames`, certain operations that don't identify a specific resource name, such as some list/watch requests, may not match the rule as expected.

For example:

```bash
kubectl get secrets
```

does not specify a resource name.

Where appropriate, use:

```bash
kubectl get secret app-secret
```

---

# Verbs

Verbs define allowed actions.

Common Kubernetes API verbs include:

```text
get
list
watch
create
update
patch
delete
deletecollection
```

---

# Read Permissions

Common read verbs:

```text
get
list
watch
```

Example:

```yaml
verbs:

- get

- list

- watch
```

---

# Write Permissions

Common write verbs:

```text
create
update
patch
delete
```

---

# Wildcards

RBAC supports wildcards.

Example:

```yaml
verbs:

- "*"
```

or:

```yaml
resources:

- "*"
```

This is powerful and dangerous.

Avoid wildcards unless the broad access is explicitly required.

---

# Example of Overly Broad RBAC

```yaml
rules:

- apiGroups:

  - "*"

  resources:

  - "*"

  verbs:

  - "*"
```

This effectively grants extremely broad access.

Do not use this for ordinary applications.

---

# Least Privilege

The preferred approach is:

```text
Minimum Resources
+
Minimum Verbs
+
Minimum Scope
```

For example:

```text
Application
 ↓
get ConfigMaps
 ↓
production namespace
```

instead of:

```text
Application
 ↓
cluster-admin
```

---

# RBAC Permission Model

Think of permissions as:

```text
WHO
 ↓
CAN DO WHAT
 ↓
TO WHICH RESOURCE
 ↓
WHERE
```

Example:

```text
Alice
 ↓
get/list/watch
 ↓
Pods
 ↓
development namespace
```

---

# Namespace Scope

A RoleBinding in:

```text
development
```

does not grant the same Role to the subject in:

```text
production
```

You need another binding if the permissions are required there.

---

# Multi-Namespace Access

Suppose a developer needs:

```text
development
staging
```

but not:

```text
production
```

One approach is:

```text
RoleBinding
 ↓
development

RoleBinding
 ↓
staging
```

The same ClusterRole can be reused through multiple RoleBindings.

---

# Reusable ClusterRole

A ClusterRole can define reusable permissions:

```text
read-workloads
```

Then namespace-specific RoleBindings can attach it:

```text
read-workloads
      │
 ┌────┴─────┐
 ▼          ▼
dev       staging
```

This avoids duplicating the same permission rules.

---

# Cluster-Scoped Resources

Some resources are cluster-scoped.

Examples include:

```text
Nodes
Namespaces
PersistentVolumes
ClusterRoles
ClusterRoleBindings
```

These cannot be accessed through a normal namespace-scoped Role.

---

# ClusterRole for Nodes

Example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRole

metadata:

  name: node-reader

rules:

- apiGroups:

  - ""

  resources:

  - nodes

  verbs:

  - get

  - list

  - watch
```

Nodes are cluster-scoped.

---

# ClusterRoleBinding for Nodes

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRoleBinding

metadata:

  name: node-reader-binding

subjects:

- kind: Group

  name: infrastructure-team

  apiGroup: rbac.authorization.k8s.io

roleRef:

  kind: ClusterRole

  name: node-reader

  apiGroup: rbac.authorization.k8s.io
```

---

# Default Kubernetes Roles

Kubernetes provides several default ClusterRoles.

Examples include:

```text
cluster-admin
admin
edit
view
```

These have different privilege levels.

---

# `cluster-admin`

The:

```text
cluster-admin
```

ClusterRole provides extremely broad administrative privileges.

Treat access to it as highly sensitive.

---

# `admin`

The:

```text
admin
```

role provides broad administrative permissions within namespaces when granted through appropriate namespace-scoped bindings.

---

# `edit`

The:

```text
edit
```

role provides permissions to manage many resources within a namespace.

---

# `view`

The:

```text
view
```

role provides read-only access to many resources.

---

# Default Roles Are Not Always Enough

Built-in roles are useful, but production environments often require custom roles.

Example:

```text
Application:
Only read one ConfigMap
```

A custom Role is more appropriate than:

```text
edit
```

---

# Role Aggregation

Kubernetes supports aggregation labels that can add rules to built-in aggregated ClusterRoles.

For example, additional rules can be aggregated into roles such as:

```text
view
edit
admin
```

This can be useful for extending standard roles carefully.

---

# Example Aggregation

Conceptually:

```yaml
metadata:

  labels:

    rbac.authorization.k8s.io/aggregate-to-view: "true"
```

This allows the rules in the ClusterRole to be aggregated into the standard `view` role.

Use aggregation carefully because it changes the permissions of a built-in role.

---

# RBAC for Developers

A developer may need:

```text
get Pods
list Pods
watch Pods
get Deployments
list Deployments
watch Deployments
```

but should not necessarily have:

```text
delete Nodes
create ClusterRoleBindings
get all Secrets
```

---

# Example Developer Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: developer-read

  namespace: development

rules:

- apiGroups:

  - ""

  resources:

  - pods

  - services

  verbs:

  - get

  - list

  - watch

- apiGroups:

  - apps

  resources:

  - deployments

  verbs:

  - get

  - list

  - watch
```

---

# RBAC for Applications

An application should receive only the permissions required for its function.

Example:

```text
Controller
 ↓
Watch Deployments
 ↓
Update ConfigMaps
```

Do not grant:

```text
cluster-admin
```

just because the application interacts with Kubernetes.

---

# Example Application Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: app-reader

  namespace: production

rules:

- apiGroups:

  - ""

  resources:

  - configmaps

  verbs:

  - get
```

---

# RBAC for CI/CD

A CI/CD system may need:

```text
get deployments
create deployments
update deployments
get pods
```

But it may not need:

```text
delete nodes
modify ClusterRoleBindings
read all Secrets
```

Use a dedicated identity.

---

# CI/CD Security

Bad:

```text
CI/CD
 ↓
cluster-admin
```

Better:

```text
CI/CD
 ↓
Dedicated ServiceAccount / External Identity
 ↓
Deployment Role
 ↓
Specific namespace
```

---

# RBAC for Security Teams

Security teams may need:

```text
get Pods
get Events
get NetworkPolicies
get RBAC objects
get Audit information
```

But security analysts should not automatically receive:

```text
cluster-admin
```

if read-only access is sufficient.

---

# RBAC for Monitoring

Monitoring agents may require:

```text
get Nodes
get Pods
get Services
get Endpoints
watch resources
```

They should receive only the permissions necessary for discovery and monitoring.

---

# RBAC for Operators

Operators and controllers may need broad permissions because they manage Kubernetes resources.

However:

```text
Operator permissions
```

should still be explicitly reviewed.

A controller requiring cluster-wide access should have:

```text
Dedicated ServiceAccount
Dedicated ClusterRole
Dedicated ClusterRoleBinding
```

---

# RBAC and Secrets

Secrets require special care.

A Role such as:

```yaml
resources:

- secrets

verbs:

- get
```

can expose sensitive credentials.

Avoid giving:

```text
get secrets
```

unless necessary.

---

# RBAC and ConfigMaps

ConfigMaps are usually less sensitive than Secrets, but they can still contain:

```text
Configuration
Endpoints
Feature Flags
Internal Information
```

Follow least privilege for them as well.

---

# RBAC and Nodes

Node permissions are highly sensitive.

For example:

```text
get nodes
```

is generally read-only.

But permissions to modify certain cluster resources can significantly increase privilege.

---

# Dangerous RBAC Permissions

Pay special attention to permissions involving:

```text
secrets
pods/exec
pods/attach
pods/portforward
nodes
roles
rolebindings
clusterroles
clusterrolebindings
serviceaccounts
```

Some of these can provide paths to sensitive access or privilege escalation depending on the surrounding configuration.

---

# `pods/exec`

The:

```text
pods/exec
```

subresource allows command execution inside containers.

Permission to use it can effectively provide shell-level access to application workloads.

Treat it as sensitive.

---

# RBAC Subresources

Some Kubernetes resources have subresources.

Examples:

```text
pods/exec
pods/log
pods/status
deployments/status
```

Permissions may need to explicitly reference the subresource.

---

# Example

```yaml
resources:

- pods/log

verbs:

- get
```

This can allow reading Pod logs.

---

# Pod Logs vs Pod Exec

```text
pods/log
```

means:

```text
Read logs
```

while:

```text
pods/exec
```

means:

```text
Execute commands
```

These should not be treated as equivalent privileges.

---

# RBAC Evaluation

When Kubernetes evaluates a request, it considers:

```text
Authenticated Identity
+
Groups
+
Roles
+
Bindings
+
Requested Resource
+
Requested Verb
+
Namespace
```

If an applicable RBAC rule allows the request:

```text
Allowed
```

Otherwise:

```text
Denied
```

---

# RBAC Is Additive

A key concept:

> **RBAC permissions are additive.**

If an identity receives:

```text
Role A
+
Role B
```

the resulting permissions are the union of the permissions granted by both.

There is no RBAC rule that says:

```text
Allow everything except X
```

in the normal RBAC model.

---

# Example

Role A:

```text
get pods
```

Role B:

```text
delete pods
```

Effective permissions:

```text
get pods
delete pods
```

You cannot create a third RBAC rule saying:

```text
Allow all except delete pods
```

to override the granted permission.

---

# RBAC Cannot Explicitly Deny

Kubernetes RBAC is primarily:

```text
Allow-based
```

There is no standard:

```text
deny rule
```

that overrides another RBAC allow.

Therefore:

```text
Least privilege
```

is extremely important.

---

# Effective Permissions

Suppose Alice has:

```text
Role A:
view

Role B:
edit
```

Her effective permissions may become broader than expected.

Therefore, when troubleshooting RBAC:

```text
Look at ALL bindings
```

not just one Role.

---

# RBAC Auditing

Regularly review:

```text
ClusterRoleBindings
RoleBindings
Service Accounts
Privileged Roles
```

Look for:

```text
cluster-admin
wildcards
Secret access
pods/exec
broad ClusterRoleBindings
```

---

# Find ClusterRoleBindings

```bash
kubectl get clusterrolebindings
```

Describe:

```bash
kubectl describe clusterrolebinding <name>
```

---

# Find RoleBindings

```bash
kubectl get rolebindings -A
```

This is useful for organization-wide review.

---

# Find Roles

```bash
kubectl get roles -A
```

---

# Find ClusterRoles

```bash
kubectl get clusterroles
```

---

# Check a User's Permissions

Use:

```bash
kubectl auth can-i --list
```

This shows the permissions available to the current identity, subject to the API server's authorization configuration.

---

# Check Another Identity

For testing:

```bash
kubectl auth can-i --list \
  --as=alice
```

Or:

```bash
kubectl auth can-i get pods \
  --as=alice \
  -n development
```

Use impersonation only when your own identity has permission to impersonate the requested user or group.

---

# Check Service Account Permissions

```bash
kubectl auth can-i --list \
  --as=system:serviceaccount:production:api-sa
```

---

# RBAC Troubleshooting

Suppose:

```bash
kubectl get pods
```

returns:

```text
Forbidden
```

Use:

```bash
kubectl auth whoami
```

Then:

```bash
kubectl auth can-i get pods
```

If:

```text
no
```

inspect:

```text
RoleBindings
ClusterRoleBindings
Roles
ClusterRoles
```

---

# Troubleshooting Workflow

```text
403 Forbidden
      ↓
Who am I?
      ↓
kubectl auth whoami
      ↓
What am I allowed to do?
      ↓
kubectl auth can-i
      ↓
Which Role grants permission?
      ↓
Check RoleBindings
      ↓
Check namespace
      ↓
Check resource/API group
      ↓
Check verb
```

---

# Common RBAC Error

Suppose the Role contains:

```yaml
apiGroups:

- apps

resources:

- deployments
```

but you request:

```text
pods
```

The permission will not match.

---

# API Group Mistake

Core resources use:

```yaml
apiGroups:

- ""
```

Deployment:

```yaml
apiGroups:

- apps
```

Job:

```yaml
apiGroups:

- batch
```

NetworkPolicy:

```yaml
apiGroups:

- networking.k8s.io
```

---

# Verb Mistake

Suppose the Role grants:

```yaml
verbs:

- get
```

but the user runs:

```bash
kubectl delete pod app
```

The request will be denied.

---

# Namespace Mistake

Suppose a RoleBinding exists in:

```text
development
```

but the user requests:

```bash
kubectl get pods -n production
```

The permission does not automatically transfer to production.

---

# RoleBinding Subject Mistake

Verify:

```text
kind
name
namespace
```

For Service Accounts, the namespace is important.

Example:

```yaml
subjects:

- kind: ServiceAccount

  name: api-sa

  namespace: production
```

---

# RoleRef Mistake

A RoleBinding contains:

```yaml
roleRef:
```

Verify:

```text
kind
name
apiGroup
```

The referenced RBAC object must exist and be correct.

---

# Hands-on Lab 1 – Create Read-Only Role

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

Apply:

```bash
kubectl apply -f pod-reader.yaml
```

---

# Hands-on Lab 2 – Create Service Account

```bash
kubectl create serviceaccount rbac-demo
```

Check:

```bash
kubectl get serviceaccount rbac-demo
```

---

# Hands-on Lab 3 – Create RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: RoleBinding

metadata:

  name: pod-reader-binding

subjects:

- kind: ServiceAccount

  name: rbac-demo

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

# Hands-on Lab 4 – Test Permissions

Run:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:rbac-demo
```

Expected:

```text
yes
```

Test:

```bash
kubectl auth can-i delete pods \
  --as=system:serviceaccount:default:rbac-demo
```

Expected:

```text
no
```

---

# Hands-on Lab 5 – Create Namespace-Scoped Access

Create:

```bash
kubectl create namespace rbac-lab
```

Create:

```text
Role
RoleBinding
ServiceAccount
```

inside:

```text
rbac-lab
```

Grant:

```text
get/list/watch Pods
```

Test:

```bash
kubectl auth can-i get pods \
  -n rbac-lab \
  --as=system:serviceaccount:rbac-lab:rbac-demo
```

---

# Hands-on Lab 6 – Test Namespace Isolation

Test another namespace:

```bash
kubectl auth can-i get pods \
  -n default \
  --as=system:serviceaccount:rbac-lab:rbac-demo
```

The result should demonstrate that a namespace-scoped RoleBinding does not automatically grant permissions elsewhere.

---

# Hands-on Lab 7 – ClusterRole + RoleBinding

Create a ClusterRole:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRole

metadata:

  name: pod-reader-global-definition

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

Create a RoleBinding in a specific namespace that references this ClusterRole.

Observe that:

```text
ClusterRole
+
RoleBinding
=
Namespace-scoped permission
```

---

# Hands-on Lab 8 – ClusterRoleBinding

Create a test ClusterRole and ClusterRoleBinding.

Then verify:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:rbac-demo \
  -n default
```

and compare access in another namespace.

Understand:

```text
ClusterRole
+
ClusterRoleBinding
=
Cluster-wide grant
```

---

# Hands-on Lab 9 – Test Resource Names

Create:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: specific-config-reader

rules:

- apiGroups:

  - ""

  resources:

  - configmaps

  resourceNames:

  - app-config

  verbs:

  - get
```

Test:

```bash
kubectl auth can-i get configmap app-config
```

Then:

```bash
kubectl auth can-i get configmap another-config
```

Compare the results.

---

# Hands-on Lab 10 – Test `pods/log`

Create a Role:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: log-reader

rules:

- apiGroups:

  - ""

  resources:

  - pods/log

  verbs:

  - get
```

Test:

```bash
kubectl auth can-i get pods/log
```

Understand that:

```text
pods/log
```

is different from:

```text
pods
```

---

# Hands-on Lab 11 – Test `pods/exec`

Create a test Role that explicitly grants:

```text
pods/exec
```

Then use:

```bash
kubectl auth can-i create pods/exec
```

Observe that `pods/exec` is a sensitive permission because it can provide command execution inside containers.

Remove the permission after the exercise.

---

# Hands-on Lab 12 – RBAC Audit

List all ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

Look for:

```text
cluster-admin
```

Inspect:

```bash
kubectl describe clusterrolebinding <name>
```

Identify:

```text
Subject
Role
Scope
```

---

# Hands-on Lab 13 – Find Broad Permissions

Inspect:

```bash
kubectl get clusterroles -o yaml
```

Look for:

```yaml
verbs:

- "*"
```

and:

```yaml
resources:

- "*"
```

Identify overly broad custom roles in a test environment.

---

# Common Mistakes

## 1. Giving `cluster-admin` to Applications

Avoid:

```text
Application
 ↓
cluster-admin
```

---

## 2. Using Wildcards

Avoid:

```yaml
resources:
- "*"

verbs:
- "*"
```

unless explicitly justified.

---

## 3. Confusing Role and RoleBinding

Remember:

```text
Role
=
Defines permissions
```

```text
RoleBinding
=
Grants those permissions
```

---

## 4. Confusing ClusterRole and ClusterRoleBinding

A ClusterRole defines permissions.

A ClusterRoleBinding grants them cluster-wide.

---

## 5. Forgetting Namespace Scope

A RoleBinding in:

```text
development
```

does not automatically grant access in:

```text
production
```

---

## 6. Granting Secret Access Unnecessarily

Secrets contain sensitive information.

Avoid broad:

```text
get secrets
```

permissions.

---

## 7. Granting `pods/exec`

`pods/exec` can provide interactive command execution and should be treated as sensitive.

---

## 8. Ignoring Existing Bindings

RBAC permissions are additive.

A user may receive permissions from multiple bindings.

---

## 9. Using the Wrong API Group

For example:

```text
Deployments
```

use:

```text
apps
```

not:

```text
""
```

---

## 10. Using the Wrong Verb

`get` does not imply:

```text
delete
```

---

## 11. Assuming RBAC Has Deny Rules

RBAC is allow-oriented and does not provide a normal deny override.

---

## 12. Forgetting Service Account Namespace

For Service Accounts, ensure the binding references the correct namespace.

---

# Best Practices

### 1. Follow Least Privilege

Grant only:

```text
Required Resource
+
Required Verb
+
Required Namespace
```

---

### 2. Prefer Role Over ClusterRole When Possible

If access only needs to exist inside one namespace:

```text
Role
```

is usually simpler.

---

### 3. Prefer RoleBinding Over ClusterRoleBinding When Possible

A namespace-scoped grant reduces blast radius.

---

### 4. Use Groups for Human Users

Instead of binding dozens of individual users:

```text
developers
 ↓
Role
```

---

### 5. Use Dedicated Service Accounts

One workload or workload class should have an appropriate identity.

---

### 6. Avoid Wildcards

Explicit permissions are easier to audit.

---

### 7. Protect Secrets

Grant Secret access only to workloads that require it.

---

### 8. Review Privileged RBAC Regularly

Audit:

```text
cluster-admin
pods/exec
secrets
RBAC modifications
Node access
```

---

### 9. Use `kubectl auth can-i`

Before assuming a permission exists:

```bash
kubectl auth can-i ...
```

---

### 10. Monitor RBAC Changes

Security-sensitive changes include:

```text
RoleBinding creation
ClusterRoleBinding creation
Role modification
ClusterRole modification
```

---

### 11. Separate Human and Workload Identities

Do not share administrative credentials with applications.

---

### 12. Keep Production Access Narrow

A developer who needs:

```text
development
```

does not automatically need:

```text
production
```

---

# RBAC Design Pattern

A clean production model can be:

```text
                    Identity Provider
                           │
                           ▼
                       Groups
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          developers    sre-team    security-team
              │            │            │
              ▼            ▼            ▼
         RoleBinding   RoleBinding   RoleBinding
              │            │            │
              ▼            ▼            ▼
          Namespace     Namespace      Cluster
          Permissions   Permissions    Read Access
```

---

# Application RBAC Pattern

```text
Application
     │
     ▼
Dedicated ServiceAccount
     │
     ▼
Role
     │
     ▼
RoleBinding
     │
     ▼
Required Namespace Resources
```

This is preferable to:

```text
Application
     │
     ▼
cluster-admin
```

---

# CI/CD RBAC Pattern

```text
CI/CD System
     │
     ▼
Dedicated Identity
     │
     ▼
Deployment Role
     │
     ▼
RoleBinding
     │
     ▼
Application Namespace
```

Example permissions:

```text
get deployments
create deployments
update deployments
get pods
```

Avoid unrelated permissions.

---

# Security Team RBAC Pattern

```text
Security Analyst
      │
      ▼
security-team
      │
      ▼
Read-only ClusterRole
      │
      ▼
ClusterRoleBinding
```

Potential permissions:

```text
get Pods
get Nodes
get Events
get NetworkPolicies
get RBAC objects
```

The exact permissions should match operational requirements.

---

# RBAC Review Strategy

A periodic RBAC review can follow:

```text
1. List all ClusterRoleBindings
2. Identify cluster-admin access
3. Identify wildcard permissions
4. Identify Secret access
5. Identify pods/exec access
6. Identify Service Accounts with broad access
7. Review unused permissions
8. Remove unnecessary bindings
9. Test effective access
10. Document exceptions
```

---

# RBAC Security Architecture

```text
                    Authentication
                          │
                          ▼
                       Identity
                          │
                          ▼
                    Group Membership
                          │
                          ▼
                    RBAC Evaluation
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
         Role        ClusterRole     Bindings
           │              │              │
           └──────────────┼──────────────┘
                          ▼
                    Effective Access
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
              Allowed            Denied
```

---

# Quick Revision

## RBAC

```text
Role-Based Access Control
```

---

## Role

```text
Namespace-scoped permission definition
```

---

## ClusterRole

```text
Cluster-level permission definition
```

---

## RoleBinding

```text
Grants a Role or ClusterRole within a namespace
```

---

## ClusterRoleBinding

```text
Grants a ClusterRole cluster-wide
```

---

## Subject

```text
User
Group
ServiceAccount
```

---

## Resource

```text
Pods
Deployments
Services
Secrets
Jobs
...
```

---

## Verb

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

## API Group

```text
apps
batch
networking.k8s.io
rbac.authorization.k8s.io
```

---

## Least Privilege

```text
Only the permissions required
```

---

## RBAC Is Additive

```text
Role A
+
Role B
=
Combined Permissions
```

---

## No Normal Deny Rule

```text
RBAC
=
Allow-oriented
```

---

# Essential Commands

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

Describe Role:

```bash
kubectl describe role <name>
```

Describe ClusterRole:

```bash
kubectl describe clusterrole <name>
```

Describe RoleBinding:

```bash
kubectl describe rolebinding <name>
```

Describe ClusterRoleBinding:

```bash
kubectl describe clusterrolebinding <name>
```

Check identity:

```bash
kubectl auth whoami
```

Check permission:

```bash
kubectl auth can-i get pods
```

Check all permissions:

```bash
kubectl auth can-i --list
```

Check Service Account:

```bash
kubectl auth can-i --list \
  --as=system:serviceaccount:default:app-sa
```

Check namespace-specific permission:

```bash
kubectl auth can-i get pods \
  -n production
```

---

# Interview Questions

## Basic

- What is RBAC?
- What is authorization?
- What is the difference between authentication and authorization?
- What are the four main RBAC objects?
- What is a Role?
- What is a ClusterRole?
- What is a RoleBinding?
- What is a ClusterRoleBinding?
- What is a Service Account?
- What are Kubernetes RBAC verbs?

---

## Intermediate

- What is the difference between Role and ClusterRole?
- What is the difference between RoleBinding and ClusterRoleBinding?
- Can a RoleBinding reference a ClusterRole?
- What are cluster-scoped resources?
- What is the difference between User, Group, and ServiceAccount subjects?
- What is the purpose of `resourceNames`?
- What is the difference between `pods` and `pods/exec`?
- What are API groups?
- What is the principle of least privilege?
- Why should applications not use `cluster-admin`?
- What happens when a user receives permissions through multiple Roles?
- Does RBAC support deny rules?
- How would you troubleshoot a `403 Forbidden` error?

---

## Advanced

- Explain the complete Kubernetes RBAC evaluation process.
- How would you design RBAC for a multi-team Kubernetes cluster?
- How would you implement namespace isolation using RBAC?
- How would you design RBAC for CI/CD?
- How would you design RBAC for a Kubernetes operator?
- How would you secure Service Accounts using RBAC?
- Why is `pods/exec` considered sensitive?
- Why is Secret access highly privileged?
- How can excessive RBAC permissions lead to cluster compromise?
- How would you audit a Kubernetes cluster for excessive permissions?
- How would you find users with cluster-admin access?
- How would you identify wildcard RBAC rules?
- How can OIDC groups simplify RBAC management?
- How would you design least-privilege access for developers?
- How would you design read-only access for security analysts?
- How would you reduce the blast radius of a compromised Service Account?

---

# Interview Scenario 1

### Question

> A developer needs to view Pods and Deployments only in the `development` namespace. How would you implement access?

### Answer

Create a Role:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: developer-read

  namespace: development

rules:

- apiGroups:

  - ""

  resources:

  - pods

  verbs:

  - get

  - list

  - watch

- apiGroups:

  - apps

  resources:

  - deployments

  verbs:

  - get

  - list

  - watch
```

Then bind the developer or developer group:

```yaml
kind: RoleBinding

metadata:

  namespace: development

subjects:

- kind: Group

  name: developers

roleRef:

  kind: Role

  name: developer-read
```

Result:

```text
developers
     ↓
RoleBinding
     ↓
developer-read
     ↓
development namespace
     ↓
Read Pods + Deployments
```

No production access is granted.

---

# Interview Scenario 2

### Question

> A CI/CD system needs to deploy applications to the `production` namespace. Should you give it `cluster-admin`?

### Answer

No.

Create:

```text
Dedicated ServiceAccount / External Identity
```

Then:

```text
Least-Privilege Role
```

containing only the required deployment permissions.

Finally:

```text
RoleBinding
```

in:

```text
production
```

Architecture:

```text
CI/CD
 ↓
Dedicated Identity
 ↓
Deployment Role
 ↓
RoleBinding
 ↓
production
```

This reduces blast radius if the CI/CD credentials are compromised.

---

# Interview Scenario 3

### Question

> A Service Account can access Secrets even though you did not grant it Secret permissions directly. How can this happen?

### Answer

RBAC permissions are additive.

The Service Account may have received Secret permissions through:

```text
Another RoleBinding
```

or:

```text
ClusterRoleBinding
```

or:

```text
A broader ClusterRole
```

Investigate:

```bash
kubectl get rolebindings -A
```

and:

```bash
kubectl get clusterrolebindings
```

Then inspect the relevant Roles and ClusterRoles.

Also use:

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:<namespace>:<serviceaccount>
```

---

# Interview Scenario 4

### Question

> A user receives `403 Forbidden` when attempting to delete a Pod. They can successfully list Pods. What is likely wrong?

### Answer

Authentication is working.

The user has:

```text
list
```

permission but not:

```text
delete
```

permission.

For example:

```yaml
verbs:

- get

- list

- watch
```

does not grant:

```text
delete
```

The Role needs an appropriate:

```yaml
delete
```

permission if deletion is genuinely required.

---

# Interview Scenario 5

### Question

> How would you reduce the impact of a compromised application Service Account?

### Answer

Use:

```text
Dedicated Service Account
+
Minimal RBAC
+
Namespace-scoped permissions
+
No unnecessary Secret access
+
No unnecessary pods/exec
+
No cluster-admin
+
NetworkPolicy
+
Pod security
+
Audit logging
+
Runtime monitoring
```

The objective is:

```text
Compromised Identity
       ↓
Limited Permissions
       ↓
Limited Blast Radius
       ↓
Detection
       ↓
Response
```

---

# Production RBAC Checklist

```text
☑ Use least privilege
☑ Prefer namespace-scoped Roles
☑ Prefer RoleBindings when possible
☑ Use dedicated Service Accounts
☑ Avoid cluster-admin
☑ Avoid wildcards
☑ Restrict Secret access
☑ Review pods/exec
☑ Review RBAC modification permissions
☑ Review ClusterRoleBindings
☑ Review Service Account permissions
☑ Use groups for human users
☑ Test with kubectl auth can-i
☑ Audit RBAC changes
☑ Periodically review permissions
```

---

# Recommended Practice

1. Create a test namespace.
2. Create a Service Account.
3. Create a Role.
4. Grant read-only Pod access.
5. Create a RoleBinding.
6. Test with `kubectl auth can-i`.
7. Attempt an unauthorized operation.
8. Create a ClusterRole.
9. Bind it using a RoleBinding.
10. Compare namespace-scoped behavior.
11. Bind the ClusterRole using a ClusterRoleBinding.
12. Compare cluster-wide behavior.
13. Test resource names.
14. Test subresources.
15. Test `pods/log`.
16. Study `pods/exec`.
17. Audit existing ClusterRoleBindings.
18. Identify `cluster-admin` assignments.
19. Search for wildcard permissions.
20. Review Secret access.
21. Design developer RBAC.
22. Design CI/CD RBAC.
23. Design application RBAC.
24. Design security-team RBAC.
25. Practice troubleshooting `403 Forbidden`.
26. Build a least-privilege RBAC architecture.

---

# References

## Official Kubernetes Documentation

- Kubernetes RBAC Authorization
- Using RBAC Authorization
- Role
- ClusterRole
- RoleBinding
- ClusterRoleBinding
- Authorization Overview
- Service Accounts
- Kubernetes API Concepts
- `kubectl auth can-i`

---

# Chapter Summary

RBAC is Kubernetes' primary authorization mechanism.

The core model is:

```text
Subject
   ↓
Role / ClusterRole
   ↓
RoleBinding / ClusterRoleBinding
   ↓
Permissions
```

The four important objects are:

```text
Role
ClusterRole
RoleBinding
ClusterRoleBinding
```

A:

```text
Role
```

defines namespace-scoped permissions.

A:

```text
ClusterRole
```

defines reusable permissions that can apply to cluster-scoped resources or namespaced resources.

A:

```text
RoleBinding
```

grants a Role or ClusterRole within a specific namespace.

A:

```text
ClusterRoleBinding
```

grants a ClusterRole across the cluster.

Subjects can be:

```text
User
Group
ServiceAccount
```

Rules define:

```text
API Groups
Resources
Verbs
Resource Names
```

The most important security principle is:

> **Grant the smallest set of permissions required for an identity to perform its job.**

For example:

```text
Developer
 ↓
Role
 ↓
get/list/watch Pods
 ↓
development namespace
```

is significantly safer than:

```text
Developer
 ↓
cluster-admin
```

RBAC permissions are:

```text
Additive
```

Therefore:

```text
Role A
+
Role B
+
ClusterRoleBinding
```

can collectively provide more access than any single Role suggests.

There is no standard RBAC deny rule that overrides an existing allow.

Sensitive permissions should receive special attention:

```text
secrets
pods/exec
pods/attach
nodes
roles
rolebindings
clusterroles
clusterrolebindings
```

The most useful troubleshooting commands are:

```bash
kubectl auth whoami
```

```bash
kubectl auth can-i get pods
```

```bash
kubectl auth can-i --list
```

and:

```bash
kubectl get rolebindings -A
kubectl get clusterrolebindings
```

The complete security relationship is:

```text
Authentication
      ↓
Who are you?
      ↓
Authorization
      ↓
What can you do?
      ↓
RBAC
      ↓
What resources and operations?
      ↓
Least Privilege
      ↓
Reduced Blast Radius
```

A production Kubernetes RBAC architecture should therefore prioritize:

```text
Least Privilege
+
Namespace Isolation
+
Dedicated Identities
+
Minimal Permissions
+
Regular Auditing
+
Strong Authentication
```

This forms the foundation for controlling access to Kubernetes resources securely.

---

## Next Chapter

# Chapter 49 – Service Accounts

Topics will include:

- What Are Service Accounts?
- Human Users vs Service Accounts
- Service Account Architecture
- Default Service Account
- Creating Service Accounts
- Assigning Service Accounts to Pods
- Service Account Identity
- Service Account Tokens
- Bound Service Account Tokens
- Projected Tokens
- TokenRequest API
- Token Expiration
- Token Rotation
- Token Audience
- `automountServiceAccountToken`
- Service Account RBAC
- Dedicated Service Accounts
- Service Accounts for Applications
- Service Accounts for Controllers
- Service Accounts for Operators
- Service Accounts for CI/CD
- Service Account Security
- Service Account Token Theft
- Workload Identity
- Cloud Workload Identity
- Service Account Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---