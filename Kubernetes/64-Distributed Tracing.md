# Chapter 64 – Distributed Tracing

## Overview

Distributed tracing is an observability technique used to follow a request as it travels through multiple services, processes, databases, APIs, and infrastructure components.

Modern applications are rarely a single process.

A typical request may travel through:

```text
User
 ↓
Load Balancer
 ↓
API Gateway
 ↓
Authentication Service
 ↓
Order Service
 ↓
Payment Service
 ↓
Database
 ↓
Message Queue
```

When a request becomes slow or fails, traditional metrics and logs may tell you **that** something is wrong, but distributed tracing helps identify **where** the problem occurred.

A distributed trace represents the complete journey of one request.

```text
                    Trace
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Gateway       Order      Payment
          │           │           │
          │           └─────┐     │
          │                 ▼     │
          │               Redis   │
          │                       ▼
          │                    Database
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Distributed tracing fundamentals
- Why distributed tracing is important
- Traces
- Spans
- Parent spans
- Child spans
- Span context
- Trace IDs
- Span IDs
- Trace trees
- Trace graphs
- Context propagation
- W3C Trace Context
- `traceparent`
- `tracestate`
- Baggage
- Span kinds
- Client spans
- Server spans
- Producer spans
- Consumer spans
- Internal spans
- Span attributes
- Span events
- Span links
- Span status
- Trace duration
- Span duration
- Critical path
- Waterfall visualization
- Service dependency maps
- HTTP tracing
- Database tracing
- gRPC tracing
- Message queue tracing
- Asynchronous tracing
- Kubernetes tracing
- OpenTelemetry
- Jaeger
- Tempo
- Zipkin
- Grafana integration
- Trace-to-log correlation
- Metrics-to-traces correlation
- Traces-to-metrics correlation
- Exemplars
- Sampling
- Head sampling
- Tail sampling
- Sampling strategies
- Trace retention
- Trace storage
- Trace security
- PII protection
- Production architecture
- Performance considerations
- Troubleshooting
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Distributed Tracing?

Distributed tracing tracks an individual request across multiple services.

For example:

```text
Request
   ↓
API Gateway
   ↓
Order Service
   ↓
Payment Service
   ↓
Database
```

Each operation generates a span.

Together:

```text
Span A
  │
  ├── Span B
  │     └── Span C
  │
  └── Span D
```

form a trace.

---

# Why Distributed Tracing?

Consider a request:

```text
GET /checkout
```

The response takes:

```text
3.5 seconds
```

Metrics tell you:

```text
Checkout latency = 3.5s
```

Logs may tell you:

```text
Payment service timeout
```

Tracing can show:

```text
Gateway       50ms
Order         100ms
Payment       3.1s
Database      2.9s
```

Now the likely bottleneck is much easier to identify.

---

# Distributed Tracing vs Traditional Logging

Traditional logs:

```text
Service A:
Request received

Service B:
Processing request

Service C:
Database timeout
```

The challenge is determining which log entries belong to the same request.

Distributed tracing adds:

```text
Trace ID
Span ID
```

allowing events across services to be correlated.

---

# Trace

A trace represents one end-to-end operation.

Example:

```text
Trace ID:
abc123
```

It may contain:

```text
Gateway Span
Order Span
Payment Span
Database Span
```

---

# Span

A span represents a single operation.

Example:

```text
HTTP GET /orders
```

or:

```text
SELECT * FROM orders
```

or:

```text
POST payment
```

Each span has a start time and end time.

---

# Span Duration

If:

```text
Start:
10:00:00.100

End:
10:00:00.350
```

then:

```text
Duration = 250ms
```

Span duration is useful for identifying slow operations.

---

# Parent Span

A parent span represents the operation that initiated a child operation.

Example:

```text
HTTP Request
     │
     ├── Database Query
     └── External API
```

The HTTP span is the parent.

---

# Child Span

A child span represents an operation performed within a parent operation.

Example:

```text
API Request
    │
    └── Database Query
```

The database query is a child span.

---

# Trace Tree

A trace can be represented as a tree.

```text
HTTP Request
│
├── Authentication
│
├── Database Query
│
├── Payment API
│   ├── Redis
│   └── Database
│
└── Response
```

---

# Trace Graph

A trace graph represents relationships between operations.

For a microservice architecture:

```text
Gateway
   ↓
Order
   ├── Inventory
   ├── Payment
   └── Shipping
```

This makes service dependencies easier to understand.

---

# Trace ID

A Trace ID identifies the complete trace.

Example:

```text
4bf92f3577b34da6a3ce929d0e0e4736
```

All related spans belonging to the same trace share the same Trace ID.

---

# Span ID

A Span ID identifies one individual span.

Example:

```text
00f067aa0ba902b7
```

A trace can contain many Span IDs.

```text
Trace ID
 │
 ├── Span ID A
 ├── Span ID B
 ├── Span ID C
 └── Span ID D
```

---

# Trace Context

Trace context contains information required to propagate tracing information between services.

Conceptually:

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

# Context Propagation

Context propagation is one of the most important concepts in distributed tracing.

Without propagation:

```text
Service A
   ↓
Trace A

Service B
   ↓
Trace B
```

The backend cannot easily know that they belong to the same request.

With propagation:

```text
Service A
   ↓
Trace ID
   ↓
Service B
   ↓
Same Trace ID
```

The complete request can be reconstructed.

---

# W3C Trace Context

OpenTelemetry commonly uses the W3C Trace Context standard.

Important headers include:

```text
traceparent
tracestate
```

---

# `traceparent`

The `traceparent` header carries the primary tracing context.

Conceptually:

```text
traceparent:
version-trace-id-parent-id-flags
```

Example:

```text
00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

---

# `tracestate`

`tracestate` carries additional vendor-specific tracing state.

It can complement:

```text
traceparent
```

---

# Baggage

Baggage allows application-defined key-value information to propagate across service boundaries.

Example:

```text
customer-tier=premium
```

Baggage should be used carefully.

Never place sensitive information such as:

```text
Passwords
API Keys
Authentication Tokens
Secrets
```

into baggage.

---

# Span Attributes

Attributes describe a span.

Example:

```text
http.request.method = GET
server.address = api.example.com
http.response.status_code = 200
```

---

# Kubernetes Span Attributes

A span may contain Kubernetes-related metadata such as:

```text
k8s.namespace.name
k8s.pod.name
k8s.container.name
k8s.node.name
```

depending on the instrumentation and Collector configuration.

---

# Span Events

Events represent significant moments inside a span.

Example:

```text
Span:
Process Payment

Events:
Validation Started
Payment Retry
Payment Completed
```

---

# Span Links

Span links associate one span with another span without requiring a parent-child relationship.

They are useful for:

```text
Asynchronous Work
Message Queues
Batch Processing
Fan-In
Fan-Out
```

---

# Span Status

A span can indicate whether an operation succeeded or encountered an error.

Conceptually:

```text
UNSET
OK
ERROR
```

Use status appropriately rather than marking every unusual event as an error.

---

# Span Kind

OpenTelemetry defines span kinds such as:

```text
Internal
Server
Client
Producer
Consumer
```

These describe the role of a span in an interaction.

---

# Internal Span

An internal span represents an operation within an application.

Example:

```text
CalculateOrderTotal
```

---

# Server Span

A server span represents handling an incoming request.

Example:

```text
HTTP Server
    ↓
GET /orders
```

---

# Client Span

A client span represents an outgoing request.

Example:

```text
Order Service
     ↓
Payment API
```

---

# Producer Span

A producer span represents sending a message.

Example:

```text
Order Service
     ↓
Kafka
```

---

# Consumer Span

A consumer span represents processing a received message.

Example:

```text
Kafka
 ↓
Notification Service
```

---

# HTTP Tracing

HTTP requests are commonly traced automatically by OpenTelemetry instrumentation.

Example:

```text
Client
  │
  │ GET /orders
  ▼
Order Service
```

Possible span attributes include:

```text
http.request.method
server.address
server.port
http.response.status_code
```

Use the semantic conventions applicable to the instrumentation version.

---

# HTTP Distributed Trace

```text
Client
  │
  ▼
API Gateway
  │
  ▼
Order Service
  │
  ▼
Payment Service
```

All services can participate in one trace.

---

# Database Tracing

Database operations can be represented as child spans.

Example:

```text
HTTP Request
     │
     └── SQL Query
```

A span may contain metadata describing the database operation.

Avoid recording sensitive query parameters or secrets.

---

# Database Trace Example

```text
GET /checkout
│
├── Validate Cart
│
├── SQL Query
│
├── Payment API
│
└── SQL Update
```

---

# gRPC Tracing

gRPC calls can also participate in distributed traces.

Architecture:

```text
Service A
    │
    │ gRPC
    ▼
Service B
    │
    │ gRPC
    ▼
Service C
```

Tracing context can propagate through supported instrumentation.

---

# Message Queue Tracing

Distributed systems often use:

```text
Kafka
RabbitMQ
Cloud Queues
```

Example:

```text
Order Service
     │
     ▼
Message Queue
     │
     ▼
Shipping Service
```

Producer and consumer spans help connect asynchronous operations.

---

# Asynchronous Tracing

Asynchronous systems are more complex because:

```text
Producer
   ↓
Queue
   ↓
Consumer
```

may not execute immediately.

Trace context must be propagated through the message metadata where supported.

---

# Fan-Out

One request creates multiple operations.

```text
Order Service
   ├── Payment
   ├── Inventory
   └── Shipping
```

Tracing helps visualize parallel work.

---

# Fan-In

Multiple operations converge into one operation.

```text
Payment
Inventory
Shipping
   │
   └──────► Order Completion
```

Span links can be useful in some asynchronous fan-in designs.

---

# Critical Path

The critical path is the sequence of operations that determines overall request latency.

Example:

```text
Request
  │
  ├── Service A: 50ms
  │
  ├── Service B: 100ms
  │
  └── Service C: 1500ms
```

Service C may dominate the critical path.

---

# Parallel Operations

Suppose:

```text
Service A
 ├── B = 500ms
 └── C = 500ms
```

The total may be approximately:

```text
500ms
```

rather than:

```text
1000ms
```

if they execute concurrently.

Tracing makes this relationship visible.

---

# Waterfall View

A waterfall visualization shows spans over time.

Example:

```text
Time ─────────────────────────────►

Gateway    █████████████████████
Order         ███████████████
Payment          █████████████
Database           ███████████
```

This makes latency bottlenecks easy to identify.

---

# Service Dependency Map

Tracing can reveal service relationships.

Example:

```text
Frontend
   ↓
API Gateway
   ↓
Order Service
 ┌─┼─────────┐
 ▼ ▼         ▼
DB Payment Inventory
```

---

# Service Map

A service map answers:

```text
Who calls whom?
```

This is extremely useful in microservice environments.

---

# Trace-to-Logs Correlation

A trace can be correlated with logs using:

```text
Trace ID
Span ID
```

Example:

```text
Trace
 ↓
Span
 ↓
Trace ID
 ↓
Logs
```

---

# Logs With Trace IDs

Example:

```text
INFO
trace_id=abc123
span_id=def456
Payment request started
```

Now the log can be associated with the exact trace.

---

# Metrics-to-Traces Correlation

Suppose:

```text
HTTP latency = 4 seconds
```

A metric can lead you to:

```text
Slow Trace
```

Then:

```text
Trace
 ↓
Slow Span
```

---

# Traces-to-Metrics Correlation

A trace can help identify:

```text
Service
Endpoint
Operation
```

which can then be correlated with service-level metrics.

---

# Exemplars

Exemplars connect metrics with specific trace examples.

Conceptually:

```text
Metric
  ↓
Exemplar
  ↓
Trace
```

For example:

```text
HTTP latency spike
        ↓
Trace ID
        ↓
Slow request
```

---

# Why Exemplars Matter

Without exemplars:

```text
Latency increased
```

With exemplars:

```text
Latency increased
 ↓
Specific trace
 ↓
Database span
 ↓
Slow query
```

This shortens troubleshooting time.

---

# Sampling

Tracing can produce enormous amounts of data.

Suppose:

```text
10 million requests/day
```

Recording every trace may be expensive.

Sampling decides which traces to retain.

---

# Head Sampling

Head sampling makes the decision early.

```text
Request Starts
      ↓
Sampling Decision
      ↓
Keep / Drop
```

Advantages:

```text
Simple
Low Overhead
Predictable
```

Disadvantage:

```text
The sampler may not know whether the request later fails.
```

---

# Tail Sampling

Tail sampling makes the decision after seeing more of the trace.

```text
Trace
 ↓
Collect
 ↓
Analyze
 ↓
Keep / Drop
```

Useful rules:

```text
Keep Errors
Keep Slow Traces
Keep Critical Services
```

---

# Sampling Strategy

A practical strategy may be:

```text
100% of Errors
100% of Very Slow Requests
Lower Percentage of Successful Requests
```

The actual percentages should be determined from workload, cost, and troubleshooting requirements.

---

# Sampling Important Traces

Consider retaining traces when:

```text
Error
High Latency
Important Customer Transaction
Critical Service
Security Investigation
```

---

# Trace Storage

Tracing backends may store:

```text
Trace ID
Span ID
Attributes
Events
Duration
Relationships
```

Examples of tracing backends include:

```text
Tempo
Jaeger
Zipkin
```

---

# Tempo

Grafana Tempo is a distributed tracing backend designed for storing and querying traces.

A common architecture is:

```text
Application
   ↓
OpenTelemetry
   ↓
Collector
   ↓
Tempo
   ↓
Grafana
```

---

# Jaeger

Jaeger is an open-source distributed tracing system.

Architecture:

```text
Application
   ↓
OpenTelemetry
   ↓
Collector
   ↓
Jaeger
```

---

# Zipkin

Zipkin is another distributed tracing system.

It can be used for:

```text
Trace Collection
Trace Storage
Trace Visualization
```

---

# OpenTelemetry + Tracing

A common modern architecture:

```text
Application
     │
     ▼
OpenTelemetry SDK
     │
     ▼
OTLP
     │
     ▼
OpenTelemetry Collector
     │
     ▼
Tempo / Jaeger
     │
     ▼
Grafana / UI
```

---

# Kubernetes Distributed Tracing

A Kubernetes application may contain:

```text
Frontend
Backend
Worker
Database
Message Queue
```

Distributed tracing can connect all components.

---

# Kubernetes Trace Example

```text
User
 ↓
Ingress
 ↓
Frontend
 ↓
API
 ↓
Order Service
 ↓
Payment Service
 ↓
PostgreSQL
```

A single trace can represent this complete path.

---

# Kubernetes Metadata

Tracing can be enriched with:

```text
Cluster
Namespace
Pod
Container
Node
Deployment
Service
```

This allows:

```text
Slow Span
 ↓
Payment Service
 ↓
Pod
 ↓
Node
```

---

# Kubernetes Incident Investigation

Suppose:

```text
Payment API latency = 5 seconds
```

Trace investigation:

```text
Trace
 ↓
Payment Span
 ↓
Database Span
 ↓
Database latency = 4.8 seconds
```

Then investigate:

```text
Database
 ↓
Connection Pool
 ↓
Query
```

---

# Trace Security

Traces may contain:

```text
URLs
Headers
User Identifiers
Database Information
Business Data
```

Treat trace data as sensitive operational data.

---

# PII Protection

Avoid storing unnecessary:

```text
Names
Email Addresses
Phone Numbers
Payment Data
Authentication Data
```

Use filtering and redaction where appropriate.

---

# Authentication Headers

Never record:

```text
Authorization: Bearer <token>
```

in raw telemetry.

If instrumentation captures sensitive headers, configure appropriate sanitization.

---

# Query Parameters

Be careful with:

```text
/api/user?email=user@example.com
```

because URLs can contain personal information.

Filter or sanitize sensitive parameters.

---

# Trace Retention

Trace data can grow rapidly.

Retention should be based on:

```text
Operational Requirements
Security Requirements
Compliance Requirements
Cost
Storage Capacity
```

Do not automatically retain every trace forever.

---

# Trace Cardinality

High-cardinality attributes can increase backend cost and query complexity.

Be careful with attributes such as:

```text
user_id
request_id
session_id
```

especially when used as dimensions in systems where high cardinality creates operational problems.

---

# Performance Overhead

Tracing introduces overhead:

```text
CPU
Memory
Network
Storage
```

Automatic instrumentation should be evaluated for production impact.

---

# Reducing Trace Overhead

Use:

```text
Sampling
Batching
Efficient Export
Filtering
Selective Instrumentation
```

---

# Production Architecture

A production Kubernetes tracing architecture can look like:

```text
                        Kubernetes
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
    Frontend            Backend              Worker
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    OTel Collector Agents
                            │
                            ▼
                    OTel Gateway Layer
                            │
                            ▼
                    Sampling / Processing
                            │
                            ▼
                     Trace Backend
                       ┌────┴────┐
                       ▼         ▼
                     Tempo     Jaeger
                       │
                       ▼
                    Grafana
```

---

# High Availability

Tracing infrastructure should avoid a single point of failure.

Possible architecture:

```text
Applications
      │
 ┌────┴────┐
 ▼         ▼
Collector A Collector B
 └────┬────┘
      ▼
Trace Backend
```

---

# Collector Scaling

Scale Collectors based on:

```text
Trace Volume
Span Rate
CPU
Memory
Network
Export Latency
```

---

# Backend Scaling

Trace backend scaling depends on:

```text
Trace Ingestion Rate
Retention
Query Rate
Storage
Replication
```

---

# Sampling Architecture

A scalable architecture can use:

```text
OTel Agents
     ↓
OTel Gateway
     ↓
Tail Sampling
     ↓
Trace Backend
```

This centralizes sampling decisions.

---

# Trace Pipeline

A typical pipeline:

```text
Application
   ↓
Instrumentation
   ↓
OTLP
   ↓
Collector
   ↓
Enrichment
   ↓
Filtering
   ↓
Sampling
   ↓
Batching
   ↓
Export
   ↓
Trace Backend
```

---

# Distributed Tracing and Incident Response

During an incident:

```text
Alert
 ↓
Metric
 ↓
Trace
 ↓
Slow Span
 ↓
Service
 ↓
Log
 ↓
Root Cause
```

This is one of the most powerful observability workflows.

---

# Distributed Tracing and SRE

Tracing helps SRE teams investigate:

```text
Latency
Errors
Service Dependencies
Capacity Problems
External API Issues
Database Bottlenecks
```

---

# Distributed Tracing and SOC

Tracing can also support security investigations.

Example:

```text
Suspicious Request
 ↓
Trace ID
 ↓
API Gateway
 ↓
Application
 ↓
Database
```

This can help reconstruct request paths during an authorized investigation.

---

# Trace-Based Security Investigation

Potential workflow:

```text
Security Alert
     ↓
Trace ID
     ↓
Request Path
     ↓
Affected Services
     ↓
Related Logs
     ↓
Infrastructure
```

Tracing should complement, not replace, security telemetry and audit logs.

---

# Common Mistakes

## 1. No Context Propagation

Services produce disconnected traces.

---

## 2. Sampling Everything

This can create unnecessary storage and cost.

---

## 3. Sampling Too Aggressively

Important error traces may be lost.

---

## 4. Recording Sensitive Data

Traces can accidentally expose secrets or personal data.

---

## 5. High-Cardinality Attributes

Too many unique dimensions can make systems expensive and difficult to query.

---

## 6. No Trace-to-Log Correlation

Engineers lose an important troubleshooting path.

---

## 7. No Metrics Correlation

Tracing should work with metrics rather than replace them.

---

## 8. No Collector HA

A single Collector can become a failure point.

---

## 9. Ignoring Async Workflows

Message queues require careful context propagation.

---

## 10. No Retention Strategy

Trace storage can grow rapidly.

---

# Troubleshooting

## No Trace Appears

Check:

```text
Instrumentation
SDK
OTLP Endpoint
Collector
Network
Exporter
Backend
Sampling
```

---

# Trace Appears Incomplete

Check:

```text
Context Propagation
traceparent
Instrumentation
Proxy Configuration
Async Context
```

---

# Services Have Separate Traces

Possible causes:

```text
Trace Context Not Propagated
Different Propagators
Missing Instrumentation
Headers Removed
```

---

# Trace Is Missing Important Spans

Check:

```text
Sampling
Instrumentation
Span Creation
Exporter
Backend
```

---

# Trace Shows Wrong Service

Check:

```text
service.name
Resource Attributes
Instrumentation Configuration
```

---

# High Trace Volume

Investigate:

```text
Sampling
Instrumentation
High Cardinality
Span Creation
Repeated Requests
```

---

# Slow Trace Queries

Possible causes:

```text
Huge Trace Volume
Long Retention
High Cardinality
Backend Resource Constraints
```

---

# Trace Backend Unavailable

Check:

```text
Collector Exporter
Network
DNS
TLS
Authentication
Queue
Retries
Backend Health
```

---

# Best Practices

### 1. Standardize Service Names

Use consistent:

```text
service.name
```

values.

---

### 2. Propagate Context Everywhere

Ensure supported service-to-service communication carries trace context.

---

### 3. Use Semantic Conventions

Standardized attributes make traces easier to analyze.

---

### 4. Correlate Metrics, Logs, and Traces

Build:

```text
Metrics
 ↓
Trace
 ↓
Logs
```

connections.

---

### 5. Use Sampling

Retain important traces while controlling cost.

---

### 6. Protect Sensitive Data

Redact:

```text
Tokens
Passwords
PII
Secrets
```

---

### 7. Monitor Trace Infrastructure

Monitor:

```text
Collector
Exporter
Backend
Storage
Sampling
Dropped Spans
```

---

### 8. Use HA

Avoid a single Collector or backend instance becoming a critical failure point.

---

### 9. Instrument Critical Paths

Prioritize:

```text
Authentication
Payments
Orders
Database
External APIs
```

---

### 10. Document Trace Operations

Define:

```text
How to Search
How to Correlate
How to Investigate
How to Troubleshoot
```

---

# Hands-on Lab 1 – Basic Trace

Create a simple HTTP application.

Instrument:

```text
GET /hello
```

Generate a trace.

Verify:

```text
Trace ID
Span ID
Duration
Status
```

---

# Hands-on Lab 2 – Parent and Child Spans

Create:

```text
HTTP Request
   ↓
Business Logic
   ↓
Database Query
```

Verify the span hierarchy.

---

# Hands-on Lab 3 – Microservice Trace

Deploy:

```text
Frontend
API
Payment
```

Send one request.

Verify:

```text
Frontend
 ↓
API
 ↓
Payment
```

appears as one distributed trace.

---

# Hands-on Lab 4 – Context Propagation

Inspect:

```text
traceparent
```

between services.

Verify that the same Trace ID is propagated.

---

# Hands-on Lab 5 – HTTP Tracing

Generate:

```text
GET
POST
PUT
DELETE
```

requests.

Inspect:

```text
Method
Status
Duration
Service
```

---

# Hands-on Lab 6 – Database Tracing

Create:

```text
API
 ↓
PostgreSQL
```

Trace a database query.

Identify:

```text
Database Span
Query Duration
Parent Span
```

---

# Hands-on Lab 7 – gRPC Tracing

Create:

```text
Service A
 ↓
gRPC
 ↓
Service B
```

Verify distributed trace propagation.

---

# Hands-on Lab 8 – Message Queue Tracing

Create:

```text
Producer
 ↓
Kafka / RabbitMQ
 ↓
Consumer
```

Propagate trace context through the message.

---

# Hands-on Lab 9 – Trace-to-Log Correlation

Configure application logs with:

```text
trace_id
span_id
```

Find logs from a specific trace.

---

# Hands-on Lab 10 – Metrics-to-Traces

Create:

```text
HTTP latency metric
```

with trace exemplars if supported by your stack.

Navigate:

```text
Metric
 ↓
Exemplar
 ↓
Trace
```

---

# Hands-on Lab 11 – Kubernetes Metadata

Deploy the application in Kubernetes.

Add:

```text
Namespace
Pod
Container
Node
Service
```

metadata to telemetry where supported.

---

# Hands-on Lab 12 – Sampling

Generate:

```text
1000 requests
```

Configure sampling.

Compare:

```text
Generated Traces
vs
Stored Traces
```

---

# Hands-on Lab 13 – Tail Sampling

Configure a test policy:

```text
Keep Errors
Keep Slow Requests
Sample Normal Requests
```

Verify the result.

---

# Hands-on Lab 14 – Slow Database

Create an intentionally slow test query in a disposable environment.

Trace:

```text
HTTP
 ↓
Service
 ↓
Database
```

Identify the database as the bottleneck.

---

# Hands-on Lab 15 – Error Trace

Generate an application error.

Verify:

```text
Span Status
Error Information
Trace
Logs
```

---

# Hands-on Lab 16 – Fan-Out

Create:

```text
Order Service
 ├── Payment
 ├── Inventory
 └── Shipping
```

Trace the request.

Observe parallel spans.

---

# Hands-on Lab 17 – Trace Backend

Deploy:

```text
OpenTelemetry Collector
+
Tempo / Jaeger
```

Send traces to the backend.

---

# Hands-on Lab 18 – Collector HA

Deploy multiple Collector replicas.

Simulate one Collector failure.

Verify trace ingestion continues according to your architecture.

---

# Hands-on Lab 19 – Sensitive Data Filtering

Generate a fake:

```text
Authorization Header
```

Configure filtering.

Verify it does not appear in the stored trace.

---

# Hands-on Lab 20 – End-to-End Incident

Simulate:

```text
High API Latency
```

Investigate using:

```text
Prometheus
Grafana
OpenTelemetry
Trace Backend
Logs
```

Find:

```text
Slow Service
 ↓
Slow Span
 ↓
Database
 ↓
Root Cause
```

---

# Quick Revision

## Distributed Tracing

```text
Tracks a request across distributed services
```

---

## Trace

```text
Complete distributed operation
```

---

## Span

```text
Individual operation inside a trace
```

---

## Trace ID

```text
Identifies the complete trace
```

---

## Span ID

```text
Identifies one span
```

---

## Parent Span

```text
Span that initiated another operation
```

---

## Child Span

```text
Operation performed within a parent span
```

---

## Context Propagation

```text
Transfers trace context between services
```

---

## `traceparent`

```text
W3C header carrying trace context
```

---

## `tracestate`

```text
Additional tracing state
```

---

## Baggage

```text
Application-defined key-value context propagated across services
```

---

## Span Attribute

```text
Structured metadata attached to a span
```

---

## Span Event

```text
Timestamped event inside a span
```

---

## Span Link

```text
Relationship between spans without normal parent-child hierarchy
```

---

## Sampling

```text
Selecting which traces to retain
```

---

## Head Sampling

```text
Sampling decision made early
```

---

## Tail Sampling

```text
Sampling decision made after more trace data is available
```

---

## Service Map

```text
Shows service-to-service relationships
```

---

## Critical Path

```text
Operations that determine overall request latency
```

---

## Exemplar

```text
Connects a metric measurement to a representative trace
```

---

# Essential Commands

Check tracing namespace:

```bash
kubectl get pods -n observability
```

Check Collector:

```bash
kubectl get deployment -n observability
```

Check Collector logs:

```bash
kubectl logs \
  deployment/otel-collector \
  -n observability
```

Check services:

```bash
kubectl get svc -n observability
```

Check endpoints:

```bash
kubectl get endpoints -n observability
```

Check configuration:

```bash
kubectl get configmap -n observability
```

Describe Collector:

```bash
kubectl describe deployment \
  otel-collector \
  -n observability
```

---

# Interview Questions

## Basic

- What is distributed tracing?
- Why is distributed tracing required?
- What is a trace?
- What is a span?
- What is a Trace ID?
- What is a Span ID?
- What is a parent span?
- What is a child span?
- What is context propagation?
- What is `traceparent`?
- What is `tracestate`?
- What is baggage?
- What is a span attribute?
- What is a span event?
- What is a span link?
- What is sampling?

---

## Intermediate

- How does distributed tracing work across microservices?
- How does OpenTelemetry propagate trace context?
- What is W3C Trace Context?
- What is the difference between Trace ID and Span ID?
- What is the difference between a trace tree and a service map?
- What are span kinds?
- What is an internal span?
- What is a server span?
- What is a client span?
- What is a producer span?
- What is a consumer span?
- How does HTTP tracing work?
- How does database tracing work?
- How does gRPC tracing work?
- How does message queue tracing work?
- What is the critical path?
- What is a waterfall trace?
- What are exemplars?
- How do you correlate traces with logs?
- How do you correlate metrics with traces?

---

## Advanced

- Design distributed tracing for a large Kubernetes environment.
- Explain end-to-end trace propagation across microservices.
- How would you trace asynchronous message processing?
- How would you implement tail-based sampling?
- How would you identify the critical path of a request?
- How would you troubleshoot broken traces?
- How would you prevent sensitive data from entering traces?
- How would you handle high-cardinality span attributes?
- How would you scale an OpenTelemetry Collector?
- How would you design highly available trace collection?
- How would you reduce tracing costs?
- How would you integrate tracing with Prometheus and Grafana?
- How would you integrate traces with logs?
- How would you use exemplars?
- How would you investigate a Kubernetes latency incident using traces?

---

# Interview Scenario 1

### Question

> What is distributed tracing?

### Answer

Distributed tracing is an observability technique that follows an individual request across multiple services and infrastructure components.

Each operation creates a span, and related spans are connected using trace context.

```text
Request
 ↓
Service A
 ↓
Service B
 ↓
Database
```

Together these operations form one distributed trace.

---

# Interview Scenario 2

### Question

> What is the difference between a trace and a span?

### Answer

A trace represents the complete end-to-end operation.

A span represents one individual operation within that trace.

```text
Trace
 │
 ├── API Span
 ├── Database Span
 └── Payment Span
```

---

# Interview Scenario 3

### Question

> How does tracing work between two microservices?

### Answer

The first service creates a span and propagates trace context through the request.

```text
Service A
   │
   │ traceparent
   ▼
Service B
```

Service B extracts the context and creates a child span belonging to the same trace.

---

# Interview Scenario 4

### Question

> What is the purpose of `traceparent`?

### Answer

`traceparent` is a W3C Trace Context HTTP header used to propagate tracing information between services.

It carries information such as:

```text
Trace ID
Parent Span ID
Trace Flags
```

This allows distributed services to connect their spans into one trace.

---

# Interview Scenario 5

### Question

> A request takes 10 seconds. How would distributed tracing help?

### Answer

Open the trace and inspect the waterfall:

```text
Gateway       100ms
Order         200ms
Payment       300ms
Database     9.2s
```

The trace immediately indicates that the database operation is dominating latency.

---

# Interview Scenario 6

### Question

> What is the difference between head and tail sampling?

### Answer

Head sampling decides whether to retain a trace near the beginning:

```text
Request
 ↓
Decision
 ↓
Keep / Drop
```

Tail sampling waits until more of the trace is available:

```text
Trace
 ↓
Analyze
 ↓
Decision
```

Tail sampling can make decisions based on conditions such as:

```text
Errors
High Latency
Important Services
```

---

# Interview Scenario 7

### Question

> How do you correlate logs with traces?

### Answer

Include:

```text
Trace ID
Span ID
```

in application logs.

Then:

```text
Trace
 ↓
Trace ID
 ↓
Related Logs
```

This allows engineers to move from a trace to detailed application logs.

---

# Interview Scenario 8

### Question

> What are exemplars?

### Answer

Exemplars associate a metric measurement with a representative trace.

For example:

```text
High Latency Metric
       ↓
Exemplar
       ↓
Trace
       ↓
Slow Database Span
```

They make it easier to move from aggregated metrics to individual requests.

---

# Interview Scenario 9

### Question

> How would you trace Kafka-based asynchronous communication?

### Answer

Use producer and consumer spans and propagate trace context through message metadata.

```text
Producer
   ↓
Kafka
   ↓
Consumer
```

For asynchronous relationships where parent-child relationships are not sufficient, span links can also be useful.

---

# Interview Scenario 10

### Question

> Design distributed tracing for Kubernetes.

### Answer

Use:

```text
Application Instrumentation
        ↓
OpenTelemetry SDK
        ↓
OTLP
        ↓
OTel Collector Agents
        ↓
OTel Gateway
        ↓
Sampling
        ↓
Tempo / Jaeger
        ↓
Grafana
```

Add:

```text
Kubernetes Metadata
Context Propagation
TLS
Authentication
Sampling
HA
Resource Limits
Trace-to-Log Correlation
```

---

# Production Distributed Tracing Checklist

```text
☑ OpenTelemetry instrumentation
☑ Consistent service.name
☑ Trace context propagation
☑ W3C Trace Context
☑ HTTP tracing
☑ Database tracing
☑ gRPC tracing
☑ Message queue tracing
☑ Kubernetes metadata
☑ Trace-to-log correlation
☑ Metrics-to-trace correlation
☑ Exemplars where supported
☑ Sampling strategy
☑ Sensitive data filtering
☑ PII protection
☑ Collector HA
☑ Backend HA
☑ Trace retention policy
☑ Resource limits
☑ Monitoring
☑ Troubleshooting runbook
```

---

# Chapter Summary

Distributed tracing provides visibility into the complete journey of a request across distributed systems.

The core hierarchy is:

```text
Trace
  │
  ├── Span
  │     ├── Child Span
  │     └── Child Span
  │
  └── Span
```

A distributed request may travel through:

```text
Gateway
 ↓
Service
 ↓
Database
 ↓
Message Queue
 ↓
Worker
```

Trace context allows all related operations to remain connected.

Important concepts include:

```text
Trace ID
Span ID
Parent / Child Spans
Context Propagation
traceparent
tracestate
Baggage
Span Attributes
Span Events
Span Links
Sampling
Critical Path
Service Maps
Exemplars
```

A production architecture commonly looks like:

```text
Applications
     ↓
OpenTelemetry SDK
     ↓
OTel Collectors
     ↓
Sampling / Processing
     ↓
Tempo / Jaeger
     ↓
Grafana
```

Distributed tracing becomes especially powerful when combined with:

```text
Metrics
+
Logs
+
Traces
```

A strong incident investigation workflow is:

```text
Alert
 ↓
Metric
 ↓
Trace
 ↓
Slow / Failed Span
 ↓
Service
 ↓
Logs
 ↓
Root Cause
```

The most important principle is:

> **Distributed tracing shows the path and timing of individual requests across a distributed system, allowing engineers to identify latency, failures, dependencies, and root causes that are difficult to understand from metrics or logs alone.**

---

## Next Chapter

# Chapter 65 – Cluster Administration

Topics will include:

- Kubernetes Cluster Administration
- Cluster Architecture
- Control Plane
- Worker Nodes
- API Server
- etcd
- Scheduler
- Controller Manager
- Cloud Controller Manager
- kubelet
- kube-proxy
- Container Runtime
- Cluster Configuration
- kubeconfig
- kubectl
- Contexts
- Namespaces
- Nodes
- Node Labels
- Node Conditions
- Node Capacity
- Node Allocatable Resources
- Node Management
- Node Registration
- Node Draining
- Node Cordon
- Node Uncordon
- Pod Eviction
- Cluster Networking
- CNI
- Cluster DNS
- CoreDNS
- Services
- Ingress
- Gateway API
- Storage
- CSI
- Persistent Volumes
- Persistent Volume Claims
- RBAC
- Service Accounts
- Authentication
- Authorization
- Admission
- Secrets
- ConfigMaps
- Resource Quotas
- Limit Ranges
- Scheduling
- Taints
- Tolerations
- Affinity
- Node Selectors
- Pod Disruption Budgets
- Cluster Monitoring
- Cluster Logging
- Events
- Metrics
- Audit Logs
- Control Plane Monitoring
- etcd Management
- Certificate Management
- Kubernetes PKI
- Cluster Health
- API Server Health
- Scheduler Health
- Controller Manager Health
- Node Health
- Resource Utilization
- Capacity Planning
- Cluster Scaling
- Cluster Autoscaler
- Manual Scaling
- Cluster Upgrades
- Backup
- Restore
- Security Administration
- Network Policies
- Pod Security
- Image Security
- Runtime Security
- High Availability
- Troubleshooting
- Production Operations
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---