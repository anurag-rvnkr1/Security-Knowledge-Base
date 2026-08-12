# Chapter 61 – Grafana

## Overview

Grafana is an open-source observability and visualization platform used to query, visualize, explore, and monitor metrics and other telemetry data.

In Kubernetes environments, Grafana is commonly used with:

```text
Prometheus
Loki
OpenTelemetry
Elasticsearch
InfluxDB
Tempo
```

A common Kubernetes monitoring architecture is:

```text
                    Kubernetes Cluster
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Applications      Nodes           Kubernetes
          │                │                │
          ▼                ▼                ▼
       Metrics        Node Exporter   kube-state-metrics
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                       Prometheus
                           │
                           ▼
                        Grafana
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Dashboard      Explore       Alerts
```

Grafana does not normally collect Kubernetes metrics itself.

Instead:

```text
Data Source
    ↓
Grafana
    ↓
Query
    ↓
Visualization
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Grafana fundamentals
- Why Grafana is used
- Grafana architecture
- Grafana Server
- Data Sources
- Prometheus Data Source
- Dashboards
- Panels
- Visualization types
- Time Series panels
- Stat panels
- Gauge panels
- Table panels
- Heatmaps
- Variables
- Template variables
- Query variables
- Dashboard variables
- PromQL in Grafana
- Transformations
- Overrides
- Thresholds
- Units
- Legends
- Annotations
- Dashboard provisioning
- Dashboard as Code
- JSON dashboards
- Grafana provisioning
- Alerting
- Grafana Alert Rules
- Contact Points
- Notification Policies
- Alert Groups
- Grafana vs Alertmanager
- Kubernetes dashboards
- Node dashboards
- Pod dashboards
- Cluster dashboards
- Application dashboards
- SLO dashboards
- RED dashboards
- USE dashboards
- Variables for Kubernetes
- Namespace filtering
- Pod filtering
- Multi-cluster dashboards
- Grafana authentication
- RBAC
- Teams
- Organizations
- Data Source security
- Secrets
- TLS
- Grafana plugins
- Grafana APIs
- Production deployment
- High availability
- Persistent storage
- Backup
- Security
- Performance optimization
- Troubleshooting
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Grafana?

Grafana is a visualization and observability platform.

It allows users to create dashboards from data stored in external systems.

For example:

```text
Prometheus
     ↓
   PromQL
     ↓
   Grafana
     ↓
 Dashboard
```

---

# Why Grafana?

Grafana makes large amounts of monitoring data easier to understand.

Instead of reading raw metrics:

```text
cpu_usage 0.73
memory_usage 4294967296
request_rate 250
```

you can visualize:

```text
CPU       ███████████░░░ 73%

Memory    ██████████░░░░ 68%

Requests  📈 250 req/s
```

---

# Grafana Architecture

A simplified architecture:

```text
                    User
                     │
                     ▼
                 Grafana UI
                     │
                     ▼
                Grafana Server
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Prometheus    Loki       Tempo
          │          │          │
       Metrics      Logs      Traces
```

Grafana queries data sources and visualizes their results.

---

# Grafana Components

Important concepts include:

```text
Grafana Server
Data Sources
Dashboards
Panels
Queries
Variables
Transformations
Alerting
Users
Teams
Organizations
Plugins
```

---

# Grafana Server

The Grafana server provides:

```text
Web UI
Authentication
Dashboard Management
Data Source Management
Alerting
API
Plugin Management
```

---

# Grafana Data Sources

A Data Source is an external system from which Grafana retrieves data.

Examples:

```text
Prometheus
Loki
Tempo
Elasticsearch
InfluxDB
MySQL
PostgreSQL
```

---

# Prometheus Data Source

In Kubernetes monitoring, Prometheus is one of the most common Grafana data sources.

Architecture:

```text
Kubernetes
     ↓
Prometheus
     ↓
Grafana
```

Grafana executes PromQL queries against Prometheus.

---

# Adding Prometheus

In Grafana:

```text
Connections
    ↓
Data Sources
    ↓
Add Data Source
    ↓
Prometheus
```

Configure the Prometheus endpoint.

Example:

```text
http://prometheus:9090
```

The actual address depends on your deployment.

---

# Test Data Source

After configuring Prometheus:

```text
Save & Test
```

A successful connection means Grafana can communicate with Prometheus.

---

# Dashboards

A dashboard is a collection of visualizations representing related information.

Example:

```text
Kubernetes Cluster Dashboard
```

may contain:

```text
CPU
Memory
Nodes
Pods
Network
Errors
Latency
```

---

# Dashboard Architecture

```text
Dashboard
    │
    ├── Panel
    ├── Panel
    ├── Panel
    └── Panel
```

---

# Panels

A Panel is an individual visualization.

Examples:

```text
Time Series
Stat
Gauge
Table
Bar Chart
Heatmap
Logs
```

---

# Time Series Panel

Best for values changing over time.

Examples:

```text
CPU Usage
Memory Usage
Request Rate
Latency
Network Traffic
```

Example:

```text
CPU
100% ┤              ╭───╮
 80% ┤         ╭────╯   ╰──╮
 60% ┤────╮────╯            ╰──
 40% ┤    ╰────────────────────
     └──────────────────────────
          Time →
```

---

# Stat Panel

Stat panels display a single important value.

Example:

```text
Active Pods

42
```

Other examples:

```text
Cluster Nodes
Error Rate
Request Rate
```

---

# Gauge Panel

A Gauge displays a value against a range.

Example:

```text
CPU Usage

       78%
    ┌────────┐
    │ ██████ │
    └────────┘
```

Useful for:

```text
CPU
Memory
Disk
SLO
```

---

# Table Panel

Tables are useful for detailed comparisons.

Example:

| Pod | CPU | Memory | Restarts |
|---|---:|---:|---:|
| backend-1 | 120m | 256Mi | 0 |
| backend-2 | 310m | 400Mi | 2 |
| backend-3 | 90m | 180Mi | 0 |

---

# Heatmap

Heatmaps are useful for distributions.

Examples:

```text
Request Latency
Response Size
Request Duration
```

---

# Bar Chart

Useful for comparing categories.

Example:

```text
CPU by Namespace

production   █████████████
staging      ███████
dev          ████
```

---

# Dashboard Queries

A panel usually contains:

```text
Data Source
+
Query
+
Visualization
```

For Prometheus:

```text
Data Source:
Prometheus

Query:
PromQL
```

---

# Example PromQL Panel

```promql
sum(
  rate(http_requests_total[5m])
)
```

Visualization:

```text
Time Series
```

---

# CPU Dashboard Query

A commonly used query pattern:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total[5m])
)
```

The exact available metric names depend on your monitoring stack.

---

# Memory Dashboard Query

Example:

```promql
sum by (pod) (
  container_memory_working_set_bytes
)
```

Again, metric availability depends on the installed exporters and Kubernetes monitoring stack.

---

# Request Rate Dashboard

```promql
sum(
  rate(http_requests_total[5m])
)
```

---

# Error Rate Dashboard

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

---

# P95 Latency Dashboard

For histogram metrics:

```promql
histogram_quantile(
  0.95,
  sum by (le) (
    rate(
      http_request_duration_seconds_bucket[5m]
    )
  )
)
```

---

# Variables

Grafana variables allow users to dynamically change dashboard filters.

For example:

```text
Namespace:
[ production ▼ ]
```

Then:

```text
Pod:
[ backend-7d8f ▼ ]
```

---

# Why Variables?

Without variables, you might create:

```text
Production Dashboard
Staging Dashboard
Development Dashboard
```

With variables:

```text
One Dashboard
      +
Namespace Variable
      +
Pod Variable
```

---

# Template Variables

Template variables allow dashboards to become reusable.

Example:

```text
$namespace
$pod
$cluster
```

---

# Query Variables

A variable can be populated from a query.

Example:

```promql
label_values(kube_pod_info, namespace)
```

Depending on the Grafana/Prometheus version and query editor, variable query syntax may differ.

---

# Namespace Variable

Conceptually:

```text
Variable:
namespace
```

Values:

```text
production
staging
development
```

---

# Pod Variable

A Pod variable can depend on the selected namespace.

Conceptually:

```text
Namespace
    ↓
Pod
```

This creates dependent filtering.

---

# Cluster Variable

For multi-cluster monitoring:

```text
Cluster:
[ cluster-a ▼ ]
```

Then all dashboard queries filter:

```text
cluster="$cluster"
```

---

# Variable Query Example

A Prometheus label query can retrieve available values.

For example:

```promql
label_values(kube_pod_info, namespace)
```

The exact Grafana variable-query interface depends on the Grafana version.

---

# Multi-Select Variables

A variable can allow:

```text
production
+
staging
```

or:

```text
All
```

This is useful for comparing environments.

---

# Variables and PromQL

Example:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total{
    namespace="$namespace"
  }[5m])
)
```

Changing:

```text
$namespace
```

changes the dashboard automatically.

---

# Transformations

Grafana transformations modify query results before visualization.

Examples:

```text
Join
Filter
Rename
Organize Fields
Calculate
Group
Reduce
```

---

# Why Transformations?

Suppose you have:

```text
Query A
```

with:

```text
Pod
CPU
```

and:

```text
Query B
```

with:

```text
Pod
Memory
```

A transformation can combine them into:

```text
Pod | CPU | Memory
```

---

# Field Overrides

Field overrides customize specific fields.

For example:

```text
CPU → Percent
Memory → Bytes
Latency → Milliseconds
```

---

# Units

Correct units improve dashboard readability.

Examples:

```text
CPU → Percent
Memory → Bytes
Latency → Seconds
Traffic → Bytes/sec
Requests → req/sec
```

---

# Thresholds

Thresholds indicate important ranges.

Example:

```text
CPU

0–70%    Normal
70–85%   Warning
85–100%  Critical
```

Thresholds should reflect actual operational requirements rather than arbitrary numbers.

---

# Legends

Legends identify individual time series.

Example:

```text
backend-1
backend-2
backend-3
```

Avoid overly long legends because they reduce dashboard readability.

---

# Annotations

Annotations mark important events on dashboards.

Examples:

```text
Deployment
Release
Incident
Scaling Event
Configuration Change
```

Example:

```text
CPU
100% ┤        ╭──────╮
 80% ┤───────╯        ╰──
     │        │
     │        │ Deployment
     └────────┼────────────
              Time
```

---

# Dashboard Variables + Annotations

Together they allow:

```text
Cluster
Namespace
Pod
Deployment
```

to be filtered while displaying operational events.

---

# Dashboard Provisioning

Grafana supports provisioning configuration through files.

Provisioning can manage:

```text
Data Sources
Dashboards
Alerting Resources
```

This helps automate deployments.

---

# Dashboard as Code

Instead of manually creating every dashboard:

```text
Dashboard JSON
      ↓
Git
      ↓
CI/CD
      ↓
Grafana
```

Benefits:

```text
Version Control
Reproducibility
Automation
Review
Rollback
```

---

# Dashboard JSON

Grafana dashboards can be represented as JSON.

Conceptually:

```json
{
  "title": "Kubernetes Cluster",
  "panels": []
}
```

A dashboard can therefore be stored in Git.

---

# Grafana Provisioning Architecture

```text
Git Repository
      │
      ▼
Dashboard JSON
      │
      ▼
CI/CD
      │
      ▼
Grafana
      │
      ▼
Dashboard
```

---

# Why Dashboard as Code?

It prevents:

```text
Manual Configuration Drift
```

and makes dashboards reproducible.

---

# Grafana Alerting

Grafana provides its own alerting capabilities.

The flow can be:

```text
Data Source
    ↓
Grafana Alert Rule
    ↓
Alert Evaluation
    ↓
Contact Point
    ↓
Notification
```

---

# Grafana Alert Rule

An alert rule defines:

```text
Query
+
Condition
+
Evaluation
+
Labels
+
Annotations
```

Example conceptually:

```text
CPU > 90%
for 10 minutes
```

---

# Contact Points

Contact points define where notifications go.

Examples:

```text
Email
Slack
PagerDuty
Webhook
Other Supported Integrations
```

The available integrations depend on the Grafana deployment and configuration.

---

# Notification Policies

Notification policies determine how alerts are routed.

For example:

```text
severity=critical
       ↓
Pager

severity=warning
       ↓
Email
```

---

# Alert Groups

Related alerts can be grouped to reduce notification noise.

Example:

```text
Node Down
Pod Down
Service Down
```

can potentially be grouped by:

```text
cluster
namespace
service
```

---

# Grafana Alerting vs Alertmanager

Both can participate in alerting, but they are not identical.

Grafana Alerting:

```text
Alert Rule Evaluation
Visualization Integration
Multi-Data-Source Alerting
```

Prometheus + Alertmanager:

```text
Prometheus Rule Evaluation
Alert Routing
Deduplication
Grouping
Silencing
Inhibition
```

A production environment should choose an alerting architecture deliberately to avoid duplicate notifications.

---

# Kubernetes Cluster Dashboard

A useful cluster dashboard may include:

```text
Cluster Nodes
CPU Usage
Memory Usage
Disk Usage
Network Traffic
Pod Count
Pending Pods
Failed Pods
Restarts
```

---

# Node Dashboard

Example panels:

```text
CPU Utilization
Memory Utilization
Filesystem Usage
Disk I/O
Network Traffic
Pod Count
```

---

# Pod Dashboard

Example:

```text
Pod CPU
Pod Memory
Restarts
Network
Readiness
Container Status
```

---

# Application Dashboard

A production application dashboard should include:

```text
Request Rate
Error Rate
Latency
Saturation
Dependency Health
```

---

# RED Dashboard

A RED dashboard focuses on:

```text
Rate
Errors
Duration
```

Example:

```text
Requests/sec
5xx/sec
P50
P95
P99
```

---

# USE Dashboard

A USE dashboard focuses on:

```text
Utilization
Saturation
Errors
```

Example:

```text
CPU Utilization
CPU Saturation
CPU Errors
```

---

# SLO Dashboard

An SLO dashboard can show:

```text
Availability
Latency
Error Budget
SLO Compliance
```

Example:

```text
Availability SLO

99.95%

Target:

99.90%
```

---

# Error Budget Dashboard

Display:

```text
SLO
Current Availability
Error Budget
Budget Remaining
```

This helps engineering teams understand reliability risk.

---

# Kubernetes Namespace Dashboard

Use:

```text
$namespace
```

to dynamically filter:

```text
CPU
Memory
Pods
Restarts
Errors
```

---

# Kubernetes Pod Dashboard

Use variables:

```text
$cluster
$namespace
$pod
```

Example query:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total{
    cluster="$cluster",
    namespace="$namespace"
  }[5m])
)
```

The exact labels depend on your metric pipeline.

---

# Multi-Cluster Dashboard

A multi-cluster dashboard can use:

```text
Cluster Variable
```

Example:

```text
cluster-a
cluster-b
cluster-c
```

Then:

```promql
sum by (cluster) (
  rate(http_requests_total[5m])
)
```

---

# Grafana Authentication

Grafana can support authentication mechanisms such as:

```text
Local Users
OAuth
OIDC
LDAP
Other Supported Identity Providers
```

Exact options depend on the Grafana edition and configuration.

---

# RBAC

Grafana should implement appropriate role-based access control.

Users may have different permissions:

```text
Viewer
Editor
Admin
```

Exact role capabilities depend on the Grafana version/edition.

---

# Teams

Teams group users with similar responsibilities.

Example:

```text
SRE Team
SOC Team
Development Team
Platform Team
```

This can simplify access management.

---

# Organizations

Grafana Organizations provide logical separation of:

```text
Users
Dashboards
Data Sources
Permissions
```

The exact organization behavior depends on the Grafana edition and deployment model.

---

# Data Source Security

A user who can query a data source may potentially access sensitive information.

Therefore:

```text
Data Source
    ↓
Access Control
```

should be carefully designed.

---

# Secrets

Do not hard-code credentials into:

```text
Dashboard
PromQL
Git
Configuration
```

Use appropriate secret-management mechanisms.

---

# TLS

Secure communication should be considered for:

```text
Browser → Grafana
Grafana → Data Sources
Grafana → External Services
```

---

# Grafana Plugins

Plugins extend Grafana capabilities.

They may provide:

```text
Data Sources
Visualizations
Applications
```

Only install trusted plugins and keep them updated.

---

# Grafana API

Grafana provides APIs for automation.

Common use cases include:

```text
Dashboard Management
Data Source Management
Folder Management
Alert Management
User/Team Automation
```

---

# Dashboard Automation

A CI/CD pipeline can automatically provision:

```text
Data Sources
Dashboards
Alert Rules
Folders
```

---

# Grafana in Kubernetes

Grafana can run as a Deployment:

```text
Deployment
    ↓
Pod
    ↓
Service
```

Example architecture:

```text
Ingress
   ↓
Grafana Service
   ↓
Grafana Pod
   ↓
Prometheus Service
```

---

# Persistent Storage

Grafana may need persistent storage for deployment-specific state such as:

```text
Database
Configuration
Plugins
```

The exact persistence requirements depend on the chosen deployment architecture and external database usage.

---

# Grafana Database

Grafana stores application state in a database.

Depending on deployment, this may be:

```text
SQLite
MySQL
PostgreSQL
```

For production environments, an external highly available database may be preferred depending on scale and availability requirements.

---

# Grafana High Availability

A highly available deployment may look like:

```text
              Load Balancer
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Grafana A           Grafana B
          │                   │
          └─────────┬─────────┘
                    ▼
             Shared Database
```

Dashboards and configuration should be managed consistently across replicas.

---

# Grafana Backup

Important items may include:

```text
Dashboards
Data Sources
Alert Rules
Folders
Configuration
Database
```

Dashboard-as-code can reduce backup complexity for dashboards.

---

# Grafana Performance

Performance depends on:

```text
Query Complexity
Time Range
Panel Count
Refresh Interval
Data Source Performance
Dashboard Variables
Browser Load
```

---

# Dashboard Performance Problems

A dashboard with:

```text
50 Panels
+
5-second Refresh
+
Large Time Range
+
Complex Queries
```

can create significant load.

---

# Dashboard Optimization

Use:

```text
Fewer Panels
Reasonable Refresh Intervals
Recording Rules
Efficient PromQL
Appropriate Time Ranges
```

---

# Query Optimization

Instead of repeatedly executing:

```promql
Complex Expensive Query
```

use a recording rule where appropriate:

```text
Prometheus
 ↓
Recording Rule
 ↓
Simple Dashboard Query
```

---

# Dashboard Refresh

Avoid unnecessarily aggressive refresh intervals.

Examples:

```text
5s
10s
30s
1m
5m
```

Choose according to operational requirements.

---

# Grafana and Observability

Grafana can provide a unified interface for:

```text
Metrics
Logs
Traces
Profiles
```

depending on the configured data sources and plugins.

---

# Metrics + Logs + Traces

A powerful troubleshooting workflow is:

```text
Dashboard Alert
      ↓
Metric
      ↓
Log
      ↓
Trace
      ↓
Root Cause
```

---

# Example Incident

Grafana shows:

```text
HTTP 5xx ↑
```

Then inspect:

```text
Latency ↑
```

Then logs:

```text
Database Timeout
```

Then traces:

```text
Database Span = 5 seconds
```

Root cause:

```text
Database latency
```

---

# Grafana Security Best Practices

### 1. Enable Authentication

Do not expose unauthenticated Grafana publicly.

---

### 2. Use HTTPS

Protect:

```text
Credentials
Sessions
Dashboard Data
```

---

### 3. Apply Least Privilege

Users should only access required resources.

---

### 4. Protect Data Sources

Do not allow unnecessary access.

---

### 5. Secure Secrets

Never store credentials in dashboards.

---

### 6. Restrict Public Sharing

Be careful with anonymous access and publicly shared dashboards.

---

### 7. Keep Plugins Updated

Remove unused plugins.

---

### 8. Monitor Grafana

Track:

```text
CPU
Memory
Request Rate
Errors
Database Health
```

---

# Production Best Practices

### 1. Use Dashboard as Code

Store dashboards in Git.

---

### 2. Standardize Dashboards

Create reusable templates for:

```text
Cluster
Node
Pod
Application
SLO
```

---

### 3. Use Variables

Make dashboards reusable.

---

### 4. Use Consistent Units

For example:

```text
CPU → %
Memory → bytes
Latency → ms
Traffic → bytes/sec
```

---

### 5. Avoid Dashboard Overload

Only show useful information.

---

### 6. Use Recording Rules

Move expensive repeated calculations into Prometheus.

---

### 7. Design for Incident Response

Put the most important signals first:

```text
Errors
Latency
Traffic
Saturation
```

---

### 8. Use Drill-Down Dashboards

Example:

```text
Cluster
 ↓
Namespace
 ↓
Deployment
 ↓
Pod
 ↓
Container
```

---

### 9. Use Alert Annotations

Alerts should explain:

```text
What
Where
Impact
Possible Cause
```

---

### 10. Version Control

Keep:

```text
Dashboards
Alerts
Provisioning
Configuration
```

under version control where practical.

---

# Production Kubernetes Grafana Architecture

```text
                         Internet / Internal Users
                                  │
                                  ▼
                              Ingress
                                  │
                                  ▼
                           Grafana Service
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
                Grafana A                   Grafana B
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                         External DB / Storage
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
               Prometheus       Loki          Tempo
                    │             │             │
                  Metrics        Logs         Traces
```

---

# Hands-on Lab 1 – Deploy Grafana

Deploy Grafana in a disposable Kubernetes cluster.

Verify:

```bash
kubectl get pods -n monitoring
```

Expose it through an appropriate Service.

---

# Hands-on Lab 2 – Add Prometheus

Configure:

```text
Grafana
    ↓
Data Source
    ↓
Prometheus
```

Test the connection.

---

# Hands-on Lab 3 – Create a Cluster Dashboard

Create panels for:

```text
Node Count
CPU
Memory
Pod Count
Pending Pods
```

---

# Hands-on Lab 4 – Create a Node Dashboard

Create:

```text
CPU Usage
Memory Usage
Disk Usage
Network Traffic
```

---

# Hands-on Lab 5 – Create a Pod Dashboard

Use variables:

```text
Namespace
Pod
```

Then display:

```text
CPU
Memory
Restarts
```

---

# Hands-on Lab 6 – Create a RED Dashboard

Create:

```text
Request Rate
Error Rate
P95 Latency
P99 Latency
```

---

# Hands-on Lab 7 – Create a USE Dashboard

Create:

```text
CPU Utilization
CPU Saturation
CPU Errors
```

Repeat for:

```text
Memory
Disk
Network
```

where suitable metrics are available.

---

# Hands-on Lab 8 – Dashboard Variables

Create:

```text
$namespace
$pod
```

Make Pod options depend on Namespace.

---

# Hands-on Lab 9 – Multi-Cluster Dashboard

Create:

```text
$cluster
```

Use it to switch between:

```text
Cluster A
Cluster B
Cluster C
```

---

# Hands-on Lab 10 – Create an SLO Dashboard

Display:

```text
SLO
Availability
Error Budget
Current Error Rate
```

---

# Hands-on Lab 11 – Create an Alert

Create:

```text
High CPU Usage
```

Example condition:

```text
CPU > 80%
```

for a sustained period.

Test the alert.

---

# Hands-on Lab 12 – Contact Point

Configure a test contact point.

Verify:

```text
Alert
 ↓
Contact Point
 ↓
Notification
```

---

# Hands-on Lab 13 – Dashboard Provisioning

Store a dashboard definition in Git.

Configure Grafana provisioning to load it automatically.

---

# Hands-on Lab 14 – Dashboard as Code

Create:

```text
dashboard.json
```

Commit it to Git.

Use CI/CD to deploy it to a test Grafana instance.

---

# Hands-on Lab 15 – Grafana API

Use the Grafana API to automate dashboard creation.

Implement:

```text
Create Dashboard
Update Dashboard
Delete Dashboard
```

in a test environment.

---

# Hands-on Lab 16 – Grafana Security

Configure:

```text
Authentication
HTTPS
RBAC
```

Then verify that users have only their intended access.

---

# Hands-on Lab 17 – Performance Testing

Create a dashboard with many panels.

Measure:

```text
Load Time
Query Time
Browser Performance
Prometheus Load
```

Optimize it.

---

# Hands-on Lab 18 – Incident Drill

Simulate:

```text
Application Error Spike
```

Use Grafana to:

```text
Detect
Investigate
Drill Down
Correlate
Resolve
```

---

# Hands-on Lab 19 – Metrics + Logs

Configure Grafana with:

```text
Prometheus
+
Loki
```

From a metric panel, navigate to related logs where your integrations support this workflow.

---

# Hands-on Lab 20 – Full Observability Dashboard

Build:

```text
Cluster Health
     ↓
Application Health
     ↓
RED Signals
     ↓
Logs
     ↓
Traces
     ↓
Alerts
```

This becomes the foundation of a production observability dashboard.

---

# Common Mistakes

## 1. Using Grafana as the Metrics Database

Grafana is primarily a visualization and observability layer.

---

## 2. Too Many Panels

Large dashboards become difficult to use.

---

## 3. Excessive Refresh Rates

Very frequent refreshes can overload data sources.

---

## 4. Complex Queries Everywhere

Use recording rules when appropriate.

---

## 5. No Variables

A dashboard for every namespace or cluster does not scale well.

---

## 6. Poor Units

Displaying:

```text
4294967296
```

is less useful than:

```text
4 GiB
```

---

## 7. No Thresholds

Important values may be difficult to identify.

---

## 8. Exposing Grafana Publicly

Grafana can expose sensitive infrastructure information.

---

## 9. Storing Secrets in Dashboards

Never embed credentials in queries or dashboard JSON.

---

## 10. No Version Control

Manually created production dashboards can be difficult to reproduce.

---

## 11. Duplicate Alerting

Running Grafana Alerting and Prometheus Alertmanager without a clear strategy can generate duplicate notifications.

---

## 12. No Incident Context

Dashboards should help answer:

```text
What broke?
When?
Where?
How severe?
What changed?
```

---

# Quick Revision

## Grafana

```text
Observability and visualization platform
```

---

## Data Source

```text
External system Grafana queries
```

---

## Dashboard

```text
Collection of related visualizations
```

---

## Panel

```text
Individual visualization
```

---

## Variable

```text
Dynamic dashboard filter
```

---

## Transformation

```text
Modifies query results before visualization
```

---

## Threshold

```text
Defines meaningful value boundaries
```

---

## Annotation

```text
Marks an event on a visualization
```

---

## ServiceMonitor

```text
Kubernetes resource used by Prometheus Operator for Service-based scraping
```

---

## Grafana Alerting

```text
Grafana-native alert rule and notification system
```

---

## Contact Point

```text
Destination for alert notifications
```

---

## Notification Policy

```text
Controls how alerts are routed
```

---

## Dashboard as Code

```text
Managing dashboards through version-controlled configuration
```

---

## Grafana HA

```text
Multiple Grafana instances sharing appropriate state/configuration
```

---

# Essential Commands

Check Grafana Pods:

```bash
kubectl get pods -n monitoring
```

Check Grafana Service:

```bash
kubectl get svc -n monitoring
```

Check Grafana Deployment:

```bash
kubectl get deployment -n monitoring
```

View logs:

```bash
kubectl logs deployment/grafana -n monitoring
```

Port forward:

```bash
kubectl port-forward \
  svc/grafana \
  3000:80 \
  -n monitoring
```

The Service port may differ depending on the deployment.

Check Prometheus:

```bash
kubectl get pods -n monitoring
```

Check ServiceMonitors:

```bash
kubectl get servicemonitor -A
```

Check PodMonitors:

```bash
kubectl get podmonitor -A
```

Check PrometheusRules:

```bash
kubectl get prometheusrule -A
```

---

# Important PromQL Queries for Grafana

Target health:

```promql
up
```

Failed targets:

```promql
up == 0
```

Request rate:

```promql
sum(
  rate(http_requests_total[5m])
)
```

Error rate:

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

CPU by Pod:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total[5m])
)
```

Memory by Pod:

```promql
sum by (pod) (
  container_memory_working_set_bytes
)
```

Requests by Namespace:

```promql
sum by (namespace) (
  rate(http_requests_total[5m])
)
```

P95 latency:

```promql
histogram_quantile(
  0.95,
  sum by (le) (
    rate(
      http_request_duration_seconds_bucket[5m]
    )
  )
)
```

---

# Interview Questions

## Basic

- What is Grafana?
- Why is Grafana used with Prometheus?
- What is a Grafana dashboard?
- What is a Panel?
- What is a Data Source?
- What is a Grafana variable?
- What is a transformation?
- What is an annotation?
- What is a threshold?
- What is Grafana Alerting?
- What is a Contact Point?
- What is a Notification Policy?
- What is Dashboard as Code?

---

## Intermediate

- How do you connect Grafana to Prometheus?
- How does Grafana execute PromQL?
- How do Grafana variables work?
- What is the difference between a dashboard and a panel?
- What are Grafana transformations?
- How do you create a Kubernetes dashboard?
- How do you create a multi-cluster dashboard?
- How do you create a RED dashboard?
- How do you create a USE dashboard?
- How do you create an SLO dashboard?
- How do you provision Grafana dashboards?
- What is the difference between Grafana Alerting and Alertmanager?
- How do you secure Grafana?
- How do you implement Grafana RBAC?
- How do you make Grafana highly available?

---

## Advanced

- Design a production Grafana architecture for Kubernetes.
- How would you design Grafana for multiple clusters?
- How would you secure Grafana in a production environment?
- How would you manage dashboards as code?
- How would you prevent dashboard query overload?
- How would you optimize a slow Grafana dashboard?
- How would you implement SLO dashboards?
- How would you integrate metrics, logs, and traces?
- How would you design Grafana RBAC for SRE, SOC, and development teams?
- How would you handle Grafana high availability?
- How would you back up Grafana?
- How would you migrate dashboards between environments?
- How would you troubleshoot a Grafana dashboard showing no data?
- How would you troubleshoot a slow dashboard?
- How would you prevent duplicate alerts when using Grafana Alerting and Alertmanager?

---

# Interview Scenario 1

### Question

> Grafana is showing "No Data" for a panel. How would you troubleshoot it?

### Answer

Start with:

```text
Grafana
 ↓
Data Source
 ↓
Query
 ↓
Prometheus
 ↓
Metric
 ↓
Labels
 ↓
Time Range
```

Check:

```text
Data Source Connectivity
PromQL
Metric Existence
Labels
Dashboard Variables
Time Range
Prometheus Target Health
```

Start with:

```promql
up
```

If that works, gradually test the original query.

---

# Interview Scenario 2

### Question

> Grafana dashboards are very slow. What would you investigate?

### Answer

Check:

```text
Panel Count
Query Complexity
Time Range
Refresh Interval
Prometheus Query Latency
Cardinality
Browser Load
Recording Rules
```

Optimize:

```text
Queries
Panels
Refresh Interval
Recording Rules
```

---

# Interview Scenario 3

### Question

> How would you create one dashboard for multiple Kubernetes namespaces?

### Answer

Create a variable:

```text
$namespace
```

Populate it from Prometheus.

Then use:

```promql
{
  namespace="$namespace"
}
```

in dashboard queries.

This allows:

```text
production
staging
development
```

to use the same dashboard.

---

# Interview Scenario 4

### Question

> How would you create a multi-cluster Grafana dashboard?

### Answer

Use a:

```text
$cluster
```

variable.

Then filter queries using:

```promql
{
  cluster="$cluster"
}
```

The metric pipeline must provide a reliable cluster label.

---

# Interview Scenario 5

### Question

> What is the difference between Grafana and Prometheus?

### Answer

Prometheus is primarily:

```text
Metrics Collection
Time-Series Storage
PromQL
Rule Evaluation
```

Grafana is primarily:

```text
Visualization
Dashboards
Exploration
Observability UI
```

Typical architecture:

```text
Prometheus
    ↓
Grafana
```

---

# Interview Scenario 6

### Question

> What is the difference between Grafana Alerting and Alertmanager?

### Answer

Grafana Alerting provides:

```text
Alert Rule Evaluation
Multi-Data-Source Alerting
Grafana-Native Alerting
```

Alertmanager provides:

```text
Grouping
Routing
Deduplication
Silencing
Inhibition
```

for alerts commonly generated by Prometheus.

They can be used separately or together, but the alerting architecture should be designed to avoid duplicate notifications.

---

# Interview Scenario 7

### Question

> How would you secure Grafana?

### Answer

Use:

```text
HTTPS
Authentication
RBAC
Least Privilege
Secure Data Sources
Secret Management
Network Restrictions
Plugin Management
Audit/Monitoring
```

Avoid:

```text
Anonymous Public Access
Hard-Coded Credentials
Untrusted Plugins
Overprivileged Users
```

---

# Interview Scenario 8

### Question

> How would you manage hundreds of Grafana dashboards?

### Answer

Use:

```text
Dashboard as Code
Git
Provisioning
CI/CD
Reusable Variables
Standard Templates
```

Architecture:

```text
Git
 ↓
CI/CD
 ↓
Dashboard Validation
 ↓
Grafana Provisioning
```

---

# Interview Scenario 9

### Question

> What would you put on a Kubernetes production dashboard?

### Answer

At cluster level:

```text
Node Health
CPU
Memory
Disk
Network
Pod Count
Pending Pods
Failed Pods
```

At application level:

```text
Rate
Errors
Latency
Saturation
```

Also:

```text
Restarts
OOMKilled
SLO
Error Budget
Active Alerts
```

---

# Interview Scenario 10

### Question

> How would you troubleshoot a Kubernetes application outage using Grafana?

### Answer

Use a drill-down approach:

```text
Cluster Dashboard
       ↓
Namespace
       ↓
Deployment
       ↓
Pod
       ↓
Container
       ↓
Metrics
       ↓
Logs
       ↓
Traces
```

Start with:

```text
Errors
Latency
Traffic
Saturation
```

and correlate them with:

```text
Deployments
Events
Logs
Traces
```

---

# Production Grafana Dashboard Architecture

```text
                         Grafana
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
    Cluster View       Application View      SLO View
        │                   │                   │
        ▼                   ▼                   ▼
      Nodes               RED                Error Budget
      Pods                Rate               Availability
      CPU                 Errors             Latency
      Memory              Duration            SLO
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    Drill-Down Dashboards
                            │
               ┌────────────┼────────────┐
               ▼            ▼            ▼
             Logs         Traces       Events
```

---

# Chapter Summary

Grafana is an observability and visualization platform commonly used with Prometheus and other data sources.

Its basic architecture is:

```text
Data Source
     ↓
Grafana
     ↓
Query
     ↓
Panel
     ↓
Dashboard
```

Important Grafana concepts include:

```text
Data Sources
Dashboards
Panels
Variables
Transformations
Thresholds
Annotations
Alert Rules
Contact Points
Notification Policies
```

For Kubernetes, useful dashboards include:

```text
Cluster Dashboard
Node Dashboard
Pod Dashboard
Application Dashboard
RED Dashboard
USE Dashboard
SLO Dashboard
```

Grafana variables make dashboards reusable:

```text
Cluster
Namespace
Pod
```

Dashboard-as-code allows dashboards to be managed through:

```text
Git
+
CI/CD
+
Provisioning
```

Grafana can also participate in alerting.

The key distinction is:

```text
Prometheus
=
Collect + Store + Query Metrics
```

```text
Grafana
=
Visualize + Explore + Present Data
```

```text
Alertmanager
=
Route + Group + Deduplicate + Silence Alerts
```

A production Grafana platform should be:

```text
Secure
Version Controlled
Observable
Scalable
Reusable
Actionable
```

The most important principle is:

> **A good Grafana dashboard should not simply display large amounts of data; it should help an engineer quickly determine what is broken, where it is broken, how severe the impact is, and what to investigate next.**

---

## Next Chapter

# Chapter 62 – Alertmanager

Topics will include:

- Alertmanager Fundamentals
- Why Alertmanager
- Alerting Architecture
- Prometheus + Alertmanager
- Alert Flow
- Alert Rules
- Alert Labels
- Alert Annotations
- Alert States
- Grouping
- Routing
- Route Trees
- Receivers
- Email
- Webhooks
- Slack
- PagerDuty
- Notification Policies
- Deduplication
- Silencing
- Inhibition
- Maintenance Windows
- Alert Severity
- Critical Alerts
- Warning Alerts
- Info Alerts
- Alert Fingerprints
- Group Wait
- Group Interval
- Repeat Interval
- Routing by Namespace
- Routing by Service
- Routing by Severity
- Routing by Team
- Inhibition Rules
- Silence Management
- Alertmanager Configuration
- `alertmanager.yml`
- Receivers
- Routes
- Matchers
- Templates
- Notification Templates
- Secret Management
- TLS
- Authentication
- HA Alertmanager
- Clustering
- Gossip
- Kubernetes Deployment
- Helm
- Prometheus Operator
- Alertmanager CRD
- AlertmanagerConfig
- Production Architecture
- Alert Fatigue
- Alert Hygiene
- Troubleshooting
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---