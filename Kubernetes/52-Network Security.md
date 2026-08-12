# Chapter 52 – Network Security

## Overview

Kubernetes networking allows Pods, Services, Nodes, and external systems to communicate with one another.

However, unrestricted connectivity can create significant security risks.

A compromised Pod may attempt to:

```text
Scan other Pods
Access internal Services
Reach databases
Contact the Kubernetes API
Exfiltrate data
Move laterally
```

Kubernetes network security aims to control:

```text
Who can communicate
With whom
On which ports
Using which protocols
In which direction
```

The primary Kubernetes-native mechanism for workload network isolation is:

```text
NetworkPolicy
```

Network security can be strengthened further with:

```text
CNI enforcement
Encryption
mTLS
Service Mesh
Egress Controls
DNS Security
Network Monitoring
Firewalls
Cloud Security Groups
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes network security fundamentals
- Pod network security
- Service network security
- NetworkPolicy
- Default-deny policies
- Ingress rules
- Egress rules
- Namespace selectors
- Pod selectors
- IP blocks
- Network segmentation
- Zero-trust networking
- NetworkPolicy limitations
- CNI enforcement
- DNS security
- Service discovery security
- East-west traffic
- North-south traffic
- Network encryption
- mTLS
- Service mesh security
- Network isolation
- Multi-tenant networking
- Egress control
- Ingress control
- API Server network security
- CNI security
- Network monitoring
- Network troubleshooting
- Common attack paths
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is Kubernetes Network Security?

Kubernetes network security controls communication between:

```text
Pods
Services
Namespaces
Nodes
External Systems
```

A simplified model:

```text
                   Kubernetes Cluster
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
        Pod A          Pod B          Pod C
          │              │              │
          └────── Network Policies ─────┘
                         │
                         ▼
                  Allowed / Denied
```

---

# Why Network Security Matters

Without network restrictions:

```text
Compromised Pod
      ↓
Network Scan
      ↓
Internal Services
      ↓
Database
      ↓
Credential Theft
      ↓
Lateral Movement
```

Network segmentation can reduce this attack path.

---

# Kubernetes Network Security Model

Kubernetes networking generally follows the principle that Pods can communicate with one another, subject to the network implementation and policies configured.

Security policies can change this behavior.

Conceptually:

```text
Pod A ───────────────► Pod B
        Allowed

Pod A ───────────────X Pod C
        Denied
```

---

# Network Security Layers

A production Kubernetes environment may use:

```text
NetworkPolicy
      +
CNI
      +
Cloud Firewall
      +
Security Groups
      +
Service Mesh
      +
mTLS
      +
Ingress Controls
      +
Egress Controls
      +
Monitoring
```

---

# NetworkPolicy

A Kubernetes:

```text
NetworkPolicy
```

defines rules controlling network traffic to and/or from selected Pods.

NetworkPolicy can control:

```text
Ingress
Egress
```

depending on the policy configuration.

---

# Basic NetworkPolicy Structure

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: backend-policy

  namespace: production

spec:

  podSelector:

    matchLabels:

      app: backend

  policyTypes:

  - Ingress

  - Egress
```

This selects:

```text
backend Pods
```

and establishes policy for:

```text
Ingress
Egress
```

The actual allow rules must then be defined.

---

# NetworkPolicy Components

Important fields include:

```text
podSelector
namespaceSelector
ipBlock
ingress
egress
policyTypes
```

---

# `podSelector`

Selects Pods within the NetworkPolicy's namespace.

Example:

```yaml
podSelector:

  matchLabels:

    app: backend
```

This targets:

```text
backend Pods
```

---

# `namespaceSelector`

Selects namespaces based on labels.

Example:

```yaml
namespaceSelector:

  matchLabels:

    environment: production
```

This can allow communication from selected namespaces.

---

# `ipBlock`

Selects IP address ranges.

Example:

```yaml
ipBlock:

  cidr: 10.0.0.0/8
```

This can allow traffic from a specified IP range.

---

# Ingress

Ingress means:

```text
Traffic entering a Pod
```

Example:

```text
Frontend
   │
   ▼
Backend Pod
```

The traffic arriving at:

```text
Backend
```

is:

```text
Ingress
```

---

# Egress

Egress means:

```text
Traffic leaving a Pod
```

Example:

```text
Backend Pod
   │
   ▼
Database
```

The traffic leaving:

```text
Backend
```

is:

```text
Egress
```

---

# Ingress vs Egress

| Direction | Meaning |
|---|---|
| Ingress | Incoming traffic |
| Egress | Outgoing traffic |

Example:

```text
Frontend → Backend
```

For Backend:

```text
Ingress
```

For Frontend:

```text
Egress
```

---

# Default-Allow Behavior

If no NetworkPolicy selects a Pod for a particular direction, traffic is generally not restricted by NetworkPolicy for that direction.

For example:

```text
No ingress policy
 ↓
Ingress not isolated
```

This is why production clusters often use:

```text
Default Deny
```

patterns.

---

# Default-Deny Ingress

A namespace-wide ingress isolation pattern:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny-ingress

spec:

  podSelector: {}

  policyTypes:

  - Ingress
```

The empty:

```yaml
podSelector: {}
```

selects all Pods in the namespace.

This establishes ingress isolation for those Pods.

---

# Default-Deny Egress

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny-egress

spec:

  podSelector: {}

  policyTypes:

  - Egress
```

This establishes egress isolation for all selected Pods.

---

# Default-Deny Both Directions

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny-all

spec:

  podSelector: {}

  policyTypes:

  - Ingress

  - Egress
```

This is a common starting point for strict segmentation.

However, you must then explicitly allow required traffic.

---

# Why Default Deny Is Important

Without default deny:

```text
Compromised Pod
      ↓
Potentially broad network reach
```

With default deny:

```text
Compromised Pod
      ↓
NetworkPolicy
      ↓
Only explicitly allowed traffic
```

This supports:

```text
Least Privilege Networking
```

---

# Allowing Ingress

Suppose:

```text
frontend
```

needs to access:

```text
backend
```

Backend policy:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: backend-ingress

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

This allows:

```text
frontend
   │
   │ TCP/8080
   ▼
backend
```

---

# Namespace-Scoped Pod Selector

An important detail:

```yaml
podSelector:
```

inside a NetworkPolicy refers to Pods in the same namespace unless combined with a `namespaceSelector`.

Example:

```yaml
from:

- podSelector:

    matchLabels:

      app: frontend
```

means:

```text
frontend Pods
in the policy's namespace
```

---

# Cross-Namespace Access

To allow Pods from another namespace:

```yaml
from:

- namespaceSelector:

    matchLabels:

      team: frontend
```

You can combine selectors.

---

# Namespace + Pod Selector

Example:

```yaml
from:

- namespaceSelector:

    matchLabels:

      team: frontend

  podSelector:

    matchLabels:

      app: frontend
```

This means:

```text
Pods with:
app=frontend

inside namespaces with:
team=frontend
```

---

# Important Selector Semantics

Consider:

```yaml
from:

- namespaceSelector:
    matchLabels:
      team: frontend

  podSelector:
    matchLabels:
      app: frontend
```

The namespace and Pod selectors in the same list item are combined.

Conceptually:

```text
Namespace matches
        AND
Pod matches
```

---

# Separate Selector Entries

If you write:

```yaml
from:

- namespaceSelector:
    matchLabels:
      team: frontend

- podSelector:
    matchLabels:
      app: frontend
```

the entries represent alternative sources.

Conceptually:

```text
Namespace matches
        OR
Pod matches
```

This distinction is important.

---

# Allowing Egress

Suppose:

```text
backend
```

needs to access:

```text
database
```

Example:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: backend-egress

spec:

  podSelector:

    matchLabels:

      app: backend

  policyTypes:

  - Egress

  egress:

  - to:

    - podSelector:

        matchLabels:

          app: database

    ports:

    - protocol: TCP

      port: 5432
```

Architecture:

```text
Backend
  │
  │ TCP/5432
  ▼
Database
```

---

# Three-Tier Application

Consider:

```text
Internet
   ↓
Frontend
   ↓
Backend
   ↓
Database
```

Network policies can enforce:

```text
Internet → Frontend
Frontend → Backend
Backend → Database
```

while blocking:

```text
Frontend → Database
Backend → Frontend
Database → Frontend
```

unless explicitly required.

---

# Three-Tier Security Model

```text
                  Internet
                     │
                     ▼
                 Frontend
                     │
                  TCP/8080
                     │
                     ▼
                  Backend
                     │
                  TCP/5432
                     │
                     ▼
                 Database
```

This is network segmentation.

---

# Zero-Trust Networking

A zero-trust approach assumes:

```text
No network connection is trusted automatically.
```

Instead:

```text
Identity
+
Policy
+
Context
=
Access
```

In Kubernetes:

```text
Pod A
 ↓
NetworkPolicy
 ↓
Is Pod A allowed to reach Pod B?
```

---

# Zero-Trust Principle

Instead of:

```text
Everything inside cluster = trusted
```

use:

```text
Everything denied by default
 ↓
Explicitly allow required communication
```

---

# Network Segmentation

Network segmentation divides workloads into logical security zones.

Example:

```text
Public
 └── frontend

Application
 └── backend

Data
 └── database
```

Policies control traffic between these zones.

---

# Namespace Segmentation

Namespaces can represent security boundaries.

Example:

```text
frontend
backend
database
```

Network policies can restrict communication across them.

---

# Multi-Tenant Networking

Consider:

```text
Tenant A
 ├── frontend
 └── backend

Tenant B
 ├── frontend
 └── backend
```

Network policies can prevent:

```text
Tenant A → Tenant B
```

while allowing:

```text
Tenant A frontend → Tenant A backend
```

---

# Tenant Isolation

A strict architecture might be:

```text
Tenant A
   │
   └── Default Deny
         │
         ├── frontend → backend
         └── backend → database

Tenant B
   │
   └── Default Deny
         │
         ├── frontend → backend
         └── backend → database
```

---

# NetworkPolicy and Services

NetworkPolicy applies to Pod traffic.

Services provide:

```text
Stable Network Endpoint
```

Example:

```text
frontend
   ↓
backend Service
   ↓
backend Pods
```

The policy controls traffic involving the selected Pods.

---

# NetworkPolicy Does Not Replace Services

These solve different problems.

```text
Service
=
Discovery + Stable Endpoint
```

```text
NetworkPolicy
=
Traffic Authorization
```

---

# NetworkPolicy and Ingress Controllers

External traffic may follow:

```text
Internet
   ↓
LoadBalancer
   ↓
Ingress Controller
   ↓
Service
   ↓
Application Pod
```

NetworkPolicy can control traffic between these components.

---

# North-South Traffic

Traffic entering or leaving the cluster is often called:

```text
North-South
```

Example:

```text
Internet
   ↓
Cluster
```

---

# East-West Traffic

Traffic between workloads inside the cluster is commonly called:

```text
East-West
```

Example:

```text
Frontend
   ↓
Backend
   ↓
Database
```

---

# Network Security Focus

North-South:

```text
Ingress
Egress
Load Balancer
Firewall
WAF
Gateway
```

East-West:

```text
NetworkPolicy
mTLS
Service Mesh
Segmentation
```

---

# Egress Security

Egress controls outbound traffic.

Without egress restrictions:

```text
Compromised Pod
      ↓
Internet
      ↓
Attacker C2
```

A default-deny egress policy can reduce this risk.

---

# Egress Allowlist

Example:

```text
Backend
 ↓
DNS
 ↓
Approved API
 ↓
Database
```

while blocking:

```text
Backend
 ↓
Unknown Internet Destination
```

---

# Egress to the Internet

If a workload needs Internet access, explicitly define what is required.

Possible controls include:

```text
NetworkPolicy
Egress Gateway
Firewall
Proxy
Cloud NAT
DNS filtering
```

---

# DNS Security

Kubernetes applications commonly use DNS for service discovery.

Example:

```text
backend.default.svc.cluster.local
```

DNS is therefore part of the network security model.

---

# DNS Traffic

Applications generally need to reach the cluster DNS service.

If egress is denied:

```text
Pod
 ↓
DNS
 ↓
Blocked
```

service discovery may fail.

---

# DNS Egress Example

A strict egress policy may need to allow traffic to the DNS service.

A common conceptual pattern:

```yaml
egress:

- to:

  - namespaceSelector: {}

    podSelector:

      matchLabels:

        k8s-app: kube-dns

  ports:

  - protocol: UDP

    port: 53

  - protocol: TCP

    port: 53
```

The exact DNS labels vary by Kubernetes distribution and cluster configuration.

---

# DNS Security Risks

Attackers may attempt:

```text
DNS tunneling
DNS spoofing
Malicious resolution
Data exfiltration
Internal service enumeration
```

Additional controls may include:

```text
DNS logging
DNS filtering
NetworkPolicy
Secure DNS infrastructure
```

---

# CNI and NetworkPolicy

NetworkPolicy requires network implementation support.

The:

```text
CNI plugin
```

is typically responsible for implementing network behavior and policy enforcement.

Examples of CNIs with NetworkPolicy capabilities include:

```text
Cilium
Calico
Antrea
```

Capabilities vary by CNI and configuration.

---

# NetworkPolicy Limitation

NetworkPolicy is intentionally focused on network-layer access control.

It does not automatically provide:

```text
Application-layer authentication
mTLS
Identity verification
HTTP authorization
Payload inspection
```

For those requirements, additional controls may be needed.

---

# CNI Enforcement

The CNI may enforce NetworkPolicy using mechanisms such as:

```text
iptables
eBPF
OVS
Other dataplane technologies
```

Implementation depends on the CNI.

---

# Cilium Example

A CNI such as:

```text
Cilium
```

can provide advanced network security and observability using eBPF.

It can support capabilities beyond basic Kubernetes NetworkPolicy.

---

# Calico Example

Calico provides:

```text
NetworkPolicy
Network Security
Routing
Observability
```

depending on the deployment model and configuration.

---

# Network Encryption

NetworkPolicy answers:

```text
Who can communicate?
```

Encryption answers:

```text
Can an attacker read the traffic?
```

These are different controls.

---

# Encryption in Transit

Example:

```text
Frontend
   │
   │ Encrypted
   ▼
Backend
```

Common technologies:

```text
TLS
mTLS
IPsec
WireGuard
```

Support depends on the networking architecture.

---

# mTLS

mTLS means:

```text
Mutual TLS
```

Both sides authenticate one another.

Conceptually:

```text
Client
  ↕
TLS
  ↕
Server
```

with both identities authenticated.

---

# NetworkPolicy vs mTLS

| Technology | Primary Purpose |
|---|---|
| NetworkPolicy | Network access control |
| TLS | Encryption |
| mTLS | Encryption + mutual identity |
| Service Mesh | Traffic management + security |

They can complement one another.

---

# Service Mesh Security

A service mesh can provide:

```text
mTLS
Identity
Traffic Policies
Authorization
Observability
```

Architecture:

```text
Application
    │
    ▼
Sidecar / Data Plane
    │
    ▼
Encrypted Traffic
    │
    ▼
Destination Proxy
    │
    ▼
Application
```

---

# Network Security with Service Mesh

A mature architecture may use:

```text
NetworkPolicy
     +
mTLS
     +
Service Mesh Authorization
```

This provides multiple layers.

---

# NetworkPolicy Limitations

NetworkPolicy implementations may differ across CNIs.

Some environments may support additional capabilities beyond the standard Kubernetes NetworkPolicy API.

Do not assume every CNI supports every advanced networking feature.

---

# NetworkPolicy and Node Traffic

NetworkPolicy is primarily about Pod traffic.

It should not be treated as a complete replacement for:

```text
Node firewall
Cloud firewall
Security groups
Host firewall
```

---

# API Server Network Security

The Kubernetes API Server is a highly sensitive endpoint.

Protect it using:

```text
TLS
Authentication
Authorization
Network Access Control
Firewall
Private Endpoints
Audit Logging
```

---

# Restrict API Server Exposure

Avoid unnecessarily exposing the API Server publicly.

Where possible:

```text
Private Network
+
VPN / Zero Trust Access
+
Strong Authentication
```

can reduce attack surface.

---

# Network Security Architecture

```text
                       Internet
                           │
                           ▼
                         WAF
                           │
                           ▼
                     Load Balancer
                           │
                           ▼
                   Ingress / Gateway
                           │
                           ▼
                       Frontend
                           │
                       NetworkPolicy
                           │
                           ▼
                        Backend
                           │
                       NetworkPolicy
                           │
                           ▼
                       Database
```

---

# Network Security Layers

```text
Internet Firewall
       ↓
WAF / Gateway
       ↓
Ingress Control
       ↓
NetworkPolicy
       ↓
mTLS
       ↓
Application Authorization
       ↓
Runtime Monitoring
```

---

# Common Attack Path

A common lateral movement scenario:

```text
Public Application
      ↓
Application Vulnerability
      ↓
Container Compromise
      ↓
Internal Network Scan
      ↓
Backend Discovery
      ↓
Database Access
```

Network segmentation can interrupt this chain.

---

# NetworkPolicy Defense

```text
Compromised Frontend
        ↓
Attempt Backend
        ↓
NetworkPolicy
        ↓
Allowed only on required port
```

and:

```text
Compromised Frontend
        ↓
Attempt Database
        ↓
NetworkPolicy
        ↓
DENIED
```

---

# Network Monitoring

Monitor:

```text
Connections
Denied Traffic
Unexpected Destinations
DNS Queries
Egress
Internal Scanning
Port Scans
```

Tools can include:

```text
CNI Observability
Flow Logs
Prometheus
Grafana
eBPF-based Monitoring
Cloud Flow Logs
```

---

# Network Security and Observability

A security monitoring architecture:

```text
Network Traffic
      ↓
CNI / Flow Logs
      ↓
Metrics / Logs
      ↓
Monitoring
      ↓
Alert
      ↓
Security Investigation
```

---

# Detecting Lateral Movement

Potential indicators:

```text
One Pod contacting many Services
Unexpected port scanning
Access to unrelated namespaces
Unexpected DNS lookups
High outbound traffic
Connections to external IPs
```

---

# Detecting Data Exfiltration

Indicators can include:

```text
Unexpected egress
Large outbound transfers
Unknown destinations
DNS tunneling
Repeated connections
```

Combine:

```text
NetworkPolicy
+
Egress Control
+
Monitoring
```

---

# Network Troubleshooting

If:

```text
Pod A cannot reach Pod B
```

check:

```text
1. Pod status
2. Service
3. DNS
4. NetworkPolicy
5. CNI
6. Ports
7. Endpoints
8. Routing
9. Firewall
10. Security Groups
```

---

# Check NetworkPolicies

```bash
kubectl get networkpolicies -A
```

or:

```bash
kubectl get netpol -A
```

---

# Describe NetworkPolicy

```bash
kubectl describe networkpolicy <name>
```

---

# Check Pod Labels

```bash
kubectl get pods --show-labels
```

This is critical because NetworkPolicy selectors depend on labels.

---

# Check Services

```bash
kubectl get svc
```

---

# Check Endpoints

```bash
kubectl get endpoints
```

or:

```bash
kubectl get endpointslices
```

---

# Test DNS

From a test Pod:

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
```

or:

```bash
kubectl exec -it <pod> -- getent hosts kubernetes.default
```

depending on the image.

---

# Test Connectivity

From a test container:

```bash
kubectl exec -it <pod> -- curl http://backend:8080
```

For a TCP port:

```bash
kubectl exec -it <pod> -- nc -vz backend 8080
```

Only use tools available in the image.

---

# NetworkPolicy Troubleshooting Flow

```text
Connection Failure
       ↓
DNS?
       ↓
Service?
       ↓
Endpoint?
       ↓
Pod?
       ↓
NetworkPolicy?
       ↓
CNI?
       ↓
Firewall?
       ↓
Application?
```

---

# Common NetworkPolicy Mistake

A developer creates:

```text
Default Deny Egress
```

but forgets DNS.

Result:

```text
Application
 ↓
DNS
 ↓
Blocked
 ↓
Service discovery fails
```

Always account for required DNS traffic.

---

# Common NetworkPolicy Mistake

A policy allows:

```text
frontend → backend
```

but backend's return traffic is not properly considered.

Network policies are stateful in typical implementations, but policies still need to be designed correctly for the traffic flows and CNI behavior.

---

# Common NetworkPolicy Mistake

Wrong labels:

```yaml
matchLabels:

  app: front-end
```

while the Pod actually has:

```text
app=frontend
```

Result:

```text
No match
```

Always verify:

```bash
kubectl get pods --show-labels
```

---

# Common NetworkPolicy Mistake

Assuming:

```text
NetworkPolicy = Firewall
```

NetworkPolicy is a Kubernetes abstraction and its exact capabilities depend on the CNI implementation.

---

# Hands-on Lab 1 – Default Deny

Create:

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

Apply:

```bash
kubectl apply -f default-deny.yaml
```

Test application connectivity.

---

# Hands-on Lab 2 – Allow Frontend to Backend

Create:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: backend-ingress

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

Test:

```text
frontend → backend
```

and:

```text
other-pod → backend
```

---

# Hands-on Lab 3 – Allow Backend to Database

Create:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: database-ingress

spec:

  podSelector:

    matchLabels:

      app: database

  policyTypes:

  - Ingress

  ingress:

  - from:

    - podSelector:

        matchLabels:

          app: backend

    ports:

    - protocol: TCP

      port: 5432
```

Test:

```text
backend → database
```

and:

```text
frontend → database
```

---

# Hands-on Lab 4 – Namespace Isolation

Create:

```text
team-a
team-b
```

Deploy Pods in each namespace.

Apply:

```text
Default Deny
```

Then explicitly allow:

```text
team-a → team-a
```

and deny:

```text
team-a → team-b
```

---

# Hands-on Lab 5 – DNS Egress

Apply default-deny egress.

Observe:

```text
DNS failure
```

Then create an egress rule allowing DNS traffic to the cluster DNS service.

Test:

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
```

---

# Hands-on Lab 6 – Egress Restriction

Create a workload with:

```text
Default Deny Egress
```

Allow only:

```text
DNS
Database
Approved API
```

Test an unauthorized destination.

Expected:

```text
Connection denied
```

---

# Hands-on Lab 7 – Network Segmentation

Build:

```text
Frontend
Backend
Database
```

Implement:

```text
Frontend → Backend
Backend → Database
```

Block:

```text
Frontend → Database
Database → Frontend
```

Verify the communication matrix.

---

# Hands-on Lab 8 – Inspect Network Policies

Run:

```bash
kubectl get networkpolicies -A
```

Then:

```bash
kubectl describe networkpolicy <name>
```

Document:

```text
Selected Pods
Ingress Rules
Egress Rules
Ports
Selectors
```

---

# Hands-on Lab 9 – Network Troubleshooting

Intentionally create an incorrect label:

```text
app=front-end
```

while the policy expects:

```text
app=frontend
```

Observe the connection failure.

Fix the label and test again.

---

# Hands-on Lab 10 – Security Review

For a production namespace, answer:

```text
1. Is ingress default-deny?
2. Is egress default-deny?
3. Which Pods can communicate?
4. Which namespaces can communicate?
5. Which external destinations are allowed?
6. Is DNS restricted?
7. Is API Server access restricted?
8. Is traffic encrypted?
9. Is network traffic monitored?
10. Are unexpected flows alerted?
```

---

# Common Mistakes

## 1. No Default Deny

Unrestricted traffic increases lateral movement risk.

---

## 2. Forgetting DNS

Strict egress policies can break service discovery.

---

## 3. Wrong Pod Labels

NetworkPolicy selectors depend on labels.

---

## 4. Forgetting Egress

Ingress restrictions do not automatically restrict outbound traffic.

---

## 5. Assuming NetworkPolicy Encrypts Traffic

NetworkPolicy controls traffic authorization.

It does not inherently encrypt traffic.

---

## 6. Assuming NetworkPolicy Provides Authentication

NetworkPolicy does not prove application identity.

Use:

```text
mTLS
Service Mesh
Application Authentication
```

when required.

---

## 7. Allowing Entire CIDRs

Avoid unnecessarily broad:

```text
0.0.0.0/0
```

rules.

---

## 8. Ignoring CNI Capabilities

Different CNIs provide different networking features.

---

## 9. Forgetting Return Traffic Requirements

Understand the actual connection flow and CNI behavior.

---

## 10. Treating Internal Traffic as Trusted

Internal network traffic can be hostile after a workload compromise.

---

# Best Practices

### 1. Start With Default Deny

Use:

```text
Ingress
Egress
```

policies wherever practical.

---

### 2. Explicitly Allow Required Communication

Use:

```text
Least Privilege
```

for networking.

---

### 3. Segment by Application

Separate:

```text
Frontend
Backend
Database
```

---

### 4. Segment by Namespace

Use namespaces as organizational and security boundaries.

---

### 5. Restrict Egress

Prevent unnecessary Internet access.

---

### 6. Protect DNS

Allow only required DNS traffic.

---

### 7. Use mTLS for Sensitive Application Traffic

NetworkPolicy and encryption solve different problems.

---

### 8. Monitor Network Flows

Detect:

```text
Unexpected Connections
Scanning
Exfiltration
Lateral Movement
```

---

### 9. Protect the API Server

Use:

```text
TLS
Strong Authentication
RBAC
Network Restrictions
Audit Logging
```

---

### 10. Use a Security-Capable CNI

Choose a CNI based on requirements such as:

```text
NetworkPolicy
Observability
Encryption
Performance
eBPF
Advanced Security
```

---

### 11. Test Policies Before Production

Validate:

```text
Allowed Traffic
Denied Traffic
DNS
External APIs
Monitoring
```

---

### 12. Document Communication Flows

Maintain a matrix:

| Source | Destination | Port | Protocol | Purpose |
|---|---|---:|---|---|
| Frontend | Backend | 8080 | TCP | API |
| Backend | Database | 5432 | TCP | Database |
| Application | DNS | 53 | UDP/TCP | DNS |
| Backend | External API | 443 | TCP | External service |

---

# Zero-Trust Kubernetes Architecture

```text
                  Internet
                     │
                     ▼
                  Gateway
                     │
                     ▼
                 Frontend
                     │
                NetworkPolicy
                     │
                     ▼
                 Backend
                     │
                NetworkPolicy
                     │
                     ▼
                 Database
```

Each connection is:

```text
Explicitly Allowed
```

rather than:

```text
Implicitly Trusted
```

---

# Network Security Threat Model

Potential threats:

```text
Port Scanning
Lateral Movement
Data Exfiltration
DNS Tunneling
C2 Communication
Unauthorized Service Access
API Server Access
Cross-Tenant Communication
```

Controls:

```text
NetworkPolicy
Firewall
CNI
mTLS
Egress Gateway
DNS Security
Monitoring
```

---

# Production Network Security Checklist

```text
☑ Default-deny ingress
☑ Default-deny egress where practical
☑ Explicit application flows
☑ Namespace segmentation
☑ Tenant isolation
☑ DNS access controlled
☑ External egress restricted
☑ API Server protected
☑ Sensitive traffic encrypted
☑ mTLS where appropriate
☑ Network flows monitored
☑ CNI supports required policies
☑ Cloud firewall configured
☑ Security groups reviewed
☑ Unauthorized traffic alerted
☑ NetworkPolicy tested
```

---

# Quick Revision

## NetworkPolicy

```text
Controls Pod traffic
```

---

## Ingress

```text
Incoming traffic
```

---

## Egress

```text
Outgoing traffic
```

---

## Pod Selector

```text
Select Pods
```

---

## Namespace Selector

```text
Select namespaces
```

---

## IP Block

```text
Select CIDR ranges
```

---

## Default Deny

```text
Deny unless explicitly allowed
```

---

## East-West

```text
Pod-to-Pod / internal traffic
```

---

## North-South

```text
External-to-cluster / cluster-to-external traffic
```

---

## Zero Trust

```text
Do not implicitly trust network location
```

---

## mTLS

```text
Mutual authentication + encryption
```

---

## CNI

```text
Provides cluster networking and may enforce NetworkPolicy
```

---

# Essential Commands

List NetworkPolicies:

```bash
kubectl get networkpolicies -A
```

or:

```bash
kubectl get netpol -A
```

Describe:

```bash
kubectl describe networkpolicy <name>
```

List Pods with labels:

```bash
kubectl get pods --show-labels
```

List Services:

```bash
kubectl get svc
```

List Endpoints:

```bash
kubectl get endpoints
```

List EndpointSlices:

```bash
kubectl get endpointslices
```

Test DNS:

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
```

Test HTTP:

```bash
kubectl exec -it <pod> -- curl http://backend:8080
```

Test TCP:

```bash
kubectl exec -it <pod> -- nc -vz backend 8080
```

Inspect Pod:

```bash
kubectl get pod <pod> -o yaml
```

---

# Interview Questions

## Basic

- What is Kubernetes NetworkPolicy?
- What is ingress traffic?
- What is egress traffic?
- What is a default-deny policy?
- What is a Pod selector?
- What is a Namespace selector?
- What is an IP block?
- What is east-west traffic?
- What is north-south traffic?
- What is network segmentation?

---

## Intermediate

- How does NetworkPolicy work?
- How do you allow one Pod to communicate with another?
- How do you restrict traffic between namespaces?
- How do you create a default-deny policy?
- How do you allow DNS after enabling default-deny egress?
- What is the difference between `podSelector` and `namespaceSelector`?
- What is the difference between NetworkPolicy and a Service?
- Does NetworkPolicy encrypt traffic?
- Does NetworkPolicy authenticate applications?
- What is CNI's role in NetworkPolicy?
- Why is egress control important?
- What is zero-trust networking?

---

## Advanced

- Design NetworkPolicies for a three-tier application.
- How would you isolate two tenants in the same cluster?
- How would you prevent lateral movement after a Pod compromise?
- How would you restrict Internet access from production workloads?
- How would you allow only approved external APIs?
- How would you secure DNS traffic?
- How would you combine NetworkPolicy with mTLS?
- How would you troubleshoot a NetworkPolicy that is blocking legitimate traffic?
- How would you troubleshoot a Pod that cannot resolve DNS?
- How would you design network security for a multi-tenant Kubernetes cluster?
- What are the limitations of Kubernetes NetworkPolicy?
- How does a CNI enforce NetworkPolicy?
- How would you detect network-based data exfiltration?
- How would you secure Kubernetes API Server network access?
- How would you design east-west security for microservices?

---

# Interview Scenario 1

### Question

> A frontend Pod should communicate with the backend on port 8080, but it should not communicate with the database. How would you design the policy?

### Answer

Use default-deny networking and explicitly allow:

```text
Frontend → Backend:8080
```

Then allow:

```text
Backend → Database:5432
```

but do not create:

```text
Frontend → Database
```

Architecture:

```text
Frontend
   │
 TCP/8080
   ▼
Backend
   │
 TCP/5432
   ▼
Database
```

This implements least-privilege network access.

---

# Interview Scenario 2

### Question

> You enabled default-deny egress and suddenly applications cannot resolve service names. What happened?

### Answer

DNS traffic is likely being blocked.

Applications commonly need to communicate with the cluster DNS service.

The fix is to explicitly allow the required DNS traffic:

```text
UDP/53
TCP/53
```

to the cluster DNS Pods or appropriate DNS endpoint.

The exact selector depends on the Kubernetes distribution and DNS deployment.

---

# Interview Scenario 3

### Question

> Does NetworkPolicy provide encryption?

### Answer

No.

NetworkPolicy primarily provides:

```text
Network access control
```

It does not inherently provide:

```text
Encryption
```

For encryption and workload identity, use mechanisms such as:

```text
TLS
mTLS
Service Mesh
```

A mature architecture may use:

```text
NetworkPolicy
+
mTLS
```

---

# Interview Scenario 4

### Question

> A compromised frontend Pod is scanning internal services. How can Kubernetes network security reduce the impact?

### Answer

Use:

```text
Default-deny ingress/egress
+
Explicit service-to-service policies
+
Namespace segmentation
+
Egress restrictions
+
Network monitoring
```

Then:

```text
Compromised Frontend
       ↓
Attempt Internal Scan
       ↓
NetworkPolicy
       ↓
Only Backend:8080 Allowed
       ↓
Other Services Denied
```

This reduces lateral movement.

---

# Interview Scenario 5

### Question

> How would you implement zero-trust networking in Kubernetes?

### Answer

Start with:

```text
Default Deny
```

Then explicitly allow:

```text
Required Service-to-Service Traffic
```

Add:

```text
Namespace Segmentation
Egress Restrictions
mTLS
Application Authorization
Network Monitoring
```

The architecture becomes:

```text
Default Deny
      ↓
Explicit Allow
      ↓
Identity Verification
      ↓
Encrypted Traffic
      ↓
Monitoring
```

---

# Production Network Security Checklist

```text
☑ Default-deny ingress
☑ Default-deny egress where practical
☑ Explicit service communication
☑ Namespace segmentation
☑ Tenant isolation
☑ DNS controlled
☑ Egress restricted
☑ API Server protected
☑ Sensitive traffic encrypted
☑ mTLS where appropriate
☑ Network flows monitored
☑ CNI capabilities reviewed
☑ Cloud firewalls reviewed
☑ Security groups reviewed
☑ Policy exceptions documented
☑ NetworkPolicy tested
```

---

# Recommended Practice

1. Create a frontend Pod.
2. Create a backend Pod.
3. Create a database Pod.
4. Verify unrestricted connectivity in a disposable namespace.
5. Apply default-deny ingress.
6. Apply default-deny egress.
7. Allow DNS.
8. Allow frontend → backend.
9. Allow backend → database.
10. Verify frontend → database is denied.
11. Create namespace-based isolation.
12. Test cross-namespace communication.
13. Restrict Internet egress.
14. Monitor network flows.
15. Study CNI enforcement.
16. Study NetworkPolicy selector semantics.
17. Study east-west traffic.
18. Study north-south traffic.
19. Study mTLS.
20. Study Service Mesh networking.
21. Design a multi-tenant network architecture.
22. Document a production communication matrix.
23. Test policy failures and troubleshooting.
24. Build a zero-trust network model.

---

# References

## Official Kubernetes Documentation

- Network Policies
- Cluster Networking
- Services
- DNS for Services and Pods
- Network Plugins
- Ingress
- Gateway API
- Kubernetes Security
- Service Accounts
- Pod Security Standards

---

# Chapter Summary

Kubernetes network security controls how workloads communicate.

The primary Kubernetes-native mechanism is:

```text
NetworkPolicy
```

NetworkPolicy can control:

```text
Ingress
Egress
```

using:

```text
podSelector
namespaceSelector
ipBlock
```

A strong production strategy is to begin with:

```text
Default Deny
```

and explicitly allow required communication.

For a three-tier application:

```text
Frontend
   ↓
Backend
   ↓
Database
```

policies should ideally permit:

```text
Frontend → Backend
Backend → Database
```

while preventing unnecessary communication such as:

```text
Frontend → Database
```

Network security should follow:

```text
Least Privilege
```

and:

```text
Zero Trust
```

principles.

East-west traffic represents internal workload communication:

```text
Frontend → Backend
Backend → Database
```

while north-south traffic represents traffic entering or leaving the cluster:

```text
Internet → Cluster
Cluster → Internet
```

Egress security is especially important because unrestricted outbound access can enable:

```text
Command and Control
Data Exfiltration
Malware Downloads
Unauthorized External Access
```

DNS is another important dependency. Strict egress policies must account for access to the cluster DNS service.

NetworkPolicy does **not** inherently provide:

```text
Encryption
Application Authentication
Application Authorization
```

For those requirements, additional mechanisms such as:

```text
TLS
mTLS
Service Mesh
Application Authentication
```

may be required.

The CNI is responsible for implementing cluster networking and may enforce NetworkPolicy using technologies such as:

```text
iptables
eBPF
OVS
```

depending on the implementation.

A production network security architecture can therefore look like:

```text
                      Internet
                          │
                          ▼
                       Gateway
                          │
                          ▼
                      Frontend
                          │
                    NetworkPolicy
                          │
                          ▼
                       Backend
                          │
                    NetworkPolicy
                          │
                          ▼
                      Database

                    + mTLS
                    + Egress Control
                    + DNS Security
                    + Flow Monitoring
                    + CNI Enforcement
```

The key principle is:

> **Do not treat network location as trust. Explicitly allow only the communication each workload requires.**

---

## Next Chapter

# Chapter 53 – Secret Management

Topics will include:

- Kubernetes Secrets
- Secret Types
- Secret Objects
- `data`
- `stringData`
- Secret Encoding
- Base64 vs Encryption
- Secret Creation
- Secret Consumption
- Environment Variables
- Secret Volumes
- Secret Rotation
- Secret Lifecycle
- Encryption at Rest
- EncryptionConfiguration
- KMS Integration
- External Secret Management
- External Secrets Operator
- Vault
- Cloud Secret Managers
- Secret CSI Driver
- Secret Access Control
- RBAC and Secrets
- Secret Leakage
- Secret Exposure Through Logs
- Secret Exposure Through Environment Variables
- Git Secret Management
- Sealed Secrets
- Secret Scanning
- Secret Rotation Strategies
- Short-Lived Credentials
- Workload Identity
- Secret Security Architecture
- Secret Incident Response
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---