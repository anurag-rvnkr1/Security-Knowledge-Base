# Kubernetes Security

## Overview

Kubernetes Security is the practice of protecting Kubernetes clusters, workloads, control plane components, worker nodes, networking, storage, identities, secrets, and applications throughout their lifecycle.

Kubernetes (often abbreviated as **K8s**) is the industry's leading container orchestration platform. It automates container deployment, scaling, networking, service discovery, load balancing, storage management, and application availability across distributed infrastructure.

Because Kubernetes manages mission-critical applications and often hosts hundreds or thousands of containers, it has become one of the most attractive targets for attackers.

A Kubernetes environment consists of multiple interconnected components, each with its own security considerations:

- Control Plane
- Worker Nodes
- Pods
- Containers
- Services
- Namespaces
- etcd
- API Server
- Scheduler
- Controller Manager
- Kubelet
- Ingress Controllers
- Persistent Storage
- Networking
- Secrets
- RBAC
- Admission Controllers

A weakness in any of these components can potentially compromise the entire cluster.

Effective Kubernetes Security requires layered protection across:

- Cluster infrastructure
- Identity and Access Management
- Workload security
- Network security
- Secret management
- Image security
- Runtime protection
- Monitoring
- Compliance
- Incident response

Kubernetes Security is a foundational discipline for securing cloud-native applications and modern DevSecOps environments.

---

## Why It Matters

Kubernetes clusters frequently host:

- Customer-facing applications
- Enterprise APIs
- Databases
- Financial systems
- Healthcare platforms
- AI/ML workloads
- Internal business services
- DevOps infrastructure

Compromise of a Kubernetes cluster may allow attackers to:

- Access sensitive data
- Deploy malicious workloads
- Steal secrets
- Execute container escape attacks
- Move laterally across environments
- Disrupt production services
- Abuse cloud resources
- Deploy cryptominers
- Modify application behavior

Poor Kubernetes security can result in:

- Data breaches
- Service outages
- Regulatory violations
- Financial loss
- Reputation damage
- Software supply chain compromise

Strong Kubernetes Security enables organizations to:

- Secure cloud-native applications
- Reduce operational risk
- Improve workload isolation
- Protect sensitive information
- Enforce organizational security policies
- Improve resilience
- Support compliance initiatives
- Strengthen DevSecOps practices

Security should be integrated into every phase of cluster deployment and operation.

---

## Architecture

A secure Kubernetes architecture consists of multiple security layers protecting both infrastructure and workloads.

```
                   Users / Developers

                           │

                           ▼

                 Identity Authentication

                           │

                           ▼

                  Kubernetes API Server

                           │

        ┌──────────────────┼──────────────────┐

        ▼                  ▼                  ▼

 Authentication        Authorization      Admission

        │                  │                  │

        └──────────────────┼──────────────────┘

                           ▼

                    Control Plane

        ┌──────────────────┼──────────────────┐

        ▼                  ▼                  ▼

 Scheduler       Controller Manager         etcd

                           │

                           ▼

                    Worker Nodes

        ┌──────────────────┼──────────────────┐

        ▼                  ▼                  ▼

       Pod               Pod               Pod

        │                  │                  │

    Containers        Containers        Containers

        └──────────────────┼──────────────────┘

                           ▼

                Storage • Networking

                           ▼

               Monitoring • Logging • SIEM
```

Every layer must be secured because compromise of one component may impact the entire cluster.

---

## Key Concepts

### Kubernetes Cluster

A Kubernetes cluster consists of:

- Control Plane
- Worker Nodes
- Networking
- Storage
- Applications

```
Cluster

├── Control Plane

└── Worker Nodes
```

The cluster is the primary administrative boundary.

---

### Control Plane

The Control Plane manages the entire Kubernetes environment.

Primary components include:

- API Server
- Scheduler
- Controller Manager
- etcd

```
Control Plane

↓

Cluster Management
```

The control plane is the most critical component and must be highly protected.

---

### Worker Node

Worker nodes execute application workloads.

Each node typically contains:

- Kubelet
- Container runtime
- Pods
- Networking components

```
Worker Node

↓

Pods

↓

Containers
```

Node compromise may expose hosted workloads.

---

### Pod

A Pod is the smallest deployable unit in Kubernetes.

A pod may contain:

- One container
- Multiple tightly coupled containers

```
Pod

├── Container A

└── Container B
```

Pods share:

- Network namespace
- Storage volumes
- Process communication

---

### Namespace

Namespaces logically separate workloads inside a cluster.

Examples include:

- Production
- Development
- Testing
- Monitoring

```
Cluster

├── Production

├── Development

└── Testing
```

Namespaces improve workload isolation and administrative organization.

---

### API Server

The Kubernetes API Server is the central management interface.

Responsibilities include:

- Authentication
- Authorization
- Resource management
- Cluster administration

Every administrative request passes through the API Server.

---

### etcd

etcd is Kubernetes' distributed key-value database.

It stores:

- Cluster configuration
- Secrets
- RBAC policies
- Deployment information
- Node metadata

```
Cluster State

↓

etcd Database
```

Because etcd contains highly sensitive information, it should always be encrypted and access-controlled.

---

### Scheduler

The Scheduler determines where new pods should execute.

Scheduling decisions consider:

- CPU availability
- Memory
- Resource requests
- Node affinity
- Taints and tolerations

---

### Controller Manager

The Controller Manager continuously ensures that the cluster matches its desired state.

Examples include:

- Replica management
- Deployment reconciliation
- Node monitoring

Controllers automatically restore workloads after failures.

---

### Kubelet

Kubelet runs on every worker node.

Responsibilities include:

- Starting containers
- Monitoring pods
- Reporting node status
- Communicating with the API Server

```
API Server

↓

Kubelet

↓

Running Pods
```

Securing kubelet communication is essential.

---

### Role-Based Access Control (RBAC)

RBAC restricts user and service permissions.

```
User

↓

Role

↓

Permissions

↓

Cluster Resources
```

RBAC helps enforce the Principle of Least Privilege.

---

### Service Account

Applications running inside Kubernetes use Service Accounts to communicate with cluster resources.

Permissions should be carefully limited.

Avoid granting cluster-wide administrative privileges unless absolutely necessary.

---

### Admission Controllers

Admission Controllers validate and modify requests before resources are created.

They can enforce:

- Image policies
- Security policies
- Resource limits
- Namespace restrictions

Admission Controllers provide automated policy enforcement.

---

### Secrets

Secrets securely store sensitive information.

Examples:

- API keys
- Database credentials
- TLS certificates
- OAuth tokens
- Encryption keys

Secrets should never be hardcoded into container images or application code.

---

### Network Policies

Network Policies control pod-to-pod communication.

```
Pod A

↓

Network Policy

↓

Pod B
```

Only required network paths should be allowed.

---

### Persistent Volumes

Persistent Volumes provide long-term storage for workloads.

They should be:

- Encrypted
- Access-controlled
- Monitored
- Backed up

Storage security is critical because data persists beyond pod lifecycles.

---

### Pod Security

Pod Security focuses on limiting workload privileges.

Recommendations include:

- Non-root containers
- Read-only filesystems
- Dropped Linux capabilities
- Restricted host access
- Limited volume mounts

Pod Security significantly reduces attack surfaces.

---

### Audit Logging

Every significant Kubernetes event should be recorded.

Examples include:

- Authentication
- Resource creation
- Resource deletion
- Role changes
- Secret access
- Pod deployments
- API requests

```
Cluster Event

↓

Audit Log

↓

SIEM

↓

SOC Analyst
```

Audit logs support compliance, threat detection, and forensic investigations.

---

## How It Works

Kubernetes Security protects containerized workloads by applying layered security controls across the cluster lifecycle. Security begins before workloads are deployed and continues through scheduling, runtime protection, monitoring, updates, and eventual removal.

Every request to the Kubernetes cluster passes through multiple validation and authorization stages before workloads are allowed to execute.

A secure Kubernetes workflow typically includes:

1. Authenticate the user or workload
2. Authorize requested actions
3. Validate admission policies
4. Schedule workloads securely
5. Protect pods and containers
6. Secure networking and storage
7. Monitor runtime activity
8. Detect and respond to threats

This defense-in-depth approach helps reduce the likelihood and impact of cluster compromise.

---

## Kubernetes Security Workflow

```
               User / CI/CD Pipeline

                        │

                        ▼

                Authentication

                        │

                        ▼

              Kubernetes API Server

                        │

                        ▼

               RBAC Authorization

                        │

                        ▼

            Admission Controllers

                        │

                        ▼

             Scheduler Validation

                        │

                        ▼

                Worker Node

                        │

                        ▼

                     Pod

                        │

                        ▼

                  Container

                        │

                        ▼

     Logging • Monitoring • Runtime Security

                        │

                        ▼

                 SIEM / SOC Platform
```

Each request is evaluated before workloads are allowed to execute inside the cluster.

---

## Step 1 – Authenticate the User

Every request to Kubernetes begins with authentication.

Authentication methods include:

- Client certificates
- OpenID Connect (OIDC)
- Cloud IAM integration
- Service accounts
- Identity providers

```
Administrator

↓

Authentication

↓

Verified Identity
```

Unauthenticated requests should be rejected immediately.

---

## Step 2 – Authorize the Request

After successful authentication, Kubernetes evaluates permissions using RBAC.

```
Identity

↓

RBAC

↓

Allowed?

↓

Yes / No
```

Authorization determines whether a user or workload may:

- Deploy pods
- Read secrets
- Create namespaces
- Modify services
- Delete workloads
- Access logs

Least Privilege should govern all permissions.

---

## Step 3 – Admission Control

Admission Controllers inspect requests before resources are created.

Typical policy checks include:

- Trusted image registry
- Image signature verification
- Resource limits
- Pod Security requirements
- Namespace restrictions

```
Deployment Request

↓

Admission Controller

↓

Policy Validation

↓

Approved
```

Requests violating organizational policies should be denied.

---

## Step 4 – Schedule the Pod

The Scheduler selects an appropriate worker node.

Scheduling decisions consider:

- CPU availability
- Memory
- Resource requests
- Node affinity
- Taints and tolerations
- Security constraints

```
Pod

↓

Scheduler

↓

Worker Node
```

Only eligible nodes receive the workload.

---

## Step 5 – Start the Container

The kubelet on the selected worker node starts the container.

```
Worker Node

↓

Kubelet

↓

Container Runtime

↓

Running Pod
```

Before startup:

- Images are downloaded
- Signatures may be verified
- Runtime configuration is applied

---

## Step 6 – Configure Networking

Each pod receives networking resources.

Security controls include:

- Network Policies
- Service Mesh
- Firewalls
- Mutual TLS
- DNS controls

```
Pod A

↓

Network Policy

↓

Pod B
```

Only approved communication paths should be permitted.

---

## Step 7 – Mount Storage Securely

If persistent storage is required:

```
Persistent Volume

↓

Encrypted Storage

↓

Running Pod
```

Storage protections include:

- Encryption
- Access control
- Backup
- Audit logging

---

## Step 8 – Inject Secrets Securely

Applications frequently require credentials.

Instead of embedding them into images:

```
Secrets Manager

↓

Kubernetes Secret

↓

Running Pod
```

Secrets should be:

- Encrypted
- Access-controlled
- Rotated regularly

---

## Step 9 – Runtime Protection

Runtime security continuously observes workload behavior.

Examples include:

- Unexpected processes
- Privilege escalation
- File modifications
- Container escape attempts
- Suspicious network traffic

```
Running Pod

↓

Runtime Monitoring

↓

Threat Detection
```

Behavioral monitoring complements preventive controls.

---

## Step 10 – Audit Logging

Cluster activity should be recorded.

Examples:

- Authentication events
- Pod creation
- Secret access
- RBAC changes
- Deployment updates
- Namespace creation
- API requests

```
Cluster Event

↓

Audit Log

↓

SIEM

↓

SOC Investigation
```

Audit logging supports compliance and incident response.

---

## Kubernetes Deployment Lifecycle

```
Develop

↓

Build Image

↓

Scan Image

↓

Sign Image

↓

Store Registry

↓

Deploy

↓

Monitor

↓

Update

↓

Retire
```

Security validation should occur throughout the deployment lifecycle.

---

## Rolling Update Workflow

```
Current Pods

↓

Deploy New Version

↓

Health Check

↓

Traffic Shift

↓

Old Pods Removed
```

Rolling updates minimize downtime while maintaining application availability.

---

## Secret Management Workflow

```
Application

↓

Request Secret

↓

Kubernetes Secret

↓

Authorized Access

↓

Application Starts
```

Only authorized workloads should retrieve sensitive information.

---

## Node Communication Workflow

```
Control Plane

↓

API Server

↓

Kubelet

↓

Worker Node

↓

Running Pods
```

All node communication should be authenticated and encrypted.

---

## Practical Example

### Example 1 – Secure Web Application Deployment

A company deploys an e-commerce application.

```
Developer

↓

CI/CD Pipeline

↓

Image Scan

↓

Private Registry

↓

Kubernetes Deployment
```

Security controls include:

- Signed container images
- RBAC
- Network Policies
- Runtime monitoring

---

### Example 2 – Restricting Secret Access

A payment application requires database credentials.

```
Payment Pod

↓

Authorized Service Account

↓

Secret Retrieved

↓

Database Connection
```

Only the payment workload receives the required credentials.

---

### Example 3 – Blocking an Untrusted Image

A deployment references an image from an unapproved registry.

```
Deployment

↓

Admission Controller

↓

Policy Violation

↓

Deployment Rejected
```

Policy enforcement prevents insecure workloads from entering production.

---

### Example 4 – Runtime Threat Detection

A compromised container launches an unexpected shell.

```
Pod

↓

Unexpected Process

↓

Runtime Detection

↓

Security Alert
```

The security team investigates before the threat spreads.

---

### Example 5 – Network Isolation

A database pod should only communicate with application pods.

```
Application Pods

↓

Network Policy

↓

Database Pod
```

All other communication attempts are denied.

---

## Kubernetes Security Components

| Component | Purpose |
|-----------|---------|
| API Server | Central management interface |
| RBAC | Authorization and access control |
| Admission Controllers | Policy enforcement |
| Scheduler | Secure workload placement |
| Kubelet | Node-level workload management |
| etcd | Secure cluster state storage |
| Secrets | Credential management |
| Network Policies | Pod communication control |
| Persistent Volumes | Secure storage |
| Runtime Security | Threat detection during execution |

---

## Indicators of Kubernetes Compromise (Detection)

Continuous monitoring is essential because Kubernetes environments are dynamic, distributed, and frequently changing.

---

### Unauthorized API Requests

Unexpected API activity may indicate:

- Credential compromise
- Privilege escalation
- Automated attacks
- Unauthorized administrators

```
API Request

↓

Unexpected Identity

↓

Security Alert
```

---

### Suspicious RBAC Changes

Unexpected creation or modification of:

- ClusterRoles
- Roles
- RoleBindings
- ClusterRoleBindings

may indicate attempts to gain elevated privileges.

---

### Privileged Pod Deployments

Monitor for pods that:

- Run as root
- Request privileged mode
- Mount the host filesystem
- Access host networking
- Add dangerous Linux capabilities

Such deployments should be uncommon and carefully reviewed.

---

### Unauthorized Secret Access

Unexpected access to Kubernetes Secrets may indicate:

- Credential theft
- Insider activity
- Compromised service accounts
- Malicious workloads

Secret access events should be audited continuously.

---

### Unexpected Pod Creation

Unexpected workloads may indicate:

- Malware
- Cryptominers
- Backdoors
- Unauthorized deployments

Monitor:

- New namespaces
- New deployments
- Unknown container images
- Unexpected replica counts

---

### Container Escape Indicators

Detect activity suggesting attempts to access:

- Host filesystem
- Host kernel
- Host namespaces
- Container runtime interfaces

Container escape attempts require immediate investigation.

---

### Image Integrity Violations

Monitor for:

- Unsigned images
- Unknown registries
- Modified images
- Failed signature verification

Image integrity protects against software supply chain attacks.

---

### Network Anomalies

Unexpected communication between:

- Namespaces
- Pods
- Worker nodes
- External networks

may indicate lateral movement or data exfiltration.

---

### etcd Access Attempts

Direct or unexpected access to etcd is highly suspicious because it stores:

- Cluster configuration
- Secrets
- RBAC policies
- Certificates

Access should be tightly controlled and monitored.

---

### Audit Log Monitoring

Security teams should monitor:

- Authentication failures
- RBAC modifications
- Secret access
- Namespace creation
- Pod deployments
- API requests
- Admission controller denials
- Worker node changes
- Network policy modifications

---

## Detection Best Practices

- Enable Kubernetes audit logging.
- Monitor RBAC and service account changes.
- Alert on privileged pod deployments.
- Detect unexpected API requests.
- Verify image signatures before execution.
- Monitor runtime process behavior continuously.
- Analyze network traffic between namespaces.
- Monitor etcd access attempts.
- Integrate Kubernetes logs with the organization's SIEM.
- Establish behavioral baselines for workloads.

---

## Next Section

Prevention

Best Practices

Common Mistakes

References

---