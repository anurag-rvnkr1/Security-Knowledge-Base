# Chapter 60 – Prometheus

## Overview

Prometheus is an open-source monitoring and alerting system designed for collecting, storing, querying, and analyzing time-series metrics.

It is one of the most widely used monitoring platforms in Kubernetes environments.

A typical Kubernetes observability architecture looks like:

```text
                    Kubernetes Cluster
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Applications      Kubernetes       Nodes
          │                │                │
          ▼                ▼                ▼
      /metrics       kube-state-metrics  Node Exporter
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                       Prometheus
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
              PromQL             Alert Rules
                 │                   │
                 ▼                   ▼
              Grafana            Alertmanager
```

Prometheus primarily works using a **pull-based scraping model**.

The basic flow is:

```text
Target
  ↓
/metrics
  ↓
Prometheus
  ↓
Time-Series Storage
  ↓
PromQL
  ↓
Grafana / Alerts
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Prometheus fundamentals
- Why Prometheus is used
- Prometheus architecture
- Prometheus Server
- Time-series database
- Pull-based monitoring
- Scraping
- Targets
- Exporters
- Service discovery
- Kubernetes service discovery
- Prometheus configuration
- `prometheus.yml`
- Jobs
- Targets
- Labels
- Metric types
- Counter
- Gauge
- Histogram
- Summary
- PromQL
- Selectors
- Instant vectors
- Range vectors
- Functions
- Aggregations
- `rate()`
- `irate()`
- `increase()`
- `sum()`
- `avg()`
- `max()`
- `min()`
- `histogram_quantile()`
- Recording rules
- Alerting rules
- Alertmanager
- Prometheus Operator
- ServiceMonitor
- PodMonitor
- PrometheusRule
- kube-state-metrics
- Node Exporter
- Kubernetes metrics
- Application metrics
- Custom metrics
- Prometheus storage
- Retention
- Remote Write
- High availability
- Federation
- Scaling
- Cardinality
- Label design
- Security
- TLS
- Authentication
- RBAC
- Production architecture
- Troubleshooting
- Performance optimization
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Prometheus?

Prometheus is a monitoring platform that stores metrics as time-series data.

A time series can be represented as:

```text
Metric Name
+
Labels
+
Timestamp
+
Value
```

Example:

```text
http_requests_total{
    service="backend",
    method="GET",
    status="200"
}
```

with values collected over time:

```text
10:00 → 1000
10:01 → 1050
10:02 → 1110
10:03 → 1175
```

---

# Why Prometheus?

Prometheus provides:

```text
Metrics Collection
Time-Series Storage
PromQL
Service Discovery
Alerting Rules
Kubernetes Integration
```

It is particularly effective for:

```text
Cloud-Native Systems
Microservices
Kubernetes
Distributed Applications
Infrastructure Monitoring
```

---

# Prometheus Architecture

A simplified architecture:

```text
                  ┌───────────────────┐
                  │     Targets       │
                  │                   │
                  │ Applications      │
                  │ Node Exporter     │
                  │ kube-state-metrics│
                  └─────────┬─────────┘
                            │
                         Scrape
                            │
                            ▼
                  ┌───────────────────┐
                  │    Prometheus     │
                  │                   │
                  │ Scraper           │
                  │ TSDB              │
                  │ PromQL            │
                  │ Rule Engine       │
                  └───────┬─────┬─────┘
                          │     │
                    Query │     │ Alerts
                          │     ▼
                          │ Alertmanager
                          ▼
                       Grafana
```

---

# Core Prometheus Components

Important components include:

```text
Prometheus Server
Time-Series Database
PromQL Engine
Scrape Manager
Rule Engine
Service Discovery
Alerting Integration
```

---

# Prometheus Server

The Prometheus server performs several tasks:

```text
Discover Targets
Scrape Metrics
Store Metrics
Evaluate Rules
Execute PromQL
```

---

# Pull-Based Monitoring

Prometheus commonly uses a pull model.

Prometheus asks the target:

```text
GET /metrics
```

The target responds:

```text
metric_name value
```

Architecture:

```text
Prometheus
    │
    │ HTTP GET
    ▼
Target /metrics
    │
    │ Metrics
    ▼
Prometheus
```

---

# Pull vs Push

## Pull

```text
Prometheus
    ↓
Target
```

Prometheus decides when to collect metrics.

## Push

```text
Application
    ↓
Monitoring Backend
```

The application sends metrics.

Prometheus primarily uses pull-based collection, although Pushgateway exists for specific short-lived job scenarios.

---

# Why Pull?

Pull-based collection makes it easier for Prometheus to:

```text
Detect Missing Targets
Control Scrape Frequency
Discover Targets
Inspect Scrape Health
```

---

# Metrics Endpoint

Applications commonly expose:

```text
/metrics
```

Example:

```text
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",status="200"} 1520
```

---

# Prometheus Text Format

A basic metric:

```text
requests_total 100
```

A labeled metric:

```text
requests_total{
  method="GET",
  status="200"
} 100
```

---

# Metric Names

Metric names should describe what is measured.

Examples:

```text
http_requests_total
process_cpu_seconds_total
node_memory_MemAvailable_bytes
```

Good metric names make queries easier to understand.

---

# Labels

Labels add dimensions to metrics.

Example:

```text
http_requests_total{
    method="GET",
    status="200",
    service="backend"
}
```

This allows queries such as:

```text
status="500"
```

---

# Labels vs Metric Names

Instead of creating:

```text
http_get_requests_total
http_post_requests_total
```

prefer:

```text
http_requests_total{
    method="GET"
}
```

and:

```text
http_requests_total{
    method="POST"
}
```

Labels provide dimensions without creating many metric names.

---

# Metric Types

Prometheus commonly supports:

```text
Counter
Gauge
Histogram
Summary
```

---

# Counter

A Counter represents a value that generally increases.

Example:

```text
http_requests_total
```

Conceptually:

```text
100
 ↓
200
 ↓
300
 ↓
400
```

It can reset when the application restarts.

---

# Counter Example

```text
http_requests_total{
    status="200"
} 10000
```

To calculate request rate:

```promql
rate(http_requests_total[5m])
```

---

# Gauge

A Gauge represents a value that can increase or decrease.

Examples:

```text
Memory Usage
CPU Temperature
Active Connections
Queue Size
```

Example:

```text
active_connections 150
```

It can become:

```text
150
 ↓
100
 ↓
175
```

---

# Histogram

A Histogram measures observations across configurable buckets.

Common use cases:

```text
Request Latency
Response Size
Processing Time
```

Example:

```text
http_request_duration_seconds_bucket
```

---

# Histogram Structure

A Histogram generates metrics such as:

```text
_count
_sum
_bucket
```

Example:

```text
http_request_duration_seconds_count
http_request_duration_seconds_sum
http_request_duration_seconds_bucket
```

---

# Histogram Buckets

Example:

```text
le="0.1"
le="0.5"
le="1"
le="5"
```

Meaning:

```text
Requests ≤ 100ms
Requests ≤ 500ms
Requests ≤ 1s
Requests ≤ 5s
```

---

# Histogram Quantiles

Prometheus can estimate quantiles using:

```promql
histogram_quantile()
```

Example:

```promql
histogram_quantile(
  0.95,
  rate(http_request_duration_seconds_bucket[5m])
)
```

This estimates the 95th percentile latency.

---

# Summary

A Summary calculates quantiles on the client side and exposes:

```text
_count
_sum
quantile
```

Summaries and histograms have different trade-offs.

Histograms are generally more useful when observations need to be aggregated across multiple instances.

---

# Prometheus Time-Series Database

Prometheus stores time-series data locally in its TSDB.

Conceptually:

```text
Metric
+
Labels
+
Timestamp
+
Value
```

form a time series.

---

# Example Time Series

```text
http_requests_total{
    service="api",
    status="200"
}
```

Values:

```text
10:00 → 100
10:01 → 120
10:02 → 150
10:03 → 180
```

---

# Prometheus Storage

Prometheus stores samples locally on disk.

Storage considerations include:

```text
Retention
Disk Capacity
Write Rate
Cardinality
Compaction
```

---

# Retention

Prometheus can retain data according to configured retention policies.

Example:

```text
15 days
```

or:

```text
30 days
```

The appropriate retention depends on:

```text
Disk Capacity
Metric Volume
Query Requirements
Business Needs
```

---

# Prometheus Is Not Usually Your Only Long-Term Store

For very large environments, organizations may use:

```text
Remote Write
Long-Term Storage
Thanos
Cortex
Mimir
VictoriaMetrics
```

depending on architecture.

---

# Scraping

Scraping is the process of retrieving metrics from a target.

Example:

```text
Prometheus
    ↓
GET /metrics
    ↓
Application
    ↓
Metrics Response
```

---

# Scrape Interval

Prometheus can scrape targets at a configured interval.

Example:

```yaml
scrape_interval: 15s
```

This means Prometheus attempts to collect metrics approximately every 15 seconds.

---

# Scrape Timeout

Example:

```yaml
scrape_timeout: 10s
```

The timeout should not exceed the configured scrape interval.

---

# Targets

A target is an endpoint from which Prometheus collects metrics.

Examples:

```text
Application
Node Exporter
kube-state-metrics
Kubernetes API-related exporters
```

---

# Jobs

Prometheus groups scrape targets into jobs.

Example:

```yaml
scrape_configs:

  - job_name: "node-exporter"
```

A job represents a collection of similar scrape targets.

---

# Basic Prometheus Configuration

Example:

```yaml
global:

  scrape_interval: 15s

scrape_configs:

  - job_name: "prometheus"

    static_configs:

      - targets:

        - "localhost:9090"
```

---

# `prometheus.yml`

The Prometheus configuration file commonly contains:

```text
Global Configuration
Scrape Configuration
Rule Files
Alerting Configuration
```

Example:

```yaml
global:

  scrape_interval: 15s

rule_files:

  - "rules.yml"

scrape_configs:

  - job_name: "prometheus"

    static_configs:

      - targets:

        - "localhost:9090"
```

---

# Static Targets

You can define targets manually:

```yaml
static_configs:

  - targets:

    - "10.0.0.10:9100"

    - "10.0.0.11:9100"
```

This works for stable environments.

Kubernetes environments usually benefit from service discovery.

---

# Service Discovery

Kubernetes is dynamic.

Pods can:

```text
Start
Stop
Move
Scale
Change IP
```

Static configuration becomes difficult.

Prometheus therefore supports service discovery.

---

# Kubernetes Service Discovery

Prometheus can discover Kubernetes resources such as:

```text
Nodes
Pods
Services
Endpoints
EndpointSlices
Ingresses
```

depending on configuration.

---

# Kubernetes Discovery Flow

```text
Kubernetes API
      ↓
Service Discovery
      ↓
Prometheus
      ↓
Discovered Targets
      ↓
Scraping
```

---

# Why Service Discovery Matters

Suppose:

```text
Pod A → 10.1.1.10
```

is replaced by:

```text
Pod B → 10.1.2.25
```

Prometheus should automatically discover the new endpoint.

---

# Exporters

An exporter exposes metrics for a system that does not natively expose Prometheus metrics.

Examples:

```text
Node Exporter
Blackbox Exporter
Database Exporters
SNMP Exporter
```

---

# Node Exporter

Node Exporter exposes host-level metrics.

Examples:

```text
CPU
Memory
Disk
Filesystem
Network
Load
```

Architecture:

```text
Node
 ↓
Node Exporter
 ↓
/metrics
 ↓
Prometheus
```

---

# kube-state-metrics

kube-state-metrics exposes metrics about Kubernetes object state.

Examples:

```text
Deployment Replicas
Pod Phase
DaemonSet Status
Job Status
Node Conditions
```

Architecture:

```text
Kubernetes API
       ↓
kube-state-metrics
       ↓
/metrics
       ↓
Prometheus
```

---

# Application Metrics

Applications can expose custom metrics.

Example:

```text
http_requests_total
```

or:

```text
orders_processed_total
```

---

# Custom Application Metrics

Suppose an order service exposes:

```text
orders_created_total
orders_failed_total
order_processing_duration_seconds
```

Prometheus can scrape these metrics.

---

# PromQL

PromQL stands for:

```text
Prometheus Query Language
```

It is used to query time-series data.

---

# Basic PromQL

Query a metric:

```promql
up
```

This returns the current `up` value for discovered targets.

---

# `up`

Usually:

```text
1 = scrape successful
0 = scrape failed
```

Example:

```text
up{job="node-exporter"} 1
```

---

# Metric Selector

Example:

```promql
http_requests_total
```

---

# Label Selector

Example:

```promql
http_requests_total{
  status="500"
}
```

---

# Multiple Labels

```promql
http_requests_total{
  service="backend",
  status="500"
}
```

---

# Negative Match

Example:

```promql
http_requests_total{
  status!="200"
}
```

---

# Regex Match

Example:

```promql
http_requests_total{
  status=~"5.."
}
```

This can match:

```text
500
501
502
503
...
```

---

# Regex Negative Match

```promql
http_requests_total{
  status!~"2.."
}
```

---

# Instant Vector

An instant vector represents a set of time series with a value at a particular point in time.

Example:

```promql
up
```

---

# Range Vector

A range vector contains samples over a time interval.

Example:

```promql
http_requests_total[5m]
```

This represents the last five minutes of samples.

---

# `rate()`

`rate()` calculates the average per-second increase of a counter over a range.

Example:

```promql
rate(http_requests_total[5m])
```

This is commonly used for request rates.

---

# `irate()`

`irate()` calculates a per-second rate based on the most recent samples.

Example:

```promql
irate(http_requests_total[5m])
```

It can react faster to short-term changes but can be noisier than `rate()`.

---

# `increase()`

`increase()` calculates the total increase in a counter over a range.

Example:

```promql
increase(http_requests_total[1h])
```

Meaning:

```text
Approximate number of requests during the last hour
```

---

# `sum()`

Add values together.

Example:

```promql
sum(http_requests_total)
```

---

# `sum by`

Group before summing.

Example:

```promql
sum by (status) (
  rate(http_requests_total[5m])
)
```

This can produce:

```text
200 → request rate
400 → request rate
500 → request rate
```

---

# `avg()`

Calculate average:

```promql
avg(cpu_usage)
```

---

# `max()`

Find maximum:

```promql
max(cpu_usage)
```

---

# `min()`

Find minimum:

```promql
min(cpu_usage)
```

---

# Aggregation by Namespace

Example:

```promql
sum by (namespace) (
  rate(container_cpu_usage_seconds_total[5m])
)
```

This can help compare CPU usage across namespaces.

---

# Aggregation by Pod

Example:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total[5m])
)
```

---

# CPU Usage Query

A commonly used query pattern is:

```promql
sum by (pod) (
  rate(container_cpu_usage_seconds_total[5m])
)
```

The exact metric availability depends on your Kubernetes monitoring stack.

---

# Memory Usage Query

Example:

```promql
sum by (pod) (
  container_memory_working_set_bytes
)
```

Metric names can vary depending on the metric source and deployment.

---

# HTTP Request Rate

Example:

```promql
sum(
  rate(http_requests_total[5m])
)
```

---

# HTTP Error Rate

Example:

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

---

# HTTP Error Percentage

Conceptually:

```promql
100 *
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

---

# P95 Latency

For a histogram:

```promql
histogram_quantile(
  0.95,
  sum by (le) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)
```

---

# P99 Latency

```promql
histogram_quantile(
  0.99,
  sum by (le) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)
```

---

# Recording Rules

Recording rules precompute frequently used queries.

Example:

```yaml
groups:

  - name: application

    rules:

      - record: job:http_requests:rate5m

        expr: |
          sum by (job) (
            rate(http_requests_total[5m])
          )
```

---

# Why Recording Rules?

They improve:

```text
Query Performance
Dashboard Performance
Rule Evaluation Efficiency
```

especially for expensive repeated queries.

---

# Alerting Rules

Prometheus can evaluate alert conditions.

Example:

```yaml
groups:

  - name: infrastructure

    rules:

      - alert: HighCPUUsage

        expr: cpu_usage > 0.9

        for: 10m

        labels:

          severity: warning

        annotations:

          summary: "High CPU usage detected"
```

---

# `for`

The `for` field prevents an alert from firing immediately.

Example:

```yaml
for: 10m
```

means the condition must remain true for the specified duration before the alert becomes active.

---

# Alert States

Prometheus alerts can conceptually be:

```text
Inactive
Pending
Firing
```

---

# Alert Flow

```text
Metric
 ↓
PromQL
 ↓
Alert Rule
 ↓
Prometheus
 ↓
Alertmanager
 ↓
Notification
```

---

# Alertmanager

Alertmanager handles alert management.

It can provide:

```text
Grouping
Deduplication
Routing
Silencing
Inhibition
```

---

# Alert Grouping

Suppose:

```text
100 Pods
```

generate related alerts.

Instead of:

```text
100 Notifications
```

Alertmanager can group related alerts.

---

# Alert Routing

Different alerts can go to different destinations.

Example:

```text
Security
 ↓
SOC

Database
 ↓
DB Team

Infrastructure
 ↓
SRE
```

---

# Silencing

Silencing temporarily prevents notifications for matching alerts.

Useful during:

```text
Maintenance
Planned Changes
Known Incidents
```

---

# Inhibition

Inhibition suppresses lower-priority alerts when a related higher-priority alert is already firing.

Example:

```text
Node Down
 ↓
Suppress individual Pod alerts
```

This reduces alert noise.

---

# Prometheus Operator

The Prometheus Operator simplifies running Prometheus on Kubernetes.

It introduces Kubernetes resources such as:

```text
Prometheus
ServiceMonitor
PodMonitor
PrometheusRule
Alertmanager
```

---

# ServiceMonitor

A `ServiceMonitor` tells the Prometheus Operator how to discover and scrape Services.

Conceptually:

```text
Service
 ↓
ServiceMonitor
 ↓
Prometheus
```

---

# PodMonitor

A `PodMonitor` allows scraping Pods directly.

Conceptually:

```text
Pod
 ↓
PodMonitor
 ↓
Prometheus
```

---

# PrometheusRule

A `PrometheusRule` can define:

```text
Recording Rules
Alerting Rules
```

in Kubernetes-native form.

---

# ServiceMonitor vs PodMonitor

| Feature | ServiceMonitor | PodMonitor |
|---|---|---|
| Target | Service | Pod |
| Discovery | Service-based | Pod-based |
| Common Use | Service endpoints | Direct Pod scraping |
| Operator Resource | Yes | Yes |

---

# Kubernetes Monitoring Stack

A common Kubernetes monitoring stack may contain:

```text
Prometheus
Alertmanager
Grafana
Node Exporter
kube-state-metrics
Prometheus Operator
```

---

# Prometheus and Metrics Server

They serve different purposes.

```text
Metrics Server
      ↓
Current Resource Metrics
      ↓
HPA / kubectl top
```

while:

```text
Prometheus
      ↓
General Metrics
      ↓
Historical Analysis
Dashboards
Alerting
```

---

# Prometheus Storage

Prometheus uses a local time-series database.

Important factors:

```text
Retention
Disk
Cardinality
Ingestion Rate
Compaction
```

---

# Retention by Time

Example configuration concept:

```text
15 days
```

---

# Retention by Size

You can also configure storage constraints based on disk usage.

Conceptually:

```text
Retain until storage reaches defined limit
```

Use both time and size controls carefully.

---

# Remote Write

Prometheus can send samples to remote storage systems.

Architecture:

```text
Prometheus
    │
    ├── Local TSDB
    │
    └── Remote Write
             ↓
      Long-Term Storage
```

---

# Why Remote Write?

Useful for:

```text
Long-Term Retention
Centralized Metrics
Multi-Cluster Monitoring
Large-Scale Storage
```

---

# Multi-Cluster Monitoring

Suppose an organization has:

```text
Cluster A
Cluster B
Cluster C
```

Each cluster can run Prometheus:

```text
Prometheus A ─┐
Prometheus B ─┼──→ Central Metrics Platform
Prometheus C ─┘
```

---

# Federation

Prometheus federation allows one Prometheus server to retrieve selected metrics from another Prometheus server.

Conceptually:

```text
Prometheus A
Prometheus B
Prometheus C
      ↓
Central Prometheus
```

Federation can be useful for hierarchical monitoring architectures.

---

# High Availability

A production monitoring system should consider:

```text
Prometheus Failure
Storage Failure
Alerting Failure
Network Failure
```

A common HA pattern is:

```text
Prometheus A
Prometheus B
      │
      ▼
Same Targets
```

with appropriate deduplication in the downstream metrics system.

---

# Prometheus Scaling

Prometheus performance is influenced by:

```text
Number of Targets
Scrape Interval
Metric Cardinality
Samples per Second
Query Complexity
Retention
```

---

# Cardinality

Cardinality is the number of unique time series.

Suppose:

```text
service = 10
method = 5
status = 10
```

Potential combinations:

```text
10 × 5 × 10
=
500
```

This is manageable.

But adding:

```text
user_id = 1,000,000
```

can explode the number of time series.

---

# High Cardinality Example

Bad:

```text
http_requests_total{
    user_id="123456"
}
```

If millions of users exist:

```text
Millions of Time Series
```

This can severely impact Prometheus.

---

# Good Labels

Prefer bounded dimensions:

```text
service
method
status
namespace
cluster
region
```

---

# Bad Labels

Avoid unbounded dimensions:

```text
user_id
request_id
session_id
UUID
full URL
timestamp
```

---

# Label Explosion

Too many unique label combinations can cause:

```text
High Memory Usage
Slow Queries
High Storage
Prometheus Instability
```

---

# Prometheus Security

Prometheus can expose sensitive infrastructure information.

Protect:

```text
Prometheus UI
Metrics Endpoints
Remote Write
Query APIs
```

---

# TLS

Use TLS where required for:

```text
Scraping
Remote Write
Web Access
Federation
```

---

# Authentication

Prometheus endpoints should not automatically be assumed to be safe because they are internal.

Use appropriate:

```text
Authentication
Authorization
Network Controls
```

---

# RBAC

In Kubernetes, Prometheus often needs permissions to discover resources.

These permissions should follow:

```text
Least Privilege
```

---

# Service Discovery Permissions

Prometheus may need access to Kubernetes resources such as:

```text
Pods
Services
Endpoints
Nodes
Namespaces
```

depending on the configured discovery mechanism.

---

# Prometheus and Secrets

Do not expose:

```text
Passwords
Tokens
API Keys
Private Keys
```

through metrics labels or metric values.

---

# Never Put Secrets in Labels

Bad:

```text
database_password="secret123"
```

This creates a serious security problem.

---

# Monitoring Sensitive Information

Be careful with:

```text
User IDs
Email Addresses
IP Addresses
Session IDs
Tokens
```

Metrics should use low-cardinality, non-sensitive dimensions whenever possible.

---

# Prometheus Performance Optimization

Important strategies:

```text
Control Cardinality
Optimize Queries
Use Recording Rules
Adjust Scrape Intervals
Filter Unnecessary Metrics
Use Appropriate Retention
Scale Storage
```

---

# Scrape Interval Optimization

Suppose:

```text
1000 targets
```

with:

```text
5-second interval
```

This creates significantly more ingestion than:

```text
30-second interval
```

Choose intervals based on monitoring requirements.

---

# Metric Filtering

If a target exposes unnecessary metrics, filtering can reduce:

```text
Storage
Memory
CPU
Network
```

---

# Query Optimization

Avoid unnecessarily expensive queries over huge time ranges.

Instead of:

```text
Very large time range
+
Complex aggregation
```

use:

```text
Appropriate Range
+
Recording Rules
```

where appropriate.

---

# Prometheus Troubleshooting

Start with:

```bash
kubectl get pods -n monitoring
```

Then:

```bash
kubectl logs <prometheus-pod>
```

Check targets:

```text
Prometheus UI
→ Status
→ Targets
```

---

# Target Health

Targets typically show:

```text
UP
DOWN
```

A target being DOWN means Prometheus cannot successfully scrape it.

---

# Common Scrape Failures

Possible causes:

```text
Network Error
Wrong Port
Wrong Path
TLS Error
Authentication Failure
Target Down
Service Discovery Error
```

---

# Debugging a DOWN Target

Check:

```text
Target Address
Port
Metrics Path
DNS
Network
TLS
Authentication
Application
```

---

# Common Error: Connection Refused

Possible causes:

```text
Application Not Listening
Wrong Port
Pod Not Ready
Service Misconfiguration
Network Policy
```

---

# Common Error: Timeout

Possible causes:

```text
Network Failure
Slow Endpoint
Firewall
Overloaded Target
Wrong Address
```

---

# Common Error: 404

Prometheus may be scraping:

```text
/metrics
```

while the application exposes:

```text
/prometheus
```

Check the metrics path.

---

# Common Error: 401 / 403

Possible causes:

```text
Authentication
Authorization
RBAC
```

---

# Common Error: TLS

Potential causes:

```text
Certificate
CA
Hostname
SAN
TLS Configuration
```

---

# PromQL Troubleshooting

If a query returns no data:

Check:

```text
Metric Name
Labels
Time Range
Target
Metric Availability
```

---

# Query Debugging

Start simple:

```promql
up
```

Then:

```promql
http_requests_total
```

Then:

```promql
http_requests_total{
  service="backend"
}
```

Then add:

```text
rate()
sum()
aggregation
```

incrementally.

---

# Production Prometheus Architecture

```text
                        Kubernetes Cluster
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
        Applications       Node Exporter    kube-state-metrics
             │                 │                 │
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                         Service Discovery
                               │
                               ▼
                           Prometheus
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
            TSDB             PromQL         Rule Engine
              │                │                │
              │                ▼                ▼
              │             Grafana        Alertmanager
              │                                  │
              ▼                                  ▼
       Remote Storage                       Notifications
```

---

# Multi-Cluster Prometheus Architecture

```text
Cluster A
    │
 Prometheus A
    │
    ├─────────────┐
                  │
Cluster B         │
    │             │
 Prometheus B     │
    │             │
    ├─────────────┤
                  ▼
          Central Metrics
             Platform
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
     Grafana            Alerting
```

---

# Prometheus Best Practices

### 1. Keep Cardinality Controlled

Use bounded labels.

---

### 2. Use Meaningful Metric Names

Follow consistent naming conventions.

---

### 3. Prefer Counters for Events

Examples:

```text
requests_total
errors_total
jobs_completed_total
```

---

### 4. Use Gauges for Current State

Examples:

```text
active_connections
queue_length
memory_usage
```

---

### 5. Use Histograms for Latency

Histograms are particularly useful for request duration analysis.

---

### 6. Use Service Discovery

Avoid static targets in dynamic Kubernetes environments where possible.

---

### 7. Use Recording Rules

Precompute expensive, frequently used queries.

---

### 8. Monitor Prometheus

Monitor:

```text
Memory
CPU
Disk
Scrape Failures
Query Latency
Series Count
Storage
```

---

### 9. Protect Prometheus

Use:

```text
Authentication
TLS
RBAC
Network Controls
```

---

### 10. Control Retention

Balance:

```text
Historical Value
Storage Cost
Performance
```

---

### 11. Avoid Secrets in Metrics

Never expose secrets through labels or values.

---

### 12. Test Alerts

Do not assume an alert works because the rule exists.

Generate controlled test conditions.

---

# Production Checklist

```text
☑ Prometheus deployed
☑ Targets discovered
☑ Scrapes successful
☑ Service discovery configured
☑ Application metrics available
☑ Node Exporter configured where required
☑ kube-state-metrics configured where required
☑ PromQL tested
☑ Recording rules configured
☑ Alert rules configured
☑ Alertmanager integrated
☑ Grafana integrated
☑ Retention configured
☑ Storage monitored
☑ Cardinality controlled
☑ Query performance monitored
☑ TLS configured where required
☑ Authentication configured
☑ RBAC configured
☑ Remote storage evaluated
☑ Backup/recovery strategy evaluated
☑ Prometheus itself monitored
```

---

# Hands-on Lab 1 – Install Prometheus

Deploy Prometheus in a disposable Kubernetes cluster.

Verify:

```bash
kubectl get pods -n monitoring
```

Then access the Prometheus UI.

---

# Hands-on Lab 2 – Check Targets

Open:

```text
Prometheus
→ Status
→ Targets
```

Verify:

```text
UP
```

for the expected targets.

---

# Hands-on Lab 3 – Query `up`

Run:

```promql
up
```

Identify:

```text
Healthy Targets
Unhealthy Targets
```

---

# Hands-on Lab 4 – Node Exporter

Deploy Node Exporter.

Verify that Prometheus discovers it.

Query:

```promql
up{job="node-exporter"}
```

---

# Hands-on Lab 5 – CPU Metrics

Find available CPU metrics.

Practice:

```promql
rate(
  node_cpu_seconds_total[5m]
)
```

Then aggregate by:

```text
instance
mode
```

---

# Hands-on Lab 6 – Memory Metrics

Query an available node memory metric.

For example:

```promql
node_memory_MemAvailable_bytes
```

Compare memory availability across nodes.

---

# Hands-on Lab 7 – Application Metrics

Create an application exposing:

```text
http_requests_total
```

Configure Prometheus to scrape it.

---

# Hands-on Lab 8 – Request Rate

Query:

```promql
rate(http_requests_total[5m])
```

Generate traffic and observe the rate change.

---

# Hands-on Lab 9 – Error Rate

Expose HTTP status labels.

Query:

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

Generate controlled failures.

---

# Hands-on Lab 10 – Histogram Latency

Create a histogram:

```text
http_request_duration_seconds
```

Query:

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

Observe P95 latency.

---

# Hands-on Lab 11 – Recording Rule

Create:

```text
job:http_requests:rate5m
```

using a recording rule.

Query:

```promql
job:http_requests:rate5m
```

Compare it with the original query.

---

# Hands-on Lab 12 – Alerting Rule

Create:

```text
HighErrorRate
```

Trigger it using a test application.

Verify:

```text
Inactive
 ↓
Pending
 ↓
Firing
```

---

# Hands-on Lab 13 – Alertmanager

Connect Prometheus to Alertmanager.

Configure a test notification route.

Generate:

```text
Test Alert
```

Verify:

```text
Prometheus
 ↓
Alertmanager
 ↓
Notification
```

---

# Hands-on Lab 14 – ServiceMonitor

If using Prometheus Operator:

Create a:

```text
Service
+
ServiceMonitor
```

Verify that Prometheus discovers and scrapes the application.

---

# Hands-on Lab 15 – PodMonitor

Create:

```text
Pod
+
PodMonitor
```

Verify direct Pod discovery.

---

# Hands-on Lab 16 – Cardinality Investigation

Find metrics with many unique label combinations.

Identify labels such as:

```text
request_id
user_id
session_id
```

Remove them from test metrics and compare:

```text
Series Count
Memory
Query Performance
```

---

# Hands-on Lab 17 – Prometheus Failure

Temporarily stop the Prometheus Pod in a disposable cluster.

Observe:

```text
Metric Collection
Dashboards
Alerts
```

Restore Prometheus and verify recovery.

---

# Hands-on Lab 18 – Target Failure

Stop a test application.

Observe:

```promql
up
```

The target should become:

```text
0
```

Investigate the target in the Prometheus UI.

---

# Hands-on Lab 19 – Query Optimization

Create an expensive PromQL query.

Then optimize it using:

```text
Recording Rules
Better Aggregation
Smaller Time Range
```

Compare query performance.

---

# Hands-on Lab 20 – Production Monitoring Stack

Build:

```text
Kubernetes
   │
   ├── Node Exporter
   ├── kube-state-metrics
   └── Applications
            │
            ▼
        Prometheus
            │
      ┌─────┴─────┐
      ▼           ▼
   Grafana    Alertmanager
```

Then add:

```text
Metrics Server
Logging
Tracing
```

to create a complete observability environment.

---

# Common Mistakes

## 1. High Cardinality

Avoid:

```text
user_id
request_id
session_id
```

as labels.

---

## 2. Using Counters as Gauges

Do not use a Counter for values that naturally move up and down.

---

## 3. Forgetting `rate()`

Counter values alone do not tell you the request rate.

Use:

```promql
rate(counter[5m])
```

---

## 4. Overly Complex Queries

Start simple:

```promql
up
```

then gradually add functions and aggregations.

---

## 5. No Service Discovery

Static targets become difficult to manage in dynamic Kubernetes environments.

---

## 6. No Retention Planning

Prometheus storage can grow rapidly.

---

## 7. Ignoring Scrape Failures

A target being DOWN means you are missing monitoring data.

---

## 8. No Alert Testing

An untested alert is not a reliable alert.

---

## 9. Exposing Prometheus Publicly

Prometheus can reveal sensitive infrastructure information.

---

## 10. Storing Secrets in Metrics

Never expose credentials through metric labels or values.

---

## 11. Using Extremely Short Scrape Intervals Everywhere

This can unnecessarily increase:

```text
CPU
Memory
Network
Storage
```

---

## 12. Using Extremely Long Scrape Intervals

Important short-lived events may be missed or detected too late.

---

## 13. No Cardinality Monitoring

Metric growth should be monitored.

---

## 14. Assuming Prometheus Alone Solves Observability

A mature platform also needs:

```text
Logs
Traces
Events
```

---

# Quick Revision

## Prometheus

```text
Metrics monitoring and alerting platform
```

---

## Scraping

```text
Prometheus retrieves metrics from targets
```

---

## Target

```text
Endpoint from which Prometheus collects metrics
```

---

## Exporter

```text
Component that exposes metrics for systems that do not natively expose Prometheus metrics
```

---

## Counter

```text
Monotonically increasing event metric
```

---

## Gauge

```text
Value that can increase or decrease
```

---

## Histogram

```text
Distribution of observations using buckets
```

---

## Summary

```text
Client-side summary/quantile metric type
```

---

## PromQL

```text
Prometheus Query Language
```

---

## `rate()`

```text
Average per-second increase of a counter over a range
```

---

## `irate()`

```text
Short-term per-second rate based on recent samples
```

---

## `increase()`

```text
Total increase of a counter over a range
```

---

## Recording Rule

```text
Precomputed query result stored as a new time series
```

---

## Alerting Rule

```text
Rule that creates an alert when an expression remains true
```

---

## Alertmanager

```text
Groups, routes, deduplicates, silences, and inhibits alerts
```

---

## ServiceMonitor

```text
Prometheus Operator resource for Service-based scraping
```

---

## PodMonitor

```text
Prometheus Operator resource for Pod-based scraping
```

---

## kube-state-metrics

```text
Exports Kubernetes object state as metrics
```

---

## Node Exporter

```text
Exports host-level metrics
```

---

## Cardinality

```text
Number of unique time series
```

---

## Remote Write

```text
Sends Prometheus samples to a remote metrics system
```

---

# Essential Commands

Check Prometheus Pods:

```bash
kubectl get pods -n monitoring
```

Check Services:

```bash
kubectl get svc -n monitoring
```

Check Prometheus configuration:

```bash
kubectl get configmap -n monitoring
```

View Prometheus logs:

```bash
kubectl logs <prometheus-pod> -n monitoring
```

Check targets through the Prometheus UI:

```text
Status → Targets
```

Check Kubernetes resources:

```bash
kubectl get pods -A
```

Check Metrics Server:

```bash
kubectl top nodes
```

Check HPA:

```bash
kubectl get hpa -A
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

# Important PromQL Queries

Check target health:

```promql
up
```

Check failed targets:

```promql
up == 0
```

Request rate:

```promql
rate(http_requests_total[5m])
```

Request increase:

```promql
increase(http_requests_total[1h])
```

HTTP 5xx rate:

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

Requests by status:

```promql
sum by (status) (
  rate(http_requests_total[5m])
)
```

Requests by service:

```promql
sum by (service) (
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

P99 latency:

```promql
histogram_quantile(
  0.99,
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

- What is Prometheus?
- Why is Prometheus commonly used with Kubernetes?
- What is a time series?
- What is scraping?
- What is a Prometheus target?
- What is an exporter?
- What is PromQL?
- What is a Counter?
- What is a Gauge?
- What is a Histogram?
- What is a Summary?
- What is Alertmanager?
- What is a ServiceMonitor?
- What is a PodMonitor?
- What is kube-state-metrics?
- What is Node Exporter?

---

## Intermediate

- How does Prometheus collect metrics?
- Why does Prometheus use a pull model?
- What is the `/metrics` endpoint?
- What is the difference between a Counter and a Gauge?
- When should you use a Histogram?
- What is the difference between `rate()` and `irate()`?
- What does `increase()` do?
- What is a range vector?
- What is an instant vector?
- What are Prometheus labels?
- What is metric cardinality?
- Why is high cardinality dangerous?
- What are recording rules?
- What are alerting rules?
- What is the purpose of Alertmanager?
- How does Prometheus discover Kubernetes targets?
- What is the difference between ServiceMonitor and PodMonitor?

---

## Advanced

- Explain the complete Prometheus architecture.
- How does Prometheus service discovery work in Kubernetes?
- How would you monitor a 500-node Kubernetes cluster with Prometheus?
- How would you reduce Prometheus memory consumption?
- How would you troubleshoot high Prometheus CPU usage?
- How would you troubleshoot a target that is DOWN?
- How would you troubleshoot Prometheus query performance?
- How would you control metric cardinality?
- How would you design Prometheus for high availability?
- What is Prometheus federation?
- What is remote write?
- How would you implement long-term Prometheus storage?
- How would you monitor Prometheus itself?
- How would you secure Prometheus?
- How would you design a multi-cluster Prometheus architecture?
- How would you prevent metric explosion?
- When would you use a Histogram instead of a Summary?
- How would you design SLO monitoring with Prometheus?

---

# Interview Scenario 1

### Question

> A Prometheus target is DOWN. How would you troubleshoot it?

### Answer

Start from the target:

```text
Target
 ↓
DNS
 ↓
Network
 ↓
Port
 ↓
Metrics Path
 ↓
TLS
 ↓
Authentication
 ↓
Application
```

Check:

```text
Prometheus → Status → Targets
```

Then inspect the target's error.

Common causes:

```text
Connection Refused
Timeout
404
401
403
TLS Error
```

---

# Interview Scenario 2

### Question

> Prometheus memory usage is continuously increasing. What would you investigate?

### Answer

Check:

```text
Time-Series Count
Metric Cardinality
Scrape Rate
Scrape Targets
Retention
Query Load
Remote Write
```

A common cause is:

```text
High Cardinality
```

especially from unbounded labels.

---

# Interview Scenario 3

### Question

> Why should request IDs not be Prometheus labels?

### Answer

Request IDs are usually high-cardinality and effectively unbounded.

For example:

```text
request_id=abc123
request_id=def456
request_id=ghi789
```

Each unique value can create another time series.

This can cause:

```text
Memory Explosion
Storage Growth
Slow Queries
```

Use request IDs in logs/traces instead.

---

# Interview Scenario 4

### Question

> How would you calculate HTTP error rate?

### Answer

For a counter such as:

```text
http_requests_total
```

you can calculate 5xx request rate with:

```promql
sum(
  rate(http_requests_total{
    status=~"5.."
  }[5m])
)
```

For an error percentage:

```promql
100 *
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

---

# Interview Scenario 5

### Question

> What is the difference between `rate()` and `irate()`?

### Answer

```text
rate()
=
Average rate over the selected range
```

```text
irate()
=
Rate calculated using the most recent samples
```

`rate()` is generally more stable and commonly preferred for alerting and dashboards.

`irate()` can be useful for seeing short-lived changes but may be noisier.

---

# Interview Scenario 6

### Question

> How would you calculate P95 latency?

### Answer

If latency is exposed as a Prometheus Histogram:

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

# Interview Scenario 7

### Question

> What is the difference between Metrics Server and Prometheus?

### Answer

Metrics Server primarily provides current Kubernetes resource metrics:

```text
CPU
Memory
```

for:

```text
Nodes
Pods
```

and is commonly consumed by:

```text
kubectl top
HPA
VPA
```

Prometheus provides:

```text
General Metrics
Historical Time Series
PromQL
Application Metrics
Exporters
Alerting Integration
```

---

# Interview Scenario 8

### Question

> How would you monitor Prometheus itself?

### Answer

Monitor:

```text
CPU
Memory
Disk
TSDB Size
Time-Series Count
Scrape Success
Scrape Duration
Query Performance
Rule Evaluation
WAL Health
Remote Write
Alert Delivery
```

Also create alerts for:

```text
Prometheus Down
Storage Almost Full
High Cardinality
Scrape Failures
Remote Write Failures
```

---

# Interview Scenario 9

### Question

> How would you design Prometheus for multiple Kubernetes clusters?

### Answer

A possible architecture:

```text
Cluster A
  ↓
Prometheus A
  ↓
  ├─────────────┐

Cluster B
  ↓
Prometheus B
  ↓
  ├─────────────┤
                ▼
        Central Metrics Store
                │
                ▼
             Grafana
```

Use technologies such as:

```text
Remote Write
Thanos
Mimir
Cortex
```

depending on scale and operational requirements.

---

# Interview Scenario 10

### Question

> Why are Histograms often preferred over Summaries for distributed systems?

### Answer

Histograms expose bucket counts that can be aggregated across instances.

For example:

```text
Pod A
Pod B
Pod C
```

can contribute to a combined histogram.

This makes centralized quantile calculations practical.

Summaries calculate quantiles on individual instances, which makes aggregation of those quantiles generally unsuitable.

---

# Production Prometheus Architecture

```text
                              Kubernetes
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
  Applications              Node Exporter          kube-state-metrics
        │                         │                         │
     /metrics                 /metrics                  /metrics
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  ▼
                           Service Discovery
                                  │
                                  ▼
                              Prometheus
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                   TSDB         PromQL        Rules
                    │             │             │
                    │             ▼             ▼
                    │          Grafana      Alertmanager
                    │                           │
                    ▼                           ▼
              Remote Storage               Notifications
```

---

# Chapter Summary

Prometheus is a powerful metrics monitoring platform built around time-series data.

Its core workflow is:

```text
Discover
 ↓
Scrape
 ↓
Store
 ↓
Query
 ↓
Visualize
 ↓
Alert
```

Prometheus commonly uses:

```text
Pull-Based Collection
```

and retrieves metrics from:

```text
/metrics
```

Important metric types are:

```text
Counter
Gauge
Histogram
Summary
```

PromQL provides powerful querying and aggregation capabilities.

Important functions include:

```promql
rate()
irate()
increase()
sum()
avg()
max()
min()
histogram_quantile()
```

Kubernetes environments commonly integrate Prometheus with:

```text
Node Exporter
kube-state-metrics
Prometheus Operator
ServiceMonitor
PodMonitor
Alertmanager
Grafana
```

The most important production concern is **cardinality**.

Avoid unbounded labels such as:

```text
request_id
user_id
session_id
UUID
```

Use bounded dimensions such as:

```text
service
namespace
method
status
cluster
region
```

Prometheus can be extended for large-scale environments using:

```text
Remote Write
Federation
Thanos
Mimir
Cortex
```

A mature Kubernetes monitoring architecture is:

```text
Kubernetes
 ↓
Service Discovery
 ↓
Prometheus
 ↓
PromQL
 ↓
Grafana
 ↓
Alertmanager
```

while application and infrastructure metrics may come from:

```text
Applications
Node Exporter
kube-state-metrics
```

The most important principle is:

> **Prometheus should collect meaningful, low-cardinality metrics that describe application and infrastructure behavior, then make those metrics actionable through queries, dashboards, recording rules, and alerts.**

---

## Next Chapter

# Chapter 61 – Grafana

Topics will include:

- Grafana Fundamentals
- Why Grafana
- Grafana Architecture
- Grafana Server
- Data Sources
- Prometheus Data Source
- Dashboards
- Panels
- Visualization Types
- Time Series Panels
- Stat Panels
- Gauge Panels
- Table Panels
- Heatmaps
- Variables
- Template Variables
- Query Variables
- Dashboard Variables
- PromQL in Grafana
- Transformations
- Overrides
- Thresholds
- Units
- Legends
- Annotations
- Dashboard Provisioning
- Dashboard as Code
- JSON Dashboards
- Grafana Provisioning
- Alerting
- Grafana Alert Rules
- Contact Points
- Notification Policies
- Alert Groups
- Grafana vs Alertmanager
- Kubernetes Dashboards
- Node Dashboards
- Pod Dashboards
- Cluster Dashboards
- Application Dashboards
- SLO Dashboards
- RED Dashboards
- USE Dashboards
- Variables for Kubernetes
- Namespace Filtering
- Pod Filtering
- Multi-Cluster Dashboards
- Grafana Authentication
- RBAC
- Teams
- Organizations
- Data Source Security
- Secrets
- TLS
- Grafana Plugins
- Grafana APIs
- Production Deployment
- High Availability
- Persistent Storage
- Backup
- Security
- Performance Optimization
- Troubleshooting
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---