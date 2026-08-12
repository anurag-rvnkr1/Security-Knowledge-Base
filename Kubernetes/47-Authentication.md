# Chapter 47 – Authentication

## Overview

Authentication is the first major security step when interacting with the Kubernetes API.

Before Kubernetes can determine:

```text
What are you allowed to do?
```

it must first determine:

```text
Who are you?
```

This process is called:

```text
Authentication
```

A simplified Kubernetes API request flow is:

```text
Client
  ↓
API Server
  ↓
Authentication
  ↓
Authorization
  ↓
Admission Control
  ↓
API Request
```

Authentication answers:

> **Who is making this request?**

Authorization answers:

> **What is that identity allowed to do?**

---

# Learning Objectives

After completing this chapter, you will understand:

- What authentication means
- Kubernetes identity model
- Authentication vs authorization
- API Server authentication
- Client certificates
- Bearer tokens
- Service Account authentication
- OIDC authentication
- External identity providers
- Cloud identity
- Authentication webhooks
- Anonymous requests
- `kubeconfig`
- Client credentials
- Certificate-based authentication
- Service Account tokens
- Bound Service Account tokens
- Token projection
- TokenRequest API
- OIDC authentication
- Identity providers
- Authentication security best practices
- Authentication troubleshooting
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Authentication?

Authentication is the process of verifying the identity of a requester.

For example:

```text
User
 ↓
Provides Credential
 ↓
Kubernetes verifies credential
 ↓
Identity established
```

The identity may be:

```text
Human User
Service Account
External Identity
```

---

# Authentication vs Authorization

This distinction is extremely important.

## Authentication

```text
Who are you?
```

Example:

```text
Alice
```

---

## Authorization

```text
What can Alice do?
```

Example:

```text
Alice can:

get pods
list deployments

Alice cannot:

delete nodes
```

---

# Simple Example

Suppose you run:

```bash
kubectl get pods
```

Kubernetes must determine:

```text
1. Who is making the request?
2. Is that identity allowed to list Pods?
```

Therefore:

```text
kubectl
   ↓
Authentication
   ↓
Identity = Alice
   ↓
Authorization
   ↓
Can Alice list Pods?
   ↓
Yes
   ↓
Return Pods
```

---

# Kubernetes Identity Model

Kubernetes does not have a traditional built-in user database for ordinary human users.

Instead, the API Server accepts identities from configured authentication mechanisms.

Common mechanisms include:

```text
Client Certificates
Bearer Tokens
Service Account Tokens
OIDC
Authentication Webhooks
Cloud-provider identity integrations
```

---

# Human Users vs Service Accounts

Kubernetes commonly distinguishes between:

```text
Human / External Users
```

and:

```text
Service Accounts
```

Service Accounts are Kubernetes API identities intended for workloads and automation.

---

# Human User

Example:

```text
developer@example.com
```

The identity may come from:

```text
OIDC
Client Certificate
External Identity Provider
```

---

# Service Account

Example:

```text
system:serviceaccount:production:api-sa
```

This identity represents a workload.

---

# Service Account Identity Format

A Service Account identity commonly looks like:

```text
system:serviceaccount:<namespace>:<name>
```

Example:

```text
system:serviceaccount:production:api-sa
```

Breakdown:

```text
system:serviceaccount
        ↓
production
        ↓
api-sa
```

---

# API Server

The Kubernetes API Server is responsible for processing API requests.

Authentication is handled at the API Server.

Conceptually:

```text
Client
   ↓
HTTPS Request
   ↓
API Server
   ↓
Authentication
   ↓
Identity
```

---

# Authentication Flow

A simplified request flow:

```text
                Client
                  │
                  ▼
             HTTPS Request
                  │
                  ▼
              API Server
                  │
                  ▼
          Authentication Layer
                  │
          ┌───────┼────────┐
          ▼       ▼        ▼
       Cert     Token     OIDC
          │       │        │
          └───────┼────────┘
                  ▼
               Identity
                  │
                  ▼
             Authorization
```

---

# Kubernetes Authentication Methods

Common mechanisms include:

```text
1. Client Certificates
2. Bearer Tokens
3. Service Account Tokens
4. OIDC
5. Authentication Webhooks
```

The exact available methods depend on the Kubernetes distribution and API Server configuration.

---

# Client Certificates

Kubernetes can authenticate clients using TLS client certificates.

The client presents:

```text
Client Certificate
+
Private Key
```

The API Server validates the certificate.

---

# Certificate Authentication

Conceptually:

```text
Client
  │
  ├── Certificate
  │
  └── Private Key
       ↓
    API Server
       ↓
Certificate Validation
       ↓
Identity
```

---

# Example Certificate Identity

A certificate may contain:

```text
Common Name (CN)
```

such as:

```text
anurag
```

and potentially groups through certificate fields supported by Kubernetes authentication configuration.

The resulting identity can then be authorized using RBAC.

---

# Important Security Point

A client certificate is:

```text
Authentication credential
```

It is not automatically:

```text
Authorization
```

RBAC determines what the authenticated identity can do.

---

# Certificate-Based Request

Conceptually:

```text
Certificate
     ↓
API Server verifies certificate
     ↓
Identity established
     ↓
RBAC evaluation
     ↓
Request allowed/denied
```

---

# Bearer Tokens

A bearer token is a credential presented with an API request.

Conceptually:

```text
Authorization:
Bearer <token>
```

The API Server validates the token according to its configured authentication mechanisms.

---

# Bearer Token Security

A bearer token should be treated as:

```text
Sensitive Credential
```

Anyone possessing a valid bearer token may potentially authenticate as the associated identity until the token expires or becomes invalid.

Therefore:

```text
Never expose tokens in:
Logs
Source Code
Git Repositories
Screenshots
Chat Messages
Public URLs
```

---

# Service Accounts

Service Accounts provide identities for workloads.

Create one:

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: api-sa

  namespace: production
```

Apply:

```bash
kubectl apply -f serviceaccount.yaml
```

---

# Assign Service Account to Pod

```yaml
spec:

  serviceAccountName: api-sa
```

Now the Pod runs under:

```text
system:serviceaccount:production:api-sa
```

---

# Why Use Dedicated Service Accounts?

Avoid using one broad identity for every workload.

Bad:

```text
All Applications
       ↓
One ServiceAccount
       ↓
Broad Permissions
```

Better:

```text
Frontend
   ↓
frontend-sa

Backend
   ↓
backend-sa

Monitoring
   ↓
monitoring-sa
```

Each can receive only the permissions it requires.

---

# Default Service Account

Every namespace has a default Service Account.

Example:

```bash
kubectl get serviceaccount
```

Output may include:

```text
default
```

If a Pod does not specify another Service Account, it generally uses the namespace's default Service Account.

---

# Default Does Not Mean Privileged

The default Service Account should not automatically be assumed to have broad Kubernetes permissions.

Authorization is separately controlled by RBAC.

---

# Service Account Tokens

Workloads may need credentials to communicate with the Kubernetes API.

Modern Kubernetes uses short-lived, audience-bound Service Account tokens through the TokenRequest mechanism and projected volumes.

Conceptually:

```text
Pod
 ↓
Service Account
 ↓
Token
 ↓
API Server
```

---

# Bound Service Account Tokens

Modern Kubernetes Service Account tokens are generally:

```text
Short-lived
Audience-bound
Pod-bound
```

where supported by the Kubernetes version and configuration.

This is more secure than relying on long-lived static credentials.

---

# Token Projection

A Service Account token can be projected into a Pod.

Conceptually:

```text
Service Account
       ↓
TokenRequest
       ↓
Projected Volume
       ↓
Container
```

The application reads the token from the mounted filesystem.

---

# TokenRequest API

Kubernetes provides the:

```text
TokenRequest API
```

to request Service Account tokens.

Tokens can include:

```text
Expiration
Audience
Binding information
```

This enables more limited credentials.

---

# Token Audience

An audience identifies the intended recipient of a token.

Conceptually:

```text
Token

Audience:
https://kubernetes.default.svc
```

An application should not blindly accept a token intended for another service.

---

# Token Expiration

Short-lived tokens reduce risk.

Example:

```text
Token issued
   ↓
Valid for limited duration
   ↓
Expires
   ↓
New token obtained
```

This is preferable to credentials that remain valid indefinitely.

---

# Token Rotation

Projected Service Account tokens can be refreshed automatically by Kubernetes mechanisms.

The application should read the token from the appropriate projected location rather than assuming a token remains valid forever.

---

# AutomountServiceAccountToken

If a Pod does not need Kubernetes API access, you can disable automatic token mounting:

```yaml
spec:

  automountServiceAccountToken: false
```

This reduces unnecessary credential exposure.

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

The application does not need Kubernetes API credentials.

Therefore:

```text
No automatic Service Account token
```

---

# When Should a Pod Use a Token?

Use a Service Account token when the application genuinely needs Kubernetes API access.

Examples:

```text
Controller
Operator
Kubernetes-aware Agent
Custom Automation
```

A normal web application often does not need direct Kubernetes API access.

---

# `kubeconfig`

`kubectl` commonly uses:

```text
kubeconfig
```

to determine:

```text
Which cluster?
Which user/credential?
Which context?
Which namespace?
```

A kubeconfig commonly contains:

```text
clusters
users
contexts
current-context
```

---

# View Current Context

```bash
kubectl config current-context
```

---

# View All Contexts

```bash
kubectl config get-contexts
```

---

# View Configuration

```bash
kubectl config view
```

Be careful:

```bash
kubectl config view --raw
```

can reveal sensitive credential material depending on your configuration.

Do not share it publicly.

---

# Kubeconfig Structure

Conceptually:

```text
kubeconfig

├── clusters
│
├── users
│
├── contexts
│
└── current-context
```

---

# Cluster

A cluster entry identifies the Kubernetes API endpoint and related certificate information.

Example:

```yaml
clusters:

- name: production

  cluster:

    server: https://kubernetes.example.com

    certificate-authority-data: ...
```

---

# User

A user entry defines client credentials.

For example:

```yaml
users:

- name: developer

  user:

    client-certificate-data: ...

    client-key-data: ...
```

or:

```yaml
users:

- name: developer

  user:

    token: ...
```

---

# Context

A context combines:

```text
Cluster
+
User
+
Namespace
```

Example:

```yaml
contexts:

- name: production

  context:

    cluster: production

    user: developer

    namespace: production
```

---

# Why Contexts Matter

A developer may have:

```text
Development Cluster
Staging Cluster
Production Cluster
```

Using the wrong context can result in modifying the wrong environment.

Always verify:

```bash
kubectl config current-context
```

before sensitive operations.

---

# OIDC Authentication

OIDC stands for:

```text
OpenID Connect
```

It is commonly used to integrate Kubernetes with an external identity provider.

Examples of identity providers can include enterprise authentication platforms supporting OIDC.

---

# OIDC Architecture

```text
                 User
                  │
                  ▼
           Identity Provider
                  │
                  ▼
              OIDC Token
                  │
                  ▼
             kubectl
                  │
                  ▼
             API Server
                  │
                  ▼
           OIDC Validation
                  │
                  ▼
               Identity
                  │
                  ▼
                 RBAC
```

---

# Why Use OIDC?

OIDC enables organizations to centralize:

```text
Identity
Authentication
MFA
User Lifecycle
Group Membership
```

instead of maintaining separate Kubernetes credentials for every employee.

---

# OIDC Groups

An identity provider can provide group information.

Example:

```text
User:

anurag@example.com

Groups:

developers
security-team
```

RBAC can then map groups to permissions.

Conceptually:

```text
OIDC Group
   ↓
RBAC RoleBinding
   ↓
Permissions
```

---

# OIDC + RBAC

Example:

```yaml
subjects:

- kind: Group

  name: developers

  apiGroup: rbac.authorization.k8s.io
```

This can grant permissions to users belonging to the:

```text
developers
```

group.

---

# External Identity Provider

A common enterprise architecture is:

```text
Employee
   ↓
SSO / Identity Provider
   ↓
OIDC
   ↓
Kubernetes API Server
   ↓
RBAC
```

Benefits:

```text
Centralized Authentication
MFA
Account Lifecycle
Group Management
```

---

# Authentication Webhook

Kubernetes can integrate with an external authentication service through supported webhook-based authentication mechanisms.

Conceptually:

```text
Client
   ↓
API Server
   ↓
Authentication Webhook
   ↓
External Auth System
   ↓
Identity
```

The exact configuration depends on the Kubernetes distribution and authentication architecture.

---

# Cloud Identity

Managed Kubernetes platforms can integrate Kubernetes authentication with cloud identity systems.

Conceptually:

```text
Cloud Identity
       ↓
Kubernetes Authentication
       ↓
Kubernetes Identity
       ↓
RBAC
```

The exact mechanism varies by platform.

---

# Anonymous Authentication

Kubernetes can be configured to allow anonymous requests in some environments.

Anonymous requests are associated with identities such as:

```text
system:anonymous
```

and:

```text
system:unauthenticated
```

Anonymous access should be carefully restricted.

---

# Why Restrict Anonymous Access?

If anonymous requests can reach sensitive APIs:

```text
Unauthenticated User
        ↓
Kubernetes API
        ↓
Sensitive Information
```

This can create a serious security issue.

---

# Authentication Groups

Authenticated identities can belong to groups.

Common Kubernetes system groups include:

```text
system:authenticated
```

and:

```text
system:unauthenticated
```

Service Accounts also belong to relevant system groups.

---

# `system:masters`

Kubernetes has a highly privileged group:

```text
system:masters
```

Membership can provide extremely powerful administrative access.

Credentials that authenticate as this group should be protected extremely carefully.

---

# Authentication and RBAC

Authentication:

```text
Identity = alice
```

RBAC:

```text
alice
 ↓
RoleBinding
 ↓
Role
 ↓
get pods
```

This demonstrates that:

```text
Authentication ≠ Authorization
```

---

# Authentication Security Model

A secure authentication architecture should use:

```text
Strong Identity
       ↓
Strong Credentials
       ↓
Short-Lived Tokens
       ↓
Least-Privilege RBAC
       ↓
Auditing
```

---

# Credential Security

Authentication credentials include:

```text
Private Keys
Tokens
Certificates
OIDC Credentials
Service Account Tokens
```

Protect them like passwords.

Never commit them to Git.

---

# Certificate Private Keys

If using certificate authentication:

```text
certificate
+
private key
```

must be protected.

If an attacker obtains a private key, they may be able to authenticate as the corresponding identity.

---

# Token Security

Do not store Kubernetes tokens in:

```text
Source Code
Docker Images
Public ConfigMaps
Git Repositories
Application Logs
```

Use secure credential-management mechanisms.

---

# Authentication and TLS

Kubernetes API communication should use:

```text
HTTPS
```

TLS provides:

```text
Confidentiality
Integrity
Server Authentication
```

Client certificate authentication can additionally provide:

```text
Client Authentication
```

---

# Authentication and Authorization Flow

The complete simplified flow is:

```text
                 kubectl
                    │
                    ▼
              HTTPS Request
                    │
                    ▼
                API Server
                    │
                    ▼
             Authentication
                    │
                    ▼
              User Identity
                    │
                    ▼
              Authorization
                    │
                    ▼
                  RBAC
                    │
                    ▼
               Admission
                    │
                    ▼
              API Operation
```

---

# Authentication Failure

If credentials are invalid:

```text
Authentication
      ↓
Failure
      ↓
401 Unauthorized
```

Conceptually:

```text
Who are you?

Cannot verify.
```

---

# Authorization Failure

If authentication succeeds but permissions are insufficient:

```text
Authentication
      ↓
Success
      ↓
Authorization
      ↓
Denied
```

Typically:

```text
403 Forbidden
```

---

# 401 vs 403

This is an important interview question.

```text
401 Unauthorized
```

generally means:

```text
Authentication failed or credentials are missing/invalid.
```

```text
403 Forbidden
```

generally means:

```text
Identity is known, but the request is not authorized.
```

---

# Troubleshooting Authentication

## Check Current Context

```bash
kubectl config current-context
```

---

# Check Contexts

```bash
kubectl config get-contexts
```

---

# Check Identity

Modern Kubernetes clients support:

```bash
kubectl auth whoami
```

This can show the authenticated username and groups when supported.

---

# Test Authorization

```bash
kubectl auth can-i get pods
```

---

# Test as a Service Account

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:production:api-sa
```

---

# Test a Specific Namespace

```bash
kubectl auth can-i get secrets \
  -n production
```

---

# Authentication Error

Example:

```text
error: You must be logged in to the server
```

Possible causes:

```text
Missing credentials
Expired credentials
Invalid token
Wrong kubeconfig
Wrong context
Certificate problems
Identity provider issue
```

---

# Certificate Authentication Troubleshooting

Check kubeconfig:

```bash
kubectl config view
```

Verify:

```text
Client Certificate
Client Key
Certificate Authority
Server Endpoint
```

Do not expose private keys while troubleshooting.

---

# OIDC Troubleshooting

Possible causes:

```text
Expired token
Invalid issuer
Incorrect client configuration
Wrong audience
Clock skew
Identity provider outage
Group claim mismatch
```

---

# Service Account Authentication Troubleshooting

Check:

```bash
kubectl get serviceaccount
```

Check Pod:

```bash
kubectl get pod <pod-name> -o yaml
```

Look for:

```text
serviceAccountName
automountServiceAccountToken
```

---

# Check Service Account

```bash
kubectl describe serviceaccount api-sa
```

---

# RBAC vs Authentication Troubleshooting

Use this approach:

```text
Step 1
Is identity valid?

↓

Step 2
What identity was recognized?

↓

Step 3
What permissions does identity have?

↓

Step 4
Is the requested resource correct?

↓

Step 5
Is the namespace correct?
```

Useful commands:

```bash
kubectl auth whoami
```

```bash
kubectl auth can-i ...
```

---

# Authentication Best Practices

### 1. Use Strong Identity Providers

For organizations, use centralized identity systems where appropriate.

---

### 2. Prefer Short-Lived Credentials

Short-lived credentials reduce the impact of credential theft.

---

### 3. Use MFA

Where supported by the identity provider, use:

```text
Multi-Factor Authentication
```

---

### 4. Protect Private Keys

Never expose:

```text
client-key
```

or:

```text
private key
```

---

### 5. Protect Service Account Tokens

Treat them as sensitive credentials.

---

### 6. Disable Unnecessary Token Mounting

If a workload does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

---

### 7. Avoid Shared Credentials

Use:

```text
Dedicated identities
```

instead of:

```text
One credential shared by many applications
```

---

### 8. Verify Context Before Production Operations

Run:

```bash
kubectl config current-context
```

before executing destructive commands.

---

### 9. Audit Authentication Activity

Monitor:

```text
Successful authentication
Failed authentication
Privileged identities
Credential changes
```

---

### 10. Rotate Credentials

Rotate:

```text
Certificates
Tokens
Keys
```

according to your security policy.

---

# Production Authentication Architecture

A mature enterprise setup can look like:

```text
                    Employees
                        │
                        ▼
                 Identity Provider
                        │
                       OIDC
                        │
                        ▼
                     kubectl
                        │
                        ▼
                  Kubernetes API
                        │
                ┌───────┴────────┐
                ▼                ▼
         Authentication       Audit
                │
                ▼
             Identity
                │
                ▼
              RBAC
                │
                ▼
             Admission
                │
                ▼
            Kubernetes
```

---

# Workload Authentication Architecture

For applications:

```text
                    Application
                         │
                         ▼
                  Service Account
                         │
                         ▼
                  Short-lived Token
                         │
                         ▼
                   Kubernetes API
                         │
                         ▼
                        RBAC
                         │
                         ▼
                    API Resource
```

---

# Human vs Workload Authentication

| Identity | Typical Mechanism |
|---|---|
| Developer | OIDC / Certificate |
| Administrator | OIDC / Certificate |
| CI/CD | Short-lived identity / Service Account / Cloud identity |
| Pod | Service Account |
| Controller | Service Account |
| Operator | Service Account |

The exact mechanism depends on the environment.

---

# Hands-on Lab 1 – Inspect kubeconfig

Run:

```bash
kubectl config current-context
```

Then:

```bash
kubectl config get-contexts
```

Then:

```bash
kubectl config view
```

Identify:

```text
Cluster
User
Context
Namespace
```

Do not share credential data.

---

# Hands-on Lab 2 – Identify Current User

Run:

```bash
kubectl auth whoami
```

Record:

```text
Username
Groups
```

Understand how your current credentials map to a Kubernetes identity.

---

# Hands-on Lab 3 – Test Authorization

Run:

```bash
kubectl auth can-i get pods
```

Then:

```bash
kubectl auth can-i delete pods
```

Compare:

```text
yes
```

and:

```text
no
```

This demonstrates:

```text
Authentication
+
Authorization
```

---

# Hands-on Lab 4 – Service Account

Create:

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: test-sa

  namespace: default
```

Apply:

```bash
kubectl apply -f test-sa.yaml
```

Check:

```bash
kubectl get serviceaccount test-sa
```

---

# Hands-on Lab 5 – Assign Service Account

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: sa-demo

spec:

  serviceAccountName: test-sa

  containers:

  - name: app

    image: nginx:1.30
```

Apply:

```bash
kubectl apply -f sa-demo.yaml
```

Check:

```bash
kubectl get pod sa-demo -o yaml
```

Find:

```text
serviceAccountName
```

---

# Hands-on Lab 6 – Disable Token Mounting

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: no-api-token

spec:

  serviceAccountName: test-sa

  automountServiceAccountToken: false

  containers:

  - name: app

    image: nginx:1.30
```

Apply:

```bash
kubectl apply -f no-api-token.yaml
```

Observe the difference from a Pod with automatic Service Account token projection enabled.

---

# Hands-on Lab 7 – Service Account RBAC

Create a Role:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

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

Create a RoleBinding:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: RoleBinding

metadata:

  name: pod-reader-binding

subjects:

- kind: ServiceAccount

  name: test-sa

roleRef:

  kind: Role

  name: pod-reader

  apiGroup: rbac.authorization.k8s.io
```

---

# Hands-on Lab 8 – Test Service Account Permissions

Run:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:test-sa
```

Expected:

```text
yes
```

Test:

```bash
kubectl auth can-i delete pods \
  --as=system:serviceaccount:default:test-sa
```

Expected:

```text
no
```

This demonstrates:

```text
Authentication Identity
+
RBAC Authorization
```

---

# Hands-on Lab 9 – Test Namespace Isolation

Create:

```bash
kubectl create namespace auth-lab
```

Create a Service Account:

```bash
kubectl create serviceaccount app-sa -n auth-lab
```

Create a Role that allows:

```text
get pods
```

only within:

```text
auth-lab
```

Then verify:

```bash
kubectl auth can-i get pods \
  -n auth-lab \
  --as=system:serviceaccount:auth-lab:app-sa
```

Compare with access to another namespace.

---

# Hands-on Lab 10 – OIDC Study Exercise

In a test environment, study the OIDC configuration of your Kubernetes platform.

Identify:

```text
Issuer
Client ID
Username Claim
Group Claim
Audience
```

Do not modify production authentication settings without a controlled change process.

---

# Hands-on Lab 11 – Authentication Failure

In a disposable environment, intentionally use invalid credentials or an expired credential.

Observe:

```text
Authentication failure
```

Compare it with:

```text
RBAC authorization failure
```

Understand the difference between:

```text
401
```

and:

```text
403
```

---

# Common Mistakes

## 1. Confusing Authentication with Authorization

Remember:

```text
Authentication
=
Who are you?
```

```text
Authorization
=
What can you do?
```

---

## 2. Sharing Service Account Credentials

Avoid using one Service Account token across unrelated applications.

---

## 3. Storing Tokens in Git

Never commit:

```text
Bearer Tokens
Private Keys
Client Certificates
Cloud Credentials
```

to repositories.

---

## 4. Using Long-Lived Credentials Unnecessarily

Prefer short-lived credentials where possible.

---

## 5. Giving Applications Powerful Identities

Avoid:

```text
cluster-admin
```

unless absolutely necessary.

---

## 6. Forgetting `automountServiceAccountToken`

Applications that do not need Kubernetes API access should not unnecessarily receive credentials.

---

## 7. Ignoring kubeconfig Security

A kubeconfig can contain highly sensitive authentication material.

Protect:

```text
~/.kube/config
```

according to your environment.

---

## 8. Running Commands Against the Wrong Cluster

Always verify:

```bash
kubectl config current-context
```

---

## 9. Ignoring Token Expiration

Short-lived tokens can expire.

Applications and automation should handle credential renewal appropriately.

---

## 10. Using Anonymous Access Carelessly

Unauthenticated access should be minimized and carefully controlled.

---

## 11. Forgetting Group Membership

OIDC and certificate-based identities can include groups that affect RBAC permissions.

---

## 12. Treating a Valid Credential as Full Access

Authentication only establishes identity.

RBAC still determines authorization.

---

# Best Practices

### 1. Centralize Human Authentication

Use an enterprise identity provider where appropriate.

---

### 2. Use OIDC for Enterprise SSO

Benefits include:

```text
Centralized Identity
MFA
User Lifecycle
Group Management
```

---

### 3. Use Dedicated Service Accounts

One workload:

```text
One appropriate identity
```

rather than:

```text
Shared administrator identity
```

---

### 4. Use Short-Lived Credentials

Reduce the lifetime of credentials where practical.

---

### 5. Minimize API Access

If an application does not use Kubernetes APIs:

```yaml
automountServiceAccountToken: false
```

---

### 6. Protect kubeconfig

Treat it as sensitive.

---

### 7. Protect Private Keys

Use secure storage and appropriate filesystem permissions.

---

### 8. Combine Authentication with RBAC

Strong authentication without authorization controls is insufficient.

---

### 9. Audit Authentication

Monitor:

```text
Failed Authentication
Successful Privileged Authentication
Identity Changes
Service Account Usage
```

---

### 10. Use MFA

Where available through the external identity provider.

---

# Quick Revision

## Authentication

```text
Who are you?
```

---

## Authorization

```text
What can you do?
```

---

## API Server

```text
Central API entry point
```

---

## Service Account

```text
Workload identity
```

---

## OIDC

```text
External identity protocol
```

---

## Client Certificate

```text
Certificate-based client authentication
```

---

## Bearer Token

```text
Token presented as a credential
```

---

## kubeconfig

```text
Cluster + User + Context configuration
```

---

## TokenRequest

```text
Mechanism for obtaining Service Account tokens
```

---

## `automountServiceAccountToken`

```text
Controls automatic Service Account credential mounting
```

---

## 401

```text
Authentication problem
```

---

## 403

```text
Authorization problem
```

---

# Essential Commands

Current context:

```bash
kubectl config current-context
```

List contexts:

```bash
kubectl config get-contexts
```

View configuration:

```bash
kubectl config view
```

View current identity:

```bash
kubectl auth whoami
```

Check permissions:

```bash
kubectl auth can-i get pods
```

Check Service Account permissions:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:default:app-sa
```

List Service Accounts:

```bash
kubectl get serviceaccounts
```

Describe Service Account:

```bash
kubectl describe serviceaccount <name>
```

List Roles:

```bash
kubectl get roles
```

List RoleBindings:

```bash
kubectl get rolebindings
```

List ClusterRoles:

```bash
kubectl get clusterroles
```

List ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

Inspect Pod identity:

```bash
kubectl get pod <name> -o yaml
```

---

# Interview Questions

## Basic

- What is authentication?
- What is the difference between authentication and authorization?
- How does Kubernetes authenticate users?
- What is a Service Account?
- What is OIDC?
- What is a kubeconfig?
- What is a bearer token?
- What is certificate-based authentication?
- What is `automountServiceAccountToken`?

---

## Intermediate

- Explain the Kubernetes API authentication flow.
- How are Service Accounts different from human users?
- What is the TokenRequest API?
- What are projected Service Account tokens?
- Why are short-lived tokens more secure?
- What is the purpose of OIDC?
- What is the difference between 401 and 403?
- How does `kubectl` authenticate to a cluster?
- What information is stored in kubeconfig?
- Why should applications use dedicated Service Accounts?

---

## Advanced

- Explain the complete Kubernetes authentication and authorization pipeline.
- How does OIDC integrate with Kubernetes?
- How do OIDC groups work with RBAC?
- How would you secure human access to a production cluster?
- How would you secure workload authentication?
- Why are bound Service Account tokens more secure than long-lived credentials?
- How does token audience improve security?
- How would you troubleshoot an authentication failure?
- How would you distinguish an authentication issue from an RBAC issue?
- How would you design Kubernetes authentication for a large enterprise?
- How would you prevent compromised Pods from abusing Service Account credentials?
- How would you secure kubeconfig files?
- What risks are associated with client certificate authentication?
- Why should anonymous authentication be restricted?
- How does authentication fit into a defense-in-depth Kubernetes architecture?

---

# Interview Scenario

### Question

> A developer says `kubectl get pods` returns `403 Forbidden`. How would you troubleshoot it?

### Answer

First determine whether authentication succeeded:

```bash
kubectl auth whoami
```

If the identity is successfully identified:

```text
Authentication = Working
```

Then test authorization:

```bash
kubectl auth can-i get pods
```

Check the namespace:

```bash
kubectl auth can-i get pods -n production
```

Inspect:

```text
Role
RoleBinding
ClusterRole
ClusterRoleBinding
```

For example:

```bash
kubectl get rolebindings -n production
```

Then:

```bash
kubectl describe rolebinding <binding>
```

The likely problem is:

```text
Authenticated identity
        ↓
Missing RBAC permission
        ↓
403 Forbidden
```

---

# Interview Scenario 2

### Question

> A Pod has been compromised. How can you reduce the risk of its Service Account credentials being abused?

### Answer

Use multiple controls:

```text
1. Dedicated Service Account
2. Least-privilege RBAC
3. Disable token mounting if API access is unnecessary
4. Use short-lived bound tokens
5. Restrict NetworkPolicy
6. Harden the container
7. Monitor API activity
8. Audit suspicious requests
```

Conceptually:

```text
Compromised Pod
      ↓
No unnecessary token
      ↓
Minimal RBAC
      ↓
Limited API access
      ↓
Network restrictions
      ↓
Audit + Detection
```

---

# Production Authentication Architecture

A strong enterprise model can be:

```text
                    Employee
                       │
                       ▼
                Identity Provider
                       │
                  MFA + OIDC
                       │
                       ▼
                    kubectl
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
                     RBAC
                       │
                       ▼
                   Admission
                       │
                       ▼
                  API Resource
```

For workloads:

```text
                    Application
                         │
                         ▼
                   Service Account
                         │
                         ▼
                  Short-lived Token
                         │
                         ▼
                   Kubernetes API
                         │
                         ▼
                        RBAC
                         │
                         ▼
                     Resource
```

---

# Authentication Security Checklist

```text
☑ Strong authentication
☑ MFA for human users
☑ Centralized identity
☑ Dedicated Service Accounts
☑ Least-privilege RBAC
☑ Short-lived tokens
☑ Protected private keys
☑ Protected kubeconfig
☑ Disable unnecessary token mounting
☑ Restrict anonymous access
☑ Audit authentication activity
☑ Monitor privileged identities
☑ Rotate credentials
☑ Verify production context before operations
```

---

# Recommended Practice

1. Learn the difference between authentication and authorization.
2. Inspect your current Kubernetes identity.
3. Inspect your kubeconfig structure without exposing credentials.
4. Create a dedicated Service Account.
5. Assign it to a Pod.
6. Test Service Account identity.
7. Create a least-privilege Role.
8. Bind the Role to the Service Account.
9. Use `kubectl auth can-i`.
10. Test an allowed operation.
11. Test a denied operation.
12. Disable automatic token mounting for a Pod that does not need API access.
13. Study projected Service Account tokens.
14. Study the TokenRequest API.
15. Study OIDC authentication.
16. Study OIDC groups and RBAC.
17. Understand 401 vs 403 errors.
18. Practice authentication troubleshooting.
19. Design a production human-authentication architecture.
20. Design a secure workload-authentication architecture.

---

# References

## Official Kubernetes Documentation

- Authentication
- Authenticating
- Service Accounts
- Configure Service Accounts for Pods
- TokenRequest API
- Bound Service Account Tokens
- Kubernetes API Access
- RBAC Authorization
- kubeconfig
- Kubernetes Auditing

---

## Identity and Authentication

- OpenID Connect (OIDC)
- OAuth 2.0
- Kubernetes Authentication APIs
- Cloud Provider Identity Integrations

---

# Chapter Summary

Authentication is the process of establishing:

```text
Who is making the request?
```

Kubernetes can authenticate identities using mechanisms such as:

```text
Client Certificates
Bearer Tokens
Service Account Tokens
OIDC
Authentication Webhooks
Cloud Identity Integrations
```

The basic API request flow is:

```text
Client
  ↓
API Server
  ↓
Authentication
  ↓
Identity
  ↓
Authorization
  ↓
Admission
  ↓
Resource
```

Remember:

```text
Authentication
=
Who are you?
```

```text
Authorization
=
What can you do?
```

Human users commonly authenticate through:

```text
OIDC
Certificates
External Identity Providers
```

while workloads commonly use:

```text
Service Accounts
```

Service Account identities look like:

```text
system:serviceaccount:<namespace>:<name>
```

Modern Kubernetes uses short-lived, audience-bound Service Account tokens through mechanisms such as:

```text
TokenRequest
Projected Volumes
```

If a workload does not need Kubernetes API access, reduce credential exposure:

```yaml
automountServiceAccountToken: false
```

Kubeconfig connects:

```text
User
+
Cluster
+
Context
```

and should be protected because it can contain sensitive credentials.

OIDC provides an enterprise-friendly model:

```text
User
 ↓
Identity Provider
 ↓
OIDC
 ↓
Kubernetes
 ↓
RBAC
```

This enables:

```text
SSO
MFA
Centralized Identity
Group-Based Authorization
```

Authentication failures and authorization failures are different:

```text
401
 ↓
Authentication problem
```

```text
403
 ↓
Authorization problem
```

The most important production principle is:

> **Authenticate strongly, authorize minimally, use short-lived credentials, and avoid giving workloads credentials they do not need.**

A secure Kubernetes identity architecture therefore looks like:

```text
                    Strong Identity
                          │
                          ▼
                    Authentication
                          │
                          ▼
                    Short-Lived Credential
                          │
                          ▼
                     Least Privilege
                          │
                          ▼
                         RBAC
                          │
                          ▼
                       Auditing
                          │
                          ▼
                      Monitoring
```

This provides the foundation for the next security topic:

```text
Authentication
      ↓
Who are you?

Authorization
      ↓
What can you do?
```

---

## Next Chapter

# Chapter 48 – Authorization (RBAC)

Topics will include:

- What is Authorization?
- Authentication vs Authorization
- RBAC Fundamentals
- RBAC Objects
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
- Namespace-Scoped Permissions
- Cluster-Scoped Permissions
- Role Aggregation
- Default Roles
- `cluster-admin`
- Least Privilege
- RBAC Design Patterns
- RBAC for Applications
- RBAC for Developers
- RBAC for CI/CD
- RBAC for Security Teams
- RBAC Auditing
- `kubectl auth can-i`
- RBAC Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---