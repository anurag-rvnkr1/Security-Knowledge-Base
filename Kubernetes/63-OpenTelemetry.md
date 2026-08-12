# Chapter 63 – OpenTelemetry

## Overview

OpenTelemetry (OTel) is an open-source observability framework for generating, collecting, processing, and exporting telemetry data.

It provides a common approach for:

```text
Metrics
Logs
Traces
```

A modern Kubernetes observability architecture can look like:

```text
                    Applications
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Metrics       Logs       Traces
             │           │           │
             └───────────┼───────────┘
                         ▼
                OpenTelemetry
                    Collector
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
         Prometheus     Loki        Tempo
```

OpenTelemetry does **not** require a single backend.

It provides standardized telemetry generation and transport so organizations can send telemetry to different observability backends.

---

# Learning Objectives

After completing this chapter, you will understand:

- OpenTelemetry fundamentals
- Why OpenTelemetry is used
- Observability concepts
- Metrics
- Logs
- Traces
- OpenTelemetry architecture
- OpenTelemetry API
- OpenTelemetry SDK
- OpenTelemetry Collector
- Receivers
- Processors
- Exporters
- Connectors
- Pipelines
- OTLP
- OTLP over gRPC
- OTLP over HTTP
- Instrumentation
- Automatic instrumentation
- Manual instrumentation
- Context propagation
- Trace context
- Spans
- Parent spans
- Child spans
- Span attributes
- Span events
- Span links
- Resource attributes
- Semantic conventions
- Baggage
- Sampling
- Head sampling
- Tail sampling
- Metrics pipeline
- Logs pipeline
- Traces pipeline
- Kubernetes integration
- OpenTelemetry Collector in Kubernetes
- DaemonSet deployment
- Deployment mode
- Sidecar pattern
- Gateway pattern
- Agent pattern
- Collector scaling
- Prometheus integration
- Grafana integration
- Loki integration
- Tempo integration
- Jaeger integration
- Zipkin integration
- Cloud backends
- Service discovery
- Kubernetes attributes
- Security
- TLS
- Authentication
- RBAC
- Secrets
- Performance
- Resource usage
- High availability
- Troubleshooting
- Production architecture
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is OpenTelemetry?

OpenTelemetry is a vendor-neutral observability framework.

It provides standardized APIs, SDKs, instrumentation libraries, and collectors for telemetry.

The core telemetry signals are:

```text
Traces
Metrics
Logs
```

---

# Why OpenTelemetry?

Without a common standard, applications may use different telemetry libraries:

```text
Application A
    ↓
Vendor SDK

Application B
    ↓
Another Vendor SDK

Application C
    ↓
Custom Agent
```

OpenTelemetry provides a standardized approach:

```text
Application
     ↓
OpenTelemetry
     ↓
Collector
     ↓
Backend
```

---

# OpenTelemetry Is Not a Backend

OpenTelemetry is not primarily a storage system.

It does not replace:

```text
Prometheus
Loki
Tempo
Jaeger
Elasticsearch
```

Instead:

```text
OpenTelemetry
      ↓
Collect / Process / Export
      ↓
Observability Backend
```

---

# OpenTelemetry Architecture

A simplified architecture:

```text
                     Application
                          │
                 OpenTelemetry SDK
                          │
                          ▼
                 OpenTelemetry Collector
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       Metrics           Logs           Traces
          │               │               │
          ▼               ▼               ▼
     Prometheus          Loki           Tempo
```

---

# OpenTelemetry Components

Important components include:

```text
API
SDK
Instrumentation
Collector
Receivers
Processors
Exporters
Connectors
Semantic Conventions
```

---

# OpenTelemetry API

The API provides interfaces that application code can use to create telemetry.

Examples:

```text
Tracer
Meter
Logger
Context
```

The API is designed to allow instrumentation without tightly coupling application code to a specific telemetry backend.

---

# OpenTelemetry SDK

The SDK provides the implementation behind the API.

It handles things such as:

```text
Telemetry Processing
Sampling
Export
Resource Configuration
Instrumentation
```

---

# Instrumentation

Instrumentation means adding telemetry generation to an application.

For example:

```text
HTTP Request
     ↓
Create Span
     ↓
Execute Handler
     ↓
Record Status
     ↓
End Span
```

---

# Automatic Instrumentation

Automatic instrumentation uses libraries or agents to generate telemetry without requiring extensive application code changes.

Example:

```text
Python Application
       ↓
OpenTelemetry Instrumentation
       ↓
HTTP / Database / Framework Telemetry
```

---

# Manual Instrumentation

Manual instrumentation explicitly creates telemetry in application code.

Conceptually:

```python
with tracer.start_as_current_span("process-order"):
    process_order()
```

This is useful when you need application-specific business context.

---

# Automatic vs Manual Instrumentation

| Feature | Automatic | Manual |
|---|---|---|
| Setup | Easier | More Development |
| Code Changes | Minimal | Required |
| Standard Libraries | Strong | Flexible |
| Business Logic | Limited | Excellent |
| Custom Spans | Limited | Excellent |

A production system often uses both.

---

# Observability

Observability is the ability to understand the internal state of a system using its externally exposed telemetry.

The three classic signals are:

```text
Metrics
Logs
Traces
```

---

# Metrics

Metrics are numerical measurements over time.

Examples:

```text
CPU Usage
Memory Usage
Request Rate
Error Rate
Latency
```

Example:

```text
http_requests_total
```

---

# Logs

Logs are records of events.

Example:

```text
2026-08-12T09:10:01
ERROR
Payment database timeout
```

Logs provide detailed event context.

---

# Traces

A trace represents the journey of a request through distributed services.

Example:

```text
Frontend
   ↓
API Gateway
   ↓
Order Service
   ↓
Payment Service
   ↓
Database
```

---

# Distributed Tracing

Without tracing:

```text
Request failed
     ↓
Which service?
```

With tracing:

```text
Frontend
  10ms
   ↓
API
  25ms
   ↓
Payment
  1500ms
   ↓
Database
```

The slow service becomes easier to identify.

---

# Trace

A trace represents an end-to-end operation.

Example:

```text
Trace ID:
abc123
```

It may contain:

```text
Span A
Span B
Span C
Span D
```

---

# Span

A span represents a single operation within a trace.

Example:

```text
Trace
 │
 ├── HTTP GET /orders
 │
 ├── Database Query
 │
 └── Redis GET
```

---

# Parent and Child Spans

Example:

```text
HTTP Request
     │
     ├── Authentication
     │
     ├── Database Query
     │
     └── External API
```

The top-level operation is the parent.

Child spans represent operations performed within it.

---

# Span Attributes

Attributes add structured information to spans.

Example:

```text
http.request.method = GET
server.address = api.example.com
http.response.status_code = 200
```

Use standardized semantic conventions where applicable.

---

# Span Events

Span events represent significant events occurring during a span.

Example:

```text
Span:
Process Payment

Events:
Payment validation started
Payment retry
Payment completed
```

---

# Span Links

Span links associate a span with another span or trace without creating a normal parent-child relationship.

Useful for:

```text
Asynchronous Processing
Message Queues
Batch Processing
Fan-In / Fan-Out
```

---

# Trace Context

Trace context allows distributed services to propagate tracing information.

Example:

```text
Service A
   │
   │ Trace Context
   ▼
Service B
   │
   │ Trace Context
   ▼
Service C
```

---

# Trace ID

A Trace ID identifies the entire distributed operation.

Example:

```text
Trace ID:
4bf92f3577b34da6a3ce929d0e0e4736
```

---

# Span ID

A Span ID identifies an individual operation within a trace.

```text
Trace ID
  │
  ├── Span ID A
  ├── Span ID B
  └── Span ID C
```

---

# W3C Trace Context

OpenTelemetry commonly uses W3C Trace Context propagation.

Important headers include:

```text
traceparent
tracestate
```

This allows tracing context to travel between services.

---

# Baggage

Baggage allows application-defined key-value information to propagate across service boundaries.

Example:

```text
customer-tier=premium
```

Use baggage carefully.

Avoid putting:

```text
Passwords
Tokens
PII
Secrets
```

into baggage.

---

# Resource Attributes

Resource attributes describe the entity producing telemetry.

Example:

```text
service.name=payment-service
service.version=2.1.0
deployment.environment=production
```

For Kubernetes:

```text
k8s.namespace.name=payments
k8s.pod.name=payment-api-abc123
```

---

# Semantic Conventions

Semantic conventions standardize attribute names and meanings.

For example:

```text
service.name
service.version
deployment.environment
```

This improves interoperability.

---

# OpenTelemetry Protocol

OTLP stands for:

```text
OpenTelemetry Protocol
```

It is used to transport telemetry data.

Architecture:

```text
Application
    ↓
OTLP
    ↓
Collector
```

---

# OTLP over gRPC

Telemetry can be transported using:

```text
gRPC
```

Advantages can include:

```text
Efficient Binary Transport
Streaming
Strongly Typed Protocol
```

---

# OTLP over HTTP

OTLP can also use HTTP.

Example concept:

```text
Application
    ↓
HTTP
    ↓
Collector
```

Both gRPC and HTTP transport options are supported by OpenTelemetry components.

---

# OpenTelemetry Collector

The Collector is one of the most important OpenTelemetry components.

It can:

```text
Receive
Process
Transform
Sample
Batch
Export
```

telemetry.

---

# Collector Architecture

```text
              Telemetry Sources
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Metrics       Logs        Traces
        │            │            │
        └────────────┼────────────┘
                     ▼
              OTel Collector
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   Prometheus       Loki          Tempo
```

---

# Collector Components

The major Collector building blocks are:

```text
Receivers
Processors
Exporters
Connectors
Extensions
Service Pipelines
```

---

# Receivers

Receivers accept telemetry.

Examples include:

```text
OTLP
Prometheus
Jaeger
Zipkin
Kafka
Filelog
```

The exact available receivers depend on the Collector distribution/build.

---

# OTLP Receiver

A common receiver is:

```text
OTLP
```

It accepts telemetry from applications and other collectors.

---

# Prometheus Receiver

The Collector can scrape Prometheus-compatible metrics.

Conceptually:

```text
Prometheus Endpoint
       ↓
OTel Collector
```

---

# Filelog Receiver

The filelog receiver can collect logs from files.

For Kubernetes:

```text
Container Logs
     ↓
Filelog Receiver
     ↓
Collector
```

---

# Processors

Processors modify or enrich telemetry.

Common examples:

```text
Batch
Memory Limiter
Resource
Attributes
Filter
Transform
Tail Sampling
```

---

# Batch Processor

The batch processor groups telemetry before exporting it.

Architecture:

```text
Individual Spans
      ↓
Batch Processor
      ↓
Exporter
```

Benefits include:

```text
Reduced Network Overhead
Improved Export Efficiency
```

---

# Memory Limiter

The memory limiter helps protect the Collector from excessive memory consumption.

Architecture:

```text
Telemetry
   ↓
Memory Limiter
   ↓
Other Processors
```

This is important in production deployments.

---

# Resource Processor

Adds or modifies resource attributes.

Example:

```text
service.name
environment
cluster
```

---

# Attributes Processor

Modifies span, metric, or log attributes.

Example:

```text
environment=production
```

---

# Filter Processor

Filters telemetry based on conditions.

Example:

```text
Drop debug logs
```

or:

```text
Drop unwanted telemetry
```

---

# Tail Sampling

Tail sampling makes sampling decisions after seeing trace information.

Architecture:

```text
Spans
 ↓
Collector
 ↓
Tail Sampling
 ↓
Keep Important Traces
```

For example:

```text
Keep:
Errors
High Latency
Important Services

Drop:
Routine Successful Requests
```

---

# Exporters

Exporters send telemetry to external systems.

Examples:

```text
OTLP
Prometheus
Loki
Jaeger
Zipkin
Kafka
```

Availability depends on the Collector distribution and version.

---

# OTLP Exporter

The Collector can export telemetry to another OTLP endpoint.

```text
Collector
    ↓
OTLP
    ↓
Backend
```

---

# Prometheus Export

Metrics can be exposed or exported for Prometheus-compatible consumption depending on the chosen Collector configuration.

Example architecture:

```text
Application
    ↓
OTel Collector
    ↓
Prometheus
```

---

# Loki Integration

Logs can be routed to Loki where supported by the selected Collector/exporter configuration.

```text
Application
    ↓
OTel Collector
    ↓
Loki
```

---

# Tempo Integration

Traces can be exported to Grafana Tempo through supported OTLP integrations.

```text
Application
    ↓
OTel Collector
    ↓
Tempo
```

---

# Jaeger Integration

OpenTelemetry can interoperate with Jaeger through supported protocols and exporters.

Architecture:

```text
Application
    ↓
OTel
    ↓
Collector
    ↓
Jaeger
```

---

# Zipkin Integration

OpenTelemetry can also interoperate with Zipkin-compatible systems.

---

# Connectors

Connectors connect one Collector pipeline to another.

Conceptually:

```text
Metrics Pipeline
       ↓
    Connector
       ↓
Logs / Traces Pipeline
```

Connectors can also generate derived telemetry or route data between pipelines depending on their implementation.

---

# Extensions

Extensions provide additional Collector capabilities such as:

```text
Health Checks
Authentication
Diagnostics
```

---

# Collector Pipelines

A pipeline defines:

```text
Receiver
   ↓
Processors
   ↓
Exporter
```

Example:

```text
OTLP
 ↓
Memory Limiter
 ↓
Batch
 ↓
OTLP Exporter
```

---

# Metrics Pipeline

Example:

```text
Prometheus Receiver
       ↓
Resource Processor
       ↓
Batch Processor
       ↓
Prometheus / OTLP Exporter
```

---

# Logs Pipeline

Example:

```text
Filelog Receiver
       ↓
Resource Processor
       ↓
Batch Processor
       ↓
Loki / OTLP Exporter
```

---

# Traces Pipeline

Example:

```text
OTLP Receiver
       ↓
Memory Limiter
       ↓
Batch
       ↓
Tail Sampling
       ↓
OTLP Exporter
```

---

# Collector Configuration

A simplified configuration might look like:

```yaml
receivers:

  otlp:

    protocols:

      grpc:

      http:


processors:

  memory_limiter:

  batch:


exporters:

  otlp:


service:

  pipelines:

    traces:

      receivers:
        - otlp

      processors:
        - memory_limiter
        - batch

      exporters:
        - otlp
```

Production configuration should include appropriate endpoints, TLS, authentication, resource limits, and error handling.

---

# Collector Deployment Models

Common deployment patterns include:

```text
Agent
DaemonSet
Gateway
Deployment
Sidecar
```

---

# Agent Pattern

Each workload or node sends telemetry to a local Collector.

```text
Application
    ↓
Local Collector
    ↓
Gateway Collector
    ↓
Backend
```

---

# Gateway Pattern

A centralized Collector receives telemetry from multiple workloads.

```text
Applications
      │
 ┌────┼────┐
 ▼    ▼    ▼
OTel  OTel OTel
 │     │    │
 └─────┼────┘
       ▼
 Gateway Collector
       │
       ▼
    Backend
```

---

# DaemonSet Pattern

A Collector can run as a DaemonSet.

```text
Node A → Collector
Node B → Collector
Node C → Collector
```

This is useful for node-local collection.

---

# Deployment Pattern

A Collector can run as a Kubernetes Deployment.

```text
Applications
     ↓
Service
     ↓
Collector Pods
```

This is useful for centralized gateway-style processing.

---

# Sidecar Pattern

A Collector can run alongside an application.

```text
Pod
 ├── Application
 └── OTel Collector
```

This provides strong isolation but increases resource consumption.

---

# Agent vs Gateway

### Agent

```text
Close to workload
Node-local
Collection
```

### Gateway

```text
Centralized
Processing
Sampling
Export
```

A common production architecture uses both.

---

# Kubernetes OpenTelemetry Architecture

```text
                         Kubernetes Cluster
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
         Application A      Application B      Application C
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                        OTel Collector Agents
                                │
                                ▼
                       OTel Gateway Collector
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
          Metrics             Logs               Traces
             │                  │                  │
             ▼                  ▼                  ▼
        Prometheus            Loki               Tempo
```

---

# Kubernetes Attributes

The Kubernetes Attributes Processor can enrich telemetry with Kubernetes metadata.

Examples:

```text
Namespace
Pod
Node
Container
Deployment
ReplicaSet
```

This allows:

```text
Trace
 ↓
Pod
 ↓
Namespace
 ↓
Deployment
```

correlation.

---

# Service Name

Every instrumented service should have a meaningful:

```text
service.name
```

Example:

```text
service.name=payment-api
```

Avoid inconsistent service naming.

---

# Service Version

Useful resource attribute:

```text
service.version=2.4.1
```

This allows analysis such as:

```text
Error Rate
    ↓
Version 2.4.1
```

---

# Deployment Environment

Example:

```text
deployment.environment=production
```

This helps distinguish:

```text
production
staging
development
```

---

# Instrumentation in Kubernetes

A Kubernetes application can be instrumented using:

```text
Application SDK
+
OTel Collector
```

Architecture:

```text
Application
   │
   ▼
OTel SDK
   │
   ▼
OTLP
   │
   ▼
Collector
```

---

# Python Example

Conceptually:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("process-order"):
    process_order()
```

---

# Automatic Python Instrumentation

The OpenTelemetry ecosystem provides instrumentation packages for supported frameworks and libraries.

Conceptually:

```bash
opentelemetry-instrument python app.py
```

The exact packages and environment variables depend on the application and instrumentation setup.

---

# Node.js Instrumentation

Node.js applications can use OpenTelemetry packages for:

```text
HTTP
Express
Database
Other Supported Libraries
```

---

# Java Instrumentation

Java applications commonly use the OpenTelemetry Java agent.

Conceptually:

```text
Application
+
OpenTelemetry Java Agent
```

This can provide automatic instrumentation for supported libraries.

---

# .NET Instrumentation

.NET applications can use OpenTelemetry SDKs and supported instrumentation packages.

---

# Go Instrumentation

Go applications generally use the OpenTelemetry Go SDK with instrumentation libraries and/or manual instrumentation.

---

# Trace Propagation

Example:

```text
Client
 │
 │ traceparent
 ▼
API Gateway
 │
 │ traceparent
 ▼
Order Service
 │
 │ traceparent
 ▼
Payment Service
```

All services can contribute spans to the same trace.

---

# Trace Correlation

A useful observability workflow:

```text
Metric
 ↓
Alert
 ↓
Trace
 ↓
Span
 ↓
Log
```

Example:

```text
High Latency
     ↓
Trace ID
     ↓
Payment Service
     ↓
Database Span
     ↓
Slow Query
```

---

# Sampling

Sampling determines which telemetry is retained.

Without sampling:

```text
1 Million Requests
↓
1 Million Traces
```

With sampling:

```text
1 Million Requests
↓
100,000 Traces
```

The exact rate depends on your architecture.

---

# Head Sampling

Head sampling makes a sampling decision near the beginning of the trace.

Example:

```text
Request Starts
      ↓
Sampling Decision
      ↓
Keep / Drop
```

It is simple and efficient but has limited knowledge of what happens later in the trace.

---

# Tail Sampling

Tail sampling waits until more of the trace is available.

Example:

```text
Trace
 ↓
All / Candidate Spans
 ↓
Evaluate
 ↓
Keep if:
   Error
   High Latency
   Important Service
```

Tail sampling can preserve unusual or important traces more effectively.

---

# Head vs Tail Sampling

| Feature | Head Sampling | Tail Sampling |
|---|---|---|
| Decision | Early | Later |
| Complexity | Lower | Higher |
| Infrastructure | Simpler | More Stateful |
| Error-Aware Sampling | Limited | Strong |
| Resource Usage | Lower | Higher |

---

# Metrics + Traces

Metrics can tell you:

```text
Latency increased
```

Traces can tell you:

```text
Database operation caused latency
```

Together:

```text
Metric
  ↓
Trace
  ↓
Root Cause
```

---

# Logs + Traces

Logs can include:

```text
Trace ID
Span ID
```

This allows engineers to navigate:

```text
Trace
 ↓
Log
```

---

# Metrics + Logs + Traces

A mature observability architecture connects all three:

```text
              Observability
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Metrics        Logs        Traces
       │            │            │
       └────────────┼────────────┘
                    ▼
             Root Cause Analysis
```

---

# OpenTelemetry and Prometheus

OpenTelemetry can participate in a metrics pipeline alongside Prometheus.

Example:

```text
Application
    ↓
OTel SDK
    ↓
Collector
    ↓
Prometheus
    ↓
Grafana
```

The exact architecture depends on whether Prometheus scrapes the Collector, receives remote-written metrics, or another supported integration is used.

---

# OpenTelemetry and Grafana

A common stack is:

```text
OpenTelemetry
      │
 ┌────┼─────┐
 ▼    ▼     ▼
Prom Loki  Tempo
 │    │     │
 └────┼─────┘
      ▼
   Grafana
```

Grafana provides the visualization and exploration layer.

---

# OpenTelemetry and Loki

Logs can flow:

```text
Application
   ↓
OTel Collector
   ↓
Loki
   ↓
Grafana
```

---

# OpenTelemetry and Tempo

Traces can flow:

```text
Application
   ↓
OTel Collector
   ↓
Tempo
   ↓
Grafana
```

---

# OpenTelemetry and Jaeger

Another possible architecture:

```text
Application
   ↓
OTel
   ↓
Collector
   ↓
Jaeger
```

---

# Cloud Backends

OpenTelemetry can export telemetry to supported cloud observability platforms.

The advantage is:

```text
Application
     ↓
OpenTelemetry
     ↓
Change Backend
```

without necessarily rewriting all application instrumentation.

---

# Vendor Neutrality

One of the major OpenTelemetry benefits is reduced application-level coupling to a particular observability vendor.

Architecture:

```text
Application
     ↓
OpenTelemetry
     ↓
Backend A
```

Later:

```text
Application
     ↓
OpenTelemetry
     ↓
Backend B
```

---

# Security

Telemetry can contain sensitive information.

Potential sensitive data:

```text
User IDs
URLs
Database Information
Request Headers
Business Data
```

Do not blindly export everything.

---

# TLS

Use TLS where appropriate for:

```text
Application → Collector
Collector → Collector
Collector → Backend
```

---

# Authentication

Collectors may require authentication when communicating with backends.

Possible mechanisms depend on the integration:

```text
API Keys
Bearer Tokens
mTLS
Basic Authentication
Cloud Identity
```

---

# RBAC

In Kubernetes, protect Collector resources with RBAC.

The Collector may need access to Kubernetes metadata.

Grant only required permissions.

---

# Secrets

Do not hard-code:

```text
API Keys
Tokens
Passwords
Certificates
```

Use:

```text
Kubernetes Secrets
External Secrets
Vault
Cloud Secret Managers
```

---

# Telemetry Filtering

Sensitive telemetry should be filtered or redacted.

For example:

```text
Authorization Header
      ↓
Remove
```

or:

```text
Password Field
      ↓
Redact
```

---

# PII Protection

Avoid exporting unnecessary personal information.

Use:

```text
Filtering
Hashing
Redaction
Tokenization
```

where appropriate.

---

# Collector Performance

Collector performance depends on:

```text
Telemetry Volume
Processors
Sampling
Exporters
Batch Size
Memory
CPU
Network
```

---

# Collector Resource Limits

Kubernetes deployment should define appropriate:

```yaml
resources:
  requests:
    cpu: ...
    memory: ...

  limits:
    cpu: ...
    memory: ...
```

The exact values should be based on telemetry volume and testing.

---

# Collector Backpressure

If the backend is slow:

```text
Collector
   ↓
Queue
   ↓
Exporter
```

Backpressure mechanisms help prevent uncontrolled resource consumption.

---

# Queues

Persistent or in-memory queues can improve resilience depending on exporter and Collector configuration.

Example:

```text
Collector
   ↓
Queue
   ↓
Backend
```

A persistent queue can help survive some temporary backend failures, but it does not replace a proper disaster recovery strategy.

---

# High Availability

A production Collector architecture can use multiple replicas:

```text
               Applications
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Collector Collector Collector
          │         │         │
          └─────────┼─────────┘
                    ▼
              Backend
```

---

# Collector Gateway HA

Example:

```text
Agents
  │
  ├──────────────┐
  ▼              ▼
Gateway A      Gateway B
  │              │
  └──────┬───────┘
         ▼
      Backend
```

This avoids a single gateway becoming a single point of failure.

---

# OpenTelemetry Collector Monitoring

Monitor:

```text
CPU
Memory
Dropped Telemetry
Export Failures
Queue Size
Receiver Errors
Processor Errors
Exporter Errors
```

---

# Collector Self-Observability

The Collector itself can expose telemetry.

This enables:

```text
Collector Health
Pipeline Health
Export Failures
Resource Usage
```

to be monitored.

---

# Kubernetes Deployment

Example conceptual architecture:

```text
Namespace: observability

OTel Collector
     │
     ├── Service
     ├── ConfigMap
     └── ServiceAccount
```

Sensitive configuration can be provided through:

```text
Secret
```

rather than ConfigMap.

---

# Collector ConfigMap

A Kubernetes deployment commonly stores non-secret Collector configuration in a ConfigMap.

Example:

```yaml
apiVersion: v1
kind: ConfigMap

metadata:
  name: otel-collector-config
```

---

# Collector Service

Applications can send telemetry to:

```text
otel-collector.observability.svc
```

The exact DNS name depends on the namespace and Service name.

---

# OTLP Endpoint

A common conceptual endpoint is:

```text
http://otel-collector:4317
```

for OTLP/gRPC.

Another commonly used port is:

```text
4318
```

for OTLP/HTTP.

The exact endpoint depends on the Collector configuration.

---

# Kubernetes Service Discovery

The Collector can use Kubernetes service discovery and metadata enrichment to associate telemetry with:

```text
Service
Pod
Namespace
Node
Deployment
```

---

# Production Architecture

A mature Kubernetes OpenTelemetry architecture may look like:

```text
                    Kubernetes
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Applications         Nodes             Platform
       │                 │                 │
       ▼                 ▼                 ▼
  OTel SDKs        OTel Agents       Kubernetes Metrics
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                  OTel Gateway
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Metrics       Logs        Traces
             │           │           │
             ▼           ▼           ▼
        Prometheus      Loki        Tempo
             │           │           │
             └───────────┼───────────┘
                         ▼
                      Grafana
```

---

# Production Design Principles

Use:

```text
Agents
+
Gateways
+
Batching
+
Memory Limiting
+
Sampling
+
TLS
+
Authentication
+
Monitoring
```

---

# Collector Configuration Best Practices

A production Collector pipeline commonly considers:

```text
Memory Limiter
Batch Processor
Resource Enrichment
Filtering
Sampling
Export Retry
Queueing
```

The exact processor order should be tested for your workload.

---

# Retry

Exporters can retry failed exports.

Architecture:

```text
Collector
   ↓
Exporter
   ↓
Failure
   ↓
Retry
```

Retries should be bounded and combined with appropriate queueing/backpressure controls.

---

# Observability Pipeline

A robust pipeline can be:

```text
Generate
   ↓
Collect
   ↓
Enrich
   ↓
Filter
   ↓
Batch
   ↓
Sample
   ↓
Export
   ↓
Store
   ↓
Visualize
```

---

# Common Mistake

Do not assume:

```text
More Telemetry = Better Observability
```

Instead:

```text
Useful Telemetry
+
Correct Context
+
Good Correlation
=
Better Observability
```

---

# Common Mistakes

## 1. No Resource Limits

A Collector can consume excessive resources under high telemetry volume.

---

## 2. No Memory Limiter

Memory pressure can destabilize the Collector.

---

## 3. Exporting Everything

This can create:

```text
High Cost
High Storage
High Network Usage
```

---

## 4. No Sampling

High-volume distributed tracing can become expensive.

---

## 5. Bad Service Names

Inconsistent:

```text
payment
payment-api
payments
payment_service
```

makes observability harder.

Use consistent naming conventions.

---

## 6. Sensitive Data in Telemetry

Never blindly export:

```text
Passwords
Tokens
Secrets
Sensitive Personal Data
```

---

## 7. Single Collector Instance

A single Collector can become a single point of failure.

---

## 8. No Monitoring of Collector

You need to monitor:

```text
Dropped Data
Export Failures
Queue Size
CPU
Memory
```

---

## 9. Poor Sampling Strategy

Dropping all slow/error traces can destroy valuable troubleshooting data.

---

## 10. Incorrect Context Propagation

Broken propagation creates disconnected traces.

---

# Troubleshooting

## No Traces

Check:

```text
Instrumentation
OTLP Endpoint
Collector Receiver
Network
TLS
Authentication
Exporter
Backend
```

---

# No Metrics

Check:

```text
Metric Instrumentation
Collector Metrics Pipeline
Exporter
Backend
```

---

# No Logs

Check:

```text
Log Source
File Permissions
Filelog Configuration
Collector Pipeline
Exporter
Backend
```

---

# Broken Distributed Trace

Possible causes:

```text
Trace Context Not Propagated
Different Propagators
Instrumentation Misconfiguration
Proxy Header Removal
```

---

# Collector Export Failure

Check:

```text
Backend URL
DNS
Network
TLS
Authentication
Credentials
Exporter Configuration
```

---

# Collector Memory Usage Too High

Investigate:

```text
Telemetry Volume
Batch Size
Queue Size
Sampling
Processor Configuration
Memory Limiter
```

---

# Collector CPU Usage Too High

Investigate:

```text
Telemetry Volume
Expensive Processors
High Cardinality
Sampling
Export Rate
```

---

# Dropped Telemetry

Possible causes:

```text
Memory Pressure
Queue Overflow
Exporter Failure
Invalid Data
Filtering
Backpressure
```

---

# Trace Sampling Troubleshooting

If important traces are missing:

```text
Check Sampling Configuration
Check Tail Sampling Rules
Check Collector Logs
Check Exporter
```

---

# Best Practices

### 1. Standardize Resource Attributes

Use:

```text
service.name
service.version
deployment.environment
```

---

### 2. Use Semantic Conventions

Standardized attributes improve interoperability.

---

### 3. Use Automatic Instrumentation Carefully

Automatic instrumentation is useful, but validate:

```text
Overhead
Cardinality
Data Sensitivity
```

---

### 4. Add Manual Instrumentation Where Valuable

Add business-specific spans where automatic instrumentation cannot provide enough context.

---

### 5. Use Sampling

Especially for high-volume tracing environments.

---

### 6. Protect Sensitive Data

Filter and redact telemetry.

---

### 7. Use Collector Agents

For node-local or workload-local collection.

---

### 8. Use Gateway Collectors

For centralized:

```text
Processing
Sampling
Export
```

---

### 9. Monitor the Collector

Treat the Collector as production infrastructure.

---

### 10. Design for Failure

Use:

```text
Multiple Collectors
Queues
Retries
HA Backends
```

where appropriate.

---

# Hands-on Lab 1 – Deploy OpenTelemetry Collector

Deploy a Collector in Kubernetes.

Verify:

```bash
kubectl get pods -n observability
```

---

# Hands-on Lab 2 – Configure OTLP

Configure:

```text
Application
   ↓
OTLP
   ↓
Collector
```

Verify that telemetry reaches the Collector.

---

# Hands-on Lab 3 – Instrument an Application

Create a simple application.

Add:

```text
HTTP Span
Database Span
Custom Business Span
```

---

# Hands-on Lab 4 – Distributed Tracing

Deploy:

```text
Frontend
API
Payment Service
Database
```

Generate one request.

Verify a single distributed trace contains multiple service spans.

---

# Hands-on Lab 5 – Resource Attributes

Configure:

```text
service.name
service.version
deployment.environment
```

Verify these attributes appear in the backend.

---

# Hands-on Lab 6 – Kubernetes Attributes

Deploy an OTel Collector with Kubernetes metadata enrichment.

Verify telemetry contains:

```text
Namespace
Pod
Node
Container
```

where supported by the configured processor and permissions.

---

# Hands-on Lab 7 – Metrics Pipeline

Build:

```text
OTLP
 ↓
Resource
 ↓
Batch
 ↓
Metrics Backend
```

Verify metrics.

---

# Hands-on Lab 8 – Logs Pipeline

Build:

```text
Filelog
 ↓
Resource
 ↓
Batch
 ↓
Loki
```

Verify logs in Grafana.

---

# Hands-on Lab 9 – Traces Pipeline

Build:

```text
OTLP
 ↓
Batch
 ↓
Tempo
```

Verify traces in Grafana.

---

# Hands-on Lab 10 – Metrics + Logs + Traces

Build:

```text
Application
   │
   ├── Metrics
   ├── Logs
   └── Traces
          │
          ▼
      OTel Collector
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
   Prom   Loki  Tempo
```

---

# Hands-on Lab 11 – Sampling

Generate:

```text
1000 traces
```

Configure sampling.

Compare:

```text
Generated
vs
Exported
```

---

# Hands-on Lab 12 – Tail Sampling

Keep:

```text
Errors
High Latency
```

Drop most routine successful traces.

---

# Hands-on Lab 13 – Collector HA

Deploy multiple gateway Collectors.

Test:

```text
Collector A Failure
```

Verify telemetry continues through the remaining Collector instances.

---

# Hands-on Lab 14 – Backend Failure

Temporarily make the backend unavailable.

Observe:

```text
Retries
Queue
Dropped Data
Collector Logs
```

---

# Hands-on Lab 15 – Security

Configure:

```text
TLS
Authentication
Kubernetes Secrets
```

for a test Collector deployment.

---

# Hands-on Lab 16 – Sensitive Data Filtering

Create telemetry containing a fake secret.

Configure filtering/redaction.

Verify the secret is not exported.

---

# Hands-on Lab 17 – Collector Monitoring

Monitor:

```text
CPU
Memory
Export Failures
Dropped Telemetry
Queue Size
```

---

# Hands-on Lab 18 – Trace-to-Log Correlation

Configure logs and traces so that:

```text
Trace ID
```

can be used to locate related logs.

---

# Hands-on Lab 19 – Kubernetes Incident Investigation

Simulate:

```text
High Application Latency
```

Use:

```text
Grafana
Metrics
Traces
Logs
```

to determine the root cause.

---

# Hands-on Lab 20 – Production OpenTelemetry Architecture

Build:

```text
Applications
     │
     ▼
OTel Agents
     │
     ▼
OTel Gateways
     │
 ┌───┼────┐
 ▼   ▼    ▼
Prom Loki Tempo
 │   │    │
 └───┼────┘
     ▼
  Grafana
```

Add:

```text
Sampling
TLS
Authentication
Resource Limits
Monitoring
HA
```

---

# Quick Revision

## OpenTelemetry

```text
Vendor-neutral observability framework
```

---

## Telemetry

```text
Metrics
Logs
Traces
```

---

## API

```text
Interfaces used to create telemetry
```

---

## SDK

```text
Implementation that generates/processes telemetry
```

---

## Instrumentation

```text
Adding telemetry generation to an application
```

---

## Collector

```text
Receive + Process + Export Telemetry
```

---

## Receiver

```text
Accepts telemetry
```

---

## Processor

```text
Modifies/enriches/filters telemetry
```

---

## Exporter

```text
Sends telemetry to a backend
```

---

## Connector

```text
Connects Collector pipelines
```

---

## OTLP

```text
OpenTelemetry Protocol
```

---

## Span

```text
Individual operation within a trace
```

---

## Trace

```text
Collection of related spans representing an operation
```

---

## Trace Context

```text
Information propagated between services to connect spans
```

---

## Resource Attributes

```text
Metadata describing the telemetry-producing entity
```

---

## Semantic Conventions

```text
Standardized telemetry attribute definitions
```

---

## Head Sampling

```text
Sampling decision made early
```

---

## Tail Sampling

```text
Sampling decision made after more trace information is available
```

---

# Essential Kubernetes Commands

Create namespace:

```bash
kubectl create namespace observability
```

Check Collector:

```bash
kubectl get pods -n observability
```

Check services:

```bash
kubectl get svc -n observability
```

Check configuration:

```bash
kubectl get configmap -n observability
```

View Collector logs:

```bash
kubectl logs \
  deployment/otel-collector \
  -n observability
```

Check DaemonSets:

```bash
kubectl get daemonset -n observability
```

Check deployments:

```bash
kubectl get deployment -n observability
```

Describe a Collector Pod:

```bash
kubectl describe pod \
  <pod-name> \
  -n observability
```

---

# Interview Questions

## Basic

- What is OpenTelemetry?
- Why is OpenTelemetry used?
- What are the three major telemetry signals?
- What is the OpenTelemetry Collector?
- What is OTLP?
- What is a trace?
- What is a span?
- What is a parent span?
- What is a child span?
- What is instrumentation?
- What is automatic instrumentation?
- What is manual instrumentation?
- What is a resource attribute?
- What are semantic conventions?
- What is trace context?
- What is baggage?

---

## Intermediate

- What are the components of the OpenTelemetry Collector?
- What is a receiver?
- What is a processor?
- What is an exporter?
- What is a connector?
- What is a Collector pipeline?
- What is the difference between OTLP/gRPC and OTLP/HTTP?
- What is head sampling?
- What is tail sampling?
- Why would you use an OTel Collector?
- How do you deploy an OTel Collector in Kubernetes?
- What is the difference between Agent and Gateway deployment?
- Why use a Collector DaemonSet?
- Why use a Collector Deployment?
- How does OpenTelemetry integrate with Prometheus?
- How does OpenTelemetry integrate with Grafana?
- How does OpenTelemetry integrate with Loki?
- How does OpenTelemetry integrate with Tempo?

---

## Advanced

- Design a production OpenTelemetry architecture for Kubernetes.
- Explain Agent + Gateway Collector architecture.
- How would you implement high availability for OTel Collectors?
- How would you perform tail-based sampling?
- How would you prevent Collector memory exhaustion?
- How would you handle backend outages?
- How would you secure OTLP traffic?
- How would you prevent sensitive data from being exported?
- How would you correlate logs, metrics, and traces?
- How does trace context propagation work?
- How does OpenTelemetry achieve vendor neutrality?
- How would you monitor the Collector itself?
- How would you troubleshoot missing traces?
- How would you troubleshoot broken distributed traces?
- How would you optimize a high-volume telemetry pipeline?
- How would you design OpenTelemetry for multiple Kubernetes clusters?

---

# Interview Scenario 1

### Question

> What is OpenTelemetry?

### Answer

OpenTelemetry is a vendor-neutral observability framework for generating, collecting, processing, and exporting:

```text
Metrics
Logs
Traces
```

It provides:

```text
APIs
SDKs
Instrumentation
Collector
OTLP
Semantic Conventions
```

It can export telemetry to multiple observability backends.

---

# Interview Scenario 2

### Question

> Is OpenTelemetry a monitoring backend?

### Answer

No.

OpenTelemetry is primarily an observability instrumentation and telemetry pipeline framework.

For example:

```text
Application
     ↓
OpenTelemetry
     ↓
Prometheus / Loki / Tempo
```

The backend stores and queries telemetry.

---

# Interview Scenario 3

### Question

> What is the difference between a trace and a span?

### Answer

A trace represents the complete distributed operation.

A span represents one operation inside that trace.

Example:

```text
Trace
 │
 ├── API Request
 ├── Database Query
 └── Payment API
```

The entire tree is the trace.

Each operation is a span.

---

# Interview Scenario 4

### Question

> What is the OpenTelemetry Collector?

### Answer

The Collector is a vendor-neutral telemetry pipeline component.

It can:

```text
Receive
Process
Filter
Enrich
Sample
Batch
Export
```

telemetry.

---

# Interview Scenario 5

### Question

> What is the difference between a Collector Agent and Gateway?

### Answer

An Agent is deployed close to the telemetry source:

```text
Application
 ↓
Agent
```

A Gateway is centralized:

```text
Agents
 ↓
Gateway
 ↓
Backend
```

Agents are useful for local collection.

Gateways are useful for centralized:

```text
Processing
Sampling
Routing
Export
```

---

# Interview Scenario 6

### Question

> What is tail sampling?

### Answer

Tail sampling makes a sampling decision after enough trace information has been collected.

For example:

```text
Keep:
Errors
High Latency
Critical Services
```

while dropping routine successful traces.

This can preserve valuable troubleshooting traces while reducing storage and network costs.

---

# Interview Scenario 7

### Question

> How does distributed tracing work across Kubernetes services?

### Answer

The tracing context is propagated between services.

Example:

```text
Frontend
   ↓
API
   ↓
Payment
   ↓
Database
```

Each service creates spans using the propagated Trace ID.

The backend can then reconstruct the complete request path.

---

# Interview Scenario 8

### Question

> How would you troubleshoot missing traces?

### Answer

Follow:

```text
Application
 ↓
Instrumentation
 ↓
OTLP
 ↓
Collector Receiver
 ↓
Processors
 ↓
Exporter
 ↓
Backend
```

Check:

```text
Instrumentation
Endpoint
Network
TLS
Authentication
Collector Logs
Exporter
Backend
Sampling
```

---

# Interview Scenario 9

### Question

> How would you protect sensitive data in OpenTelemetry?

### Answer

Use:

```text
Filtering
Redaction
Attribute Processing
Sampling
Access Control
TLS
Secrets Management
```

Avoid exporting:

```text
Passwords
Tokens
API Keys
Sensitive Personal Information
```

unless explicitly required and appropriately protected.

---

# Interview Scenario 10

### Question

> Design an OpenTelemetry architecture for a large Kubernetes cluster.

### Answer

Use:

```text
Application SDKs
       ↓
Node / Workload Collectors
       ↓
Gateway Collectors
       ↓
Processing + Sampling
       ↓
Backends
```

For example:

```text
Applications
     │
     ▼
OTel Agents
     │
     ▼
OTel Gateways
     │
 ┌───┼────┐
 ▼   ▼    ▼
Prom Loki Tempo
     │
     ▼
  Grafana
```

Add:

```text
TLS
Authentication
Resource Limits
Memory Limiter
Batching
Sampling
HA
Monitoring
```

---

# Production OpenTelemetry Checklist

```text
☑ Standard service.name
☑ Standard resource attributes
☑ Semantic conventions
☑ Automatic instrumentation evaluated
☑ Manual instrumentation where needed
☑ OTLP configured
☑ Collector deployed
☑ Memory limiter configured
☑ Batch processor configured
☑ Sampling strategy defined
☑ Sensitive data filtering
☑ TLS configured
☑ Authentication configured
☑ Secrets protected
☑ Collector resource limits
☑ Collector monitoring
☑ Export retry strategy
☑ Queueing where appropriate
☑ High availability
☑ Backend monitoring
☑ Trace/log correlation
```

---

# Chapter Summary

OpenTelemetry provides a standardized way to generate, collect, process, and export observability telemetry.

Its three major signals are:

```text
Metrics
Logs
Traces
```

The major architecture is:

```text
Application
    ↓
Instrumentation
    ↓
OpenTelemetry SDK
    ↓
OTLP
    ↓
OpenTelemetry Collector
    ↓
Backend
```

The Collector consists of:

```text
Receivers
Processors
Exporters
Connectors
Extensions
Pipelines
```

A production Kubernetes deployment commonly uses:

```text
OTel Agents
      ↓
OTel Gateways
      ↓
Observability Backends
```

OpenTelemetry enables:

```text
Vendor Neutrality
Distributed Tracing
Telemetry Standardization
Centralized Processing
Sampling
Telemetry Enrichment
```

A strong Kubernetes observability platform combines:

```text
OpenTelemetry
+
Prometheus
+
Loki
+
Tempo
+
Grafana
```

The most important principle is:

> **OpenTelemetry provides the instrumentation and telemetry pipeline; your observability backends provide storage, querying, and analysis.**

---

## Next Chapter

# Chapter 64 – Distributed Tracing

Topics will include:

- Distributed Tracing Fundamentals
- Why Distributed Tracing
- Observability
- Request Tracing
- Trace
- Span
- Parent Span
- Child Span
- Span Context
- Trace Context
- Trace ID
- Span ID
- Trace Tree
- Trace Graph
- Context Propagation
- W3C Trace Context
- `traceparent`
- `tracestate`
- Baggage
- Sampling
- Head Sampling
- Tail Sampling
- Trace Sampling Strategies
- Latency Analysis
- Error Analysis
- Service Dependencies
- Service Maps
- Critical Path
- Waterfall View
- Trace Attributes
- Span Attributes
- Span Events
- Span Links
- Status
- Span Kind
- Client Spans
- Server Spans
- Producer Spans
- Consumer Spans
- Internal Spans
- Database Tracing
- HTTP Tracing
- gRPC Tracing
- Message Queue Tracing
- Async Tracing
- Kubernetes Distributed Tracing
- OpenTelemetry
- Tempo
- Jaeger
- Zipkin
- Grafana Integration
- Trace-to-Logs Correlation
- Metrics-to-Traces Correlation
- Trace-to-Metrics Correlation
- Exemplars
- Service Dependency Mapping
- Trace Sampling
- Production Architecture
- Performance Considerations
- Security
- PII Protection
- Troubleshooting
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---