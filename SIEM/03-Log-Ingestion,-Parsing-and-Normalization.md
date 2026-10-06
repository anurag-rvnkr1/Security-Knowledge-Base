# Chapter 03 – Log Ingestion, Parsing & Normalization

> Raw security telemetry is rarely ready for analysis. A SIEM must reliably receive data, parse its structure, normalize fields, enrich context, and make the resulting events searchable and usable for detection engineering.

---

# 1. Introduction

In the previous chapter, we learned:

```text
Where SIEM data comes from
        ↓
Endpoints
Networks
Identity
Applications
Cloud
Security Tools
```

This chapter focuses on what happens **after the data leaves the source**.

```text
LOG SOURCE
    ↓
COLLECTION
    ↓
TRANSPORT
    ↓
INGESTION
    ↓
PARSING
    ↓
NORMALIZATION
    ↓
ENRICHMENT
    ↓
VALIDATION
    ↓
INDEX / STORAGE
    ↓
SEARCH / DETECTION
```

The goal is to transform:

```text
Raw Data
```

into:

```text
Reliable, structured, searchable security events
```

---

# 2. What is Log Ingestion?

**Log ingestion** is the process of receiving telemetry into a SIEM or security data platform.

Conceptually:

```text
Source
  ↓
Collector
  ↓
Transport
  ↓
Ingestion Pipeline
  ↓
SIEM
```

Ingestion may involve:

```text
Receiving
Buffering
Decoding
Filtering
Routing
Parsing
Transforming
Enriching
Indexing
```

---

# 3. Collection vs Ingestion

These terms are related but different.

### Collection

Getting data from the source.

```text
Firewall
   ↓
Collector
```

### Ingestion

Receiving and processing that data into the SIEM pipeline.

```text
Collector
   ↓
Ingestion Pipeline
```

Simplified:

```text
COLLECTION
"Get the data."

INGESTION
"Bring the data into the processing platform."
```

---

# 4. Complete Ingestion Pipeline

A typical architecture:

```text
                    LOG SOURCE
                         │
                         ▼
                    COLLECTION
                         │
                         ▼
                     FORWARDER
                         │
                         ▼
                      NETWORK
                         │
                         ▼
                     RECEIVER
                         │
                         ▼
                     BUFFERING
                         │
                         ▼
                       PARSER
                         │
                         ▼
                    NORMALIZER
                         │
                         ▼
                    ENRICHMENT
                         │
                         ▼
                     VALIDATION
                         │
                         ▼
                    INDEX / STORE
```

---

# 5. Why Ingestion Matters

Poor ingestion can cause:

```text
Dropped Events
Delayed Events
Malformed Events
Duplicate Events
Incorrect Timestamps
Missing Fields
Parsing Errors
Detection Failures
```

Therefore:

> **A detection is only as reliable as the data pipeline supporting it.**

---

# 6. Ingestion Architecture

Large environments may separate ingestion into multiple stages.

```text
Sources
   │
   ▼
Collectors
   │
   ▼
Load Balancer
   │
   ▼
Ingestion Nodes
   │
   ▼
Message Queue
   │
   ▼
Processing
   │
   ▼
Storage
```

This provides scalability and resilience.

---

# 7. Collectors

A collector receives logs from one or more sources.

Examples:

```text
Syslog Collector
Windows Collector
Cloud Collector
API Collector
Agent Gateway
```

Architecture:

```text
Firewall ─────┐
Router ───────┤
VPN ──────────┤
              ▼
          Collector
              │
              ▼
             SIEM
```

---

# 8. Forwarders

A forwarder transfers logs from one location to another.

```text
Endpoint
   ↓
Forwarder
   ↓
Collector
   ↓
SIEM
```

A forwarder may perform:

```text
Filtering
Compression
Buffering
Encryption
Routing
Load Distribution
```

---

# 9. Ingestion Endpoints

A SIEM may expose different ingestion interfaces.

Examples:

```text
Syslog Listener
HTTP API
HTTPS API
TCP Listener
Message Queue
Cloud Connector
Agent Endpoint
File Collector
```

The correct method depends on the data source.

---

# 10. Syslog Ingestion

A common architecture:

```text
Firewall
   │
   │ Syslog
   ▼
Collector
   │
   ▼
Parser
   │
   ▼
SIEM
```

Transport may use:

```text
UDP
TCP
TLS
```

Where reliability and confidentiality are important, secure transport should be used when supported.

---

# 11. UDP vs TCP for Logs

## UDP

Advantages:

```text
Low Overhead
Simple
Fast
```

Disadvantages:

```text
No Delivery Guarantee
Potential Packet Loss
No Connection State
```

## TCP

Advantages:

```text
Reliable Transport
Ordered Delivery
Connection-Oriented
```

Disadvantages:

```text
More Overhead
Connection Management
```

---

# 12. TLS-Protected Logging

When logs contain sensitive information:

```text
Source
   ↓
TLS
   ↓
Collector
   ↓
SIEM
```

Benefits include:

```text
Confidentiality
Integrity Protection in Transit
Server Authentication
```

Exact security properties depend on certificate configuration and deployment.

---

# 13. API-Based Ingestion

Cloud and SaaS platforms commonly provide APIs.

```text
Cloud Service
      │
      ▼
     API
      │
      ▼
Collector
      │
      ▼
Processing
      │
      ▼
SIEM
```

API ingestion may require:

```text
Authentication
Authorization
Pagination
Rate-Limit Handling
Retry Logic
Checkpointing
```

---

# 14. Polling vs Streaming

## Polling

The collector periodically asks:

```text
"Give me new events."
```

Example:

```text
Every 60 seconds
 ↓
API request
 ↓
Retrieve events
```

## Streaming

The source continuously sends events.

```text
Event
 ↓
Immediately forwarded
 ↓
Collector
```

Streaming can provide lower latency.

---

# 15. Ingestion Latency

There may be a delay between:

```text
Event Occurs
```

and:

```text
Event Available in SIEM
```

Example:

```text
10:00:00
Event occurs

10:00:03
Collector receives it

10:00:04
Parser processes it

10:00:05
Event indexed
```

Ingestion latency:

```text
≈ 5 seconds
```

---

# 16. Why Ingestion Latency Matters

High latency can affect:

```text
Real-Time Detection
Incident Response
Automated Response
Threat Hunting
Correlation
```

Example:

```text
Attack occurs
 ↓
30-minute ingestion delay
 ↓
Detection delayed
```

This can significantly increase attacker dwell time.

---

# 17. Event Ordering

Events do not always arrive in the same order they occurred.

Example:

```text
Event A occurred at 10:00:01
Event B occurred at 10:00:02

But SIEM receives:

Event B
Event A
```

Possible causes:

```text
Network Delay
Multiple Collectors
Buffering
Processing Delay
Clock Differences
```

Detection systems should account for such conditions where necessary.

---

# 18. Event Time vs Ingestion Time

An event can contain multiple timestamps.

```text
event_time
ingest_time
process_time
index_time
```

Example:

```text
Event Time:
10:00:00

Ingest Time:
10:00:05

Index Time:
10:00:06
```

For security investigation, the original event time is usually essential.

---

# 19. Timestamp Normalization

Different sources may produce:

```text
2026-08-13 10:00:00
13/08/2026 10:00:00
Aug 13 10:00:00
2026-08-13T10:00:00Z
```

The SIEM should normalize these into a consistent representation.

Example:

```text
2026-08-13T10:00:00Z
```

---

# 20. Time Zones

A global organization may have:

```text
India
USA
Europe
Singapore
Australia
```

Logs may use:

```text
UTC
Local Time
Server Time
Application Time
```

A SIEM should maintain clear timezone semantics.

Best practice is often to store timestamps in a standardized form such as UTC while preserving relevant original timestamp information when needed.

---

# 21. Parsing

Parsing converts raw data into structured fields.

Raw:

```text
Failed password for alice from 10.10.10.20 port 55221
```

Parsed:

```text
event.action = authentication
event.outcome = failure
user.name = alice
source.ip = 10.10.10.20
source.port = 55221
```

---

# 22. Why Parsing Matters

Without parsing:

```text
Search:
"failed login"
```

With parsing:

```text
event.action = login
event.outcome = failure
user.name = alice
source.ip = 10.10.10.20
```

Structured fields enable:

```text
Search
Correlation
Aggregation
Detection
Dashboards
Automation
```

---

# 23. Parsing Methods

Common parsing approaches:

```text
Delimiter Parsing
Regular Expressions
Key-Value Parsing
JSON Parsing
XML Parsing
CSV Parsing
Pattern Matching
Schema-Based Parsing
Vendor Parsers
```

---

# 24. Delimiter Parsing

Example:

```text
alice,10.10.10.20,login,failed
```

Fields:

```text
user = alice
source_ip = 10.10.10.20
action = login
status = failed
```

---

# 25. Key-Value Parsing

Example:

```text
user=alice src_ip=10.10.10.20 action=login status=failed
```

Extract:

```text
user
src_ip
action
status
```

This is often easier to parse than free-form text.

---

# 26. JSON Parsing

Example:

```json
{
  "user": "alice",
  "source_ip": "10.10.10.20",
  "action": "login",
  "outcome": "failure"
}
```

The parser can directly map:

```text
user
source_ip
action
outcome
```

into structured fields.

---

# 27. XML Parsing

Some enterprise systems use XML.

Example:

```xml
<Event>
    <User>alice</User>
    <Action>login</Action>
    <Status>failure</Status>
</Event>
```

The SIEM extracts:

```text
user = alice
action = login
status = failure
```

---

# 28. Regular Expressions

Regular expressions can extract fields from unstructured logs.

Example:

```text
Failed password for alice from 10.10.10.20
```

Conceptually:

```text
username → alice
source_ip → 10.10.10.20
```

Regex is powerful but can become difficult to maintain if used excessively.

---

# 29. Vendor Parsers

SIEM platforms often provide parsers for common vendors.

Examples:

```text
Firewall Parser
Windows Parser
Linux Parser
Cloud Parser
EDR Parser
Web Server Parser
```

Advantages:

```text
Faster Onboarding
Standardized Fields
Reduced Development
```

But parsers still need testing and validation.

---

# 30. Parsing Failure

Suppose the parser expects:

```text
src_ip=10.10.10.20
```

but the vendor changes the format:

```text
source=10.10.10.20
```

The parser may fail.

Result:

```text
Missing source.ip
```

Potential impact:

```text
Detection Failure
Search Failure
Correlation Failure
```

---

# 31. Parser Validation

After onboarding a source:

```text
Raw Event
   ↓
Parser
   ↓
Expected Fields
```

Validate:

```text
Timestamp
Source IP
Destination IP
User
Action
Outcome
Host
Severity
```

---

# 32. Parsing Success Rate

A useful operational metric:

```text
Total Events:
100,000

Successfully Parsed:
99,000

Parsing Success:
99%
```

A sudden drop may indicate:

```text
Format Change
Parser Failure
Malformed Events
Vendor Upgrade
Configuration Problem
```

---

# 33. Normalization

Normalization creates a common representation across different sources.

Example:

```text
Windows:
IpAddress

Firewall:
src

Linux:
rhost

Application:
client_ip
```

Normalize:

```text
source.ip
```

---

# 34. Why Normalization Matters

Without normalization:

```text
Detection A:
src

Detection B:
source_ip

Detection C:
client_ip

Detection D:
IpAddress
```

This creates complexity.

With normalization:

```text
source.ip
```

Detections can use a common field.

---

# 35. Common Normalized Fields

Examples:

```text
@timestamp

event.kind
event.category
event.type
event.action
event.outcome
event.severity

user.name
user.id

source.ip
source.port

destination.ip
destination.port

host.name
host.id

process.name
process.pid
process.command_line

file.name
file.hash

url.domain
url.full

network.protocol
```

Exact schemas vary by platform.

---

# 36. ECS

**Elastic Common Schema (ECS)** is one example of a standardized field schema used in security data pipelines.

It defines common fields for entities such as:

```text
Host
User
Network
Process
File
URL
Event
Source
Destination
```

Other SIEM ecosystems use different schemas.

The underlying principle is:

> **Common fields make cross-source analytics easier.**

---

# 37. Schema-on-Write vs Schema-on-Read

## Schema-on-Write

Data is transformed into a defined structure before or during ingestion.

```text
Raw
 ↓
Transform
 ↓
Normalized
 ↓
Store
```

Advantages:

```text
Consistent Data
Fast Search
Predictable Fields
```

Potential disadvantage:

```text
Transformation Complexity
```

---

## Schema-on-Read

Raw data is stored and interpreted when queried.

```text
Raw Data
 ↓
Store
 ↓
Interpret During Search
```

Advantages:

```text
Flexible
Preserves Original Data
```

Potential disadvantage:

```text
More Query-Time Processing
```

Modern systems may use combinations of these approaches.

---

# 38. Data Transformation

During ingestion, fields may be:

```text
Renamed
Converted
Extracted
Normalized
Dropped
Enriched
Calculated
```

Example:

```text
src=10.10.10.20
```

becomes:

```text
source.ip=10.10.10.20
```

---

# 39. Data Type Normalization

Fields should have consistent data types.

Bad:

```text
port = "443"
```

Elsewhere:

```text
port = 443
```

A normalized schema should consistently represent the field as an appropriate numeric type.

This improves:

```text
Sorting
Aggregation
Comparison
Querying
```

---

# 40. IP Address Normalization

Different representations may exist:

```text
10.0.0.1
10.000.000.001
IPv6
IPv4-mapped IPv6
```

The ingestion pipeline should handle supported formats consistently.

---

# 41. User Identity Normalization

The same user may appear as:

```text
alice
ALICE
alice@example.com
CORP\alice
alice@corp.local
```

These may represent the same identity.

Normalization can help map them to a canonical identity.

---

# 42. Hostname Normalization

The same host may appear as:

```text
WEB01
web01
web01.company.local
10.10.10.10
```

Asset enrichment can map these identifiers to a canonical asset.

---

# 43. Identity Resolution

Identity resolution attempts to connect different identifiers.

Example:

```text
alice
alice@company.com
CORP\alice
```

↓

```text
User ID:
12345
```

This is extremely useful for investigation.

---

# 44. Asset Resolution

Example:

```text
10.10.10.25
```

Enrichment:

```text
Hostname: DC01
Role: Domain Controller
Criticality: Critical
Owner: Identity Team
```

---

# 45. Enrichment

Enrichment adds information not directly present in the original event.

Common enrichment sources:

```text
Threat Intelligence
GeoIP
Asset Inventory
Identity Directory
Vulnerability Scanner
CMDB
DNS
WHOIS
User Metadata
Cloud Metadata
```

---

# 46. GeoIP Enrichment

Example:

```text
source.ip = 203.0.113.10
```

Enriched:

```text
country = Example
region = Example
ASN = Example
```

GeoIP is contextual and may be inaccurate, so it should not be treated as definitive identity/location evidence.

---

# 47. Threat Intelligence Enrichment

Example:

```text
source.ip = X
```

Lookup:

```text
Known Malicious
Confidence = High
Category = C2
```

The SIEM can add:

```text
threat.indicator
threat.category
threat.confidence
```

---

# 48. Asset Enrichment

Example:

```text
destination.ip = 10.10.10.10
```

CMDB lookup:

```text
host = DB01
role = Database
criticality = Critical
```

This can increase alert priority.

---

# 49. User Enrichment

Example:

```text
user.name = alice
```

Directory lookup:

```text
Department = Finance
Role = Administrator
Manager = ...
Privilege = High
```

Again, only appropriate and authorized contextual data should be included.

---

# 50. Vulnerability Enrichment

Example:

```text
Connection
 ↓
Server
 ↓
Known Critical Vulnerability
```

This provides additional risk context.

---

# 51. Deduplication

The same event may arrive multiple times.

Example:

```text
Event A
Event A
Event A
```

Possible causes:

```text
Multiple Collectors
Retries
Forwarding
Source Duplication
Configuration Error
```

Deduplication prevents inflated counts and unnecessary alerts.

---

# 52. Event Fingerprinting

A system can create an event fingerprint from fields such as:

```text
Timestamp
Host
User
Action
Source IP
Destination
Event ID
```

Similar fingerprints can help identify duplicates.

---

# 53. Event Ordering

Consider:

```text
Event A: 10:00:01
Event B: 10:00:02
Event C: 10:00:03
```

But arrival order:

```text
B
A
C
```

Correlation engines may need:

```text
Time Windows
Event-Time Processing
Watermarks
Late Event Handling
```

---

# 54. Late-Arriving Events

An event may arrive after the correlation window.

Example:

```text
Attack event:
10:00:00

Detection event arrives:
10:06:00
```

If the rule only looks at:

```text
Last 5 minutes
```

the event may be missed.

This is an important engineering consideration.

---

# 55. Buffering

Buffers temporarily hold data.

```text
Source
 ↓
Collector
 ↓
Buffer
 ↓
Processor
 ↓
SIEM
```

Benefits:

```text
Handles Bursts
Improves Resilience
Absorbs Temporary Outages
```

---

# 56. Backpressure

If downstream processing cannot keep up:

```text
Incoming:
100,000 events/sec

Processing:
60,000 events/sec
```

Backlog grows.

This is a form of:

```text
Backpressure
```

Possible responses:

```text
Scale Consumers
Increase Buffer
Throttle Sources
Filter Low-Value Data
Optimize Processing
```

---

# 57. Throughput

SIEM pipelines must handle large event volumes.

Measured using:

```text
Events Per Second (EPS)
Bytes Per Second
Events Per Minute
```

Example:

```text
100,000 EPS
```

means:

```text
100,000 events every second
```

---

# 58. Data Volume

Suppose:

```text
50,000 EPS
```

Average event size:

```text
1 KB
```

Approximate raw data rate:

```text
50,000 KB/sec
≈ 50 MB/sec
```

Daily:

```text
≈ 4.32 TB/day
```

This is a simplified estimate before compression, metadata, indexing overhead, and retention strategy.

---

# 59. Ingestion Scaling

A large environment may use:

```text
Load Balancer
     │
 ┌───┼────┐
 ▼   ▼    ▼
Node1 Node2 Node3
 │     │    │
 └─────┼────┘
       ▼
    Processing
```

This improves scalability and availability.

---

# 60. Horizontal Scaling

Instead of making one server larger:

```text
One Large Server
```

add multiple nodes:

```text
Node 1
Node 2
Node 3
Node 4
```

This is:

```text
Horizontal Scaling
```

---

# 61. Vertical Scaling

Increase resources of a node:

```text
More CPU
More RAM
Faster Storage
```

This is:

```text
Vertical Scaling
```

Large SIEM platforms often combine both approaches.

---

# 62. Load Balancing

Incoming telemetry can be distributed:

```text
Sources
   │
   ▼
Load Balancer
   │
 ┌─┼──────┐
 ▼ ▼      ▼
N1 N2     N3
```

Benefits:

```text
Scalability
Availability
Balanced Processing
```

---

# 63. Queue-Based Architecture

A queue can decouple ingestion from processing.

```text
Sources
   ↓
Collectors
   ↓
Message Queue
   ↓
Consumers
   ↓
Processors
   ↓
Storage
```

Benefits:

```text
Buffering
Retry
Scalability
Fault Isolation
```

---

# 64. Ingestion Failure Modes

Common failures:

```text
Source Failure
Network Failure
Collector Failure
Parser Failure
Queue Overflow
Storage Failure
Authentication Failure
Certificate Expiration
API Rate Limit
Schema Change
```

Each should be monitored.

---

# 65. API Rate Limits

SaaS/cloud APIs may limit requests.

Example:

```text
API allows:
1,000 requests/hour
```

Collector exceeds limit:

```text
Requests rejected
```

Potential result:

```text
Missing Telemetry
```

Solutions include:

```text
Backoff
Retry
Pagination
Checkpointing
Rate Control
Multiple Authorized Consumers
```

---

# 66. Checkpointing

A collector can remember:

```text
Last Event ID
Last Timestamp
Last Sequence Number
```

If it restarts:

```text
Resume from checkpoint
```

This reduces event loss or duplication.

---

# 67. Retry Logic

Temporary failure:

```text
SIEM unavailable
```

Collector:

```text
Retry
 ↓
Retry
 ↓
Retry
```

Proper retry strategies should use controlled backoff rather than creating additional overload.

---

# 68. Dead-Letter Queue

Events that cannot be processed may be sent to a separate location:

```text
Invalid Event
     ↓
Processing Failure
     ↓
Dead-Letter Queue
```

This prevents malformed events from blocking the entire pipeline.

---

# 69. Schema Evolution

Vendors may change event formats.

Version 1:

```text
src_ip
```

Version 2:

```text
sourceAddress
```

Version 3:

```text
source.ip
```

Ingestion pipelines must handle schema evolution safely.

---

# 70. Parser Versioning

Parsers should ideally be version-controlled.

```text
Parser v1
Parser v2
Parser v3
```

When a vendor changes its log format:

```text
Test New Parser
       ↓
Validate
       ↓
Deploy
```

---

# 71. Testing Ingestion

Before production:

```text
Generate Test Event
       ↓
Send to Collector
       ↓
Verify Ingestion
       ↓
Verify Parsing
       ↓
Verify Normalization
       ↓
Verify Search
       ↓
Verify Detection
```

---

# 72. Data Validation

Validate:

```text
Timestamp
Source
Destination
User
Host
Event Type
Outcome
Severity
Unique ID
```

Check for:

```text
Nulls
Invalid Values
Wrong Types
Unexpected Formats
```

---

# 73. Required vs Optional Fields

Not every event needs every field.

Example:

Authentication event:

```text
Required:
user
timestamp
outcome

Optional:
device
geo
application
```

A detection should clearly define which fields it actually requires.

---

# 74. Null Handling

Example:

```text
source.ip = null
```

Possible reasons:

```text
Local Event
Parser Failure
Missing Source Data
```

A detection should not blindly assume every field is populated.

---

# 75. Data Quality Pipeline

```text
RAW EVENT
    ↓
Parsing Check
    ↓
Schema Check
    ↓
Field Validation
    ↓
Timestamp Check
    ↓
Duplicate Check
    ↓
Enrichment
    ↓
Quality Score
    ↓
STORE
```

---

# 76. Quality Scoring

A platform can conceptually assign:

```text
Parsing Quality = 100%
Field Completeness = 95%
Timestamp Accuracy = 100%
Enrichment = 90%
```

This helps identify problematic sources.

---

# 77. Filtering

Filtering removes events that are not needed.

Example:

```text
Debug Event
Debug Event
Debug Event
```

If they have no security value:

```text
Filter
```

But filtering should be based on:

```text
Detection Requirements
Compliance
Investigation Needs
Business Requirements
```

---

# 78. Sampling

In very high-volume environments, some telemetry may be sampled.

Example:

```text
100 million network flows
       ↓
Sample subset
```

Sampling reduces cost but may reduce visibility.

Therefore, sampling is generally unsuitable for telemetry where every event may be security-critical.

---

# 79. Compression

Logs can be compressed:

```text
Raw Data
   ↓
Compression
   ↓
Lower Storage / Transfer Cost
```

Trade-off:

```text
CPU Usage
Processing Complexity
```

---

# 80. Data Routing

Different events may go to different destinations.

Example:

```text
Security Events
      ↓
SIEM

Debug Logs
      ↓
Application Log Platform

Long-Term Archive
      ↓
Object Storage
```

Routing can reduce unnecessary SIEM cost.

---

# 81. Hot vs Cold Routing

Example:

```text
Critical Security Events
       ↓
Hot Storage

Older Events
       ↓
Warm Storage

Archive
       ↓
Cold Storage
```

---

# 82. Ingestion Security

Protect ingestion endpoints with:

```text
TLS
Authentication
Authorization
Network Segmentation
IP Restrictions
Rate Limiting
Certificate Management
Monitoring
```

---

# 83. Certificate Management

TLS-based ingestion may fail if:

```text
Certificate Expired
Certificate Revoked
Wrong Hostname
Trust Chain Broken
```

Therefore:

```text
Certificate Expiration Monitoring
```

is important.

---

# 84. Authentication for Collectors

Collectors may use:

```text
API Keys
Certificates
Service Accounts
OAuth
Mutual TLS
Cloud IAM
```

Credentials should be:

```text
Least Privilege
Rotated
Protected
Monitored
```

---

# 85. Secrets in Logs

Logs themselves may accidentally contain:

```text
Passwords
API Keys
Tokens
Session IDs
Personal Data
Authorization Headers
```

Sensitive secrets should not be logged unnecessarily.

Where possible:

```text
Redact
Mask
Hash
Tokenize
```

before storage.

---

# 86. Data Privacy

SIEM data may contain:

```text
Personal Information
Authentication Information
User Activity
Network Information
Business Data
```

Organizations should consider:

```text
Data Minimization
Access Control
Retention
Encryption
Privacy Requirements
Legal Requirements
```

---

# 87. Original Event Preservation

When possible, preserve sufficient original context for investigation.

Architecture:

```text
Raw Event
   ↓
Parsed Event
   ↓
Normalized Event
```

The normalized representation is convenient, while the original event can help debug parsing or investigate unusual activity.

Retention policies determine how long original data can be retained.

---

# 88. Parsing vs Normalization

These are frequently confused.

### Parsing

Extract information:

```text
Raw
 ↓
user=alice
ip=10.10.10.20
```

### Normalization

Map to standard fields:

```text
user.name=alice
source.ip=10.10.10.20
```

So:

```text
PARSING
"What does the log contain?"

NORMALIZATION
"How should we represent it consistently?"
```

---

# 89. Normalization vs Enrichment

### Normalization

Makes data consistent.

```text
src_ip
 ↓
source.ip
```

### Enrichment

Adds new information.

```text
source.ip
 ↓
GeoIP
 ↓
Country
ASN
Threat Reputation
```

---

# 90. Complete Transformation

```text
RAW
"Failed password for alice from 10.10.10.20"

       ↓ PARSE

user = alice
source_ip = 10.10.10.20
status = failed

       ↓ NORMALIZE

user.name = alice
source.ip = 10.10.10.20
event.outcome = failure

       ↓ ENRICH

asset = WEB01
geo = ...
reputation = ...

       ↓ STORE

Structured Security Event
```

---

# 91. Example: Windows Event

Raw:

```text
EventID=4625
AccountName=alice
IpAddress=10.10.10.20
```

Parsed:

```text
event.id = 4625
user = alice
source_ip = 10.10.10.20
```

Normalized:

```text
event.code = 4625
user.name = alice
source.ip = 10.10.10.20
event.outcome = failure
```

Enriched:

```text
user.role = Finance
host.criticality = High
source.reputation = Unknown
```

---

# 92. Example: Firewall Event

Raw:

```text
ALLOW TCP 10.10.10.20:51522 -> 10.10.20.10:443
```

Parsed:

```text
action = ALLOW
protocol = TCP
src_ip = 10.10.10.20
src_port = 51522
dst_ip = 10.10.20.10
dst_port = 443
```

Normalized:

```text
event.action = network_connection
network.transport = tcp
source.ip = 10.10.10.20
source.port = 51522
destination.ip = 10.10.20.10
destination.port = 443
```

---

# 93. Example: DNS Event

Raw:

```text
client=10.10.10.20 query=example.com type=A
```

Normalized:

```text
source.ip = 10.10.10.20
dns.question.name = example.com
dns.question.type = A
```

Enrichment:

```text
domain.reputation = ...
domain.age = ...
threat.category = ...
```

---

# 94. Data Lineage

Data lineage answers:

```text
Where did this event come from?

Which parser processed it?

Which transformations occurred?

Which enrichment was applied?

Where was it stored?
```

Example:

```text
Firewall
 ↓
Syslog
 ↓
Collector A
 ↓
Parser v3
 ↓
Normalization
 ↓
Threat Intel
 ↓
Index A
```

Data lineage is useful for troubleshooting and auditability.

---

# 95. Observability of the SIEM Pipeline

The SIEM should monitor itself.

Monitor:

```text
Ingestion Rate
Parsing Rate
Error Rate
Queue Depth
Latency
Dropped Events
Storage
CPU
Memory
Network
```

---

# 96. Ingestion Monitoring Dashboard

A useful dashboard might show:

```text
Events/sec
Bytes/sec
Parsing Success %
Dropped Events
Queue Depth
Average Latency
Top Sources
Failed Sources
Storage Usage
```

---

# 97. Example Pipeline Failure

Suppose:

```text
Firewall
 ↓
Collector
 ↓
Parser
 X
```

Parser failure causes:

```text
Missing source.ip
Missing destination.ip
Missing action
```

Consequences:

```text
Firewall Detection
       ↓
Broken
```

This demonstrates why pipeline health is itself a security concern.

---

# 98. Ingestion Best Practices

```text
1. Use reliable transport where appropriate.

2. Encrypt sensitive telemetry in transit.

3. Monitor collector health.

4. Monitor parsing success.

5. Monitor ingestion latency.

6. Monitor event loss.

7. Normalize important fields.

8. Preserve useful original context.

9. Version parsers.

10. Test schema changes.

11. Handle API rate limits.

12. Implement retries carefully.

13. Use buffering for resilience.

14. Monitor queue depth.

15. Protect ingestion credentials.

16. Minimize sensitive data in logs.

17. Avoid excessive filtering.

18. Document transformations.

19. Monitor source health.

20. Test detections after pipeline changes.
```

---

# 99. Practical Lab

Build a small pipeline:

```text
Windows
   │
   ▼
Sysmon
   │
   ▼
Agent
   │
   ▼
SIEM
```

Generate legitimate activity:

```text
Process Creation
DNS Query
Network Connection
File Creation
```

Then inspect:

```text
Raw Event
 ↓
Parsed Fields
 ↓
Normalized Fields
 ↓
Search
```

---

# 100. Parsing Exercise

Start with:

```text
Failed password for alice from 10.10.10.20 port 55221
```

Extract:

```text
user.name
source.ip
source.port
event.outcome
```

Expected:

```text
user.name = alice
source.ip = 10.10.10.20
source.port = 55221
event.outcome = failure
```

---

# 101. Normalization Exercise

Given:

```text
Windows:
IpAddress

Firewall:
src

Linux:
rhost

Application:
client_ip
```

Normalize all to:

```text
source.ip
```

Then build a detection that searches:

```text
source.ip
```

regardless of the original source.

---

# 102. Enrichment Exercise

Given:

```text
source.ip = 203.0.113.10
```

Add:

```text
GeoIP
ASN
Threat Reputation
Known Organization
```

Then determine how the additional context changes investigation priority.

---

# 103. Ingestion Failure Exercise

Simulate:

```text
Collector stops
```

Observe:

```text
Event volume drops
 ↓
Detection visibility decreases
```

Then restore the collector and verify:

```text
Events resume
Parsing works
Normalization works
Detections work
```

---

# 104. Interview Questions

### What is log ingestion?

> The process of receiving telemetry into a SIEM or security data platform for processing and analysis.

### What is the difference between collection and ingestion?

> Collection obtains telemetry from the source, while ingestion brings that telemetry into the processing pipeline.

### What is parsing?

> Extracting structured fields from raw log data.

### What is normalization?

> Converting source-specific fields and formats into a consistent schema.

### What is enrichment?

> Adding contextual information such as asset, identity, geographic, vulnerability, or threat intelligence data.

### Why is normalization important?

> It allows detections and searches to use consistent fields across different log sources.

### What is ingestion latency?

> The time between an event occurring and becoming available for processing or search in the SIEM.

### What is log loss?

> Events generated by a source but not successfully delivered or retained by the SIEM pipeline.

### What causes parsing failures?

> Format changes, malformed logs, incorrect parser logic, schema changes, and configuration errors.

### What is buffering?

> Temporarily storing events during transport or processing to absorb bursts or temporary downstream failures.

### What is backpressure?

> A condition where incoming data arrives faster than downstream systems can process it.

### What is deduplication?

> Identifying and removing or suppressing duplicate copies of the same event.

### Why is time synchronization important?

> It allows accurate event correlation and incident timeline reconstruction.

### What is schema evolution?

> Changes to the structure or fields of telemetry over time.

### Why should parsers be versioned?

> To safely manage format changes and allow controlled testing and rollback.

---

# 105. Quick Revision

```text
COLLECTION
→ Get data from source

INGESTION
→ Bring data into processing pipeline

TRANSPORT
→ Move data

BUFFER
→ Temporarily hold data

PARSER
→ Extract fields

NORMALIZER
→ Standardize fields

ENRICHMENT
→ Add context

VALIDATION
→ Check data quality

DEDUPLICATION
→ Remove duplicate events

ROUTING
→ Send data to appropriate destination

INDEXING
→ Make data efficiently searchable

LATENCY
→ Delay between event and availability

THROUGHPUT
→ Amount of data processed per unit time

BACKPRESSURE
→ Incoming data exceeds processing capacity

SCHEMA
→ Structure describing event fields
```

---

# 106. Golden Rules

```text
1. Raw logs are not automatically analysis-ready.

2. Collection and ingestion are different stages.

3. Parsing extracts meaning from raw data.

4. Normalization creates consistency.

5. Enrichment adds context.

6. Incorrect timestamps can break investigations.

7. Duplicate events can distort detections.

8. Late events can affect correlation.

9. High ingestion latency delays detection.

10. Log loss creates security blind spots.

11. Parsing failures can silently break detections.

12. Schema changes must be tested.

13. API rate limits must be handled.

14. Buffers improve resilience.

15. Queues can decouple ingestion from processing.

16. Ingestion infrastructure must be monitored.

17. Protect collectors and ingestion credentials.

18. Do not blindly filter security telemetry.

19. Preserve enough original context for investigation.

20. Always validate telemetry after pipeline changes.
```

---

# 107. Chapter Summary

The key transformation is:

```text
RAW DATA
   ↓
COLLECTION
   ↓
TRANSPORT
   ↓
INGESTION
   ↓
PARSING
   ↓
NORMALIZATION
   ↓
ENRICHMENT
   ↓
VALIDATION
   ↓
INDEX / STORAGE
   ↓
SEARCH
   ↓
DETECTION
```

The most important distinctions are:

```text
Parsing
"What information is inside this log?"

Normalization
"How do we represent that information consistently?"

Enrichment
"What additional context can we add?"

Validation
"Can we trust the resulting event?"
```

A reliable SIEM therefore requires more than simply forwarding logs.

It requires a well-engineered pipeline:

```text
              RAW TELEMETRY
                    │
                    ▼
               COLLECTION
                    │
                    ▼
                INGESTION
                    │
                    ▼
                  PARSE
                    │
                    ▼
               NORMALIZE
                    │
                    ▼
                ENRICH
                    │
                    ▼
                VALIDATE
                    │
                    ▼
             INDEX / STORE
                    │
                    ▼
             SEARCH / DETECT
```

The next chapter moves from the data pipeline into the **architecture of the SIEM itself**:

```text
Chapter 04
    ↓
SIEM Architecture, Components & Data Pipeline
```

There we will examine how collectors, ingestion layers, processing engines, storage, indexing, search, correlation, detection, dashboards, APIs, and case-management components fit together into a production SIEM architecture.